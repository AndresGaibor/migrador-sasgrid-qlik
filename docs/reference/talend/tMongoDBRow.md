<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbrow · versión 8.0 -->
# tMongoDBRow

Last updated: 9/30/2026

Executes the commands and functions of the MongoDB database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMongoDBRow Standard properties

These properties are used to configure tMongoDBRow running in the Standard Job framework.

The Standard
tMongoDBRow component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| DB Version | List of the database versions. This option is available when the Use existing connection check box is not selected. |
| Use connection string | Select this option to establish a connection using a MongoDB Atlas URI. Enter the URI in the field to the right. See [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) for related information.  This option is available when you select `MongoDB 4.4.X and later` from the DB Version drop-down list.  Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use replica set address | Select this check box to show the Replica address table. In the Replica address table, you can define multiple MongoDB database servers for failover.  This option is available when the Use existing connection check box is not selected. |
| Server and Port | Address and listening port of the database server. This option is available when the Use existing connection or Use replica set address check box is not selected. |
| Database | Name of the database. |
| Use SSL connection (Configure the SSL authentication in tSetKeystore or in Studio preferences) | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Required authentication | Select this check box to enable the database authentication. Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Construct command from keys and values | Select this check box to use a MongoDB database command and enter key-value pairs that will be used to construct a BSON document and be sent to the database server. For more information about MongoDB database commands, see the corresponding [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/method/db.runCommand/#:~:text=Definition%20db.runCommand%28command%2C%20%5Boptions%5D%29%20Provides%20a%20helper%20to%20run,a%20consistent%20interface%20between%20the%20shell%20and%20drivers). |
| Construct command from a JSON string | Select this check box to use a MongoDB database command and enter a JSON string that will be converted to a BSON document and be sent to the database server. For more information about MongoDB database commands, see the corresponding [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/method/db.runCommand/#:~:text=Definition%20db.runCommand%28command%2C%20%5Boptions%5D%29%20Provides%20a%20helper%20to%20run,a%20consistent%20interface%20between%20the%20shell%20and%20drivers).  This component supports [Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/) capabilities, you can use this field to create a vector search index that can then be used in [tMongoDBInput](https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-standard-properties). The [command syntax](https://www.mongodb.com/docs/manual/reference/command/createSearchIndexes/) to create a search index is: ``` "{createSearchIndexes: '<collection name>', indexes: [{name: '<index_name>',type: 'vectorSearch', definition:  {fields: [{type: 'vector', path: '<field_to_index>',numDimensions: <number_of_vector_dimensions>, similarity: '<vector_similarity_function>'}]}}]}" ```  For more information on the index configuration, see [the corresponding MongoDB documentation](https://www.mongodb.com/docs/compass/current/indexes/create-vector-search-index/#provide-the-atlas-vector-search-index-configurations). |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tMongoDBRow allows you to manipulate the MongoDB database through the MongoDB commands and functions. |

**Related concepts**  

* [Using MongoDB functions to create a collection and write data to it](tmongodbinput-tmongodbrow-tlogrow-using-mongodb-functions-to-create-collection-and-write-data-to-it-standard-component-bigdata-this)
