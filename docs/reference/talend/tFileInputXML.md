<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml · versión 8.0 -->
# tFileInputXML

Last updated: 9/30/2026

Reads an XML structured file row by row to split them up into fields and sends the
fields as defined in the schema to the next component.

### In this section

* [tFileInputXML Standard properties](/talend/en-US/components/8.0/xml-connectors/tfileinputxml-standard-properties)
* [tFileInputXML properties for Apache Spark Batch](/talend/en-US/components/8.0/xml-connectors/tfileinputxml-properties-for-apache-spark-batch)
* [tFileInputXML properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/xml-connectors/tfileinputxml-properties-for-apache-spark-streaming)

**Related concepts**  

* [Extracting erroneous XML data via a reject flow](tfileinputxml-tfileoutputxml-tlogrow-tfileoutputxml-tlogrow-extracting-erroneous-xml-data-via-reject-flow-standard-component)
* [Reading and extracting data from an XML structure](tfileinputxml-tlogrow-reading-and-extracting-data-from-xml-structure-standard-component "This scenario extracts specific information from an XML file (areas.xml in this example) and displays the information through a tLogRow component.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml-properties-for-apache-spark-batch -->
# tFileInputXML properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileInputXML running in the Spark Batch Job framework.

The Spark Batch
tFileInputXML component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will read all of the files stored in that folder, for example, /user/talend/in; if sub-folders exist, the sub-folders are automatically ignored unless you define the property spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive to be true in the Advanced properties table in the Spark configuration tab.  * Depending on the filesystem to be used, properly configure the corresponding   configuration component placed in your Job, for example, a   tHDFSConfiguration component for HDFS, a   tS3Configuration component for S3 and a   tAzureFSConfiguration for Azure Storage and Azure Data Lake   Storage.  If you want to specify more than one files or directories in this field, separate each path using a comma (,).  If the file to be read is a compressed one, enter the file name with its extension; then ttFileInputXML automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Element to extract | Enter the element from which you need to read the contents and the child elements of the input XML data.  The element defined in this field is used at the root node of any XPath specified within this component. This element helps define the atomic units of the XML data to be used so that however big the original document is or wherever the input is split, the rows within this element can be correctly distributed to the mapper tasks.  Note that any content outside this element is ignored and the child elements of this element cannot contain this element itself. |
| Loop XPath query | Node of the tree, which the loop is based on.  Note its root is the element you have defined in the Element to extract field. |
| Mapping | Column:  Columns to map. They reflect the schema as defined in the Schema type field.  XPath Query: Enter the fields to be extracted from the structured input.  Get nodes: Select this check box to recuperate the XML content of all current nodes specified in the Xpath query list, or select the check box next to specific XML nodes to recuperate only the content of the selected nodes. These nodes are important when the output flow from this component needs to use the XML structure, for example, the Document data type.  For further information about the Document type, see [Setting up Document type](/talend/r/en-US/8.0/studio-user-guide/setting-up-document-type). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set minimum partitions | Select this check box to control the number of partitions to be created from the input data over the default partitioning behavior of Spark.  In the displayed field, enter, without quotation marks, the minimum number of partitions you want to obtain.  When you want to control the partition number, you can generally set at least as many partitions as the number of executors for parallelism, while bearing in mind the available memory and the data transfer pressure on your network. |
| Custom encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml-standard-properties -->
# tFileInputXML Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileInputXML running in the Standard Job framework.

The Standard
tFileInputXML component belongs to the File and the XML families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| File name/Stream | File name: Name and path of the file to be processed.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors.  Stream: The data flow to be processed. The data must be added to the flow in order for tFileInputXML to fetch these data via the corresponding representative variable.  This variable could be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component, for example, the *INPUT\_STREAM* variable of tFileFetch; otherwise, you could define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.    Related scenario to the input stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| Loop XPath query | Node of the tree, which the loop is based on. |
| Mapping | Column:  Columns to map. They reflect the schema as defined in the Schema type field.  XPath Query: Enter the fields to be extracted from the structured input.  Get nodes: Select this check box to recuperate the XML content of all current nodes specified in the Xpath query list, or select the check box next to specific XML nodes to recuperate only the content of the selected nodes. These nodes are important when the output flow from this component needs to use the XML structure, for example, the Document data type.  For further information about the Document type, see [Setting up Document type](/talend/r/en-US/8.0/studio-user-guide/setting-up-document-type).  Information noteNote: The Get Nodes option functions in the DOM4j and SAX modes, although in SAX mode namespaces are not supported. For further information concerning the DOM4j and SAX modes, please see the properties noted in the Generation mode list of the Advanced Settings tab. |
| Limit | Maximum number of rows to be processed. If Limit = 0, no row is read nor processed. If -1, all rows are read or processed. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Ignore DTD file | Select this check box to ignore the DTD file indicated in the XML file being processed. |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  Thousands separator: define the separators to use for thousands.  Decimal separator: define the separators to use for decimals. |
| Ignore the namespaces | Select this check box to ignore name spaces.  Generate a temporary file: click the [...] button to browse to the XML temporary file and set its path in the field. |
| Use Separator for mode Xerces | Select this check box if you want to separate concatenated children node values.  Information noteNote: This field can only be used if the selected Generation mode is Xerces.  The following field displays:  Field separator: Define the delimiter to be used to separate the children node values. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Generation mode | From the drop-down list select the generation mode for the XML file, according to the memory available and the desired speed:   * Slow and memory-consuming   (Dom4j)  Information noteNote: This option allows you to use dom4j to process the XML   files of high complexity. * Memory-consuming   (Xerces). * Fast with low memory consumption   (SAX) |
| Validate date | Select this check box to check the date format strictly against the input schema. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tFileInputXML is for use as an entry componant. It allows you to create a flow of XML data using a Row > Main link. You can also create a rejection flow using a Row > Reject link to filter the data which doesn't correspond to the type defined. For an example of how to use these two links, see [Procedure](/talend/en-US/components/8.0/processing/textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-procedure-standard-component-drop). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tfileoutputxml-tlogrow-tfileoutputxml-tlogrow-extracting-erroneous-xml-data-via-reject-flow-standard-component -->
# Extracting erroneous XML data via a reject flow

Last updated: 9/30/2026

This Java scenario describes a three-component Job that reads an XML file and:

1. first, returns correct XML data in an output XML file,
2. and second, displays on the console erroneous XML data which type does not
   correspond to the defined one in the schema.

### In this section

* [Procedure](/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tfileoutputxml-tlogrow-tfileoutputxml-tlogrow-procedure-standard-component-drop)

**Related concepts**  

* [tFileInputXML](tfileinputxml "Reads an XML structured file row by row to split them up into fields and sends the fields as defined in the schema to the next component.")
* [tFileOutputXML](tfileoutputxml "Writes an XML file with separated data values according to a defined schema.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tlogrow-reading-and-extracting-data-from-xml-structure-standard-component -->
# Reading and extracting data from an XML structure

Last updated: 9/30/2026

This scenario extracts specific information from an XML file
(areas.xml in this example) and displays the information through a
tLogRow component.

The following lists the content of the areas.xml file:

```
<areas>
	<area city="Paris">
		<street district="2eme arroundissement">Rue de la Paix</street>
	</area>
	<area city="Paris">
		<street district="8eme arroundissement">Champs Elysees</street>
	</area>
	<area city="New York City">
		<street district="Manhattan">Madison avenue</street>
	</area>
	<area city="New York City">
		<street district="Brooklyn">Washington heights</street>
	</area>
</areas>
```

### In this section

* [Creating the Job](/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tlogrow-reading-and-extracting-data-from-an-xml-structure-creating-job)
* [Setting up and executing the Job](/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tlogrow-reading-and-extracting-data-from-an-xml-structure-configuring-job)

**Related concepts**  

* [tFileInputXML](tfileinputxml "Reads an XML structured file row by row to split them up into fields and sends the fields as defined in the schema to the next component.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tfileoutputxml-tlogrow-tfileoutputxml-tlogrow-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette to the design workspace: tFileInputXML, tFileOutputXML
   and tLogRow.

   Right-click tFileInputXML and select
   Row > Main in the contextual menu and then click tFileOutputXML to connect the components together.

   Right-click tFileInputXML and select
   Row > Reject in the contextual menu and then click tLogRow to connect the components together using a
   reject link.
2. Double-click tFileInputXML to display the
   Basic settings view and define the
   component properties.
3. In the Property Type list, select Repository and click the [...] button next to the
   field to display the Repository Content
   dialog box where you can select the metadata relative to the input
   file if you have already stored it in the File xml node under the Metadata folder of the Repository tree view. The fields that follow are automatically
   filled with the fetched data. If not, select Built-in and fill in the fields that follow manually.

   For more information about storing schema metadata in the
   Repository tree view, see [Managing metadata in Talend Studio](/talend/r/en-US/8.0/studio-user-guide/managing-metadata-in-studio).
4. In the Schema Type list, select Repository and click the [...] button to open the
   dialog box where you can select the schema that describe the structure of the
   input file if you have already stored it in the Repository tree view. If not, select Built-in and click the [...] button next to Edit schema to open a dialog box where you can define
   the schema manually.

   The schema in this example consists of five columns: *id,
   CustomerName, CustomerAddress, idState* and
   *id2*.
5. Click the [...] button next to the Filename field and browse to the XML file you want to
   process.
6. In the Loop XPath query, enter between
   inverted commas the path of the XML node on which to loop in order to retrieve
   data.

   In the Mapping table, Column is automatically populated with the defined
   schema.

   In the XPath query column, enter between
   inverted commas the node of the XML file that holds the data you want to extract
   from the corresponding column.
7. In the Limit field, enter the number of lines
   to be processed, the first 10 lines in this example.
8. Double-click tFileOutputXML to display its
   Basic settings view and define the
   component properties.
9. Click the [...] button next to the File
   Name field and browse to the output XML file you want to collect
   data in, *customer\_data.xml* in this example.

   In the Row tag field, enter between inverted
   commas the name you want to give to the tag that will hold the recuperated
   data.

   Click Edit schema to display the schema
   dialog box and make sure that the schema matches that of the preceding
   component. If not, click Sync columns to
   retrieve the schema from the preceding component.
10. Double-click tLogRow to display its Basic settings view and define the component
    properties.

    Click Edit schema to open the schema dialog
    box and make sure that the schema matches that of the preceding component. If
    not, click Sync columns to retrieve the schema
    of the preceding component.

    In the Mode area, select the Vertical option.
11. Save your Job and press F6 to execute
    it.

## Results

The output file *customer\_data.xml* holding the correct XML data is
created in the defined path and erroneous XML data is displayed on the console of the
Run view.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tlogrow-reading-and-extracting-data-from-an-xml-structure-configuring-job -->
# Setting up and executing the Job

Last updated: 9/30/2026

## Procedure

1. Open the Basic settings view of the
   tFileInputXML component by double-clicking the component and
   specify the following properties:
   1. Click the [...] button next to Edit
      schema to define the schema for this component and then click
      Yes to propagate the schema and close the schema
      editor. 

      In this example, the input file has three columns: City,
      District, and Street, which are all
      set as String data type. The following figure shows the
      columns added for the schema.

      The columns appears in the Column field of the
      Mapping table.
   2. Enter the path to the areas.xml file
      ("D:/obs/areas.xml" in this example) in the
      File name/Stream field.

      You can also enter the file path by clicking the [...] button to the
      right of this field and navigating to the areas.xml
      file.
   3. Enter the XPath of the street element of the
      areas.xml in the Loop XPath
      query field (`"/areas/area/street"` in this
      example).
   4. Enter the XPaths of the city and
      district attributes and the XPath of the
      street node of the areas.xml file in
      the XPath query column of the
      Mapping table, as shown in the following
      figure.
   5. Leave the other options as they are.
2. Open the Basic settings view of the
   tLogRow component by double-clicking the component and select
   Table (print values in cells of a table).
3. Save your Job and press F6 to execute
   it.

## Results

The city, district, and
street values are extracted from the XML file and displayed on the
console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tfileinputxml-tlogrow-reading-and-extracting-data-from-an-xml-structure-creating-job -->
# Creating the Job

Last updated: 9/30/2026

## Procedure

1. In the Integration
   perspective of Talend Studio,
   create an empty Standard Job.
2. Drop tFileInputXML and tLogRow from the Palette to the
   design workspace.
3. Connect both components together using a Main Row
   link.
