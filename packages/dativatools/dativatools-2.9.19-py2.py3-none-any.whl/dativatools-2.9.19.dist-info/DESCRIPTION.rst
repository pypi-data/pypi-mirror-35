# Dativa Tools

Provides useful libraries for processing large data sets. Developed by the team at [www.dativa.com](https://www.dativa.com) as we find them useful in our projects.

Any questions, please email hello AT dativa.com

## Installation

```
pip install dativatools
```

## Description

The library includes two modules:
* dativatools - which contains the legacy classes
* dativa.tools - which contains the more recent classes.

Over time it is expected that we will migrate all classes over to the dativa.tools module

### dativa.tools.aws.AthenaClient
 An easy to use client for AWS Athena that will create tables from S3 buckets (using AWS Glue) and run queries against these tables. It support full customisation of SerDe and column names on table creation.

 Examples:

#### Creating tables

The library creates a temporary Glue crawler which is deleted after use, and will also create the database if it does not exist.

 ```
ac = AthenaClient(aws_region, db_name)
ac.create_table(table_name='my_first_table',
                crawler_target={'S3Targets': [
                    {'Path': 's3://my-bucket/table-data'}]}
                )

# Create a table with a custom SerDe and column names, typical for CSV files
ac.create_table(table_name='comcast_visio_match',
                crawler_target={'S3Targets': [
                    {'Path': 's3://my-bucket/table-data-2', 'Exclusions': ['**._manifest']}]},
                serde='org.apache.hadoop.hive.serde2.OpenCSVSerde',
                columns=[{'Name': 'id', 'Type': 'string'}, {
                    'Name': 'device_id', 'Type': 'string'}, {'Name': 'subscriber_id', 'Type': 'string'}]
                )
 ```

#### Running queries

```
ac = AthenaClient(aws_region, db_name)
 ac.add_query(sql=query,
                 name="From field {0}".format(test_columns[i]),
                 output_location=s3_bucket + 'test-processed')

    i = i + number_fields + 1

ac.wait_for_completion()
```

#### Fetch results of query

```
ac = AthenaClient(aws_region, db_name)
ac.add_query(sql=query,
                 name="From field {0}".format(test_columns[i]),
                 output_location=s3_bucket + 'test-processed')

ac.wait_for_completion()
ac.get_query_result(query)
```

### dativa.tools.aws.S3Client
 An easy to use client for AWS S3 that copies data to S3.
 Examples:

#### Batch deleting of files on S3

```
# Delete all files in a folder
s3 = S3Client()
s3.delete_files(bucket="bucket_name", prefix="/delete-this-folder/")

# Delete only .csv.metadata files in a folder
s3 = S3Client()
s3.delete_files(bucket="bucket_name", prefix="/delete-this-folder/", suffix=".csv.metadata")

```

#### Copy files from folder in local filesystem to s3 bucket

```
s3 = S3Client()
s3.put_folder(source="/home/user/my_folder", bucket="bucket_name", destination="backup/files")

# Copy all csv files from folder to s3
s3.put_folder(source="/home/user/my_folder", bucket="bucket_name", destination="backup/files", 'file_format="*.csv")
```

### dativa.tools.SQLClient

A SQL client that wraps any PEP249 compliant connection object and provides detailed logging and simple query execution. In provides the following methods:

#### execute_query
Runs a query and ignores any output

Parameters:

- query - the query to run, either a SQL file or a SQL query
- parameters - a dict of parameters to substitute in the query
- replace - a dict or items to be replaced in the SQL text
- first_to_run - the index of the first query in a mult-command query to be executed

#### execute_query_to_df

Runs a query and returns the output of the final statement in a DataFrame.

Parameters:

- query - the query to run, either a SQL file or a SQL query
- parameters - a dict of parameters to substitute in the query
- replace - a dict or items to be replaced in the SQL text


#### def execute_query_to_csv

Runs a query and writes the output of the final statement to a CSV file.

Parameters:

- query - the query to run, either a SQL file or a SQL query
- csvfile - the file name to save the query results to
- parameters - a dict of parameters to substitute in the query
- replace - a dict or items to be replaced in the SQL text

#### Example code

```
# set up the SQL client from environment variables
sql = SqlClient(psycopg2.connect(
    database=os.environ["DB_NAME"],
    user=os.environ["USER"],
    password=os.environ["PASSWORD"],
    host=os.environ["HOST"],
    port=os.environ["PORT"],
    client_encoding="UTF-8",
    connect_timeout=10))

# create the full schedule table
df = sql.execute_query_to_df(query="sql/my_query.sql",
                             parameters={"start_date": "2018-01-01",
                                         "end_date": "2018-02-01"})
```

### dativa.tools.log_to_stdout

A convenience function to redirect a specific logger and its children to stdout

```
log_to_stdout("dativa.tools", logging.DEBUG)
```

### dativa.tools.pandas.CSVHandler

A wrapper for pandas CSV handling to read and write DataFrames with consistent CSV parameters by sniffing the parameters automatically. Includes reading a CSV into a DataFrame, and writing it out to a string. Files can be read/written from/to local file system or AWS S3. 

For S3 access suitable credentials should be available in '~/.aws/credentials' or the AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY environment variables.

#### CSVHandler

- base_path - the base path for any CSV file read, defaults to ""
- detect_parameters - whether the encoding of the CSV file should be automatically detected, defaults to False
- csv_encoding - the encoding of the CSV files, defaults to UTF-8
- csv_delimiter - the delimeter used in the CSV, defaults to ','
- csv_header - the index of the header row, or -1 if there is no header
- csv_skiprows - the number of rows at the beginning of file to skip
- csv_quotechar - the quoting character to use, defaults to "

#### load_df

Opens a CSV file using the specified configuration for the class and raises an exception if the encoding is unparseable. Detects if base_path is an S3 location and loads data from there if required.

Parameters:

- file - File path. Should begin with 's3://' to load from S3 location.
- force_dtype - Force data type for data or columns, defaults to None

Returns:

- dataframe

#### save_df

Writes a formatted string from a dataframe using the specified configuration for the class the file. Detects if base_path is an S3 location and saves data there if required.

Parameters:

- df - Dataframe to save
- file - File path. Should begin with 's3://' to save to an S3 location.

#### df_to_string

Returns a formatted string from a dataframe using the specified configuration for the class.

Parameters:

- df - Dataframe to convert to string

Returns:

- string

#### Example code
```
from dativa.tools.pandas import CSVHandler

# Create the CSV handler
csv = CSVHandler(base_path='s3://my-bucket-name/')

# Load a file
df = csv.load_df('my-file-name.csv')

# Create a string
str = csv.df_to_string(df)

# Save a file
csv.save_df(df, 'another-path/another-file-name.csv')
```

### Support functions for Pandas

* dativa.tools.pandas.is_numeric - a function to check whether a series or string is numeric
* dativa.tools.pandas.string_to_datetime - a function to convert a string, or series of strings to a datetime, with a strptime date format that supports nanoseconds
* dativa.tools.pandas.datetime_to_string - a function to convert a datetime, or a series of datetimes to a string, with a strptime date format that supports nanoseconds
* dativa.tools.pandas.format_string_is_valid - a function to confirm whether a strptime format string returns a date
* dativa.tools.pandas.get_column_name - a function to return the name of a column from a passed column name or index.
* dativa.tools.pandas.get_unique_column_name - a function to return a unique column name when adding new columns to a DataFrame

### dativa.tools.aws import S3Csv2Parquet
 An easy to use module for converting csv files on s3 to praquet using aws glue jobs.
 For S3 access and glue access suitable credentials should be available in '~/.aws/credentials' or the AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY environment variables.

#### S3Csv2Parquet
Parameters:
- region - str,
           AWS region in which glue job is to be run
- template_location - str,
                      S3 bucket Folder in which template scripts are
                      located or need to be copied.
                      format s3://bucketname/folder/file.csv

- glue_role - str,
              Name of the glue role which need to be assigned to the
              Glue Job.
- max_jobs - int, default 5
             Maximum number of jobs the can run concurrently in the queue
- retry_limit - int, default 3
                Maximum number of retries allowed per job on failure

#### convert
Parameters:
- csv_path - str or list of str for multiple files,
             s3 location of the csv file
             format s3://bucketname/folder/file.csv
             Pass a list for multiple files
- output_folder - str, default set to folder where csv files are located 
                  s3 location at which paraquet file should be copied
                  format s3://bucketname/folder
- schema - list of tuples,
           If not specified scema is inferred from the file
           format [(column1, datatype), (column2, datatype)]
           Supported datatypes are boolean, double, float, integer,
           long, null, short, string
- name - str, default 'parquet_csv_convert'
         Name to be assigned to glue job

- allocated_capacity - int, default 2
                       The number of AWS Glue data processing units (DPUs) to allocate to this Job.
                       From 2 to 100 DPUs can be allocated
- delete_csv - boolean, default False
               If set source csv files are deleted post successful completion of job
- separator - character, default ','
              Delimiter character in csv files
- withHeader- int, default 1
              Specifies whether to treat the first line as a header
              Can take values 0 or 1
- compression - str, default None
                If not specified compression is not applied.
                Can take values snappy, gzip, and lzo
- partition_by - list of str, default None
                 List containing columns to partition data by
- mode - str, default append
         Options include:
         overwrite: will remove data from output_folder before writing out
                    converted file.
         append: Will write out to  output_folder without deleting existing
                 data.
         ignore: Silently ignore this operation if data already exists.

####Example
```
# Initial setup
csv2parquet_obj = S3Csv2Parquet(region, "s3://my-bucket/templatefolder")

# Create/update a glue job to convert csv files and execute it
csv2parquet_obj.convert("s3://my-bucket/file_to_be_converted_1.csv")
csv2parquet_obj.convert("s3://my-bucket/file_to_be_converted_2.csv")

# Wait for completion of jobs 
csv2parquet_obj.wait_for_completion()
```
## Parquet_Handler
ParquetHandler class, specify path of parquet file,
and get pandas dataframe for analysis and modification.
* param base_path                       : The base location where the parquet_files are stored.
* type base_path                        : str
* param row_group_size                  : The size of the row groups while writing out the parquet file.
* type row_group_size                   : int
* param use_dictionary                  : Specify whether to use boolean encoding or not
* type use_dictionary                   : bool
* param use_deprecated_int96_timestamps : Write nanosecond resolution timestamps to INT96 Parquet format.
* type use_deprecated_int96_timestamps  : bool
* param coerce_timestamps               : Cast timestamps a particular resolution. Valid values: {None, 'ms', 'us'}
* type coerce_timestamps                : str
* param compression                     : Specify the compression codec.
* type compression                      : str

```
from dativa.tools.pandas import CSVHandler, ParquetHandler

# Read a parquet file
pq_obj = ParquetHandler()
df = pq_obj.load_df('data.parquet')

# save a csv_file to parquet
csv_file_path = os.path.join(self.orig_base_path, 'emails.csv')
csv = CSVHandler(csv_delimiter=",")
df = csv.load_df(csv_file_path)
pq_obj = ParquetHandler()
new_file_path = os.path.join(self.orig_base_path, 'new_data.parquet')
pq_obj.save_df(df,new_file_path)
```


### Legacy classes

#### dativatools.CommonUtility
Supports various common activities including getting detailed descriptions about exceptions, logging activity into a CSV file or database table
 and sending email reports of failures.

#### dativatools.DataValidation
Class containing methods to validate file sizes, dates, counts, names and extensions at a specified location.

#### dativatools.DatabaseManagement
Generic database management operations including data insertion, table deletion, backup, rename, drop and create as well as query execution.

#### dativatools.RsyncLib
Class to perform file transfer using Rsync.

#### dativatools.SFTPLib
Class to perform file transfer using SFTP.

#### dativatools.ArchiveManager
Class to manage archiving and unarchiving of files to and from specific locations.

#### dativatools.TextToCsvConverter
Class containing methods required to convert a text file to CSV and change certain parameters like headers, separators etc.

#### dativatools.S3Lib
Supports connecting to and getting and putting data to and from AWS S3 buckets.


