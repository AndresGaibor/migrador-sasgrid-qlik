<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryconfiguration · versión 8.0 -->
# tBigQueryConfiguration

Last updated: 9/30/2026

Provides the connection configuration to Google BigQuery and Google Cloud Storage
for a Spark Job.

### In this section

* [tBigQueryConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/google-bigquery/tbigqueryconfiguration-properties-for-apache-spark-batch)
* [tBigQueryConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/google-bigquery/tbigqueryconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryconfiguration-properties-for-apache-spark-batch -->
# tBigQueryConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tBigQueryConfiguration running in the Spark Batch Job framework.

The Spark Batch
tBigQueryConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

When you use this component with Google Dataproc:

| Properties | Description |
| --- | --- |
| BigQuery temp GCS path | Enter the directory on Google Storage to temporarily store the data to be used with Google BigQuery. If not existing yet, this directory is created on the fly but the bucket that contains this directory must already exist. The syntax of the directory should be gs://my\_bucket/my\_directory.  When you use Google BigQuery with Dataproc, in Google Cloud Platform, select the same region for your BigQuery dataset as for the Dataproc cluster to be run. |
| Location | Select one of the Google multi-regional locations in which you want to read or write data. The resource dataset and the target dataset must be in the same location.  In Spark Jobs, only the US and the EU locations are supported.  For further information about Google locations and how to properly use the locations, see [Dataset Locations](https://cloud.google.com/bigquery/docs/dataset-locations) in the Google Cloud documentation. |

When you use this component with the other distributions

| Properties | Description |
| --- | --- |
| Project ID | Enter the ID of your Google Cloud Platform project.  If you are not certain about your project ID, confirm it in the Manage Resources page of your Google Cloud Platform services. |
| Path to Google Credentials file | Enter the path to the credentials file associated to the user account to be used. This file must be stored in the machine in which your Talend Job is actually launched and executed.  If you use Talend JobServer to run your Job, store the credentials file not only in the machine of the Talend JobServer, in which the Job is launched, but also in the worker machines of the Spark cluster, in which the Job is executed; if you do not use the Talend JobServer, store the credentials file in your local machine from which you launch the Job and in the worker machines of the Spark cluster. |
| Use P12 credentials file format | When the Google credentials file to be used is in P12 format, select this check box and then in the Service account Id field that is displayed, enter the ID of the service account for which this P12 credentials file has been created. |
| BigQuery temp GCS path | Enter the directory on Google Storage to temporarily store the data to be used with Google BigQuery. If not existing yet, this directory is created on the fly but the bucket that contains this directory must already exist. The syntax of the directory should be gs://my\_bucket/my\_directory.  When you use Google BigQuery with Dataproc, in Google Cloud Platform, select the same region for your BigQuery dataset as for the Dataproc cluster to be run. |
| Location | Select one of the Google multi-regional locations in which you want to read or write data. The resource dataset and the target dataset must be in the same location.  In Spark Jobs, only the US and the EU locations are supported.  For further information about Google locations and how to properly use the locations, see [Dataset Locations](https://cloud.google.com/bigquery/docs/dataset-locations) in the Google Cloud documentation. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used standalone in a subJob to provide connection configuration to Google BigQuery and Google Storage for the whole Job. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
