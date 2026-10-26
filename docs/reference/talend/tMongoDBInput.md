<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput · versión 8.0 -->
# tMongoDBInput

Last updated: 9/30/2026

Retrieves records from a collection in the MongoDB database and transfers them to
the following component for display or storage.

tMongoDBInput retrieves certain
documents from a MongoDB database collection by supplying a query document containing
the fields the desired documents should match.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tMongoDBInput Standard properties](/talend/en-US/components/8.0/mongodb/tmongodbinput-standard-properties)
* [tMongoDBInput properties for Apache Spark Batch](/talend/en-US/components/8.0/mongodb/tmongodbinput-properties-for-apache-spark-batch)
* [tMongoDBInput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/mongodb/tmongodbinput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Creating a collection and writing data to it](tmongodbinput-tmongodboutput-tlogrow-creating-collection-and-writing-data-to-it-standard-component-bigdata-this)
* [Importing data into MongoDB database](tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-importing-data-into-mongodb-database-standard-component-bigdata-the)
* [Inserting records to a MongoDB collection using a dynamic schema](inserting-records-to-a-mongodb-collection-using-dynamic-schema)
* [Retrieving data from a collection by advanced queries](tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-retrieving-data-from-collection-by-advanced-queries-standard-component-bigdata-in-this)
* [Upserting records in a collection](tmongodbinput-tmongodboutput-tlogrow-upserting-records-in-collection-standard-component-bigdata-this)
* [Using MongoDB functions to create a collection and write data to it](tmongodbinput-tmongodbrow-tlogrow-using-mongodb-functions-to-create-collection-and-write-data-to-it-standard-component-bigdata-this)
* [Writing and reading data from MongoDB using a Spark Batch Job](tmongodboutput-tmongodbinput-ts3configuration-writing-and-reading-data-from-mongodb-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-properties-for-apache-spark-batch -->
# tMongoDBInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMongoDBInput running in the Spark Batch Job framework.

The Spark Batch
tMongoDBInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| MongoDB configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   If a column in the database is a JSON document and you need to read the entire document, put an asterisk (\*) in the DB column column, without quotation marks around. |
| Collection | Enter the name of the collection to be used.  A MongoDB collection is the equivalent of an RDBMS table and contains documents.  If the collection to be used is not shared, it is recommended to add the *mongo.input.split\_size* property to the Advanced Hadoop MongoDB properties table. This parameter determines how the collection is going to be partitioned and read by the Spark executors. The number of partitions of the input collection can be calculated using the following formula:  ``` Number of partitions = Collection size in MB / mongo.input.split_size ```  Without this property, Spark uses the default value, 8 MB, for the partition size.  For example:  ``` mongo.input.split_size   1 ```  In this example, Spark dispatches 1 MB to each Spark executor in order to read the non-shared collection in parallel. If the collection size is 10 MB, 10 executors are employed. |
| Set read preference | Select this check box and from the Read preference drop-down list that is displayed, select the member to which you need to direct the read operations.  If you leave this check box clear, the Job uses the default Read preference, that is to say, uses the primary member in a replica set.  For further information, see MongoDB's documentation about Replication and its Read preferences. |
| Query | Specify the query statement to select documents from the collection specified in the Collection field. For example, type in "{'id':'4'}" to retrieve the record whose *id* is *4* from the collection.  The default query, {} within double quotation marks provided with this component, means to select all of the files. You can also apply a regular expression by putting {'filename':{'$regex':'REGEX\_PATTERN'}} to define the file names to be used.  Different from the query statements required in the MongoDB client software, the query here refers to the contents inside find(), such as the query {'filename':{'$regex':'REGEX\_PATTERN'}} here is the equivalent of db.blog.find({filename:{$regex:REGEX\_PATTERN}}) in the MongoDB client query. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |
| Limit | Enter the maximum number of records to be retrieved. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced Hadoop MongoDB properties | Add properties to define extra operations you need tMongoDBInput to perform when reading data.  The available properties are listed and explained in [MongoDB Connector for Hadoop](https://github.com/mongodb/mongo-hadoop/wiki/Configuration-Reference).  If the collection to be used is not shared, it is recommended to add the *mongo.input.split\_size* property to the Advanced Hadoop MongoDB properties table. This parameter determines how the collection is going to be partitioned and read by the Spark executors. The number of partitions of the input collection can be calculated using the following formula:  ``` Number of partitions = Collection size in MB / mongo.input.split_size ```  Without this property, Spark uses the default value, 8 MB, for the partition size.  For example:  ``` mongo.input.split_size   1 ```  In this example, Spark dispatches 1 MB to each Spark executor in order to read the non-shared collection in parallel. If the collection size is 10 MB, 10 executors are employed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tMongoDBConfiguration component present in the same Job to connect to a MongoDB database. You need to drop a tMongoDBConfiguration component alongside this component and configure the Basic settings of this component to use tMongoDBConfiguration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-standard-properties -->
# tMongoDBInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tMongoDBInput running in the Standard Job framework.

The Standard
tMongoDBInput component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| DB Version | Select the database version you want to use from the drop-down list. This field is available when the Use existing connection check box is not selected. |
| Use connection string | Select this option to establish a connection using a MongoDB Atlas URI. Enter the URI in the field to the right. See [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) for related information.  This option is available when you select `MongoDB 4.4.X and later` from the DB Version drop-down list.  Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use replica set address | Select this check box to show the Replica address table. In the Replica address table, you can define multiple MongoDB database servers for failover.  This field is available when the Use existing connection check box is not selected. |
| Server and Port | Enter the IP address and listening port of the database server. These fields are available when the Use existing connection or Use replica set address check box are not selected. |
| Database | Enter the name of the database. |
| Use SSL connection (Configure the SSL authentication in tSetKeystore or in Studio preferences) | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Set read preference | Select this check box and from the Read preference drop-down list that is displayed, select the member to which you need to direct the read operations.  If you leave this check box clear, the Job uses the default Read preference, that is to say, uses the primary member in a replica set.  For further information, see MongoDB's documentation about Replication and its Read preferences. |
| Required authentication | Select this check box to enable the database authentication. Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This field is available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Collection | Enter the name of the collection in the MongoDB database. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   If a column in the database is a JSON document and you need to read the entire document, put an asterisk (\*) in the DB column column, without quotation marks around. |
| Query | Specify the query condition. This field is available only when you have selected Find query from the Query type drop-down list. For example, type in "{id:4}" to retrieve the record whose *id* is *4* from the collection specified in the Collection field.  Information noteNote: Different from the query statements required in the MongoDB client software, the query here refers to the contents inside find(), such as the query here {id:4} versus the MongoDB client query db.blog.find({id:4}). |
| Specify fields to return | Select this check box to define a set of fields in the documents to be returned from the database |
| Return only these fields | Enter the name of the fields to be returned from the data in this table. This field is only available when you check the Specify fields to return from the Basic settings view. |
| Aggregation stages | Create a MongoDB aggregation pipeline by adding the stages you want the documents to pass through so as to obtain aggregated results from these documents. This table is available only when you have selected Aggregation pipeline query from the Query type drop-down list. Only one stage is allowed per row in this Aggregation stages table and the stages are executed one by one in the order you place them in this table. For more information about MongoDB aggregation pipeline, see [Aggregation pipeline](https://docs.mongodb.org/manual/core/aggregation-pipeline/).  Example 1:  * If you want to aggregate documents about your customers using the *$match* and the *$group*   stages, you need to add two rows to this Aggregation stages table and define the two stages as   follows: ```   "{$match : {status : 'A'}}"   "{$group : {_id : '$cust_id', total : {$sum : '$amount'}}}"   ```  In this aggregation, the customer documents with   status `A` are selected; then among the selected   customers, those using the same customer ID are grouped and the values   from the `amount` fields of the same customer are   summed up.  For a full list of the stages you can use and their   related operators, see [Aggregation pipeline   operators](https://docs.mongodb.org/manual/reference/operator/aggregation/#aggregation-pipeline-operator-reference).  Example 2:  * This component supports [Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/)   capabilities, you can use this option to query data using the   $vectorSearch aggregation stage, and a vector search index previously   created using a [tMongoDBRow](https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbrow#tmongodbrow-standard-properties)   component: ```   "{$vectorSearch : {index : '<index_name>', path : '<field_to_search>',    queryVector:"[<array_of_numbers>], numCandidates: <number_of_candidates>, limit: <number_of_results>}}}"   ``` For   more information on the $vectorSearch query parameters, see [the corresponding MongoDB   documentation](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-stage/). |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |
| Sort by | Specify the column and choose the order for the sort operation. This field is available only when you have selected Find query from the Query type drop-down list. |
| Limit | Type in the maximum number of records to be retrieved. This field is available only when you have selected Find query from the Query type drop-down list. |
| Skip | Specify the number of the retrieved lines to skip. Note that lines are skipped from the first line. Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Batch size | Specify the maximum number of lines that can be retrieved in one batch. To avoid possible errors, do not set this option to `1`. Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |
| Convert BSON document to string | Select this check box to convert all values in BSON to string. The values for array type are then basic object list. This option is only available for MongoDB 3.5.x, 4.4.x and later versions. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | As a start component, tMongoDBInput allows you to retrieve records from a collection in the MongoDB database and transfer them to the following component for display or storage. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-importing-data-into-mongodb-database-standard-component-bigdata-the -->
# Importing data into MongoDB database

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

The following scenario describes a Job that firstly imports data from a CSV file into
the specified MongoDB collection, then reads data from the MongoDB collection to check
if the import is successful, next continues to import data from a JSON file with the
same data structure into the same MongoDB collection, and finally displays the data from
the MongoDB collection to demonstrate that the data from the JSON file is also imported
successfully.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-dropping-and-linking-components-standard-component-bigdata-drop)
* [Configuring the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-configuring-components-standard-component-bigdata)
* [Saving and executing the Job](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-saving-and-executing-job-standard-component-bigdata-press)

**Related concepts**  

* [tMongoDBInput](tmongodbinput "Retrieves records from a collection in the MongoDB database and transfers them to the following component for display or storage.")

**Related reference**  

* [tMongoDBBulkLoad](tmongodbbulkload "Imports data files in different formats (CSV, TSV or JSON) into the specified MongoDB database so that the data can be further processed.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-retrieving-data-from-collection-by-advanced-queries-standard-component-bigdata-in-this -->
# Retrieving data from a collection by advanced queries

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

In this scenario, advanced MongoDB queries are used to retrieve the post by the author
Anderson.

There are such posts in the collection *blog* of the
MongoDB database *talend*:

To insert data into the database, see [Creating a collection and writing data to it](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-creating-collection-and-writing-data-to-it-standard-component-bigdata-this).

### In this section

* [Linking the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-linking-components-standard-component-bigdata-drop)
* [Configuring the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-configuring-components-standard-component-bigdata)
* [Executing the Job](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-executing-job-standard-component-bigdata-press)

**Related concepts**  

* [tMongoDBInput](tmongodbinput "Retrieves records from a collection in the MongoDB database and transfers them to the following component for display or storage.")

**Related reference**  

* [tMongoDBConnection](tmongodbconnection "Creates a connection to a MongoDB database and reuse that connection in other components.")
* [tMongoDBClose](tmongodbclose "Closes a connection to the MongoDB database.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-creating-collection-and-writing-data-to-it-standard-component-bigdata-this -->
# Creating a collection and writing data to it

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

This scenario creates the collection *blog* and
writes post data to it.

### In this section

* [Designingn the data flow](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-designingn-data-flow-standard-component-bigdata-drop)
* [Configuring the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-configuring-components-standard-component-bigdata)
* [Starting the Job](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-starting-job-standard-component-bigdata-press)

**Related concepts**  

* [tMongoDBInput](tmongodbinput "Retrieves records from a collection in the MongoDB database and transfers them to the following component for display or storage.")
* [tMongoDBOutput](tmongodboutput "Executes the action defined on the collection in the MongoDB database.")

**Related reference**  

* [tMongoDBConnection](tmongodbconnection "Creates a connection to a MongoDB database and reuse that connection in other components.")
* [tMongoDBClose](tmongodbclose "Closes a connection to the MongoDB database.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-upserting-records-in-collection-standard-component-bigdata-this -->
# Upserting records in a collection

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend products
with Big Data.

This scenario upserts the collection *blog* as an existing
record has its author changed and a new record is added. Before the upsert, the collection *blog* looks like:

```
1;Andy;Open Source Outlook;Open Source,Talend;Talend, the leader of the open source world...
2;Andy;Data Integration Overview;Data Integration,Talend;Talend, the leading player in the DI field...
3;Andy;ELT Overview;ELT,Talend;Talend, the big name in the ELT circle...
```

Such records can be inserted to the database following the instructions of
[Creating a collection and writing data to it](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-creating-collection-and-writing-data-to-it-standard-component-bigdata-this).

### In this section

* [Linking the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-linking-components-standard-component-bigdata-drop)
* [Upserting data to MongoDB](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-upserting-data-to-mongodb-standard-component-bigdata)
* [Executing the Job](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-executing-job-standard-component-bigdata-press)

**Related concepts**  

* [tMongoDBInput](tmongodbinput "Retrieves records from a collection in the MongoDB database and transfers them to the following component for display or storage.")
* [tMongoDBOutput](tmongodboutput "Executes the action defined on the collection in the MongoDB database.")

**Related reference**  

* [tMongoDBConnection](tmongodbconnection "Creates a connection to a MongoDB database and reuse that connection in other components.")
* [tMongoDBClose](tmongodbclose "Closes a connection to the MongoDB database.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbrow-tlogrow-using-mongodb-functions-to-create-collection-and-write-data-to-it-standard-component-bigdata-this -->
# Using MongoDB functions to create a collection and write data to it

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

This scenario creates the collection *blog* and writes post
data to it through the MongoDB functions.

### In this section

* [Linking the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbrow-tlogrow-linking-components-standard-component-bigdata-drop)
* [Configuring the components](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbrow-tlogrow-configuring-components-standard-component-bigdata)
* [Executing the Job](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbrow-tlogrow-executing-job-standard-component-bigdata-press)

**Related concepts**  

* [tMongoDBInput](tmongodbinput "Retrieves records from a collection in the MongoDB database and transfers them to the following component for display or storage.")

**Related reference**  

* [tMongoDBConnection](tmongodbconnection "Creates a connection to a MongoDB database and reuse that connection in other components.")
* [tMongoDBClose](tmongodbclose "Closes a connection to the MongoDB database.")
* [tMongoDBRow](tmongodbrow "Executes the commands and functions of the MongoDB database.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-configuring-components-standard-component-bigdata -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Importing data from a CSV file](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-importing-data-from-csv-file-standard-component-bigdata)
* [Validating that the CSV file is imported successfully](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-validating-that-csv-file-is-imported-successfully-standard-component-bigdata)
* [Importing data from a JSON file](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-importing-data-from-json-file-standard-component-bigdata)
* [Validating that the JSON file is imported successfully](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-validating-that-json-file-is-imported-successfully-standard-component-bigdata-repeat)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-dropping-and-linking-components-standard-component-bigdata-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: two tMongoDBBulkLoad components, two tMongoDBInput components, and two tLogRow components.
2. Connect the first tMongoDBBulkLoad to the
   first tMongoDBInput using a Trigger > OnSubjobOk link.
3. Connect the first tMongoDBInput to the
   first tLogRow using a Row > Main link.
4. Repeat the two steps above to connect the second tMongoDBBulkLoad to the second tMongoDBInput, and the second tMongoDBInput to the second tLogRow.
5. Connect the first tMongoDBInput to the
   second tMongoDBBulkLoad using a Trigger > OnSubjobOk link.
6. Label the two tLogRow components to
   better identify the data displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-saving-and-executing-job-standard-component-bigdata-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Execute the Job by pressing F6 or clicking Run on the
   Run tab.

## Results

The data from the collection *books* in the MongoDB database *bookstore* is
displayed on the console, which contains the data imported from both the CSV file
*books.csv* and the JSON file *books.json*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-configuring-components-standard-component-bigdata -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBConnection to open
   its Basic settings view.
2. From the DB Version list, select the
   MongoDB version you are using.
3. In the Server and Port fields, enter the connection details.
4. In the Database field, enter the name of the MongoDB
   database.
5. Double-click tMongoDBInput to open its
   Basic settings view.
6. Select the Use existing connection
   option.
7. In the Collection field, enter the name
   of the collection, namely *blog*.
8. Click the [...] button next to Edit schema to open the schema editor.
9. Click the [+] button to add five columns,
   namely *id*, *author*, *title*, *keywords* and *contents*, with the type as *Integer* and *String*
   respectively.
10. Click OK to close the editor.
11. The columns now appear in the left part of the Mapping area.
12. For columns *author*, *title*, *keywords* and *contents*,
    enter their parent node *post* so that the
    data can be retrieved from the correct positions.
13. In the Query box, enter the advanced
    query statement to retrieve the posts whose author is Anderson:

    ```
    "{post.author : 'Anderson'}"
    ```

    This statement requires that the sub-node of *post*, the node *author*,
    should have the value "Anderson".
14. Double-click tLogRow to open its
    Basic settings view.

    Select Table (print values in cells of a
    table) for a better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-executing-job-standard-component-bigdata-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.

   As shown above, the post by Anderson is retrieved.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbconnection-tmongodbclose-tlogrow-linking-components-standard-component-bigdata-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tMongoDBConnection, tMongoDBClose, tMongoDBInput and tLogRow
   onto the workspace.
2. Link tMongoDBConnection to tMongoDBInput using the OnSubjobOk trigger.
3. Link tMongoDBInput to tMongoDBClose using the OnSubjobOk trigger.
4. Link tMongoDBInput to tLogRow using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-configuring-components-standard-component-bigdata -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBConnection to open
   its Basic settings view.
2. From the DB Version list, select the
   MongoDB version you are using.
3. In the Server and Port fields, enter the connection details.

   In the Database field, enter the name of the MongoDB
   database.
4. Double-click tFixedFlowInput to open its
   Basic settings view.

   Select Use Inline Content (delimited
   file) in the Mode
   area.

   In the Content field, enter the data to write to the
   MongoDB database, for example:

   ```
   1;Andy;Open Source Outlook;Open Source,Talend;Talend, the leader of the open source world...
   3;Andy;ELT Overview;ELT,Talend;Talend, the big name in the ELT circle...
   2;Andy;Data Integration Overview;Data Integration,Talend;Talend, the leading player in the DI field...
   ```
5. Double-click tMongoDBOutput to open its
   Basic settings view.

   Select the Use existing connection and
   Drop collection if exist check
   boxes.

   In the Collection field, enter the name
   of the collection, namely *blog*.
6. Click the [...] button next to Edit schema to open the schema editor.
7. Click the [+] button to add five columns
   in the right part, namely *id*, *author*, *title*, *keywords* and
   *contents*, with the type as *Integer* and *String* respectively.

   Click
   to copy all the columns to the input table.

   Click Ok to close the editor.
8. The columns now appear in the left part of the Mapping area.

   For columns *author*, *title*, *keywords* and
   *contents*, enter their parent node
   *post*. By doing so, those nodes reside
   under the node *post* in the MongoDB
   collection.
9. Double-click tMongoDBInput to open its
   Basic settings view.

   Select the Use existing connection check
   box.

   In the Collection field, enter the name
   of the collection, namely *blog*.
10. Click the [...] button next to Edit schema to open the schema editor.
11. Click the [+] button to add five columns,
    namely *id*, *author*, *title*, *keywords* and *contents*, with the type as *Integer* and *String*
    respectively.

    Click OK to close the editor.
12. The columns now appear in the left part of the Mapping area.

    For columns *author*, *title*, *keywords* and *contents*,
    enter their parent node *post* so that the
    data can be retrieved from the correct positions.
13. In the Sort by area, click the [+] button to add one line and enter *id* under Column.

    Select asc from the Order asc or desc? column to the right of the *id* column. This way, the retrieved records will
    appear in ascending order of the *id*
    column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-designingn-data-flow-standard-component-bigdata-drop -->
# Designingn the data flow

Last updated: 9/30/2026

## Procedure

1. Drop tMongoDBConnection, tFixedFlowInput, tMongoDBOutput, tMongoDBClose, tMongoDBInput and tLogRow
   onto the workspace.
2. Rename tFixedFlowInput as blog\_post\_data, tMongoDBOutput as write\_data\_to\_collection, tMongoDBInput as read\_data\_from\_collection and tLogRow as show\_data\_from\_collection.
3. Link tMongoDBConnection to tFixedFlowInput using the OnSubjobOk trigger.
4. Link tFixedFlowInput to tMongoDBOutput using a Row > Main
   connection.
5. Link tFixedFlowInput to tMongoDBInput using the OnSubjobOk trigger.
6. Link tMongoDBInput to tMongoDBClose using the OnSubjobOk trigger.
7. Link tMongoDBInput to tLogRow using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-starting-job-standard-component-bigdata-press -->
# Starting the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.
3. Switch to the database *talend* and read data from the
   collection *blog* in the MongoDB command
   line client. You can find that *author*,
   *title*, *keywords* and *contents* all
   reside under the node *post*. Meanwhile,
   the records are stored in the same order as the source input.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-executing-job-standard-component-bigdata-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.

   As shown above, the 3rd record has its author updated and the 4th record
   is inserted.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-linking-components-standard-component-bigdata-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tMongoDBConnection, tFixedFlowInput, tMongoDBOutput, tMongoDBClose, tMongoDBInput and tLogRow
   from the Palette onto the design
   workspace.
2. Rename tFixedFlowInput as blog\_post\_data, tMongoDBOutput as write\_data\_to\_collection, tMongoDBInput as read\_data\_from\_collection and tLogRow as show\_data\_from\_collection.
3. Link tMongoDBConnection to tFixedFlowInput using the OnSubjobOk trigger.
4. Link tFixedFlowInput to tMongoDBOutput using a Row > Main
   connection.
5. Link tFixedFlowInput to tMongoDBInput using the OnSubjobOk trigger.
6. Link tMongoDBInput to tMongoDBClose using the OnSubjobOk trigger.
7. Link tMongoDBInput to tLogRow using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodboutput-tlogrow-upserting-data-to-mongodb-standard-component-bigdata -->
# Upserting data to MongoDB

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBConnection to open
   its Basic settings view.
2. From the DB Version list, select the
   MongoDB version you are using.
3. In the Server and Port fields, enter the connection details.

   In the Database field, enter the name of the MongoDB
   database.
4. Double-click tFixedFlowInput to open its
   Basic settings view.

   Select Use Inline Content (delimited
   file) in the Mode
   area.

   In the Content field, enter the data for upserting the
   MongoDB database, for example:

   ```
   1;Andy;Open Source Outlook;Open Source,Talend;Talend, the leader of the open source world...
   2;Andy;Data Integration Overview;Data Integration,Talend;Talend, the leading player in the DI field...
   3;Anderson;ELT Overview;ELT,Talend;Talend, the big name in the ELT circle...
   4;Andy;Big Data Bang;Big Data,Talend;Talend, the driving force for Big Data applications...
   ```

   As shown above, the 3rd record has its author changed and the 4th record
   is new.
5. Double-click tMongoDBOutput to open its
   Basic settings view.

   Select the Use existing connection and
   Die on error check boxes.

   In the Collection field, enter the name
   of the collection, namely *blog*.

   Select Upsert from the Action on data list.
6. Click the [...] button next to Edit schema to open the schema editor.
7. Click the [+] button to add five columns
   in the right part, namely *id*, *author*, *title*, *keywords* and
   *contents*, with the type as *Integer* and *String* respectively.

   Click
   to copy all the columns to the input table.

   Click Ok to close the editor.
8. In the Advanced Settings view, select the
   Generate JSON Document check
   box.

   Select the Remove root node check box.
9. Click the [...] button next to Configure JSON Tree to open the configuration
   interface.
10. Right-click the node *rootTag* and select
    Add Sub-element from the contextual
    menu.

    In the dialog box that appears, type in *data* for the Data
    node:

    Click OK to close the window.

    Repeat this operation to define *query*
    as the Query node.

    Right-click the node *data* and select
    Set As Loop Element from the contextual
    menu.

    Information noteWarning:

    These nodes are mandatory for update and upsert actions. They are
    intended to enable the update and upsert actions though will not be
    stored in the database.
11. Select all the columns under the Schema
    list and place them to the *data* node. 

    In the window that appears, select Create as sub-element of target node.

    Click OK to close the
    window.

    Repeat this operation to drop the *id* column
    from the Schema list under the *Query* node.
12. Right-click the node *id* under *data* and select Add Attribute from the contextual menu.

    In the dialog box that appears, type in *type* as the attribute name.

    Click OK to close the window.

    Right-click the node *@type* under
    *id* and select Set A Fix Value from the contextual menu.

    In the dialog box that appears, type in *integer* as the attribute value, ensuring the *id* values are stored as integers in the
    database.

    Click OK to close the window.

    Repeat this operation to set this attribute for the *id* node under *Query*.

    Click OK to close the JSON Tree
    configuration interface.
13. Double-click tMongoDBInput to open its
    Basic settings view.

    Select the Use existing connection check
    box.

    In the Collection field, enter the name
    of the collection, namely *blog*.

    Click the [...] button next to Edit schema to open the schema editor.

    Click the [+] button to add five columns,
    namely *id*, *author*, *title*, *keywords* and *contents*, with the type as *Integer* and *String*
    respectively.

    Click OK to close the editor.

    The columns now appear in the left part of the Mapping area.

    For columns *author*, *title*, *keywords* and *contents*,
    enter their parent node *post* so that the
    data can be retrieved from the correct positions.
14. Double-click tLogRow to open its
    Basic settings view.

    In the Mode area, select Table (print values in cells of a table for
    better display.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbrow-tlogrow-configuring-components-standard-component-bigdata -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBConnection to open
   its Basic settings view.
2. From the DB Version list, select the
   MongoDB version you are using.
3. In the Server and Port fields, enter the connection details.

   In the Database field, enter the name of the MongoDB
   database.
4. Double-click tFixedFlowInput to open its
   Basic settings view.

   Select Use Inline Content (delimited
   file) in the Mode
   area.

   In the Content field, enter the data to write to the
   MongoDB database, for example:

   ```
   Andy;Open Source Outlook;Open Source,Talend;Talend, the leader of the open source world...
   Andy;Data Integration Overview;Data Integration,Talend;Talend, the leading player in the DI field...
   Andy;ELT Overview;ELT,Talend;Talend, the big name in the ELT circle...
   ```
5. Double-click tMongoDBRow to open its
   Basic settings view.

   Select the Use existing connection check
   box.

   In the Function field, enter the MongoDB function to
   create the collection *blog* and insert
   data to it:

   ```
   "function(author,title,keywords,contents){
   return db.blog.save(
   {author:author,title:title,keywords:keywords,contents:contents}
   );

   }"
   ```
6. Click the [...] button next to Edit schema to open the schema editor.
7. Click the [+] button to add four columns
   in the right part, namely *author*,
   *title*, *keywords* and *contents*,
   with the type of *String*.

   Click
   to copy all the columns to the input table.

   Click OK to close the editor.
8. In the Parameters value table, click the
   [+] button to add four lines and enter
   the values in sequence: *row1.author*,
   *row1.title*, *row1.keywords* and *row1.contents*. By doing so, data of *row1* will be transferred to the parameters defined in the
   function.
9. Double-click tMongoDBInput to open its
   Basic settings view.

   Select the Use existing connection check
   box.

   In the Collection field, enter the name
   of the collection, namely *blog*.
10. Click the [...] button next to Edit schema to open the schema editor.
11. Click the [+] button to add four columns,
    namely *author*, *title*, *keywords* and
    *contents*, with the type as *String*.

    Click OK to close the editor.
12. Double-click tLogRow to open its
    Basic settings view.

    In the Mode area, select Table (print values in cells of a table for
    better display.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbrow-tlogrow-executing-job-standard-component-bigdata-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbrow-tlogrow-linking-components-standard-component-bigdata-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tMongoDBConnection, tFixedFlowInput, tMongoDBRow, tMongoDBClose,
   tMongoDBInput and tLogRow onto the workspace.
2. Rename tFixedFlowInput as blog\_post\_data, tMongoDBRow as write\_data\_to\_collection, tMongoDBInput as read\_data\_from\_collection and tLogRow as show\_data\_from\_collection.
3. Link tMongoDBConnection to tFixedFlowInput using the OnSubjobOk trigger.
4. Link tFixedFlowInput to tMongoDBRow using a Row > Main
   connection.
5. Link tFixedFlowInput to tMongoDBInput using the OnSubjobOk trigger.
6. Link tMongoDBInput to tMongoDBClose using the OnSubjobOk trigger.
7. Link tMongoDBInput to tLogRow using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-importing-data-from-csv-file-standard-component-bigdata -->
# Importing data from a CSV file

Last updated: 9/30/2026

## Procedure

1. Double-click the first tMongoDBBulkLoad
   component to open its Basic settings view
   in the Component tab.
2. In the MongoDB directory field, type in
   the MongoDB home directory. In this example, it is *D:/MongoDB*.
3. In the Server and Port fields, fill in the information required for the
   connection to MongoDB. In this example, type in *localhost* and *27017*.
4. In the Database field,
   type in the database to import data to, *bookstore* in this
   example.
5. In the Collection field, type in the collection to
   import data to, *books* in this example.
6. Select the Drop collection if exist check
   box to remove the specified collection if it already exists.
7. Browse to the desired data file from which you want to import data. In
   this example, it is *D:/Input/books.csv*,
   which is a standard CSV file containing four columns: *id*, *title*,
   *author*, and *category*.id,title,author,category
   1,Computer Networks,Larry Peterson,Computer Science
   2,David Copperfield,Charles Dickens,Language&Literature
   3,Life of Pi,Yann Martel,Language&Literature
8. Select CSV from the File type list.
9. Select Insert from the Action on data list.
10. Select the First line is
    header check box to use the first line in the CSV file as a
    header.
11. Select the Ignore blanks check box to ignore the blank
    fields (if any) in the CSV file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-importing-data-from-json-file-standard-component-bigdata -->
# Importing data from a JSON file

Last updated: 9/30/2026

## Procedure

1. Double-click the second tMongoDBBulkLoad component to open its Basic settings view in the Component tab.
2. In the MongoDB directory field, type in
   the MongoDB home directory. In this example, it is *D:/MongoDB*.
3. In the Server and Port fields, fill in the information required for the
   connection to MongoDB. In this example, type in *localhost* and *27017*.
4. In the Database field, type in the target
   database to import data, *bookstore* in
   this example.
5. In the Collection field, type in the target collection
   to import data, *books* in this example
6. Browse to the desired data file from which you want to import data. Here,
   select *books.json*.{
   "id": "4",
   "title": "Les Miserables",
   "author": "Victor Hugo",
   "category": "Language&Literature"
   }
   {
   "id": "5",
   "title": "Advanced Database Systems",
   "author": "Carlo Zaniolo",
   "category": "Database"
   }
7. Select *JSON* from the File type list.
8. Select *Insert* from the Action on data list.
9. Click the Advanced
   settings tab to define the additional arguments as needed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-validating-that-csv-file-is-imported-successfully-standard-component-bigdata -->
# Validating that the CSV file is imported successfully

Last updated: 9/30/2026

## Procedure

1. Double-click the first tMongoDBInput component to open its Basic settings view in the Component tab.
2. From the DB Version list, select the
   MongoDB version you are using.
3. In the Server and Port fields, fill in the information required for the
   connection to MongoDB. In this example, type in *localhost* and *27017*.
4. In the Database field, type in the
   database from which the data will be read, *bookstore* in this example.
5. In the Collection field, type in the
   collection from which the data will be read, *books* in this example.
6. Click Edit schema to
   define the data structure to be read from the MongoDB collection.
7. In the Mapping table, the Column field is automatically populated with the
   defined schema. You do not need to fill in the Parent
   node path column.
8. Double-click the first tLogRow component to open its Basic
   settings view in the Component tab.
9. In the Mode area, select Table (print values in cells of a table).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-validating-that-json-file-is-imported-successfully-standard-component-bigdata-repeat -->
# Validating that the JSON file is imported successfully

Last updated: 9/30/2026

## Procedure

1. Repeat Step 1 through Step 7 described in the procedure [Validating that the CSV file is imported successfully](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-validating-that-csv-file-is-imported-successfully-standard-component-bigdata) to configure the second tMongoDBInput component.
2. Repeat Step 8 through Step 9 described in the procedure [Validating that the CSV file is imported successfully](/talend/en-US/components/8.0/mongodb/tmongodbinput-tmongodbbulkload-tlogrow-tmongodbbulkload-tlogrow-validating-that-csv-file-is-imported-successfully-standard-component-bigdata) to configure the second tLogRow component.
