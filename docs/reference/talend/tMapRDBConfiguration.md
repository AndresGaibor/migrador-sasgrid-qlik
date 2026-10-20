<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprdbconfiguration · versión 8.0 -->
# tMapRDBConfiguration

Last updated: 9/30/2026

Stores connection information and credentials to be reused by other MapRDB
components.

You configure the connection to a MapR-DB database in tMapRDBConfiguration and configure the other
MapRDB components to reuse this configuration. At runtime, the Spark
executors read this configuration in order to connect to MapR-DB.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tMapRDBConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/maprdb/tmaprdbconfiguration-properties-for-apache-spark-batch)
* [tMapRDBConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/maprdb/tmaprdbconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprdbconfiguration-properties-for-apache-spark-batch -->
# tMapRDBConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMapRDBConfiguration running in the Spark Batch Job framework.

The Spark Batch
tMapRDBConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored.  The properties are stored centrally under the Hadoop Cluster node of the Repository tree. |
| Distribution and Version | Select the MapR distribution to be used. Only MapR V5.2 onwards is supported by the MapRDB components.  If the distribution you need to use with your MapRDB database is not officially supported by this MapRBD component, that is to say, this distribution is MapR but is not listed in the Version drop-down list of this components or this distribution is not MapR at all, select Custom.   1. Select Import from existing    version to import an officially supported distribution as base    and then add other required jar files which the base distribution does not    provide. 2. Select Import from zip to    import the configuration zip for the custom distribution to be used. This zip    file should contain the libraries of the different Hadoop elements and the index    file of these libraries.  Note that custom versions are not officially supported by    Talend    .     Talend     and its community provide you with the opportunity to connect to    custom versions from Talend Studio but cannot guarantee that the configuration of whichever version you choose    will be easy, due to the wide range of different Hadoop distributions and    versions that are available. As such, you should only attempt to set up such a    connection if you have sufficient Hadoop experience to handle any issues on your    own.  Information noteNote: In this dialog box, the active check box must be kept    selected so as to import the jar files pertinent to the connection to be    created between the custom distribution and this component.  For a step-by-step example about how to connect to a custom    distribution and share this connection, see [Hortonworks](/talend/r/en-US/8.0/hortonworks). |
| Zookeeper quorum | Type in the name or the URL of the ZooKeeper service you use to coordinate the transaction between your Talend Studio and your database. Note that when you configure the ZooKeeper, you might need to explicitly set the *zookeeper.znode.parent* property to define the path to the root Znode that contains all the Znodes created and used by your database; then select the Set Zookeeper znode parent check box to define this property. |
| Zookeeper client port | Type in the number of the client listening port of the ZooKeeper service you are using. |
| Use kerberos authentication | If the database to be used is running with Kerberos security, select this checkbox, then, enter the principal names in the HBase Master principal and HBase Region Server principal fields. You should be able to find the information in the *hbase-site.xml* file of the cluster to be used.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used.  For further information about how Kerberos can be configured for your database in a MapR cluster, see [Configuring Kerberos Authentication](http://doc.mapr.com/display/MapR/Configure+Kerberos+Authentication+for+the+HBase+REST+Gateway). |
| HBase Properties | If you need to use custom configuration for your database, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those corresponding ones defined earlier for your database.  For example, you need to define the value of the *dfs.replication* property as *1* for the database configuration. Then you need to add one row to this table using the plus button and type in the name and the value of this property in this row. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used only with the other MapRDB components to provide MapR-DB connection to Spark. |
| Prerequisites | Before starting, ensure that you have met the Loopback IP prerequisites expected by your database.  The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
