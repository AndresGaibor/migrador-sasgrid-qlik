<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbconnection · versión 8.0 -->
# tMongoDBConnection

Last updated: 9/30/2026

Creates a connection to a MongoDB database and reuse that connection in other
components.

tMongoDBConnection opens a connection to a database in order that a
transaction may be made.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMongoDBConnection Standard properties

These properties are used to configure tMongoDBConnection running in the Standard Job framework.

The Standard
tMongoDBConnection component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| DB Version | List of the database versions. |
| Use connection string | Select this option to establish a connection using a MongoDB Atlas URI. Enter the URI in the field to the right. See [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) for related information.  This option is available when you select `MongoDB 4.4.X and later` from the DB Version drop-down list.  Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use replica set address | Select this check box to show the Replica address table.  In the Replica address table, you can define multiple MongoDB database servers for failover. |
| Server and Port | IP address and listening port of the database server.  Available when the Use replica set address check box is not selected. |
| Database | Name of the database. |
| Use SSL connection (Configure the SSL authentication in tSetKeystore or in Studio preferences) | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you must specify the encryption information using one of these methods:  * If you want to centralize the connection information, set up the SSL   connection in Windows > Preferences > Talend > SSL and check the Enable SSL field in   the MongoDB connection configuration in   Metadata. * If you want to keep this information within the scope of this Job, use   the tSetKeystore component in the   same Job.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Required authentication | Select this check box to enable the database authentication.  Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>.  This parameter is only available when you select MongoDB 3.5.x from the DB version drop-down list in the Basic settings tab. |
| Apply optional attributes | Select this option to set and apply optional attributes for the connection to be established.  In the Optional attributes table, click the plus button on the bottom to add a row, select the desired attribute from the drop-down list in the Name column, and set a value for the attribute in the Value column. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other MongoDB components, particularly tMongoClose. |

**Related concepts**  

* [Creating a collection and writing data to it](tmongodbinput-tmongodboutput-tlogrow-creating-collection-and-writing-data-to-it-standard-component-bigdata-this)
* [Inserting records to a MongoDB collection using a dynamic schema](inserting-records-to-a-mongodb-collection-using-dynamic-schema)
* [Managing files using MongoDB GridFS](tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-managing-files-using-mongodb-gridfs-standard-component-bigdata-in-this)
* [Retrieving data from a collection by advanced queries](tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-retrieving-data-from-collection-by-advanced-queries-standard-component-bigdata-in-this)
* [Upserting records in a collection](tmongodbinput-tmongodboutput-tlogrow-upserting-records-in-collection-standard-component-bigdata-this)
* [Using MongoDB functions to create a collection and write data to it](tmongodbinput-tmongodbrow-tlogrow-using-mongodb-functions-to-create-collection-and-write-data-to-it-standard-component-bigdata-this)
