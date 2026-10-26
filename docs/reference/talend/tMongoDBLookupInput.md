<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmongodblookupinput · versión 8.0 -->
# tMongoDBLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a database query with a strictly defined order which must correspond to
the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tMongoDBLookupInput properties for Apache Spark Streaming

These properties are used to configure tMongoDBLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tMongoDBLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| MongoDB configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   If a column in the database is a JSON document and you need to read the entire document, put an asterisk (\*) in the DB column column, without quotation marks around. |
| Collection | Enter the name of the collection to be used.  A MongoDB collection is the equivalent of an RDBMS table and contains documents. |
| Set read preference | Select this check box and from the Read preference drop-down list that is displayed, select the member to which you need to direct the read operations.  If you leave this check box clear, the Job uses the default Read preference, that is to say, uses the primary member in a replica set.  For further information, see MongoDB's documentation about Replication and its Read preferences. |
| Query | Specify the query statement to select documents from the collection specified in the Collection field.  For example ``` "{'customer_id':" + row1.customer_id +"}" ```  In this code, *row1* is not the label of the link to tMongoDBLookupInput, but represents the main row entering into tMap.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |
| Limit | Enter the maximum number of records to be retrieved. |

## Advanced settings

| Properties | Description |
| --- | --- |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tMongoDBConfiguration component present in the same Job to connect to a MongoDB database. You need to drop a tMongoDBConfiguration component alongside this component and configure the Basic settings of this component to use tMongoDBConfiguration.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |

**Related concepts**  

* [Reading and writing data in MongoDB using a Spark Streaming Job](tmongodblookupinput-tmongodbconfiguration-ts3configuration-reading-and-writing-data-in-mongodb-using-spark-streaming-job-spark-stream-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmongodblookupinput -->
# tMongoDBLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a database query with a strictly defined order which must correspond to
the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tMongoDBLookupInput properties for Apache Spark Streaming

These properties are used to configure tMongoDBLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tMongoDBLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| MongoDB configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   If a column in the database is a JSON document and you need to read the entire document, put an asterisk (\*) in the DB column column, without quotation marks around. |
| Collection | Enter the name of the collection to be used.  A MongoDB collection is the equivalent of an RDBMS table and contains documents. |
| Set read preference | Select this check box and from the Read preference drop-down list that is displayed, select the member to which you need to direct the read operations.  If you leave this check box clear, the Job uses the default Read preference, that is to say, uses the primary member in a replica set.  For further information, see MongoDB's documentation about Replication and its Read preferences. |
| Query | Specify the query statement to select documents from the collection specified in the Collection field.  For example ``` "{'customer_id':" + row1.customer_id +"}" ```  In this code, *row1* is not the label of the link to tMongoDBLookupInput, but represents the main row entering into tMap.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |
| Limit | Enter the maximum number of records to be retrieved. |

## Advanced settings

| Properties | Description |
| --- | --- |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tMongoDBConfiguration component present in the same Job to connect to a MongoDB database. You need to drop a tMongoDBConfiguration component alongside this component and configure the Basic settings of this component to use tMongoDBConfiguration.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |

**Related concepts**  

* [Reading and writing data in MongoDB using a Spark Streaming Job](tmongodblookupinput-tmongodbconfiguration-ts3configuration-reading-and-writing-data-in-mongodb-using-spark-streaming-job-spark-stream-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmongodblookupinput-tmongodbconfiguration-ts3configuration-reading-and-writing-data-in-mongodb-using-spark-streaming-job-spark-stream-component-in-this -->
# Reading and writing data in MongoDB using a Spark Streaming Job

Last updated: 9/30/2026

This scenario applies only to Talend Real-Time Big Data Platform and
Talend Data Fabric.

In this scenario, you create a Spark Streaming Job to extract data about
given movie directors from MongoDB, use this data to filter and complete movie
information and then write the result into a MongoDB collection.

The sample data about movie directors reads as
follows:

```
1;Gregg Araki	
2;P.J. Hogan 
3;Alan Rudolph 
4;Alex Proyas
5;Alex Sichel
```

This data contains the names of these directors and the ID numbers
distributed to them.

The structure of this data in MongoDB reads as
follows:

```
{ "_id" : ObjectId("575546da3b1c7e22bc7b2189"), "person" : { "id" : 3, "name" : "Alan Rudolph" } }
{ "_id" : ObjectId("575546da3b1c7e22bc7b218b"), "person" : { "id" : 4, "name" : "Alex Proyas" } }
{ "_id" : ObjectId("575546da3b1c7e22bc7b218c"), "person" : { "id" : 5, "name" : "Alex Sichel" } }
{ "_id" : ObjectId("575546da3b1c7e22bc7b2188"), "person" : { "id" : 1, "name" : "Gregg Arakit" } }
{ "_id" : ObjectId("575546da3b1c7e22bc7b218a"), "person" : { "id" : 2, "name" : "P.J. Hogan" } }
```

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

Prerequisites:

* The Spark cluster and the MongoDB database to be used have
  been properly installed and are running.
* The above-mentioned data has been loaded in the MongoDB
  collection to be used.

To replicate this scenario, proceed as follows:

### In this section

* [Linking the components](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-linking-components-spark-stream-component-in)
* [Selecting the Spark mode](/talend/en-US/components/8.0/mongodb/selecting-spark-mode-spark-batch?id=3410)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/mongodb/configuring-connection-to-file-system-to-be-used-by-spark?id=3412)
* [Configuring the connection to the MongoDB database to be used by Spark](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-configuring-connection-to-mongodb-database-to-be-used-by-spark?id=3413)
* [Loading the movie data](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-loading-movie-data-spark-stream-component)
* [Extracting director data from MongoDB](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-extracting-director-data-from-mongodb-spark-stream-component)
* [Configuring the transformation in tMap](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-configuring-transformation-in-tmap-spark-stream-component)
* [Writing processed data to MongoDB](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-writing-processed-data-to-mongodb-spark-stream-component)
* [Writing rejected data to tLogRow](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-writing-rejected-data-to-tlogrow-spark-stream-component)
* [Executing the Job](/talend/en-US/components/8.0/mongodb/tmongodblookupinput-tmongodbconfiguration-ts3configuration-executing-job-spark-stream-component-then-you)

**Related concepts**  

* [tMongoDBOutput](tmongodboutput "Executes the action defined on the collection in the MongoDB database.")
* [tMongoDBConfiguration](tmongodbconfiguration "Stores connection information and credentials to be reused by other MongoDB components.")

**Related reference**  

* [tMongoDBLookupInput (deprecated)](tmongodblookupinput "Executes a database query with a strictly defined order which must correspond to the schema definition.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tS3Configuration](/talend/en-US/components/8.0/amazon-s3/ts3configuration)
