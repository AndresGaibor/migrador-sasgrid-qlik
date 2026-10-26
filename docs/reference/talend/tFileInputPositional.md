<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional · versión 8.0 -->
# tFileInputPositional

Last updated: 9/30/2026

Reads a positional file row by row to split them up into fields based on a given
pattern and then sends the fields as defined in the schema to the next
component.

### In this section

* [tFileInputPositional Standard properties](/talend/en-US/components/8.0/positional/tfileinputpositional-standard-properties)
* [tFileInputPositional properties for Apache Spark Batch](/talend/en-US/components/8.0/positional/tfileinputpositional-properties-for-apache-spark-batch)
* [tFileInputPositional properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/positional/tfileinputpositional-properties-for-apache-spark-streaming)

**Related concepts**  

* [Handling a positional file based on a dynamic schema](tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-handling-positional-file-based-on-dynamic-schema-standard-component-enterprise-this)
* [Reading a Positional file and saving filtered results to XML](tfileinputpositional-tfileoutputxml-reading-positional-file-and-saving-filtered-results-to-xml-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional-properties-for-apache-spark-batch -->
# tFileInputPositional properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileInputPositional running in the Spark Batch Job framework.

The Spark Batch
tFileInputPositional component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit schema to make changes to   the schema. If you make changes, the schema automatically becomes built-in. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will read all of the files stored in that folder, for example, /user/talend/in; if sub-folders exist, the sub-folders are automatically ignored unless you define the property spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive to be true in the Advanced properties table in the Spark configuration tab.  * Depending on the filesystem to be used, properly configure the corresponding   configuration component placed in your Job, for example, a   tHDFSConfiguration component for HDFS, a   tS3Configuration component for S3 and a   tAzureFSConfiguration for Azure Storage and Azure Data Lake   Storage.  If you want to specify more than one files or directories in this field, separate each path using a comma (,).  If the file to be read is a compressed one, enter the file name with its extension; then tFileInputPositional automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |
| Row separator | The separator used to identify the end of a row. |
| Customize | Select this check box to customize the data format of the positional file and define the table columns:  Column: Select the column you want to customize.  Size: Enter the column size.  Padding char: Enter, between double quotation marks, the padding charater you need to remove from the field. A space by default.  Alignment: Select the appropriate alignment parameter. |
| Pattern | Enter between double quotes the length values separated by commas, interpreted as a string. Make sure the values entered in this field are consistent with the schema defined. |
| Header | Enter the number of rows to be skipped in the beginning of file.  For example, enter *0* to ignore no rows for the data without header and set *1* for the data with header at the first row. |
| Skip empty rows | Select this checkbox to skip the empty rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set minimum partitions | Select this check box to control the number of partitions to be created from the input data over the default partitioning behavior of Spark.  In the displayed field, enter, without quotation marks, the minimum number of partitions you want to obtain.  When you want to control the partition number, you can generally set at least as many partitions as the number of executors for parallelism, while bearing in mind the available memory and the data transfer pressure on your network. |
| Custom Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Trim columns | Select this check box to remove the leading and trailing whitespaces from all columns. When this check box is cleared, the Check column to trim table is displayed, which lets you select particular columns to trim. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional-standard-properties -->
# tFileInputPositional Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileInputPositional
running in the Standard Job framework.

The Standard
tFileInputPositional component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use existing dynamic | Select this check box to reuse an existing dynamic schema to handle data from unknown columns. When this check box is selected, a Component list appears allowing you to select the component used to set the dynamic schema. |
| File name/Stream | File name: Name and path of the file to be processed. Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors.  Stream: The data flow to be processed. The data must be added to the flow in order for tFileInputPositional to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component, for example, the *INPUT\_STREAM* variable of tFileFetch; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  Related scenario to the input stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| Row separator | The separator used to identify the end of a row. |
| Customize | Select this check box to customize the data format of the positional file and define the table columns:  Column: Select the column you want to customize.  Size: Enter the column size.  Padding char: Enter, between double quotation marks, the padding charater you need to remove from the field. A space by default.  Alignment: Select the appropriate alignment parameter. |
| Pattern | Length values separated by commas, interpreted as a string between quotes. Make sure the values entered in this field are consistent with the schema defined. |
| Pattern Units | The unit of the length values specified in the Pattern field.   * Bytes: With this option selected, the length   values in the Pattern field should be the count of   bytes that represent symbols in original encoding of the input file. * Symbols: With this option selected, the length   values in the Pattern field should be the count of   regular symbols, not including surrogate pairs. * Symbols (including rare): With this option   selected, the length values in the Pattern field   should be the count of symbols, including rare symbols such as surrogate   pairs, and each surrogate pair counts as a single symbol. Considering the   performance factor, it is not recommended to use this option when your   input data consists of only regular symbols. |
| Skip empty rows | Select this checkbox to skip the empty rows. |
| Uncompress as zip file | Select this check box to uncompress the input file. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |
| Header | Enter the number of rows to be skipped in the beginning of file. |
| Footer | Number of rows to be skipped at the end of the file. |
| Limit | Maximum number of rows to be processed. If Limit = 0, no row is read or processed. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables.  This component must work with tSetDynamicSchema to leverage the dynamic schema feature. * Built-in: The schema will be created and   stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists   and is stored in the Repository, hence can be reused in various projects and   Job flowcharts. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Needed to process rows longer than 100 000 characters | Select this check box if the rows to be processed in the input file are longer than 100 000 characters. |
| Advanced separator (for numbers) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| Trim all column | Select this check box to remove leading and trailing whitespaces from defined columns. |
| Validate date | Select this check box to check the date format strictly against the input schema. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to read a file and separate fields using a position separator value. You can also create a rejection flow using a Row > Reject link to filter the data which does not correspond to the type defined. For an example of how to use these two links, see [Procedure](/talend/en-US/components/8.0/processing/textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-procedure-standard-component-drop). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-reading-positional-file-and-saving-filtered-results-to-xml-standard-component-the -->
# Reading a Positional file and saving filtered results to XML

Last updated: 9/30/2026

The following scenario describes a two-component Job, which aims at reading data from
an input file that contains contract numbers, customer references, and insurance numbers
as shown below, and outputting the selected data (according to the data position) into
an XML
file.

```
Contract       CustomerRef    InsuranceNr
00001          8200           50330      
00001          8201           50331      
00002          8202           50332      
00002          8203           50333
```

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-dropping-and-linking-components-standard-component-drop)
* [Configuring data input](/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-configuring-data-input-standard-component)
* [Configuring data output](/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-configuring-data-output-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tFileInputPositional](tfileinputpositional "Reads a positional file row by row to split them up into fields based on a given pattern and then sends the fields as defined in the schema to the next component.")

**Related information**  

* [tFileOutputXML](/talend/en-US/components/8.0/xml-connectors/tfileoutputxml)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-configuring-data-input-standard-component -->
# Configuring data input

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputPositional
   component to show its Basic settings view
   and define its properties.
2. Define the Job Property type if needed. For this scenario, we use the
   built-in Property type. 

   As opposed to the Repository, this means that the Property type is set for
   this station only.
3. Fill in a path to the input file in the File
   Name field. This field is mandatory.
4. Define the Row separator identifying the
   end of a row if needed, by default, a carriage return.
5. If required, select the Use byte length as the
   cardinality check box to enable the support of double-byte
   character.
6. Define the Pattern to delimit fields in a
   row. The pattern is a series of length values corresponding to the values of
   your input files. The values should be entered between quotes, and separated
   by a comma. Make sure the values you enter match the schema defined.
7. Fill in the Header, Footer and Limit fields
   according to your input file structure and your need. In this scenario, we
   only need to skip the first row when reading the input file. To do this,
   fill the Header field with *1* and leave the other fields as they are.
8. Next to Schema, select Repository  if the input schema is stored in the
   Repository. In this use case, we use a Built-In input schema to define the data to pass on to the
   tFileOutputXML component.
9. You can load and/or edit the schema via the Edit
   Schema function. For this schema, define three columns,
   respectively *Contract*, *CustomerRef*
   and *InsuranceNr* matching the structure of the input
   file. Then, click OK to close the Schema dialog box and propagate the
   changes.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-configuring-data-output-standard-component -->
# Configuring data output

Last updated: 9/30/2026

## Procedure

1. Double-click tFileOutputXML to show its
   Basic settings view.
2. Enter the XML output file path.
3. Define the row tag that will wrap each row of data, in this use case
   *ContractRef*.
4. Click the [...] button next to Edit
   schema to view the data structure, and click Sync columns to retrieve the data structure from
   the input component if needed.
5. Switch to the Advanced settings tab view
   to define other settings for the XML output.
6. Click the plus button to add a line in the Root
   tags table, and enter a root tag (or more) to wrap the XML
   output structure, in this case *ContractsList*.
7. Define parameters in the Output format
   table if needed. For example, select the As
   attribute check box for a column if you want to use its name
   and value as an attribute for the parent XML element, clear the Use schema column name check box for a column to
   reuse the column label from the input schema as the tag label. In this use
   case, we keep all the default output format settings as they are.
8. To group output rows according to the contract number, select the
   Use dynamic grouping check box, add a
   line in the Group by table, select
   Contract from the Column list field, and enter an attribute for it in the
   Attribute label field.
9. Leave all the other parameters as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking components

Last updated: 9/30/2026

## About this task

## Procedure

1. Drop a tFileInputPositional component
   from the Palette to the design workspace.
2. Drop a tFileOutputXML component as well.
   This file is meant to receive the references in a structured way.
3. Right-click the tFileInputPositional
   component and select Row
    *>*
   Main. Then drag it onto the
   tFileOutputXML component and release
   when the plug symbol shows up.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileinputpositional-tfileoutputxml-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job to ensure
   that all the configured parameters take effect.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The file is read row by row based on the length values defined in the
   Pattern field and output as an XML file
   as defined in the output settings. You can open it using any standard XML
   editor.
