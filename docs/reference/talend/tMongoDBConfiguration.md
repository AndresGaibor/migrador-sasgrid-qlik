<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbconfiguration · versión 8.0 -->
# tMongoDBConfiguration

Last updated: 9/30/2026

Stores connection information and credentials to be reused by other MongoDB
components.

You configure the connection to a MongoDB database in tMongoDBConfiguration and configure the other
MongoDB components to reuse this configuration. At runtime, the Spark
executors read this configuration in order to connect to MongoDB.

### In this section

* [tMongoDBConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/mongodb/tmongodbconfiguration-properties-for-apache-spark-batch)
* [tMongoDBConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/mongodb/tmongodbconfiguration-properties-for-apache-spark-streaming)

**Related concepts**  

* [Reading and writing data in MongoDB using a Spark Streaming Job](tmongodblookupinput-tmongodbconfiguration-ts3configuration-reading-and-writing-data-in-mongodb-using-spark-streaming-job-spark-stream-component-in-this)
* [Writing and reading data from MongoDB using a Spark Batch Job](tmongodboutput-tmongodbinput-ts3configuration-writing-and-reading-data-from-mongodb-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbconfiguration-properties-for-apache-spark-batch -->
# tMongoDBConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMongoDBConfiguration running in the Spark Batch Job framework.

The Spark Batch
tMongoDBConfiguration component belongs to the Databases and Databases NoSQL families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| DB Version | Select the version of the MongoDB database you need to connect to. |
| Use connection string | Select this check box to establish a connection using a Uniform Resource Identifier (URI). Then you need to click the [...] button and enter the URI in double quotation marks in the Enter a new password pop-up dialog box that appears, and finally click OK to save the settings.  Note that the URI directly provide the username and password so the Username and Password parameters are not available.  For more information, see [Connection String URI Format](https://www.mongodb.com/docs/manual/reference/connection-string/) from MongoDB documentation.  This option is only available when you select MongoDB 4+ from the DB Version drop-down list and when you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend. |
| Use replica set address or multiple query routers | Select this check box to show the Server addresses table.  In the Server addresses table, define the shared MongoDB databases or the MongoDB replica sets you want to connect to. |
| Server and Port | Enter the IP address and listening port of the database server.  Available when the Use replica set address or multiple query routers check box is not selected. |
| Database | Enter the name of the MongoDB database to be connected to. |
| Use SSL connection | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  In addition, set the *spark.executor.extraJavaOptions* property in the Advanced properties table in the Spark configuration tab of the Run view. For example:  ``` "spark.executor.extraJavaOptions" : "-Djavax.net.ssl.trustStorePassword =password  -Djavax.net.ssl.trustStore= /tmp/keystore.jks  -Djavax.net.ssl.trustStoreType=JKS" ```  This property sets the same parameters as tSetKeystore does for the Spark executors, so you can copy the values from tSetKeystore. Furthermore, you must deploy the keystore on all worker nodes at the exact same location. In the example above, it is */tmp/keystore.jks*.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Use authentication | If the MongoDB database to be used requires authentication, select this check box to enable the database authentication.  Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | Enter the DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  These options are available when the Use authentication check box is selected and when the Use connection string check box is cleared.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Connection string options | You can define more properties in this table for the connection to MongoDB, in addition to the properties defined in the Basic settings tab.  For example, you can add the following option to specify a timeout value for this connection.  ``` connectTimeoutMS=300000 ```  For further information about the options you can add in this table, see [Connection options](https://docs.mongodb.com/manual/reference/connection-string/#connection-string-options). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  The configuration in a tMongoDBConfiguration component applies only on the MongoDB related components in the same Job. In other words, the MongoDB components used in a child or a parent Job that is called via tRunJob cannot reuse this configuration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
