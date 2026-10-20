<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-matching/tmatchgroup · versión 8.0 -->
# tMatchGroup

Last updated: 9/30/2026

Creates groups of similar data records in any source data including large volumes
of data by using one or several match rules.

tMatchGroup compares columns in both standard input data flows and in
Spark input data flows by using matching methods and groups similar encountered duplicates
together.

Several tMatchGroup components can be used sequentially to match data
against different blocking keys. This will refine the groups received by
each of the tMatchGroup components through
creating different data partitions that overlap previous data blocks and so
on.

In defining a group, the first processed record of each
group is the master record of the group. The other records are computed as
to their distances from the master records and then are distributed to the
due master record accordingly.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tMatchGroup Standard properties](/talend/en-US/components/8.0/data-matching/tmatchgroup-standard-properties)
* [tMatchGroup properties for Apache Spark Batch](/talend/en-US/components/8.0/data-matching/tmatchgroup-properties-for-apache-spark-batch)
* [Configuration wizard](/talend/en-US/components/8.0/data-matching/configuration-wizard)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-matching/tmatchgroup-properties-for-apache-spark-batch -->
# tMatchGroup properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMatchGroup running in
the Spark Batch Job framework.

The Spark Batch
tMatchGroup component belongs to the Data Quality family.

This component is available from the 8.0 R2024-08 Talend Studio monthly
release.

Information noteImportant: When using the Simple VSR algorithm, the results depend on the input
data and the Spark API shuffling. This causes different results at each Job run. To
optimize the result stability, it is highly recommended to use the [tPartition component](/talend/en-US/components/8.0/processing/tpartition) right before the
tMatchGroup component.

To optimize the result stability, you can also:

* Set the same Blocking key
  (tMatchGroup) and Partition key
  (tPartition).
* Select unique values as the Sort key
  (tPartition). For example, the ID.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  The output schema of this component contains the following   read-only fields:  The output schema of this component contains   the following read-only fields:  + `GID`: Provides a group     identifier of the data type *String*.   + `GRP_SIZE`: Counts the     number of records in the group, computed only on the master record.   + `MASTER`: Identifies, by     true or false, if the record used in the matching comparisons is a     master record. There is only one master record per group. Each input record     will be compared to the master record, if they match, the input record will     be in the group.   + `SCORE`: Measures the     distance between the input record and the master record according to the     matching algorithm used. In case the tMatchGroup component is used to have multiple output     flows, the score in this column decides to what output group the record     should go.   + `GRP_QUALITY` provides the     quality of similarities in the group by taking the minimal     matching value. Only the master record has a quality     score. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Matching Algorithm | Simple VSR is set by default. Information noteRestriction: The T-Swoosh algorithm is not available for the Apache Spark Batch component. You can use it for the [Standard component](tmatchgroup-standard-properties "These properties are used to configure tMatchGroup running in the Standard Job framework."). |
|  | Click the import icon to import a match rule from the Talend Studio repository.  For further information about how to import rules, see [Importing match rules from the repository](/talend/en-US/data-matching/8.0/importing-match-rules-from-studio-repository) |
| Key Definition - Input Key Attribute column | Select the columns from the input flow on which you want to apply a matching algorithm.  Information noteNote: When you select a date column on which to apply an algorithm or a matching algorithm, you can decide what to compare in the date format. For example, if you want to only compare the year in the date, in the component schema set the type of the date column to Date and then enter "*yyyy*" in the Date Pattern field. The component then converts the date format to a string according to the pattern defined in the schema before starting a string comparison. |
| Key Definition - Matching Function column | Select a matching algorithm from the list. For more information on each algorithm, see [Matching algorithms](#matching-algorithms-section). |
| Key Definition - Custom Matcher Class column | When you select Custom as the matching type, enter the path pointing to the custom class (external matching algorithm) you need to use. This path is defined by yourself in the library file (*.jar* file) which you can import by using the tLibraryLoad component.  For example, to use a *MyDistance.class* class stored in the directory *org/talend/mydistance* in a user-defined *mydistance.jar* library, the path to be entered is *org.talend.mydistance.MyDistance*. |
| Key Definition - Tokenized measure column | Tokenization is the concept of splitting a string into words. Select the method to use to compute a tokenized measure for the selected algorithm:  * No: No tokenization method is used on the   string. With this option, "John Doe" and "Jon Doe" should   match. * Same place: Splits the two strings by words   to two lists, list1 and list2. Associates each element from list1   with the element which has the same position in list2. Using this   method, "She is red and he is pink" and "Catherine is red and he is   pink" should match. * Same order: Splits the two strings by words   to two lists, list1 and list2 and assumes that list1 is shorter than   list2. Tries to associate the elements from list1 with the elements   in list2 taken in the same order. Using this method, "John Doe" and   "John B. Doe" match. * This method should be used only with strings which has a few words,   otherwise the number of possible combinations can be large. * Any order: Splits the two strings by words to   two lists, list1 and list2 and assumes that list1 is shorter than   list2. Tries to assign each word of list1 to a word of list2, in   order to have the highest global similarity (with respect to the   used similarity). Using this method, "John Doe" and "Doe John"   match. |
| Key Definition - Confidence Weight column | Set a numerical weight for each attribute (column) of the key definition.  You can enter a number or a context variable.  The value must be an integer greater than 0. |
| Key Definition - Handle Null column | To handle null values, select from the list the null operator you want to use on the column:  Null Match Null: A Null attribute only matches another Null attribute.  Null Match NONE: A Null attribute never matches another attribute.  Null Match ALL: A Null attribute matches any other value of an attribute.  For example, two columns, *name* and *firstname* where the name is never null, but the first name can be null.  If two records:  "Doe", "John"  "Doe", ""  Depending on the operator you choose, these two records may or may not match:  Null Match Null: They do not match.  Null Match NONE: They do not match.  Null Match ALL: They match.  For the records:  "Doe", ""  "Doe", ""  Null Match Null: They match.  Null Match NONE: They do not match.  Null Match ALL: They match. |
| Match Threshold | Enter the match probability. Two data records match when the probability is greater than or equal to the set value.  You can enter a different match threshold for each match rule. |
| Blocking Selection | If required, select the columns from the input flow according to which you want to partition the processed data in blocks, this is usually referred to as "blocking".  Blocking reduces the number of pairs of records that needs to be examined. In blocking, input data is partitioned into exhaustive blocks designed to increase the proportion of matches observed while decreasing the number of pairs to compare. Comparisons are restricted to record pairs within each block.  Using blocking columns is very useful when you are processing very big data. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Multiple output | Select the Separate output check box to have several output flows:  * Uniques: when the group size   is equal to *1*, the record is listed in this   flow. When records are not unique, they can be: * Matches: when the   group quality is greater than or equal to the threshold   you define in the Confident match   threshold field, the record is listed   in this flow. * Suspects: when the group quality   is less than the threshold you define in the Confident match   threshold field, the record is listed in   this flow.  Confident match threshold: set a numerical value between the current Match threshold and *1*. From this threshold, you can be confident in the quality of the group. |
| Multi-pass | Select this check box to enable a tMatchGroup  component to receive data sets from another tMatchGroup  that precedes it in the Job. This will refine the groups received by each of the tMatchGroup components through creating data partitions based on different blocking keys.  With multi-pass matching, all master records are generated but intermediate master records are removed from the output flow. Only final master and original records are kept at the end.  When single master records from the 1st tMatchGroup merge into one group after passing the 2nd tMatchGroup, their order in the group may change every time you run the Job.  For an example Job, see [Matching customer data through multiple passes](/talend/en-US/data-matching/8.0/matching-customer-data-through-multiple-passes). |
| Sort the output data by GID | Select this check box to group the output data by the group identifier.  The output is sorted in descending alphanumeric order by group identifier. |
| Output distance details | Select this check box to add an output column *MATCHING\_DISTANCES* in the schema of the component. This column provides the distance between the input and master records in each group.  Information noteImportant: When you use two tMatchGroup components in a Job and select this option in one component, you must select this check box in both tMatchGroup components before linking them together. If you linked the components before selecting this check box, select this check box in the second component in the Job flow and then, in the first component. Otherwise, you may have an issue as there are two columns in the output schema with the same name. Selecting this check box in only one tMatchGroup component may cause schema mismatch issues. |
| Display detailed labels | This checkbox is available when Output distance details is selected.  Select this check box to have in the output *MATCHING\_DISTANCES* column not only the matching distance but also the names of the columns used as key attributes in the applied rule.  For example, if you try to match on first name and last name fields, *lname* and *fname*, the output would be fname:1.0|lname:0.97 when the check box is selected and 1.0|0.97 when it is not selected. |
| Deactivate matching computation when opening the wizard | Select this check box to open the Configuration wizard without running the match rules defined in the wizard.  This enables you to have a better experience with the component. Otherwise, the wizard may take some time to open. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is cleared, if the component has this check box.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediary step. It requires an input flow as well as an output flow. |

## Matching algorithms

This list describes each matching algorithm from the Matching
Function column:

* Exact: Matches each processed
  entry to all possible reference entries with exactly the same value. It returns
  *1* when the two strings exactly match, otherwise it
  returns *0*.
* Exact - ignore case: Matches each
  processed entry to all possible reference entries with exactly the same value
  while ignoring the value case.
* Soundex: Matches processed entries
  according to a standard English phonetic algorithm. It indexes strings by sound,
  as pronounced in English, for example "Hello": "H400".It does not support Chinese characters.
* Levenshtein (edit distance): Calculates
  the minimum number of edits (insertion, deletion, or substitution) required to
  transform one string into another. Using this algorithm in the tMatchGroup  component, you do not need to
  specify a maximum distance. The component automatically calculates a matching
  percentage based on the distance. This matching score will be used for the
  global matching calculation, based on the weight you assign in the Confidence Weight field.
* Metaphone: Based on a phonetic algorithm for
  indexing entries by their pronunciation. It first loads the phonetics of all entries
  of the lookup reference and checks all entries of the main flow against the entries
  of the reference flow. It does not support Chinese characters.
* Double Metaphone: A new version of the
  Metaphone phonetic algorithm, that produces more accurate results than the
  original algorithm. It can return both a primary and a secondary code for a
  string. This accounts for some ambiguous cases as well as for multiple variants
  of surnames with common ancestry. It does not support Chinese characters.
* Soundex FR: Matches processed entries
  according to a standard French phonetic algorithm.It does not support Chinese characters.
* Jaro: Matches processed entries according
  to spelling deviations. It counts the number of matched characters between two
  strings. The higher the distance is, the more similar the strings are.
* Jaro-Winkler: A variant of Jaro, but it
  gives more importance to the beginning of the string.
* Fingerprint key: Matches entries after
  doing the following sequential process:
  1. Remove leading and trailing whitespace.
  2. Change all characters to their lowercase representation.
     It does not support Chinese characters.
  3. Remove all punctuation and control characters.
  4. Split the string into whitespace-separated tokens.
  5. Sort the tokens and remove duplicates.
  6. Join the tokens back together. Because the string parts
     are sorted, the given order of tokens does not matter. So, *Cruise, Tom* and *Tom
     Cruise* both end up with a fingerprint *cruise
     tom* and therefore end up in the same cluster.
  7. Normalize extended western characters to their ASCII
     representation, for example *gödel* to *godel*. This reproduces data entry mistakes
     performed when entering extended characters with an ASCII-only keyboard.
     However, this procedure can also lead to false positives, for example *gödel* and *godél* would
     both end up with *godel* as their fingerprint but
     they are likely to be different names. So this might work less
     effectively for datasets where extended characters play substantial
     differentiation role.
* q-grams: Matches processed entries by
  dividing strings into letter blocks of length q
  in order to create a number of q length grams.
  The matching result is given as the number of q-gram matches over possible
  q-grams.
* Hamming: Calculates the minimum number of
  substitutions required to transform one string into another string having the
  same length. For example, the Hamming distance between "masking"
  and "pairing" is 3.
* custom...: Lets you load an external
  matching algorithm from a Java library using the custom Matcher column.

For further information about how to load an external Java library, see
[tLibraryLoad](/talend/en-US/components/8.0/library-import/tlibraryload).

For further information about how to
create a custom matching algorithm, see [Creating a custom matching algorithm](/talend/en-US/data-matching/8.0/creating-custom-matching-algorithm).

For a related scenario about how to use a custom matching algorithm,
see [Using a custom matching algorithm to match entries](/talend/en-US/data-matching/8.0/using-custom-matching-algorithm-to-match-entries).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-matching/tmatchgroup-standard-properties -->
# tMatchGroup Standard properties

Last updated: 9/30/2026

These properties are used to configure
tMatchGroup running in the Standard Job framework.

The Standard
tMatchGroup
component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  The output schema of this component contains   the following read-only fields:    + `GID`: Provides a group     identifier of the data type *String*.  Information noteNote: In Jobs migrated from previous releases to your current     Talend Studio, the group identifier may be of the Long data type. To have a group     identifier of the String data type, replace the     tMatchGroup components in the migrated Jobs with     tMatchGroup components from the Palette.   + `GRP_SIZE`: Counts the     number of records in the group, computed only on the master record.   + `MASTER`: Identifies, by     true or false, if the record used in the matching comparisons is a     master record. There is only one master record per group. Each input record     will be compared to the master record, if they match, the input record will     be in the group.   + `SCORE`: Measures the     distance between the input record and the master record according to the     matching algorithm used. In case the tMatchGroup component is used to have multiple output     flows, the score in this column decides to what output group the record     should go.   + `GRP_QUALITY` depends     on the Matching Algorithm:     - Simple VSR: `GRP_QUALITY` provides the       quality of similarities in the group by taking the minimal       matching value. Only the master record has a quality       score.     - T-Swoosh:       `GRP_QUALITY` provides the quality of       similarities in the group by taking the minimal matching value among       all record pairs of the group. Only the master record has a quality       score.   + `MERGED_RECORD`: this output column is available     only:     - When you have more than one tMatchGroup component in the Job and     - When the T-Swoosh algorithm is selected. The column explains with *true* or *false* if the record is respectively a master     record or not a master record in the first pass. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Matching Algorithm | Select from the list the algorithm you want to use in the component: Simple VSR or T-Swoosh. |
|  | Click the import icon to import a match rule from the Talend Studio repository.  In the Match Rule Selector wizard, import a match rule with the same algorithm as the selected matching algorithm in the basic settings of the component. Otherwise, the Job runs with default values for the parameters which are not compatible between the Simple VSR and the T-Swoosh algorithms.  For further information about how to import rules, see [Importing match rules from the repository](/talend/en-US/data-matching/8.0/importing-match-rules-from-studio-repository) |
| Key Definition - Input Key Attribute column | Select the columns from the input flow on which you want to apply a matching algorithm.  Information noteNote: When you select a date column on which to apply an algorithm or a matching algorithm, you can decide what to compare in the date format. For example, if you want to only compare the year in the date, in the component schema set the type of the date column to Date and then enter "*yyyy*" in the Date Pattern field. The component then converts the date format to a string according to the pattern defined in the schema before starting a string comparison. |
| Key Definition - Matching Function column | Select a matching algorithm from the list. For more information on each algorithm, see [Matching algorithms](#matching-algorithms-section). |
| Key Definition - Custom Matcher Class column | When you select Custom as the matching type, enter the path pointing to the custom class (external matching algorithm) you need to use. This path is defined by yourself in the library file (*.jar* file) which you can import by using the tLibraryLoad component.  For example, to use a *MyDistance.class* class stored in the directory *org/talend/mydistance* in a user-defined *mydistance.jar* library, the path to be entered is *org.talend.mydistance.MyDistance*. |
| Key Definition - Tokenized measure column | Tokenization is the concept of splitting a string into words. Select the method to use to compute a tokenized measure for the selected algorithm:  * No: No tokenization method is used on the   string. With this option, "John Doe" and "Jon Doe" should   match. * Same place: Splits the two strings by words   to two lists, list1 and list2. Associates each element from list1   with the element which has the same position in list2. Using this   method, "She is red and he is pink" and "Catherine is red and he is   pink" should match. * Same order: Splits the two strings by words   to two lists, list1 and list2 and assumes that list1 is shorter than   list2. Tries to associate the elements from list1 with the elements   in list2 taken in the same order. Using this method, "John Doe" and   "John B. Doe" match. * This method should be used only with strings which has a few words,   otherwise the number of possible combinations can be large. * Any order: Splits the two strings by words to   two lists, list1 and list2 and assumes that list1 is shorter than   list2. Tries to assign each word of list1 to a word of list2, in   order to have the highest global similarity (with respect to the   used similarity). Using this method, "John Doe" and "Doe John"   match. |
| Key Definition - Threshold column | This column is displayed when you selected T-Swoosh as the matching algorithm.  Two data records match when the probability is greater than or equal to the set value.  Set a threshold between *0* and *1*. You can enter up to 6 decimals.  *0* means that the similarity between values in the column is not measured. *1* means that you want each two compared values of the column to exactly match. Default value is *1*. |
| Key Definition - Confidence Weight column | Set a numerical weight for each attribute (column) of the key definition.  You can enter a number or a context variable.  The value must be an integer greater than 0. |
| Key Definition - Handle Null column | To handle null values, select from the list the null operator you want to use on the column:  Null Match Null: A Null attribute only matches another Null attribute.  Null Match NONE: A Null attribute never matches another attribute.  Null Match ALL: A Null attribute matches any other value of an attribute.  For example, two columns, *name* and *firstname* where the name is never null, but the first name can be null.  If two records:  "Doe", "John"  "Doe", ""  Depending on the operator you choose, these two records may or may not match:  Null Match Null: They do not match.  Null Match NONE: They do not match.  Null Match ALL: They match.  For the records:  "Doe", ""  "Doe", ""  Null Match Null: They match.  Null Match NONE: They do not match.  Null Match ALL: They match. |
| Key Definition - Survivorship Function column | This column is available when the T-Swoosh algorithm is selected.  Select how two similar records will be merged from the drop-down list.   * Concatenate: This function adds the content of the   first record and the content of the second record together. For example,   `Bill` and `William` will be   merged into `BillWilliam`. In the   Parameter field, you can specify a separator to be   used to separate values. * Prefer True (for   booleans): This function always set booleans to True   in the merged record, unless all booleans in the source records are   False. * Prefer False (for   booleans): This function always sets booleans to   False in the merged record, unless all booleans in the source   records are True. * Most   common: This function validates the most   frequently-occurring field value in each group of duplicate   records. * Most   recent: This function validates the latest date value in   each group of duplicate records. If more than one date type is   defined in the schema, select a column in Reference column. If no date type   is defined in the schema, the data are sorted into most recent   loading order. * Most   ancient: This function validates the earliest date   value in each group of duplicate records. If more than one date type   is defined in the schema, select a column in Reference column. If no date type   is defined in the schema, the data are sorted into most ancient   loading order. * Longest (for   strings): This function validates the longest field   value in each group of duplicate records. * Shortest (for   strings): This function validates the shortest field   value in each group of duplicate records. * Largest (for   numbers): This function validates the largest   numerical value in each group of duplicate records. * Smallest (for   numbers): This function validates the smallest   numerical value in each group of duplicate records. * Most trusted source: This function takes the data   coming from the source which has been defined as being most trustworthy. The   most trusted data source is set in the Parameter   field. |
| Key Definition - Reference column column | If you set Survivor Function to Most recent or Most ancient, this column is used to select the reference column. |
| Key Definition - Parameter column | If you set Survivorship Function to Most trusted source, this item is used to set the name of the data source you want to use as a base for the master record.  If you set Survivorship Function to Concatenate, this item is used to specify a separator you want to use for concatenating data. |
| Match Threshold | Enter the match probability. Two data records match when the probability is greater than or equal to the set value.  You can enter a different match threshold for each match rule. |
| Survivorship Rules For Columns | This setting is available when the T-Swoosh algorithm is selected. Input Column: Select the columns from the input flow on which you want to apply a survivorship function.  Survivorship Function: Select how two similar records will be merged from the drop-down list. |
| Default Survivorship Rules | This setting is available when the T-Swoosh algorithm is selected. Input Column: Select the columns from the input flow on which you want to apply a survivorship function.  Survivorship Function: Select how two similar records will be merged from the drop-down list. |
| Blocking Selection | If required, select the columns from the input flow according to which you want to partition the processed data in blocks, this is usually referred to as "blocking".  Blocking reduces the number of pairs of records that needs to be examined. In blocking, input data is partitioned into exhaustive blocks designed to increase the proportion of matches observed while decreasing the number of pairs to compare. Comparisons are restricted to record pairs within each block.  Using blocking columns is very useful when you are processing very big data. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Store on disk | Select the Store on disk check box if you want to store processed data blocks on the disk to maximize system performance.  Max buffer size: Type in the size of physical memory you want to allocate to processed data.  Temporary data directory path: Set the location where the temporary file should be stored. |
| Multiple output | Select the Separate output check box to have several output flows:  * Uniques: when the group size   is equal to *1*, the record is listed in this   flow. When records are not unique, they can be: * Matches: when the   group quality is greater than or equal to the threshold   you define in the Confident match   threshold field, the record is listed   in this flow. * Suspects: when the group quality   is less than the threshold you define in the Confident match   threshold field, the record is listed in   this flow.  Information noteNote: When using the Simple VSR algorithm, the group quality is the minimal distance computed in the record.  When using the T-Swoosh algorithm, the group quality is the minimal distance computed among all record pairs of the group.  Confident match threshold: set a numerical value between the current Match threshold and *1*. From this threshold, you can be confident in the quality of the group. |
| Multi-pass | Select this check box to enable a tMatchGroup  component to receive data sets from another tMatchGroup  that precedes it in the Job. This will refine the groups received by each of the tMatchGroup components through creating data partitions based on different blocking keys.  With multi-pass matching, all master records are generated but intermediate master records are removed from the output flow. Only final master and original records are kept at the end.  When single master records from the 1st tMatchGroup merge into one group after passing the 2nd tMatchGroup, their order in the group may change every time you run the Job.  For an example Job, see [Matching customer data through multiple passes](/talend/en-US/data-matching/8.0/matching-customer-data-through-multiple-passes).  Propagate original values: This option is available only with the T-Swoosh algorithm. Select this check box to allow the original records from each pass (and not only the unmatched records) to also be considered in the second pass of matching, both against each other and against the survived masters. This helps to make sure that no matches are missed. |
| Sort the output data by GID | Select this check box to group the output data by the group identifier.  The output is sorted in descending alphanumeric order by group identifier. |
| Output distance details | Select this check box to add an output column *MATCHING\_DISTANCES* in the schema of the component. This column provides the distance between the input and master records in each group.  Information noteImportant: When you use two tMatchGroup components in a Job and select this option in one component, you must select this check box in both tMatchGroup components before linking them together. If you linked the components before selecting this check box, select this check box in the second component in the Job flow and then, in the first component. Otherwise, you may have an issue as there are two columns in the output schema with the same name. Selecting this check box in only one tMatchGroup component may cause schema mismatch issues. |
| Display detailed labels | This checkbox is available when Output distance details is selected.  Select this check box to have in the output *MATCHING\_DISTANCES* column not only the matching distance but also the names of the columns used as key attributes in the applied rule.  For example, if you try to match on first name and last name fields, *lname* and *fname*, the output would be fname:1.0|lname:0.97 when the check box is selected and 1.0|0.97 when it is not selected. |
| Deactivate matching computation when opening the wizard | Select this check box to open the Configuration wizard without running the match rules defined in the wizard.  This enables you to have a better experience with the component. Otherwise, the wizard may take some time to open. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is cleared, if the component has this check box.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediary step. It requires an input flow as well as an output flow. |

## Matching algorithms

This list describes each matching algorithm from the Matching
Function column:

* Exact: Matches each processed
  entry to all possible reference entries with exactly the same value. It returns
  *1* when the two strings exactly match, otherwise it
  returns *0*.
* Exact - ignore case: Matches each
  processed entry to all possible reference entries with exactly the same value
  while ignoring the value case.
* Soundex: Matches processed entries
  according to a standard English phonetic algorithm. It indexes strings by sound,
  as pronounced in English, for example "Hello": "H400".It does not support Chinese characters.
* Levenshtein (edit distance): Calculates
  the minimum number of edits (insertion, deletion, or substitution) required to
  transform one string into another. Using this algorithm in the tMatchGroup  component, you do not need to
  specify a maximum distance. The component automatically calculates a matching
  percentage based on the distance. This matching score will be used for the
  global matching calculation, based on the weight you assign in the Confidence Weight field.
* Metaphone: Based on a phonetic algorithm for
  indexing entries by their pronunciation. It first loads the phonetics of all entries
  of the lookup reference and checks all entries of the main flow against the entries
  of the reference flow. It does not support Chinese characters.
* Double Metaphone: A new version of the
  Metaphone phonetic algorithm, that produces more accurate results than the
  original algorithm. It can return both a primary and a secondary code for a
  string. This accounts for some ambiguous cases as well as for multiple variants
  of surnames with common ancestry. It does not support Chinese characters.
* Soundex FR: Matches processed entries
  according to a standard French phonetic algorithm.It does not support Chinese characters.
* Jaro: Matches processed entries according
  to spelling deviations. It counts the number of matched characters between two
  strings. The higher the distance is, the more similar the strings are.
* Jaro-Winkler: A variant of Jaro, but it
  gives more importance to the beginning of the string.
* Fingerprint key: Matches entries after
  doing the following sequential process:
  1. Remove leading and trailing whitespace.
  2. Change all characters to their lowercase representation.
     It does not support Chinese characters.
  3. Remove all punctuation and control characters.
  4. Split the string into whitespace-separated tokens.
  5. Sort the tokens and remove duplicates.
  6. Join the tokens back together. Because the string parts
     are sorted, the given order of tokens does not matter. So, *Cruise, Tom* and *Tom
     Cruise* both end up with a fingerprint *cruise
     tom* and therefore end up in the same cluster.
  7. Normalize extended western characters to their ASCII
     representation, for example *gödel* to *godel*. This reproduces data entry mistakes
     performed when entering extended characters with an ASCII-only keyboard.
     However, this procedure can also lead to false positives, for example *gödel* and *godél* would
     both end up with *godel* as their fingerprint but
     they are likely to be different names. So this might work less
     effectively for datasets where extended characters play substantial
     differentiation role.
* q-grams: Matches processed entries by
  dividing strings into letter blocks of length q
  in order to create a number of q length grams.
  The matching result is given as the number of q-gram matches over possible
  q-grams.
* Hamming: Calculates the minimum number of
  substitutions required to transform one string into another string having the
  same length. For example, the Hamming distance between "masking"
  and "pairing" is 3.
* custom...: Lets you load an external
  matching algorithm from a Java library using the custom Matcher column.

For further information about how to load an external Java library, see
[tLibraryLoad](/talend/en-US/components/8.0/library-import/tlibraryload).

For further information about how to
create a custom matching algorithm, see [Creating a custom matching algorithm](/talend/en-US/data-matching/8.0/creating-custom-matching-algorithm).

For a related scenario about how to use a custom matching algorithm,
see [Using a custom matching algorithm to match entries](/talend/en-US/data-matching/8.0/using-custom-matching-algorithm-to-match-entries).
