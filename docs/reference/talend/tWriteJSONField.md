<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/twritejsonfield · versión 8.0 -->
# tWriteJSONField

Last updated: 9/30/2026

Transforms the incoming data into JSON fields and transfers them to a file, a
database table, etc.

### In this section

* [tWriteJSONField Standard properties](/talend/en-US/components/8.0/processing/twritejsonfield-standard-properties)
* [tWriteJSONField properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/twritejsonfield-properties-for-apache-spark-batch)
* [tWriteJSONField properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/twritejsonfield-properties-for-apache-spark-streaming)
* [tWriteJSONFields properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/processing/twritejsonfields-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Retrieving error messages while extracting data from JSON fields](textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-retrieving-error-messages-while-extracting-data-from-json-fields-standard-component-in-this)
* [Writing flat data into JSON fields](twritejsonfield-tfixedflowinput-tlogrow-tlogrow-writing-flat-data-into-json-fields-standard-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/twritejsonfield-properties-for-apache-spark-batch -->
# tWriteJSONField properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tWriteJSONField running in the Spark Batch Job framework.

The Spark Batch
tWriteJSONField component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Editor | Opens the interface to create the JSON data structure. For more information, see [Configuring a JSON Tree](/talend/en-US/components/8.0/processing/configuring-a-json-tree). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the output component. |
| Group by | Define the aggregation set, the columns you want to use to regroup the data.  Information noteWarning: Make sure that the data to be grouped is in sequential order.  Information noteNote: If the Group by field is not empty, the order of rows within the group is not guaranteed by Spark. |
| Remove root node | Select this check box to remove the root node from the JSON field generated. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/twritejsonfield-standard-properties -->
# tWriteJSONField Standard properties

Last updated: 9/30/2026

These properties are used to configure tWriteJSONField running in the Standard Job framework.

The Standard
tWriteJSONField component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Output Column | Select the column from the list for holding the JSON string generated. The columns in the list are defined in the output schema. |
| Configure JSON Tree | Opens the interface to create the JSON data structure. For more information, see [Configuring a JSON Tree](/talend/en-US/components/8.0/processing/configuring-a-json-tree). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Information noteNote: In the output schema, a column is null by default; only the column selected   from Output Column holds the JSON string generated. You   can add rows in the Group by table and specify other   output columns to hold Group-by values.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the output component. |
| Group by | Define the aggregation set, the columns you want to use to regroup the data.  Information noteWarning: Make sure that the data to be grouped is in sequential order. |
| Remove root node | Select this check box to remove the root node from the JSON field generated. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Quote all not-null values | Select this check box to surround all values including number and boolean values in the generated JSON field with double quotation marks.  Clear this check box to surround only string values in the generated JSON field with double quotation marks. |
| Quote also null values | Select this check box to surround all the strings with the value of `null` in the generated JSON field with double quotation marks.  This option is available when Quote all not-null values is selected. |
| Pass null values and empty strings explicitly | Select this check box to write the string `null` for fields that are empty. If this check box is not selected, empty fields are filled with `[]`. |
| Use scientific notation for float values | Select this check box to use scientific notation for float values.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-05 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Preceded by an input component, this component wraps the incoming data into a JSON field. |

Information noteNote: For any field with the null value, this
component writes a pair of square brackets ([]). If needed, you can remove or replace
them using a regular expression in a tJavaRow component next to the tWriteJSONField
component. For
example:

```
output_row.rootNode = input_row.rootNode.replaceAll("\\[\\]", "");
```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/twritejsonfield-tfixedflowinput-tlogrow-tlogrow-writing-flat-data-into-json-fields-standard-component-in-this -->
# Writing flat data into JSON fields

Last updated: 9/30/2026

In this scenario, flat data is wrapped into JSON fields via tWriteJSONField.

### In this section

* [Linking the components](/talend/en-US/components/8.0/processing/twritejsonfield-tfixedflowinput-tlogrow-tlogrow-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/processing/twritejsonfield-tfixedflowinput-tlogrow-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/processing/twritejsonfield-tfixedflowinput-tlogrow-tlogrow-executing-job-standard-component-press)

**Related concepts**  

* [tWriteJSONField](twritejsonfield "Transforms the incoming data into JSON fields and transfers them to a file, a database table, etc.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/twritejsonfield-tfixedflowinput-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display
   its Basic settings view.
2. Click Edit schema to open the schema
   editor.

   Click the [+] button to add three
   columns, namely *firstname*, *lastname* and *dept*, with the type of string.

   Click OK to close the editor.
3. Select the Use Inline Content option and
   enter the data below in the Content box: 

   ```
   Andrew;Wallace;Doc
   John;Smith;R&D
   Christian;Dior;Sales
   ```
4. Click tWriteJSONField to display its
   Basic settings view.

   Select the Remove root node option to
   remove the root node setting from the JSON fields generated.
5. Click Configure JSON Tree to open the XML
   tree editor.

   The schema of tFixedFlowInput appears in
   the Linker source panel.
6. In the Linker target panel, click the
   default rootTag and type in staff, which is the root node of the JSON field
   to be generated.
7. Right-click staff and select Add Sub-element from the context menu.
8. In the pop-up box, enter the sub-node name, namely *firstname*.

   Repeat the steps to add two more sub-nodes, namely *lastname* and *dept*.
9. Right-click firstname and select
   Set As Loop Element from the context
   menu.
10. Drop firstname from the Linker source panel to its counterpart in the
    Linker target panel.

    In the pop-up dialog box, select Add linker to
    target node.

    Click OK to close the dialog box.

    Repeat the steps to link the two other items.

    Click OK to close the XML tree
    editor.
11. Click Edit schema to open the schema
    editor.
12. Click the [+] button in the right panel
    to add one column, namely *staff*, which
    will hold the JSON data generated.

    Click OK to close the editor.
13. Double-click tLogRow to display its
    Basic settings view.

    Select Table (print values in cells of a
    table) for a better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/twritejsonfield-tfixedflowinput-tlogrow-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Click F6 to execute the Job.

   As shown above, the JSON fields have been generated correctly, with the
   root node settings removed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/twritejsonfield-tfixedflowinput-tlogrow-tlogrow-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tWriteJSONField and tLogRow.
2. Link tFixedFlowInput and tWriteJSONField using a Row > Main connection.
3. Link tWriteJSONField and tLogRow using a Row > Main connection.
