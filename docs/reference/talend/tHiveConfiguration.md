<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconfiguration · versión 8.0 -->
# tHiveConfiguration

Last updated: 9/30/2026

Enables the reuse of the connection configuration to Hive in the same
Job.

Hive allows you to access external tables from Spark but does not support ACID
transactions.

tHiveConfiguration provides Hive
connection information for the Hive related components used in the same
Spark Job. The Spark cluster to be used reads this configuration to
eventually connect to Hive.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tHiveConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/hive/thiveconfiguration-properties-for-apache-spark-batch)
* [tHiveConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/hive/thiveconfiguration-properties-for-apache-spark-streaming)
* [tHiveConfiguration properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/hive/thiveconfiguration-properties-for-apache-spark-structured-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconfiguration-properties-for-apache-spark-batch -->
# tHiveConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tHiveConfiguration running in the Spark Batch Job framework.

The Spark Batch
tHiveConfiguration component belongs to the Storage family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Distribution and Version | Select the Hadoop distribution you are using for Hive.  Note that the Hive version required by Spark must be 0.13+.  Select the HBase version of the distribution you are using. |
| Hive thrift metastore | Enter the location of the metastore of the Hive system to be used by specifying the name of its Host and the number of its listening Port. If HA metastore has been defined for this Hive system, select the Enable high availability check box and in the field that is displayed, enter the URIs of the multiple remote metastore services, each being separated with a comma(,). |
| Use Kerberos authentication | If you are accessing a Hive metastore running with Kerberos security, select this checkbox.  Then you need to enter the Hive principal that should have been defined in the *hive-site.xml* file of the cluster to be used.  Hive principal uses the value of *hive.metastore.kerberos.principal*. This is the service principal of the Hive metastore. |
| Spark catalog | Select the Spark implementation to use.  * In-memory: select this value   if you set the Hive thrift   metastore to a Hive metastore that is   not an external metastore. * Hive: select this value if   you set the Hive thrift   metastore to an external Hive   metastore that exists outside of your cluster. |
| Force MapR Ticket authentication | If this cluster is a MapR cluster of the version 5.0.0 or later, you can set the MapR ticket authentication configuration in addition or as an alternative by following the explanation in [Connecting to a security-enabled MapR](/talend/en-US/components/8.0/mapr/connecting-to-security-enabled-mapr).  Keep in mind that this configuration generates a new MapR security ticket for the username defined in the Job in each execution. If you need to reuse an existing ticket issued for the same username, leave both the Force MapR ticket authentication check box and the Use Kerberos authentication check box clear, and then MapR should be able to automatically find that ticket on the fly. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  You need to drop tHiveConfiguration along with the Hive-related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconfiguration-properties-for-apache-spark-structured-streaming -->
# tHiveConfiguration properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tHiveConfiguration running
in the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tHiveConfiguration component belongs to the Databases family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Hive thrift metastore | Enter the location of the metastore of the Hive system to be used by specifying the name of its Host and the number of its listening Port. If HA metastore has been defined for this Hive system, select the Enable high availability check box and in the field that is displayed, enter the URIs of the multiple remote metastore services, each being separated with a comma(,). |
| Use kerberos authentication | If you are accessing a Hive metastore running with Kerberos security, select this checkbox.  Then you need to enter the Hive principal that should have been defined in the *hive-site.xml* file of the cluster to be used.  Hive principal uses the value of *hive.metastore.kerberos.principal*. This is the service principal of the Hive metastore. |
| Spark catalog | Select the Spark implementation to use.  * In-memory: select this value   if you set the Hive thrift   metastore to a Hive metastore that is   not an external metastore. * Hive: select this value if   you set the Hive thrift   metastore to an external Hive   metastore that exists outside of your cluster. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used standalone. Add it to the same Job as the Hive-related subJob so that the configuration is available to the whole Job at runtime.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | In the Structured Streaming Configuration tab of the Run view, define the connection to the Spark cluster for the whole Job. Specify the directory to which the Job's dependent JAR files are transferred so Spark can access them.  This connection is effective on a per-Job basis. |
