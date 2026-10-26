<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tpartition · versión 8.0 -->
# tPartition (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Information noteDeprecation: The tPartition component is
deprecated from the 8.0 R2023-02 Talend
monthly patch. Talend
recommends you to use the tManagePartitions component for newly created Jobs.

Allows you to visually define how an input dataset is partitioned.

The tPartition splits the input dataset
into a given number of partitions.

## tPartition properties for Apache Spark Batch

These properties are used to configure tPartition running in the Spark Batch Job framework.

The Spark Batch
tPartition component belongs to the Processing family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Number of partitions | Enter the number of partitions you want to split the input dataset up into. |
| Repartition by range | Select this check box to divide the dataset into multiple partitions. For more information, see the [official Spark documentation](https://spark.apache.org/docs/2.4.0/api/java/org/apache/spark/sql/Dataset.html#repartitionByRange-scala.collection.Seq-).  This option is only available in Dataset mode.  Information noteNote: tPartition component supports Spark Dataset API only when:  * The Job uses with SparkV2 and onwards. * The Use Dataset API check box from the   Spark configuration view of your Job is   selected. * The Job do not use custom partitioner nor custom comparator. |
| Use coalesce | Select this check box to reduce the number of partitions that are returned. For more information, see the [official Spark documentation](https://spark.apache.org/docs/2.4.0/api/java/org/apache/spark/sql/Dataset.html#coalesce-int-).  This option is only available in Dataset mode.  Information noteNote: tPartition component supports Spark Dataset API only when:  * The Job uses with SparkV2 and onwards. * The Use Dataset API check box from the   Spark configuration view of your Job is   selected. * The Job do not use custom partitioner nor custom comparator. |
| Partition key | Complete this table to define the key to be used for the partitioning.  In the Partition key table, the schema columns are automatically added into the Column column and in the Partition column column, you need to select the check box(es) corresponding to the column(s) you want to use as the key of the partitioning.  This partitioning proceeds in the hash mode, that is to say, the records meeting the same criteria (the key) are dispatched into the same partition. |
| Use custom partitioner | Select this check box to use a Spark partitioner you need to import from outside Talend Studio. For example, a partitioner you have developed by yourself. In this situation, you need to give the following information:  * Custom partitioner FQCN: enter   the fully qualified class name of the partitioner to be imported. * Custom partitioner JAR: click   the [+] button as many time as   needed to add the same number of rows. In each row, click the   [...] button to import the   jar file containing this partitioner class and its dependent jar   files. |
| Sort within partitions | Select this check box to sort the records in each partition.  This feature is useful when a partition contains several distinct key values.  * Natural key order: keys   are sorted in their natural order, for example, in the   alphabetical order. * Custom comparator: this   allows you to use a custom program to sort the keys.  You need to enter the fully qualified class name of the   comparator to be imported in the Custom comparator FQCN field and add the jar   files to be loaded in the Custom   comparator JAR table. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
