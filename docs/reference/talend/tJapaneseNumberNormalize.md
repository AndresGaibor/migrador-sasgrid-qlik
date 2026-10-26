<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize · versión 8.0 -->
# tJapaneseNumberNormalize

Last updated: 9/30/2026

Normalizes Japanese numbers (kansūji) to regular Arabic
numbers.

Japanese numbers are often written using a combination of kanji and Arabic
numbers with punctuation marks. Normalizing Japanese numbers can make those numbers more
easily searchable and improve matching accuracy.

For example, tJapaneseNumberNormalize
normalizes ３．２千 to 3200. This enables you to match the Japanese number "３．２千" with its
Arabic counterpart "3200".

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tJapaneseNumberNormalize standard properties](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-standard-properties)
* [tJapaneseNumberNormalize properties for Apache Spark Batch](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-properties-for-apache-spark-batch)
* [tJapaneseNumberNormalize properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-properties-for-apache-spark-streaming)
* [tJapaneseNumberNormalize properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Converting Japanese numbers to Arabic numbers](tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-converting-japanese-numbers-to-arabic-numbers-using)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-properties-for-apache-spark-batch -->
# tJapaneseNumberNormalize properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure
tJapaneseNumberNormalize running in the Spark
Batch Job framework.

The Spark Batch
tJapaneseNumberNormalize component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Normalization | The columns from the output schema are added to the Column column in the Normalization table.  For each of the schema columns containing Japanese numbers to be normalized to Arabic numbers, select the corresponding check box in the Normalize column.  You can select the check box in the header row to select all schema columns. |

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
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-properties-for-apache-spark-structured-streaming -->
# tJapaneseNumberNormalize properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tJapaneseNumberNormalize running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tJapaneseNumberNormalize component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Normalization | The columns from the output schema are added to the Column column in the Normalization table.  For each of the schema columns containing Japanese numbers to be normalized to Arabic numbers, select the corresponding check box in the Normalize column.  You can select the check box in the header row to select all schema columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-standard-properties -->
# tJapaneseNumberNormalize standard properties

Last updated: 9/30/2026

These properties are used to configure
tJapaneseNumberNormalize running in the
Standard Job framework.

The Standard
tJapaneseNumberNormalize component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Normalization | The columns from the output schema are added to the Column column in the Normalization table.  For each of the schema columns containing Japanese numbers to be normalized to Arabic numbers, select the corresponding check box in the Normalize column.  You can select the check box in the header row to select all schema columns. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-converting-japanese-numbers-to-arabic-numbers-using -->
# Converting Japanese numbers to Arabic numbers

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

Using the tJapaneseNumberNormalize component, you can convert Japanese
numbers to Arabic Numbers.

To replicate the example described below, download the [tJapaneseNumberNormalize\_standard\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tJapaneseNumberNormalize_standard_scenario.zip)
file.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-configuring-input-component-standard-component-enterprise-you)
* [Configuring the normalization of Japanese numbers](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-configuring-normalization-of-japanese-numbers-standard-component-enterprise)
* [Configuring the output component and executing the Job](/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-configuring-output-component-and-executing-job-standard-component-enterprise)

**Related concepts**  

* [tJapaneseNumberNormalize](tjapanesenumbernormalize "Normalizes Japanese numbers (kansūji) to regular Arabic numbers.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-configuring-input-component-standard-component-enterprise-you -->
# Configuring the input component

Last updated: 9/30/2026

## Before you begin

You downloaded the [tJapaneseNumberNormalize\_standard\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tJapaneseNumberNormalize_standard_scenario.zip)
file.

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view in the
   Component tab.
2. Click the Edit schema button to define the columns of
   the source dataset and their data type.
3. Click the [+] button to add the schema columns.

   ### Example
4. Click OK to validate these changes and accept the
   propagation when prompted.
5. Select Use Inline Content(delimited file) in the
   Mode area.
6. Define the characters to be used as Row Separator and
   Field Separator.
7. Enter the input data in the Content table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-configuring-normalization-of-japanese-numbers-standard-component-enterprise -->
# Configuring the normalization of Japanese numbers

Last updated: 9/30/2026

## Procedure

1. Double-click tJapaneseNumberNormalize to open its
   Basic settings view in the
   Component tab.
2. Click Sync columns to retrieve the schema from the
   preceding component.
3. In the Normalization table, select the corresponding
   check box in the Normalize column for each of the schema
   columns containing Japanese numbers to be normalized to Arabic numbers.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-configuring-output-component-and-executing-job-standard-component-enterprise -->
# Configuring the output component and executing the Job

Last updated: 9/30/2026

## Procedure

1. Double-click tLogRow to open its Basic
   settings view in the Component tab.
2. Click Sync columns to retrieve the schema from the
   preceding component.
3. Select Table (print values in cells of a table) in the
   Mode area.
4. Press 
   F6
    to run the Job.

## Results

The normalized numbers are written in Run view:

```
.-----------------+---------------------.
|               tLogRow_1               |
|=----------------+--------------------=|
|kansuji          |normalized_arabic_num|
|=----------------+--------------------=|
|〇〇七              |7                    |
|一〇〇〇             |1000                 |
|三千2百２十三          |3223                 |
|15,7             |157                  |
|一万               |10000                |
|負一千一百五十八         |-1158                |
|１．２万３４５．６７       |12345.67             |
|１．２万３４５．６三       |12345.63             |
|4,647.100        |4647.1               |
|七十五點四零二五         |75.4025              |
|万                |10000                |
|億                |100000000            |
|兆                |1000000000000        |
|京                |10000000000000000    |
|垓                |100000000000000000000|
|九百八十三万 六千七百三     |9836703              |
|二十億 三千六百五十二万 千八百一|2036521801           |
|¥百二十三            |¥123                 |
|百二十三円            |123円                 |
'-----------------+---------------------'
```

The tJapaneseNumberNormalize supports Japanese numbers written
using a sequence of kanji numerals: 〇〇七 becomes 7.

The tJapaneseNumberNormalize supports Japanese numbers written
using a combination of kanji and Arabic numbers: 三千2百２十三 becomes 3223.

The decimal comma is not kept in the normalized numbers returned by the
tJapaneseNumberNormalize component. As a result, 4,647.100
becomes 4647.1 and 15,7 becomes 157. If the input numbers use the decimal comma as
the decimal separator, you must replace the decimal comma with a decimal point.

The input numbers can use a comma to separate groups of thousands: 4,647.100 becomes
4647.1. The tJapaneseNumberNormalize component also removes
trailing zeros from the input number.

The tJapaneseNumberNormalize supports large kanji numbers: 兆六百万五千一
becomes 1000006005001.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesenumbernormalize-tfixedflowinput-tlogrow-tlogrow-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the
   design workspace: tFixedFlowInput,
   tJapaneseNumberNormalize and
   tLogRow.
2. Connect the tFixedFlowInput component to the
   tJapaneseNumberNormalize component using the Row > Main link.
3. Connect the tJapaneseNumberNormalize component to the
   tLogRow component using the Row > Main link.

## Results
