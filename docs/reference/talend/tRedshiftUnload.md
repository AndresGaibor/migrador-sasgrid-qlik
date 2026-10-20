<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftunload · versión 8.0 -->
# tRedshiftUnload

Last updated: 9/30/2026

Unloads data on Amazon Redshift to files on Amazon S3.

This component runs a specified query in Amazon Redshift and then unloads the result of
the query to one or more files on Amazon S3.

## tRedshiftUnload Standard properties

These properties are used to configure
tRedshiftUnload running in the Standard Job framework.

The
Standard
tRedshiftUnload component belongs to the Cloud and the Databases
families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In:   No property data stored centrally. * Repository: Select the repository file in which the   properties are stored. The database connection fields that   follow are completed automatically using the data retrieved. |
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
| Table Name | Type in the name of the table from which the data will be read. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Query Type and Query | Enter the database query paying particularly attention to the proper sequence of the fields in order to match the schema definition.  Double-escape each simple quotation marks in the query. For example, ``` SELECT name, birth,\"Add\" FROM my_table WHERE birth between \\'2018-01-01 00:00:00\\' and \\'2019-01-01 00:00:00\\' ``` |
| Guess Query | Click the button to generate the query which corresponds to the table schema in the Query field. |
| Use an existing S3 connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Access Key | Specify the Access Key ID that uniquely identifies an AWS Account. For how to get your Access Key and Access Secret, visit [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html).  This option is not available if Use an existing S3 connection is selected. |
| Secret Key | Specify the Secret Access Key, constituting the security credentials in combination with the access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  This option is not available if Use an existing S3 connection is selected. |
| Assume Role | Select this checkbox and specify the values for the following parameters used to create a new assumed role session.   * IAM Role ARNs chains: a series of   chained roles, which may belong to other accounts, that your cluster   can assume to access resources.  You can chain a maximum of 10 roles. * Role ARN: the Amazon Resource Name   (ARN) of the role to assume.   This option is not available if Use an existing S3 connection is selected.  For more information on IAM Role ARNs chains, see [Authorizing Redshift service](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service.html). |
| Bucket | Type in the name of the Amazon S3 bucket, namely the top level folder, to which the data is unloaded. |
| Key prefix | Type in the name prefix for the unload files on Amazon S3. By default, the unload files are written per slice of the Redshift cluster and the file names are written in the format <object\_path>/<name\_prefix><slice-number>\_part\_<file-number>. |

## Advanced settings

| Properties | Description |
| --- | --- |
| File type | Select the type of the unload files on Amazon S3 from the list:   * Delimited file or CSV: a delimited/CSV file. * Fixed width: a fixed-width file. * Apache Parquet: an Apache Parquet file. |
| Fields terminated by | Enter the character used to separate fields.  This field appears only when Delimited file or CSV is selected from the File type list. |
| Enclosed by | Select the character in a pair of which the fields are enclosed.  This list appears only when Delimited file or CSV is selected from the File type list. |
| Fixed width mapping | Enter a string that specifies a user-defined column label and column width between double quotation marks. The format of the string is:  ColumnLabel1:ColumnWidth1,ColumnLabel2:ColumnWidth2,....  Note that the column label in the string has no relation to the table column name and it can be either a text string or an integer. The order of the label/width pairs must match the order of the table columns exactly.  This field appears only when Fixed width is selected from the File type list. |
| Compressed by | Select this check box and from the list displayed select the compression type of the files. |
| Encrypt | Select this check box to encrypt unload file(s) using Amazon S3 client-side encryption. In the Encryption key field displayed, enter the encryption key used to encrypt the unload file(s).  Note that only a base64 encoded AES 128-bit or AES 256-bit envelope key is supported. For more information, see [Unloading Encrypted Data Files](http://docs.aws.amazon.com/redshift/latest/dg/t_unloading_encrypted_files.html).  Because client-side encryption for Parquet files is not supported, this option only works for delimited/CSV files and fixed-width files.  This option is not available if Use an existing S3 connection is selected. |
| Specify null string | Select this check box and from the list displayed select a string that represents a null value in unload files. |
| Escape | Select this check box to place an escape character (\) before every occurrence of the following characters for CHAR and VARCHAR columns in the delimited unload files: linefeed (\n), carriage return (\r), the delimiter character specified for the unloaded data, the escape character (\), a quote character (" or '). |
| Overwrite s3 object if exist | Select this check box to overwrite the existing Amazon S3 object files. |
| Parallel | Select this check box to write data in parallel to multiple unload files on Amazon S3 according to the number of slices in the Redshift cluster. |
| JDBC url | Select a way to access to an Amazon Redshift database from the JDBC url drop-down list.  * Standard: Use the   standard way to access the Redshift database. * SSO: Use the IAM   Single Sign-ON (SSO) authentication way to access the Redshift Database. Before selecting   this option, ensure that the IAM role added to your Redshift cluster has appropriate   access rights and permissions to this cluster. You can ask the administrator of your AWS   services for more details. This option is available only when Use an existing connection check box is not selected from   the Basic settings. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for the Amazon Redshift database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Loading/unloading data to/from Amazon S3](tredshiftinput-tredshiftbulkexec-ts3get-loading-unloading-data-to-from-amazon-s3-standard-component-this)
