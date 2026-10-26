<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileoutputpositional · versión 8.0 -->
# tFileOutputPositional

Last updated: 9/30/2026

Writes a file row by row according to the length and the format of the fields or
columns in a row.

### In this section

* [tFileOutputPositional Standard properties](/talend/en-US/components/8.0/positional/tfileoutputpositional-standard-properties)
* [tFileOutputPositional properties for Apache Spark Batch](/talend/en-US/components/8.0/positional/tfileoutputpositional-properties-for-apache-spark-batch)
* [tFileOutputPositional properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/positional/tfileoutputpositional-properties-for-apache-spark-streaming)

**Related concepts**  

* [Handling a positional file based on a dynamic schema](tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-handling-positional-file-based-on-dynamic-schema-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileoutputpositional-properties-for-apache-spark-batch -->
# tFileOutputPositional properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileOutputPositional running in the Spark Batch Job framework.

The Spark Batch
tFileOutputPositional component belongs to the File family.

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
| Folder | Browse to, or enter the path pointing to the data to be used in the file system.  This path must point to a folder rather than a file.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Action | Select an operation for writing data:  Create: Creates a file and write data in it.  Overwrite: Overwrites the file existing in the directory specified in the Folder field. |
| Compress the data | Select the Compress the data check box to compress the output data. |
| Row separator | The separator used to identify the end of a row. |
| Include header | Select this check box to include the column header to the file. |
| Custom encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. |
| Merge result to single file | Select this check box to merge the final *part* files into a single file and put that file in a specified directory.  Once selecting it, you need to enter the path to, or browse to the folder you want to store the merged file in. This directory is automatically created if it does not exist.  The following check boxes are used to manage the source and the target files:  * Remove source dir: select   this check box to remove the source files after the merge. * Override target file:   select this check box to override the file already existing in the target   location. This option does not override the folder.  If this component is writing merged files with a Databricks cluster, add the following parameter to the Spark configuration console of your cluster: ``` spark.sql.sources.commitProtocolClass org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol ``` This parameter prevents the merge file including the log file automatically generated by the DBIO service of Databricks.  This option is not available for a Sequence file. |
| Formats | Customize the positional file data format and fill in the columns in the Formats table.  Column: Select the column you want to customize.  Size: Enter the column size.  Padding char: Type in between quotes the padding characters used. A space by default.  Alignment: Select the appropriate alignment parameter.  Keep: If the data in the column or in the field are too long, select the part you want to keep. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for numbers) | Select this check box to modify the separators used for numbers:  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/positional/tfileoutputpositional-standard-properties -->
# tFileOutputPositional Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileOutputPositional running in the Standard Job framework.

The Standard
tFileOutputPositional component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use existing dynamic | Select this check box to reuse an existing dynamic schema to handle data from unknown columns.  When this check box is selected, a Component list appears allowing you to select the component used to set the dynamic schema. |
| Use Output Stream | Select this check box process the data flow of interest. Once you have selected it, the Output Stream field displays and you can type in the data flow of interest.  The data flow to be processed must be added to the flow in order for this component to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  For further information about how to use a stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| File Name | Name or path to the file to be processed and or the variable to be used.  This field becomes unavailable once you have selected the Use Output Stream check box.  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Schema  and  Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Row separator | The separator used to identify the end of a row. |
| Append | Select this check box to add the new rows at the end of the file. |
| Include header | Select this check box to include the column header to the file. |
| Compress as zip file | Select this check box to compress the output file in zip format. |
| Formats | Customize the positional file data format and fill in the columns in the Formats table.  Column: Select the column you want to customize.  Size: Enter the column size.  Padding char: Type in between quotes the padding characters used. A space by default.  Alignment: Select the appropriate alignment parameter.  Keep: If the data in the column or in the field are too long, select the part you want to keep. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for numbers) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| Use byte length as the cardinality | Select this check box to add support of double-byte character to this component. JDK 1.6 is required for this feature. |
| Create directory if not exists | This check box is selected by default. It creates a directory to hold the output table if it does not exist. |
| Custom the flush buffer size | Select this check box to define the number of lines to write before emptying the buffer.  Row Number: set the number of lines to write. |
| Output in row mode | Writes in row mode. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Don't generate empty file | Select this check box if you do not want to generate empty files. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to read a file and separate the fields using the specified separator. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your HDFS connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access files in different HDFS systems or different distributions, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of *Talend Studio*.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
