<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tnormalize · versión 8.0 -->
# tNormalize

Last updated: 9/30/2026

Normalizes the input flow following SQL standard to help improve data quality and
thus eases the data update.

### In this section

* [tNormalize Standard properties](/talend/en-US/components/8.0/processing/tnormalize-standard-properties)
* [tNormalize properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/tnormalize-properties-for-apache-spark-batch)
* [tNormalize properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/tnormalize-properties-for-apache-spark-streaming)

**Related concepts**  

* [Normalizing data](tnormalize-tfileinputdelimited-tlogrow-tlogrow-normalizing-data-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tnormalize-properties-for-apache-spark-batch -->
# tNormalize properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tNormalize running in the Spark Batch Job framework.

The Spark Batch
tNormalize component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Column to normalize | Select the column from the input flow which the normalization is based on. |
| Item separator | Enter the separator which will delimit data in the input flow.  Information noteNote: The item separator is based on regular expressions, so the character *"."* (a special character for regular expression) should be avoided or used carefully here. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use CSV parameters | Select this check box to include CSV specific parameters such as escape mode and enclosure character. |
| Discard the trailing empty strings | Select this check box to discard the trailing empty strings. |
| Trim resulting values | Select this check box to trim leading and trailing whitespace from the resulting data.  Information noteNote: When both Discard the trailing empty string and Trim resulting values check boxes are selected, the former works first. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tnormalize-standard-properties -->
# tNormalize Standard properties

Last updated: 9/30/2026

These properties are used to configure tNormalize running in the Standard Job framework.

The Standard
tNormalize component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Column to normalize | Select the column from the input flow which the normalization is based on. |
| Item separator | Enter the separator which will delimit data in the input flow.  Information noteNote: The item separator is based on regular expressions, so the character *"."* (a special character for regular expression) should be avoided or used carefully here. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Get rid of duplicated rows from output | Select this check box to deduplicate rows in the data of the output flow. |
| Use CSV parameters | Select this check box to include CSV specific parameters such as escape mode and enclosure character. |
| Discard the trailing empty strings | Select this check box to discard the trailing empty strings. |
| Trim resulting values | Select this check box to trim leading and trailing whitespace from the resulting data.  Information noteNote: When both Discard the trailing empty string and Trim resulting values check boxes are selected, the former works first. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as intermediate step in a data flow. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tnormalize-tfileinputdelimited-tlogrow-tlogrow-normalizing-data-standard-component-this -->
# Normalizing data

Last updated: 9/30/2026

This scenario illustrates a Job that normalizes a list of tags for Web forum
topics, and displays the result in a table on the Run
console.

This list is not well organized and it contains trailing empty strings,
leading, and trailing whitespace, and repeated tags, as shown below.

```
ldap,
  db2, jdbc driver,
grid computing,  talend architecture  ,
content, environment,,
tmap,,
eclipse,
database,java,postgresql,
tmap,
database,java,sybase,
deployment,,
repository,
database,informix,java
```

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/processing/tnormalize-tfileinputdelimited-tlogrow-tlogrow-setting-up-job-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/processing/tnormalize-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/processing/tnormalize-tfileinputdelimited-tlogrow-tlogrow-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tNormalize](tnormalize "Normalizes the input flow following SQL standard to help improve data quality and thus eases the data update.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tnormalize-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Basic settings
   view.
2. In the File name field, specify the path
   to the input file to be normalized.
3. Click the [...] button next
   to Edit schema to open the Schema dialog box.
4. Add one column named *Labels*.
5. Click OK.
6. Enter `","` as Field Separator.
7. Double-click the tNormalize component to
   open Basic settings view.
8. Check the schema, and if necessary, click Sync
   columns to get the schema synchronized with the input
   component.
9. Define the column the normalization operation is based on. 

   In this example, the input schema has only one column, *Labels*.
10. In the tLogRow component,
    select the Table mode.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tnormalize-tfileinputdelimited-tlogrow-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

Save the Job and press F6 to execute
it.

All the unnecessary characters are cleaned
up.

```
|=------------=|
|Labels        |
|=------------=|
|ldap          |
|db2           |
|grid computing|
|content       |
|tmap          |
|eclipse       |
|database      |
|tmap          |
|database      |
|deployment    |
|repository    |
|database      |
'--------------'
```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tnormalize-tfileinputdelimited-tlogrow-tlogrow-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette to the design workspace: tFileInputDelimited, tNormalize, tLogRow.
2. Connect the components by right-clicking the components Row > Main.
