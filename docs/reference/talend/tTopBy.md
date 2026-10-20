<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/ttopby · versión 8.0 -->
# tTopBy

Last updated: 9/30/2026

Groups and sorts data and outputs several rows from the first one of the data in
each group.

tTopBy groups the
input data by applying user-defined keys, sorts records in each group and sends to its
following component a given number of first rows of the sorted records.

### In this section

* [tTopBy properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/ttopby-properties-for-apache-spark-batch)
* [tTopBy properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/ttopby-properties-for-apache-spark-streaming)
* [tTopBy properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/processing/ttopby-properties-for-apache-spark-structured-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/ttopby-properties-for-apache-spark-batch -->
# tTopBy properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tTopBy running in the Spark Batch Job framework.

The Spark Batch
tTopBy component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Number of line selected | Enter the number of rows to be outputted. The current component selects this number of rows down from the first rows of the sorted data. |
| Key | Select the column(s) from which the records are used as keys to group the input data.  You need to click [+] to add as many lines as required to use as keys for the grouping to be completed |
| Criteria | * Click [+] to add as many lines as required for the sort   to be completed. * In the Schema column column, select the column from your   schema, which the sort will be based on. Note that the order is essential as it determines   the sorting priority. * In the other columns, select how you need the data to be sorted. For example, if you need   to sort the data in ascending alphabetical order (from A to Z), select alpha and asc in the corresponding   columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/ttopby-properties-for-apache-spark-structured-streaming -->
# tTopBy properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tTopBy running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tTopBy component belongs to the Processing family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the fields (columns) processed by the component. When you create a Spark Job, avoid the reserved word `line` when naming fields.   * Built-In: create and store the schema locally for   this component only. * Repository: reuse a schema created and stored in   the Repository across projects and Job designs.   Click Edit schema to modify the schema. If you modify a Repository schema, the available options include:   * View schema: view the schema without modifying it. * Change to built-in property: change the schema to   Built-in for local changes. * Update repository connection: modify the Repository   schema and choose whether to propagate the changes to other Jobs. |
| Number of line selected | Enter the number of rows to be outputted. The current component selects this number of rows down from the first rows of the sorted data. |
| Partition Key | Select the column(s) from which the records are used as keys to group the input data.  You need to click [+] to add as many lines as required to use as keys for the grouping to be completed |
| Criteria | * Click [+] to add as many lines as required for the sort   to be completed. * In the Schema column column, select the column from your   schema, which the sort will be based on. Note that the order is essential as it determines   the sorting priority. * In the other columns, select how you need the data to be sorted. For example, if you need   to sort the data in ascending alphabetical order (from A to Z), select alpha and asc in the corresponding   columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used as an intermediate step.  This component maintains a stateful ranking of the top N rows per partition group across micro-batches. If no partition key is defined, all rows are ranked together as a single global group.  Information noteRestriction: The output mode of the downstream output component must not be set to Append. Use Update or Complete instead.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |
