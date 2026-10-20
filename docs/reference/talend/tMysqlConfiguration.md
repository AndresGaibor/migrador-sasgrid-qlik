<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconfiguration · versión 8.0 -->
# tMysqlConfiguration

Last updated: 9/30/2026

Stores connection information and credentials to be reused by other MySQL
components.

You configure the connection to a MySQL database in tMysqlConfiguration and configure the other
MySQL components to reuse this configuration. At runtime, the Spark
executors read this configuration in order to connect to MySQL.

### In this section

* [tMysqlConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/mysql/tmysqlconfiguration-properties-for-apache-spark-batch)
* [tMysqlConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/mysql/tmysqlconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconfiguration-properties-for-apache-spark-batch -->
# tMysqlConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMysqlConfiguration running in the Spark Batch Job framework.

The Spark Batch
tMysqlConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| DB version | Select the version of the database to be used.  When the database to be used is RDS Aurora, you need to select Mysql 5 (deprecated).  Information noteNote: MySQL 5 has been removed from Talend Studio 8.0 R2026-04. Use MySQL 8.0 or later. |
| Host | Enter the IP address of the database server. |
| Port | Enter the listening port number of the database server. |
| Database | Select or enter the name of the database to be used. |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating.  In order for tMysqlInput component to correctly handle boolean type column, append the following parameter: tinyInt1isBit=false. |
| Username and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  The configuration in a tMysqlConfiguration component applies only on the MySQL related components in the same Job. In other words, the MySQL components used in a child or a parent Job that is called via tRunJob cannot reuse this configuration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
