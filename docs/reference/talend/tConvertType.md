<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tconverttype · versión 8.0 -->
# tConvertType

Last updated: 9/30/2026

Converts one Talend java type to another automatically, and thus avoid
compiling errors.

tConvertType allows specific
conversions at runtime from one Talend
java type to another.

### In this section

* [tConvertType Standard properties](/talend/en-US/components/8.0/processing/tconverttype-standard-properties)
* [tConvertType properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/tconverttype-properties-for-apache-spark-batch)
* [tConvertType properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/tconverttype-properties-for-apache-spark-streaming)

**Related concepts**  

* [Converting java types](tconverttype-tfileinputdelimited-tmap-tlogrow-converting-java-types-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tconverttype-properties-for-apache-spark-batch -->
# tConvertType properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tConvertType running in the Spark Batch Job framework.

The Spark Batch
tConvertType component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Auto Cast | This check box is selected by default. It performs an automatic java type conversion. |
| Manual Cast | This mode is not visible if the Auto Cast check box is selected. It allows you to precise manually the columns where a java type conversion is needed. |
| Set empty values to Null before converting | This check box is selected to set the empty values of String or Object type to null for the input data. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tconverttype-standard-properties -->
# tConvertType Standard properties

Last updated: 9/30/2026

These properties are used to configure tConvertType running in
the Standard Job framework.

The Standard
tConvertType component belongs to the Processing
family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Auto Cast | This check box is selected by default. It performs an automatic java type conversion. |
| Manual Cast | This mode is not visible if the Auto Cast check box is selected. It allows you to precise manually the columns where a java type conversion is needed. |
| Set empty values to Null before converting | This check box is selected to set the empty values of String or Object type to null for the input data. |
| Die on error Information noteNote: Not available for Map/Reduce Jobs. | This check box is selected to kill the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component cannot be used as a start component as it requires an input flow to operate. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tconverttype-tfileinputdelimited-tmap-tlogrow-converting-java-types-standard-component-this -->
# Converting java types

Last updated: 9/30/2026

This Java scenario describes a four-component Job where the tConvertType component is used to convert Java types in three columns,
and a tMap is used to adapt the schema and have as an
output the first of the three columns and the sum of the two others after
conversion.

Information noteNote:

In this scenario, the input schemas for the input delimited file are
stored in the repository, you can simply drag and drop the relevant file node from
Repository - Metadata - File delimited onto the
design workspace to automatically retrieve the tFileInputDelimited component's setting. For more information, see [Centralizing File Delimited metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-file-delimited-metadata).

### In this section

* [Dropping the components](/talend/en-US/components/8.0/processing/tconverttype-tfileinputdelimited-tmap-tlogrow-dropping-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/processing/tconverttype-tfileinputdelimited-tmap-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/processing/tconverttype-tfileinputdelimited-tmap-tlogrow-executing-job-standard-component-press)

**Related concepts**  

* [tConvertType](tconverttype "Converts one Talend java type to another automatically, and thus avoid compiling errors.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tconverttype-tfileinputdelimited-tmap-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputDelimited to enter
   its Basic settings view.
2. Set Property Type to Repository since the file details are stored in
   the repository. The fields to follow are pre-defined using the fetched
   data.

   The input file used in this scenario is called *input.*
   It is a text file that holds string, integer, and float java types.

   Fill in all other fields as needed. For more information, see [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited). In this scenario, the header and the
   footer are not set and there is no limit for the number of processed
   rows.
3. Click Edit schema to
   describe the data structure of this input file. In this scenario, the schema is made
   of three columns, *StringtoInteger, IntegerField,* and *FloatToInteger*.
4. Click Ok to close the dialog
   box.
5. Double-click tConvertType to enter its
   Basic settings view.
6. Set Schema Type to
   Built in, and click Sync columns to automatically retrieve the columns
   from the tFileInputDelimited component.
7. Click Edit schema to
   describe manually the data structure of this processing component.

   In this scenario, we want to convert a string type data into an
   integer type and a float type data into an integer type.

   Click OK to close the
   Schema of tConvertType dialog box.
8. Double-click tMap to open
   the Map editor.

   The Map editor displays the input metadata of the tFileInputDelimited component
9. In the Schema editor panel
   of the Map editor, click the plus button of the output table to add two rows and name
   them to *StringToInteger* and *Sum*.
10. In the Map editor, drag the *StringToInteger*
    row from the input table to the *StringToInteger* row in the
    output table.
11. In the Map editor, drag each of the *IntegerField*and the *FloatToInteger* rows from the input table to the *Sum* row in the output table and click OK to close the Map editor.
12. In the design workspace, select tLogRow
    and click the Component tab to define its
    basic settings. For more information, see [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tconverttype-tfileinputdelimited-tmap-tlogrow-dropping-components-standard-component-drop -->
# Dropping the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tConvertType, tMap, and
   tLogRow.
2. In the Repository tree view, expand Metadata and from File delimited
   drag the relevant node, *JavaTypes* in this
   scenario, to the design workspace.

   The Components dialog box
   displays.
3. From the component list, select tFileInputDelimited and click Ok.

   A tFileInputComponent called
   *Java types* displays in the design workspace.
4. Connect the components using Row > Main
   links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tconverttype-tfileinputdelimited-tmap-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to execute it.

   The string type data is converted into an integer type and displayed in
   the *StringToInteger* column on the console. The float
   type data is converted into an integer and added to the
   *IntegerField* value to give the addition result in
   the *Sum* column on the console.
