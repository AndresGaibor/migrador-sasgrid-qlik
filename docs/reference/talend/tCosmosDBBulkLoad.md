<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cosmosdb/tcosmosdbbulkload · versión 8.0 -->
# tCosmosDBBulkLoad

Last updated: 9/30/2026

Imports data files in different formats (CSV, TSV or JSON) into the specified
Cosmos database so that the data can be further processed.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tCosmosDBBulkLoad Standard properties

These properties are used to configure tCosmosDBBulkLoad running in the Standard Job framework.

The Standard
tCosmosDBBulkLoad component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| MongoDB directory | Fill in this field with the MongoDB home directory. |
| Use replica set address or multiple query routers | Select this check box to show the Server addresses table.  In the Server addresses table, define the shared MongoDB databases or the MongoDB replica sets you want to connect to. |
| Server and Port | Enter the IP address and listening port of the database server.  Available when the Use replica set address or multiple query routers check box is not selected. |
| Database | Enter the name of the MongoDB database to be connected to. |
| Collection | Type in the name of the collection to import data to. |
| Drop collection if exist | Select this check box to remove the collection if it already exists. |
| Authentication mechanism | Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Data file | Type in the full path of the file from which the data will be imported or click the [...] button to browse to the desired data file. Make sure that the data file is in standard format. For example, the fields in CSV files should be separated with commas. |
| File type | Select the proper file type from the list. CSV, TSV, and JSON are supported. |
| The JSON file starts with an array | Select this check box to allow tCosmosDBBulkload to read the JSON files starting with an array. This check box appears when the File type you have selected is JSON. |
| Action on data | Select the action that you want to perform on the data.  * Insert: Insert the data into the database. Note   that when inserting data from CSV or TSV files into the MongoDB database,   you need to specify fields either by selecting the First line   is header check box or defining them in the   schema. * Upsert: Insert the data if they do not exist or   update the existing data. Note that when upserting data into the MongoDB   database, you need to specify a list of fields for the query portion of   the upsert operation. |
| Upsert fields | Customize the fields that you want to upsert as needed. This table is available when you select Upsert from the Action on data list. |
| First line is header | Select this check box to use the first line in CSV or TSV files as a header. This check box is available only when you select CSV or TSV from the File type list. |
| Ignore blanks | Select this check box to ignore the empty fields in CSV or TSV files. This check box is available only when you select CSV or TSV from the File type list. |
| Print log | Select this check box to print logs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional arguments | Complete this table to use the additional arguments as required. For example, you can use the argument "--jsonArray" to accept the import of data expressed with multiple MongoDB documents within a single JSON array. For more information about the additional arguments, go to <http://docs.mongodb.org/manual/reference/program/mongoimport/> and read the description of options. |
| Disable retryable writes | Select this check box to disable automatic retries of write operations. For more information about this option, read [the MongoDB documentation](https://www.mongodb.com/docs/manual/core/retryable-writes/). This option is only supported with mongoimport from version 100.9.5 onwards. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used together with the tCosmosDBInput component to verify if the data is imported as expected. |
| Limitation | The MongoDB client tool needs to be installed on the machine where Jobs using this component are executed. |
