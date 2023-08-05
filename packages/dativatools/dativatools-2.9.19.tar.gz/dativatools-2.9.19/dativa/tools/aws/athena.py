# (c) 2012-2018 Dativa, all rights reserved
# -----------------------------------------
#  This code is licensed under MIT license (see license.txt for details)
import boto3
import logging
import time
import pandas as pd
import os

logger = logging.getLogger("dativa.tools.aws")


class Object(object):
    pass


class AthenaClientError(Exception):
    """
    A generic class for reporting errors in the athena client
    """

    def __init__(self, reason):
        Exception.__init__(self, 'Athena Client failed: reason {}'.format(reason))
        self.reason = reason


class AthenaClient():
    """
    A client for AWS Athena that will create tables from S3 buckets (using AWS Glue)
    and run queries against these tables.
    """

    def __init__(self, region, db, max_queries=3, max_retries=3):
        """
        Create an AthenaClient

        ## Parameters

        region - the AWS region to create the object, e.g. us-east-2
        db - the Glue database to use
        max_queries - the maximum number of queries to run at any one time, defaults to three
        max_retries - the maximum number of times execution of the query will be retried on failure

        """
        self.athena = boto3.client(service_name='athena', region_name=region)
        self.glue = boto3.client(service_name='glue', region_name=region,
                                 endpoint_url='https://glue.{0}.amazonaws.com'.format(region))
        self.db_name = db
        self.max_queries = max_queries
        self.queue = []
        self.aws_region = region
        self.max_retries = max_retries

    @property
    def is_active(self):
        """
        Returns True if there are active or pending queries in the queue.
        Processes the queue before returning a result
        """
        self._process_queue()
        return self.number_active + self.number_pending > 0

    @property
    def number_active(self):
        """
        Returns the number of active queries being processed by Athena
        """
        i = 0
        for query in self.queue:
            if query.is_active:
                i = i + 1
        return i

    @property
    def number_pending(self):
        """
        Returns the number of pending queries that have not yet been
        sent to Athena
        """
        i = 0
        for query in self.queue:
            if query.is_pending:
                i = i + 1
        return i

    def _get_query_status(self, query):
        """
        Gets the status of the query, and updates its status in the queue.
        Any queries that fail are reset to pending so they will be run a second time
        """

        logger.debug("...checking status of query {0}".format(query.name))

        status = self.athena.get_query_execution(QueryExecutionId=query.id)["QueryExecution"]["Status"]

        if status["State"] == "RUNNING":
            query.is_active = True
        elif status["State"] == "SUCCEEDED":
            query.is_active = False
        else:
            if query.retries < self.max_retries:
                logger.info("Retrying query {0} completed with state {1}".format(query.name, status["State"]))
                if "StateChangeReason" in status:
                    logger.info(status["StateChangeReason"])

                query.is_active = False
                query.is_pending = True
                query.retries += 1
            else:
                logger.info("Query {0} exceeded maximum retry limit: Marking as failed".format(query.name))
                query.is_active = False

        return query

    def _query_athena(self, query):
        """
        Runs a query in Athena
        """

        logger.info("Starting query {0} to {1}".format(query.name, query.output_location))

        query.id = self.athena.start_query_execution(
            QueryString=query.sql,
            QueryExecutionContext={'Database': self.db_name},
            ResultConfiguration={'OutputLocation': query.output_location}
        )["QueryExecutionId"]

        query.is_active = True
        query.is_pending = False
        return query

    def _process_queue(self):
        """
        Checks the status of each active query in the queue and starts
        any news ones that are pending.
        """
        for ix, query in enumerate(self.queue):
            if query.is_active:
                query = self._get_query_status(query)
                self.queue[ix] = query
            elif query.is_pending and self.number_active < self.max_queries:
                    self.queue[ix] = self._query_athena(query)

    def add_query(self, sql, name, output_location):
        """
        Adds a query to Athena. Respects the maximum number of queries specified when the module was created.
        Retries queries when they fail so only use when you are sure your syntax is correct!
        Returns a query object

        ## Parameters

        - sql - the SQL query to run
        - name - the name which will be logged when running this query
        - location - the S3 prefix where you want the results stored

        """
        query = Object()
        query.sql = sql
        query.name = name
        query.output_location = output_location
        query.is_active = False
        query.is_pending = True
        query.id = None
        query.retries = 0

        self.queue.append(query)
        if self.number_active < self.max_queries:
            self._process_queue()
        return query

    def wait_for_completion(self):
        """
        Waits for any pending queries to be completed
        """
        while self.is_active:
            logger.info("{0} of {1} queries remaining to run".format(self.number_pending, len(self.queue)))
            time.sleep(10)

    def _db_exists(self):
        for database in self.glue.get_databases(MaxResults=1000)["DatabaseList"]:
            if database["Name"] == self.db_name:
                return True
        return False

    def create_table(self,
                     crawler_target,
                     table_name,
                     columns=None,
                     schema_change_policy={'UpdateBehavior': 'UPDATE_IN_DATABASE', 'DeleteBehavior': 'DEPRECATE_IN_DATABASE'},
                     aws_role='AWSGlueServiceRoleDefault',
                     serde=None,
                     serde_parameters=[]):
        """
        Creates a table in AWS Glue using a crawler.

        ## Parameters

        - region: the AWS region in which to create the table
        - db_name: the name of the Glue database in which to create the table
        - crawler_target: the definition of where the crawler should crawl

        Optional parameters
        - columns: column definitions, typically required for CSV
        - schema_change_policy: the schema change policy to use
        - aws_role: the role that Glue should use when creating it
        - serde: the SerDe to use when parsing the files on S3
        - serde_parameters: any parameters to pass to the SerDe

        For more information on the crawler target and the schema change policies, go here:
        https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html

        Columns are defined here:
        https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html

        """

        crawler_name = "{1}_{0}_crawler".format(self.db_name, table_name)

        # creare the database if it exists
        if not self._db_exists():
            self.glue.create_database(DatabaseInput={"Name": self.db_name})

        # if the crawler exists then update it:
        have_updated = False
        for crawler in self.glue.get_crawlers(MaxResults=1000)["Crawlers"]:
            if crawler_name == crawler["Name"]:
                logger.info("updating crawler {0}".format(crawler_name))
                self.glue.update_crawler(Name=crawler_name,
                                         Role=aws_role,
                                         Targets=crawler_target,
                                         DatabaseName=self.db_name,
                                         Classifiers=[],
                                         SchemaChangePolicy=schema_change_policy)
                have_updated = True
                break

        # otherwise create it
        if not have_updated:
            logger.info("creating crawler {0} ".format(crawler_name))
            self.glue.create_crawler(Name=crawler_name,
                                     Role=aws_role,
                                     Targets=crawler_target,
                                     DatabaseName=self.db_name,
                                     Classifiers=[],
                                     SchemaChangePolicy=schema_change_policy)
 
        # start the crawler and wait for it to complete:
        logger.info("starting crawler {0}".format(crawler_name))
        self.glue.start_crawler(Name=crawler_name)
        while self.glue.get_crawler(Name=crawler_name)["Crawler"]["State"] != "READY":
            logger.info("... waiting for crawler {0} to finish".format(crawler_name))
            time.sleep(5)

        if columns is not None or serde is not None:
            # get the table and update the column names
            logger.info("updating tables {0}".format(table_name))
            table = self.glue.get_table(DatabaseName=self.db_name, Name=table_name)["Table"]
            
            if columns is not None:
                table["StorageDescriptor"]["Columns"] = columns
            
            if serde is not None:
                table["StorageDescriptor"]["SerdeInfo"]["SerializationLibrary"] = serde

            if "Parameters" in table["StorageDescriptor"]["SerdeInfo"]:
                for key in serde_parameters:
                    table["StorageDescriptor"]["SerdeInfo"]["Parameters"][key] = serde_parameters[key]
            else:
                table["StorageDescriptor"]["SerdeInfo"]["Parameters"] = serde_parameters

            self.glue.update_table(DatabaseName=self.db_name,
                                   TableInput={'Name': table_name,
                                               'StorageDescriptor': table["StorageDescriptor"],
                                               'PartitionKeys': table["PartitionKeys"],
                                               'TableType': table["TableType"],
                                               'Parameters': table["Parameters"]})

            # now check for partitions
            partitions = self.glue.get_partitions(DatabaseName=self.db_name, TableName=table_name)

            for partition in partitions["Partitions"]:
                logger.info("Updating partition {0}".format(partition["Values"]))
                if columns is not None:
                    partition["StorageDescriptor"]["Columns"] = columns

                if serde is not None:
                    partition["StorageDescriptor"]["SerdeInfo"]["SerializationLibrary"] = serde

                if "Parameters" in partition["StorageDescriptor"]["SerdeInfo"]:
                    for key in serde_parameters:
                        partition["StorageDescriptor"]["SerdeInfo"]["Parameters"][key] = serde_parameters[key]
                else:
                    partition["StorageDescriptor"]["SerdeInfo"]["Parameters"] = serde_parameters

                self.glue.update_partition(DatabaseName=self.db_name,
                                           TableName=table_name,
                                           PartitionValueList=partition["Values"],
                                           PartitionInput={'StorageDescriptor': partition["StorageDescriptor"],
                                                           'Values': partition["Values"]})
        # delete the crawler...
        self.glue.delete_crawler(Name=crawler_name)

    def get_query_result(self, query):
        """
        Returns Pandas dataframe containing query result if query has completed
        """
        query = self._get_query_status(query)

        if query.is_active is False and query.is_pending is False:
            filepath = os.path.join(query.output_location, "{}.csv".format(query.id))
            logger.info("Fetching results from {}".format(filepath))
            df = pd.read_csv(filepath)
            return df
        else:
            raise AthenaClientError("Cannot fetch results since query hasn't completed")
