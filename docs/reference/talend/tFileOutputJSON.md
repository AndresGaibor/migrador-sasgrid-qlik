<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileoutputjson · versión 8.0 -->
# tFileOutputJSON

Last updated: 9/30/2026

Receives data and rewrites it in a JSON structured data block in an output
file.

### In this section

* [tFileOutputJSON Standard properties](/talend/en-US/components/8.0/json/tfileoutputjson-standard-properties)
* [tFileOutputJSON properties for Apache Spark Batch](/talend/en-US/components/8.0/json/tfileoutputjson-properties-for-apache-spark-batch)
* [tFileOutputJSON properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/json/tfileoutputjson-properties-for-apache-spark-streaming)

**Related concepts**  

* [Writing a JSON structured file](tfileoutputjson-trowgenerator-writing-json-structured-file-standard-component "This is a 2 component scenario in which a tRowGenerator component generates random data which a tFileOutputJSON component then writes to a JSON structured output file.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileoutputjson-properties-for-apache-spark-batch -->
# tFileOutputJSON properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileOutputJSON running in the Spark Batch Job framework.

The Spark Batch
tFileOutputJSON component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder | Browse to, or enter the path pointing to the data to be used in the file system.  Note that this path must point to a folder rather than a file.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Output type | Select the structure for the JSON output file(s).   * All in one block: the received   data will be written into one data block. * One row per record: the received   data will be written into separate data blocks row by row. |
| Name of data block | Type in the name of the data block for the JSON output file(s).  This field will be available only if you select *All in one block* from the Output type list. |
| Action | Select the action that you want to perform on the data:   * Overwrite: the data on HDFS will   be overwritten if it already exists. * Create: the data will be   created. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileoutputjson-standard-properties -->
# tFileOutputJSON Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileOutputJSON running in the Standard Job framework.

The Standard
tFileOutputJSON component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| File Name | Name and path of the output file.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Generate an array json | Select this check box to generate an array JSON file. |
| Name of data block | Enter a name for the data block to be written, between double quotation marks.  This field disappears when the Generate an array json check box is selected. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Information noteNote: The support for dynamic schema is available only when you have installed the 8.0.1-R2022-05 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the Output component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Create directory if not exists | This check box is selected by default. This option creates the directory that will hold the output files if it does not already exist. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to rewrite received data in a JSON structured output file. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileoutputjson-trowgenerator-writing-json-structured-file-standard-component -->
# Writing a JSON structured file

Last updated: 9/30/2026

This is a 2 component scenario in which a
tRowGenerator component generates random data which a tFileOutputJSON component then writes to a JSON structured
output file.

### In this section

* [Procedure](/talend/en-US/components/8.0/json/tfileoutputjson-trowgenerator-procedure-standard-component-drop)

**Related concepts**  

* [tFileOutputJSON](tfileoutputjson "Receives data and rewrites it in a JSON structured data block in an output file.")

**Related information**  

* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileoutputjson-trowgenerator-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop a tRowGenerator and a tFileOutputJSON component onto the workspace from the
   Palette.
2. Link the components using a Row > Main
   connection.
3. Double-click tRowGenerator to define
   its Basic Settings properties in the
   Component view.
4. Click [...] next to Edit Schema to display the corresponding dialog box and define
   the schema.
5. Click [+] to add the number of columns
   desired.
6. Under Columns type in the column
   names.
7. Under Type, select the data type from the
   list.
8. Click OK to close the dialog box.
9. Click [+] next to RowGenerator Editor to open the corresponding dialog box.
10. Under Functions, select pre-defined functions
    for the columns, if required, or select [...]
    to set customized function parameters in the Function
    parameters tab.
11. Enter the number of rows to be generated in the corresponding field.
12. Click OK to close the dialog box.
13. Click tFileOutputJSON to set its Basic Settings properties in the Component view.
14. Click [...] to browse to where you want the
    output JSON file to be generated and enter the file name.
15. Enter a name for the data block to be generated in the corresponding field,
    between double quotation marks.
16. Select Built-In as the Schema type.
17. Click Sync Columns to retrieve the schema
    from the preceding component.
18. Press F6 to run the Job.

## Results

The data from the input schema is written in a JSON structured data block in the
output file.
