<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow · versión 8.0 -->
# tStandardizeRow

Last updated: 9/30/2026

Normalizes the incoming data in a separate XML or JSON data flow
to separate or standardize the rule-compliant data from the non-compliant
data.

tStandardizeRow tokenizes the data flow
it has received from the preceding component and applies user-defined parser rules to
analyze the data. Based on this analysis, this component normalizes and writes analyzed
data in a separate data flow and tags them using the user-defined rule names. It does
not make any changes on your raw data.

The standardization option adds a supplementary column to
the output flow where the normalized data are then standardized.

The Java library ANTLR is used to parse and tokenize the
incoming data. For further information about ANTLR, see the site

<http://www.antlr.org/>

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tStandardizeRow Standard properties](/talend/en-US/components/8.0/standardization/tstandardizerow-standard-properties)
* [tStandardizeRow properties for Apache Spark Batch](/talend/en-US/components/8.0/standardization/tstandardizerow-properties-for-apache-spark-batch)
* [tStandardizeRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/standardization/tstandardizerow-properties-for-apache-spark-streaming)
* [tStandardizeRow properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/standardization/tstandardizerow-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Extracting exact match by using Index rules](tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-extracting-exact-match-by-using-index-rules-standard-component-enterprise-in-this)
* [Normalizing data using rules of basic types](tstandardizerow-tlogrow-tfilterrow-textractxmlfield-normalizing-data-using-rules-of-basic-types-standard-component-enterprise-in-this)
* [Standardizing addresses from unstructured data](tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-standardizing-addresses-from-unstructured-data-standard-component-enterprise-in-this)
* [Using two parsing levels to extract information from unstructured data](tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-using-two-parsing-levels-to-extract-information-from-unstructured-data-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-properties-for-apache-spark-batch -->
# tStandardizeRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tStandardizeRow running
in the Spark Batch Job framework.

The Spark Batch
tStandardizeRow component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Column to parse | Select the column to be parsed from the received data flow |
| Standardize this field | Select this check box to standardize the rule-compliant data identified, that is, to replace the duplicates of the identified data with the corresponding standardized data from a given index.  For further information about this index providing standardized data, see [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput).  Every time you select or clear this check box, the schema of this component is changed automatically, so in a given Job, you need to click the activated Sync columns button to fix the inconsistencies in the schema. |
| Generate analyzer code as routine | Click this button to enable the data parser of Talend Studio to recognize the rules defined in the Conversion rules table.  In a given Job, when a rule is created, this operation is required for the execution of this rule, while if it is on an existing rule that you have modified, this operation is required only when the modified rule is of type Enumeration, Format or Combination. For further information about all of the rule types, see [Rule types](/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-rule-types-standard-component-enterprise-two). |
| and | Click the import or export button to exchange a given standardization rule set with the DQ Repository.  - When you click the export button, Talend Studio is switched to the Profiling perspective and the Parser rule Settings view is opened on the workspace with the relative contents filled automatically. Then if need be, you can edit the exported rule set and save it to the Libraries > Rules > Parser folder in the DQ Repository tree view.  - When you click the import button, a import wizard is opened to help you import the standardization rule of interest.  For further information, see [Setting and managing parser rules](/talend/r/en-US/8.0/studio-user-guide/setting-and-managing-parser-rules). |
| Conversion rules | Define the rules you need to apply as the following:  - In the Name column, type in a name of the rule you want to use. This name is used as the XML tag or the JSON attribute name and the token name to label the incoming data identified by this rule.  - In the Type column, select the type of the rule you need to apply. For further information about available rule types, see [Rule types](/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-rule-types-standard-component-enterprise-two).  - In the Value column, type in the syntax of the rule.  - In the Search mode column, select a search mode from the list. The search modes can be used only with the Index rule type. For further information about available search modes, see [Search modes for Index rules](/talend/en-US/components/8.0/standardization/search-modes-for-index-rules).  - When you select the Index rule type, set the path as follows:  * In local mode:   + Apache Spark 3.1 and earlier: prefix://file     path or file:///file     path.   + Apache Spark 3.2 and later: file:///file path. * In Standalone and Yarn modes: prefix://file path. * If the index is on a cluster: hdfs://hdpnameservice1/file path.  A test view is provided to help you create the parser rules of interest. For further information, see [Setting and managing parser rules](/talend/r/en-US/8.0/studio-user-guide/setting-and-managing-parser-rules). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced options for INDEX rules | - Search UNDEFINED fields: select this check box if you want the component to search for undefined tokens in the index run results.  - Word distance for partial match (available for the *Match partial* mode): set the maximum number of words allowed to come inside a sequence of words that may be found in the index, default value is *1*.  - Max edits for fuzzy match (Based on the Levenshtein algorithm and available for fuzzy modes): select an edit distance,*1* or *2*, from the list. Any terms within the edit distance from the input data are matched. With a max edit distance *2*, for example, you can have up to two insertions, deletions, or substitutions. The score for each match is based on the edit distance of that term.  Fuzzy match gains much in performance with Max edits for fuzzy match.  Information noteNote: Jobs migrated in Talend Studio from older releases run correctly, but results might be slightly different because Max edits for fuzzy match is now used in place of Minimum similarity for fuzzy match. |
| Output format | -XML: this option is selected by default. It outputs normalized data in XML format.  -JSON: select this option to output normalized data in JSON format. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Connections | Outgoing links (from this component to another):  Row: Main; Reject    Incoming links (from one component to this one):  Row: Main; Reject    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-properties-for-apache-spark-structured-streaming -->
# tStandardizeRow properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tStandardizeRow running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tStandardizeRow component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Column to parse | Select the column to be parsed from the received data flow |
| Standardize this field | Select this check box to standardize the rule-compliant data identified, that is, to replace the duplicates of the identified data with the corresponding standardized data from a given index.  For further information about this index providing standardized data, see [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput).  Every time you select or clear this check box, the schema of this component is changed automatically, so in a given Job, you need to click the activated Sync columns button to fix the inconsistencies in the schema. |
| Generate analyzer code as routine | Click this button to enable the data parser of Talend Studio to recognize the rules defined in the Conversion rules table.  In a given Job, when a rule is created, this operation is required for the execution of this rule, while if it is on an existing rule that you have modified, this operation is required only when the modified rule is of type Enumeration, Format or Combination. For further information about all of the rule types, see [Rule types](/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-rule-types-standard-component-enterprise-two). |
| and | Click the import or export button to exchange a given standardization rule set with the DQ Repository.  - When you click the export button, Talend Studio is switched to the Profiling perspective and the Parser rule Settings view is opened on the workspace with the relative contents filled automatically. Then if need be, you can edit the exported rule set and save it to the Libraries > Rules > Parser folder in the DQ Repository tree view.  - When you click the import button, a import wizard is opened to help you import the standardization rule of interest.  For further information, see [Setting and managing parser rules](/talend/r/en-US/8.0/studio-user-guide/setting-and-managing-parser-rules). |
| Conversion rules | Define the rules you need to apply as the following:  - In the Name column, type in a name of the rule you want to use. This name is used as the XML tag or the JSON attribute name and the token name to label the incoming data identified by this rule.  - In the Type column, select the type of the rule you need to apply. For further information about available rule types, see [Rule types](/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-rule-types-standard-component-enterprise-two).  - In the Value column, type in the syntax of the rule.  - In the Search mode column, select a search mode from the list. The search modes can be used only with the Index rule type. For further information about available search modes, see [Search modes for Index rules](/talend/en-US/components/8.0/standardization/search-modes-for-index-rules).  - When you select the Index rule type, set the path as follows:  * In local mode:   + Apache Spark 3.1 and earlier: prefix://file     path or file:///file     path.   + Apache Spark 3.2 and later: file:///file path. * In Standalone and Yarn modes: prefix://file path. * If the index is on a cluster: hdfs://hdpnameservice1/file path.  A test view is provided to help you create the parser rules of interest. For further information, see [Setting and managing parser rules](/talend/r/en-US/8.0/studio-user-guide/setting-and-managing-parser-rules). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-standard-properties -->
# tStandardizeRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tStandardizeRow running
in the Standard Job framework.

The Standard
tStandardizeRow component belongs to the Data Quality
family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Column to parse | Select the column to be parsed from the received data flow |
| Standardize this field | Select this check box to standardize the rule-compliant data identified, that is, to replace the duplicates of the identified data with the corresponding standardized data from a given index.  For further information about this index providing standardized data, see [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput).  Every time you select or clear this check box, the schema of this component is changed automatically, so in a given Job, you need to click the activated Sync columns button to fix the inconsistencies in the schema. |
| Generate parser code in Routines | Click this button to enable the data parser of Talend Studio to recognize the rules defined in the Conversion rules table.  In a given Job, when a rule is created, this operation is required for the execution of this rule, while if it is on an existing rule that you have modified, this operation is required only when the modified rule is of type Enumeration, Format or Combination. For further information about all of the rule types, see [Rule types](/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-rule-types-standard-component-enterprise-two). |
| and | Click the import or export button to exchange a given standardization rule set with the DQ Repository.  - When you click the export button, Talend Studio is switched to the Profiling perspective and the Parser rule Settings view is opened on the workspace with the relative contents filled automatically. Then if need be, you can edit the exported rule set and save it to the Libraries > Rules > Parser folder in the DQ Repository tree view.  - When you click the import button, a import wizard is opened to help you import the standardization rule of interest.  For further information, see [Setting and managing parser rules](/talend/r/en-US/8.0/studio-user-guide/setting-and-managing-parser-rules). |
| Conversion rules | Define the rules you need to apply as the following:  - In the Name column, type in a name of the rule you want to use. This name is used as the XML tag or the JSON attribute name and the token name to label the incoming data identified by this rule.  - In the Type column, select the type of the rule you need to apply. For further information about available rule types, see [Rule types](/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-rule-types-standard-component-enterprise-two).  - In the Value column, type in the syntax of the rule.  - In the Search mode column, select a search mode from the list. The search modes can be used only with the Index rule type. For further information about available search modes, see [Search modes for Index rules](/talend/en-US/components/8.0/standardization/search-modes-for-index-rules).  A test view is provided to help you create the parser rules of interest. For further information, see [Setting and managing parser rules](/talend/r/en-US/8.0/studio-user-guide/setting-and-managing-parser-rules). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced options for INDEX rules | - Search UNDEFINED fields: select this check box if you want the component to search for undefined tokens in the index run results.  - Word distance for partial match (available for the *Match partial* mode): set the maximum number of words allowed to come inside a sequence of words that may be found in the index, default value is *1*.  - Max edits for fuzzy match (Based on the Levenshtein algorithm and available for fuzzy modes): select an edit distance,*1* or *2*, from the list. Any terms within the edit distance from the input data are matched. With a max edit distance *2*, for example, you can have up to two insertions, deletions or substitutions. The score for each match is based on the edit distance of that term.  Fuzzy match gains much in performance with Max edits for fuzzy match.  Information noteNote: Jobs migrated in Talend Studio from older releases run correctly, but results might be slightly different because Max edits for fuzzy match is now used in place of Minimum similarity for fuzzy match. |
| Output format | -XML: this option is selected by default. It outputs normalized data in XML format.  -JSON: select this option to output normalized data in JSON format.  -Pretty print: this option is selected by default. It allows you to have the output on several rows. If you clear this check box, you will have the output in one row. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediary step. It requires an input flow as well as an output.  This component generates Java code in the Routines node of the Repository tree view. This code implements the grammar defined in rules. It is automatically compiled to be used by the component.  When you modify /add/delete a rule, the code must be generated again, so that the Job takes the modifications into account and then becomes runnable.  To generate it, click the Generate parser code in Routines button. |
| Connections | Outgoing links (from this component to another):  Row: Main; Reject  Trigger: Run if; On Component Ok; On Component Error.    Incoming links (from one component to this one):  Row: Main; Reject    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-standardizing-addresses-from-unstructured-data-standard-component-enterprise-in-this -->
# Standardizing addresses from unstructured data

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

In this scenario, six components are used to standardize addresses from
unstructured input data copied from a Website, by matching the data with the data contained
in an index previously generated by a Job.

For more information about index creation, see [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput).

Drop the following components from the Palette to the design workspace.

* tFixedFlowInput: this component holds the
  unstructured data from which the addresses are extracted.
* tStandardizeRow: this component defines the
  address rules and generates the addresses in XML format with the defined tags. This
  is the process of normalizing and standardizing the initially unstructured data.
* tFilterColumns: this component filters the
  standardized addresses.
* tExtractXMLField: this component extracts the
  attributes from the *Address* node of the XML tree in order to
  output every address item in formatted columns.
* two tLogRow: these components
  are used to display the output data. The first tLogRow returns the errors, if any. The second tLogRow displays the result in the console.

Before starting up to replicate this scenario, you have to retrieve the
content of an index in order to match the unstructured data with the index data. The
content of the index reads as follows:

On the left side are held Paris street names and on the right side are held
the synonyms used in the data. The data will be used as references to standardize the
address data collected from a website.

To replicate this scenario, proceed as the following sections
illustrate.

### In this section

* [Preparing the unstructured data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-preparing-unstructured-data-standard-component-enterprise-to-do)
* [Configuring the process of standardizing the unstructured data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-configuring-process-of-standardizing-unstructured-data-standard-component-enterprise-to-do)
* [Configuring the process of filtering and extracting the data of interest](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-configuring-process-of-filtering-and-extracting-data-of-interest-standard-component-enterprise-to-do)
* [Executing the Job](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-executing-job-standard-component-enterprise-before)

**Related concepts**  

* [tStandardizeRow](tstandardizerow "Normalizes the incoming data in a separate XML or JSON data flow to separate or standardize the rule-compliant data from the non-compliant data.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tExtractXMLField](/talend/en-US/components/8.0/processing/textractxmlfield)
* [tFilterColumns](/talend/en-US/components/8.0/processing/tfiltercolumns)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-normalizing-data-using-rules-of-basic-types-standard-component-enterprise-in-this -->
# Normalizing data using rules of basic types

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

In this scenario, two steps are performed to:

1. normalize the incoming data (separate the compliant data from the
   non-compliant data) and,
2. extract the data of interests and display it.

Before replicating these two steps, we need to analyze the source data in order to
figure out what rules need to be composed. For this scenario, the source data is stored
in a *.csv* file called *partsmaster*.

There are totally 59 rows of raw data, but some of them are not shown in our
capture.

Through observation, you can expect that the third row will not be recognized as it
contains Oriental characters. Furthermore, you can figure out that:

* the *SKU* data contains 34-9923, XC-3211 and pb710125 and
  so on. So the rule used to parse the *SKU* data could
  be:

  | Name | Type | Value |
  | --- | --- | --- |
  | "SKU" | "Format" | "(DIGIT DIGIT|LETTER LETTER) '-'? DIGIT DIGIT DIGIT DIGIT (DIGIT DIGIT?)? " |

* for the *Size* data, the correct format is the
  multiplication of two or three lengths plus the length units. Therefore, the
  rules used to parse the *Size* data could be:

  | Name | Type | Value |
  | --- | --- | --- |
  | "LengthUnit" | "Enumeration" | " 'm' | '\'' | 'inch' | 'inches' | '\"'" |
  | "BY" | "Enumeration" | "'X' | 'x' | 'by' " |
  | "Length" | "Format" | "(INT | FRACTION | DECIMAL) WHITESPACE\* LengthUnit " |
  | "Size" | "Combination" | "Length BY Length BY Length" |
  | "Size" | "Combination" | "Length BY Length" |

Two Combination rules use the same name, in which
case, they will be executed in top-down order as is presented in this table.

* for the *Weight* data, the correct format is the weight
  plus the weight unit. Therefore, the rules used to parse the
  *Weight* data are:

  | Name | Type | Value |
  | --- | --- | --- |
  | "WeightUnit" | "Enumeration" | " 'lb' | 'lbs' | 'pounds' | 'Kg' | 'pinds'" |
  | "Weight" | "Format" | "(INT | FRACTION | DECIMAL) WHITESPACE\* WeightUnit " |

Now, you can begin to replicate the two steps of this scenario.

### In this section

* [Separating the compliant data and the non-compliant data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-separating-compliant-data-and-non-compliant-data-standard-component-enterprise-in-this)
* [Extracting data of interest from the normalized XML data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-extracting-data-of-interest-from-normalized-xml-data-standard-component-enterprise-this)

**Related concepts**  

* [tStandardizeRow](tstandardizerow "Normalizes the incoming data in a separate XML or JSON data flow to separate or standardize the rule-compliant data from the non-compliant data.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tExtractXMLField](/talend/en-US/components/8.0/processing/textractxmlfield)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFilterRow](/talend/en-US/components/8.0/processing/tfilterrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-using-two-parsing-levels-to-extract-information-from-unstructured-data-standard-component-enterprise-this -->
# Using two parsing levels to extract information from unstructured data

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes how to build a set of rules to extract some information from
unstructured data. It explains how to use a basic ANTLR rule to tokenize data then how
to use an advanced rule to check each token created by ANTLR against a regular
expression.

This scenario uses:

* a  tFixedFlowInput component to create the
  unstructured data strings.
* a  tStandardizeRow component to define the
  rules necessary to extract the liquid amounts from the data strings.
* a tLogRow component to display the output
  data.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-setting-up-job-standard-component-enterprise-drop)
* [Creating the unstructured data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-creating-unstructured-data-standard-component-enterprise)
* [Creating the parsing rules](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-creating-parsing-rules-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-executing-job-standard-component-enterprise-save)

**Related concepts**  

* [tStandardizeRow](tstandardizerow "Normalizes the incoming data in a separate XML or JSON data flow to separate or standardize the rule-compliant data from the non-compliant data.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-extracting-exact-match-by-using-index-rules-standard-component-enterprise-in-this -->
# Extracting exact match by using Index rules

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

In this scenario, you will standardize some long descriptions of customer
products by matching the input flow with the data contained in an index. This scenario
explains how to use Index rules to tokenize product
data and then check each token against an index to extract exact match.

For this scenario, you must first create an index by using a Job with the
tSynonymOutput component. You need to create
indexes for the brand, range, color and unit of the customer products. Use the tSynonymOutput component to generate the indexes and feed
them with entries and synonyms. The below capture shows an example Job:

Below is a sample of the generated indexes for this scenario:

Each of the generated indexes has strings (sequences of words) in one column
and their corresponding synonyms in the second column. These strings are used as a
reference data against which the product data, generated by 
tFixedFlowInput, will be matched. For further information about index
creation, see [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput).

In this scenario, the generated indexes are defined as context variable. For
further information about context variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-setting-up-job-standard-component-enterprise-drop)
* [Generating unstructured data](/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-generating-unstructured-data-standard-component-enterprise)
* [Defining parsing rules to standardize data](/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-defining-parsing-rules-to-standardize-data-standard-component-enterprise)
* [Extracting exact match](/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-extracting-exact-match-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-executing-job-standard-component-enterprise-save)

**Related concepts**  

* [tStandardizeRow](tstandardizerow "Normalizes the incoming data in a separate XML or JSON data flow to separate or standardize the rule-compliant data from the non-compliant data.")

**Related information**  

* [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tExtractXMLField](/talend/en-US/components/8.0/processing/textractxmlfield)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-rule-types-standard-component-enterprise-two -->
# Rule types

Last updated: 9/30/2026

Two groups of rule types are provided: the basic rule types
and the advanced rule types.

* Basic rule types: Enumeration, Format and Combination. Rules of these types are composed
  with some given ANTLR symbols.
* Advanced rule types: Regex, Index and Shape. Rules of these types match the tokenized
  data and standardize them when needed.

The advanced rule types are always executed after the ANTLR specific rules regardless
of rule order. For further information about basic and advanced rules, see [Different rule types for different parsing levels](/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-different-rule-types-for-different-parsing-levels-standard-component-enterprise-the) and
[Using two parsing levels to extract information from unstructured
data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-using-two-parsing-levels-to-extract-information-from-unstructured-data-standard-component-enterprise-this).

To create the rules of any type, 
Talend
 provides the pre-defined and case-sensitive elements (ANTLR tokens) as
follows for defining the composition of a string to be matched:

* INT: integer;
* WORD: word;
* WORD+: literals of several words;
* CAPWORD: capitalized word;
* DECIMAL: decimal float;
* FRACTION: fraction float;
* CURRENCY: currencies;
* ROMAN\_NUMERAL: Roman numerals;
* ALPHANUM: combination of alphabetic and numeric
  characters;
* WHITESPACE: whitespace
* UNDEFINED: unexpected strings such as ASCII
  codes that any other token cannot recognize.

The following three tables successively present detailed information about the basic
types, the advanced types and the ANTLR symbols used by the basic rule types. These
three tables help you to complete the Conversion rules
table in the Basic settings of this component.

For basic rule types:

| Basic Rule Type | Usage | Example | Conditions of rule composition |
| --- | --- | --- | --- |
| Enumeration | A rule of this type provides a list of possible matches. | *RuleName*: LengthUnit *RuleValue:* " 'inch' | 'cm' " | Each option must be put in a pair of single quotation marks unless this option is a pre-defined element. Defined options must be separated by the | symbol. |
| Format (Rule name starts with upper case) | A rule of this type uses the pre-defined elements along with any of user-defined Enumeration, Format or Combination rules to define the composition of a string. | *RuleName*: Length *RuleValue*: "DECIMAL WHITESPACE LengthUnit"  This rule means that a whitespace between decimal and lengthunit is required, so it matches strings like, *1.4 cm* but does not match a string like 1.4cm. To match both of these cases, you need to define this rule as, for example, "DECIMAL WHITESPACE\* LengthUnit" .  LengthUnit is an Enumeration rule defining " 'inch' | 'cm' ". | When the name of a Format rule starts with upper case, this rule requires the exact matching result. It means that you need to define exactly any single element of a string, even a whitespace. |
| Format (Rule name starts with lower case) | A rule of this type is almost the same as a Format rule starting its name with upper case. The difference is that the Format rule with lower-case initial does not require exact match. | *RuleName*: length *RuleValue*: "DECIMAL LengthUnit"  The rule matches strings like *1.4 cm* or *1.4cm* etc. where the Decimal is one of the pre-defined element types and LengthUnit is an Enumeration rule defining " 'inch' | 'cm' ". | N/A |
| Combination | A rule of this type is used when you need to create several rules of the same name. | *RuleName*: Size (or size) *RuleValue*: "length BY length"  The rule matches strings like *1.4 cm by 1.4 cm*, where length is a Format rule (starting with lower case) and BY is an Enumeration rule defining " 'By' | 'by' | 'x' | 'X' ". | Literal texts or characters are not accepted as a part of the rule value. When the literal texts or characters are needed, you must create an Enumeration rule to define these texts or characters and then use this Enumeration rule instead. When several Combination rules use the identical rule name, they are executed in top-down order in the Conversion rules table of the Basic settings of tStandardizeRow, so arrange them properly in order to obtain the best result. For an example, see the following scenario. |

Information noteWarning: Any characters or string literals, if
accepted by a rule type, must be put in single quotation marks when used, otherwise they
will be treated as ANTLR grammar symbols or variables and generate errors or unexpected
results at runtime.

For advanced rule types:

| Advanced Rule Type | Usage | Example | Conditions |
| --- | --- | --- | --- |
| Regex | A rule of this type uses regular expressions to match the incoming data tokenized by ANTLR. | *RuleName*: ZipCode *RuleValue*: "\\d{5}"  The rule matches strings like *"92150"* | Regular expressions must be Java compliant. |
| Index | A rule of this type uses a synonym index as reference to search for the matched incoming data. For further information about available synonym indexes, see [Data synonym dictionaries](/talend/r/en-US/8.0/studio-user-guide/overview-of-available-indexes). | A scenario is available in [Standardizing addresses from unstructured data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-standardizing-addresses-from-unstructured-data-standard-component-enterprise-in-this). | On Windows, the backslashes \ need to be doubled or replaced by slashes / if the path is copied from the file system. If you run the Job using Spark Local mode or if you run the Job locally, the path to index folder must start with file:///, even. If the index is stored in HDFS, the path to the index folder must start with `hdfs://`.  When processing a record, a given Index rule matches up only the first string identified as matchable.  In a Talend Map/Reduce Job, you need to compress each synonym index to be used as a zip file. |
| Shape | A rule of this type uses pre-defined elements along with the established Regex or Index rules or both to match the incoming data. | *RuleName*: Address *RuleValue*: "<INT><WORD><StreetType>"  This rule matches the addresses like *12 main street*, where *INT* and *WORD* are pre-defined tokens (rule elements) and *StreetType* is an Index rule which you define along with this example rule in the Basic settings view of this component.  For further information about the Shape rule type, see [Standardizing addresses from unstructured data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-standardizing-addresses-from-unstructured-data-standard-component-enterprise-in-this). | Only the contents put in < > are recognizable. In the other cases, the contents are considered as error or are omitted. |

For the given ANTLR symbols:

| Symbols | Description |
| --- | --- |
| | | alternative |
| 's' | char or string literal |
| + | 1 or more |
| \* | 0 or more |
| ? | optional or semantic predicate |
| ~ | match not |

For more information about ANTLR symbols, see: <https://theantlrguy.atlassian.net/wiki/display/ANTLR3/ANTLR+Cheat+Sheet>.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-configuring-process-of-filtering-and-extracting-data-of-interest-standard-component-enterprise-to-do -->
# Configuring the process of filtering and extracting the data of interest

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. In the design workspace, connect tStandardizeRow to tFilterColumns with a Row
   > Main link.
2. In the Basic settings view of tFilterColumns, click the [...] button next to the Edit
   schema field to open the schema editor.
3. Click on the *STANDARDIZED\_FIELD* column, click the
   first arrow to filter this column, and then click OK to close the editor and validate the changes.
4. In the design workspace, connect tFilterColumns to tExtractXMLField with a Row
   > Main link.
5. Double-click the tExtractXMLField
   component to display its Basic settings
   view.
6. Click the [...] button next to the
   Edit schema field to open the schema
   editor, add four columns and name them respectively
   *number*, *street*,
   *zip* and *city*, and then click
   OK to validate and close the
   editor.
7. In the XML field field, check that the
   *STANDARDIZED\_FIELD* column is selected.

   The content of the *STANDARDIZED\_FIELD* column is an
   XML field with a <record> tag as root. Under this tag,
   the structure defined by the rules configured in the tStandardizeRow component allows to extract each item of the
   address, as you can see in the following capture.
8. In the Loop XPath query field, type in
   *"/record/Address"*.
9. In the Mapping table, in the XPath query field, enter
   *"INT"* for the *number* column,
   *"StreetName"* for the *street*
   column, *"Zip"* for the *zip* column
   and *"City"* for the *city*
   column.

## Results

Then you can prepare to execute the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-configuring-process-of-standardizing-unstructured-data-standard-component-enterprise-to-do -->
# Configuring the process of standardizing the unstructured data

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. Connect the tFixedFlowInput component to
   the tStandardizeRow component with a
   Row > Main link.
2. Double-click the tStandardizeRow
   component to display its Basic settings
   view.

   The advanced rule types are always executed after the ANTLR specific rules
   regardless of rule order.
3. In the Column to parse list, select
   input.
4. Select the Standardize this field check
   box.
5. In the Conversion rules
   table, click six times on the [+] button
   to add six columns. Name them and configure them as shown in the capture. For
   "StreetName" rule:
   1. Select the Index type in the Type field.
   2. Enter the path to your index in the Value field.

      Set the file path as follows:
      * In local mode:
        + Apache Spark 3.1 and earlier: prefix://file
          path or file:///file path.
        + Apache Spark 3.2 and later: file:///file
          path.
      * In Standalone and Yarn modes: prefix://file
        path.
      * If the index is on a cluster: hdfs://hdpnameservice1/file
        path.
   3. Select Match exact as the search mode from the
      Search mode list.

      By using the Match exact mode, you will extract
      from the input flow only the strings that exactly match the street name
      indexes. For further information about available search modes, see [Search modes for Index rules](/talend/en-US/components/8.0/standardization/search-modes-for-index-rules)

   Then the other rules are:

   | Name | Type | Value |
   | --- | --- | --- |
   | "Zip" | Format | " DIGIT DIGIT DIGIT DIGIT DIGIT " |
   | "City" | Enumeration | " 'Paris' | 'Paris' | 'PARIS' | 'Bagnolet' " |
   | "SpecialStreetNumber" | Format | " (INT ('bis'|'ter')) | ( INT '-' INT) " |
   | "INT" | Shape | "<SpecialStreetNumber>" |
   | "Address" | Shape | " <INT> <StreetName> <Zip> <City> " |

   As advanced rule types are always executed after the ANTLR specific
   rules, the basic rules "Zip",
   "City" and "SpecialStreetNumber"
   are executed first followed by "INT" and
   "Address", the advanced rules.
6. Click the Generate parser code in
   Routines button in order to generate the code in the
   Routines.

   If you do not click on this button, the Job will not be executed.
7. In the Advanced settings view, leave the
   options selected by default in the Output
   format area as they are.

   The Max edits for fuzzy
   match is set to 1 by default.
8. In the design workspace, right-click the tStandardizeRow component to connect it to the tLogRow below with a Row > Reject link.
9. Double-click the tLogRow component linked
   to the tStandardizeRow component to display
   its Basic settings view.
10. In the Mode area, select the Table (print values in cells of a table)
    option.

## Results

Then continue to configure the process of filtering and extracting the data of
interest.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-executing-job-standard-component-enterprise-before -->
# Executing the Job

Last updated: 9/30/2026

## About this task

Before executing the Job, you need to add the tLogRow component to display the execution result.

To do this, perform the following operations:

## Procedure

1. In the design workspace, connect tExtractXMLField to the second tLogRow with a Row >
   Main link.
2. Double-click the tLogRow component to
   open its Basic settings view.
3. In the Schema list, select Built-In.
4. Click the [...] button next to the
   Edit schema field and check that the
   input and the output schemas in the tLogRow
   are synchronized.

   If not, click on the Sync columns
   button.
5. In the Mode area, select the Table (print values in cells of a table) option.

## Results

Press F6 to execute the Job.

The second tLogRow displays the normalized and
standardized addresses in the console according to the index.

For example, you can see that the Champs Elysées address has been selected and
formatted, and only input street names that exactly match an index string are
extracted.

The first tLogRow does not return anything in
this scenario because no error has been generated.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfiltercolumns-tfixedflowinput-preparing-unstructured-data-standard-component-enterprise-to-do -->
# Preparing the unstructured data

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. Double-click the tFixedFlowInput
   component to display its Basic settings
   view.
2. Click the [...] button to open the
   Schema dialog box, click the
   [+] button to add a column, and name it
   *input*. Then, click OK to validate and close the editor.
3. In the Mode area, select Use Inline Content (delimited file).
4. In the Content field, paste the data
   copied from the Website. This data is unstructured.

## Results

Then you can continue to configure the standardization process.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-extracting-data-of-interest-from-normalized-xml-data-standard-component-enterprise-this -->
# Extracting data of interest from the normalized XML data

Last updated: 9/30/2026

This section presents the second step of this scenario. Four components are added
to receive the normalized XML data in place of the tLogRow component which was set for this action in the first step.
The four components are:

* tExtractXMLField: this component reads
  an input XML field and extracts desired data;
* tFilterRow: this component filters input
  rows by setting conditions on the selected columns;
* tLogRow (two times): the two components
  receive and display respectively the valid or invalid data against
  conditions set in tFilterRow.

To replicate the second step, proceed as the following sections illustrate.

### In this section

* [Dropping and linking the additional components](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-dropping-and-linking-additional-components-standard-component-enterprise-to-do)
* [Configuring the process of extracting the XML fields of interest](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-configuring-process-of-extracting-xml-fields-of-interest-standard-component-enterprise-to-do)
* [Configuring the process of filtering the rows of interest](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-configuring-process-of-filtering-rows-of-interest-standard-component-enterprise-to-do)
* [Executing the Job](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-executing-job-standard-component-enterprise-press-f6)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-separating-compliant-data-and-non-compliant-data-standard-component-enterprise-in-this -->
# Separating the compliant data and the non-compliant data

Last updated: 9/30/2026

In this first step, four components are used. They are

* tFileInputDelimited (*partsmaster*): this component loads and outputs the source data to the component
  that follows.
* tStandardizeRow: this component normalizes the
  incoming data and rejects the exception data that it cannot recognize.
* tLogRow: this component is used two times to
  display respectively the exception data and the output XML data.

To replicate this step, proceed as the following sections illustrate.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-dropping-and-linking-components-standard-component-enterprise-to)
* [Configuring the process of normalizing rows](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-configuring-process-of-normalizing-rows-standard-component-enterprise-to-do)
* [Executing the normalization Job](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-executing-normalization-job-standard-component-enterprise-press-f6)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-creating-parsing-rules-standard-component-enterprise -->
# Creating the parsing rules

Last updated: 9/30/2026

## Procedure

1. Double-click the tStandardizeRow
   component to display its Basic settings
   view.
2. From the Column to parse list, select
   product.
3. In the Conversion rules table, define a
   basic rule and an advanced rule as the following:
   * Click twice on the [+] button to
     add two columns. Name the first as *"Amount"* and
     the second as *"LiquidAmount"*.
   * Select *Format* as the type for
     the basic rule, and define it to read "INT WHITESPACE\*
     WORD".
   * Select *RegExp* as the type for
     the advanced rule, and define it to read
     "\\d+\\s\*(L|ML)\\b".

     The advanced rule will be executed after the basic ANTLR rule. The
     *"Amount"* rule will tokenize the amounts in
     the three strings, it matches any word with a numeric in front of
     it. Then the *RegExp* rule will
     check each token created by ANTLR against a regular
     expression.
4. Click the Generate parser code in
   Routines button in order to generate the code under the
   Routines folder in the DQ Repository tree view of the 
   Profiling
    perspective.

   This step is mandatory, otherwise the Job will not be executed.
5. In the Advanced settings view, leave the
   options selected by default in the Output
   format area as they are.

   The Max edits for fuzzy match is set to
   *1* by default.
6. Double-click the tLogRow component and
   select the Table (print values in cells of a
   table) option in the Mode
   area.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-creating-unstructured-data-standard-component-enterprise -->
# Creating the unstructured data

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowInput
   component to display its Basic settings
   view.
2. Click the [...] button to open the
   Schema dialog box, click the
   [+] button to add a column, name the
   column *product* and finally click
   OK to validate and close the
   box.
3. In the Mode area, select Use Inline Content (delimited file).
4. In the Content field, enter the following
   three strings:
   3M PROJECT LAMP 7 LUMENS 32ML
   A 5 LUMINES 5 LOW VANILLA 5L 5LIGHT 5 L DULUX L
   54MLP FAC 32 ML


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-executing-job-standard-component-enterprise-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Save your Job and press F6 to execute
it.

The liquid amount has been extracted from the unstructured data by using a
basic ANTLR rule that has tokenized amounts followed by an advanced rule
that has checked each token created by ANTLR against the regular
expression.

Each instance of the XML data is written on a separate row because the
Pretty print check box is selected in
the Advanced settings of the tStandardizeRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: 
   tFixedFlowInput, 
   tStandardizeRow and tLogRow.
2. Connect the three components together using the Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-defining-parsing-rules-to-standardize-data-standard-component-enterprise -->
# Defining parsing rules to standardize data

Last updated: 9/30/2026

## Procedure

1. Double-click tStandardizeRow to display
   the component Basic settings view.

   This component helps you to define the rules necessary to standardize the
   unstructured input flow and generates the brand, range, color and unit in
   XML format.
2. From the Column to parse
   list, select Long\_Description.
3. Select the Standardize this field check
   box.
4. Define your rules as the following:
   1. In the Conversion rules table, click on the
      [+] button to add the columns necessary to define
      the rules. 

      This scenario focuses on the rules of the type
      Index. For detail examples about the other
      rule types defined in the capture above, please refer to the other
      tStandardizeRow scenarios.
   2. Define three rules as Brand,
      Range and Color.
   3. From the Type list, select
      Index and fill in the
      Value field with the context variable of the
      indexes you generated.

      For further information about how to create and use context variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).
   4. From the Search mode list, select
      Match exact. Search modes are only applicable to
      the Index rules.

      Using the Match exact mode, you will extract from the
      input flow only the strings that exactly match the brand, range, and color
      index strings you generated with the tSynonymOutput
      component. For further information about available search modes, see [Search modes for Index rules](/talend/en-US/components/8.0/standardization/search-modes-for-index-rules)
5. Click the Generate parser code in
   Routines button in order to generate the code under the
   Routines folder in the DQ Repository tree view of the 
   Profiling
    perspective.

   This step is mandatory, otherwise the Job will not be executed.
6. In the Advanced settings view, leave the
   options selected by default in the Output
   format area as they are.

   The Max edits for fuzzy
   match is set to 1 by default.
7. Double-click tLogRow and define the
   component settings in the Basic settings
   view.
8. In the Mode area, select the Table (print values in cells of a table)
   option.

   This component displays the tokens from the input flow that could not be
   analysed and matched to any of the index strings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-executing-job-standard-component-enterprise-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Save your Job and press F6 to execute
   it.

   The tLogRow component
   displays on Talend Studio the
   data the Job can not analyze:

   The normalized and standardized data is written in the output excel
   file.
2. Right-click the tFileOutputExcel
   component and select Data viewer

   A preview of the standardized data is opened in Talend Studio.

   The *Brand*, *Range* and
   *Color* rules you defined have checked each token in
   the input flow against the index strings and only input strings that exactly
   match an index string are extracted. Take for example line 11, no color has
   been extracted from this record as the record does not have an exact match
   to any of the color index strings.

   Try and change in the tStandardizeRow
   basic settings the search mode for the *Color* rule to
   *Match any*, and then execute the Job.

   You can see that a color has now been extracted for the record on line 11.
   This record has one word, "EXTRA", that matches to the color index "Extra
   Deep Base" and that is enough according to the *Match
   any* search mode to consider that the record has a
   color.

   The different search modes available in the tStandardizeRow component allow you to standardize and
   output the data you expect.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-extracting-exact-match-standard-component-enterprise -->
# Extracting exact match

Last updated: 9/30/2026

## Procedure

1. Double-click tExtractXMLField to display
   the component  Basic settings view.
2. Click the [...] button next to the
   Edit schema field to open the schema
   editor, add four columns in the output flow and name them as
   *Brand*, *Range*,
   *Color* and *Amount*. Click
   OK to validate and close the
   editor.
3. In the XML field field, check that the
   STANDARDIZED\_FIELD column is
   selected.

   The content of the STANDARDIZED\_FIELD
   column is an XML field with a <record> tag as root. Under
   this tag, the structure defined by the rules configured in the tStandardizeRow component allows to extract items
   from the input flow.
4. In the Loop XPath query field, enter "/"
   to define the root as the loop node.
5. In XPath query field in the Mapping table, enter respectively
   *"record/Brand"*,
   *"record/Range"*
   *"record/Color"*
   and *"record/Measure"*.
6. Double-click tFileOutputExcel to display
   the component  Basic settings view.
7. Set the destination file name as well as the Sheet name and select the
   Include header check box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-generating-unstructured-data-standard-component-enterprise -->
# Generating unstructured data

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display
   the component Basic settings view.

   This component will generate the unstructured product data from
   which the brand, range, color, and unit are extracted.
2. Click the [...] button to open the
   Schema dialog box.
3. Click the [+] button and add two columns,
   name them as *Long\_Description* and
   *Supplier\_Product\_Code*. Click
   OK to close the dialog box.
4. In the Mode area, select Use Inline Content (delimited file).
5. In the Content field, enter the
   unstructured product data you want to standardize, for example as the
   following:HONEYWELL 7DAY SNGL CHNL TIMESWITCH C/W EX LARGE BACKLIT DISPLAY ST9100C1106|ST9100C1006||Data to be standardised||
   HONEYWELL AQUASTAT SINGLE IMMERSION T/STAT WITH CAPILLARY 70-140C|L6188B2018U||||
   HONEYWELL S PLAN ZONE VALVE CONTROL PACK TW6Z910C|TW6Z910C||||
   H/WELL ST6100S1001 24HR 1CH SERVIC TIMER|||||
   H/WELL Y603A1133 BOXED Y PLAN |||||
   HWEL V8600N2056 LOW VOLT COMBI VALVE |||||
   HWEL VR4700C4022 GAS VALVE |||||
   DULUX PAINTPOD 2M EXTENSION TUBE |6030950||||
   DULUX PAINTPOD REPLACEMENT ROLLER SLEEVE|6030948||||
   DULUX PAINTPOD EXTRA REACH HANDLE |6030951||||
   DULUX PAINTPOD REPLACEMENT EDGING BRUSH |6030952||||
   DT TRADE WEATHERSHIELD ULTIMATE OPAQUE BLACK 1L|5180583||||
   DT TRADE WEATHERSHIELD ULTIMATE OPAQUE BLACK 2.5L|5180652||||
   DT TRADE WEATHERSHIELD ULTIMATE OPAQUE BLACK 5L|5180744||||
   DT TRADE WEATHERSHIELD ULTIMATE OPAQUE EXTRA DEEP BASE 1L|5180584||||


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tsynonymoutput-tfileoutputexcel-textractxmlfield-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette to the design workspace: tFixedFlowInput, 
   tStandardizeRow, 
   tExtractXMLField and tFileOutputExcel.
2. Connect the components together using Main links.
3. Drop tLogRow to the Job and link
   tStandardizeRow to it using a Reject link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tstandardizerow-different-rule-types-for-different-parsing-levels-standard-component-enterprise-the -->
# Different rule types for different parsing levels

Last updated: 9/30/2026

The tStandardizeRow component uses basic rules based
on ANTLR grammar and advanced rules defined by 
Talend
 and not based on
ANTLR.

Sometimes, using ANTLR rules can not answer all your expectations when normalizing and
standardizing data. Suppose, for example, that you want to extract the liquid amount in
the following three records:

```
3M PROJECT LAMP 7 LUMENS 32ML
A 5 LUMINES 5 LOW VANILLA 5L 5LIGHT 5 L DULUX L
54MLP FAC 32 ML
```

You may start by defining a liquid unit and a liquid amount in basic parser rules as
the following:

If you test these rules in the Profiling perspective of Talend Studio, you can
see that these rules extract *7 L* from *7
LUMENS* and this is not what you expect. You do not want that the word *LUMENS* is split into two tokens.

The basic rules you have defined above are ANTLR lexer rules and lexer rules are used
for tokenizing the input string. ANTLR does not provide a word boundary symbol like the
\b used in regular expressions. You must then be careful when choosing
lexer rules because they define how the input strings will be split in tokens.

You can solve such a problem using two approaches:

The first approach is to define another basic rule that matches a word with a numeric
value in front of it, the *Amount* rule in this example:

This basic rule is a lexer rule, a
Format rule that starts with an uppercase. If you test this rule in the
Profiling perspective of Talend Studio, you can
see that non liquid amounts are matched by this rule and the *LiquidAmount* rule only matches the expected sequence of characters.

The second approach is to use an advanced rule like a regular expression and define a
word boundary with \b. You can use a lexer rule to tokenize amounts where
you match any word with a numeric in front of it. Then use a regular expression that
matches liquid amounts as the following: a digit optionally followed by space and
followed by L or ML and terminated by a word boundary.

Note that the regular expression will be applied on the tokens created by the basic
lexer rule.

You can not check the results of the advanced rule by testing the rule in
the Profiling perspective of Talend Studio as you do
with basic rules. The only means to see the results of advanced rules is by using them in a
Job. The results will look as the following:

```
3M PROJECT LAMP 7 LUMENS 32ML
<record>
	<Amount>3M</Amount> 
	<Amount>7 LUMENS</Amount>
	<LiquidAmount>32ML</LiquidAmount> 
	<UNMATCHED> 
		<CAPWORD>PROJECT</CAPWORD> 
		<CAPWORD>LAMP</CAPWORD> 
	</UNMATCHED> 
</record>
```

For a Job example about the use of the above rules, see [Using two parsing levels to extract information from unstructured
data](/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfixedflowinput-tfixedflowinput-using-two-parsing-levels-to-extract-information-from-unstructured-data-standard-component-enterprise-this).

Comparing these two approaches, the first one uses only ANTLR grammar and may be more
efficient than the second solution which requires a second parsing pass to check each
token against the regular expression. But regular expressions can help people
experienced in regular expressions to create more advanced rules that could hardly be
created using ANTLR only.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-configuring-process-of-extracting-xml-fields-of-interest-standard-component-enterprise-to-do -->
# Configuring the process of extracting the XML fields of interest

Last updated: 9/30/2026

## About this task

To do this, proceed as follows

## Procedure

1. Double-click tExtractXMLField to open
   its Component view.
2. Next to Edit schema, click the
   [...] button to open the schema editor.
3. On the left side of this editor, select the
   *SKU\_Description\_Size\_Weight* row.
4. Click the
   button to add this row to the right side of the
   editor.
5. On the right side of this editor, click the plus button on the bottom
   toolbar three times to add three rows.
6. Rename the three rows as *SKU*,
   *Size*, *Weight*, all of which
   are tags of the normalized XML data.
7. Click OK to validate this editing and
   accept the schema propagation prompted by the pop-up dialog box. Four
   rows are automatically filled in the Mapping table on the Component view.
8. In the XML field field of the
   Component view, select the desired
   XML field of the incoming data. In this example, it is
   *Normalized\_field*.
9. In the Loop XPath Query field, type
   in the name of the XML Tree root tag to replace the default value. In
   this example, type in "/record".
10. In the XPath query column of the
    Mapping table, type in the XML Tree
    tags corresponding to desired normalized data between quotation marks.
    In this example, they are "SKU", "Size",
    "Weight".


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-configuring-process-of-filtering-rows-of-interest-standard-component-enterprise-to-do -->
# Configuring the process of filtering the rows of interest

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. Double-click tFilterRow to open its
   Component view.
2. Under the Conditions table, click the
   plus button to add one row.
3. In the InputColumn column of this
   row, select *Size* from the drop-down list.
4. In the Function column, select
   Empty.
5. In the Operator column, select
   Not equal to.
6. In the Value column, type in the
   quotation marks "".

## Results

The condition is set up. The normalized data which contain no null in the
*Size* tag will be output while those which contain null
in this *Size* tag will be rejected.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-dropping-and-linking-additional-components-standard-component-enterprise-to-do -->
# Dropping and linking the additional components

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. On the design workspace, delete the tLogRow component that is connected to tStandardizeRow with Main row link.
2. From the Palette, drop tExtractXMLField, tFilterRow and two tLogRow components into the design workspace. In this
   scenario, the two tLogRow components
   are named respectively *ValidSize* and
   *InvalidSize*.

   For further information about how to rename a component, see
   [View tab](/talend/r/en-US/8.0/studio-user-guide/view-tab).
3. Connect tExtractXMLField to tFilterRow with Main link as you did in the first step to connect
   *partsmaster* to tStandardizeRow.
4. Do the same but with Filter link to
   connect tFilterRow to
   *ValidSize*.
5. Connect tFilterRow to
   *InvalidSize* with Reject link as you did in the first step to connect
   tSandardizeRow to
   *Exception*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-executing-job-standard-component-enterprise-press-f6 -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Press F6 to run this Job.

In the console of the Run view, you
can read the desired data selected from the normalized XML data
flow.

This Job lists the normalized data of interest in parallel with the
raw data.

You can read the data rejected by tFilterRow as well.

Information noteNote:

For reason of page space, all of the results are not
displayed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-configuring-process-of-normalizing-rows-standard-component-enterprise-to-do -->
# Configuring the process of normalizing rows

Last updated: 9/30/2026

## Procedure

1. Double-click tStandardizeRow to open
   its Component view.
2. In the Column to parse field, select
   *SKU\_Description\_Size\_Weight*. This is the only
   column that the incoming schema has.
3. Under the Conversion rules table,
   click the plus button eight times to add eight rows in this
   table.
4. To complete these rows, enter the rules you have figured out when
   analyzing the raw data at the beginning of this scenario.

   The two *Size* rules are executed in top-down
   order. In this example, this order allows this component to match firstly the sizes
   with three numbers and then those with two numbers. If you reverse this order, this
   component will match the first two numbers of all sizes before all and then treat the
   last number of the three-numbers sizes as unmatched.
5. Click the Generate parser code in
   routines button.
6. In the Advanced settings view, leave the
   options selected by default in the Output
   format area as they are.

   The Max edits for fuzzy match is set to
   *1* by default.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-dropping-and-linking-components-standard-component-enterprise-to -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

To replicate this step, proceed as follows:

## Procedure

1. Set up the file delimited schema for the *partsmaster.csv* file in the Repository
   of Talend Studio.
   For further information about how to set up a file delimited schema, see [Centralizing File Delimited metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-file-delimited-metadata).
2. Under the Metadata node of
   the Repository of Talend Studio,
   select the file delimited schema for *partsmaster.csv* and drop
   it on the design workspace.
3. From the dialog box that pops up, select tFileInputDelimited.

   Then the tFileInputDelimited
   (*partsmaster*) component displays in the design
   workspace.
4. From the Palette, drop the tStandardizeRow component and two tLogRow components into the design
   workspace.
5. Right-click tFileInputDelimited
   (*partsmaster*) to open the contextual
   menu.
6. From the contextual menu, select Row >
   Main link to connect this component to tStandardizeRow.
7. Accept the schema propagation prompted by the pop-up dialog
   box.
8. From tStandardizeRow, do the same to
   connect this component to one of the two tLogRow components using Row >
   Main link and to the other using Row > Reject link and accept the schema
   propagation.

   You can change the name displayed for each of these component as
   what has been done for one of the tLogRow
   component, named as *Exception* in this scenario. For further
   information, see [View tab](/talend/r/en-US/8.0/studio-user-guide/view-tab).

## Results

Then you can continue to configure each component to be used.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/standardization/tstandardizerow-tlogrow-tfilterrow-textractxmlfield-executing-normalization-job-standard-component-enterprise-press-f6 -->
# Executing the normalization Job

Last updated: 9/30/2026

Press F6 to run this Job.

In the console of the Run view, you can read
the output data structure. Each instance of the XML data is written on a
separate row because the Pretty print check box
is selected in the Advanced settings view of
the tStandardizeRow component.

Corresponding to the raw data, such as, *34-9923, Monolithic
Membrance, 4' x 8', 26 lbs*, an XML segment is generated where the
compliant data are separated from the noncompliant data (unmatched). Thus the
raw data are normalized.

Again from this console, you can read that a row is rejected as it contains
unrecognizable data.
