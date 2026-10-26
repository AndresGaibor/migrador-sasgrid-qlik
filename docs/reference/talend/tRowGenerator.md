<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator · versión 8.0 -->
# tRowGenerator

Last updated: 9/30/2026

### In this section

* [tRowGenerator component](/talend/en-US/components/8.0/trowgenerator/trowgenerator-component)
* [tRowGenerator scenario](/talend/en-US/components/8.0/trowgenerator/trowgenerator-scenario)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator/trowgenerator-component -->
# tRowGenerator component

Last updated: 9/30/2026

| [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator) | Creates an input flow in a Job for testing purposes, in particular for boundary test sets. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator/trowgenerator -->
# tRowGenerator

Last updated: 9/30/2026

Creates an input flow in a Job for testing purposes, in particular for boundary
test sets.

tRowGenerator generates as many rows and fields as are required
using random values taken from a list.

### In this section

* [tRowGenerator Standard properties](/talend/en-US/components/8.0/trowgenerator/trowgenerator-standard-properties)
* [tRowGenerator properties for Apache Spark Batch](/talend/en-US/components/8.0/trowgenerator/trowgenerator-properties-for-apache-spark-batch)
* [tRowGenerator properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/trowgenerator/trowgenerator-properties-for-apache-spark-streaming)

**Related tasks**  

* [Generating random Java data](trowgenerator-tlogrow-generating-random-java-data-standard-component-the "The following scenario creates a two-component Job, generating 50 rows structured as follows: a randomly picked-up ID in a 1-to-3 range, a random ascii First Name and Last Name generation and a random date taken in a defined range.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator/trowgenerator-properties-for-apache-spark-batch -->
# tRowGenerator properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tRowGenerator running in the Spark Batch Job framework.

The Spark Batch
tRowGenerator component belongs to the Misc family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   The schema of tRowGenerator does not support the Object type.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| RowGenerator editor | The editor allows you to define the columns and the nature of data to be generated. You can use predefined routines or type in the function to be used to generate the data specified. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator/trowgenerator-standard-properties -->
# tRowGenerator Standard properties

Last updated: 9/30/2026

These properties are used to configure tRowGenerator running in
the Standard Job framework.

The Standard
tRowGenerator component belongs to the Misc family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| RowGenerator editor | The editor allows you to define the columns and the nature of data to be generated. You can use predefined routines or type in the function to be used to generate the data specified. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rules | The tRowGenerator Editor's ease of use allows users without any Java knowledge to generate random data for test purposes. Information noteNote: When running on Java 17 or later, the getAsciiRandomString function uses the SHA1PRNG algorithm to generate random strings, restoring the performance of earlier Java versions. If SHA1PRNG is unavailable in your runtime environment, the component falls back to the JDK or OS default algorithm automatically. |

### In this section

* [Defining the schema](/talend/en-US/components/8.0/trowgenerator/trowgenerator-trowgenerator-defining-schema-standard-component-first)
* [Defining the function](/talend/en-US/components/8.0/trowgenerator/trowgenerator-trowgenerator-defining-function-standard-component-select)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator/trowgenerator-tlogrow-generating-random-java-data-standard-component-the -->
# Generating random Java data

Last updated: 9/30/2026

The following scenario creates a two-component Job, generating 50 rows structured
as follows: a randomly picked-up ID in a 1-to-3 range, a random ascii First Name and Last
Name generation and a random date taken in a defined range.

## Procedure

1. Place a tRowGenerator and a tLogRow
   component from the Palette to the design workspace.
2. Right-click tRowGenerator and select
   Row > Main. Drag this main row
   link onto the tLogRow component and release when the plug
   symbol displays.
3. Double-click tRowGenerator to open the Editor.
4. Define the fields to be generated. 

   * The random ID column is of integer type, the First and Last names are of
     string type and the Date is of date type.
   * In the Function list, select the relevant function or
     set on the three dots for custom function.
   * On the Function parameters tab, define the Values to
     be randomly picked up.
   * First\_Name and Last\_Name columns
     are to be generated using the getAsciiRandomString function that is
     predefined in the system routines. By default, the length defined is 6
     characters long. You can change this if need be.
   * The Date column calls the predefined getRandomDate
     function. You can edit the parameter values in the Function
     parameters tab.
5. Set the Number of Rows to be generated to 50.
6. Click OK to validate the setting.
7. Double-click tLogRow to view the Basic settings. The default
   setting is retained for this Job.
8. Press F6 to run the Job.

   The 50 rows are generated following the setting defined in the
   tRowGenerator editor and the output is
   displayed in the Run console.

**Related concepts**  

* [tRowGenerator](trowgenerator "Creates an input flow in a Job for testing purposes, in particular for boundary test sets.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator/trowgenerator-trowgenerator-defining-function-standard-component-select -->
# Defining the function

Last updated: 9/30/2026

Select the [...] under Function in the Schema definition panel in order to customize the
function parameters.

* Select the Function parameters
  tab.
* The Parameter area displays
  Customized parameter as function name
  (read-only).

* In the Value area, type in the Java
  function to be used to generate the data specified.
* Click on the Preview tab and click
  Preview to check out a sample of the
  data generated.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trowgenerator/trowgenerator-trowgenerator-defining-schema-standard-component-first -->
# Defining the schema

Last updated: 9/30/2026

First you need to define the structure of data to be generated.

* Add as many columns to your schema as needed, using the (+) button.
* Type in the names of the columns to be created in the Columns area and select the Key check box if required
* Make sure you define then the nature of the data contained in the column,
  by selecting the Type in the list.
  According to the type you select, the list of Functions offered will differ. This information is therefore
  compulsory.

* Some extra information, although not required, might be useful such as
  Length, Precision or Comment. You
  can also hide these columns, by clicking on the Columns drop-down button next to the toolbar, and unchecking
  the relevant entries on the list.
* In the Function area, you can
  select the predefined routine/function if one of them corresponds to your needs. You
  can also add to this list any routine you stored in the Routine area of the Repository. Or you can type in the function you want to use in the
  Function definition panel. For more
  information, see [What are routines](/talend/r/en-US/8.0/studio-user-guide/what-are-routines).
* Click Refresh to have a preview of the
  data generated.
* Type in a number of rows to be generated. The more rows to be generated,
  the longer it'll take to carry out the generation operation.
