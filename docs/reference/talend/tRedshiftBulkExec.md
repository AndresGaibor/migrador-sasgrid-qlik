<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftbulkexec · versión 8.0 -->
# tRedshiftBulkExec

Last updated: 9/30/2026

Loads data into Amazon Redshift from Amazon S3, Amazon EMR cluster, Amazon
DynamoDB, or remote hosts.

The tRedshiftOutputBulk and tRedshiftBulkExec components can be used together in a two step process
to load data to Amazon Redshift from a delimited/CSV file on Amazon S3. In the first
step, a delimited/CSV file is generated. In the second step, this file is used in the
INSERT statement used to feed Amazon Redshift. These two steps are fused together in the
tRedshiftOutputBulkExec component. The advantage of
using two separate steps is that the data can be transformed before it is loaded to
Amazon Redshift.

tRedshiftBulkExec loads data into an Amazon Redshift
table from an Amazon DynamoDB table or from data files located in an
Amazon S3 bucket, an Amazon EMR cluster, or a remote host that is
accessed using an SSH connection.

## tRedshiftBulkExec Standard properties

These properties are used to configure
tRedshiftBulkExec running in the Standard Job framework.

The
Standard
tRedshiftBulkExec component belongs to the Cloud and the Databases
families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Driver version | Select the Redshift driver version to be used: Driver v1 or Driver v2.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Host | Type in the IP address or hostname of the database server. |
| Port | Type in the listening port number of the database server. |
| Database | Type in the name of the database. |
| Schema | Type in the name of the schema. |
| Username and Password | Type in the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use String JDBC parameters | Set JDBC properties in a string. If you select this option, enter your JDBC parameter string in the Additional JDBC Parameters field; otherwise, enter JDBC properties and property values in the Additional JDBC Parameters table.  This option is not available if Driver v1 is selected from the Driver version drop-down list.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Additional JDBC Parameters | Specify additional JDBC properties for the connection you are creating. The properties are separated by ampersand & and each property is a key-value pair. For example, *ssl=true & sslfactory=com.amazon.redshift.ssl.NonValidatingFactory*, which means the connection will be created using SSL.  This field is not available if Driver v2 is selected from the Driver version drop-down list and the Use String JDBC parameters option is not selected. |
| Additional JDBC Parameters (table) | Specify JDBC properties in table rows.  To specify a JDBC property, add a row in the table by clicking the plus button on the bottom of this table, enter the property name in the Key column, and then enter the property value in the Value column.  This table is available when Driver v2 is selected from the Driver version drop-down list and the Use String JDBC parameters option is not selected.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Table Name | Specify the name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:   * None: No operation is carried out. * Drop and create   table: The table is removed and created   again. * Create   table: The table does not exist and gets   created. * Create table if   not exists: The table is created if it does not   exist. * Drop table if   exists and create: The table is removed if it   already exists and created again. * Clear   table: The table content is deleted. You have   the possibility to rollback the operation. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Data source type | Select the location of the source data to be loaded.   * S3:   load data from a file in an Amazon S3 bucket. * EMR: load data from an Amazon EMR cluster. * DynamoDB: load data from an existing DynamoDB   table. * Remote   host: load data from one or more remote hosts,   such as Amazon Elastic Compute Cloud (Amazon EC2) instances or   other computers.   For more information, see [Data Sources](http://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-source.html). |
| Use an existing S3 connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  This option is available when S3 is selected from the Data source type drop-down list.  Information noteNote: This component works with static credentials only. That is, it does not inherit credentials from AWS role. The component will generate an error in Job execution if any option other than Static Credentials is selected from the Credential Provider drop-down list of the tS3Connection component that creates the S3 connection. |
| Access Key/S3 Access Key | Specify the Access Key ID that uniquely identifies an AWS account. For how to get your Access Key and Access Secret Key, visit [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html).  Information noteNote:  * This option is not available if Use an existing S3 connection   is selected. * This option appears as S3 Access Key if you select   Remote host from the   Data source type   drop-down list. |
| Secret Key/S3 Secret Key | Specify the Secret Access Key, constituting the security credentials in combination with the Access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  Information noteNote:  * This option is not available if Use an existing S3 connection   is selected. * This option appears as S3 Secret Key if you select   Remote host from the   Data source type   drop-down list. |
| Assume Role | Select this checkbox and specify the values for the following parameters used to create a new assumed role session.   * IAM Role ARNs chains: a series of   chained roles, which may belong to other accounts, that your cluster   can assume to access resources.  You can chain a maximum of 10 roles. * Role ARN: the Amazon Resource Name   (ARN) of the role to assume.   This option is not available if Use an existing S3 connection is selected.  For more information on IAM Role ARNs chains, see [Authorizing Redshift service](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service.html). |
| Bucket/S3 bucket | Specify the name of the Amazon S3 bucket in which the file is located.  This field is available only when S3 or Remote host is selected from the Data source type drop-down list.  Information noteNote: This field appears as Bucket if you select S3 from the Data source type drop-down list; it appears as S3 bucket if you select Remote host from the drop-down list.  The bucket and the Redshift database to be used must be in the same region on Amazon. This could avoid the S3ServiceException errors known to Amazon. For further information about these errors, see [S3ServiceException Errors](https://docs.aws.amazon.com/redshift/latest/dg/s3serviceexception-error.html). |
| Key | Specify the path to the file that contains the data to be loaded.  This field is available only when S3 is selected from the Data source type drop-down list. |
| Cluster id | Specify the ID of the cluster that stores the data to be loaded.  This field is available only when EMR is selected from the Data source type drop-down list. |
| HDFS path | Specify the HDFS file path that references the data file.  This field is available only when EMR is selected from the Data source type drop-down list. |
| Table | Specify the name of the DynamoDB table that contains the data to be loaded.  This field is available only when DynamoDB is selected from the Data source type drop-down list. |
| Read ratio | Specify the percentage of the DynamoDB table's provisioned throughput to use for the data load.  This field is available only when DynamoDB is selected from the Data source type drop-down list. |
| SSH manifest file | Specify the object key for the SSH manifest file that provides the information used to open SSH connections and execute remote commands.  This field is available only when Remote host is selected from the Data source type drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| File type | Select the type of the file that contains the data to be loaded.   * Delimited file   or CSV: a delimited/CSV file. * JSON: a JSON file. * AVRO: an Avro file. * Fixed   width: a fixed-width file. * Apache Parquet: an Apache Parquet file. This   option is available only when S3 is selected from the Data source type drop-down list   in the Basic settings   view.   This list is available when S3, EMR, or Remote host is selected from the Data source type drop-down list. |
| Fields terminated by | Enter the character used to separate fields.  This field is available only when Delimited file or CSV is selected from the File type list. |
| Enclosed by | Select the character in which the fields are enclosed.  This list is available only when Delimited file or CSV is selected from the File type list. |
| JSON mapping | Specify how to map the data elements in the source file to the columns in the target table on Amazon Redshift. The valid values are:   * auto: Map the data by matching object keys or   names in the source name/value pairs for a JSON file or field   names in the Avro schema for an Avro file to the names of   columns in the target table. The argument is case-sensitive and   must be enclosed in double quotation marks. * *s3://jsonpaths\_file*: Map the data using the named JSONPaths   file. The parameter must be an Amazon S3 object key that is   enclosed in double quotation marks and explicitly references a   single file, for example, *s3://mybucket/jsonpaths.txt*. For more information, see   [Data   Format Parameters](http://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-data-format.html#copy-json-jsonpaths).   This field is available only when JSON or AVRO is selected from the File type list. |
| Fixed width mapping | Enter a string that specifies a user-defined column label and column width between double quotation marks. The format of the string is:  ColumnLabel1:ColumnWidth1,ColumnLabel2:ColumnWidth2,....  Note that the column label in the string has no relation to the table column name and it can be either a text string or an integer. The order of the label/width pairs must match the order of the table columns exactly.  This field is available only when Fixed width is selected from the File type list. |
| Compressed by | Select this check box and from the list displayed select the compression type of the source file.  This check box is available when S3, EMR, or Remote host is selected from the Data source type drop-down list. |
| Decrypt | Select this check box if the file is encrypted using Amazon S3 client-side encryption. In the Encryption key field displayed, specify the encryption key used to encrypt the file. Note that only a base64 encoded AES 128-bit or AES 256-bit envelope key is supported. For more information, see [Loading Encrypted Data Files from Amazon S3](http://docs.aws.amazon.com/redshift/latest/dg/c_loading-encrypted-files.html).  This check box is available when S3 is selected from the Data source type drop-down list and Use an existing S3 connection is not selected in the Basic settings view. |
| Encoding | Select the encoding type of the data to be loaded from the list.  This list is available when S3, EMR, or Remote host is selected from the Data source type drop-down list. |
| Date format | Select one of the following items from the list to specify the date format in the source data:   * NONE: No date format is specified. * PATTERN: Select this item and specify the date   format in the field displayed. The default date format is   YYYY-MM-DD. * AUTO: Select this item if you want Amazon   Redshift to recognize and convert automatically the date   format. |
| Time format | Select one of the following items from the list to specify the time format in the source data:   * NONE: No time format is specified. * PATTERN: Select this item and specify the time   format in the field displayed. The default time format is   YYYY-MM-DD HH:MI:SS. * AUTO: Select this item if you want Amazon   Redshift to recognize and convert automatically the time   format. * EPOCHSECS: Select this item if the source data   is represented as epoch time, the number of seconds since Jan 1,   1970 00:00:00 UTC. * EPOCHMILLISECS: Select this item if the source   data is represented as epoch time, the number of milliseconds   since Jan 1, 1970 00:00:00 UTC. |
| Settings | Click the [+] button below the table to specify more parameters for loading the data.   * Parameter: Click the cell and select a   parameter from the drop-down list. * Value: Set the value for the corresponding   parameter. Note that you cannot set the value for a parameter   (such as IGNOREBLANKLINES) that does not need a   value.   For more information about the parameters, see <http://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>. |
| JDBC url | Select a way to access to an Amazon Redshift database from the JDBC url drop-down list.  * Standard: Use the   standard way to access the Redshift database. * SSO: Use the IAM   Single Sign-ON (SSO) authentication way to access the Redshift Database. Before selecting   this option, ensure that the IAM role added to your Redshift cluster has appropriate   access rights and permissions to this cluster. You can ask the administrator of your AWS   services for more details. This option is available only when Use an existing connection check box is not selected from   the Basic settings. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

Information noteNote:

This component does not support the Row > Reject link.

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | The tRedshiftBulkExec component supports loading data to Amazon Redshift from a delimited/CSV, JSON, or fixed-width file on Amazon S3, but the tRedshiftOutputBulk component now only supports generating and uploading a delimited/CSV file to Amazon S3. When you need to load data from a JSON or fixed-width file, you can use the tFileOutputJSON or tFileOutputPositional component together with the tS3Put component instead of using the tRedshiftOutputBulk component to generate and upload the file to Amazon S3. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Loading/unloading data to/from Amazon S3](tredshiftinput-tredshiftbulkexec-ts3get-loading-unloading-data-to-from-amazon-s3-standard-component-this)
