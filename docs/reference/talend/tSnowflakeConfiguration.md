<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconfiguration · versión 8.0 -->
# tSnowflakeConfiguration

Last updated: 9/30/2026

Stores connection information and credentials to be reused by other Snowflake
components in the Apache Spark Batch framework.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSnowflakeConfiguration properties for Apache Spark Batch

These properties are used to configure tSnowflakeConfiguration running in the Spark Batch Job framework.

The Spark Batch
tSnowflakeConfiguration component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Account | In the Account field, enter, in double quotation marks, the account name that has been assigned to you by Snowflake. |
| Region | Select an AWS or Azure region from the drop-down list. |
| Authentication method | Set the authentication method.   * Key Pair:   Select this option if key pair authentication is enabled. For more   information about key pair authentication, see [Using Key Pair   Authentication](https://docs.snowflake.net/manuals/user-guide/jdbc-configure.html#using-key-pair-authentication).   Information noteNote: Before selecting the Key Pair option, make sure you have set the key pair authentication data in the Basic settings view of the tSetKeystore component as follows.  1. Leave the TrustStore type field unchanged. 2. Set TrustStore file to    `""`. 3. Clear the TrustStore password field. 4. Select Need Client authentication. 5. Enter the path to the key store file in double quotation marks in the    KeyStore file field (or click the    […] button to the right of the    KeyStore file field and navigate to the key    store file). 6. Enter the key store file password in the KeyStore    password field. 7. Clear the Check server identity option.  Information noteNote: The Key Pair option is available only with the EMR 5.29 and CDH 6.1 distributions when you are using Spark v2.4 and onwards in the Local Spark mode. |
| Username and Password | Enter, in double quotation marks, your authentication information to log in to Snowflake. |
| Database | Enter, in double quotation marks, the name of the Snowflake database to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Database Schema | Enter, within double quotation marks, the name of the database schema to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Warehouse | Enter, in double quotation marks, the name of the Snowflake warehouse to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Connection properties | Enter, in double quotation marks, a connection property and the associated value in the corresponding columns. You can find the properties available in [Setting Configuration Options for the Connector](https://docs.snowflake.com/en/user-guide/spark-connector-use.html#setting-configuration-options-for-the-connector) from the official Snowflake documentation. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use Custom Region | Select this check box to use the customized Snowflake region. |
| Custom Region | Enter, within double quotation marks, the name of the region to be used. This name is case-sensitive and is normally upper case in Snowflake. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  The configuration in a tSnowflakeConfiguration component applies only on the Snowflake related components that use this configuration and that are in the same Job. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
