<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited · versión 8.0 -->
# tFileOutputDelimited

Last updated: 9/30/2026

Outputs the input data to a delimited file according to the defined
schema.

### In this section

* [tFileOutputDelimited Standard properties](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties)
* [tFileOutputDelimited properties for Apache Spark Batch](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-properties-for-apache-spark-batch)
* [tFileOutputDelimited properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-properties-for-apache-spark-streaming)

**Related concepts**  

* [Utilizing Output Stream to save filtered data to a local file](tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-utilizing-output-stream-to-save-filtered-data-to-local-file-standard-component-based-on)
* [Writing data in a delimited file](tfileinputdelimited-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-data-in-delimited-file-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-properties-for-apache-spark-batch -->
# tFileOutputDelimited properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileOutputDelimited running in the Spark Batch Job framework.

The Spark Batch
tFileOutputDelimited component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder | Browse to, or enter the path pointing to the data to be used in the file system.  Note that this path must point to a folder rather than a file.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Action | Select an operation for writing data:  Create: Creates a file and write data in it.  Overwrite: Overwrites the file existing in the directory specified in the Folder field.  When you want to sort the rows, row order is not guaranteed with this component. |
| Use OS line separator as row separator when CSV Row Separator is set to CR, LF or CRLF | Select this check box to automatically select the appropriate row separator for the OS on which you run the Job:  * LF, for Linux * CR or CRLF for Windows   If you leave the check box cleared, you can specify the row separator to be used regardless of the OS.  This option is available only when you select the CSV options check box from the Advanced settings view. |
| Row separator | The separator used to identify the end of a row. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Include Header | Select this check box to include the column header to the file. |
| Custom encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Compress the data | Select the Compress the data check box to compress the output data.  Hadoop provides different compression formats that help reduce the space needed for storing files and speed up data transfer. When reading a compressed file, Talend Studio needs to uncompress it before being able to feed it to the input flow. |
| Merge result to single file | Select this check box to merge the final *part* files into a single file and put that file in a specified directory.  Once selecting it, you need to enter the path to, or browse to the folder you want to store the merged file in. This directory is automatically created if it does not exist.  The following check boxes are used to manage the source and the target files:  * Remove source dir: select   this check box to remove the source files after the merge. * Override target file:   select this check box to override the file already existing in the target   location. This option does not override the folder.  If this component is writing merged files with a Databricks cluster, add the following parameter to the Spark configuration console of your cluster: ``` spark.sql.sources.commitProtocolClass org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol ``` This parameter prevents the merge file including the log file automatically generated by the DBIO service of Databricks.  This option is not available for a Sequence file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  This option is not available for a Sequence file. |
| CSV options | Select this check box to include CSV specific parameters such as Escape char and Text enclosure. Information noteImportant: With Spark version 2.0 and onward, special characters must be escaped, that is `"\\"` and `"\""` instead of `"\"` and `"""`. |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties -->
# tFileOutputDelimited Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileOutputDelimited running in the Standard Job framework.

The Standard
tFileOutputDelimited component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use Output Stream | Select this check box process the data flow of interest. Once you have selected it, the Output Stream field displays and you can type in the data flow of interest.  The data flow to be processed must be added to the flow in order for this component to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  For further information about how to use a stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| File Name | Name or path to the output file and/or the variable to be used.  This field becomes unavailable once you have selected the Use Output Stream check box.  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Row Separator | The separator used to identify the end of a row. |
| Field Separator | Enter a character or a string to separate fields for the transferred data.  Information noteNote: With CSV options selected in the Advanced settings view, the field separator can only be a single character. In this case, if you enter multiple characters in this field, only the first character acts as the field separator. |
| Append | Select this check box to add the new rows at the end of the file. |
| Include Header | Select this check box to include the column header to the file. |
| Compress as zip file | Select this check box to compress the output file in zip format. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window.   This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the output component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for numbers) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| CSV options | Select this check box to specify the following CSV parameters:   * Escape char: enter the escape character between double   quotation marks. * Text enclosure: enter the enclosure character (only one   character) between double quotation marks. For example, `"""`   needs to be entered when double quotation marks (") are used as the enclosure   character.   It is recommended to use standard escape character, that is `"\"`. Otherwise, you should set the same character for Escape char and Text enclosure. For example, if the escape character is set to `"\"`, the text enclosure can be set to any other character. On the other hand, if the escape character is set to other character rather than `"\"`, the text enclosure can be set to any other characters. However, the escape character will be changed to the same character as the text enclosure. For instance, if the escape character is set to `"#"` and the text enclosure is set to `"@"`, the escape character will be changed to `"@"`, not `"#"`. |
| Create directory if not exists | This check box is selected by default. It creates the directory that holds the output delimited file, if it does not already exist. |
| Split output in several files | In case of very big output files, select this check box to divide the output delimited file into several files.  Rows in each output file: set the number of lines in each of the output files. |
| Custom the flush buffer size | Select this check box to define the number of lines to write before emptying the buffer.  Row Number: set the number of lines to write. |
| Output in row mode | Select this check box to ensure atomicity of the flush so that each row of data can remain consistent as a set and incomplete rows of data are never written to a file.  This check box is mostly useful when using this component in the multi-thread situation. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Don't generate empty file | Select this check box if you do not want to generate empty files. |
| Throw an error if the file already exist | Select this check box to throw an exception if the output file specified in the File Name field on the Basic settings view already exists.  Clear this check box to overwrite the existing file. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  FILE\_NAME: the name of the file being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to write a delimited file and separate fields using a field separator value.  This component does not support the use of tSetDynamicSchema. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-utilizing-output-stream-to-save-filtered-data-to-local-file-standard-component-based-on -->
# Utilizing Output Stream to save filtered data to a local file

Last updated: 9/30/2026

Based on the preceding scenario, this scenario saves the filtered data to a
local file using output stream.

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tFileInputDelimited](tfileinputdelimited "Reads a delimited file row by row to split them up into fields and then sends the fields as defined in the schema to the next component.")
* [tFileOutputDelimited](tfileoutputdelimited "Outputs the input data to a delimited file according to the defined schema.")

**Related information**  

* [tJava](/talend/en-US/components/8.0/java-custom-code/tjava)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tJava to open its Basic settings view.
2. In the Code area, type in the following
   command:

   ```
   new java.io.File("C:/myFolder").mkdirs(); 
   globalMap.put("out_file",new
   java.io.FileOutputStream("C:/myFolder/customerselection.txt",false));
   ```

   Information noteNote:

   In this scenario, the command we use in the Code area of tJava will
   create a new folder *C:/myFolder* where the output
   file *customerselection.txt* will be saved. You can
   customize the command in accordance with actual practice.
3. Double-click tFileOutputDelimited to open
   its Basic settings view.
4. Select Use Output Stream check box to
   enable the Output Stream field in which you
   can define the output stream using command.

   Fill in the Output Stream field with
   following command:

   ```
   (java.io.OutputStream)globalMap.get("out_file")
   ```

   Information noteNote:

   You can customize the command in the Output
   Stream field by pressing CTRL+SPACE to
   select built-in command from the list or type in the command into
   the field manually in accordance with actual practice. In this
   scenario, the command we use in the Output
   Stream field will call the
   java.io.OutputStream class to output the filtered
   data stream to a local file which is defined in the Code area of tJava in this scenario.
5. Click Sync columns to retrieve the schema
   defined in the preceding component.
6. Leave rest of the components as they were in the previous scenario.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. Drop tJava from the Palette to the design workspace.
2. Connect tJava to tFileInputDelimited using a Trigger > On Subjob OK
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save
   your Job.
2. Press F6 or click
   Run on the Run tab to execute the Job.

   The three specified columns *Id*, *CustomerName* and *CustomerAddress*
   are output in the defined output file.

   For an example of how to use dynamic schemas with
   tFileOutputDelimited, see [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties · versión 8.0 -->
# tFileOutputDelimited Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileOutputDelimited running in the Standard Job framework.

The Standard
tFileOutputDelimited component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use Output Stream | Select this check box process the data flow of interest. Once you have selected it, the Output Stream field displays and you can type in the data flow of interest.  The data flow to be processed must be added to the flow in order for this component to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  For further information about how to use a stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| File Name | Name or path to the output file and/or the variable to be used.  This field becomes unavailable once you have selected the Use Output Stream check box.  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Row Separator | The separator used to identify the end of a row. |
| Field Separator | Enter a character or a string to separate fields for the transferred data.  Information noteNote: With CSV options selected in the Advanced settings view, the field separator can only be a single character. In this case, if you enter multiple characters in this field, only the first character acts as the field separator. |
| Append | Select this check box to add the new rows at the end of the file. |
| Include Header | Select this check box to include the column header to the file. |
| Compress as zip file | Select this check box to compress the output file in zip format. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window.   This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the output component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for numbers) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| CSV options | Select this check box to specify the following CSV parameters:   * Escape char: enter the escape character between double   quotation marks. * Text enclosure: enter the enclosure character (only one   character) between double quotation marks. For example, `"""`   needs to be entered when double quotation marks (") are used as the enclosure   character.   It is recommended to use standard escape character, that is `"\"`. Otherwise, you should set the same character for Escape char and Text enclosure. For example, if the escape character is set to `"\"`, the text enclosure can be set to any other character. On the other hand, if the escape character is set to other character rather than `"\"`, the text enclosure can be set to any other characters. However, the escape character will be changed to the same character as the text enclosure. For instance, if the escape character is set to `"#"` and the text enclosure is set to `"@"`, the escape character will be changed to `"@"`, not `"#"`. |
| Create directory if not exists | This check box is selected by default. It creates the directory that holds the output delimited file, if it does not already exist. |
| Split output in several files | In case of very big output files, select this check box to divide the output delimited file into several files.  Rows in each output file: set the number of lines in each of the output files. |
| Custom the flush buffer size | Select this check box to define the number of lines to write before emptying the buffer.  Row Number: set the number of lines to write. |
| Output in row mode | Select this check box to ensure atomicity of the flush so that each row of data can remain consistent as a set and incomplete rows of data are never written to a file.  This check box is mostly useful when using this component in the multi-thread situation. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Don't generate empty file | Select this check box if you do not want to generate empty files. |
| Throw an error if the file already exist | Select this check box to throw an exception if the output file specified in the File Name field on the Basic settings view already exists.  Clear this check box to overwrite the existing file. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  FILE\_NAME: the name of the file being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to write a delimited file and separate fields using a field separator value.  This component does not support the use of tSetDynamicSchema. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited -->
# tFileOutputDelimited

Last updated: 9/30/2026

Outputs the input data to a delimited file according to the defined
schema.

### In this section

* [tFileOutputDelimited Standard properties](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties)
* [tFileOutputDelimited properties for Apache Spark Batch](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-properties-for-apache-spark-batch)
* [tFileOutputDelimited properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-properties-for-apache-spark-streaming)

**Related concepts**  

* [Utilizing Output Stream to save filtered data to a local file](tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-utilizing-output-stream-to-save-filtered-data-to-local-file-standard-component-based-on)
* [Writing data in a delimited file](tfileinputdelimited-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-data-in-delimited-file-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-properties-for-apache-spark-batch -->
# tFileOutputDelimited properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileOutputDelimited running in the Spark Batch Job framework.

The Spark Batch
tFileOutputDelimited component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder | Browse to, or enter the path pointing to the data to be used in the file system.  Note that this path must point to a folder rather than a file.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Action | Select an operation for writing data:  Create: Creates a file and write data in it.  Overwrite: Overwrites the file existing in the directory specified in the Folder field.  When you want to sort the rows, row order is not guaranteed with this component. |
| Use OS line separator as row separator when CSV Row Separator is set to CR, LF or CRLF | Select this check box to automatically select the appropriate row separator for the OS on which you run the Job:  * LF, for Linux * CR or CRLF for Windows   If you leave the check box cleared, you can specify the row separator to be used regardless of the OS.  This option is available only when you select the CSV options check box from the Advanced settings view. |
| Row separator | The separator used to identify the end of a row. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Include Header | Select this check box to include the column header to the file. |
| Custom encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Compress the data | Select the Compress the data check box to compress the output data.  Hadoop provides different compression formats that help reduce the space needed for storing files and speed up data transfer. When reading a compressed file, Talend Studio needs to uncompress it before being able to feed it to the input flow. |
| Merge result to single file | Select this check box to merge the final *part* files into a single file and put that file in a specified directory.  Once selecting it, you need to enter the path to, or browse to the folder you want to store the merged file in. This directory is automatically created if it does not exist.  The following check boxes are used to manage the source and the target files:  * Remove source dir: select   this check box to remove the source files after the merge. * Override target file:   select this check box to override the file already existing in the target   location. This option does not override the folder.  If this component is writing merged files with a Databricks cluster, add the following parameter to the Spark configuration console of your cluster: ``` spark.sql.sources.commitProtocolClass org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol ``` This parameter prevents the merge file including the log file automatically generated by the DBIO service of Databricks.  This option is not available for a Sequence file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  This option is not available for a Sequence file. |
| CSV options | Select this check box to include CSV specific parameters such as Escape char and Text enclosure. Information noteImportant: With Spark version 2.0 and onward, special characters must be escaped, that is `"\\"` and `"\""` instead of `"\"` and `"""`. |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-utilizing-output-stream-to-save-filtered-data-to-local-file-standard-component-based-on -->
# Utilizing Output Stream to save filtered data to a local file

Last updated: 9/30/2026

Based on the preceding scenario, this scenario saves the filtered data to a
local file using output stream.

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tFileInputDelimited](tfileinputdelimited "Reads a delimited file row by row to split them up into fields and then sends the fields as defined in the schema to the next component.")
* [tFileOutputDelimited](tfileoutputdelimited "Outputs the input data to a delimited file according to the defined schema.")

**Related information**  

* [tJava](/talend/en-US/components/8.0/java-custom-code/tjava)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tJava to open its Basic settings view.
2. In the Code area, type in the following
   command:

   ```
   new java.io.File("C:/myFolder").mkdirs(); 
   globalMap.put("out_file",new
   java.io.FileOutputStream("C:/myFolder/customerselection.txt",false));
   ```

   Information noteNote:

   In this scenario, the command we use in the Code area of tJava will
   create a new folder *C:/myFolder* where the output
   file *customerselection.txt* will be saved. You can
   customize the command in accordance with actual practice.
3. Double-click tFileOutputDelimited to open
   its Basic settings view.
4. Select Use Output Stream check box to
   enable the Output Stream field in which you
   can define the output stream using command.

   Fill in the Output Stream field with
   following command:

   ```
   (java.io.OutputStream)globalMap.get("out_file")
   ```

   Information noteNote:

   You can customize the command in the Output
   Stream field by pressing CTRL+SPACE to
   select built-in command from the list or type in the command into
   the field manually in accordance with actual practice. In this
   scenario, the command we use in the Output
   Stream field will call the
   java.io.OutputStream class to output the filtered
   data stream to a local file which is defined in the Code area of tJava in this scenario.
5. Click Sync columns to retrieve the schema
   defined in the preceding component.
6. Leave rest of the components as they were in the previous scenario.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. Drop tJava from the Palette to the design workspace.
2. Connect tJava to tFileInputDelimited using a Trigger > On Subjob OK
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-tfileinputdelimited-tjava-tfileinputdelimited-tjava-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save
   your Job.
2. Press F6 or click
   Run on the Run tab to execute the Job.

   The three specified columns *Id*, *CustomerName* and *CustomerAddress*
   are output in the defined output file.

   For an example of how to use dynamic schemas with
   tFileOutputDelimited, see [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
