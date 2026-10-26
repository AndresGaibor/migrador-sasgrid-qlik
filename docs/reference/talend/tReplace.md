<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/treplace · versión 8.0 -->
# tReplace

Last updated: 9/30/2026

Cleanses all files before further processing.

Carries out a Search &
Replace operation in the input columns defined.

### In this section

* [tReplace Standard properties](/talend/en-US/components/8.0/processing/treplace-standard-properties)
* [tReplace properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/treplace-properties-for-apache-spark-batch)
* [tReplace properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/treplace-properties-for-apache-spark-streaming)

**Related concepts**  

* [Cleaning up and filtering a CSV file](treplace-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-cleaning-up-and-filtering-csv-file-standard-component-thi)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/treplace-properties-for-apache-spark-batch -->
# tReplace properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tReplace running in the Spark Batch Job framework.

The Spark Batch
tReplace component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Simple Mode Search / Replace | Click the button to add as many conditions as needed. The conditions are performed one after the other for each row.  Input column: Select the column of the schema the search & replace is to be operated on  Search: Type in the value to search in the input column  Replace with: Type in the substitution value.  Whole word: Select this check box if the searched value is to be considered as whole.  Case sensitive: Select this check box to care about the case.  Note that you cannot use regular expression in these columns. |
| Advanced mode | Select this check box when the operation you want to perform cannot be carried out through the simple mode. In the text field, type in the regular expression as required. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/treplace-standard-properties -->
# tReplace Standard properties

Last updated: 9/30/2026

These properties are used to configure tReplace running in the Standard Job framework.

The Standard
tReplace component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Two read-only columns, Value and Match are added to the output   schema automatically. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Simple Mode Search / Replace | Click the button to add as many conditions as needed. The conditions are performed one after the other for each row.  Input column: Select the column of the schema the search & replace is to be operated on  Search: Type in the value to search in the input column  Replace with: Type in the substitution value.  Whole word: Select this check box if the searched value is to be considered as whole.  Case sensitive: Select this check box to care about the case.  Note that you cannot use regular expression in these columns. |
| Use advanced mode | Select this check box when the operation you want to perform cannot be carried out through the simple mode. In the text field, type in the regular expression as required. |

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
| **Usage rule** | This component is not startable as it requires an input flow. And it requires an output component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/treplace-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-cleaning-up-and-filtering-csv-file-standard-component-thi -->
# Cleaning up and filtering a CSV file

Last updated: 9/30/2026

This Job searches and replaces various typos and defects in a csv
file then operates a column filtering before producing a new csv file with the final
output.

* Drop the following components from the Palette onto the design workspace: tFileInputDelimited, tReplace, tFilterColumn
  and tFileOutputDelimited.
* Connect the components using Main
  Row connections via a right-click each component.
* Select the tFileInputDelimited component and set the input flow
  parameters.

* The File is a simple csv
  file stored locally. The Row Separator is
  a carriage return and the Field Separator
  is a semi-colon. In the Header is the name
  of the column, and no Footer nor
  Limit are to be set.
* The file contains characters such as: \*t,
  . or Nikson which we want to turn
  into Nixon, and streat, which we want to turn into Street.

* The schema for this file is built in also and made of four
  columns of various types (string or int).
* Now select the tReplace
  component to set the search & replace parameters.

* The schema can be synchronized with the incoming flow.
* Select the Simple mode
  check box as the search parameters can be easily set without requiring the use
  of regexp.
* Click the plus sign to add some lines to the parameters table.
* On the first parameter line, select *Amount* as InputColumn. Type *"."* in the Search
  field, and *","* in the Replace field.
* On the second parameter line, select *Street* as InputColumn. Type *"streat"* in the Search field, and *"Street"* in the
  Replace field.
* On the third parameter line, select again *Amount* as InputColumn. Type *"$"* in the Search
  field, and *"£"* in the Replace field.
* On the fourth paramater line, select *Name*
  as InputColumn. Type *"Nikson"* in the Search field,
  and *"Nixon"* in the Replace field.
* On the fifth parameter line, select *Firstname* as InputColumn. Type
  *"\*t"* in the Search field, and replace them with nothing between double
  quotes.
* The advanced mode isn't used in this scenario.
* Select the next component in the Job, tFilterColumn.

* The tFilterColumn
  component holds a schema editor allowing to build the output schema based on the
  column names of the input schema. In this use case, add one new column named *empty\_field* and change the order of the input schema
  columns to obtain a schema as follows: *empty\_field,
  Firstname, Name, Street, Amount*.
* Click OK to validate.

* Set the tFileOutputDelimited properties manually.
* The schema is built-in for this scenario, and comes from the
  preceding component in the Job.
* Save the Job and press F6
  to execute it.

The first column is empty, the rest of the columns have been cleaned up
from the parasitical characters, and *Nikson* was replaced with *Nixon*. The street column was moved and the decimal delimiter has
been changed from a dot to a comma, along with the currency sign.

**Related concepts**  

* [tReplace](treplace "Cleanses all files before further processing.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
