<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandraconfiguration · versión 8.0 -->
# tCassandraConfiguration

Last updated: 9/30/2026

Enables the reuse of the connection configuration to a Cassandra server in the same
Job.

tCassandraConfiguration provides Cassandra connection information for the
Cassandra components used in the same Spark Job. The Spark cluster to be used reads this
configuration to eventually connect to Cassandra.

### In this section

* [tCassandraConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/cassandra/tcassandraconfiguration-properties-for-apache-spark-batch)
* [tCassandraConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/cassandra/tcassandraconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandraconfiguration-properties-for-apache-spark-batch -->
# tCassandraConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tCassandraConfiguration running in the Spark Batch Job framework.

The Spark Batch
tCassandraConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Host | Enter the URL of the Cassandra server you need the Job to connect to. |
| Port | Type in the listening port number of the Cassandra server to be connected to. |
| Username | Fill in this field with the username for the Cassandra authentication. |
| Password | Fill in this field with the password for the Cassandra authentication.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Configuration | Add the Spark properties relating to Cassandra to this table and give them the values you want to use in order to override the default ones at runtime.  * For example, if you need to define the Cassandra consistency level for   reading, select the *input\_consistency\_level*   property in the Property name column and enter   the numeric level value in the Value   column.  The following list presents the numerical values you can put and the consistency levels they signify:  * 0: ANY, * 1: ONE, * 2: TWO, * 3: THREE, * 4: QUORUM, * 5: ALL, * 6: LOCAL\_QUORUM, * 7: EACH\_QUORUM, * 8: SERIAL, * 9: LOCAL\_SERIAL, * 10: LOCAL\_ONE  For further details about each of the consistency policies, see Datastax documentation about Cassandra.  For further information for all the properties listed in this table and their default values, see <https://github.com/datastax/spark-cassandra-connector/blob/master/doc/1_connecting.md>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  You need to drop tCassandraConfiguration along with the Cassandra-related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
