<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-extraction/textractregexfields · versión 8.0 -->
# tExtractRegexFields

Last updated: 9/30/2026

Extracts data and generates multiple columns from a formatted string using regex
matching.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tExtractRegexFields Standard properties](/talend/en-US/components/8.0/data-extraction/textractregexfields-standard-properties?id=913)
* [tExtractRegexFields properties for Apache Spark Batch](/talend/en-US/components/8.0/data-extraction/textractregexfields-properties-for-apache-spark-batch?id=914)
* [tExtractRegexFields properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/data-extraction/textractregexfields-properties-for-apache-spark-streaming?id=915)

**Related concepts**  

* [Extracting name, domain and TLD from e-mail addresses](textractregexfields-tfileinputdelimited-tlogrow-tlogrow-extracting-name-domain-and-tld-from-e-mail-addresses-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-extraction/textractregexfields-properties-for-apache-spark-batch -->
# tExtractRegexFields properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tExtractRegexFields running in the Spark Batch Job framework.

The Spark Batch
tExtractRegexFields component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Information noteNote: This component is not supported with the Databricks Serverless runtime.

## Basic settings

| Properties | Description |
| --- | --- |
| Prev.Comp.Column list | Select the column you need to extract data from. |
| Regex | Enter a regular expression according to the programming language you are using. |
| Schema  and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve the   schema from the previous component connected in the Job.  Information noteWarning: Make sure that the output schema does not contain any column with   the same name as the input column to be split. Otherwise, the   regular expression will not work as expected. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-extraction/textractregexfields-standard-properties -->
# tExtractRegexFields Standard properties

Last updated: 9/30/2026

These properties are used to configure tExtractRegexFields running in the Standard Job framework.

The Standard
tExtractRegexFields component belongs to the Data Quality and the Processing families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Field to split | Select an incoming field from the Field to split list to split. |
| Regex | Enter a regular expression according to the programming language you are using. |
| Schema  and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve   the schema from the previous component connected in the Job.  Information noteWarning: Make sure that the output schema does not contain any column   with the same name as the input column to be split. Otherwise,   the regular expression will not work as expected. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |
| Check each row structure against schema | Select this check box to check whether the total number of columns in each row is consistent with the schema. If not consistent, an error message will be displayed on the console. |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles flow of data therefore it requires input and output components. It allows you to extract data from a delimited field, using a Row > Main link, and enables you to create a reject flow filtering data which type does not match the defined type. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-extraction/textractregexfields-tfileinputdelimited-tlogrow-tlogrow-extracting-name-domain-and-tld-from-e-mail-addresses-standard-component-this -->
# Extracting name, domain and TLD from e-mail addresses

Last updated: 9/30/2026

This scenario describes a three-component Job where tExtractRegexFields is used to specify a regular
expression that corresponds to one column in the input data, *email*. The tExtractRegexFields component is
used to perform the actual regular expression matching. This regular expression includes
field identifiers for user name, domain name and Top-Level Domain (TLD) name portions in
each e-mail address. If the given e-mail address is valid, the name, domain and TLD are
extracted and displayed on the console in three separate columns. Data in the other two
input columns, *id* and *age* is extracted and
routed to destination as well.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/data-extraction/textractregexfields-tfileinputdelimited-tlogrow-tlogrow-setting-up-job-standard-component-drop?id=919)
* [Configuring the components](/talend/en-US/components/8.0/data-extraction/textractregexfields-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component?id=920)
* [Saving and executing the Job](/talend/en-US/components/8.0/data-extraction/textractregexfields-tfileinputdelimited-tlogrow-tlogrow-saving-and-executing-job-standard-component-press?id=921)

**Related concepts**  

* [tExtractRegexFields](textractregexfields "Extracts data and generates multiple columns from a formatted string using regex matching.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-extraction/textractregexfields-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Basic settings view
   in the Component tab.
2. Click the [...] button next to the
   File name/Stream field to browse to the
   file where you want to extract information from. 

   The input file used in this scenario is called *test4.*
   It is a text file that holds three columns: *id*,
   *email*, and
   *age*.

   ```
   id;email;age
   1;anna@yahoo.net;24
   2;diana@sohu.com;31
   3;fiona@gmail.org;20
   ```

   For more information, see [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited).
3. Click Edit schema to define the data
   structure of this input file.
4. Double-click the tExtractRegexFields
   component to open its Basic settings
   view.
5. Select the column to split from the Field to
   split list: *email* in this
   scenario.
6. Enter the regular expression you want to use to perform data matching in
   the Regex panel. In this scenario, the
   regular expression "([a-z]\*)@([a-z]\*).([a-z]\*)" is used to
   match the three parts of an email address: user name, domain name and TLD
   name. 

   For more information about the regular expression, see <http://en.wikipedia.org/wiki/Regular_expression>.
7. Click Edit schema to open the Schema of tExtractRegexFields dialog box, and
   click the plus button to add five columns for the output schema.

   In this scenario, we want to split the input *email*
   column into three columns in the output flow, *name,
   domain,* and *tld.* The two other input
   columns will be extracted as they are.
8. Double-click the tLogRow component to
   open its Component view.
9. In the Mode area, select Table (print values in cells of a table).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-extraction/textractregexfields-tfileinputdelimited-tlogrow-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Execute the Job by pressing F6 or
   clicking Run on the Run tab.

## Results

The tExtractRegexFields component matches all
given e-mail addresses with the defined regular expression and extracts the name,
domain, and TLD names and displays them on the console in three separate columns.
The two other columns, *id* and *age*, are
extracted as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-extraction/textractregexfields-tfileinputdelimited-tlogrow-tlogrow-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFileInputDelimited, tExtractRegexFields, and tLogRow.
2. Connect tFileInputDelimited to tExtractRegexFields using a Row >  Main link, and do
   the same to connect tExtractRegexFields to
   tLogRow.
