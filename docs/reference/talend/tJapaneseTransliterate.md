<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate · versión 8.0 -->
# tJapaneseTransliterate

Last updated: 9/30/2026

Converts textual data in Japanese to kana and Latin scripts.

Transliteration is a phonetic operation where the tJapaneseTransliterate component attempts to create in kana characters or Roman characters (rōmaji) an equivalent of the original textual data based on the sounds the string represents.

The modern Japanese writing system uses a combination of kanji (Chinese characters) and syllabic kana (hiragana and katakana). For the benefit of non-Japanese speakers who cannot read kanji or kana, romanization systems have been developed to write the Japanese language in Latin script.

The tJapaneseTransliterate component converts Japanese into kana or rōmaji (Roman characters):

* Kana characters
  + Hiragana
  + Katakana reading
  + Katakana pronunciation
* Rōmaji
  + Revised Hepburn: This is the most widely used romanization system.
  + Kunrei-shiki: This romanization system has been standardized by the Japanese Government and the International Organisation for Standardisation as ISO 3602. It is a modified version of the Nihon-shiki system for modern standard Japanese.
  + Nihon-shiki: This romanization system is the most regular romanization system because it maintains a one-to-one correspondence between kana and rōmaji.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tJapaneseTransliterate Standard properties](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-standard-properties)
* [tJapaneseTransliterate properties for Apache Spark Batch](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-properties-for-apache-spark-batch)
* [tJapaneseTransliterate properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-properties-for-apache-spark-streaming)
* [tJapaneseTransliterate properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Transliterating Japanese text](tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-transliterating-japanese-text-using)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-properties-for-apache-spark-batch -->
# tJapaneseTransliterate properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJapaneseTransliterate
running in the Spark Batch Job framework.

The Spark Batch
tJapaneseTransliterate component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Transliteration | The columns from the output schema are added to the Column column in the Transliteration table.  For each of the schema columns containing Japanese text to be transliterated into another system, select the corresponding check box in the Transliterate column.  You can select the check box in the header row to select all schema columns.  After selecting the Transliterate check box, select the transliteration system from the Way to transliterate list:   * Hiragana (default value): this system   converts the input Japanese text into its hiragana form. * Katakana reading: this system converts the   input Japanese text (Kanji/Hiragana) into its katakana reading   form. * Katakana pronunication: this system converts   the input Japanese text (Kanji/Hiragana) into its katakana   pronunciation form. * Revised Hepburn: This is the most widely used   romanization system. * Kunrei-shiki: This romanization system has   been standardized by the Japanese Government and the International   Organisation for Standardisation as ISO 3602. It is a modified   version of the Nihon-shiki system for modern standard Japanese. * Nihon-shiki: This romanization system   maintains a one-to-one correspondence between kana and rōmaji. |

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
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-properties-for-apache-spark-structured-streaming -->
# tJapaneseTransliterate properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tJapaneseTransliterate running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tJapaneseTransliterate component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Transliteration | The columns from the output schema are added to the Column column in the Transliteration table.  For each of the schema columns containing Japanese text to be transliterated into another system, select the corresponding check box in the Transliterate column.  You can select the check box in the header row to select all schema columns.  After selecting the Transliterate check box, select the transliteration system from the Way to transliterate list:   * Hiragana (default value): this system   converts the input Japanese text into its hiragana form. * Katakana reading: this system converts the   input Japanese text (Kanji/Hiragana) into its katakana reading   form. * Katakana pronunication: this system converts   the input Japanese text (Kanji/Hiragana) into its katakana   pronunciation form. * Revised Hepburn: This is the most widely used   romanization system. * Kunrei-shiki: This romanization system has   been standardized by the Japanese Government and the International   Organisation for Standardisation as ISO 3602. It is a modified   version of the Nihon-shiki system for modern standard Japanese. * Nihon-shiki: This romanization system   maintains a one-to-one correspondence between kana and rōmaji. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-standard-properties -->
# tJapaneseTransliterate Standard properties

Last updated: 9/30/2026

These properties are used to configure tJapaneseTransliterate
running in the Standard Job framework.

The Standard
tJapaneseTransliterate component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description, and   it defines the fields to be processed and passed on to the next component.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Transliteration | The columns from the output schema are added to the Column column in the Transliteration table.  For each of the schema columns containing Japanese text to be transliterated into another system, select the corresponding check box in the Transliterate column.  You can select the check box in the header row to select all schema columns.  After selecting the Transliterate check box, select the transliteration system from the Way to transliterate list:   * Hiragana (default value): this system   converts the input Japanese text into its hiragana form. * Katakana reading: this system converts the   input Japanese text (Kanji/Hiragana) into its katakana reading   form. * Katakana pronunication: this system converts   the input Japanese text (Kanji/Hiragana) into its katakana   pronunciation form. * Revised Hepburn: This is the most widely used   romanization system. * Kunrei-shiki: This romanization system has   been standardized by the Japanese Government and the International   Organisation for Standardisation as ISO 3602. It is a modified   version of the Nihon-shiki system for modern standard Japanese. * Nihon-shiki: This romanization system   maintains a one-to-one correspondence between kana and rōmaji. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-transliterating-japanese-text-using -->
# Transliterating Japanese text

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

Using the tJapaneseTransliterate component, you can transliterate
Japanese.

To replicate the example described below, download the [tJapaneseTransliterate\_standard\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tJapaneseTransliterate_standard_scenario.zip)
file.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-configuring-input-component-standard-component-enterprise-you)
* [Configuring the transliteration](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-configuring-transliteration-standard-component-enterprise)
* [Configuring the output component and executing the Job](/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-configuring-output-component-and-executing-job-standard-component-enterprise)

**Related concepts**  

* [tJapaneseTransliterate](tjapanesetransliterate "Converts textual data in Japanese to kana and Latin scripts.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-configuring-input-component-standard-component-enterprise-you -->
# Configuring the input component

Last updated: 9/30/2026

## Before you begin

You downloaded the [tJapaneseTransliterate\_standard\_scenario.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tJapaneseTransliterate_standard_scenario.zip)
file.

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view in the
   Component tab.
2. Click the Edit schema button to define the columns of
   the source dataset and their data type.
3. Click the [+] button to add the schema columns.

   ### Example

   In this example, the input schema is made of six columns to show the ways
   to transliterate supported by the
   tJapaneseTransliterate component.
4. Click OK to validate these changes and accept the
   propagation when prompted.
5. In the Mode area, select Use Inline
   Content(delimited file).
6. Define the characters to be used as Row Separator and
   Field Separator.
7. In the Content field, enter the input data.

   In this example, the input sentences in Japanese are duplicated in each of the
   input columns.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-configuring-output-component-and-executing-job-standard-component-enterprise -->
# Configuring the output component and executing the Job

Last updated: 9/30/2026

## Procedure

1. Double-click tLogRow to open its Basic
   settings view in the Component tab.
2. Click Sync columns to retrieve the schema from the
   preceding component.
3. In the Mode area, select Vertical (each row
   is a key/value list).
4. Press 
   F6
    to run the Job.

## Results

Three tables are displayed in the console of the Run
view.

The tables correspond the three rows in the input data.

Each of the
tables contains the original sentence in Japanese, the transliterated text into
hiragana, katakana (reading and pronunciation), revised Hepburn, Kunrei-shiki and
Nihon-shiki
systems.

```
.-------------------------------------------------------.
|                     #1. tLogRow_1                     |
+------------------------+------------------------------+
| key                    | value                        |
+------------------------+------------------------------+
| Japanese               | 日本は漫画の国です                    |
| Hiragana               | にっぽん は まんが の くに です           |
| Katakana_reading       | ニッポン ハ マンガ ノ クニ デス           |
| Katakana_pronunciation | ニッポン ワ マンガ ノ クニ デス           |
| Revised_Hepburn        | nippon wa manga no kuni desu |
| Kunrei_shiki           | nippon wa manga no kuni desu |
| Nihon_shiki            | nippon wa manga no kuni desu |
+------------------------+------------------------------+

.----------------------------------------------------------------------.
|                            #2. tLogRow_1                             |
+------------------------+---------------------------------------------+
| key                    | value                                       |
+------------------------+---------------------------------------------+
| Japanese               | ンスフラ語はこの文を理解していない                           |
| Hiragana               | んすふら ご は この ぶん を りかい し て い ない               |
| Katakana_reading       | ンスフラ ゴ ハ コノ ブン ヲ リカイ シ テ イ ナイ               |
| Katakana_pronunciation | ンスフラ ゴ ワ コノ ブン ヲ リカイ シ テ イ ナイ               |
| Revised_Hepburn        | nsufura go wa kono bun o rikai shi te i nai |
| Kunrei_shiki           | nsuhura go wa kono bun o rikai si te i nai  |
| Nihon_shiki            | nsuhura go wa kono bun wo rikai si te i nai |
+------------------------+---------------------------------------------+

.------------------------------------------.
|              #3. tLogRow_1               |
+------------------------+-----------------+
| key                    | value           |
+------------------------+-----------------+
| Japanese               | リンゴを食べる         |
| Hiragana               | りんご を たべる       |
| Katakana_reading       | リンゴ ヲ タベル       |
| Katakana_pronunciation | リンゴ ヲ タベル       |
| Revised_Hepburn        | ringo o taberu  |
| Kunrei_shiki           | ringo o taberu  |
| Nihon_shiki            | ringo wo taberu |
+------------------------+-----------------+
```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-configuring-transliteration-standard-component-enterprise -->
# Configuring the transliteration

Last updated: 9/30/2026

## Procedure

1. Double-click tJapaneseTransliterate to open its
   Basic settings view in the
   Component tab.
2. Click Sync columns to retrieve the schema from the
   preceding component.
3. In the Transliteration table, select the corresponding
   check box in the Transliterate column for each of the
   schema columns containing Japanese text to be transliterated.
4. Select the target transliteration system from the Way to
   transliterate column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/tjapanesetransliterate-tfixedflowinput-tlogrow-tlogrow-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the
   design workspace: tFixedFlowInput,
   tJapaneseTransliterate and
   tLogRow.
2. Connect the tFixedFlowInput component to the
   tJapaneseTransliterate component using the Row > Main link.
3. Connect the tJapaneseTransliterate component to the
   tLogRow component using the Row > Main link.

## Results
