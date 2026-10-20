<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/ttop · versión 8.0 -->
# tTop

Last updated: 9/30/2026

Sorts data and outputs several rows from the first one of this data.

tTop sorts input
records based on their schema columns and sends to its following component a given
number of first rows of the sorted records.

### In this section

* [tTop properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/ttop-properties-for-apache-spark-batch)
* [tTop properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/ttop-properties-for-apache-spark-streaming)

**Related concepts**  

* [Performing download analysis using a Spark Batch Job](tcacheout-textractdelimitedfields-ts3configuration-performing-download-analysis-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/ttop-properties-for-apache-spark-batch -->
# tTop properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tTop running in the Spark Batch Job framework.

The Spark Batch
tTop component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Number of line selected | Enter the number of rows to be outputted. The current component selects this number of rows down from the first rows of the sorted data. |
| Criteria | * Click [+] to add as many lines as required for the sort   to be completed. * In the Schema column column, select the column from your   schema, which the sort will be based on. Note that the order is essential as it determines   the sorting priority. * In the other columns, select how you need the data to be sorted. For example, if you need   to sort the data in ascending alphabetical order (from A to Z), select alpha and asc in the corresponding   columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
