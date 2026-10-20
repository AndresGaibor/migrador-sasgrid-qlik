<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cosmosdb/tcosmosdbinput · versión 8.0 -->
# tCosmosDBInput

Last updated: 9/30/2026

Retrieves certain documents from a Cosmos database collection by supplying a query
document containing the fields the desired documents should match.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tCosmosDBInput Standard properties

These properties are used to configure tCosmosDBInput running in the Standard Job framework.

The Standard
tCosmosDBInput component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| API | Select the database API to be used. Then the corresponding parameters to be defined are displayed in the Component view.  In the current version of this component, only the MongoDB API is supported. For this reason, MongoDB database is often mentioned in the documentation of the CosmosDB components. |
| Use replica set address or multiple query routers | Select this check box to show the Server addresses table.  In the Server addresses table, define the shared MongoDB databases or the MongoDB replica sets you want to connect to. |
| Server and Port | Enter the IP address and listening port of the database server.  Available when the Use replica set address or multiple query routers check box is not selected. |
| Database | Enter the name of the MongoDB database to be connected to. |
| Set read preference | Select this check box and from the Read preference drop-down list that is displayed, select the member to which you need to direct the read operations.  If you leave this check box clear, the Job uses the default Read preference, that is to say, uses the primary member in a replica set.  For further information, see MongoDB's documentation about Replication and its Read preferences. |
| Authentication mechanism | Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Use authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Collection | Name of the collection in the database. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   If a column in the database is a JSON document and you need to read the entire document, put an asterisk (\*) in the DB column column, without quotation marks around. |
| Query | Specify the query condition. This field is available only when you have selected Find query from the Query type drop-down list.  For example, type in "{id:4}" to retrieve the record whose `id` is `4` from the collection specified in the Collection field.  Different from the query statements required in the MongoDB client software, the query here refers to the contents inside find(), such as the query here {id:4} versus the MongoDB client query db.blog.find({id:4}). |
| Specify fields to return | Select this check box to define a set of fields in the documents to be returned from the database |
| Return only these fields | Enter the name of the fields to be returned from the data in this table.  This field is only available when you check the Specify fields to return from the Basic settings view. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |
| Sort by | Specify the column and choose the order for the sort operation.  This field is available only when you have selected Find query from the Query type drop-down list. |
| Limit | Type in the maximum number of records to be retrieved.  This field is available only when you have selected Find query from the Query type drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | As a start component, tCosmosDBInput allows you to retrieve records from a collection in the Cosmos database and transfer them to the following component for display or storage. |
