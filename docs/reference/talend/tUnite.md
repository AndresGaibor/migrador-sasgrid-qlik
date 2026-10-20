<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite · versión 8.0 -->
# tUnite

Last updated: 9/30/2026

Centralizes data from various and heterogeneous sources.

tUnite merges data from various
sources, based on a common schema.

Note that tUnite cannot exist in a
data flow loop. For instance, if a data flow goes through several tMap components to generate two flows, they cannot be fed to tUnite.

Information noteNote: This component is for sequential flow only and does not support parallelization.

### In this section

* [tUnite Standard properties](/talend/en-US/components/8.0/orchestration/tunite-standard-properties?id=3831)
* [tUnite properties for Apache Spark Batch](/talend/en-US/components/8.0/orchestration/tunite-properties-for-apache-spark-batch?id=3832)
* [tUnite properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/orchestration/tunite-properties-for-apache-spark-streaming?id=3833)

**Related concepts**  

* [Iterating on files and merge the content](tunite-tfilelist-tfileinputdelimited-tlogrow-iterating-on-files-and-merge-content-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-properties-for-apache-spark-batch -->
# tUnite properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tUnite running in the Spark Batch Job framework.

The Spark Batch
tUnite component belongs to the Orchestration family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to be   processed and passed on to the next component. The schema is either   Built-in or stored remotely in the   Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve the   schema from the previous component in the Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-standard-properties -->
# tUnite Standard properties

Last updated: 9/30/2026

These properties are used to configure tUnite running in the Standard Job framework.

The Standard
tUnite component belongs to the Orchestration family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous   component in the Job.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-in: The   schema will be created and stored locally for this component only.   For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The   schema already exists and is stored in the Repository, hence can be   reused in various projects and Job designs. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is not startable and requires one or several input components and an output component. |
| Connections | Outgoing links (from this component to another):  Row: Main.  Trigger: Run if; On Component Ok; On Component Error    Incoming links (from one component to this one):  Row: Main; Reject.    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-tfilelist-tfileinputdelimited-tlogrow-iterating-on-files-and-merge-content-standard-component-the -->
# Iterating on files and merge the content

Last updated: 9/30/2026

The following Job iterates on a list of files then merges their content and displays
the final 2-column content on the console.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/orchestration/tunite-tfilelist-tfileinputdelimited-tlogrow-dropping-and-linking-components-standard-component-drop?id=3852)
* [Configuring the components](/talend/en-US/components/8.0/orchestration/tunite-tfilelist-tfileinputdelimited-tlogrow-configuring-components-standard-component-in?id=3853)
* [Saving and executing the Job](/talend/en-US/components/8.0/orchestration/tunite-tfilelist-tfileinputdelimited-tlogrow-saving-and-executing-job-standard-component-press?id=3854)

**Related concepts**  

* [tUnite](tunite "Centralizes data from various and heterogeneous sources.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileList](/talend/en-US/components/8.0/tfilelist/tfilelist)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-tfilelist-tfileinputdelimited-tlogrow-configuring-components-standard-component-in -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. In the tFileList
   Basic settings view, browse to the
   directory, where the files to merge are stored.

   The files are pretty basic and contain a list of countries and their
   respective score.
2. In the Case Sensitive field, select
   Yes to consider the letter case.
3. Select the tFileInputDelimited component,
   and display this component's Basic settings
   view.
4. Fill in the File Name/Stream field by
   using the Ctrl+Space bar combination to
   access the variable completion list, and selecting
   tFileList.CURRENT\_FILEPATH from the global variable list to
   process all files from the directory defined in the tFileList.
5. Click the Edit Schema button and set
   manually the 2-column schema to reflect the input files' content. 

   For this example, the 2 columns are *Country* and
   *Points*. They are both nullable. The *Country* column is of
   String type and the
   *Points* column is of Integer type.
6. Click OK to validate the setting and
   accept to propagate the schema throughout the Job.
7. Then select the tUnite component and
   display the Component view. Notice that the
   output schema strictly reflects the input schema and is read-only.
8. In the Basic settings view of tLogRow, select the Table option to display properly the output values.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-tfilelist-tfileinputdelimited-tlogrow-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components onto the design workspace: tFileList, tFileInputDelimited, tUnite
   and tLogRow.
2. Connect the tFileList to the tFileInputDelimited using an Iterate connection and connect the other
   component using a row main link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-tfilelist-tfileinputdelimited-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6, or click Run on the Run console to
   execute the Job.

   The console shows the data from the various files, merged into one single
   table.
