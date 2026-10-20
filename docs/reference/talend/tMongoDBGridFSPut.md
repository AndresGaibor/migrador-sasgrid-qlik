<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfsput · versión 8.0 -->
# tMongoDBGridFSPut

Last updated: 9/30/2026

Connects to a MongoDB GridFS system to load files into it.

tMongoDBGridFSPut copies files from a
local directory, pastes them into a given MongoDB GridFS system and if needs be, renames
these files.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMongoDBGridFSPut Standard properties

These properties are used to configure tMongoDBGridFSPut running in the Standard Job framework.

The Standard
tMongoDBGridFSPut component belongs to the Big Data and the Databases NoSQL families.

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
| Required authentication | Select this check box to enable the database authentication.  Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Bucket | Enter the name of the bucket you need to write files in. A bucket of GridFS is similar to a folder. |
| Local Folder | Browse to, or enter the path to the folder in which the files to be copied and written to GridFS are stored. |
| Use Perl5 Regex Expression as Filemask | Select this check box if you want to use Perl5 regular expressions in the Files field as file filters. This is useful when the name of the file to be used contains special characters such as parentheses.  For information about Perl5 regular expression syntax, see [Perl5 Regular Expression Syntax](http://perldoc.perl.org/perlre.html#Regular-Expressions). |
| Files | In the Files area, the fields to be completed are:  - File mask: type in the file name to be selected from the local directory. Regular expression is available.  - New name: give a new name to the loaded file. |

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
| **Usage rule** | This component combines MongoDB GridFS connection and data extraction, thus usually used as a single-component subJob to copy data from a user-defined local directory to GridFS.  It is often connected to the Job using OnSubjobOk or OnComponentOk link, depending on the context. |

**Related concepts**  

* [Managing files using MongoDB GridFS](tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-managing-files-using-mongodb-gridfs-standard-component-bigdata-in-this)
