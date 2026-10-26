<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractpositionalfields · versión 8.0 -->
# tExtractPositionalFields

Last updated: 9/30/2026

Extracts data and generates multiple columns from a formatted string using
positional fields.

tExtractPositionalFields generates multiple columns from one
column using positional fields.

### In this section

* [tExtractPositionalFields Standard properties](/talend/en-US/components/8.0/processing/textractpositionalfields-standard-properties)
* [tExtractPositionalFields properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/textractpositionalfields-properties-for-apache-spark-batch)
* [tExtractPositionalFields properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/textractpositionalfields-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractpositionalfields-properties-for-apache-spark-batch -->
# tExtractPositionalFields properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tExtractPositionalFields running in the Spark Batch Job framework.

The Spark Batch
tExtractPositionalFields component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Information noteNote: This component is not supported with the Databricks Serverless runtime.

## Basic settings

| Properties | Description |
| --- | --- |
| Prev.Comp.Column list | Select an incoming field from the Field list to extract. |
| Customize | Select this check box to customize the data format of the positional file and define the table columns:  Column: Select the column you want to customize.  Size: Enter the column size.  Padding char: Type in between inverted commas the padding character used, in order for it to be removed from the field. A space by default.  Alignment: Select the appropriate alignment parameter. |
| Pattern | Enter the pattern to use as basis for the extraction.  A pattern is length values separated by commas, interpreted as a string between quotes. Make sure the values entered in this fields are consistent with the schema defined. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Trim Column | Select this check box to remove leading and trailing whitespace from all columns. |
| Check each row structure against schema | Select this check box to check whether the total number of columns in each row is consistent with the schema. If not consistent, an error message will be displayed on the console. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractpositionalfields-standard-properties -->
# tExtractPositionalFields Standard properties

Last updated: 9/30/2026

These properties are used to configure
tExtractPositionalFields running in the
Standard Job framework.

The Standard
tExtractPositionalFields component belongs to the
Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Field | Select an incoming field from the Field list to extract. |
| Ignore NULL as the source data | Select this check box to ignore the Null value in the source data.  Clear this check box to generate the Null records that correspond to the Null value in the source data. |
| Customize | Select this check box to customize the data format of the positional file and define the table columns:  Column: Select the column you want to customize.  Size: Enter the column size.  Padding char: Type in between inverted commas the padding character used, in order for it to be removed from the field. A space by default.  Alignment: Select the appropriate alignment parameter. |
| Pattern | Enter the pattern to use as basis for the extraction.  A pattern is length values separated by commas, interpreted as a string between quotes. Make sure the values entered in this fields are consistent with the schema defined. |
| Die on error | Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Trim Column | Select this check box to remove leading and trailing whitespace from all columns. |
| Check each row structure against schema | Select this check box to check whether the total number of columns in each row is consistent with the schema. If not consistent, an error message will be displayed on the console. |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  The NB\_LINE variable is not available to the Map/Reduce version.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles flow of data therefore it requires input and output components. It allows you to extract data from a delimited field, using a Row > Main link, and enables you to create a reject flow filtering data which type does not match the defined type. |
