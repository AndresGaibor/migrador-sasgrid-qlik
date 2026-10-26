<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile · versión 8.0 -->
# tHMapFile

Last updated: 9/30/2026

Information noteNote: This component is not shipped
with your Talend Studio by
default. To use it, you need to install the Data Mapper > Talend Data Mapper for Spark feature using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

Runs a
Talend Data Mapper
map where input and output structures may differ, as a Spark batch
execution.

tHMapFile transforms data from a
single source, in a Spark environment.

## tHMapFile properties for Apache Spark Batch

These properties are used to configure tHMapFile running in the Spark Batch Job framework.

The Spark Batch
tHMapFile component belongs to the Processing family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Storage | To connect to an HDFS installation, select the Define a storage configuration component check box and then select the name of the component to use from those available in the drop-down list.  This option requires you to have previously configured the connection to the HDFS installation to be used, as described in the *documentation* for the tHDFSConfiguration component.  If you leave the Define a storage configuration component check box unselected, you can only convert files locally. |
| Configure Component | To configure the component, click the [...] button and, in the Component Configuration window, perform the following actions.   1. Click the Select button next to the Record Map field and then, in    the Select a Map dialog box    that opens, select the map you want to use and then click    OK.  This map must have been previously created in *Talend Data Mapper*.  Note that the input and output representations    are those defined in the map, and cannot be changed in the    component. 2. Click Next. 3. Tell the component where each new record begins.    In order for you to be able to do so, you need to fully    understand the structure of your data.  Exactly how you do this varies depending on the    input representation being used, and you will be presented with    one of the following options.     1. Select an appropriate       record delimiter for your data. Note that you must       specify this value without quotes.       * Separator lets you specify a         separator indicator, such as *\n*, to identify a new         line.  Supported         indicators are *\n* for a Unix-type new line, *\r\n* for         Windows and *\r* for Mac, and *\t* for tab characters.       * Start/End with lets you specify the         initial characters that indicate a new record,         such as *<root*, or the characters that indicate         where a record ends. This can also be a regular         expression.  Start         with also supports new lines, *\n* for a         Unix-type new line, *\r\n* for Windows and *\r* for Mac,         and *\t* for         tab characters.       * Sample         File: To test the signature with a         sample file, click the [...] button, browse to the file you         want to use as a sample, click Open, and then click         Run to test         your sample. Testing the         signature lets you check that the total number of         records and their minimum and maximum length         corresponds to what you expect based on your         knowledge of the data. This step assumes you have         a local subset of your data to use as a         sample.       * Click Finish.    2. If your input representation is COBOL or       Flat with positional and/or binary encoding properties,       define the signature for the input record structure:       * Input Record root         corresponds to the root element in your input         record.       * Minimum Record         Size corresponds to the size in bytes         of the smallest record. If you set this value too         low, you may encounter performance issues, since         the component will perform more checks than         necessary when looking for a new record.       * Maximum Record         Size corresponds to the size in bytes         of the largest record, and is used to determine         how much memory is allocated to read the         input.       * Sample from Workspace or         Sample from File System: To         test the signature with a sample file, click the         [...]         button, and then browse to the file you want to         use as a sample. Testing the signature lets you         check that the total number of records and their         minimum and maximum length corresponds to what you         expect based on your knowledge of the data. This         step assumes you have a local subset of your data         to use as a sample.       * Footer Size         corresponds to the size in bytes of the footer, if         any. At runtime, the footer will be ignored rather         than being mistakenly included in the last record.         Leave this field empty if there is no footer.       * Click the Next button to open         the Signature         Parameters window, select the fields         that define the signature of your record input         structure (that is, to identify where a new record         begins), update the Operation and Value columns as         appropriate, and then click Next.       * In the Record         Signature Test window that opens, check         that your Records are correctly delineated by         scrolling through them with the         Back and         Next buttons and performing         a visual check, and then click         Finish. |
| Input | Click the [...] button to define the path to where the input file is stored. |
| Output | Click the [...] button to define the path to where the output files will be stored. |
| Action | From the drop-down list, select:  * Create if you want   the mapping process to create a new file. * Overwrite if you want   the mapping process to overwrite an existing file. |
| Open Map Editor | Click the [...] button to open the Structure Generate/Select wizard.  You can first select the type of map to create:  * Standard Map: Map that perform mappings using   functions based on xQuery * DSQL Map: Map that performs mappings using   Data Shaping Query Language.  You can select the Don't ask me again check box to save this preference. For more information about these map types, see [Working with maps](/talend/r/en-US/8.0/data-mapper-user-guide/working-with-maps). Information noteNote: This option is available only if you have installed the R2023-10 Studio monthly update or a later one delivered by Talend. For more information, check with your administrator.  Then you can either have the hierarchical mapper structure generated automatically based on the schema, or select an existing hierarchical mapper structure. You must do this for both the input and output sides of your Map. The following lists the options for the output structure:  * Generate hierarchical mapper structure based on the   schema option: When you connect multiple output   connections to the tHMap, the page displays a confirmation message   that informs you that the mapper structures are generated based on   the output connections. * Select an existing hierarchical mapper   structure option: You can connect multiple outputs   that are payload-based connections to the tHMap. If there is a   single payload-type connection, you can select the Allow   support for multiple output connections check box.   The generated output map inherits from the existing payload   structure.  If Talend Studio detects multiple output connections available, the window displays both output structure options without the support for multiple output connections check boxes.  If neither input nor output connection exists, the Structure Selection page is displayed. |
| **Die on error** | This check box is selected by default.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  If you opt to clear the check box, you can perform any of these options:  * Row >  Rejectsconnection. In the output component, ensure   that you add a fixed metadata with the following columns:   + inputRecord: contains the rejected     input record during the transformation.   + recordId: refers to the record     identifier. For a text or binary input, the recordId     specifies the start offset of the record in the     input file. For an AVRO input, the recordId     specifies the timestamp when the input was     processed.   + errorMessage: contains the     transformation status with details of the cause of     the transformation error. * If the check box is unselected, you can retrieve the rejected   records in a file. One of these mechanisms triggers this   feature: (1) a context variable   (Connect the tHMapFile component to an output   component, for example tAvroOutput, using a talend\_transform\_reject\_file\_path)   and (2) a system variable set in the Advanced Job parameters   (spark.hadoop.talend.transform.reject.file.path).  When you set the file path on the Hadoop Distributed File   System (HDFS), no further configurations are needed. When   you set the file on Amazon S3 or any other Hadoop-compatible   file systems, add the associated Spark advanced   configuration parameter.  In case of errors at runtime, tHMapFile checks if one of   the mechanisms exists and, if so, appends the rejected   record to the designated file. The reject file content   includes the concatenation of the rejected records without   any additional metadata.  If the file system you use does not support   appending to a file, a separate file is created for each   rejection. The file uses the provided file path as the   prefix and adds a suffix that is the offset of the input   file and the size of the rejected record.  Information noteNote: Any errors while trying to store the reject are logged and the processing continues. |
| Merge result to single file | By default, the tHMapFile creates several part files. Select this check box to merge these files into a single file.  The following options are used to manage the source and the target files:  * Merge File   Path: enter the path to the file which will   contain the merged content from all parts. * Remove source   dir: select this check box to remove the source   files after the merge. * Override target file: select   this check box to override the file already existing in the   target location. This option does not override the folder. * Include   Header: select this check box to add the CSV   header to the beginning of the merged file. This option is only   used for CSV outputs. For other representations, it has no   effect on the target file.  Information noteWarning: Using this option with an Avro output creates an invalid Avro file. Since each part starts with an Avro Schema header, the merged file would have more than one Avro Schema, which is invalid. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use old Eclipse runtime (deprecated) | Select this check box to include the old Eclipse runtime in your Job. Information noteNote: This option is available only if you have installed the R2024-03 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator.  Information noteNote: From Talend Studio 8.0 R2025-04 onwards, the Use old Eclipse runtime (deprecated) parameter has been removed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used with a tHDFSConfiguration component which defines the connection to the HDFS storage, or as a standalone component for mapping local files only. |
| Usage with Talend Runtime | If you want to deploy a Job or Route containing a data mapping component with Talend Runtime, you first need to install the Talend Data Mapper feature. For more information, see [Using Talend Data Mapper with Talend Runtime](/talend/r/en-US/8.0/data-mapper-user-guide/using-talend-data-mapper-with-talend-runtime). |

**Related concepts**  

* [Transforming data in a Spark environment](thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-transforming-data-in-spark-environment-spark-batch-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-transforming-data-in-spark-environment-spark-batch-component-the -->
# Transforming data in a Spark environment

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend Platform
products with Big Data and Talend Data Fabric.

The following scenario creates a two-component Job that transforms data in
a Spark environment using a map that was previously created in *Talend Data Mapper*.

tHDFSConfiguration is used in this scenario by Spark to connect
to the HDFS system where the jar files dependent on the Job are transferred.

In the Spark
Configuration tab in the Run
view, define the connection to a given Spark cluster for the whole Job. In
addition, since the Job expects its dependent jar files for execution, you must
specify the directory in the file system to which these jar files are
transferred so that Spark can access these files:

* Yarn mode (Yarn client or Yarn cluster):
  + When using Google Dataproc, specify a bucket in the
    Google Storage staging bucket
    field in the Spark configuration
    tab.
  + When using HDInsight, specify the blob to be used for Job
    deployment in the Windows Azure Storage
    configuration area in the Spark
    configuration tab.
  + When using Altus, specify the S3 bucket or the Azure
    Data Lake Storage for Job deployment in the Spark
    configuration tab.
  + When using on-premises distributions, use
    the configuration component corresponding to the file system
    your cluster is using. Typically, this system is HDFS and so
    use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
* Standalone mode: use the
  configuration component corresponding to the file system your cluster is
  using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

  If you are using Databricks without any configuration component present
  in your Job, your business data is written directly in DBFS (Databricks
  Filesystem).

### In this section

* [Downloading the input files](/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-downloading-input-files-spark-batch-component-re)
* [Creating the input and output structures](/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-creating-input-and-output-structures-spark-batch-component-in)
* [Creating the map](/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-creating-map-spark-batch-component-in)
* [Adding the components](/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-adding-components-spark-batch-component-in)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/data-mapping/configuring-connection-to-file-system-to-be-used-by-spark?id=767)
* [Defining the properties of tHMapFile](/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-defining-properties-of-thmapfile-spark-batch-component-in)
* [Selecting the Spark mode](/talend/en-US/components/8.0/data-mapping/selecting-spark-mode-spark-batch?id=769)
* [Saving and executing the Job](/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-saving-and-executing-job-spark-batch-component-press)

**Related reference**  

* [tHMapFile](thmapfile "Runs a Talend Data Mapper map where input and output structures may differ, as a Spark batch execution.")

**Related information**  

* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tS3Configuration](/talend/en-US/components/8.0/amazon-s3/ts3configuration)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-adding-components-spark-batch-component-in -->
# Adding the components

Last updated: 9/30/2026

## Procedure

1. In the 
   Integration
    perspective, create a new
   Job and call it *thmapfile\_transform*.
2. Click any point in the design workspace, start typing tHDFSConfiguration, and then click the name of the component when it
   appears in the list proposed in order to select it.

   Note that for testing purposes, you can also perform this scenario locally. In
   that case, do not add the tHDSFConfiguration
   component and skip the *Configuring the connection to the
   file system used by Spark* section below.
3. Do the same to add a tHMapFile component, but do
   not link the two components.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-creating-input-and-output-structures-spark-batch-component-in -->
# Creating the input and output structures

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective, in the Repository tree view, expand Metadata >
   Hierarchical Mapper, right click Structures, and then click New >
   Structure.
2. In the New Structure dialog box that opens,
   select Import a structure definion, and then click
   Next.
3. Select JSON Sample Document, and then click
   Next.
4. Select Local file, browse to the location on your
   local file system where you saved the source files, import *gdelt-onerec.json* as your sample document, and then click Next.
5. Give your new structure a name, *gdelt-onerec* in
   this example, click Next, and then click Finish.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-creating-map-spark-batch-component-in -->
# Creating the map

Last updated: 9/30/2026

## Procedure

1. In the Repository tree view, expand Metadata > Hierarchical Mapper, right click Maps, and then click New >
   Map.
2. In the Select Type of New Map dialog box that
   opens, select Standard Map and then click Next.
3. Give your new map a name, *json2xml* in this
   example, and then click Finish.
4. Drag the *gdelt-onerec* structure you created
   earlier into both the Input and Output sides of the map.
5. On the Output side of the map, change the
   representation used from JSON to XML by double-clicking Output
   (JSON) and selecting the XML output
   representation.
6. Drag the Root element from the Input side of the map to the Root element on the Output side. This
   maps each element from the Input side with its
   corresponding element on the Outside side, which is
   a very simple map just for testing purposes.
7. Press Ctrl+S to save your map.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-defining-properties-of-thmapfile-spark-batch-component-in -->
# Defining the properties of tHMapFile

Last updated: 9/30/2026

## Procedure

1. In the Job, select the tHMapFile component to define its
   properties.
2. Select the Define a storage configuration
   component check box and then select the name of the component to use
   from those available in the drop-down list, tHDFSConfiguration\_1 in this example.

   Note that if you leave the Define a storage configuration
   component check box unselected, you can only transform files
   locally.
3. Click the [...] button and, in the Component Configuration window, click the Select button next to the Record
   Map field.
4. In the Select a Map dialog box that opens,
   select the map you want to use and then click OK.
   In this example, use the *json2xml* map you just
   created.
5. Click Next.
6. Select an appropriate record delimitor for your data that tells the component
   where each new record begins.

   In this example, each record is on a new line, so select Separator and specify the newline character, *\n* in this example.
7. Click Finish.
8. Click the [...] button next to the Input field to define the path to the input file, */talend/input/gdelt.json* in this example.
9. Click the [...] button next to the Output field to define the path to where the output file is
   to be stored, */talend/output* in this
   example.
10. Leave the other settings unchanged.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-downloading-input-files-spark-batch-component-re -->
# Downloading the input files

Last updated: 9/30/2026

## Procedure

1. Download the input files for this scenario. 

   The [thmapfile\_transform\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/thmapfile_transform_scenario.zip) file contains two files:
   gdelt.json is a JSON file built using data from the GDELT
   project <http://gdeltproject.org>, and gdelt-onerec.json is a
   subset of gdelt.json containing just one record and is used as a
   sample document for creating the structure in *Talend Data Mapper*.
2. Save the thmapfile\_scenario.zip file on your
   local machine and unpack the .zip file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/thmapfile-thdfsconfiguration-ts3configuration-ts3configuration-saving-and-executing-job-spark-batch-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. In the Run tab, click Run to execute the Job.
3. Browse to the location on your file system where the output files are stored to
   check that the transformation was performed successfully.
