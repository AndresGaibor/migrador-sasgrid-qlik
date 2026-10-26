<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate · versión 8.0 -->
# tTransliterate

Last updated: 9/30/2026

Converts strings from many languages of the world to a standard set of characters (Universal Coded Character Set, UCS).

This is a phonetic operation where the tTransliterate component attempts to create in UCS an equivalent of the original string based on the sounds the string represents.

tTransliterate encodes text expressed in many of the world's writing systems to readable characters based on the repertoire of the Unicode Standard. This makes it easier for you to recognize and interpret words from different languages than if the letters are left in the original script. For further information about Unicode and Unicode Standard, check [Unicode](https://en.wikipedia.org/wiki/Unicode) and [Unicode Standard](http://unicode.org/standard/standard.html).

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tTransliterate Standard properties](/talend/en-US/components/8.0/text-standardization/ttransliterate-standard-properties)
* [tTransliterate properties for Apache Spark Batch](/talend/en-US/components/8.0/text-standardization/ttransliterate-properties-for-apache-spark-batch)
* [tTransliterate properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/text-standardization/ttransliterate-properties-for-apache-spark-streaming)
* [tTransliterate properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/text-standardization/ttransliterate-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Converting words from different languages to standard set of characters](ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-converting-words-from-different-languages-to-standard-set-of-characters-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-properties-for-apache-spark-batch -->
# tTransliterate properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tTransliterate running in the Spark Batch Job framework.

The Spark Batch
tTransliterate component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Transliteration | This table lists the columns defined in the schema of the tTransliterate component.  Select the Transliterate check box next to the column(s) of which you want to convert the content to readable standard set of characters. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-properties-for-apache-spark-structured-streaming -->
# tTransliterate properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tTransliterate running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tTransliterate component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Transliteration | This table lists the columns defined in the schema of the tTransliterate component.  Select the Transliterate check box next to the column(s) of which you want to convert the content to readable standard set of characters. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-standard-properties -->
# tTransliterate Standard properties

Last updated: 9/30/2026

These properties are used to configure tTransliterate running in the Standard Job framework.

The Standard
tTransliterate component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Transliteration | This table lists the columns defined in the schema of the tTransliterate component.  Select the Transliterate check box next to the column(s) of which you want to convert the content to readable standard set of characters. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediary step. It requires an input and output flows. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-converting-words-from-different-languages-to-standard-set-of-characters-standard-component-enterprise-this -->
# Converting words from different languages to standard set of characters

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes a Job which uses:

* the tFixedFlowInput component to generate the
  data you want to process,
* the tTransliterate component to encode initial
  data expressed in different languages to readable characters based on the repertoire
  of the Unicode Standard,
* the tFileOutputExcel component to output
  converted data in an .xls file.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise)
* [Transliterating data](/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-transliterating-data-standard-component-enterprise)
* [Configuring the output component and executing the Job](/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise)

**Related concepts**  

* [tTransliterate](ttransliterate "Converts strings from many languages of the world to a standard set of characters (Universal Coded Character Set, UCS).")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view in the Component tab.
2. Create the schema through the Edit Schema
   button.

   In the open dialog box, click the [+] button
   and add the columns that will hold input data. For this example, add
   *column1*, *column2*,
   *column3* and *column4*. The first two
   columns hold names written in different languages.
3. Click OK.
4. In the Number of rows field, enter
   *1*.
5. In the Mode area, select the Use Inline Content option.
6. In the Content table, enter the data you want
   to convert to readable characters based on the Unicode Standard repertoire as
   shown in the above image.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise -->
# Configuring the output component and executing the Job

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileOutputExcel component
   to display the Basic settings view and define
   the component properties.
2. Set the destination file name as well as the sheet name and then select the
   Define all columns auto size check box.
3. Save your Job and press F6 to execute
   it.

   The tTransliterate component encodes input
   data to readable characters based on the repertoire of the Unicode
   Standard.
4. Right-click the output component and select Data
   Viewer to display the transliterated data.

   All names written in characters from diverse languages have been phonetically
   converted to a standard set of characters based on the Universal Coded Character
   Set, UCS. For example, the names in the first and second rows in the below image
   have been changed to *Ragnarr,Lodbrok* and to
   *Routse,Anna* respectively.

   For further information about
   Unicode and Unicode Standards, check [Unicode](https://en.wikipedia.org/wiki/Unicode) and [Unicode
   Standard](http://unicode.org/standard/standard.html).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tTransliterate and
   tFileOutputExcel.
2. Connect the three components together using the Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/text-standardization/ttransliterate-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-transliterating-data-standard-component-enterprise -->
# Transliterating data

Last updated: 9/30/2026

## Procedure

1. Double-click tTransliterate to display the
   Basic settings view and define the component
   properties.
2. If required, click Sync columns to retrieve
   the schema defined in the input component.

   In this example, only the first two columns are processed. You can click the
   Edit schema button to open the schema dialog
   box and see the input and output schemas.
3. In the Transliteration table of the component
   basic settings view, select the check boxes next to the columns you want to
   convert to standard characters.
