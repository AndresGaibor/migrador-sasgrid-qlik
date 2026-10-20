<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow · versión 8.0 -->
# tLogRow

Last updated: 9/30/2026

Displays data or results in the Run console
to monitor data processed.

### In this section

* [tLogRow Standard properties](/talend/en-US/components/8.0/logs-and-errors/tlogrow-standard-properties)
* [tLogRow properties for Apache Spark Batch](/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-batch)
* [tLogRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-streaming)
* [tLogRow properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Catching flow metrics from a Job](tflowmeter-tflowmetercatcher-tmysqlinput-catching-flow-metrics-from-job-standard-component-the)
* [Catching messages triggered by a tWarn component](twarn-tlogcatcher-tlogrow-trowgenerator-catching-messages-triggered-by-twarn-component-standard-component "This example shows you how to use the tLogCatcher component to catch the messages triggered by a tWarn component.")
* [Catching the message triggered by a tDie component](tdie-tlogcatcher-tjava-catching-message-triggered-by-tdie-component-standard-component "This example shows you how to use the tLogCatcher component to catch the message triggered by a tDie component.")
* [Displaying the statistics log of Job execution](tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-displaying-statistics-log-of-job-execution-standard-component-this)
* [Setting up the assertive condition for a Job execution](tassert-tassertcatcher-tfileoutputdelimited-setting-up-assertive-condition-for-job-execution-standard-component-this)
* [Viewing product orders status (on a daily basis) against a benchmark number](tassert-tlogrow-tmysqloutput-viewing-product-orders-status-on-daily-basis-against-benchmark-number-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-batch -->
# tLogRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tLogRow running in the Spark Batch Job framework.

The Spark Batch
tLogRow component belongs to the Misc family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function is available only when the component is linked with the preceding component using a Row connection. |
| Basic | Displays the output flow in basic mode. |
| Table | Displays the output flow in table cells. |
| Vertical | Displays each row of the output flow as a key-value list.  With this mode selected, you can choose to show either the unique name or the label of component, or both of them, for each output row. |
| Separator  (For Basic mode only) | Enter the separator which will delimit data on the Log display. |
| Print header  (For Basic mode only) | Select this check box to include the header of the input flow in the output display. |
| Print component unique name in front of each output row  (For Basic mode only) | Select this check box to show the unique name the component in front of each output row to differentiate outputs in case several tLogRow components are used. |
| Print schema column name in front of each value  (For Basic mode only) | Select this check box to retrieve column labels from output schema. |
| Use fixed length for values  (For Basic mode only) | Select this check box to set a fixed width for the value display. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate or an end step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-structured-streaming -->
# tLogRow properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tLogRow running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tLogRow component belongs to the Misc family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Basic | Displays the output flow in Basic mode. The following properties are available in this mode:  * Field Separator: Enter the separator to delimit data in the log display. * Print header: Select this check box to include the header of the input flow in the output display. * Print component unique name in front of each output row: Select this check box to show the unique name of the component in front of each output row, to differentiate outputs when several tLogRow components are used. * Print schema column name in front of each value: Select this check box to retrieve column labels from the output schema. * Use fixed length for values: Select this check box to use a fixed length for the value display. |
| Table | Displays the output flow in table cells. |
| Vertical | Displays each row of the output flow as a key-value list. Select how to identify each output row in the Title printing mode field:  * Print unique name: Shows the unique name of the component. * Print label: Shows the label of the component. * Print unique name and label: Shows both the unique name and the label. |
| Output mode | Select the output mode from the drop-down list:  * Append: Adds new rows to the output without   modifying existing rows. * Complete: Overwrites the entire output with the   updated result after every trigger. * Update: Writes only the rows that were updated since   the last trigger.   Information noteNote: When groupBy is enabled, set the output mode to Complete or Update. If groupBy is not used, set the output mode to Append. |
| Set trigger | Select this check box to set a trigger for the streaming query:  * Available now: Processes all available data and stops. * Fixed interval: Processes data at a fixed time interval. In the Duration field, enter the interval. For example, 10 seconds. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate or an end step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-standard-properties -->
# tLogRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tLogRow running in the Standard Job framework.

The Standard
tLogRow component belongs to the Logs & Errors family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function is available only when the component is linked with the preceding component using a Row connection. |
| Basic | Displays the output flow in basic mode. |
| Table | Displays the output flow in table cells. |
| Vertical | Displays each row of the output flow as a key-value list.  With this mode selected, you can choose to show either the unique name or the label of component, or both of them, for each output row. |
| Separator  (For Basic mode only) | Enter the separator which will delimit data on the Log display. |
| Print header  (For Basic mode only) | Select this check box to include the header of the input flow in the output display. |
| Print component unique name in front of each output row  (For Basic mode only) | Select this check box to show the unique name the component in front of each output row to differentiate outputs in case several tLogRow components are used. |
| Print schema column name in front of each value  (For Basic mode only) | Select this check box to retrieve column labels from output schema. |
| Use fixed length for values  (For Basic mode only) | Select this check box to set a fixed width for the value display. |
| Print content with log4j | Select this check box to output the data flow content if the log4j feature is activated and the log4j output level is set to INFO or lower than INFO for your Job. For how to activate the log4j feature and customize the log4j output level, refer to *Talend Studio*  *User Guide*. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as intermediate step in a data flow or as an end object in the Job flowchart. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-displaying-statistics-log-of-job-execution-standard-component-this -->
# Displaying the statistics log of Job execution

Last updated: 9/30/2026

This scenario collects the statistics log for the Job execution and displays it on the
Run console. Note that, since the tStatCatcher
Statistics check box is not selected for the components, the statistics log applies
solely to this specific Job.

### In this section

* [Linking the components](/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-executing-job-standard-component-press)

**Related concepts**  

* [tLogRow](tlogrow "Displays data or results in the Run console to monitor data processed.")

**Related reference**  

* [tStatCatcher](tstatcatcher "Gathers the Job processing metadata at the Job level and at the component level and transfers the log data to the subsequent component for display or storage.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the Edit schema button to open the
   schema editor.
3. Click the [+] button to add three
   columns, namely *ID\_Owners*, *Name\_Customer* and *ID\_Insurance*, of the Integer and String types respectively.
4. Click Ok to validate the setup and close
   the editor.
5. In the dialog box that appears, click Yes
   to propagate the changes to the subsequent component.
6. Select the Use Inline Content (delimited
   file) option.
7. In the Content box, enter
   1;Andrew;888.
8. Double-click tFileOutputDelimited to open
   its Basic settings view.
9. In the File Name field, enter the full
   name of the file to save the statistics data.
10. Double-click tLogRow to open its
    Basic settings view.
11. Select Vertical (each row is a key/value
    list) for a better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, the statistics log of the Job execution is correctly
   generated.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tFixedFlowInput, tFileOutputDelimited, tStatCatcher and tLogRow
   onto the workspace.
2. Link tFixedFlowInput to tFileOutputDelimited using a Row > Main
   connection.
3. Link tStatCatcher to tLogRow using a Row > Main
   connection.
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-standard-properties · versión 8.0 -->
# tLogRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tLogRow running in the Standard Job framework.

The Standard
tLogRow component belongs to the Logs & Errors family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function is available only when the component is linked with the preceding component using a Row connection. |
| Basic | Displays the output flow in basic mode. |
| Table | Displays the output flow in table cells. |
| Vertical | Displays each row of the output flow as a key-value list.  With this mode selected, you can choose to show either the unique name or the label of component, or both of them, for each output row. |
| Separator  (For Basic mode only) | Enter the separator which will delimit data on the Log display. |
| Print header  (For Basic mode only) | Select this check box to include the header of the input flow in the output display. |
| Print component unique name in front of each output row  (For Basic mode only) | Select this check box to show the unique name the component in front of each output row to differentiate outputs in case several tLogRow components are used. |
| Print schema column name in front of each value  (For Basic mode only) | Select this check box to retrieve column labels from output schema. |
| Use fixed length for values  (For Basic mode only) | Select this check box to set a fixed width for the value display. |
| Print content with log4j | Select this check box to output the data flow content if the log4j feature is activated and the log4j output level is set to INFO or lower than INFO for your Job. For how to activate the log4j feature and customize the log4j output level, refer to *Talend Studio*  *User Guide*. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as intermediate step in a data flow or as an end object in the Job flowchart. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow -->
# tLogRow

Last updated: 9/30/2026

Displays data or results in the Run console
to monitor data processed.

### In this section

* [tLogRow Standard properties](/talend/en-US/components/8.0/logs-and-errors/tlogrow-standard-properties)
* [tLogRow properties for Apache Spark Batch](/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-batch)
* [tLogRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-streaming)
* [tLogRow properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Catching flow metrics from a Job](tflowmeter-tflowmetercatcher-tmysqlinput-catching-flow-metrics-from-job-standard-component-the)
* [Catching messages triggered by a tWarn component](twarn-tlogcatcher-tlogrow-trowgenerator-catching-messages-triggered-by-twarn-component-standard-component "This example shows you how to use the tLogCatcher component to catch the messages triggered by a tWarn component.")
* [Catching the message triggered by a tDie component](tdie-tlogcatcher-tjava-catching-message-triggered-by-tdie-component-standard-component "This example shows you how to use the tLogCatcher component to catch the message triggered by a tDie component.")
* [Displaying the statistics log of Job execution](tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-displaying-statistics-log-of-job-execution-standard-component-this)
* [Setting up the assertive condition for a Job execution](tassert-tassertcatcher-tfileoutputdelimited-setting-up-assertive-condition-for-job-execution-standard-component-this)
* [Viewing product orders status (on a daily basis) against a benchmark number](tassert-tlogrow-tmysqloutput-viewing-product-orders-status-on-daily-basis-against-benchmark-number-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-batch -->
# tLogRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tLogRow running in the Spark Batch Job framework.

The Spark Batch
tLogRow component belongs to the Misc family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function is available only when the component is linked with the preceding component using a Row connection. |
| Basic | Displays the output flow in basic mode. |
| Table | Displays the output flow in table cells. |
| Vertical | Displays each row of the output flow as a key-value list.  With this mode selected, you can choose to show either the unique name or the label of component, or both of them, for each output row. |
| Separator  (For Basic mode only) | Enter the separator which will delimit data on the Log display. |
| Print header  (For Basic mode only) | Select this check box to include the header of the input flow in the output display. |
| Print component unique name in front of each output row  (For Basic mode only) | Select this check box to show the unique name the component in front of each output row to differentiate outputs in case several tLogRow components are used. |
| Print schema column name in front of each value  (For Basic mode only) | Select this check box to retrieve column labels from output schema. |
| Use fixed length for values  (For Basic mode only) | Select this check box to set a fixed width for the value display. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate or an end step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-properties-for-apache-spark-structured-streaming -->
# tLogRow properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tLogRow running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tLogRow component belongs to the Misc family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Basic | Displays the output flow in Basic mode. The following properties are available in this mode:  * Field Separator: Enter the separator to delimit data in the log display. * Print header: Select this check box to include the header of the input flow in the output display. * Print component unique name in front of each output row: Select this check box to show the unique name of the component in front of each output row, to differentiate outputs when several tLogRow components are used. * Print schema column name in front of each value: Select this check box to retrieve column labels from the output schema. * Use fixed length for values: Select this check box to use a fixed length for the value display. |
| Table | Displays the output flow in table cells. |
| Vertical | Displays each row of the output flow as a key-value list. Select how to identify each output row in the Title printing mode field:  * Print unique name: Shows the unique name of the component. * Print label: Shows the label of the component. * Print unique name and label: Shows both the unique name and the label. |
| Output mode | Select the output mode from the drop-down list:  * Append: Adds new rows to the output without   modifying existing rows. * Complete: Overwrites the entire output with the   updated result after every trigger. * Update: Writes only the rows that were updated since   the last trigger.   Information noteNote: When groupBy is enabled, set the output mode to Complete or Update. If groupBy is not used, set the output mode to Append. |
| Set trigger | Select this check box to set a trigger for the streaming query:  * Available now: Processes all available data and stops. * Fixed interval: Processes data at a fixed time interval. In the Duration field, enter the interval. For example, 10 seconds. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate or an end step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-displaying-statistics-log-of-job-execution-standard-component-this -->
# Displaying the statistics log of Job execution

Last updated: 9/30/2026

This scenario collects the statistics log for the Job execution and displays it on the
Run console. Note that, since the tStatCatcher
Statistics check box is not selected for the components, the statistics log applies
solely to this specific Job.

### In this section

* [Linking the components](/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-executing-job-standard-component-press)

**Related concepts**  

* [tLogRow](tlogrow "Displays data or results in the Run console to monitor data processed.")

**Related reference**  

* [tStatCatcher](tstatcatcher "Gathers the Job processing metadata at the Job level and at the component level and transfers the log data to the subsequent component for display or storage.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the Edit schema button to open the
   schema editor.
3. Click the [+] button to add three
   columns, namely *ID\_Owners*, *Name\_Customer* and *ID\_Insurance*, of the Integer and String types respectively.
4. Click Ok to validate the setup and close
   the editor.
5. In the dialog box that appears, click Yes
   to propagate the changes to the subsequent component.
6. Select the Use Inline Content (delimited
   file) option.
7. In the Content box, enter
   1;Andrew;888.
8. Double-click tFileOutputDelimited to open
   its Basic settings view.
9. In the File Name field, enter the full
   name of the file to save the statistics data.
10. Double-click tLogRow to open its
    Basic settings view.
11. Select Vertical (each row is a key/value
    list) for a better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, the statistics log of the Job execution is correctly
   generated.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/logs-and-errors/tlogrow-tstatcatcher-tfixedflowinput-tfileoutputdelimited-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tFixedFlowInput, tFileOutputDelimited, tStatCatcher and tLogRow
   onto the workspace.
2. Link tFixedFlowInput to tFileOutputDelimited using a Row > Main
   connection.
3. Link tStatCatcher to tLogRow using a Row > Main
   connection.
