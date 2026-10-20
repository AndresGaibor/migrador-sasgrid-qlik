<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeoutput · versión 8.0 -->
# tSnowflakeOutput

Last updated: 9/30/2026

Uses the data incoming from its preceding component to insert, update, upsert or
delete data in a Snowflake table.

tSnowflakeOutput uses the bulk loader provided by Snowflake for high
performance database operations.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tSnowflakeOutput Standard properties](/talend/en-US/components/8.0/snowflake/tsnowflakeoutput-standard-properties)
* [tSnowflakeOutput properties for Apache Spark Batch (technical preview)](/talend/en-US/components/8.0/snowflake/tsnowflakeoutput-properties-for-apache-spark-batch-technical-preview)

**Related concepts**  

* [Writing data into and reading data from a Snowflake table](tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-writing-data-into-and-reading-data-from-snowflake-table-standard-component "Here is an example of using Talend Snowflake components to connect to Snowflake, create a Snowflake table, write data into the table, then read data from this table, finally close the connection to Snowflake.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeoutput-properties-for-apache-spark-batch-technical-preview -->
# tSnowflakeOutput properties for Apache Spark Batch (technical preview)

Last updated: 9/30/2026

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

These properties are used to configure tSnowflakeOutput running in the Spark Batch Job framework.

The Spark Batch
tSnowflakeOutput component belongs to the
Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Account | In the Account field, enter, in double quotation marks, the account name that has been assigned to you by Snowflake. |
| Snowflake Region | Select an AWS region or an Azure region from the Snowflake Region dropdown list. |
| Authentication method | Set the authentication method.   * Key Pair: Select   this option if key pair authentication is enabled. For more information   about key pair authentication, see [Using Key Pair   Authentication](https://docs.snowflake.net/manuals/user-guide/jdbc-configure.html#using-key-pair-authentication).   Information noteNote: Before selecting the Key Pair option, make sure you have set the key pair authentication data in the Basic settings view of the tSetKeystore component as follows.  1. Leave the TrustStore type field unchanged. 2. Set TrustStore file to    `""`. 3. Clear the TrustStore password field. 4. Select Need Client authentication. 5. Enter the path to the key store file in double quotation marks in the    KeyStore file field (or click the    […] button to the right of the    KeyStore file field and navigate to the key    store file). 6. Enter the key store file password in the KeyStore    password field. 7. Clear the Check server identity option.  Information noteNote: The Key Pair option is available only with the EMR 5.29 and CDH 6.1 distributions when you are using Spark v2.4 and onwards in the Local Spark mode. |
| User Id and Password | Enter, in double quotation marks, your authentication information to log in to Snowflake.   * In the User ID field, enter, in   double quotation marks, your login name that has been defined in Snowflake   using the *LOGIN\_NAME* parameter of   Snowflake. For details, ask the administrator of your Snowflake   system. * To enter the password, click the [...] button   next to the password field, enter the password in double quotes in the pop-up dialog box,   and click OK to save the settings. |
| Warehouse | Enter, in double quotation marks, the name of the Snowflake warehouse to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Schema | Enter, within double quotation marks, the name of the database schema to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Database | Enter, in double quotation marks, the name of the Snowflake database to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Table | Click the [...] button and in the displayed wizard, select the Snowflake table to be used. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  If the Snowflake data type to be handled is VARIANT, OBJECT, or ARRAY, while defining the schema in the component, select `String` for the corresponding data in the Type column of the schema editor wizard.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Note that if the input value of any non-nullable primitive field is null, the row of data including that field will be rejected. |
| Output Action | Only the Insert action is supported by Snowflake on Spark. |
| Connection properties | Enter, in double quotation marks, a connection property and the associated value in the corresponding columns. You can find the properties available in [Setting Configuration Options for the Connector](https://docs.snowflake.com/en/user-guide/spark-connector-use.html#setting-configuration-options-for-the-connector) from the official Snowflake documentation. |

## Usage

| Properties | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  Use a tSnowflakeConfiguration: update component in the same Job to connect to Snowflake. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeoutput-standard-properties -->
# tSnowflakeOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure tSnowflakeOutput running in the Standard Job framework.

The Standard
tSnowflakeOutput component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Component list | Select the component that opens the database connection to be reused by this component. |
| Account | In the Account field, enter, in double quotation marks, the account name that has been assigned to you by Snowflake. |
| Authentication Type | Set the authentication type.   * Basic: Select this option if key pair   authentication is not enabled. * Key Pair: Select this option if key pair   authentication is enabled.  See [Using Key Pair Authentication](https://docs.snowflake.net/manuals/user-guide/jdbc-configure.html#using-key-pair-authentication) for related   information. * OAuth 2.0: Select this option to use external   OAuth for data accessing.  See [External OAuth Overview](https://docs.snowflake.com/en/user-guide/oauth-ext-overview.html) for related   information.   Information noteNote: Before selecting the Key Pair option, make sure you have set the key pair authentication data in the Basic settings view of the tSetKeystore component as follows.  1. Leave the TrustStore type field unchanged. 2. Set TrustStore file to    `""`. 3. Clear the TrustStore password field. 4. Select Need Client authentication. 5. Enter the path to the key store file in double quotation marks in the    KeyStore file field (or click the    […] button to the right of the    KeyStore file field and navigate to the key    store file). 6. Enter the key store file password in the KeyStore    password field. 7. Clear the Check server identity option. |
| OAuth token endpoint | Enter OAuth 2.0 token endpoint. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Client ID | Enter the client ID of your application. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Client Secret | Enter the client secret of your application. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Grant type | Set the grant type for retrieving the access token. Two options are provided: Client Credentials and Password. Click [Client Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.4) and [Resource Owner Password Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.3) for related information.  This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| OAuth username | Enter the OAuth username. This option is available when Password is selected from the Grant type dropdown list. |
| OAuth password | Enter the OAuth password. To enter the password, click the [...] button next to the password field, enter the password between double quotes in the pop-up dialog box, and then click OK to save the settings.  This option is available when Password is selected from the Grant type dropdown list.  Information noteNote: OAuth password does not support spaces. |
| Scope | Enter the scope. See [Scopes](https://docs.snowflake.com/en/user-guide/oauth-ext-overview.html#scopes) for related information. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| User Id and Password | Enter, in double quotation marks, your authentication information to log in to Snowflake.   * In the User ID field, enter, in   double quotation marks, your login name that has been defined in Snowflake   using the *LOGIN\_NAME* parameter of   Snowflake. For details, ask the administrator of your Snowflake   system. * To enter the password, click the [...] button   next to the password field, enter the password in double quotes in the pop-up dialog box,   and click OK to save the settings. |
| Warehouse | Enter, in double quotation marks, the name of the Snowflake warehouse to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Schema | Enter, within double quotation marks, the name of the database schema to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Database | Enter, in double quotation marks, the name of the Snowflake database to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Table | Click the [...] button and in the displayed wizard, select the Snowflake table to be used. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  If the Snowflake data type to be handled is VARIANT, OBJECT, or ARRAY, while defining the schema in the component, select `String` for the corresponding data in the Type column of the schema editor wizard.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Note that if the input value of any non-nullable primitive field is null, the row of data including that field will be rejected.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Table Action | Select the action to be carried out to the table.  * NONE: Leave the table as is. * DROP\_CREATE: Remove the table and create it   again. * CREATE: Create a new table. * CREATE\_IF\_NOT\_EXISTS: Create the table if it does not   exist. * DROP\_IF\_EXISTS\_AND\_CREATE: Remove the table if it   already exists and create again. * CLEAR: Remove all the data records in the table. * TRUNCATE: Remove all the rows in the table. This   action releases the space occupied by the table. |
| Output Action | Select the operation you want to perform to the incoming data and data records in the Snowflake database table. You can insert, delete, update, or merge data in the Snowflake table. This option assumes that the Snowflake table specified in Table field already exists.  * INSERT: Insert new records in the Snowflake   table. * UPDATE: Update existing records in the Snowflake   table. * UPSERT: Create new records and update existing   records. You need to specify a schema column as the join key from the   Upsert Key Column dropdown list or specify to use   the schema keys for the operation by selecting Use schema keys   for upsert in the Advanced settings   view. Information noteNote: The Upsert Key Column dropdown list is   available when Use schema keys for upsert is not   selected. * DELETE: Remove records from the Snowflake table. |
| Die on error | Select this option to stop the execution of the Job when an error occurs; clear this option to skip any rows on error and complete the process for error-free rows.  This option cannot work with Row > Reject connections. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| Login Timeout | Specify the timeout period (in minutes) of Snowflake login attempts. An error will be generated if no response is received in this period. |
| Role | Enter, in double quotation marks, the default access control role to use to initiate the Snowflake session.  This role must already exist and has been granted to the user ID you are using to connect to Snowflake. If this field is left empty, the PUBLIC role is automatically granted. For information about Snowflake access control model, see [Understanding the Access Control Model](https://docs.snowflake.net/manuals/user-guide/security-access-control.html). |
| URL suffix | Enter, in double quotation marks, the Snowflake custom domain URL of your choice. For more information about Snowflake URL formats, see [Standard account URLs](https://docs.snowflake.com/en/user-guide/organizations-connect#standard-account-urls).  For Snowflake components other than tSnowflakeConnection, this field is available when you select Use This Component from the Connection Component dropdown list in the Basic settings view. |
| Allow Snowflake to convert columns and tables to uppercase | Select this checkbox to convert lowercase in the defined table name and schema column names to uppercase. Note that unquoted identifiers should match the Snowflake Identifier Syntax. If you deselect the checkbox, all identifiers are automatically quoted.  This property is not available when you select the Manual Query checkbox.  For more information on the Snowflake Identifier Syntax, see [Identifier Syntax](https://docs.snowflake.net/manuals/sql-reference/identifiers-syntax.html). |
| Convert empty strings to null | Select this option to convert empty strings to null. |
| Use existing database schema as the dynamic schema | If you are using the dynamic schema feature, select this checkbox to pick the schema from the database itself (if the table exists). If this option is not selected, the input schema is used by default. |
| Use schema keys for upsert | Select this option to use schema keys for the Upsert operation. This option is available when you select UPSERT from the Output Action dropdown list in the Basic settings view. |
| Custom DB Type | Select this checkbox to specify the DB type for each column in the schema. This property is available only when you select an action with Create Table from the Table Action dropdown list in the Basic settings. |
| Custom Date type mapping for creating table with dynamic schema | If you are using the dynamic schema feature, select this checkbox to use a custom mapping for your date type date, and then select the mapping from the Convert Date values to dropdown list. This option is available when you select the following option from the Table Action dropdown list in the Basic settings view:  * CREATE * DROP\_CREATE * CREATE\_IF\_NOT\_EXISTS |
| Use schema date pattern | Select this option to convert data in schema columns that are of Date type using the date pattern defined in the schema. To achieve this, you need also to specify the DB type of the schema columns as STRING, TEXT, or VARCHAR in the Custom DB Type field. |
| Use vectors | This component supports vector search capabilities, you can use this option to specify which column holds the vector data type used for vector search. To do this, you need to specify in the Vector properties table the column name (Column), the data type of the schema column (Vector type), and its size (Vector size).  For more information on Snowflake vector search, see the corresponding [Snowflake documentation](https://docs.snowflake.com/en/sql-reference/data-types-vector). |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| NB\_SUCCESS | The number of rows successfully processed. This is an After variable and it returns an integer. |
| NB\_REJECT | The number of rows rejected. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is end component of a data flow in your Job. It receives data fromRow > Main link.  It can also send error messages to other components via a Row > Rejects link. The provided information about an error could be:  * The name of the column in error. * The number of the row in error. * The category of the error, such as a parsing error or   a conversion error. * The character offset in the line in error. * The related error message. * The offset of the byte in error. * The number of the line in error. * SQLSTATE for the error. * Snowflake error code. |
