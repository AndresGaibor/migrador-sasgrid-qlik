<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tdenormalize · versión 8.0 -->
# tDenormalize

Last updated: 9/30/2026

Denormalizes the input flow based on one column.

### In this section

* [tDenormalize Standard properties](/talend/en-US/components/8.0/processing/tdenormalize-standard-properties)
* [tDenormalize properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/tdenormalize-properties-for-apache-spark-batch)
* [tDenormalize properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/tdenormalize-properties-for-apache-spark-streaming)

**Related concepts**  

* [Denormalizing multiple columns](tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-multiple-columns-this)
* [Denormalizing one column](tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-one-column-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tdenormalize-properties-for-apache-spark-batch -->
# tDenormalize properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDenormalize running in the Spark Batch Job framework.

The Spark Batch
tDenormalize component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| To denormalize | In this table, define the parameters used to denormalize your columns.  Column: Select the column to denormalize.  Delimiter: Type in the separator you want to use to denormalize your data between double quotes.  Merge same value: Select this check box to merge identical values. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tdenormalize-standard-properties -->
# tDenormalize Standard properties

Last updated: 9/30/2026

These properties are used to configure tDenormalize running in the Standard Job framework.

The Standard
tDenormalize component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| To denormalize | In this table, define the parameters used to denormalize your columns.  * Column: Select the column to   denormalize. * Delimiter: Type in the separator you   want to use to denormalize your data between double quotes. * Merge same value: Select this check   box to merge identical values. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Null value as an empty string in concatenation | Select this check box to convert null values to empty strings. If an input column in the To denormalize table is null, and the column output type is "String", the null value is replaced with an empty string. |
| tStatCatcher Statistics | Select this check box to collect the log data at component level. Note that this check box is not available in the Map/Reduce version of the component. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as intermediate step in a data flow. |
| Limitation | Note that this component may change the order in the incoming Java flow. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-multiple-columns-this -->
# Denormalizing multiple columns

Last updated: 9/30/2026

This scenario illustrates a Job denormalizing two columns from a delimited
file.

### In this section

* [Denormalizing on multiple columns](/talend/en-US/components/8.0/processing/tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-multiple-columns-standard-component-drop)

**Related concepts**  

* [tDenormalize](tdenormalize "Denormalizes the input flow based on one column.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-one-column-this -->
# Denormalizing one column

Last updated: 9/30/2026

This scenario illustrates a Job denormalizing one column in a delimited
file.

### In this section

* [Denormalizing on one column](/talend/en-US/components/8.0/processing/tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-one-column-standard-component-drop)

**Related concepts**  

* [tDenormalize](tdenormalize "Denormalizes the input flow based on one column.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-multiple-columns-standard-component-drop -->
# Denormalizing on multiple columns

Last updated: 9/30/2026

## Procedure

1. Drop the following components: tFileInputDelimited, tDenormalize, tLogRow
   from the Palette to the design
   workspace.
2. Connect all components using a Row
   main connection.
3. On the tFileInputDelimited
   Basic settings panel, set the filepath to
   the file to be denormalized.
4. Define the Row and
   Field 
   separators, the Header and other information if required.
5. The file schema is made of four columns including: Name, FirstName,
   HomeCity, WorkCity.

   ```
   Name;FirstName;HomeCity;WorkCity
   Pitt;Brad;Berverly Hills;Los Angeles
   Pitt;Brad;Paris;London
   Joli;Angelina;Berlin;Berlin
   Joli;Angelina;Berlin;Los Angeles
   Joli;Angelina;Los Angeles;Los Angeles
   Willis;Bruce;Paris;Los Angeles
   Willis;Bruce;Paris;Madrid
   Willis;Bruce;Madrid;Paris
   Willis;Bruce;Roma;Dublin
   Moore;Demi;New York;Paris
   Moore;Demi;Rio de Janeiro;Los Angeles
   ```
6. In the tDenormalize
   component Basic settings, select the columns
   that contain the repetition.

   These are the column which are meant to occur multiple times in the document. In
   this example, *FirstName*, *HomeCity* and
   *WorkCity* are the columns against which the denormalization
   is performed.
7. Click the  to add rows and define the columns to denormalize.
8. In the Delimiter column,
   define the separator between double quotes, to split concatenated values.
9. Save your Job and press F6 to execute it.

   The denormalized values are concatenated using a semicolon.

   ```
   |=-----+--------------------------+-------------------------+------------------------------=|
   |Name  |FirstName                 |HomeCity                 |WorkCity                       |
   |=-----+--------------------------+-------------------------+------------------------------=|
   |Joli  |Angelina;Angelina;Angelina|Berlin;Berlin;Los Angeles|Berlin;Los Angeles;Los Angeles |
   |Moore |Demi;Demi                 |New York;Rio de Janeiro  |Paris;Los Angeles              |
   |Willis|Bruce;Bruce;Bruce;Bruce   |Paris;Paris;Madrid;Roma  |Los Angeles;Madrid;Paris;Dublin|
   |Pitt  |Brad;Brad                 |Berverly Hills;Paris     |Los Angeles;London             |
   '------+--------------------------+-------------------------+-------------------------------'
   ```
10. To delete the duplicate occurrences, open the Basic
    settings of tDenormalize.
11. Select the Merge same value check
    box.
12. Save your Job again and press F6 to execute it.

## Results

The duplicate occurrences are
merged.

```
|=-----+---------+-----------------------+------------------------------=|
|Name  |FirstName|HomeCity               |WorkCity                       |
|=-----+---------+-----------------------+------------------------------=|
|Joli  |Angelina |Berlin;Los Angeles     |Berlin;Los Angeles             |
|Moore |Demi     |New York;Rio de Janeiro|Paris;Los Angeles              |
|Willis|Bruce    |Paris;Madrid;Roma      |Los Angeles;Madrid;Paris;Dublin|
|Pitt  |Brad     |Berverly Hills;Paris   |Los Angeles;London             |
'------+---------+-----------------------+-------------------------------'
```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tdenormalize-tfileinputdelimited-tlogrow-tlogrow-denormalizing-on-one-column-standard-component-drop -->
# Denormalizing on one column

Last updated: 9/30/2026

## Procedure

1. Drop the following components: tFileInputDelimited, tDenormalize, tLogRow
   from the Palette to the design
   workspace.
2. Connect the components using Row
   main connections.
3. On the tFileInputDelimited 
   Component view, set the filepath to the
   file to be denormalized.
4. Define the Header,
   Row Separator and Field Separator parameters.
5. The input file schema is made of two columns, *Parents* and *Children*.

   ```
   Parents;Children
   Peter;John
   William;Mary
   Kate;Jack
   Chris;Liz
   Peter;Michael
   Kate;Caroline
   ```
6. In the Basic settings of
   tDenormalize, define the column that
   contains multiple values to be grouped.
7. In this example, the column to denormalize is *Children*.
8. Set the Delimiter to
   separate the grouped values.
9. Select the Merge same
   value check box, if you know that some values to be grouped are
   strictly identical.
10. Save your Job and press F6 to execute it.

## Results

All values from the column *Children* are grouped
by their *Parents* column.

```
|Parents|Children     |
|=------+------------=|
|Kate   |Jack;Caroline|
|Chris  |Liz          |
|Peter  |John;Michael |
|William|Mary
```
