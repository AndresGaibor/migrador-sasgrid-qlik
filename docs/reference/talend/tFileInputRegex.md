<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/regex/tfileinputregex · versión 8.0 -->
# tFileInputRegex

Last updated: 9/30/2026

Reads a file row by row to split them up into fields using regular expressions and
sends the fields as defined in the schema to the next component.

Powerful feature which can replace number of other
components of the File family. Requires some advanced knowledge on regular expression
syntax.

### In this section

* [tFileInputRegex Standard properties](/talend/en-US/components/8.0/regex/tfileinputregex-standard-properties)
* [tFileInputRegex properties for Apache Spark Batch](/talend/en-US/components/8.0/regex/tfileinputregex-properties-for-apache-spark-batch)
* [tFileInputRegex properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/regex/tfileinputregex-properties-for-apache-spark-streaming)

**Related concepts**  

* [Reading data using a Regex and outputting the result to Positional file](tfileinputregex-tfileoutputpositional-reading-data-using-regex-and-outputting-result-to-positional-file-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/regex/tfileinputregex-properties-for-apache-spark-batch -->
# tFileInputRegex properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileInputRegex running in the Spark Batch Job framework.

The Spark Batch
tFileInputRegex component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will read all of the files stored in that folder, for example, /user/talend/in; if sub-folders exist, the sub-folders are automatically ignored unless you define the property spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive to be true in the Advanced properties table in the Spark configuration tab.  * Depending on the filesystem to be used, properly configure the corresponding   configuration component placed in your Job, for example, a   tHDFSConfiguration component for HDFS, a   tS3Configuration component for S3 and a   tAzureFSConfiguration for Azure Storage and Azure Data Lake   Storage.  If you want to specify more than one files or directories in this field, separate each path using a comma (,).  If the file to be read is a compressed one, enter the file name with its extension; then ttFileInputRegex automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Row separator | The separator used to identify the end of a row. |
| Regex | This field can contain multiple lines. Type in your regular expressions including the subpattern matching the fields to be extracted.  Note: Antislashes need to be doubled in regexp  Information noteWarning: *Regex syntax requires double quotes.* |
| Header | Enter the number of rows to be skipped in the beginning of file. |
| Schema and Edit Schema | * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Skip empty rows | Select this checkbox to skip the empty rows. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set minimum partitions | Select this check box to control the number of partitions to be created from the input data over the default partitioning behavior of Spark.  In the displayed field, enter, without quotation marks, the minimum number of partitions you want to obtain.  When you want to control the partition number, you can generally set at least as many partitions as the number of executors for parallelism, while bearing in mind the available memory and the data transfer pressure on your network. |
| Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/regex/tfileinputregex-standard-properties -->
# tFileInputRegex Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileInputRegex running
in the Standard Job framework.

The Standard
tFileInputRegex component belongs to the File
family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| File name/Stream | File name: Name of the file and/or the variable to be processed.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors.  Stream: Data flow to be processed. The data must be added to the flow so that it can be collected by the tFileInputRegex via the *INPUT\_STREAM* variable in the auto-completion list (Ctrl+Space).  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |
| Row separator | The separator used to identify the end of a row. |
| Regex | Type in your Java regular expression including the subpattern matching the fields to be extracted. This field can contain multiple lines. Note: Antislashes need to be doubled in regexp  Information noteWarning: * The regular expression needs to be in double quotes. * To extract all the desired strings, make sure the regular expression   contains the corresponding subpatterns that match the strings. Also,   each subpattern in the regular expression needs to be in a pair of   brackets. |
| Header | Enter the number of rows to be skipped in the beginning of file. |
| Footer | Number of rows to be skipped at the end of the file. |
| Limit | Maximum number of rows to be processed. If Limit = 0, no row is read or processed. |
| Ignore error message for the unmatched record | Select this checkbox to avoid outputing error messages for records that do not match the specified regex. This checkbox is cleared by default. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Skip empty rows | Select this checkbox to skip the empty rows. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link.  In this component configuration, this option applies to Java runtime exceptions. It does not stop the Job when a row does not match the configured regular expression. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>.  In the Map/Reduce version of tFileInputRegex, you need to select the Custom encoding check box to display this list. |
| Fail on unmatched row | Select this checkbox to stop the Job when at least one input row does not match the configured regular expression.  This option is available only when Die on error is selected.  This checkbox is cleared by default. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to read a file and separate fields contained in this file according to the defined Regex. You can also create a rejection flow using a Row > Reject link to filter the data which doesn't correspond to the type defined. For an example of how to use these two links, see [Procedure](/talend/en-US/components/8.0/processing/textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-procedure-standard-component-drop). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/regex/tfileinputregex-tfileoutputpositional-reading-data-using-regex-and-outputting-result-to-positional-file-standard-component-the -->
# Reading data using a Regex and outputting the result to Positional file

Last updated: 9/30/2026

The following scenario creates a two-component Job, reading data from an Input
file using regular expression and outputting delimited data into a positional file.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/regex/tfileinputregex-tfileoutputpositional-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/regex/tfileinputregex-tfileoutputpositional-configuring-components-standard-component-select)
* [Saving and executing the Job](/talend/en-US/components/8.0/regex/tfileinputregex-tfileoutputpositional-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tFileInputRegex](tfileinputregex "Reads a file row by row to split them up into fields using regular expressions and sends the fields as defined in the schema to the next component.")

**Related information**  

* [tFileOutputPositional](/talend/en-US/components/8.0/positional/tfileoutputpositional)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/regex/tfileinputregex-tfileoutputpositional-configuring-components-standard-component-select -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Select the tFileInputRegex again so the
   Component view shows up, and define the
   properties:
2. The Job is built-in for this scenario. Hence, the Properties are set for this
   station only.
3. Fill in a path to the file in File Name
   field. This field is mandatory.
4. Define the Row separator identifying the end
   of a row.
5. Then define the Regular expression in order
   to delimit fields of a row, which are to be passed on to the next component. You
   can type in a regular expression using Java code, and on mutiple lines if
   needed. 

   Information noteWarning:

   *Regex syntax requires double quotes.*
6. In this expression, make sure you include all subpatterns matching the fields
   to be extracted.
7. In this scenario, ignore the header, footer and limit fields.
8. Select a local (Built-in) Schema to define the data to pass on to the tFileOutputPositional component.
9. You can load or create the schema through the Edit
   Schema function.
10. Then define the second component properties:
11. Enter the Positional file output path.
12. Enter the Encoding standard, the output file
    is encoded in. Note that, for the time being, the encoding consistency
    verification is not supported.
13. Select the Schema type. Click on Sync columns to automatically synchronize the schema
    with the Input file schema.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/regex/tfileinputregex-tfileoutputpositional-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop a tFileInputRegex component from the
   Palette to the design workspace.
2. Drop a tFileOutputPositional component the
   same way.
3. Right-click on the tFileInputRegex component
   and select Row
    *>*
   Main. Drag this main row link
   onto the tFileOutputPositional component and
   release when the plug symbol displays.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/regex/tfileinputregex-tfileoutputpositional-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Now go to the Run tab, and click on Run to execute the Job.

   The file is read row by row and split up into fields based on the Regular Expression definition. You can open it using
   any standard file editor.
