<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling · versión 8.0 -->
# tReservoirSampling

Last updated: 9/30/2026

Extracts a random sample data from a big data set.

tReservoirSampling extracts a sample from the input data set in such a way that profiling results on the sample data are uniform and homogeneous with the profiling results on the full data set.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tReservoirSampling Standard properties](/talend/en-US/components/8.0/sampling/treservoirsampling-standard-properties)
* [tReservoirSampling properties for Apache Spark Batch](/talend/en-US/components/8.0/sampling/treservoirsampling-properties-for-apache-spark-batch)

**Related concepts**  

* [Extracting sample data from an input data set](treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-extracting-sample-data-from-input-data-set-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-properties-for-apache-spark-batch -->
# tReservoirSampling properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tReservoirSampling running in the Spark Batch Job framework.

The Spark Batch
tReservoirSampling component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync columns to retrieve the schema from   the previous component in the Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sample Size | Set how many rows to sample from the input flow. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Seed for random generator | Set a random number if you want to extract the same sample in different executions of the Job.  Repeating the execution with a different value for the seed will result in a different data samples being extracted.  Keep this field empty if you want to extract a different data sample each time you execute the Job. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-standard-properties -->
# tReservoirSampling Standard properties

Last updated: 9/30/2026

These properties are used to configure tReservoirSampling running in the Standard Job framework.

The Standard
tReservoirSampling component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync columns to retrieve the schema from   the previous component in the Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sample Size | Set how many rows to sample from the input flow. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Seed for random generator | Set a random number if you want to extract the same sample in different executions of the Job.  Repeating the execution with a different value for the seed will result in a different data samples being extracted.  Keep this field empty if you want to extract a different data sample each time you execute the Job. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component helps you to test profiling analyses on a sample data and have results similar to the results on the full dataset.  tReservoirSampling can not be used in Map/Reduce Jobs for the time being. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-extracting-sample-data-from-input-data-set-standard-component-enterprise-this -->
# Extracting sample data from an input data set

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes a basic Job that extracts sample data from an input flow.

Below is a capture of the input flow:

To replicate the example described below, download the [tReservoirSampling\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tReservoirSampling_scenario.zip) file.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input data](/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-data-standard-component-enterprise)
* [Configuring the sample data](/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-sample-data-standard-component-enterprise)
* [Configuring the output component](/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-output-component-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-executing-job-standard-component-enterprise-save)

**Related concepts**  

* [tReservoirSampling](treservoirsampling "Extracts a random sample data from a big data set.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-data-standard-component-enterprise -->
# Configuring the input data

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputDelimited to display the
   Basic settings view and define the component
   properties.
2. In the File name/Stream field, browse to the file
   to be used as the main input.

   This file provides some information about customers.
3. Define the row and field separators and the header and footer in the corresponding
   fields, if any.
4. Click the [...] button next to Edit schema to open a dialog box and define the input schema. 

   In this example, according to the input file structure, the schema is made of ten
   columns.
5. Click the [+] button and define the input columns
   in the dialog box as in the above figure. Click OK to
   close the dialog box.
6. If needed, right-click tFileInputDelimited and
   select Data Viewer to display a view of the input
   data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-output-component-standard-component-enterprise -->
# Configuring the output component

Last updated: 9/30/2026

## Procedure

1. Double-click tFileOutputDelimited to display its
   Basic settings view and define the component
   properties.
2. In the File Name field, specify the path to the
   file to which you want to write the sample data.
3. Define the row and field separators in the corresponding fields, if any.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-sample-data-standard-component-enterprise -->
# Configuring the sample data

Last updated: 9/30/2026

## Procedure

1. Double-click tReservoirSampling to display the
   Basic settings view and define the component
   properties.
2. Click the Edit schema button to view the input and
   output columns and do any modifications in the output schema, if needed.
3. In the Sample Size field, enter a number for the
   rows you want to extract from the input flow, 24 in this example.
4. Click the Advanced settings tab and enter a random
   number in the Seed for random generator  field.

   By setting a number in this field, you will extract the same sample in each
   execution of the Job. Change the value if you want to extract a different sample.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-executing-job-standard-component-enterprise-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Save your Job and press F6 to execute it.

   The sample data is extracted and written to the output file.
2. Right-click the output component and select Data
   Viewer to display the extracted data.

   24 records have been extracted from the input file as you defined in the tReservoirSampling component settings. The Code column indicates that data has not been extracted
   sequentially from the input file. Data has been extracted in a way that any profiling
   results on the sample data will be close to the profiling results on the full data
   set.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sampling/treservoirsampling-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto
   the design workspace: tFileInputDelimited, tReservoirSampling and tFileOutputDelimited.
2. Connect all the components together using the Row 
   > Main link.
