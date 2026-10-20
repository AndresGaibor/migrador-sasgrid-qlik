<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfsproperties · versión 8.0 -->
# tMongoDBGridFSProperties

Last updated: 9/30/2026

Obtains information about the properties of given files selected based on a
query.

tMongoDBGridFSProperties iterates on
files of a bucket in MongoDB GridFS to extract the attributes of these files.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMongoDBGridFSProperties Standard properties

These properties are used to configure tMongoDBGridFSProperties running in the Standard Job framework.

The Standard
tMongoDBGridFSProperties component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| DB Version | List of the database versions.  Available when the Use existing connection check box is not selected. |
| Use connection string | Select this option to establish a connection using a MongoDB Atlas URI. Enter the URI in the field to the right. See [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) for related information.  This option is available when you select `MongoDB 4.4.X and later` from the DB Version drop-down list.  Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use replica set address or multiple query routers | Select this check box to show the Server addresses table.  In the Server addresses table, define the shared MongoDB databases or the MongoDB replica sets you want to connect to. |
| Server and Port | IP address and listening port of the database server.  Available when the Use replica set address check box is not selected.  Note that if you use the authentication mechanisms to connect to this MongoDB database, you must enter the name, rather than the IP address, of the host of the database server. |
| Database | Name of the database. |
| Use SSL connection (Configure the SSL authentication in tSetKeystore or in Studio preferences) | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Set read preference | Select this check box and from the Read preference drop-down list that is displayed, select the member to which you need to direct the read operations.  If you leave this check box clear, the Job uses the default Read preference, that is to say, uses the primary member in a replica set.  For further information, see MongoDB's documentation about Replication and its Read preferences. |
| Use authentication | Select this check box to enable the database authentication.  Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Bucket | Enter the name of the bucket in which the files to be used are stored. A bucket of GridFS is similar to a folder. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The columns of the predefined schema of tMongoDBGridFSProperties represent the default attributes of a GridFS file and the column names are already identical with the attribute names.  * If you want to exclude some attributes from the data   flow to be processed in your Job, you can remove the columns corresponding to those   attributes from this schema. * Do not change the names of the columns to be used,   because the names of each column must be identical with the name of the file attribute   it represents. * If the files to be processed contain some custom   attributes you want to extract, you need to add their representative columns accordingly   and ensure that these columns and these custom attributes are using identical names. |
| Query type | Select the type of the query you want tMongoDBGridFSProperties to perform to select the files from which you need to extract the attributes.   * Filename: you need to enter   the name of the file to be used. This name is the value of the   *filename* attribute of this   file. Note that only one name is allowed.  In GridFS, a file is identified only by its unique identifier   (its object ID); its file name is not necessarily unique. * Mongo Query: enter the query   to be used to select the files to be used.  The example query, {} within double quotation   marks provided with tMongoDBGridFSProperties, means to select all of the   files in a bucket. You can put   {'filename':{'$regex':'REGEX\_PATTERN'}} to apply a   regular expression to defining the file names to be used. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_FILE: the number of files processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component combines MongoDB GridFS connection and data extraction and needs to use a Main link to connect to its following component in order to send data to this component. |

**Related concepts**  

* [Managing files using MongoDB GridFS](tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-managing-files-using-mongodb-gridfs-standard-component-bigdata-in-this)
