<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize · versión 8.0 -->
# tJapaneseTokenize

Last updated: 9/30/2026

Splits Japanese text into tokens.

Tokenization is an important pre-processing step and prepares text data for subsequent analysis, transliteration, text mining or natural language processing tasks.

Unlike English or French, there are no spaces to mark word boundaries in Japanese. Splitting Japanese text into tokens is then more challenging.

Based on the IPADIC dictionary, tJapaneseTokenize deduces where word boundaries exist and adds a space to separate tokens.

The IPADIC dictionary was developed by the Information-Technology Promotion Agency of Japan (IPA). This dictionary is based on the IPA corpus and is the most widely used dictionary for Japanese tokenization.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tJapaneseTokenize Standard properties](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-standard-properties)
* [tJapaneseTokenize properties for Apache Spark Batch](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-properties-for-apache-spark-batch)
* [tJapaneseTokenize properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-properties-for-apache-spark-streaming)
* [tJapaneseTokenize properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Tokenizing Japanese text](tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-tokenizing-japanese-text-using)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-properties-for-apache-spark-batch -->
# tJapaneseTokenize properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJapaneseTokenize
running in the Spark Batch Job framework.

The Spark Batch
tJapaneseTokenize component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Tokenization | The columns from the output schema are added to the Column column in the Tokenization table.  For each of the schema columns containing Japanese text to be tokenized, select the corresponding check box in the Tokenize column.  You can select the check box in the header row to select all schema columns. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-properties-for-apache-spark-structured-streaming -->
# tJapaneseTokenize properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tJapaneseTokenize running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tJapaneseTokenize component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

Information noteImportant: Before you run this component, manually upload the kuromoji-ipadic JAR to the cluster because it is too large for automatic upload.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Tokenization | The columns from the output schema are added to the Column column in the Tokenization table.  For each of the schema columns containing Japanese text to be tokenized, select the corresponding check box in the Tokenize column.  You can select the check box in the header row to select all schema columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-standard-properties -->
# tJapaneseTokenize Standard properties

Last updated: 9/30/2026

These properties are used to configure tJapaneseTokenize running
in the Standard Job framework.

The Standard
tJapaneseTokenize component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Tokenization | The columns from the output schema are added to the Column column in the Tokenization table.  For each of the schema columns containing Japanese text to be tokenized, select the corresponding check box in the Tokenize column.  You can select the check box in the header row to select all schema columns. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-tokenizing-japanese-text-using -->
# Tokenizing Japanese text

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

Using the tJapaneseTokenize component, you can split Japanese text
into tokens.

To replicate the example described below, download the [tJapaneseTokenize\_standard\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tJapaneseTokenize_standard_scenario.zip) file.

The [tJapaneseTokenize\_standard\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tJapaneseTokenize_standard_scenario.zip) file is composed of:

* the plain text file inputJapaneseText.txt containing
  Japanese text, the transcription and the English translation; and
* the tJapaneseTokenizeJob.zip file containing the Job.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-component-standard-component-enterprise-you)
* [Configuring the tokenization](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-tokenization-standard-component-enterprise)
* [Configuring the output component and executing the Job](/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-output-component-and-executing-job-standard-component-enterprise)

**Related concepts**  

* [tJapaneseTokenize](tjapanesetokenize "Splits Japanese text into tokens.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-component-standard-component-enterprise-you -->
# Configuring the input component

Last updated: 9/30/2026

## Before you begin

You downloaded the [tJapaneseTokenize\_standard\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tJapaneseTokenize_standard_scenario.zip) file.

## Procedure

1. Double-click tFileInputDelimited to open its
   Basic settings view in the
   Component tab.
2. In the File name/Stream field, enter the path to the
   file containing the input text to be tokenized.
3. Define the characters to be used as Row Separator and
   Field Separator.
4. Define the numbers of rows in the Header and the
   Footer.
5. Click the Edit schema button to define the columns of
   the source dataset and their data type.
6. Click the [+] button to add the schema columns.

   ### Example
7. Click OK to validate these changes and accept the
   propagation when prompted.
8. In the Advanced settings tab of the
   tFileInputDelimited component, select the right
   encoding from the Encoding list.

   The inputJapaneseText.txt file uses the UTF-8
   encoding.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-output-component-and-executing-job-standard-component-enterprise -->
# Configuring the output component and executing the Job

Last updated: 9/30/2026

## Procedure

1. Double-click tFileOutputDelimited to open its
   Basic settings view in the
   Component tab.
2. In the File Name field, enter the path to the output
   file.
3. Click Sync columns to retrieve the schema from the
   preceding component.
4. Optional: 
   Select the Include Header check box to include columns
   headers in the output file.
5. In the Advanced settings tab of the
   tFileOutputDelimited component, select
   UTF-8 from the Encoding
   list.
6. Press 
   F6
    to run the Job.

## Results

The tokenized text is written in the file you defined in the File
Name field of the tFileOutputDelimited
component.

Spaces have been added to separate tokens.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-tokenization-standard-component-enterprise -->
# Configuring the tokenization

Last updated: 9/30/2026

## Procedure

1. Double-click tJapaneseTokenize to open its
   Basic settings view in the
   Component tab.
2. Click Sync columns to retrieve the schema from the
   preceding component.
3. In the Tokenization table, select the corresponding
   check box in the Tokenize column for each of the schema
   columns containing Japanese text to be tokenized.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetokenize-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the
   design workspace: tFileInputDelimited,
   tJapaneseTokenize and
   tFileOutputDelimited.
2. Connect the tFileInputDelimited component to the
   tJapaneseTokenize component using the Row > Main link.
3. Connect the tJapaneseTokenize component to the
   tFileOutputDelimited component using the Row > Main link.

## Results
