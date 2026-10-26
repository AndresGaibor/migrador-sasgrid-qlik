<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow · versión 8.0 -->
# tSortRow

Last updated: 9/30/2026

Helps creating metrics and
classification table.

tSortRow sorts input data based on one or several
columns, by sort type and order.

### In this section

* [tSortRow Standard properties](/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
* [tSortRow properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/tsortrow-properties-for-apache-spark-batch)
* [tSortRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/tsortrow-properties-for-apache-spark-streaming)
* [tSortRow properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/processing/tsortrow-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Aggregating values and sorting data](taggregaterow-tsortrow-tfixedflowinput-tlogrow-aggregating-values-and-sorting-data-standard-component "This example shows you how to use Talend components to aggregate the students' comprehensive scores and then sort the aggregated scores based on the student names.")
* [Deduplicating entries](deduplicating-entries)
* [Regrouping sorted rows](tsortrow-tdenormalizesortedrow-tfileinputdelimited-tlogrow-regrouping-sorted-rows-standard-component-this)
* [Replicating a flow and sorting two identical flows respectively](tsortrow-treplicate-tfileinputdelimited-tlogrow-replicating-flow-and-sorting-two-identical-flows-respectively-standard-component-the)
* [Sorting and aggregating the input data](tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-sorting-and-aggregating-input-data-standard-component-this)
* [Sorting entries based on dynamic schema](tsortrow-tfileinputdelimited-tlogrow-tfileoutputdelimited-sorting-entries-based-on-dynamic-schema-standard-component-enterprise-in-this)
* [Sorting entries](tsortrow-trowgenerator-tlogrow-tlogrow-sorting-entries-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-properties-for-apache-spark-batch -->
# tSortRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tSortRow running in the Spark Batch Job framework.

The Spark Batch
tSortRow component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve   the schema from the previous component connected in the Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Criteria | * Click + to add as many lines as required for the sort to be   complete. By default the first column defined in your schema is   selected. * Schema column: Select the column   label from your schema, which the sort will be based on. Note that   the order is essential as it determines the sorting priority. * Sort type: Numerical and   Alphabetical order are proposed. More sorting types to come. * Order: Ascending or descending   order. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-properties-for-apache-spark-structured-streaming -->
# tSortRow properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tSortRow running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tSortRow component belongs to the Processing family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the fields (columns) processed by the component. When you create a Spark Job, avoid the reserved word `line` when naming fields.   * Built-In: create and store the schema locally for   this component only. * Repository: reuse a schema created and stored in   the Repository across projects and Job designs.   Click Edit schema to modify the schema. If you modify a Repository schema, the available options include:   * View schema: view the schema without modifying it. * Change to built-in property: change the schema to   Built-in for local changes. * Update repository connection: modify the Repository   schema and choose whether to propagate the changes to other Jobs. |
| Criteria | Add the sort criteria by clicking the plus button. Each row defines one sort rule applied in order:  * Schema column: select the column to sort on. The   order of the criteria rows determines the sorting priority. * Sort type: select the comparison type —   Alpha (alphabetical),   Numeric, or   Date. * Order: select Asc for   ascending or Desc for descending. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties -->
# tSortRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tSortRow running in the Standard Job framework.

The Standard
tSortRow component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve   the schema from the previous component connected in the Job.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Criteria | * Click + to add as many lines as required for the sort to be   complete. By default the first column defined in your schema is   selected. * Schema column: Select the column   label from your schema, which the sort will be based on. Note that   the order is essential as it determines the sorting priority. * Sort type: Numerical and   Alphabetical order are proposed. More sorting types to come. * Order: Ascending or descending   order. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Sort on disk | Customize the memory used to temporarily store output data.  Temp data directory path: Set the location where the temporary files should be stored.  Create temp data directory if not exists: Select this check box to create the directory if it does not exist.  Buffer size of external sort: Type in the size of physical memory you want to allocate to sort processing. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles flow of data therefore it requires input and output, hence is defined as an intermediary step. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-sorting-and-aggregating-input-data-standard-component-this -->
# Sorting and aggregating the input data

Last updated: 9/30/2026

This scenario describes a Job that sorts the entries of the input data based on two
columns and displays the sorted data on the console, then aggregates the sorted data based
on one column and displays the aggregated data on the console.

### In this section

* [Adding and linking components](/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tSortRow](tsortrow "Helps creating metrics and classification table.")

**Related reference**  

* [tAggregateSortedRow](taggregatesortedrow "Aggregates the sorted input data for output column based on a set of operations. Each output column is configured with many rows as required, the operations to be carried out and the input column from which the data will be taken for better data aggregation.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-tdenormalizesortedrow-tfileinputdelimited-tlogrow-regrouping-sorted-rows-standard-component-this -->
# Regrouping sorted rows

Last updated: 9/30/2026

This Java scenario describes a four-component Job. It aims at reading a
given delimited file row by row, sorting input data by sort type and order,
denormalizing all input sorted rows and displaying the output on the Run log console.

* Drop the following components from the Palette onto the design workspace: tFileInputDelimited, tSortRow, tDenormalizeSortedRow, and tLogRow.
* Connect the four components using Row
  Main links.

* In the design workspace, select tFileInputDelimited.
* Click the Component tab to
  define the basic settings for tFileInputDelimited.

* Set Property Type to
  Built-In.
* Fill in a path to the processed file in the File Name field. The *name\_list* file used in this example holds two columns, id and first
  name.

* If needed, define row and field separators, header and footer,
  and the number of processed rows.
* Set Schema to Built in and click the [...] button next to
  Edit Schema to define the data to
  pass on to the next component. The schema in this example consists of two
  columns, *id* and *name.*

* In the design workspace, select tSortRow.
* Click the Component tab
  to define the basic settings for tSortRow.

* Set the Schema Type to
  Built-In and click Sync columns to retrieve the schema from the
  tFileInputDelimited component.
* In the Criteria panel,
  use the plus button to add a line and set the sorting parameters for the schema
  column to be processed. In this example we want to sort the *id* columns in ascending order.
* In the design workspace, select tDenormalizeSortedRow.
* Click the Component tab
  to define the basic settings for tDenormalizeSortedRow.

* Set the Schema Type to
  Built-In and click Sync columns to retrieve the schema from the
  tSortRow component.
* In the Input rows
  countfield, enter the number of the input rows to be processed or
  press Ctrl+Space to access the context
  variable list and select the variable: tFileInputDelimited\_1\_NB\_LINE.
* In the To denormalize
  panel, use the plus button to add a line and set the parameters to the column to
  be denormalize. In this example we want to denormalize the *name* column.
* In the design workspace, select tLogRow and click the Component tab to define its basic settings. For more
  information about tLogRow, see [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow).
* Save your Job and press F6 to execute it.

The result displayed on the console shows how the *name* column was denormalize.

**Related concepts**  

* [tSortRow](tsortrow "Helps creating metrics and classification table.")

**Related reference**  

* [tDenormalizeSortedRow](tdenormalizesortedrow "Synthesizes sorted input flow to save memory.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-tfileinputdelimited-tlogrow-tfileoutputdelimited-sorting-entries-based-on-dynamic-schema-standard-component-enterprise-in-this -->
# Sorting entries based on dynamic schema

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

In this scenario we will sort entries in an input file based on a dynamic
schema, display the sorting result on the Run console,
and save the sorting result in an output file. For more information about the dynamic
schema feature, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).

* Drop the components required for this use case: tFileInputDelimited, tSortRow,
  tLogRow and tFileOutputDelimited from the Palette to the design workspace.
* Connect these components together using Row
  > Main links.
* Double-click the tFileInputDelimited
  component to display its Basic settings view.

Information noteWarning:

*The dynamic schema feature is only supported in Built-In mode and requires the input file to have a
header row.*

* Select Built-In from the Property Type list.
* Click the [...] button next to the File Name field to browse to your input file. In this
  use case, the input file *cars.csv* has five columns:
  *ID\_Owner*, *Registration*,
  *Make*, *Color*, and
  *ID\_Reseller*.
* Specify the header row in Header field. In
  this use case the first row is the header row.
* Select Built-In from the Schema list, and click Edit
  schema to set the input schema.

Information noteWarning:

*The dynamic column must be defined in the last row of the
schema.*

* In the schema editor, add two columns and name them
  *ID\_Owner* and *Other* respectively.
  Set the data type of the *Other* column to Dynamic to retrieve all the columns undefined in the
  schema.
* Click OK to propagate the schema and close
  the schema editor.
* Double-click tSortRow to display the
  Basic settings view.

* Add a row in the Criteria table by clicking
  the plus button, select *Other* under Schema column, select *alpha* as the sorting
  type, and select the *ascending* or
  *descending* order for data output.

Information noteWarning:

*Dynamic column sorting works only when the sorting type is
set to alpha.*

* To view the output in the form of a table on the Run console, double-click the tLogRow component and select the Table option in the Basic
  settings view.
* Double-click the tFileOutputDelimited
  component to display its Basic Settings
  view.

* Click the [...] button next to the File Name field to browse to the directory where you
  want to save the output file, and then enter a name for the file.
* Select the Include Header check box to
  retrieve the column names as well as the sorted data.
* Save your Job and press F6 to run it.

  The sorting result is displayed on the Run
  console and written into the output file.

**Related concepts**  

* [tSortRow](tsortrow "Helps creating metrics and classification table.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-treplicate-tfileinputdelimited-tlogrow-replicating-flow-and-sorting-two-identical-flows-respectively-standard-component-the -->
# Replicating a flow and sorting two identical flows respectively

Last updated: 9/30/2026

The scenario describes a Job that reads an input flow which contains names and states
from a CSV file, replicates the input flow, then sorts the two identical flows based on
name and state respectively, and displays the sorted data on the console.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/processing/tsortrow-treplicate-tfileinputdelimited-tlogrow-setting-up-job-standard-component-drop?id=4192)
* [Configuring the components](/talend/en-US/components/8.0/processing/tsortrow-treplicate-tfileinputdelimited-tlogrow-configuring-components-standard-component?id=4193)
* [Saving and executing the Job](/talend/en-US/components/8.0/processing/tsortrow-treplicate-tfileinputdelimited-tlogrow-saving-and-executing-job-standard-component-press?id=4194)

**Related concepts**  

* [tSortRow](tsortrow "Helps creating metrics and classification table.")
* [tReplicate](treplicate "Duplicates the incoming schema into two identical output flows.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-trowgenerator-tlogrow-tlogrow-sorting-entries-standard-component-this -->
# Sorting entries

Last updated: 9/30/2026

This scenario describes a three-component Job. A tRowGenerator is used to create random entries which are directly sent
to a tSortRow to be ordered following a defined value
entry. In this scenario, we suppose the input flow contains names of salespersons along
with their respective sales and their years of presence in the company. The result of
the sorting operation is displayed on the Run
console.

* Drop the three components required for this use case: tRowGenerator, tSortRow and
  tLogRow from the Palette to the design workspace.
* Connect them together using Row
  main links.
* On the tRowGenerator editor, define the
  values to be randomly used in the Sort component. For more information regarding
  the use of this particular component, see [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)

* In this scenario, we want to rank each salesperson according to its
  *Sales* value and to its number of years in the
  company.
* Double-click tSortRow to display the
  Basic settings tab panel. Set the sort
  priority on the Sales value and as secondary criteria, set the number of years
  in the company.

* Use the plus button to add the number of rows required. Set the type of
  sorting, in this case, both criteria being integer, the sort is numerical. At
  last, given that the output wanted is a rank classification, set the order as
  descending.
* Display the Advanced Settings tab and select
  the Sort on disk check box to modify the
  temporary memory parameters. In the Temp data directory
  path field, type the path to the directory where you want to
  store the temporary data. In the Buffer size of external
  sort field, set the maximum buffer value you want to allocate to
  the processing.

Information noteWarning:

*The default buffer value is 1000000 but the more rows and/or columns you
process, the higher the value needs to be to prevent the Job from automatically
stopping. In that event, an "out of memory" error message displays.*

* Make sure you connected this flow to the output component, tLogRow, to display the result in the Job
  console.
* Press F6 to run the Job. The ranking is based
  first on the Sales value and then on the number of years of experience.

**Related concepts**  

* [tSortRow](tsortrow "Helps creating metrics and classification table.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-adding-and-linking-components-standard-component-create -->
# Adding and linking components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in the
   design workspace or dropping them from the Palette: a tFixedFlowInput
   component, a tSortRow component, a tAggregateSortedRow component, and two tLogRow components.
2. Link tFixedFlowInput to tSortRow using a Row >
   Main connection.
3. Do the same to link tSortRow to the first
   tLogRow, link the first tLogRow to tAggregateSortedRow, and link tAggregateSortedRow to the second tLogRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Sorting the input data](/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-sorting-input-data-standard-component)
* [Aggregating the sorted data](/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-aggregating-sorted-data-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Execute the Job by pressing F6 or clicking
   Run on the Run tab.

   As shown above, the input entries are sorted based on the column *Team* and then the column *Age*, both in ascending order, and the sorted entries are then
   aggregated based on the column *Team*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-treplicate-tfileinputdelimited-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Basic settings view
   in the Component tab.
2. Click the [...] button next to the
   File name/Stream field to browse to the
   file from which you want to read the input flow. In this example, the input
   file is *Names&States.csv*, which
   contains two columns: *name* and *state*.

   ```
   name;state
   Andrew Kennedy;Mississippi
   Benjamin Carter;Louisiana
   Benjamin Monroe;West Virginia
   Bill Harrison;Tennessee
   Calvin Grant;Virginia
   Chester Harrison;Rhode Island
   Chester Hoover;Kansas
   Chester Kennedy;Maryland
   Chester Polk;Indiana
   Dwight Nixon;Nevada
   Dwight Roosevelt;Mississippi
   Franklin Grant;Nebraska
   ```
3. Fill in the Header, Footer and Limit fields
   according to your needs. In this example, type in *1* in the Header field to
   skip the first row of the input file.
4. Click Edit schema to define the data
   structure of the input flow.
5. Double-click the first tSortRow component
   to open its Basic settings view.
6. In the Criteria panel, click the
   [+] button to add one row and set the
   sorting parameters for the schema column to be processed. To sort the input
   data by name, select *name* under Schema column. Select *alpha* as the sorting type and *asc* as the sorting order.

   For more information about those parameters, see [tSortRow Standard properties](/talend/en-US/components/8.0/processing/tsortrow-standard-properties).
7. Double-click the second tSortRow
   component and repeat the step above to define the sorting parameters for the
   state column.
8. In the Basic settings view of each
   tLogRow component, select Table in the Mode area for a better view of the Job execution
   result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-treplicate-tfileinputdelimited-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Execute the Job by pressing F6 or
   clicking Run on the Run tab.

   The data sorted by name and state are both displayed on the
   console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-treplicate-tfileinputdelimited-tlogrow-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette to the design workspace: one tFileInputDelimited component, one tReplicate component, two tSortRow components, and two tLogRow components.
2. Connect tFileInputDelimited to tReplicate using a Row > Main link.
3. Repeat the step above to connect tReplicate to two tSortRow
   components respectively and connect tSortRow to tLogRow.
4. Label the components to better identify their functions.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-aggregating-sorted-data-standard-component -->
# Aggregating the sorted data

Last updated: 9/30/2026

## Procedure

1. Double-click tAggregateSortedRow to open its
   Basic settings view.
2. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding five columns: *AggTeam* of
   String type, *AggCount*, *MinAge*, *MaxAge*,
   and *AvgAge* of Integer type.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
3. In the Input rows count field, enter the
   exact number of rows of the input data. In this example, it is *8*.
4. Click the [+] button below the Group by table to add as many rows as required and
   specify the aggregation set in the table. In this example, the data will be
   aggregated based on the input column *Team*.
5. Click the [+] button below the Operations table to add as many rows as required and
   specify the operation to be carried out and the corresponding input column from
   which the data will be taken for each output column. In this example, we want to
   calculate the number of the input entries, the minimum age, the maximum age, and
   the average age for each team.
6. Double-click the second tLogRow to open its
   Basic settings view.
7. In the Mode area, select Table (print values in cells of a table) for better
   readability of the sorting result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-sorting-input-data-standard-component -->
# Sorting the input data

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding four columns: *Id* and
   *Age* of Integer type, and *Name* and *Team* of
   String type.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
3. In the Mode area, select Use Inline Content(delimited file), and then in the
   Content field displayed, enter the input
   data to be sorted and aggregated. In this example, the input data is as
   follows:

   ```
   1;Thomas;28;Component Team
   2;Harry;32;Doc Team
   3;John;26;Component Team
   4;Nicolas;27;QA Team
   5;George;24;Component Team
   6;Peter;30;Doc Team
   7;Teddy;23;QA Team
   8;James;26;Component Team
   ```
4. Double-click tSortRow to open its Basic settings view.
5. Click the [+] button below the Criteria table to add as many rows as required and
   then specify the sorting criteria in the table. In this example, two rows are
   added, and the input entries will be sorted based on the column *Team* and then the column *Age*, both in ascending order.
6. Double-click the first tLogRow to open its
   Basic settings view.
7. In the Mode area, select Table (print values in cells of a table) for better
   readability of the sorting result.
