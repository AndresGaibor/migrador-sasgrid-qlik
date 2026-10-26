<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconfiguration · versión 8.0 -->
# tHBaseConfiguration

Last updated: 9/30/2026

Enables the reuse of the connection configuration to HBase in the same
Job.

tHBaseConfiguration provides HBase
connection information for the HBase components used in the same Spark
Job. The Spark cluster to be used reads this configuration to eventually
connect to HBase.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tHBaseConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/hbase/thbaseconfiguration-properties-for-apache-spark-batch)
* [tHBaseConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/hbase/thbaseconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconfiguration-properties-for-apache-spark-batch -->
# tHBaseConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tHBaseConfiguration running in the Spark Batch Job framework.

The Spark Batch
tHBaseConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| HBase version | Select the HBase version of the distribution you are using. |
| Zookeeper quorum | Type in the name or the URL of the ZooKeeper service you use to coordinate the transaction between your Talend Studio and your database. Note that when you configure the ZooKeeper, you might need to explicitly set the *zookeeper.znode.parent* property to define the path to the root Znode that contains all the Znodes created and used by your database; then select the Set Zookeeper znode parent check box to define this property. |
| Zookeeper client port | Type in the number of the client listening port of the ZooKeeper service you are using. |
| Use kerberos authentication | If the database to be used is running with Kerberos security, select this checkbox, then, enter the principal names in the HBase Master principal and HBase Region Server principal fields. You should be able to find the information in the *hbase-site.xml* file of the cluster to be used.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| HBase parameters | If you need to use custom configuration for your database, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override the corresponding ones used by Talend Studio. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  You must drop tHBaseConfiguration along with the HBase-related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Prerequisites | Before starting, ensure that you have met the Loopback IP prerequisites expected by your database.  For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster): When using on-premises distributions, use   the configuration component corresponding to the file system   your cluster is using. Typically, this system is HDFS and so   use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).  Actually, this component is relevant with the traditional on-premises   Hadoop distributions only. * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
