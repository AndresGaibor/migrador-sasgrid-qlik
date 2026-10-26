<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch · versión 8.0 -->
# tSynonymSearch

Last updated: 9/30/2026

Searches a given index for the reference entries matching the data you input.

tSynonymSearch reads input data and searches for reference entries defined in a given synonym index. If this component finds matched entries in the synonym index, it outputs them along with the corresponding input data and the relative matching details.

For further information about how to create a synonym index and define the reference entries, see [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput).

For further information about how to access and manage the words and the
reference entries (documents) of an existing synonym index using the synonym index editor,
see [Using the synonym index editor](/talend/r/en-US/8.0/studio-user-guide/using-synonym-index-editor).

For further information about available synonym indexes, see [Data synonym dictionaries](/talend/r/Lfrx8uSM%7EUd8zWd9BsWB5g/btg5jctOg_g2f_EBmyRgzA).

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tSynonymSearch Standard properties](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-standard-properties)
* [tSynonymSearch properties for Apache Spark Batch](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-properties-for-apache-spark-batch)
* [tSynonymSearch properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-properties-for-apache-spark-streaming)
* [tSynonymSearch properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Searching a given index for matched reference entries](tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-searching-given-index-for-matched-reference-entries-standard-component-enterprise-in-this)
* [Searching for matched reference entries for two input columns](tsynonymsearch-tfixedflowinput-searching-for-matched-reference-entries-for-two-input-columns-standard-component-enterprise-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-properties-for-apache-spark-batch -->
# tSynonymSearch properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tSynonymSearch running in the Spark Batch Job framework.

The Spark Batch
tSynonymSearch component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Default columns are provided in the schema of this component in   order to present the matching details between the input data and the reference entries.  For further information about the default schema columns, see [Default schema columns](/talend/r/en-US/8.0/components/synonym-index/default-schema-columns).  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Limit of each group | Type in a number to indicate the maximum display of the reference entries matched to each group of the input data. Each row of input data is recognized as one group by this component.  If the entries count exceeds the indicated limit, this component displays the ones scored the highest. For further information about the scores used on the matched entries, see [Default schema columns](/talend/r/en-US/8.0/components/synonym-index/default-schema-columns). |
| Columns to search | Complete this table to provide parameters used to match the input data and the reference entries in a given index.  The columns to be completed are:  - Input column: select the column(s) of interest from the input data schema.  - Reference output column: select the column(s) from the output data schema to present the matched reference entries found in the given synonym index.  Index path: enter the path to the index you need to search in the cluster. The value must be enclosed in double quotation marks.  When using Spark Local mode, use a path to a local folder:  * Apache Spark 3.1 and earlier: prefix://file path or   file:///file path. * Apache Spark 3.2 and later: file:///file path.  Otherwise, use a path to the folder where the index is stored in HDFS. The path must start with `hdfs://`. You cannot use a path to a local folder.  - Search mode: select the search mode you want to use to match input strings against index strings. For further information about available search modes, see [Search modes for Index rules](/talend/r/en-US/8.0/components/standardization/search-modes-for-index-rules).  - Score threshold (available for all modes): set a numerical value above `0.0` by which you want to filter the results. Set the threshold to `0.0` to disable the filter.  The score value is returned by the Lucene engine and can be anything above 0. The higher the score is, the higher is the similarity of the match. Use the threshold to remove low scoring matches from the output results. There is no easy way to decide about a good threshold value. It will depend on the input data and the indexed data.  - Max edits (based on the Levenshtein algorithm and available for the Match all fuzzy and Match any fuzzy modes): select an edit distance, `1` or `2`, from the list. Any terms within the edit distance from the input data are matched. With a max edit distance `2`, for example, you can have up to 2 insertions, deletions, or substitutions  Fuzzy match gains much in performance with Max edits for fuzzy match.  Information noteNote: Jobs migrated in Talend Studio from older releases run correctly, but results might be slightly different because Max edits for fuzzy match is now used in place of Minimum similarity for fuzzy match.  - Word distance (available for the Match partial mode): select from the list the maximum number of words allowed to come inside a sequence of words that may be found in the index, default value is `1`.  - Limit: type in a number to indicate the maximum reference entries to be matched to each record of the corresponding input column you have selected. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Connections | Outgoing links (from this component to another):  Row: Main; Reject  Trigger: Run if; On Component Ok; On Component Error.  Incoming links (from one component to this one):  Row: Main; Reject  For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-properties-for-apache-spark-structured-streaming -->
# tSynonymSearch properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tSynonymSearch running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tSynonymSearch component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Default columns are provided in the schema of this component in   order to present the matching details between the input data and the reference entries.  For further information about the default schema columns, see [Default schema columns](/talend/r/en-US/8.0/components/synonym-index/default-schema-columns).  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Limit of each group | Type in a number to indicate the maximum display of the reference entries matched to each group of the input data. Each row of input data is recognized as one group by this component.  If the entries count exceeds the indicated limit, this component displays the ones scored the highest. For further information about the scores used on the matched entries, see [Default schema columns](/talend/r/en-US/8.0/components/synonym-index/default-schema-columns). |
| Columns to search | Complete this table to provide parameters used to match the input data and the reference entries in a given index.  The columns to be completed are:  - Input column: select the column(s) of interest from the input data schema.  - Reference output column: select the column(s) from the output data schema to present the matched reference entries found in the given synonym index.  Index path: enter the path to the index you need to search in the cluster. The value must be enclosed in double quotation marks.  When using Spark Local mode, use a path to a local folder:  * Apache Spark 3.1 and earlier: prefix://file path or   file:///file path. * Apache Spark 3.2 and later: file:///file path.  Otherwise, use a path to the folder where the index is stored in HDFS. The path must start with `hdfs://`. You cannot use a path to a local folder.  - Search mode: select the search mode you want to use to match input strings against index strings. For further information about available search modes, see [Search modes for Index rules](/talend/r/en-US/8.0/components/standardization/search-modes-for-index-rules).  - Score threshold (available for all modes): set a numerical value above `0.0` by which you want to filter the results. Set the threshold to `0.0` to disable the filter.  The score value is returned by the Lucene engine and can be anything above 0. The higher the score is, the higher is the similarity of the match. Use the threshold to remove low scoring matches from the output results. There is no easy way to decide about a good threshold value. It will depend on the input data and the indexed data.  - Max edits (based on the Levenshtein algorithm and available for the Match all fuzzy and Match any fuzzy modes): select an edit distance, `1` or `2`, from the list. Any terms within the edit distance from the input data are matched. With a max edit distance `2`, for example, you can have up to 2 insertions, deletions, or substitutions  Fuzzy match gains much in performance with Max edits for fuzzy match.  Information noteNote: Jobs migrated in Talend Studio from older releases run correctly, but results might be slightly different because Max edits for fuzzy match is now used in place of Minimum similarity for fuzzy match.  - Word distance (available for the Match partial mode): select from the list the maximum number of words allowed to come inside a sequence of words that may be found in the index, default value is `1`.  - Limit: type in a number to indicate the maximum reference entries to be matched to each record of the corresponding input column you have selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-standard-properties -->
# tSynonymSearch Standard properties

Last updated: 9/30/2026

These properties are used to configure tSynonymSearch running in the Standard Job framework.

The Standard
tSynonymSearch component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Default columns are provided in the schema of this component in   order to present the matching details between the input data and the reference entries.  For further information about the default schema columns, see [Default schema columns](/talend/r/en-US/8.0/components/synonym-index/default-schema-columns).  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Limit of each group | Type in a number to indicate the maximum display of the reference entries matched to each group of the input data. Each row of input data is recognized as one group by this component.  If the entries count exceeds the indicated limit, this component displays the ones scored the highest. For further information about the scores used on the matched entries, see [Default schema columns](/talend/r/en-US/8.0/components/synonym-index/default-schema-columns). |
| Columns to search | Complete this table to provide parameters used to match the input data and the reference entries in a given index.  The columns to be completed are:  - Input column: select the column(s) of interest from the input data schema.  - Reference output column: select the column(s) from the output data schema to present the matched reference entries found in the given synonym index.  - Index path: enter the path to the index you need to search. The value must be enclosed in double quotation marks.  - Search mode: select the search mode you want to use to match input strings against index strings. For further information about available search modes, see [Search modes for Index rules](/talend/r/en-US/8.0/components/standardization/search-modes-for-index-rules).  - Score threshold (available for all modes): set a numerical value above `0.0` by which you want to filter the results. Set the threshold to `0.0` to disable the filter.  The score value is returned by the Lucene engine and can be anything above 0. The higher the score is, the higher is the similarity of the match. Use the threshold to remove low scoring matches from the output results. There is no easy way to decide about a good threshold value. It will depend on the input data and the indexed data.  - Max edits (based on the Levenshtein algorithm and available for the Match all fuzzy and Match any fuzzy modes): select an edit distance, `1` or `2`, from the list. Any terms within the edit distance from the input data are matched. With a max edit distance `2`, for example, you can have up to 2 insertions, deletions, or substitutions  Fuzzy match gains much in performance with Max edits for fuzzy match.  Information noteNote: Jobs migrated in Talend Studio from older releases run correctly, but results might be slightly different because Max edits for fuzzy match is now used in place of Minimum similarity for fuzzy match.  - Word distance (available for the Match partial mode): select from the list the maximum number of words allowed to come inside a sequence of words that may be found in the index, default value is `1`.  - Limit: type in a number to indicate the maximum reference entries to be matched to each record of the corresponding input column you have selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component needs incoming data from the preceding component. |
| Connections | Outgoing links (from this component to another):  Row: Main; Reject  Trigger: Run if; On Component Ok; On Component Error.  Incoming links (from one component to this one):  Row: Main; Reject  For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tfixedflowinput-searching-for-matched-reference-entries-for-two-input-columns-standard-component-enterprise-in-this -->
# Searching for matched reference entries for two input columns

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

In this scenario, you are going to use the previous Job with slight modifications on
it in order to search two synonym indexes for input data from two columns.

In addition to the index used earlier, another index is used alongside holding the
last name data, for example, *Correia*, *Corria*,
*Toum*, *Toom*, *toom*,
*Walker*, *Waker*.

To replicate this scenario, open the Job created in the previous section and proceed
as follows:

### In this section

* [Configuring the components](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tfixedflowinput-configuring-components-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tfixedflowinput-executing-job-standard-component-enterprise-press-f6)

**Related concepts**  

* [tSynonymSearch](tsynonymsearch "Searches a given index for the reference entries matching the data you input.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-searching-given-index-for-matched-reference-entries-standard-component-enterprise-in-this -->
# Searching a given index for matched reference entries

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

In this scenario, a three-component Job reads the provided first name data, searches a
given synonym index for reference entries that match the input data and then outputs the
results.

Create a first-name synonym index for this Job following the procedures outlined in
[Creating a synonym index for people names using tMap](/talend/en-US/components/8.0/synonym-index/tsynonymoutput-tfileinputdelimited-tmap-tlogrow-creating-synonym-index-for-people-names-using-tmap-standard-component-enterprise-in-this).

The three components used in this Job are:

* tFixedFlowInput: this component generates the
  input data you will match against the reference entries in the synonym
  index.
* tSynonymSearch: this component searches for
  the matched reference entries in the synonym index.
* tLogRow
   *(found)*: this
  component lists the result of this matching search.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-setting-up-job-standard-component-enterprise-drop)
* [Configuring the components](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-configuring-components-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-executing-job-standard-component-enterprise-press-f6)

**Related concepts**  

* [tSynonymSearch](tsynonymsearch "Searches a given index for the reference entries matching the data you input.")

**Related reference**  

* [tSynonymOutput](tsynonymoutput "Creates a Lucene index and feeds it with entries and the related synonyms it receives.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tfixedflowinput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Next to Edit schema, click the [...] button to open the Schema dialog box, and add a second column
   *LASTNAME* next to the *FIRSTNAME*
   column you have defined in the previous scenario.

   When done, click OK to validate this
   change and thus close the dialog box.
3. In the Content field of the Mode area, add more first name and last name data
   to make the input data read as
   follows:Kristof;Toum
   Chris;Toom
   Tony;Walker
   Anton;Correia
   Jim;Correia
   Jim;Walker
4. Double-click tSynonymSearch to open its
   Basic settings view.
5. Click Sync columns to synchronize the
   columns of this component with the preceding one and click Yes to propagate the changes to the next
   component when prompted.
6. Click the [...] button next to Edit schema to open the Schema dialog box, and add two columns to the output
   schema: *matched\_fname* and
   *matched\_lname*. 

   These columns will hold the matched reference entries in the output
   flow.

   When done, click OK to validate the
   setting and accept propagating the changes when prompted.
7. In the Limit of each group field, type in
   *10* to replace the one you have defined in the
   previous scenario.
8. Under the Columns to search table, click
   the [+] button to add a second row and
   define the parameters as follows:
   * In the Input column column,
     select *LASTNAME* from the drop-down list.
   * In the Reference output column
     column, select *matched\_lname* from the drop-down
     list.
   * In the Index path column, type
     in, between quotation marks, the path to the synonym index holding
     the last name entries.

     When using Spark Local mode, use a path to
     a local folder:
     + Apache Spark 3.1 and earlier: prefix://file path or
       file:///file path.
     + Apache Spark 3.2 and later: file:///file path.
   * In the Search mode column, select
     *Match exact* for both input columns. This
     will match the exact input word against an exact index word.
   * In the Score threshold column,
     enter *0.9* to filter results and list only terms
     with higher similarity.
   * Leave the Min similarity and
     Word distance columns as they
     are only for the fuzzy modes and the *Match
     partial* mode respectively.
   * In the Limit column of this row,
     leave the default value *5*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tfixedflowinput-executing-job-standard-component-enterprise-press-f6 -->
# Executing the Job

Last updated: 9/30/2026

1. Press F6 to run this Job.

   The execution result reads as follows in the console of the Run view.

   From this result, if you take the input data *Chris
   Toom* for example, you can see that:

* this record is recognized as group 2 with a group size equal to 3. This
  means that 3 pairs of exact match reference entries are found from the two
  synonym indexes in use. The exact match for the first name are
  *Christian*, *Christiaan* and
  *Christoffel*, and the exact match for the last name
  are *toom*x3.
* the *SCORES* column contains two sub-columns.

  These sub-columns present the matching scores in regards to the
  *matched\_fname* and to the
  *matched\_lname* reference columns respectively. Each
  figure listed in the *SCORE* column is equal to the sum
  of the two figures of the same row in the sub-columns of the
  *SCORES* column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Next to the Schema field, click the
   Edit schema button to open the
   Schema dialog box, add one column and
   name it *FIRSTNAME*. When done, click OK to validate these changes and close the dialog
   box.
3. In the Mode area, select the Use Inline Content (delimited file) option, and
   supply the following names in the Content
   field:

   ```
   Kristof
   Chris
   Tony
   Anton
   ```
4. Double-click tSynonymSearch to open its
   Basic settings view.
5. Click Sync columns to add the schema
   columns of its preceding component to the default schema columns of
   tSynonymSearch.

   When prompted, click Yes to propagate the
   changes to the next component.
6. Click the [...] button next to Edit schema to open the Schema dialog box, and add one column to the output
   schema: *matched\_fname*. 

   This column will hold the matched reference entries in the output
   flow.

   When done, click OK to validate the
   setting and accept propagating the changes when prompted.
7. In the Limit of each group field, type in
   *5* to replace the default value.
8. Under the Columns to search table, click
   the [+] button to add one row and define
   the parameters as follows:
   * In the Input column column,
     select *FIRSTNAME* from the list of the input
     columns.
   * In the Reference output column
     column, select *matched\_fname* from the list of
     the output columns.
   * In the Index path column, type in
     the path to the synonym index to be used, between double quotation
     marks.

     When using Spark Local mode, use a path to
     a local folder:
     + Apache Spark 3.1 and earlier: prefix://file path or
       file:///file path.
     + Apache Spark 3.2 and later: file:///file path.
   * In the Search mode column, select
     *Match all fuzzy*. This will match each word
     of the input string against similar word of the index string.
   * In the Score threshold column,
     enter *0.9* to filter results and list only terms
     with higher similarity.
   * In the Max edits column,
     select*1* to be the allowed edit distance to
     use.

     With max edit distance *1*, you can have
     only one insertion, deletion, or substitution. Any terms within that edit
     distance from the input data are matched.
   * Leave the Word distance column as
     it is only for the *Match partial* mode.
   * In the Limit column, leave the
     default value *5*.
9. In the Basic settings view of the
   tLogRow component, select the Table option for better readable display of the
   Job execution result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-executing-job-standard-component-enterprise-press-f6 -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Press F6 to run this Job.

The execution result reads as follows in the console of the Run view.

From this result, you can see that each first name of the input string matches a similar
word of the index string. For example, the entry *Chris* from the input flow is found to fuzzy match
*3* words in the given synonym index. And this record
is recognized as group *2* that has a group size equal to
*3*, meaning that three matched reference entries are
found for this group.

The *SCORE* and the *SCORES* columns
present the same values in this scenario because only one input column is
used.

If you want to extract only the input entries that match exactly an index
string, select *Match exact* in the Search mode column in tSynonymSearch basic settings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/synonym-index/tsynonymsearch-tsynonymoutput-tlogrow-tfixedflowinput-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop tFixedFlowInput, tSynonymSearch and tLogRow from the Palette
   onto the design workspace.

   You can change the displayed name of each of these component as
   what has been done for the tLogRow component,
   named *found* in this scenario. For further information, see
   [View tab](/talend/r/en-US/8.0/studio-user-guide/view-tab).
2. Right-click the tFixedFlowInput component
   to open the contextual menu and select Row > Main.
3. Drop the link on the tSynonymSearch
   component to create an connection between these two components.
4. Do the same thing to connect tSynonymOutput to tLogRow
   *(found)*.
