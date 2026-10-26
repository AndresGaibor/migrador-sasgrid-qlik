<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey · versión 8.0 -->
# tGenKey

Last updated: 9/30/2026

Generates a functional key from the input columns, by applying different types of algorithms on each column and grouping the computed results in one key, then outputs this key with the input columns.

tGenKey enables you to apply several kinds of algorithms on each input column and use the computed results to generate a functional key, which can be used, for example, to narrow down your data filter/matching results. These algorithms can be key or optional algorithms.

The values returned by the key algorithms will be concatenated, according to the column order in the Key composition table.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tGenKey Standard properties](/talend/en-US/components/8.0/identification/tgenkey-standard-properties)
* [tGenKey properties for Apache Spark Batch](/talend/en-US/components/8.0/identification/tgenkey-properties-for-apache-spark-batch)
* [tGenKey properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/identification/tgenkey-properties-for-apache-spark-streaming)

**Related concepts**  

* [Comparing columns and grouping in the output flow duplicate records that have the same functional key](tgenkey-tmatchgroup-trowgenerator-tlogrow-comparing-columns-and-grouping-in-output-flow-duplicate-records-that-have-same-functional-key-standard-component-enterprise-this)
* [Generating functional keys in the output flow](tgenkey-tfixedflowinput-tlogrow-tmatchgroup-generating-functional-keys-in-output-flow-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-properties-for-apache-spark-batch -->
# tGenKey properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tGenKey running in the Spark Batch Job framework.

The Spark Batch
tGenKey component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click the import icon to import blocking keys from the match rules that are   defined and saved in the Talend Studio   repository.  When you click the import icon, a Match Rule   Selector wizard is opened to help you import blocking keys from the match   rules listed in the Talend Studio   repository and use them in your Job.  You can import blocking keys only from match rules that are defined with the VSR   algorithm and saved in the Talend Studio   repository. For further information, see [Importing match rules from the Talend Studio repository](/talend/r/en-US/8.0/components/data-matching/importing-match-rules-from-studio-repository) |
| Column | Select the columns from the main flow on which you want to define certain algorithms to set the functional key.  Information noteNote: When you select a date column on which to apply an algorithm or a matching algorithm, you can decide what to compare in the date format. For example, if you want to only compare the year in the date, in the component schema set the type of the date column to Date and then enter "*yyyy*" in the Date Pattern field. The component then converts the date format to a string according to the pattern defined in the schema before starting a string comparison. |
| Pre-Algorithm | If required, select the relevant matching algorithm from the list:  Remove diacritical marks: removes any diacritical mark.  Remove diacritical marks and lower case: removes any diacritical mark and converts to lower case before generating the code of the column.  Remove diacritical marks and upper case: removes any diacritical mark and converts to upper case before generating the code of the column.  Lower case: converts the field to lower case before applying the key algorithm.  Upper case: converts the field to upper case before applying the key algorithm.  Add left position character: enables you to add a character to the left of the column.  Add right position character: enables you to add a character to the right of the column. |
| Value | Set the algorithm value, where applicable. |
| Algorithm | Select the relevant algorithm from the list:  First character of each word: includes in the functional key the first character of each word in the column. When using Japanese characters in the input data, the input text should be tokenized. For more information, see [tJapaneseTokenize](/talend/r/en-US/8.0/components/text-standardization/tjapanesetokenize).  First N characters of each word: includes in the functional key first N characters of each word in the column. When using Japanese characters in the input data, the input text should be tokenized. For more information, see [tJapaneseTokenize](/talend/r/en-US/8.0/components/text-standardization/tjapanesetokenize).  First N characters of the string: includes in the functional key first N characters of the string.  Last N characters of the string: includes in the functional key last N characters of the string.  First N consonants of the string: includes in the functional key first N consonants of the string. Japanese and Chinese characters are not supported.  First N vowels of the string: includes in the functional key first N vowels of the string. Japanese and Chinese characters are not supported.  Pick characters: includes in the functional key the characters located at a fixed position (corresponding to the set digital/range).  Exact: includes in the functional key the full string.  Substring(a,b): includes in the functional key character according to the set index.  Soundex code: generates a code according to a standard English phonetic algorithm. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported.  Metaphone code: generates a code according to the character pronunciation. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported.  Double-metaphone code: generates a code according to the character pronunciation using a new version of the Metaphone phonetic algorithm, that produces more accurate results than the original algorithm. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported.  Fingerprint key: generates the functional key from a string value through the following sequential process:  1. remove leading and trailing whitespace, 2. change all characters to their lowercase representation, 3. remove all punctuation and control characters, 4. split the string into whitespace-separated tokens, 5. sort the tokens and remove duplicates, 6. join the tokens back together,  Because the string parts are sorted, the given order of tokens does not matter.    So, *Cruise, Tom* and *Tom Cruise* both end up    with a fingerprint *cruise tom* and therefore end up in the same    cluster. 7. normalize extended western characters to their ASCII representation, for example    *gödel* to *godel*.  This reproduce data entry mistakes performed when entering extended characters    with an ASCII-only keyboard. However, this procedure can also lead to false    positives, for example *gödel* and *godél*    would both end up with *godel* as their fingerprint but they are    likely to be different names. So this might work less effectively for datasets where    extended characters play substantial differentiation role.  nGramkey: this algorithm is similar to the fingerPrintkey method described above. But instead of using whitespace separated tokens, it uses n-grams, where the *n* can be specified by the user. This method generates the functional key from a string value through the following sequential process:  1. change all characters to their lowercase representation, 2. remove all punctuation and control characters, 3. obtain all the string n-grams, 4. sort the n-grams and remove duplicates, 5. join the sorted n-grams back together, 6. normalize extended western characters to their ASCII representation, for example    *gödel* to *godel*.  For example, the 2-gram fingerprint of *Paris* is    *arispari* and the 1-gram fingerprint is    *aiprs*.  The delivered implementation of this algorithm is 2-grams.   Information noteNote: If the column on which you want to use the nGramkey algorithm can have data, with only *0* or *1* characters, you must filter this data before generating the functional key. This way you avoid potentially comparing records to each other that should not be match candidates.  Cologne phonetics: a Soundex phonetic algorithm optimized for the German language. It encodes a string into a Cologne phonetic value. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported. |
| Value | Set the algorithm value, where applicable.  If you do not set a value for the algorithms which need one, the Job runs with a compilation error. |
| Post-Algorithm | If required, select the relevant matching algorithm from the list:  Use default value (string): enables you to choose a string to replace null or empty data.  Add left position character: enables you to add a character to the left of the column.  Add right position character: enables you to add a character to the right of the column. |
| Value | Set the option value, where applicable. |
| Show help | Select this check box to display instructions on how to set algorithms/options parameters. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-standard-properties -->
# tGenKey Standard properties

Last updated: 9/30/2026

These properties are used to configure tGenKey running in the Standard Job framework.

The Standard
tGenKey component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click the import icon to import blocking keys from the match rules that are   defined and saved in the Talend Studio   repository.  When you click the import icon, a Match Rule   Selector wizard is opened to help you import blocking keys from the match   rules listed in the Talend Studio   repository and use them in your Job.  You can import blocking keys only from match rules that are defined with the VSR   algorithm and saved in the Talend Studio   repository. For further information, see [Importing match rules from the Talend Studio repository](/talend/r/en-US/8.0/components/data-matching/importing-match-rules-from-studio-repository) |
| Column | Select the columns from the main flow on which you want to define certain algorithms to set the functional key.  Information noteNote: When you select a date column on which to apply an algorithm or a matching algorithm, you can decide what to compare in the date format. For example, if you want to only compare the year in the date, in the component schema set the type of the date column to Date and then enter "*yyyy*" in the Date Pattern field. The component then converts the date format to a string according to the pattern defined in the schema before starting a string comparison. |
| Pre-Algorithm | If required, select the relevant matching algorithm from the list:  Remove diacritical marks: removes any diacritical mark.  Remove diacritical marks and lower case: removes any diacritical mark and converts to lower case before generating the code of the column.  Remove diacritical marks and upper case: removes any diacritical mark and converts to upper case before generating the code of the column.  Lower case: converts the field to lower case before applying the key algorithm.  Upper case: converts the field to upper case before applying the key algorithm.  Add left position character: enables you to add a character to the left of the column.  Add right position character: enables you to add a character to the right of the column. |
| Value | Set the algorithm value, where applicable. |
| Algorithm | Select the relevant algorithm from the list:  First character of each word: includes in the functional key the first character of each word in the column. When using Japanese characters in the input data, the input text should be tokenized. For more information, see [tJapaneseTokenize](/talend/r/en-US/8.0/components/text-standardization/tjapanesetokenize).  First N characters of each word: includes in the functional key first N characters of each word in the column. When using Japanese characters in the input data, the input text should be tokenized. For more information, see [tJapaneseTokenize](/talend/r/en-US/8.0/components/text-standardization/tjapanesetokenize).  First N characters of the string: includes in the functional key first N characters of the string.  Last N characters of the string: includes in the functional key last N characters of the string.  First N consonants of the string: includes in the functional key first N consonants of the string. Japanese and Chinese characters are not supported.  First N vowels of the string: includes in the functional key first N vowels of the string. Japanese and Chinese characters are not supported.  Pick characters: includes in the functional key the characters located at a fixed position (corresponding to the set digital/range).  Exact: includes in the functional key the full string.  Substring(a,b): includes in the functional key character according to the set index.  Soundex code: generates a code according to a standard English phonetic algorithm. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported.  Metaphone code: generates a code according to the character pronunciation. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported.  Double-metaphone code: generates a code according to the character pronunciation using a new version of the Metaphone phonetic algorithm, that produces more accurate results than the original algorithm. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported.  Fingerprint key: generates the functional key from a string value through the following sequential process:  1. remove leading and trailing whitespace, 2. change all characters to their lowercase representation, 3. remove all punctuation and control characters, 4. split the string into whitespace-separated tokens, 5. sort the tokens and remove duplicates, 6. join the tokens back together,  Because the string parts are sorted, the given order of tokens does not matter.    So, *Cruise, Tom* and *Tom Cruise* both end up    with a fingerprint *cruise tom* and therefore end up in the same    cluster. 7. normalize extended western characters to their ASCII representation, for example    *gödel* to *godel*.  This reproduce data entry mistakes performed when entering extended characters    with an ASCII-only keyboard. However, this procedure can also lead to false    positives, for example *gödel* and *godél*    would both end up with *godel* as their fingerprint but they are    likely to be different names. So this might work less effectively for datasets where    extended characters play substantial differentiation role.  nGramkey: this algorithm is similar to the fingerPrintkey method described above. But instead of using whitespace separated tokens, it uses n-grams, where the *n* can be specified by the user. This method generates the functional key from a string value through the following sequential process:  1. change all characters to their lowercase representation, 2. remove all punctuation and control characters, 3. obtain all the string n-grams, 4. sort the n-grams and remove duplicates, 5. join the sorted n-grams back together, 6. normalize extended western characters to their ASCII representation, for example    *gödel* to *godel*.  For example, the 2-gram fingerprint of *Paris* is    *arispari* and the 1-gram fingerprint is    *aiprs*.  The delivered implementation of this algorithm is 2-grams.   Information noteNote: If the column on which you want to use the nGramkey algorithm can have data, with only *0* or *1* characters, you must filter this data before generating the functional key. This way you avoid potentially comparing records to each other that should not be match candidates.  Cologne phonetics: a Soundex phonetic algorithm optimized for the German language. It encodes a string into a Cologne phonetic value. This code represents the character string that will be included in the functional key. Japanese and Chinese characters are not supported. |
| Value | Set the algorithm value, where applicable.  If you do not set a value for the algorithms which need one, the Job runs with a compilation error. |
| Post-Algorithm | If required, select the relevant matching algorithm from the list:  Use default value (string): enables you to choose a string to replace null or empty data.  Add left position character: enables you to add a character to the left of the column.  Add right position character: enables you to add a character to the right of the column. |
| Value | Set the option value, where applicable. |
| Show help | Select this check box to display instructions on how to set algorithms/options parameters. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStat Catcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level.  Note that this check box is not available in the Map/Reduce version of the component. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component.  This component can be used with other components, such as tMatchGroup, in order to create a blocking key. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-generating-functional-keys-in-output-flow-standard-component-enterprise-this -->
# Generating functional keys in the output flow

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This three-component scenario describes a basic Job that generates a functional
key for each of the data records using one algorithm on one of the input columns, *PostalCode*.

This functional key can be used in different ways to narrow down the results
of data filtering or data matching, for example. So the
tGenKey component can be used with so many other data quality and data
integration components to form different useful use cases. For an example of one use case of
tGenKey, see [Comparing columns and grouping in the output flow duplicate
records that have the same functional key](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-comparing-columns-and-grouping-in-output-flow-duplicate-records-that-have-same-functional-key-standard-component-enterprise-this).

In this scenario, the input data flow has four columns: *Firstname*, *Lastname*, *DOB* (date of birth),
and *PostalCode*. This data has problems such as duplication, first or
last names spelled differently or wrongly, different information for the same customer, etc.
This scenario generates a functional key for each data record using an algorithm that
concatenates the first two characters of the postal code.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-setting-up-job-standard-component-enterprise-drop)
* [Configuring the data input](/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-configuring-data-input-standard-component-enterprise)
* [Configuring key generation](/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-configuring-key-generation-standard-component-enterprise)
* [Configuring the console output](/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-configuring-console-output-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-executing-job-standard-component-enterprise-save)

**Related concepts**  

* [tGenKey](tgenkey "Generates a functional key from the input columns, by applying different types of algorithms on each column and grouping the computed results in one key, then outputs this key with the input columns.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMatchGroup](/talend/en-US/components/8.0/data-matching/tmatchgroup)
* [tRecordMatching](/talend/en-US/components/8.0/data-matching/trecordmatching)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-comparing-columns-and-grouping-in-output-flow-duplicate-records-that-have-same-functional-key-standard-component-enterprise-this -->
# Comparing columns and grouping in the output flow duplicate records that have the same functional key

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This second scenario describes a Job that aims at:

* generating a functional key using one algorithm on
  one of the input columns, *DoB* as
  described in scenario 1.
* matching two input columns using the *Jaro-Winkler* algorithm.
* grouping the output columns by the generated functional key to
  optimize the matching operation and compare only the records that have the same
  blocking value, functional key in this scenario. For more information on grouping
  output columns and using blocking values, see [tMatchGroup](/talend/en-US/data-matching/8.0/tmatchgroup).

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-setting-up-job-standard-component-enterprise-drop)
* [Configuring the data input](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-data-input-standard-component-enterprise)
* [Configuring key generation](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-key-generation-standard-component-enterprise)
* [Configuring the grouping of the output data](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-grouping-of-output-data-standard-component-enterprise-click)
* [Configuring the console output](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-console-output-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-executing-job-standard-component-enterprise-save)

**Related concepts**  

* [tGenKey](tgenkey "Generates a functional key from the input columns, by applying different types of algorithms on each column and grouping the computed results in one key, then outputs this key with the input columns.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMatchGroup](/talend/en-US/components/8.0/data-matching/tmatchgroup)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tRecordMatching](/talend/en-US/components/8.0/data-matching/trecordmatching)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-configuring-console-output-standard-component-enterprise -->
# Configuring the console output

Last updated: 9/30/2026

## Procedure

1. Double-click the tLogRow
   component to display the Basic settings view.
2. In the Mode area,
   select Table to
   display the Job execution result in table cells.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-configuring-data-input-standard-component-enterprise -->
# Configuring the data input

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display the
   Basic settings
   view and define the component properties.
2. Click the [...]
   button next to Edit
   Schema to open the Schema dialog box.
3. Click the plus button to add as many lines as needed
   for the input schema you want to create from
   internal variables. 

   In this example, the schema is made of four columns:
   *Firstnam*,
   *Lastname*,
   *DOB* and
   *PostalCode*.

   Then, click OK to
   close the dialog box.
4. In the Mode area,
   select the Use Inline
   Table option.

   The Value table
   displays as Inline
   Table.
5. Click the plus button to add as many line as needed
   and then click in each of the lines to define the
   input data for the four columns.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-configuring-key-generation-standard-component-enterprise -->
# Configuring key generation

Last updated: 9/30/2026

1. Double-click tGenKey to
   display the Basic settings
   view and define the component properties.

   You can click
   and import blocking keys from the match
   rules created with the VSR algorithm and tested in the
   Profiling
    perspective of
   *Talend Studio* and use them in your
   Job. Otherwise, define the blocking key parameters as
   described in the below steps.
2. Under the Algorithm table,
   click the plus button to add a row in this table.
3. In the column column, click
   the newly added row and select from the list the column you
   want to process using an algorithm. In this example, select
   *PostalCode*.

   Information noteNote: When you select a date column on which to apply an algorithm or a matching
   algorithm, you can decide what to compare in the date format.

   For example,
   if you want to only compare the year in the date, in the component schema set the type
   of the date column to Date and then enter "*yyyy*" in the Date Pattern field.
   The component then converts the date format to a string according to the pattern defined
   in the schema before starting a string comparison.
4. Select the Show help check
   box to display instructions on how to set algorithms/options
   parameters.
5. In the algorithm column,
   click the newly added row and select from the list the
   algorithm you want to apply to the corresponding column. In
   this example, select first N
   characters of the string.
6. Click in the Value column and
   enter the value for the selected algorithm, when needed. In
   this scenario, type in *2*.

   In this example, we want to generate a functional key that
   holds the first two characters of the postal code for each
   of the data rows and we do not want to define any extra
   options on these columns.

   Make sure to set a value for the algorithm which need one,
   otherwise you may have a compilation error when you run the
   Job.

Once you have defined the tGenKey
properties, you can display a statistical view of these parameters.
To do so:

1. Right-click the tGenKey
   component and select View Key
   Profile in the contextual menu.

   The View Key Profile editor
   displays, allowing you to visualize the statistics regarding
   the number of rows per block and to adapt them according to
   the results you want to get.

   When you are processing a large amount of data and when this
   component is used to partition data in order to use them in
   a matching component (such as tRecordMatching or tMatchGroup), it is preferable to have a
   limited number of rows in one block. An amount of about 50
   rows per block is considered optimal, but it depends on the
   number of fields to compare, the total number of rows and
   the time considered acceptable for data processing.

   For a use example of the View Key
   Profile option, see [Comparing columns and grouping in the output flow duplicate
   records that have the same functional key](/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-comparing-columns-and-grouping-in-output-flow-duplicate-records-that-have-same-functional-key-standard-component-enterprise-this).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-executing-job-standard-component-enterprise-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Save your Job and press F6 to execute it.

All the output columns including the
*T\_GEN\_KEY* column are listed
in the Run console.
The functional key for each data record is
concatenated from the first two characters of the
corresponding value in the *PostalCode*column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tfixedflowinput-tlogrow-tmatchgroup-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design
   workspace: tFixedFlowInput, tGenKey and tLogRow.
2. Connect all the components together using the
   Main link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-console-output-standard-component-enterprise -->
# Configuring the console output

Last updated: 9/30/2026

## Procedure

1. Double-click the tLogRow
   component to display the Basic settings view.
2. In the Mode area,
   select Table to
   display the Job execution result in table cells.

## Results


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-data-input-standard-component-enterprise -->
# Configuring the data input

Last updated: 9/30/2026

## Procedure

1. Double-click tRowGenerator to define its schema as
   follows:

   The tRowGenerator
   component will generate an input data flow that has
   three columns: *Firstname,
   Lastname*, and *DoB*
   (date of birth). This data may have problems such as
   duplication, first or last names spelled differently
   or wrongly, different information for the same
   customer, etc.
2. Click OK to validate
   the settings and close the dialog box, and accept to
   propagate the changes when prompted.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-grouping-of-output-data-standard-component-enterprise-click -->
# Configuring the grouping of the output data

Last updated: 9/30/2026

## Procedure

1. Click the tMatchGroup
   component, and then in its basic settings click the
   Edit schema
   button to view the input and output columns and do
   any modifications in the output schema, if
   needed.

   In the output schema of this component, there are
   output standard columns that are read-only. For more
   information, see [tMatchGroup Standard properties](/talend/en-US/data-matching/8.0/tmatchgroup-standard-properties).
2. Click OK to close the
   dialog box.
3. Double-click the tMatchGroup component to
   display its Configuration Wizard and define the
   component properties.

   If you want to add a fixed output column,
   *MATCHING\_DISTANCES,* which gives the details of the distance
   between each column, click the Advanced
   settings tab and select the Output distance
   details check box. For more information, see [tMatchGroup Standard properties](/talend/en-US/data-matching/8.0/tmatchgroup-standard-properties).
4. In the Key definition
   table, click the plus button to add to the list the
   columns on which you want to do the matching
   operation, *FirstName* and
   *LastName* in this
   scenario.
5. Click in the first and second cells of the Matching Function column
   and select from the list the algorithm(s) to be used
   for the matching operation,
   *Jaro-Winkler* in this
   example.
6. Click in the first and second cells of the Weight column and set the
   numerical weights for each of the columns used as
   key attributes.
7. In the Match
   threshold field, enter the match
   probability threshold. Two data records match when
   the probability threshold is above this value.
8. Click the plus button below the Blocking Selection table to add a line
   in the table, then click in the line and select from
   the list the column you want to use as a blocking
   value, *T\_GEN\_KEY* in this
   example. 

   Using a blocking value reduces the number of pairs of
   records that needs to be examined. The input data is
   partitioned into exhaustive blocks based on the
   functional key. This will decrease the number of
   pairs to compare, as comparison is restricted to
   record pairs within each block.
9. Click the Chart
   button in the top right corner of the wizard to
   execute the Job in the defined configuration and
   have the matching results directly in the
   wizard.

   The matching chart gives a global picture about the
   duplicates in the analyzed data. The matching table
   indicates the details of items in each group and
   colors the groups in accordance with their color in
   the matching chart.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-configuring-key-generation-standard-component-enterprise -->
# Configuring key generation

Last updated: 9/30/2026

## Procedure

1. Double-click tGenKey
   to display the Basic
   settings view and define the component
   properties.

   You can click
   and import blocking keys from
   the match rules created with the VSR algorithm and
   tested in the 
   Profiling
    perspective of
   *Talend Studio* and use them in your
   Job. Otherwise, define the blocking key parameters
   as described in the below steps.
2. Under the Algorithm
   table, click the [+] button to add a row in this
   table.
3. On the column column,
   click the newly added row and select from the list
   the column you want to process using an algorithm.
   In this example, select
   *DoB*.
4. On the algorithm
   column, click the newly added row and select from
   the list the algorithm you want to apply to the
   corresponding column. In this example, select
   *substring(a,b)*.
5. Click in the value column and enter the value
   for the selected algorithm, when needed. In this scenario, type in
   *6;10*.

   The *substring(a,b)* algorithm allows you to extract the
   characters from a string, between two specified indices, and to return the new
   substring. First character is at index *0*. In this scenario,
   for a given *DoB*
   "*21-01-1995*", *6;10* will return only
   the year of birth, that is to say "1995" which is the substring from the 7th to
   the 10th character.

   In this example, we want to generate a functional key that holds the last four
   characters of the date of birth, which correspond to the year of birth, for each
   of the data rows and we do not want to define any extra options on these
   columns.

   You can select the Show help check box to
   display instructions on how to set algorithms/options parameters.

   Once you have defined the tGenKey properties,
   you can display a statistical view of these parameters. To do so:
6. Right-click on the tGenKey component and
   select View Key Profile in the contextual
   menu.

   The View Key Profile editor displays,
   allowing you to visualize statistics regarding the number of blocks and to adapt
   the parameters according to the results you want to get.

   Information noteNote:

   When you are processing a large amount of data and when this component is
   used to partition data in order to use them in a matching component (such as
   tRecordMatching or tMatchGroup), it is preferable to have a limited number of rows
   in one block. An amount of about 50 rows per block is considered optimal,
   but it depends on the number of fields to compare, the total number of rows
   and the time considered acceptable for data processing.

   From the key editor, you can:
   * Edit the Limit of
     rows used to calculate the statistics.
   * Click  and import blocking keys from the Talend Studio repository and use them in your Job.
   * Edit the input column you want to process using an
     algorithm.
   * Edit the parameters of the algorithm you want to apply to
     input columns.

   Every time you make a modification, you can see its implications by clicking
   the Refresh button which is located at the top
   right part of the editor.
7. Click OK to close the
   View Key Profile
   editor.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-executing-job-standard-component-enterprise-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Save your Job and press F6 to execute it.

The output columns include the
*T\_GEN\_KEY* column that holds
the functional key generated by the tGenKey component.

You can see that all records that have the same
functional key are grouped together in different
blocks "groups". The identifier for each group is
listed in the *GID* column next
to the corresponding record. The number of records
in each of the output blocks is listed in the
*GRP\_SIZE* column and computed
only on the master record. The
*MASTER* column indicates with
true/false if the corresponding record is a master
record or not a master record. The
*SCORE* column lists the
calculated distance between the input record and the
master record according to the
*Jaro-Winkler* matching
algorithm.

For an example of creating data partitions based on different
blocking keys and using them with multiple tMatchGroup components, see [tMatchGroup](/talend/en-US/data-matching/8.0/tmatchgroup).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/identification/tgenkey-tmatchgroup-trowgenerator-tlogrow-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design
   workspace: tRowGenerator, tGenKey and tMatchGroup.
2. Connect all the components together using the
   Main link.
