<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileoutputxml · versión 8.0 -->
# tFileOutputXML

Last updated: 9/30/2026

Writes an XML file with separated data values according to a defined
schema.

### In this section

* [tFileOutputXML Standard properties](/talend/en-US/components/8.0/xml-connectors/tfileoutputxml-standard-properties)
* [tFileOutputXML properties for Apache Spark Batch](/talend/en-US/components/8.0/xml-connectors/tfileoutputxml-properties-for-apache-spark-batch)
* [tFileOutputXML properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/xml-connectors/tfileoutputxml-properties-for-apache-spark-streaming)

**Related concepts**  

* [Extracting erroneous XML data via a reject flow](tfileinputxml-tfileoutputxml-tlogrow-tfileoutputxml-tlogrow-extracting-erroneous-xml-data-via-reject-flow-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileoutputxml-properties-for-apache-spark-batch -->
# tFileOutputXML properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileOutputXML running in the Spark Batch Job framework.

The Spark Batch
tFileOutputXML component belongs to the File and the XML families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Row tag | Specify the tag that will wrap data and structure per row. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder | Browse to, or enter the path pointing to the data to be used in the file system.  This path must point to a folder rather than a file.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Action | Select an operation for writing data:  Create: Creates a file and write data in it.  Overwrite: Overwrites the file existing in the directory specified in the Folder field.  When you want to sort the rows, row order is not guaranteed with this component. |
| Compress the data | Select the Compress the data check box to compress the output data. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Root tags | Specify one or more root tags to wrap the whole output file structure and data. The default root tag is *root*. |
| Output format | Define the output format.   * Column: The columns retrieved   from the input schema. * As attribute: select check box   for the column(s) you want to use as attribute(s) of the parent   element in the XML output.   Information noteNote: If the same column is selected in both the Output format table as an attribute and in the Use dynamic grouping setting as the criterion for dynamic grouping, only the dynamic group setting will take effect for that column.  Use schema column name: By default, this check box is selected for all columns so that the column labels from the input schema are used as data wrapping tags. If you want to use a different tag than from the input schema for any column, clear this check box for that column and specify a tag label between quotation marks in the Label field. |
| Use dynamic grouping | Select this check box if you want to dynamically group the output columns. Click the plus button to add one ore more grouping criteria in the Group by table.  Column: Select a column you want to use as a wrapping element for the grouped output rows.  Attribute label: Enter an attribute label for the group wrapping element, between quotation marks. |
| Custom encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Advanced separator (for numbers) | Select this check box to modify the separators used for numbers:  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileoutputxml-standard-properties -->
# tFileOutputXML Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileOutputXML running in the Standard Job framework.

The Standard
tFileOutputXML component belongs to the File and the XML families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| File Name | Name or path to the output file or the variable to be used.  Related topic: see [Defining variables from the Component view](/talend/r/en-US/8.0/studio-user-guide/defining-variables-from-component-view).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Incoming record is a document | Select this check box if the data from the preceding component is in XML format.  When this check box is selected, a Column list appears allowing you to select a Document type column of the schema that holds the data, and the Row tag field disappears.  When this check box is selected, in the Advanced settings view, only the check boxes Create directory if not exists, Don't generate empty file, Trim data, tStatCatcher Statistics and the list Encoding are available. |
| Row tag | Specify the tag that will wrap data and structure per row. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the input component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Split output in several files | If the output is big, you can split the output into several files, each containing the specified number of rows.  Rows in each output file: Specify the number of rows in each output file. |
| Create directory if not exists | This check box is selected by default. It creates a directory to hold the output XML files if required. |
| Root tags | Specify one or more root tags to wrap the whole output file structure and data. The default root tag is *root*. |
| Output format | Define the output format.   * Column: The columns retrieved   from the input schema. * As attribute: select check box   for the column(s) you want to use as attribute(s) of the parent   element in the XML output.   Information noteNote: If the same column is selected in both the Output format table as an attribute and in the Use dynamic grouping setting as the criterion for dynamic grouping, only the dynamic group setting will take effect for that column.  Use schema column name: By default, this check box is selected for all columns so that the column labels from the input schema are used as data wrapping tags. If you want to use a different tag than from the input schema for any column, clear this check box for that column and specify a tag label between quotation marks in the Label field. |
| Use dynamic grouping | Select this check box if you want to dynamically group the output columns. Click the plus button to add one ore more grouping criteria in the Group by table.  Column: Select a column you want to use as a wrapping element for the grouped output rows.  Attribute label: Enter an attribute label for the group wrapping element, between quotation marks. |
| Custom the flush buffer size | Select this check box to define the number of rows to buffer before the data is written into the target file and the buffer is emptied.  Row Number: Specify the number of rows to buffer. |
| Advanced separator (for numbers) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Don't generate empty file | Select the check box to avoid the generation of an empty file. |
| Trim data | Select this check box to remove the spaces at the beginning and at the end of the text, and merge multiple consecutive spaces into one within the text. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to write an XML file with data passed on from other components using a Row link. |
