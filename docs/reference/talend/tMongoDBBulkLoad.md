<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbbulkload · versión 8.0 -->
# tMongoDBBulkLoad

Last updated: 9/30/2026

Imports data files in different formats (CSV, TSV or JSON) into the specified
MongoDB database so that the data can be further processed.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMongoDBBulkLoad Standard properties

These properties are used to configure tMongoDBBulkLoad running in the Standard Job framework.

The Standard
tMongoDBBulkLoad component belongs to the Big Data and the Databases NoSQLfamilies.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| MongoDB directory | Fill in this field with the MongoDB home directory. |
| Use local DB path | Select this check box to provide the information of the local database that you want to use. MongoDB V3.0 and onward versions do not support this feature.  * Local DB path: type in the path to   the local database specified when starting the MongoDB server. |
| Use replica set address | Select this check box to define a replica set to be connected.  * Replica set name: specify the name   of the replica set. * Replica address: specify multiple   MongoDB database servers for failover as needed. Note that if you leave   the replica host or replica port unspecified, their default values *localhost* and *27017* will be   used. |
| Use connection string | Select this option to establish a connection using a MongoDB Atlas URI. Enter the URI in the field to the right. See [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) for related information.  Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Server | Hostname or IP address of the database server. Note that the default value *localhost* will be used if the server is not specified. This field is available only when the Use replica set address check box is not selected. |
| Port | Listening port of the database server. Note that the default value *27017* will be used if the port is not specified. This field is available only when the Use replica set address check box is not selected. |
| Database | Type in the name of the database to import data to. |
| Collection | Type in the name of the collection to import data to. |
| Use SSL connection | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Drop collection if exist | Select this check box to remove the collection if it already exists. |
| Required authentication | Select this check box to enable the database authentication. Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Certificate | Enter the path to the certificate file. You can also fill this field by clicking the [...] button to the right of this field, navigating to the folder where the certificate file resides, and selecting the certificate file. This field is available when you select `X509` from the Authentication mechanism drop-down list. |
| Use certificate authority | Select this option to use a CA certificate. You need to enter the path to the CA certificate file in the field to the right. You can also fill this field by clicking the [...] button to the right of this field, navigating to the folder where the certificate file resides, and selecting the certificate file. This field is available when you select `X509` from the Authentication mechanism drop-down list. |
| Data file | Type in the full path of the file from which the data will be imported or click the [...] button to browse to the desired data file. Make sure that the data file is in standard format. For example, the fields in CSV files should be separated with commas. |
| File type | Select the proper file type from the list. CSV, TSV, and JSON are supported. |
| The JSON file starts with an array | Select this check box to allow tMongoDBBulkload to read the JSON files starting with an array. This check box appears when the File type you have selected is JSON. |
| Action on data | Select the action that you want to perform on the data.  * Insert: Insert the data into the   database.  Note that when inserting data from CSV or TSV files into   the MongoDB database, you need to specify fields either by selecting the   First line is header check box   or defining them in the schema. * Upsert: Insert the data if they do   not exist or update the existing data.  Note that when upserting data into the MongoDB database,   you need to specify a list of fields for the query portion of the upsert   operation. |
| Upsert fields | Customize the fields that you want to upsert as needed. This table is available when you select Upsert from the Action on data list. |
| First line is header | Select this check box to use the first line in CSV or TSV files as a header. This check box is available only when you select CSV or TSV from the File type list. |
| Ignore blanks | Select this check box to ignore the empty fields in CSV or TSV files. This check box is available only when you select CSV or TSV from the File type list. |
| Print log | Select this check box to print logs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional arguments | Complete this table to use the additional arguments as required. For example, you can use the argument "--jsonArray" to accept the import of data expressed with multiple MongoDB documents within a single JSON array. For more information about the additional arguments, read [the MongoDB documentation](https://www.mongodb.com/docs/database-tools/mongoimport/#options). |
| Disable retryable writes | Select this check box to disable automatic retries of write operations. For more information about this option, read [the MongoDB documentation](https://www.mongodb.com/docs/manual/core/retryable-writes/). This option is only supported with mongoimport from version 100.9.5 onwards. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used together with the tMongoDBInput component to check if the data is imported as expected. |
| Limitation | The MongoDB client tool needs to be installed on the machine where Jobs using this component are executed. |

**Related concepts**  

* [Importing data into MongoDB database](tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-importing-data-into-mongodb-database-standard-component-bigdata-the)
