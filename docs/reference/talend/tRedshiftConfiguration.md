<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconfiguration · versión 8.0 -->
# tRedshiftConfiguration

Last updated: 9/30/2026

Reuses the connection configuration to a Redshift database in the same
Job.

tRedshiftConfiguration provides the
connection information to a given Redshift database for the Redshift
related components used in the same Spark Job. The Spark cluster to be
used reads this configuration to eventually connect to Redshift.

### In this section

* [tRedshiftConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/amazon-redshift/tredshiftconfiguration-properties-for-apache-spark-batch)
* [tRedshiftConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/amazon-redshift/tredshiftconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconfiguration-properties-for-apache-spark-batch -->
# tRedshiftConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tRedshiftConfiguration running in the Spark Batch Job framework.

The Spark Batch
tRedshiftConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Driver version | Select the Redshift driver version to be used between Driver v1 or Driver v2.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Host | Enter the endpoint of the database you need to connect to in Redshift. |
| Port | Enter the port number of the database you need to connect to in Redshift.  The related information can be found in the Cluster Database Properties area in the Web console of your Redshift.  For further information, see [Managing clusters console](http://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html). |
| Username and Password | Enter the authentication information to the Redshift database you need to connect to.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Database | Enter the name of the database you need to connect to in Redshift.  The related information can be found in the Cluster Database Properties area in the Web console of your Redshift.  For further information, see [Managing clusters console](http://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html).  The bucket and the Redshift database to be used must be in the same region on Amazon. This could avoid the S3ServiceException errors known to Amazon. For further information about these errors, see [S3ServiceException Errors](https://docs.aws.amazon.com/redshift/latest/dg/s3serviceexception-error.html). |
| Schema | Enter the name of the database schema to be used in Redshift. The default schema is called *PUBLIC*.  A schema in terms of Redshift is similar to a operating system directory. For further information about a Redshift schema, see [Schemas](http://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables.html). |
| Additional JDBC Parameters (field) | Specify additional JDBC properties for the connection you are creating. The properties are separated by ampersand & and each property is a key-value pair. For example, *ssl=true & sslfactory=com.amazon.redshift.ssl.NonValidatingFactory*, which means the connection will be created using SSL.  This option is only available when you select Driver v1 from the Driver version drop-down list or when you select Driver v2 from the Driver version drop-down list with Use String JDBC parameters selected. |
| Additional JDBC Parameters (table) | Specify JDBC properties in table rows.  To specify a JDBC property, add a row in the table by clicking the plus button on the bottom of this table, enter the property name in the Key column, and then enter the property value in the Value column.  This table is available when you select Driver v2 from the Driver version drop-down list and clear Use String JDBC parameters option.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| S3 configuration | Select the tS3Configuration component from which you want Spark to use the configuration details to connect to S3.  You need drop the tS3Configuration component to be used alongside tRedshiftConfiguration in the same Job so that this tS3Configuration is displayed on the S3 configuration list. |
| S3 temp path | Enter the location in S3 in which the data to be transferred from or to Redshift is temporarily stored.  This path is independent of the temporary path you need to set in the Basic settings tab of tS3Configuration. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  You need to drop tRedshiftConfiguration alongside the other Redshift related subJobs to be run in the same Job so that the configuration is used by the whole Job at runtime.  Since Redshift uses S3 to store temporary data, you need to drop a tS3Configuration component alongside tRedshiftConfiguration in the same Job so that the S3 configuration is used by the whole Job at runtime.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
