<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdatashuffling · versión 8.0 -->
# tDataShuffling

Last updated: 9/30/2026

Shuffles the data from in an input table to protect the actual data while having a
functional data set. Data will remain usable for purposes such as testing and
training.

tDataShuffling replaces original values with other
values for the same column from a different row.

If you define one or several columns as the partition group, the whole
table is split into a given number of partitions. These partitions share
the same values in the columns partitioned. Then, the shuffling process
is applied independently to each partition. All partitions are merged
into one output table.

If you do not set columns as the partition group, the shuffling
process is applied to the whole input table.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tDataShuffling Standard properties](/talend/en-US/components/8.0/data-privacy/tdatashuffling-standard-properties)
* [tDataShuffling properties for Apache Spark Batch](/talend/en-US/components/8.0/data-privacy/tdatashuffling-properties-for-apache-spark-batch)

**Related tasks**  

* [Shuffling data values to restrict the use of actual sensitive data](shuffling-data-values-to-restrict-use-of-actual-sensitive-data "With the tDataShuffling component, you can shuffle sensitive information to replace it with other values for the same column from a different row, allowing production data to be safely used for purposes such as testing and training.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdatashuffling-properties-for-apache-spark-batch -->
# tDataShuffling properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDataShuffling running in the Spark Batch Job framework.

The Spark Batch
tDataShuffling component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Shuffling columns | Define the groups of columns to be shuffled:   * Column: Select the columns to be shuffled. * Group ID: Select the group identifier to group   columns. The columns having the same group identifier are shuffled together.  This field is set to *0* by default. This means that the column   is not part of the shuffling process. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Seed for random generator | Set a random number if you want to shuffle the data in the same order in each execution of the Job. The seed is not set by default.  If you do not set the seed, the component creates a new random seed for each Job execution. Repeating the execution with a different value for this field will shuffle the data in a different order. |
| Partitioning columns | Add the columns used for partitioning the data.  The selected columns separate the shuffling process into small partitions. Only the rows within a partition can be shuffled together. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdatashuffling-standard-properties -->
# tDataShuffling Standard properties

Last updated: 9/30/2026

These properties are used to configure tDataShuffling running in the Standard Job framework.

The Standard
tDataShuffling component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Shuffling columns | Define the groups of columns to be shuffled:   * Column: Select the columns to be shuffled. * Group ID: Select the group identifier to group   columns. The columns having the same group identifier are shuffled together.  This field is set to *0* by default. This means that the column   is not part of the shuffling process. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Seed for random generator | Set a random number if you want to shuffle the data in the same order in each execution of the Job. The seed is not set by default.  If you do not set the seed, the component creates a new random seed for each Job execution. Repeating the execution with a different value for this field will shuffle the data in a different order. |
| Buffer size | Type in the size of physical memory, in number of rows, you want to allocate to processed data. |
| Partitioning columns | Add the columns used for partitioning the data.  The selected columns separate the shuffling process into small partitions. Only the rows within a partition can be shuffled together. |
| tStat Catcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |
