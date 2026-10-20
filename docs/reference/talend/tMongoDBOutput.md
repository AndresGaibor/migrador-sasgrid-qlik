<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput · versión 8.0 -->
# tMongoDBOutput

Last updated: 9/30/2026

Executes the action defined on the collection in the MongoDB database.

tMongoDBOutput
inserts, updates, upserts or deletes documents in a MongoDB database collection based on
the incoming flow from the preceding component in the Job.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tMongoDBOutput Standard properties](/talend/en-US/components/8.0/mongodb/tmongodboutput-standard-properties)
* [tMongoDBOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/mongodb/tmongodboutput-properties-for-apache-spark-batch)
* [tMongoDBOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/mongodb/tmongodboutput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Creating a collection and writing data to it](tmongodbinput-tmongodboutput-tlogrow-creating-collection-and-writing-data-to-it-standard-component-bigdata-this)
* [Inserting records to a MongoDB collection using a dynamic schema](inserting-records-to-a-mongodb-collection-using-dynamic-schema)
* [Reading and writing data in MongoDB using a Spark Streaming Job](tmongodblookupinput-tmongodbconfiguration-ts3configuration-reading-and-writing-data-in-mongodb-using-spark-streaming-job-spark-stream-component-in-this)
* [Upserting records in a collection](tmongodbinput-tmongodboutput-tlogrow-upserting-records-in-collection-standard-component-bigdata-this)
* [Writing and reading data from MongoDB using a Spark Batch Job](tmongodboutput-tmongodbinput-ts3configuration-writing-and-reading-data-from-mongodb-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-properties-for-apache-spark-batch -->
# tMongoDBOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMongoDBOutput running in the Spark Batch Job framework.

The Spark Batch
tMongoDBOutput component belongs to the Databases family.

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
| Collection | Enter the name of the collection to be used.  A MongoDB collection is the equivalent of an RDBMS table and contains documents. |
| Set write concern | Select this check box to set the level of acknowledgement requested for write operations. Then you need to select the level of this operation.  For further information, see the related MongoDB documentation on <http://docs.mongodb.org/manual/core/write-concern/>. |
| Action on data | The following operations are available:   * Insert: insert documents. * Set: modifies the existing fields of an existing   document and appends a field if it does not exist in this document.  If you need to apply this action on all the documents in the collection to be   used, select the Update all document check box that   is displayed; otherwise, only the first document is updated.  If you need to append a new field to a parent node you specify in the Mapping table, select Append to   parent. If you leave this check box clear, this new field is appended   to the root of the document being updated. * Upsert with set: inserts a document if it does   not exist otherwise it applies the same rules as Set  If you need to apply this action on all the documents in the collection to be   used, select the Update all document check box that   is displayed; otherwise, only the first document is updated.  If you need to append a new field to a parent node you specify in the Mapping table, select Append to   parent. If you leave this check box clear, this new field is appended   to the root of the document being updated. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced Hadoop MongoDB properties | Add properties to define extra operations you need tMongoDBOutput to perform when writing data.  The available properties are listed and explained in [MongoDB Connector for Hadoop](https://github.com/mongodb/mongo-hadoop/wiki/Configuration-Reference). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tMongoDBConfiguration component present in the same Job to connect to a MongoDB database. You need to drop a tMongoDBConfiguration component alongside this component and configure the Basic settings of this component to use tMongoDBConfiguration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-standard-properties -->
# tMongoDBOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure
tMongoDBOutput running in the
Standard Job framework.

The
Standard
tMongoDBOutput component belongs to the
Big Data and the
Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| DB Version | Select the database version you want to use from the drop-down list This field is available when the Use existing connection check box is not selected. |
| Use connection string | Select this option to establish a connection using a MongoDB Atlas URI. Enter the URI in the field to the right. See [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) for related information.  This option is available when you select `MongoDB 4.4.X and later` from the DB Version drop-down list.  Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use replica set address | Select this check box to show the Replica address table. In the Replica address table, you can define multiple MongoDB database servers for failover.  Available when the Use existing connection check box is not selected. |
| Server and Port | Enter the IP address and listening port of the database server. These fields are available when the Use existing connection or Use replica set address check box are not selected. |
| Database | Enter the name of the database. |
| Use SSL connection (Configure the SSL authentication in tSetKeystore or in Studio preferences) | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Set write concern | Select this check box to set the level of acknowledgement requested for write operations. Then you need to select the level of this operation.  For further information, see the related MongoDB documentation on <http://docs.mongodb.org/manual/core/write-concern/>. |
| Bulk write | Select this check box to insert, update or remove data in bulk. Note this feature is available only when the version of MongoDB you are using is 2.6+.  Then you need to select Ordered or Unordered to define how the MongoDB database processes the data sent by Talend Studio.  * If you select Ordered,   MongoDB processes the queries sequentially. * If you select Unordered,   MongoDB optimizes the bulk write operations without keeping the order in which the   individual operations were inserted in the bulk write.  In the Bulk write size field, enter the size of each query group to be processed by MongoDB. In the documentation of MongoDB, some restrictions and expected behaviors as to this size are explained. You can find the details on <http://docs.mongodb.org/manual/core/bulk-write-operations/>. |
| Required authentication | Select this check box to enable the database authentication. Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This field is available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Collection | Enter the name of the collection in the MongoDB database. |
| Drop collection if exist | Select this check box to drop the collection if it already exists. |
| Action on data | The following operations are available:  * Insert: insert documents. * Set: modifies the existing fields of an existing   document and appends a field if it does not exist in this document.  If you need to apply this action on all the documents in the collection to be   used, select the Update all document check box that   is displayed; otherwise, only the first document is updated. * Update: replaces the existing documents with the   incoming data but keeps the technical ID of these documents. * Upsert: inserts a document if it does not exist   otherwise it applies the same rules as Update. * Upsert with set: inserts a document if it does   not exist otherwise it applies the same rules as Set  If you need to apply this action on all the documents in the collection to be   used, select the Update all document check box that   is displayed; otherwise, only the first document is updated. * Delete: delete documents.  If you need to apply this action on all the documents in the collection to be   used, selected the Delete all documents check box that is   displayed, otherwise, only one documented is deleted. |
| Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  This component supports dynamic schema when inserting documents to a collection. To use the dynamic schema feature, make sure the schema contains only one column, with the DB column set to `*` and Type set to `String` (if the input type is String) or `Object` (if the input type is Object).  Information noteNote:  * The dynamic schema feature is available only when `Insert` is selected from the Action on data drop-down list. * The dynamic schema feature is available only when you have installed the   8.0.1-R2022-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ```  Updatable and Insertable: As the name applies, specify whether or not a field can be updated and inserted. These two columns appear when `Upsert with set` is selected from the Action on data drop-down list.  Not available when the Generate JSON Document check box is selected in Advanced settings.  Select the Remove Null Field checkbox to avoid having a column in the output when the value is null. For example with the following table:  ``` id    name a   null b   Jane ```  * If you select the checkbox, the output will read as   follows:    ```   {"id":"a"}   {"id":"b","name":"Jane"}   ``` * If you leave the checkbox clear, the output will read as   follows:    ```   {"id":"a","name":null}   {"id":"b","name":"Jane"}   ``` |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Generate JSON Document | Select this check box for JSON configuration: Configure JSON Tree: click the [...] button to open the interface for JSON tree configuration. For more information, see [Configuring a JSON Tree](/talend/en-US/components/8.0/processing/configuring-a-json-tree). Information noteNote: You can adapt the JSON objects into BSON objects by adding \_\_DOLLAR\_\_ before the object (for example, $oid and $date become respectively \_\_DOLLAR\_\_oid and \_\_DOLLAR\_\_date). The MongoDB specific objects can then be read and not considered as character string.  Create empty element if needed: If the Related Column in the XML tree editor has null values, or if no column is associated with the XML node, this option creates an open/close tag in the expected place. This check box is selected by default.  Ignore service attributes for empty elements: Select this option to prevent the component from generating a node if the input node is null but has service attributes (such as @type, @class, and @array). This option is available when the Create empty element if needed option is not selected.  Group by: click the [+] button to add lines and choose the input columns for grouping the records.  Remove root node: select this check box to remove the root node.  Data node and Query node (available for Update and Upsert actions): type in the name of data node and query node configured on the JSON tree.  Information noteWarning: These nodes are mandatory for update and upsert actions. They are intended to enable the update and upsert actions though will not be stored in the database.  Node (available for Set and Upsert with set actions): specify the update operations for specific JSON nodes. To add an update operation, click the plus button at the bottom of this field, enter the update operator or select the update operator from the drop-down list in the Node type column, and enter the node name in double quotation marks in the Node reference column. See [Update Operators](https://docs.mongodb.com/v4.4/reference/operator/update/) for information about update operators. Information noteNote: This field is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | * tMongoDBOutput executes the action   defined on the collection in the MongoDB database based on the flow incoming   from the preceding component in the Job. * tMongoDBOutput supports [Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/) capabilities,   you can use it to perform actions on vector embeddings. For more information   on vector embeddings, see [the corresponding MongoDB   documentation](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/#std-term-vector-embeddings). |
| Limitation | Information noteNote:  * The "multi" parameter, which allows to update multiple   documents at a time, is not supported. Therefore, if two documents have   the same key, the first is always updated, but the second never will. * For the update operation, the key cannot be a JSON   array. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-writing-and-reading-data-from-mongodb-using-spark-batch-job-spark-batch-component-in-this -->
# Writing and reading data from MongoDB using a Spark Batch Job

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend products
with Big Data.

In this scenario, you create a Spark Batch Job to write data about some movie
directors into the MongoDB *default* database and then read the data from
this database.

The sample data about movie directors reads as
follows:

```
1;Gregg Araki	
2;P.J. Hogan 
3;Alan Rudolph 
4;Alex Proyas
5;Alex Sichel
```

This data contains the names of these directors and the ID numbers distributed
to them.

Note that the sample data is created for demonstration purposes only.

tHDFSConfiguration is used in this scenario by Spark to connect
to the HDFS system where the jar files dependent on the Job are transferred.

In the Spark
Configuration tab in the Run
view, define the connection to a given Spark cluster for the whole Job. In
addition, since the Job expects its dependent jar files for execution, you must
specify the directory in the file system to which these jar files are
transferred so that Spark can access these files:

* Yarn mode (Yarn client or Yarn cluster):
  + When using Google Dataproc, specify a bucket in the
    Google Storage staging bucket
    field in the Spark configuration
    tab.
  + When using HDInsight, specify the blob to be used for Job
    deployment in the Windows Azure Storage
    configuration area in the Spark
    configuration tab.
  + When using Altus, specify the S3 bucket or the Azure
    Data Lake Storage for Job deployment in the Spark
    configuration tab.
  + When using on-premises distributions, use
    the configuration component corresponding to the file system
    your cluster is using. Typically, this system is HDFS and so
    use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
* Standalone mode: use the
  configuration component corresponding to the file system your cluster is
  using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

  If you are using Databricks without any configuration component present
  in your Job, your business data is written directly in DBFS (Databricks
  Filesystem).

Prerequisite: ensure that the Spark cluster and the
MongoDB database to be used have been properly installed and are running.

To replicate this scenario, proceed as follows:

### In this section

* [Linking the components](/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-linking-components-spark-batch-component-in)
* [Selecting the Spark mode](/talend/en-US/components/8.0/mongodb/selecting-spark-mode-spark-batch?id=3436)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/mongodb/configuring-connection-to-file-system-to-be-used-by-spark?id=3437)
* [Configuring the connection to the MongoDB database to be used by Spark](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-configuring-connection-to-mongodb-database-to-be-used-by-spark?id=3438)
* [Loading the sample data](/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-loading-sample-data-spark-batch-component)
* [Writing data to MongoDB](/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-writing-data-to-mongodb-spark-batch-component)
* [Reading data from MongoDB](/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-reading-data-from-mongodb-spark-batch-component)
* [Executing the Job](/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-executing-job-spark-batch-component-then-you)

**Related concepts**  

* [tMongoDBInput](tmongodbinput "Retrieves records from a collection in the MongoDB database and transfers them to the following component for display or storage.")
* [tMongoDBOutput](tmongodboutput "Executes the action defined on the collection in the MongoDB database.")
* [tMongoDBConfiguration](tmongodbconfiguration "Stores connection information and credentials to be reused by other MongoDB components.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tS3Configuration](/talend/en-US/components/8.0/amazon-s3/ts3configuration)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-executing-job-spark-batch-component-then-you -->
# Executing the Job

Last updated: 9/30/2026

## About this task

Then you can run this Job.

The tLogRow component is used to present the
execution result of the Job.

## Procedure

1. Double-click the tLogRow component to open
   the Component view.
2. Select the Table radio button to present the
   result in a table.
3. Press F6 to run this Job.

## Results

Once done, in the console of the Run view, you can
check the execution result.

Note that you can manage the level of the execution information to be outputted in
this console by selecting the log4jLevel check box in
the Advanced settings tab and then selecting the level
of the information you want to display.

For more information on the log4j logging levels, see the Apache documentation at <http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html>.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-linking-components-spark-batch-component-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective of Talend Studio,
   create an empty Spark Batch Job from the Job
   Designs node in the Repository
   tree view.
2. In the workspace, enter the name of the component to be used and select this
   component from the list that appears. In this scenario, the components are
   tHDFSConfiguration, tMongoDBConfiguration, tFixedFlowInput, tMongoDBOutput,
   tMongoDBInput and tLogRow.

   The tFixedFlowInput components are used to
   load the sample data into the data flow. In the real-world practice, you can use
   other components such as tFileInputDelimited,
   alone or even with a tMap, in the place of
   tFixedFlowInput to design a sophisticated
   process to prepare your data to be processed.
3. Connect tFixedFlowInput to tMongoDBOutput using the Row >
   Main link.
4. Connect tMongoDBInput to tLogRow using the Row >
   Main link.
5. Connect tFixedFlowInput to tMongoDBInput using the Trigger >
   OnSubjobOk link.
6. Leave tHDFSConfiguration and tMongoDBConfiguration alone without any
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-loading-sample-data-spark-batch-component -->
# Loading the sample data

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowIput component to
   open its Component view.
2. Click the [...] button next to Edit schema to open the schema editor.
3. Click the [+] button to add the schema
   columns as shown in this image.
4. Click OK to validate these changes and accept
   the propagation prompted by the pop-up dialog box.
5. In the Mode area, select the Use Inline Content radio button and paste the
   above-mentioned sample data about movie directors into the Content field that is displayed.
6. In the Field separator field, enter a
   semicolon (*;*).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-reading-data-from-mongodb-spark-batch-component -->
# Reading data from MongoDB

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBInput to open its
   Component view.
2. Click the [...] button next to Edit schema to open the schema editor.
3. Click the [+] button to add the schema
   columns for output as shown in this image.

   If you want to extract the technical ID of each document, add a column called
   *\_id* to the schema. In this example, this
   column is added. These technical IDs were generated at random by MongoDB when
   the sample data was written to the database.
4. In the Collection field, enter the name of
   the collection from which you need to read data. In this example, it is the
   *director* one used previously in tMongoDBOutput.
5. In the Mapping table, the three output
   columns have been automatically added. You need to add the parent nodes they
   belong to in the MongoDB documents. In this example, enter, within double
   quotation marks, *person* in the Parent node path column for the *id* and the *name* columns and leave
   the *\_id* column as is, meaning that the
   *\_id* field is at the root of each
   document.

   The tMongDBInput component parses the
   extracted documents according to this mapping and writes the data in the
   corresponding columns.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodboutput-tmongodbinput-ts3configuration-writing-data-to-mongodb-spark-batch-component -->
# Writing data to MongoDB

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBOutput to open its
   Component view.
2. If this component does not have the same schema of the preceding
   component, a warning icon appears. In this situation, click the Sync columns button to retrieve the schema from the
   preceding one and once done, the warning icon disappears.
3. In the Collection field, enter the name of
   the collection to which you need to write data. If this collection does not
   exist, it will be automatically created at runtime.
4. From the Action on data list, select the
   operation to be performed on the data. In this example, select Insert, which creates documents in MongoDB whether
   these documents already exist or not and in either case, generates a new
   technical ID for each of the new documents.
5. In the Mapping table, the *id* and the *name*
   columns have been automatically added. You need to define how the data from
   these two columns should be transformed into a hierarchical construct in
   MongoDB.

   In this example, enter, within double quotation marks, *person* in the Parent node path
   column for each row. This way, each director record is added to a node called
   *person*. If you leave this Parent node path column empty, these records are added to
   the root of each document.
