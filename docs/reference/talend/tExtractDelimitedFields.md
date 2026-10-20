<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields · versión 8.0 -->
# tExtractDelimitedFields

Last updated: 9/30/2026

Generates multiple columns from a delimited string column.

The extracted fields are written in new columns of the output schema. If you need to keep
the original columns in the output of this component, define these columns in the output
schema using the same column names as the original ones.

### In this section

* [tExtractDelimitedFields Standard properties](/talend/en-US/components/8.0/processing/textractdelimitedfields-standard-properties)
* [tExtractDelimitedFields properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/textractdelimitedfields-properties-for-apache-spark-batch)
* [tExtractDelimitedFields properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/textractdelimitedfields-properties-for-apache-spark-streaming)

**Related concepts**  

* [Extracting a delimited string column of a database table](textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-extracting-delimited-string-column-of-database-table-standard-component-this)
* [Performing download analysis using a Spark Batch Job](tcacheout-textractdelimitedfields-ts3configuration-performing-download-analysis-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-properties-for-apache-spark-batch -->
# tExtractDelimitedFields properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tExtractDelimitedFields running in the Spark Batch Job framework.

The Spark Batch
tExtractDelimitedFields component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Information noteNote: This component is not supported with the Databricks Serverless runtime.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit schema to make changes to   the schema. If you make changes, the schema automatically becomes built-in. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Prev.Comp.Column list | Select the column you need to extract data from. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| CSV options | Select this check box to include CSV specific parameters such as Escape char and Text enclosure. Information noteImportant: With Spark version 2.0 and onward, special characters must be escaped, that is `"\\"` and `"\""` instead of `"\"` and `"""`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Custom Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Then select the encoding to be used from the list or select Custom and define it manually. |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Trim all columns | Select this check box to remove the leading and trailing whitespaces from all columns. When this check box is cleared, the Check column to trim table is displayed, which lets you select particular columns to trim. |
| Check column to trim | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |
| Check each row structure against schema | Select this check box to check whether the total number of columns in each row is consistent with the schema. If not consistent, an error message will be displayed on the console. |
| Check date | Select this check box to check the date format strictly against the input schema. |
| Decode String for long, int, short, byte Types | Select this check box if any of your numeric types (long, integer, short, or byte type), will be parsed from a hexadecimal or octal string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-standard-properties -->
# tExtractDelimitedFields Standard properties

Last updated: 9/30/2026

These properties are used to configure tExtractDelimitedFields running in the Standard Job framework.

The Standard
tExtractDelimitedFields component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Field to split | Select an incoming field from the Field to split list to split. |
| Ignore NULL as the source data | Select this check box to ignore the Null value in the source data.  Clear this check box to generate the Null records that correspond to the Null value in the source data. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data.  Information noteNote: Since this component uses regex to split a filed and the regex syntax uses special characters as operators, make sure to precede the regex operator you use as a field separator by a double backslash. For example, you have to use "\\|" instead of "|". |
| Die on error | Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Trim column | Select this check box to remove leading and trailing whitespace from all columns. |
| Check each row structure against schema | Select this check box to check whether the total number of columns in each row is consistent with the schema. If not consistent, an error message will be displayed on the console. |
| Validate date | Select this check box to check the date format strictly against the input schema. |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles flow of data therefore it requires input and output components. It allows you to extract data from a delimited field, using a Row > Main link, and enables you to create a reject flow filtering data which type does not match the defined type. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-extracting-delimited-string-column-of-database-table-standard-component-this -->
# Extracting a delimited string column of a database table

Last updated: 9/30/2026

This scenario describes a Job that writes data including a delimited string column into a
MySQL database table and displays the data on the console, then extracts the delimited
string column into multiple columns and displays the data after extraction on the
console.

### In this section

* [Adding and linking components](/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tExtractDelimitedFields](textractdelimitedfields "Generates multiple columns from a delimited string column.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput)
* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-adding-and-linking-components-standard-component-create -->
# Adding and linking components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in the
   design workspace or dropping them from the Palette: a tFixedFlowInput
   component, a tMysqlOutput component, a
   tMysqlInput component, a tExtractDelimitedFields component, two tLogRow components.
2. Link tFixedFlowInput to tMysqlOutput using a Row >
   Main connection.
3. Do the same to link tMysqlOutput to the first
   tLogRow, link tMysqlInput to tExtractDelimitedFields, link tExtractDelimitedFields to the second tLogRow.
4. Link tFixedFlowInput to tMysqlInput using a Trigger
   > On Subjob Ok connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Populating data in a MySQL database table](/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-populating-data-in-mysql-database-table-standard-component)
* [Extracting the delimited string column in the database table into multiple columns](/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-extracting-delimited-string-column-in-database-table-into-multiple-columns-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Execute the Job by pressing F6 or clicking
   Run on the Run tab.

   As shown above, the primitive input data and the data after extraction are
   displayed on the console, and the delimited string column *DelimitedField* is extracted into three columns
   *Age*, *Team*, and *Title*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-extracting-delimited-string-column-in-database-table-into-multiple-columns-standard-component -->
# Extracting the delimited string column in the database table into multiple columns

Last updated: 9/30/2026

## Procedure

1. Double-click tMysqlInput to open its
   Basic settings view.
2. Fill the Host, Port, Database, Username, Password
   fields with the MySQL database connection information.
3. Click the [...] button next to Edit schema and in the pop-up window define the
   schema of the tMysqlInput component same as the
   schema of the tMysqlOutput component.
4. In the Table Name field, enter the name of
   the table into which the data was written. In this example, it is *employee*.
5. Click the Guess Query button to fill the
   Query field with the SQL query statement to
   be executed on the specified table. In this example, it is as follows:

   ```
   SELECT 
     `employee`.`Id`, 
     `employee`.`Name`, 
     `employee`.`DelimitedField`
   FROM `employee`
   ```
6. Double-click tExtractDelimitedFields to open
   its Basic settings view.
7. In the Field to split list, select the
   delimited string column to be extracted. In this example, it is DelimitedField.

   In the Field separator, enter the separator
   used to separate the fields in the delimited string column. In this example, it
   is *,*.
8. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding five columns: *Id* of Integer
   type, and *Name*, *Age*, *Team*, *Title* of String type.

   In this example, the delimited string column *DelimitedField* is split into three columns *Age*, *Team* and
   *Title*, and the *Id* and *Name* columns are kept
   as well.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
9. Double-click the second tLogRow to open its
   Basic settings view.

   In the Mode area, select Table (print values in cells of a table) for better
   readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractdelimitedfields-tmysqloutput-tmysqlinput-tfixedflowinput-populating-data-in-mysql-database-table-standard-component -->
# Populating data in a MySQL database table

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding three columns: *Id* of Integer
   type, and *Name* and *DelimitedField* of String type.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
3. In the Mode area, select Use Inline Content(delimited file). Then in the
   Content field displayed, enter the data to
   write to the database. This input data includes a delimited string column. In
   this example, the input data is as follows:

   ```
   1;Adam;32,Component Team,Developer
   2;Bill;28,Component Team,Tester
   3;Chris;30,Doc Team,Writer
   4;David;35,Doc Team,Leader
   5;Eddie;33,QA Team,Tester
   ```
4. Double-click tMysqlOutput to open its
   Basic settings view.
5. Fill the Host, Port, Database, Username, Password
   fields with the MySQL database connection information.
6. Fill the Table field with the name of the
   table to be written. In this example, it is *employee*.
7. Select Drop table if exists and create from
   the Action on table list.
8. Double-click the first tLogRow to open its
   Basic settings view.

   In the Mode area, select Table (print values in cells of a table) for better
   readability of the result.
