<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow · versión 8.0 -->
# tFilterRow

Last updated: 9/30/2026

Filters input rows by setting one or more conditions on the selected
columns.

### In this section

* [tFilterRow Standard properties](/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
* [tFilterRow properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/tfilterrow-properties-for-apache-spark-batch)
* [tFilterRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/tfilterrow-properties-for-apache-spark-streaming)
* [tFilterRow properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/processing/tfilterrow-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Filtering a list of names through different logical operations](tfilterrow-filtering-list-of-names-through-different-logical-operations-standard-component "Based on the previous scenario, this scenario further filters the input data so that only those records of people from New York and Chicago are accepted. Without changing the filter settings defined in the previous scenario, advanced conditions are added in this scenario to enable both logical AND and logical OR operations in the same tFilterRow component.")
* [Filtering a list of names using simple conditions](tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-filtering-list-of-names-using-simple-conditions-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-filtering-list-of-names-through-different-logical-operations-standard-component -->
# Filtering a list of names through different logical operations

Last updated: 9/30/2026

Based on the previous scenario, this scenario further filters the input data so that
only those records of people from New York and Chicago are accepted. Without changing
the filter settings defined in the previous scenario, advanced conditions are added in
this scenario to enable both logical AND and logical OR operations in the same tFilterRow component.

### In this section

* [Procedure](/talend/en-US/components/8.0/processing/tfilterrow-procedure-standard-component)

**Related concepts**  

* [tFilterRow](tfilterrow "Filters input rows by setting one or more conditions on the selected columns.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-properties-for-apache-spark-batch -->
# tFilterRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFilterRow running in the Spark Batch Job framework.

The Spark Batch
tFilterRow component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields. |
| Logical operator used to combine conditions | Select a logical operator to combine simple conditions and to combine the filter results of both modes if any advanced conditions are defined.  And: returns the boolean value of *true* if all conditions are true; otherwise *false*. For each two conditions combined using a logical AND, the second condition is evaluated only if the first condition is evaluated to be true.  Or: returns the boolean value of *true* if any condition is true; otherwise *false*. For each two conditions combined using a logical OR, the second condition is evaluated only if the first condition is evaluated to be false. |
| Conditions | Click the plus button to add as many simple conditions as needed. Based on the logical operator selected, the conditions are evaluated one after the other in sequential order for each row. When evaluated, each condition returns the boolean value of *true* or *false*.  Input column: Select the column of the schema the function is to be operated on  Function: Select the function on the list  Operator: Select the operator to bind the input column with the value  Value: Type in the filtered value, between quotes if needed. |
| Use advanced mode | Select this check box when the operations you want to perform cannot be carried out through the standard functions offered, for example, different logical operations in the same component. In the text field, type in the regular expression as required.  If multiple advanced conditions are defined, use a logical operator between two conditions:  && (logical AND): returns the boolean value of *true* if both conditions are true; otherwise *false*. The second condition is evaluated only if the first condition is evaluated to be true.  || (logical OR): returns the boolean value of *true* if either condition is true; otherwise *false*. The second condition is evaluated only if the first condition is evaluated to be false. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-properties-for-apache-spark-structured-streaming -->
# tFilterRow properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tFilterRow running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tFilterRow component belongs to the Processing family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Logical operator used to combine conditions | Select a logical operator to combine simple conditions and the filter results of both modes when you define advanced conditions. And: Returns true if all conditions are true; otherwise false. The second condition is evaluated only if the first is true.  Or: Returns true if any condition is true; otherwise false. The second condition is evaluated only if the first is false. |
| Conditions | Click + to add simple conditions. Based on the selected logical operator, the component evaluates conditions sequentially for each row and returns true or false. Input column: Select the schema column to apply the function to.  Function: Select the function from the list.  Operator: Select the operator to bind the input column with the value.  Value: Enter the filter value, in quotation marks if required. |
| Use advanced mode | Select this check box when standard functions cannot perform the required operations. Enter a regular expression in the text field. If multiple advanced conditions are defined, use a logical operator to combine conditions:  && (logical AND): Returns true if both conditions are true. The second condition is evaluated only if the first is true.  || (logical OR): Returns true if either condition is true. The second condition is evaluated only if the first is false. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties -->
# tFilterRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tFilterRow running in the Standard Job framework.

The Standard
tFilterRow component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is built-in only.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Logical operator used to combine conditions | Select a logical operator to combine simple conditions and to combine the filter results of both modes if any advanced conditions are defined.  And: returns the boolean value of *true* if all conditions are true; otherwise *false*. For each two conditions combined using a logical AND, the second condition is evaluated only if the first condition is evaluated to be true.  Or: returns the boolean value of *true* if any condition is true; otherwise *false*. For each two conditions combined using a logical OR, the second condition is evaluated only if the first condition is evaluated to be false. |
| Conditions | Click the plus button to add as many simple conditions as needed. Based on the logical operator selected, the conditions are evaluated one after the other in sequential order for each row. When evaluated, each condition returns the boolean value of *true* or *false*.  Input column: Select the column of the schema the function is to be operated on  Function: Select the function on the list  Operator: Select the operator to bind the input column with the value  Value: Type in the filtered value, between quotes if needed. |
| Use advanced mode | Select this check box when the operations you want to perform cannot be carried out through the standard functions offered, for example, different logical operations in the same component. In the text field, type in the regular expression as required.  If multiple advanced conditions are defined, use a logical operator between two conditions:  && (logical AND): returns the boolean value of *true* if both conditions are true; otherwise *false*. The second condition is evaluated only if the first condition is evaluated to be true.  || (logical OR): returns the boolean value of *true* if either condition is true; otherwise *false*. The second condition is evaluated only if the first condition is evaluated to be false. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_OK: the number of rows matching the filter. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is not startable (green background) and it requires an output component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-filtering-list-of-names-using-simple-conditions-standard-component-the -->
# Filtering a list of names using simple conditions

Last updated: 9/30/2026

The following scenario shows a Job that uses simple conditions to filter a list of
records. This scenario will output two tables: the first will list all male persons with
a last name shorter than nine characters and aged between 10 and 80 years; the second
will list all rejected records. An error message for each rejected record will display
in the same table to explain why such a record has been rejected.

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/processing/tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/processing/tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/processing/tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-executing-job-standard-component-save)

**Related concepts**  

* [tFilterRow](tfilterrow "Filters input rows by setting one or more conditions on the selected columns.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-procedure-standard-component -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Double-click the tFilterRow component to show
   its Basic settings view.
2. Select the Use advanced mode check box, and
   type in the following expression in the text field:

   ```
   input_row.City.equals("Chicago") || input_row.City.equals("New York")
   ```

   This defines two conditions on the *City*
   column of the input data to filter records that contain the cities of Chicago
   and New York, and uses a logical OR to combine the two conditions so that
   records satisfying either condition will be accepted.
3. Press Ctrl+S to save the Job and press
   F6 to execute it.

   As shown above, the result list of the previous scenario has been further
   filtered, and only the records containing the cities of New York and Chicago are
   accepted.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display
   its Basic settings view and define its
   properties.
2. Click the [...] button next to Edit schema to define the schema for the input
   data. In this example, the schema is made of the following four columns:
   *LastName* (type String), *Gender*
   (type String), *Age* (type Integer) and
   *City* (type String). 

   When done, click OK to validate the
   schema setting and close the dialog box. A new dialog box opens and asks you
   if you want to propagate the schema. Click Yes.
3. Set the row and field separators in the corresponding fields if needed. In
   this example, use the default settings for both, namely the row separator is
   a carriage return and the field separator is a semi-colon.
4. Select the Use Inline Content(delimited
   file) option in the Mode
   area and type in the input data in the Content field.

   The input data used in this example is shown
   below:

   ```
   Van Buren;M;73;Chicago
   Adams;M;40;Albany
   Jefferson;F;66;New York
   Adams;M;9;Albany
   Jefferson;M;30;Chicago
   Carter;F;26;Chicago
   Harrison;M;40;New York
   Roosevelt;F;15;Chicago
   Monroe;M;8;Boston
   Arthur;M;20;Albany
   Pierce;M;18;New York
   Quincy;F;83;Albany
   McKinley;M;70;Boston
   Coolidge;M;4;Chicago
   Monroe;M;60;Chicago
   ```
5. Double-click tFilterRow to display its
   Basic settings view and define its
   properties.
6. In the Conditions table, add four
   conditions and fill in the filtering parameters. 
   * From the InputColumn list field
     of the first row, select *LastName*, from the
     Function list field, select
     Length, from the Operator list field, select Lower than, and in the Value column, type in
     *9* to limit the length of last names to nine
     characters.
   * From the InputColumn list field
     of the second row, select *Gender*, from the
     Operator list field, select
     Equals, and in the Value column, type in
     *M* in double quotes to filter records of
     male persons.

     Information noteWarning:

     In the Value field, you must
     type in your values between double quotes for all types of
     values, except for integer values, which do not need
     quotes.
   * From the InputColumn list field
     of the third row, select *Age*, from the
     Operator list field, select
     Greater than, and in the
     Value column, type in
     *10* to set the lower limit to 10
     years.
   * From the InputColumn list field
     of the four row, select *Age*, from the Operator list field, select Lower than, and in the Value column, type in
     *80* to set the upper limit to 80
     years.
7. To combine the conditions, select And as
   that only those records that meet all the defined conditions are
   accepted.
8. In the Basic settings of tLogRow components, select Table (print values in cells of a table) in the Mode area.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. Drop tFixedFlowInput, tFilterRow and tLogRow from the Palette
   onto the design workspace.
2. Connect the tFixedFlowInput to the
   tFilterRow, using a Row > Main
   link. Then, connect the tFilterRow to the
   tLogRow, using a Row > Filter
   link.
3. Drop tLogRow from the Palette onto the design workspace and rename it
   as *reject*. Then, connect the tFilterRow to the *reject*, using a
   Row > Reject link.
4. Label the components to better identify their roles in the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-tlogrow-tfixedflowinput-tfixedflowinput-executing-job-standard-component-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Save your Job and press F6 to execute
it.

As shown above, the first table lists the records of male persons aged
between 10 and 80 years, whose last names are made up of less than nine
characters, and the second table lists all the records that do not match the
filter conditions. Each rejected record has a corresponding error message
that explains the reason of rejection.
