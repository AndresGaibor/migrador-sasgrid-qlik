<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow · versión 8.0 -->
# tAggregateRow

Last updated: 9/30/2026

Receives a flow and aggregates it based on one or more columns.

For each output line, are provided the aggregation key and the relevant
result of set operations (min, max, sum...).

tAggregateRow helps to provide a set of metrics based on values or
calculations.

### In this section

* [tAggregateRow Standard properties](/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
* [tAggregateRow properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-batch)
* [tAggregateRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-streaming)
* [tAggregateRow properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Aggregating values and sorting data](taggregaterow-tsortrow-tfixedflowinput-tlogrow-aggregating-values-and-sorting-data-standard-component "This example shows you how to use Talend components to aggregate the students' comprehensive scores and then sort the aggregated scores based on the student names.")
* [Aggregating values based on dynamic schema](taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-aggregating-values-based-on-dynamic-schema-standard-component-enterprise "Here is an example of using the tAggregateRow component to aggregate some task assignment data in a CSV file based on a dynamic schema column.")
* [Performing download analysis using a Spark Batch Job](tcacheout-textractdelimitedfields-ts3configuration-performing-download-analysis-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-batch -->
# tAggregateRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tAggregateRow running in the Spark Batch Job framework.

The Spark Batch
tAggregateRow component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Information noteTip: By default, when Spark aggregates BigDecimal, the   precision and scale are set at the maximum values of the data type.   You can change the scale and the precision for BigDecimal in the   corresponding columns of the schema. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Group by | * Define the aggregation sets, the values of which will be used for   calculations. * Output Column: Select the column   label in the list offered based on the schema structure you defined. You   can add as many output columns as you wish to make more precise   aggregations.  Ex: Select Country to calculate an average of values for each country   of a list or select Country and Region if you want to compare one   country's regions with another country' regions. * Input Column: Match the input column   label with your output columns, in case the output label of the   aggregation set needs to be different. |
| Operations | * Select the type of operation along with the value to use for the   calculation and the output field. * Output Column: Select the destination   field in the list.  Function: Select the operator among: * Input column: Select the input column   from which the values are taken to be aggregated. * Ignore null values: Select the check   boxes corresponding to the names of the columns for which you want the   NULL value to be ignored. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use financial precision, this is the max precision for "sum" and "avg" operations, checked option heaps more memory and slower than unchecked. | Select this check box to use a financial precision. This is a max precision but consumes more memory and slows the processing.  Information noteWarning: *We advise you to use the BigDecimal type for the output in order to obtain precise results.* |
| Check type overflow (slower) | Checks the type of data to ensure that the Job doesn't crash. |
| Check ULP (Unit in the Last Place), ensure that a value will be incremented or decremented correctly, only float and double types. (slower) | Select this check box to ensure the most precise results possible for the Float and Double types. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-structured-streaming -->
# tAggregateRow properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tAggregateRow running in
the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tAggregateRow component belongs to the Processing family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Group by | Define the aggregation sets whose values are used for calculations. Output Column: Select the column label from the list based on the schema structure you defined. Add as many output columns as needed to refine the aggregation. For example, select Country to calculate an average for each country, or select Country and Region to compare regions across countries.  Input Column: Match the input column label to the output column when the aggregation set needs a different output label. |
| Operations | Select the type of operation to perform along with the input value and the output field. Output Column: Select the destination field from the list.  Function: Select the operator among:  Input column: Select the input column whose values are aggregated.  Ignore null values: Select the check boxes for the columns where NULL values should be ignored. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties -->
# tAggregateRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tAggregateRow running
in the Standard Job framework.

The Standard
tAggregateRow component belongs to the Processing
family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Group by | * Define the aggregation sets, the values of which will be   used for calculations. * Output Column: Select the column   label in the list offered based on the schema structure you defined. You   can add as many output columns as you wish to make more precise   aggregations.  Ex: Select Country to calculate an average of values for   each country of a list or select Country and Region if you want to   compare one country's regions with another country' regions. * Input Column: Match the input   column label with your output columns, in case the output label of the   aggregation set needs to be different. |
| Operations | * Select the type of operation along with the value to use   for the calculation and the output field. * Output Column: Select the   destination field in the list.  Function: Select the operator among:   + count: calculates the number of rows   + min: selects the minimum value   + max: selects the maximum value   + avg: calculates the average   + sum: calculates the sum   + first: returns the first value   + last: returns the last value   + list: lists values of an aggregation by multiple keys.   + list (object): lists Java values of an aggregation by multiple keys   + count (distinct): counts the number of the distinct rows   + standard deviation: calculates the     variability of a set of value.   + union (geometry): makes the union of a set of Geometry objects   + population standard deviation: calculates the     spread of a data distribution. Use this function if the data to be     calculated is considered a population on its own. This calculation     supports 39 decimal places.   + sample     standard deviation: calculates the spread of a data     distribution. Use this function if the data to be calculated is     considered a sample from a larger population. This calculation     supports 39 decimal places. * Input column: Select the input   column from which the values are taken to be aggregated. * Ignore null values: Select the   check boxes corresponding to the names of the columns for which you want   the NULL value to be ignored. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Delimiter(only for list operation) | Enter the delimiter you want to use to separate the different operations. |
| Use financial precision, this is the max precision for "sum" and "avg" operations, checked option heaps more memory and slower than unchecked. | Select this check box to use a financial precision. This is a max precision but consumes more memory and slows the processing.  Information noteWarning: *We advise you to use the BigDecimal type for the output in order to obtain precise results.* |
| Check type overflow (slower) | Checks the type of data to ensure that the Job doesn't crash. |
| Check ULP (Unit in the Last Place), ensure that a value will be incremented or decremented correctly, only float and double types. (slower) | Select this check box to ensure the most precise results possible for the Float and Double types. |
| tStatCatcher Statistics | Check this box to collect the log data at component level. Note that this check box is not available in the Map/Reduce version of the component. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles flow of data therefore it requires input and output, hence is defined as an intermediary step. Usually the use of tAggregateRow is combined with the tSortRow component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-aggregating-values-based-on-dynamic-schema-standard-component-enterprise -->
# Aggregating values based on dynamic schema

Last updated: 9/30/2026

Here is an example of using the tAggregateRow component to aggregate some task assignment data in a CSV file
based on a dynamic schema column.

This scenario applies only to subscription-based Talend
products.

### In this section

* [Creating a Job for aggregating values based on dynamic schema](/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-creating-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise-create)
* [Configuring the Job for aggregating values based on dynamic schema](/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-configuring-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise)
* [Executing the Job to aggregate values based on dynamic schema](/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-executing-job-to-aggregate-values-based-on-dynamic-schema-standard-component-enterprise-press)

**Related concepts**  

* [tAggregateRow](taggregaterow "Receives a flow and aggregates it based on one or more columns.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-aggregating-values-and-sorting-data-standard-component -->
# Aggregating values and sorting data

Last updated: 9/30/2026

This example shows you how to use Talend components
to aggregate the students' comprehensive scores and then sort the aggregated scores based on
the student names.

### In this section

* [Creating a Job for aggregating and sorting data](/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-creating-job-for-aggregating-and-sorting-data-standard-component-create)
* [Configuring the Job for aggregating and sorting data](/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-configuring-job-for-aggregating-and-sorting-data-standard-component)
* [Executing the Job to aggregate and sort data](/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-executing-job-to-aggregate-and-sort-data-standard-component-press)

**Related concepts**  

* [tAggregateRow](taggregaterow "Receives a flow and aggregates it based on one or more columns.")
* [tSortRow](tsortrow "Helps creating metrics and classification table.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-configuring-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise -->
# Configuring the Job for aggregating values based on dynamic schema

Last updated: 9/30/2026

Configure the Job to aggregate some task assignment data in a CSV
file based on a dynamic schema column using the tAggregateRow component.

Then this Job displays the aggregated data on the console
using the tLogRow component and writes it into an
output CSV file using the tFileOutputDelimited
component.

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Basic settings view.
2. In the File name/Stream field, specify
   the path to the CSV file that holds the following task assignment data, *D:/tasks.csv* in this example.

   ```
   task;team;status
   task1;team1;done
   task2;team2;done
   task3;team1;done
   task4;team2;pending
   task5;team1;pending
   task6;team2;pending
   ```
3. In the Header field, enter the number
   of rows to be skipped in the beginning of the file, *1* in this example.

   Note that the dynamic schema feature is only supported in the Built-In mode and requires the input file to have a
   header row.
4. Click the
   button next to Edit schema to
   open the schema dialog box and define the schema by adding two columns, *task* of String type and *other* of Dynamic type. When done, click OK to save the changes and close the schema dialog box.

   Note that the dynamic column must be defined in the last row of
   the schema. For more information about dynamic schema, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).
5. Double-click the tAggregateRow
   component, and on its Basic settings view, click
   the Sync columns button to retrieve the schema from
   the preceding component.
6. Add one row in the Group by table by
   clicking the
   button below it, and select *other* from both the Output column
   and Input column position column fields to group
   the input data by the *other* dynamic
   column.

   Note that the dynamic column aggregation can be carried out only for the grouping
   operation.
7. Add one row in the Operations table
   and define the operation to be carried out. In this example, the operation function
   is *list*. Then select *task* from both the Output column
   and Input column position column fields to list the
   entries in the *task* column in the grouping result.
8. Double-click the tLogRow component to
   open its Basic settings view, and then select
   Table (print values in cells of a table) in the
   Mode area for better readability of the
   result.
9. Double-click the tFileOutputDelimited
   component to open its Basic settings view, and in
   the File Name field, specify the path to the CSV
   file into which the aggregated data will be written, *D:/tasks\_aggregated.csv* in this example.
10. Select the Include Header check box to
    include the header of each column in the CSV file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-creating-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise-create -->
# Creating a Job for aggregating values based on dynamic schema

Last updated: 9/30/2026

Create a Job to aggregate some task assignment data in a CSV file
based on a dynamic schema column using the tAggregateRow component, then display the aggregated data on the console and
write it into an output CSV file.

## Procedure

1. Create a new Job and add a tFileInputDelimited component, a tAggregateRow component, a tLogRow
   component, and a tFileOutputDelimited component by
   typing their names in the design workspace or dropping them from the Palette.
2. Link the tFileInputDelimited component
   to the tAggregateRow component using a Row > Main
   connection.
3. Do the same to link the tAggregateRow
   component to the tLogRow component, and the
   tLogRow component to the tFileOutputDelimited component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-executing-job-to-aggregate-values-based-on-dynamic-schema-standard-component-enterprise-press -->
# Executing the Job to aggregate values based on dynamic schema

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the
Job for aggregating the task assignment data based on a dynamic schema column, you can then
execute the Job and verify the Job execution result.

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

## Results

As shown above, the task assignment data is aggregated based on
the *other* dynamic column, and the aggregated data
is displayed on the console and written into the output CSV file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-configuring-job-for-aggregating-and-sorting-data-standard-component -->
# Configuring the Job for aggregating and sorting data

Last updated: 9/30/2026

Configure the Job to aggregate the students' comprehensive scores
using the tAggregateRow component and then sort
the aggregated data using the tSortRow
component.

## Procedure

1. Double-click the tFixedFlowInput
   component to open its Basic settings view.
2. Click the
   button next to Edit schema to
   open the schema dialog box and define the schema by adding two columns, *name* of String type and *score* of Double type. When done, click OK to save the changes and close the schema dialog box.
3. In the Mode area, select Use Inline Content (delimited file) and in the Content field displayed, enter the following input
   data:

   ```
   Peter;92
   James;93
   Thomas;91
   Peter;94
   James;96
   Thomas;95
   Peter;96
   James;92
   Thomas;98
   Peter;95
   James;96
   Thomas;93
   Peter;98
   James;97
   Thomas;95
   ```
4. Double-click the tAggregateRow
   component to open its Basic settings view.
5. Click the
   button next to Edit schema to
   open the schema dialog box and define the schema by adding five columns, *name* of String type, and *sum*, *average*, *max*, and *min* of
   Double type.

   When done, click OK to save the changes and close
   the schema dialog box.
6. Add one row in the Group by table by
   clicking the
   button below it, and select *name* from both the Output column
   and Input column position column fields to group
   the input data by the *name* column.
7. Add four rows in the Operations table
   and define the operations to be carried out. In this example, the operations are
   *sum*, *average*, *max*, and *min*. Then select *score* from all four Input column
   position column fields to aggregate the input data based on
   it.
8. Double-click the tSortRow component to
   open its Basic settings view.
9. Add one row in the Criteria table and
   specify the column based on which the sort operation is performed. In this example,
   it is the *name* column. Then select *alpha* from the sort num or
   alpha? column field and *asc* from
   the Order asc or desc? column field to sort the
   aggregated data in ascending alphabetical order.
10. Double-click the tLogRow component to
    open its Basic settings view, and then select
    Table (print values in cells of a table) in the
    Mode area for better readability of the
    result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-creating-job-for-aggregating-and-sorting-data-standard-component-create -->
# Creating a Job for aggregating and sorting data

Last updated: 9/30/2026

Create a Job to aggregate the students' comprehensive scores using the
tAggregateRow component, then sort the aggregated data
using the tSortRow component, finally display the
aggregated and sorted data on the console.

## Procedure

1. Create a new Job and add a tFixedFlowInput component, a tAggregateRow component, a tSortRow
   component, and a tLogRow component by typing their
   names in the design workspace or dropping them from the Palette.
2. Link the tFixedFlowInput component to
   the tAggregateRow component using a Row > Main
   connection.
3. Do the same to link the tAggregateRow
   component to the tSortRow component, and the
   tSortRow component to the tLogRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-executing-job-to-aggregate-and-sort-data-standard-component-press -->
# Executing the Job to aggregate and sort data

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the
Job for aggregating and sorting data, you can then execute the Job and verify the Job
execution result.

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

## Results

As shown above, the students' comprehensive scores are
aggregated and then sorted in ascending alphabetical order based on the student
names.
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties · versión 8.0 -->
# tAggregateRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tAggregateRow running
in the Standard Job framework.

The Standard
tAggregateRow component belongs to the Processing
family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Group by | * Define the aggregation sets, the values of which will be   used for calculations. * Output Column: Select the column   label in the list offered based on the schema structure you defined. You   can add as many output columns as you wish to make more precise   aggregations.  Ex: Select Country to calculate an average of values for   each country of a list or select Country and Region if you want to   compare one country's regions with another country' regions. * Input Column: Match the input   column label with your output columns, in case the output label of the   aggregation set needs to be different. |
| Operations | * Select the type of operation along with the value to use   for the calculation and the output field. * Output Column: Select the   destination field in the list.  Function: Select the operator among:   + count: calculates the number of rows   + min: selects the minimum value   + max: selects the maximum value   + avg: calculates the average   + sum: calculates the sum   + first: returns the first value   + last: returns the last value   + list: lists values of an aggregation by multiple keys.   + list (object): lists Java values of an aggregation by multiple keys   + count (distinct): counts the number of the distinct rows   + standard deviation: calculates the     variability of a set of value.   + union (geometry): makes the union of a set of Geometry objects   + population standard deviation: calculates the     spread of a data distribution. Use this function if the data to be     calculated is considered a population on its own. This calculation     supports 39 decimal places.   + sample     standard deviation: calculates the spread of a data     distribution. Use this function if the data to be calculated is     considered a sample from a larger population. This calculation     supports 39 decimal places. * Input column: Select the input   column from which the values are taken to be aggregated. * Ignore null values: Select the   check boxes corresponding to the names of the columns for which you want   the NULL value to be ignored. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Delimiter(only for list operation) | Enter the delimiter you want to use to separate the different operations. |
| Use financial precision, this is the max precision for "sum" and "avg" operations, checked option heaps more memory and slower than unchecked. | Select this check box to use a financial precision. This is a max precision but consumes more memory and slows the processing.  Information noteWarning: *We advise you to use the BigDecimal type for the output in order to obtain precise results.* |
| Check type overflow (slower) | Checks the type of data to ensure that the Job doesn't crash. |
| Check ULP (Unit in the Last Place), ensure that a value will be incremented or decremented correctly, only float and double types. (slower) | Select this check box to ensure the most precise results possible for the Float and Double types. |
| tStatCatcher Statistics | Check this box to collect the log data at component level. Note that this check box is not available in the Map/Reduce version of the component. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles flow of data therefore it requires input and output, hence is defined as an intermediary step. Usually the use of tAggregateRow is combined with the tSortRow component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow -->
# tAggregateRow

Last updated: 9/30/2026

Receives a flow and aggregates it based on one or more columns.

For each output line, are provided the aggregation key and the relevant
result of set operations (min, max, sum...).

tAggregateRow helps to provide a set of metrics based on values or
calculations.

### In this section

* [tAggregateRow Standard properties](/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
* [tAggregateRow properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-batch)
* [tAggregateRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-streaming)
* [tAggregateRow properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Aggregating values and sorting data](taggregaterow-tsortrow-tfixedflowinput-tlogrow-aggregating-values-and-sorting-data-standard-component "This example shows you how to use Talend components to aggregate the students' comprehensive scores and then sort the aggregated scores based on the student names.")
* [Aggregating values based on dynamic schema](taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-aggregating-values-based-on-dynamic-schema-standard-component-enterprise "Here is an example of using the tAggregateRow component to aggregate some task assignment data in a CSV file based on a dynamic schema column.")
* [Performing download analysis using a Spark Batch Job](tcacheout-textractdelimitedfields-ts3configuration-performing-download-analysis-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-batch -->
# tAggregateRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tAggregateRow running in the Spark Batch Job framework.

The Spark Batch
tAggregateRow component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Information noteTip: By default, when Spark aggregates BigDecimal, the   precision and scale are set at the maximum values of the data type.   You can change the scale and the precision for BigDecimal in the   corresponding columns of the schema. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Group by | * Define the aggregation sets, the values of which will be used for   calculations. * Output Column: Select the column   label in the list offered based on the schema structure you defined. You   can add as many output columns as you wish to make more precise   aggregations.  Ex: Select Country to calculate an average of values for each country   of a list or select Country and Region if you want to compare one   country's regions with another country' regions. * Input Column: Match the input column   label with your output columns, in case the output label of the   aggregation set needs to be different. |
| Operations | * Select the type of operation along with the value to use for the   calculation and the output field. * Output Column: Select the destination   field in the list.  Function: Select the operator among: * Input column: Select the input column   from which the values are taken to be aggregated. * Ignore null values: Select the check   boxes corresponding to the names of the columns for which you want the   NULL value to be ignored. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use financial precision, this is the max precision for "sum" and "avg" operations, checked option heaps more memory and slower than unchecked. | Select this check box to use a financial precision. This is a max precision but consumes more memory and slows the processing.  Information noteWarning: *We advise you to use the BigDecimal type for the output in order to obtain precise results.* |
| Check type overflow (slower) | Checks the type of data to ensure that the Job doesn't crash. |
| Check ULP (Unit in the Last Place), ensure that a value will be incremented or decremented correctly, only float and double types. (slower) | Select this check box to ensure the most precise results possible for the Float and Double types. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-properties-for-apache-spark-structured-streaming -->
# tAggregateRow properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tAggregateRow running in
the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tAggregateRow component belongs to the Processing family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Group by | Define the aggregation sets whose values are used for calculations. Output Column: Select the column label from the list based on the schema structure you defined. Add as many output columns as needed to refine the aggregation. For example, select Country to calculate an average for each country, or select Country and Region to compare regions across countries.  Input Column: Match the input column label to the output column when the aggregation set needs a different output label. |
| Operations | Select the type of operation to perform along with the input value and the output field. Output Column: Select the destination field from the list.  Function: Select the operator among:  Input column: Select the input column whose values are aggregated.  Ignore null values: Select the check boxes for the columns where NULL values should be ignored. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-aggregating-values-based-on-dynamic-schema-standard-component-enterprise -->
# Aggregating values based on dynamic schema

Last updated: 9/30/2026

Here is an example of using the tAggregateRow component to aggregate some task assignment data in a CSV file
based on a dynamic schema column.

This scenario applies only to subscription-based Talend
products.

### In this section

* [Creating a Job for aggregating values based on dynamic schema](/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-creating-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise-create)
* [Configuring the Job for aggregating values based on dynamic schema](/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-configuring-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise)
* [Executing the Job to aggregate values based on dynamic schema](/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-executing-job-to-aggregate-values-based-on-dynamic-schema-standard-component-enterprise-press)

**Related concepts**  

* [tAggregateRow](taggregaterow "Receives a flow and aggregates it based on one or more columns.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-aggregating-values-and-sorting-data-standard-component -->
# Aggregating values and sorting data

Last updated: 9/30/2026

This example shows you how to use Talend components
to aggregate the students' comprehensive scores and then sort the aggregated scores based on
the student names.

### In this section

* [Creating a Job for aggregating and sorting data](/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-creating-job-for-aggregating-and-sorting-data-standard-component-create)
* [Configuring the Job for aggregating and sorting data](/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-configuring-job-for-aggregating-and-sorting-data-standard-component)
* [Executing the Job to aggregate and sort data](/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-executing-job-to-aggregate-and-sort-data-standard-component-press)

**Related concepts**  

* [tAggregateRow](taggregaterow "Receives a flow and aggregates it based on one or more columns.")
* [tSortRow](tsortrow "Helps creating metrics and classification table.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-configuring-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise -->
# Configuring the Job for aggregating values based on dynamic schema

Last updated: 9/30/2026

Configure the Job to aggregate some task assignment data in a CSV
file based on a dynamic schema column using the tAggregateRow component.

Then this Job displays the aggregated data on the console
using the tLogRow component and writes it into an
output CSV file using the tFileOutputDelimited
component.

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Basic settings view.
2. In the File name/Stream field, specify
   the path to the CSV file that holds the following task assignment data, *D:/tasks.csv* in this example.

   ```
   task;team;status
   task1;team1;done
   task2;team2;done
   task3;team1;done
   task4;team2;pending
   task5;team1;pending
   task6;team2;pending
   ```
3. In the Header field, enter the number
   of rows to be skipped in the beginning of the file, *1* in this example.

   Note that the dynamic schema feature is only supported in the Built-In mode and requires the input file to have a
   header row.
4. Click the
   button next to Edit schema to
   open the schema dialog box and define the schema by adding two columns, *task* of String type and *other* of Dynamic type. When done, click OK to save the changes and close the schema dialog box.

   Note that the dynamic column must be defined in the last row of
   the schema. For more information about dynamic schema, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).
5. Double-click the tAggregateRow
   component, and on its Basic settings view, click
   the Sync columns button to retrieve the schema from
   the preceding component.
6. Add one row in the Group by table by
   clicking the
   button below it, and select *other* from both the Output column
   and Input column position column fields to group
   the input data by the *other* dynamic
   column.

   Note that the dynamic column aggregation can be carried out only for the grouping
   operation.
7. Add one row in the Operations table
   and define the operation to be carried out. In this example, the operation function
   is *list*. Then select *task* from both the Output column
   and Input column position column fields to list the
   entries in the *task* column in the grouping result.
8. Double-click the tLogRow component to
   open its Basic settings view, and then select
   Table (print values in cells of a table) in the
   Mode area for better readability of the
   result.
9. Double-click the tFileOutputDelimited
   component to open its Basic settings view, and in
   the File Name field, specify the path to the CSV
   file into which the aggregated data will be written, *D:/tasks\_aggregated.csv* in this example.
10. Select the Include Header check box to
    include the header of each column in the CSV file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-creating-job-for-aggregating-values-based-on-dynamic-schema-standard-component-enterprise-create -->
# Creating a Job for aggregating values based on dynamic schema

Last updated: 9/30/2026

Create a Job to aggregate some task assignment data in a CSV file
based on a dynamic schema column using the tAggregateRow component, then display the aggregated data on the console and
write it into an output CSV file.

## Procedure

1. Create a new Job and add a tFileInputDelimited component, a tAggregateRow component, a tLogRow
   component, and a tFileOutputDelimited component by
   typing their names in the design workspace or dropping them from the Palette.
2. Link the tFileInputDelimited component
   to the tAggregateRow component using a Row > Main
   connection.
3. Do the same to link the tAggregateRow
   component to the tLogRow component, and the
   tLogRow component to the tFileOutputDelimited component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tlogrow-tfileoutputdelimited-tfileinputdelimited-executing-job-to-aggregate-values-based-on-dynamic-schema-standard-component-enterprise-press -->
# Executing the Job to aggregate values based on dynamic schema

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the
Job for aggregating the task assignment data based on a dynamic schema column, you can then
execute the Job and verify the Job execution result.

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

## Results

As shown above, the task assignment data is aggregated based on
the *other* dynamic column, and the aggregated data
is displayed on the console and written into the output CSV file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-configuring-job-for-aggregating-and-sorting-data-standard-component -->
# Configuring the Job for aggregating and sorting data

Last updated: 9/30/2026

Configure the Job to aggregate the students' comprehensive scores
using the tAggregateRow component and then sort
the aggregated data using the tSortRow
component.

## Procedure

1. Double-click the tFixedFlowInput
   component to open its Basic settings view.
2. Click the
   button next to Edit schema to
   open the schema dialog box and define the schema by adding two columns, *name* of String type and *score* of Double type. When done, click OK to save the changes and close the schema dialog box.
3. In the Mode area, select Use Inline Content (delimited file) and in the Content field displayed, enter the following input
   data:

   ```
   Peter;92
   James;93
   Thomas;91
   Peter;94
   James;96
   Thomas;95
   Peter;96
   James;92
   Thomas;98
   Peter;95
   James;96
   Thomas;93
   Peter;98
   James;97
   Thomas;95
   ```
4. Double-click the tAggregateRow
   component to open its Basic settings view.
5. Click the
   button next to Edit schema to
   open the schema dialog box and define the schema by adding five columns, *name* of String type, and *sum*, *average*, *max*, and *min* of
   Double type.

   When done, click OK to save the changes and close
   the schema dialog box.
6. Add one row in the Group by table by
   clicking the
   button below it, and select *name* from both the Output column
   and Input column position column fields to group
   the input data by the *name* column.
7. Add four rows in the Operations table
   and define the operations to be carried out. In this example, the operations are
   *sum*, *average*, *max*, and *min*. Then select *score* from all four Input column
   position column fields to aggregate the input data based on
   it.
8. Double-click the tSortRow component to
   open its Basic settings view.
9. Add one row in the Criteria table and
   specify the column based on which the sort operation is performed. In this example,
   it is the *name* column. Then select *alpha* from the sort num or
   alpha? column field and *asc* from
   the Order asc or desc? column field to sort the
   aggregated data in ascending alphabetical order.
10. Double-click the tLogRow component to
    open its Basic settings view, and then select
    Table (print values in cells of a table) in the
    Mode area for better readability of the
    result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-creating-job-for-aggregating-and-sorting-data-standard-component-create -->
# Creating a Job for aggregating and sorting data

Last updated: 9/30/2026

Create a Job to aggregate the students' comprehensive scores using the
tAggregateRow component, then sort the aggregated data
using the tSortRow component, finally display the
aggregated and sorted data on the console.

## Procedure

1. Create a new Job and add a tFixedFlowInput component, a tAggregateRow component, a tSortRow
   component, and a tLogRow component by typing their
   names in the design workspace or dropping them from the Palette.
2. Link the tFixedFlowInput component to
   the tAggregateRow component using a Row > Main
   connection.
3. Do the same to link the tAggregateRow
   component to the tSortRow component, and the
   tSortRow component to the tLogRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-tsortrow-tfixedflowinput-tlogrow-executing-job-to-aggregate-and-sort-data-standard-component-press -->
# Executing the Job to aggregate and sort data

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the
Job for aggregating and sorting data, you can then execute the Job and verify the Job
execution result.

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

## Results

As shown above, the students' comprehensive scores are
aggregated and then sorted in ascending alphabetical order based on the student
names.
