<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/treplicate · versión 8.0 -->
# tReplicate

Last updated: 9/30/2026

Duplicates the incoming schema into two identical output flows.

This component performs different operations on the same
schema.

### In this section

* [tReplicate Standard properties](/talend/en-US/components/8.0/orchestration/treplicate-standard-properties?id=3822)
* [tReplicate properties for Apache Spark Batch](/talend/en-US/components/8.0/orchestration/treplicate-properties-for-apache-spark-batch?id=3823)
* [tReplicate properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/orchestration/treplicate-properties-for-apache-spark-streaming?id=3824)
* [tReplicate properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/orchestration/treplicate-properties-for-apache-spark-structured-streaming?id=3825)

**Related concepts**  

* [Replicating a flow and sorting two identical flows respectively](tsortrow-treplicate-tfileinputdelimited-tlogrow-replicating-flow-and-sorting-two-identical-flows-respectively-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/treplicate-properties-for-apache-spark-batch -->
# tReplicate properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tReplicate running in the Spark Batch Job framework.

The Spark Batch
tReplicate component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve the   schema from the previous component in the Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Cache replicated RDD | Select this check box to store the replicated RDD in the cache.  From the Storage level drop-down list that is displayed, select how the cached RDDs are stored, such as in memory only or in memory and on disk.  For further information about each of the storage level, see <https://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/treplicate-properties-for-apache-spark-structured-streaming -->
# tReplicate properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tReplicate running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tReplicate component belongs to the Processing family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the fields (columns) processed by the component. When you create a Spark Job, avoid the reserved word `line` when naming fields.   * Built-In: create and store the schema locally for   this component only. * Repository: reuse a schema created and stored in   the Repository across projects and Job designs.   Click Edit schema to modify the schema. If you modify a Repository schema, the available options include:   * View schema: view the schema without modifying it. * Change to built-in property: change the schema to   Built-in for local changes. * Update repository connection: modify the Repository   schema and choose whether to propagate the changes to other Jobs. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/treplicate-standard-properties -->
# tReplicate Standard properties

Last updated: 9/30/2026

These properties are used to configure tReplicate running in the Standard Job framework.

The Standard
tReplicate component belongs to the Orchestration family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve   the schema from the previous component in the Job.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is not startable (green background), it requires an Input component and an output component. |
| Connections | Outgoing links (from this component to another):  Row: Main.  Trigger: Run if; On Component Ok; On Component Error.    Incoming links (from one component to this one):  Row: Main; Reject;    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
