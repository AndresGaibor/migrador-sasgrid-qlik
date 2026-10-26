<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap · versión 8.0 -->
# tMap

Last updated: 9/30/2026

### In this section

* [tMap component](/talend/en-US/components/8.0/tmap/tmap-component)
* [tMap scenarios](/talend/en-US/components/8.0/tmap/tmap-scenario)
* [tMap related topics](/talend/en-US/components/8.0/tmap/tmap-other)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-component -->
# tMap component

Last updated: 9/30/2026

| [tMap](/talend/en-US/components/8.0/tmap/tmap) | Transforms and routes data from single or multiple sources to single or multiple destinations. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap -->
# tMap

Last updated: 9/30/2026

Transforms and routes data from single or multiple sources to single or multiple
destinations.

tMap is an advanced component, which integrates itself as plugin to
Talend Studio.

Information noteTip:

There is no order among the output flows of
tMap. To make the output flows to be executed one by one,
you can output them to temporary files or memory, and then read and insert them into
files or databases using different subJobs linked by Trigger > OnSubjobOK connections.

### In this section

* [tMap Standard properties](/talend/en-US/components/8.0/tmap/tmap-standard-properties)
* [tMap properties for Apache Spark Batch](/talend/en-US/components/8.0/tmap/tmap-properties-for-apache-spark-batch)
* [tMap properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/tmap/tmap-properties-for-apache-spark-streaming)
* [tMap properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/tmap/tmap-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Mapping data using a filter and a simple explicit join](tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-mapping-data-using-filter-and-simple-explicit-join-standard-component-the-job)

**Related tasks**  

* [Advanced mapping with lookup reload at each row](tmap-tmysqlinput-tmysqloutput-tmysqlcommit-advanced-mapping-with-lookup-reload-at-each-row-standard-component-the)
* [Converting a UNIX timestamp to a readable date](converting-a-unix-timestamp-to-a-readable-date "A Unix timestamp is a series of numbers non-human readable such as 13959.583,1330578363. This scenario shows how to convert it to a readable date or map it to the target system format.")
* [Mapping with join output tables](tmap-tlogrow-tfileinputdelimited-tfileinputdelimited-mapping-with-join-output-tables-standard-component-the "The following scenario describes a Job that processes reject flows without separating them from the main flow.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-properties-for-apache-spark-batch -->
# tMap properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMap running in the Spark Batch Job framework.

The Spark Batch
tMap component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Map editor | It allows you to define the tMap routing and transformation properties but note that only the Load once lookup model is supported by the Spark Batch Jobs.  For further information about this Load once lookup model, see the related description of Handling Lookups.  When you click the Property Settings button at the top of the input area, a Property Settings dialog box is displayed in which you can set the following parameters:   * If you do not want to handle execution errors, select the   Die on error check box   (selected by default). It will kill the Job if there is an   error. * To maximize the data transformation performance in a Job that   handles multiple lookup input flows with large amounts of data,   you can select the Lookup in   parallel check box. * Temp data directory path: enter the path where you   want to store the temporary data generated for lookup loading. For more information on   this folder, see [Solving memory limitation issues in tMap use](/talend/r/en-US/8.0/studio-user-guide/solving-memory-limitation-issues-in-tmap-use). * Max buffer size (nb of rows): enter the size of physical   memory, in number of rows, you want to allocate to processed   data. |
| Mapping links display as | Auto: the default setting is curves links  Curves: the mapping display as curves  Lines: the mapping displays as straight lines. This last option allows to slightly enhance performance. |
| Preview | The preview is an instant shot of the Mapper data. It becomes available when Mapper properties have been filled in with data. The preview synchronization takes effect only after saving changes. |
| Use replicated join | Select this check box to perform a replicated join between the input flows. By replicating each lookup table into memory, this type of join doesn't require an additional shuffle-and-sort step, thus speeding up the whole process.  You need to ensure that the entire lookup tables fit in memory. |
| Max buffer size (nb of rows) | Type in the size of physical memory, in number of rows, you want to allocate to processed data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-properties-for-apache-spark-structured-streaming -->
# tMap properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tMap running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tMap component belongs to the Processing
family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Map editor | Use the map editor to define the tMap routing and transformation properties. When you click the Property Settings button at the top of the input area, a Property Settings dialog box is displayed in which you can set the following parameters:   * If you do not want to handle execution errors, select the   Die on error check box   (selected by default). It will kill the Job if there is an   error. * To maximize the data transformation performance in a Job that   handles multiple lookup input flows with large amounts of data,   you can select the Lookup in   parallel check box. * Temp data directory path: enter the path where you   want to store the temporary data generated for lookup loading. For more information on   this folder, see [Solving memory limitation issues in tMap use](/talend/r/en-US/8.0/studio-user-guide/solving-memory-limitation-issues-in-tmap-use). * Max buffer size (nb of rows): enter the size of physical   memory, in number of rows, you want to allocate to processed   data. |
| Mapping links display as | Select how mapping links are displayed:  * Auto: the default setting displays   links as curves. * Curves: the mapping displays as   curves. * Lines: the mapping displays as   straight lines. The Lines option can slightly improve performance. |
| Use replicated join (when all lookup tables can fit in memory) | Select this check box to perform a replicated join between the input flows. By replicating each lookup table into memory, this type of join does not require an additional shuffle-and-sort step, thus speeding up the whole process. Ensure that all lookup tables fit in memory. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties -->
# tMap Standard properties

Last updated: 9/30/2026

These properties are used to configure tMap running in the Standard Job framework.

The Standard
tMap component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Map editor | It allows you to define the tMap routing and transformation properties.  If needed, click the  button at the top of the input area to open the Property Settings dialog box, which provides the following options:   * Die on error: Select this   check box if you want to kill the Job if there is an error. This   check box is selected by default. * Lookup in parallel: Select   this check to maximize the data transformation performance in a   Job that handles multiple lookup input flows with large amounts   of data. * Enable Auto-Conversion of   types: If your input and output columns across a   mapping are of different data types, select this check box to   enable automatic type conversion at the run time to avoid   compiling errors.  This option is enabled by default if the Enable Auto-Conversion of types check box   is selected in the Project   Settings view when this component is added. You can also   override the default conversion behavior of this component by setting   conversion rules in the Project   Settings view. For more information, see [Defining rules to override the default conversion behavior](/talend/r/en-US/8.0/studio-user-guide/defining-rules-to-override-default-conversion-behavior).  Note that auto conversion between Date and BigDecimal is not   supported. * Store on disk: The options   provided in this area are identical to the relevant options   provided on the Basic settings   and Advanced settings tabs   respectively. Settings made in the Property Settings dialog box are reflected in   the respective tab views and vice versa.     This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Mapping links display as | Auto: the default setting is curves links  Curves: the mapping display as curves  Lines: the mapping displays as straight lines. This last option allows to slightly enhance performance. |
| Temp data directory path | Enter the path where you want to store the temporary data generated for lookup loading. For more information on this folder, see [Solving memory limitation issues in tMap use](/talend/r/en-US/8.0/studio-user-guide/solving-memory-limitation-issues-in-tmap-use). |
| Preview | The preview is an instant shot of the Mapper data. It becomes available when Mapper properties have been filled in with data. The preview synchronization takes effect only after saving changes. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Max buffer size (nb of rows) | Type in the size of physical memory, in number of rows, you want to allocate to processed data. |
| Ignore trailing zeros for BigDecimal | Select this check box to ignore trailing zeros for BigDecimal data. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Possible uses are from a simple reorganization of fields to the most complex Jobs of data multiplexing or demultiplexing transformation, concatenation, inversion, filtering, and more. |
| Limitation | The use of tMap supposes minimum Java knowledge in order to fully exploit its functionalities.  This component is a junction step, and for this reason cannot be a start nor end component in the Job. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-mapping-data-using-filter-and-simple-explicit-join-standard-component-the-job -->
# Mapping data using a filter and a simple explicit join

Last updated: 9/30/2026

The Job described below aims at reading data from a csv file with its schema stored in
the Repository, looking up at a reference file, the schema of which is also stored in
the Repository, then extracting data from these two files based on a defined filter to
an output file and reject files.

### In this section

* [Linking the components](/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-linking-components-standard-component-drop)
* [Configuring how to map the data](/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-how-to-map-data-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-executing-job-simple-join-press)
* [Mapping data using inner join rejections](/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-mapping-data-using-inner-join-rejections-standard-component-this)
* [Advanced mapping using filters, explicit joins and rejections](/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-advanced-mapping-using-filters-explicit-joins-and-rejections-standard-component-this)
* [Advanced mapping with filters and different rejections](/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-advanced-mapping-with-filters-and-different-rejections-standard-component-this)

**Related concepts**  

* [tMap](tmap "Transforms and routes data from single or multiple sources to single or multiple destinations.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tlogrow-tfileinputdelimited-tfileinputdelimited-mapping-with-join-output-tables-standard-component-the -->
# Mapping with join output tables

Last updated: 9/30/2026

The following scenario describes a Job that processes reject flows without
separating them from the main flow.

## Linking the components

### Before you begin

You have created two file metadata connections under
Metadata > File delimited in the
Repository view for the following two files.

* states.csv
* customers.csv

For more information about centralizing metadata, see [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).

### Procedure

1. In the Repository tree view,
   click Metadata > File delimited. Place the customers metadata
   onto the workspace. 

   The customers metadata contains information
   about customers, such as their ID, their name or their address, etc.
2. In the dialog box that asks you to choose which component type you want to
   use, select tFileInputDelimited and click
   OK.
3. Place the states metadata onto the design
   workspace. Select the same component in the dialog box and click OK. 

   The states metadata contains the ID of the
   state, and its name.
4. Place a tMap and two tLogRow components from the Palette onto the design workspace.
5. Connect the customers component to the
   tMap, using a Row
   > Main connection.
6. Connect the states component to the
   tMap, using a Row
   > Main connection. This flow will automatically be defined as
   Lookup.

## Configuring the components

### Procedure

1. Double-click the tMap component to open
   the Map Editor. 

   Place the idState column from the main input
   table to the idState column of the lookup table to create a
   join.

   Click the tMap settings button and set
   Join Model to Inner Join.
2. Click the Property Settings button at the
   top of the input area to open the Property
   Settings dialog box, and clear the Die
   on error check box in order to handle the execution errors. 

   The ErrorReject table is
   automatically created.
3. Select the id, idState,
   RegTime and RegisterTime in the input
   table and drag them to the ErrorReject
   table.
4. Click the [+] button at the
   top right of the editor to add an output table. In the dialog box that opens,
   select New output. In the field next to it,
   type in the name of the table, `out1`. Click OK.
5. Drag the following columns from the input tables to the
   out1 table: id,
   CustomerName, idState, and
   LabelState. 

   Add two columns, `RegTime` and
   `RegisterTime`, to the end of the
   out1 table and set their date formats: "dd/MM/yyyy HH:mm" and "yyyy-MM-dd
   HH:mm:ss.SSS" respectively.
6. Click in the Expression field
   for the RegTime column, and press Ctrl+Space to display the auto-completion list. Find and
   double-click  TalendDate.parseDate. Change the
   pattern to ("dd/MM/yyyy HH:mm",row1.RegTime).
7. Do the same thing for the RegisterTime
   column, but change the pattern to ("yyyy-MM-dd
   HH:mm:ss.SSS",row1.RegisterTime).
8. Click the [+] button at the
   top of the output area to add an output table. In the dialog box that opens,
   select Create join table from, choose
   Out1, and name it`rejectInner`. Click
   OK.
9. Click the tMap settings button and set
   Catch lookup inner join reject to
   true in order to handle rejects.
10. Drag the id,
    CustomerName, and idState columns
    from the input tables to the corresponding columns of the
    rejectInner table.

    Click in the Expression
    field for the LabelState column, and type in "UNKNOWN".
11. Click in the Expression field
    for the RegTime column, press Ctrl+Space, and select TalendDate.parseDate. Change the pattern to ("dd/MM/yyyy HH:mm",row1.RegTime).
12. Click in the Expression field
    for the RegisterTime column, press Ctrl+Space, and select TalendDate.parseDate, but change the pattern to ("yyyy-MM-dd HH:mm:ss.SSS",row1.RegisterTime).

    If the data from row1 has a wrong pattern,
    it will be returned by the ErrorReject flow.

    Click OK to validate the
    changes and close the editor.
13. Double-click the first tLogRow component
    to display its Component view.

    Click Sync columns to
    retrieve the schema structure from the mapper if needed.

    In the Mode area, select Table.

    Do the same thing with the second tLogRow.

## Executing the Job

### Procedure

1. Press Ctrl+S to save your
   Job.
2. Press F6 to execute it.

### Results

The Run console displays the main
out flow and the ErrorReject flow. The main output flow unites both valid data and
inner join rejects, while the ErrorReject flow contains the error information about
rows with unparseable date formats.

For examples of how to use dynamic
schemas with tMap, see:

* [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
* [Writing dynamic columns from a source file to a database](/talend/en-US/components/8.0/mysql/writing-dynamic-columns-from-source-file-to-database).

**Related concepts**  

* [tMap](tmap "Transforms and routes data from single or multiple sources to single or multiple destinations.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tmysqlinput-tmysqloutput-tmysqlcommit-advanced-mapping-with-lookup-reload-at-each-row-standard-component-the -->
# Advanced mapping with lookup reload at each row

Last updated: 9/30/2026

The following scenario describes a Job that retrieves people details from a
lookup database, based on a join on the age. The main flow source data is read from a
MySQL database table called *people\_age* that contains people details
such as numeric id, alphanumeric first name and last name and numeric age. The people
age is either 40 or 60. The number of records in this table is intentionally
restricted.

The reference or lookup information is also stored in a MySQL database
table called *large\_data\_volume*. This lookup table contains a
number of records including the city where people from the main flow have been to. For
the sake of clarity, the number of records is restricted but, in a normal use, the
usefulness of the feature described in the example below is more obvious for very large
reference data volume.

To optimize performance, a database connection component is used in the
beginning of the Job to open the connection to the lookup database table in order not to do
that every time you want to load a row from the lookup table.

An Expression Filter is applied to this lookup source flow in order to
select only data from people whose age is equal to 60 or 40. This way only the relevant
rows from the lookup database table are loaded for each row from the main flow.

Therefore this Job shows how, from a limited number of main flow rows, the
lookup join can be optimized to load only results matching the expression key.

Information noteNote:

Generally speaking, as the lookup loading is performed for each main
flow row, this option is mainly interesting when a limited number of rows is
processed in the main flow while a large number of reference rows are to be looked
up to.

The join is solved on the *age* field. Then, using the
relevant loading option in the tMap component
editor, the lookup database information is loaded for each main flow incoming row.

For this Job, the metadata has been prepared for the source and connection
components. For more information on how to set up the DB connection schema metadata, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata).

This Job is formed with five components, four database components and a
mapping component.

## Linking the components

### Procedure

1. Place the DB Connection under the Metadata node of the Repository to the design workspace. In this example, the source
   table is called *people\_age*.
2. Select tMysqlInput from the list that
   pops up when dropping the component.
3. Place the lookup DB connection table from the Metadata node to the design workspace selecting
   tMysqlInput from the list that pops up.
   In this Job, the lookup is called *large\_data\_volume*.
4. Place the DB connection from the Metadata node to the design workspace selecting tMysqlConnection from the list that pops up.

   This component creates a permanent connection to the lookup database table in
   order not to do that every time you want to load a row from the lookup
   table.
5. Pick the tMap component
   from the Processing family, and the
   tMysqlOutput and tMysqlCommit components from the Database family in the Palette to the right hand side of the editor.
6. To connect all the components together, right-click the
   tMysqlInput component corresponding to
   the *people* table and drag the link towards tMap.
7. Release the link over the tMap component,
   the main row flow is automatically set up.
8. Rename the Main row link to
   *people*, to identify more easily the main flow
   data.
9. Perform the same operation to connect the lookup table
   (*large\_data\_volume*) to the tMap component and the tMap
   to the tMysqlOutput component.

   A dialog box prompts for a name to the output link. In this example, the output
   flow is named: people\_mixandmatch
10. Rename the lookup row connection link to *large\_volume,* to help identify the reference data flow.
11. Connect tMysqlConnection to tMysqlInput using the trigger link OnSubjobOk.
12. Connect the tMysqlInput component to the
    tMysqlCommit component using the
    trigger link OnSubjobOk.

## Configuring the components

### Procedure

1. Double-click the tMap component to open
   the graphical mapping editor.

   The Output table (that was created automatically when
   you linked the tMap to the
   tMysqlOutput) will be formed by the matching rows from
   the lookup flow (large\_data\_volume) and the main flow
   (people\_age).
2. Select the main flow rows that are to be passed on to the output
   and drag them over to paste them in the Output table (to the right hand side of
   the mapping editor). 

   Select the main flow rows that are to be passed on to the
   output and drag them over to paste them in the Output table (to the right hand
   side of the mapping editor).

   In this example, the selection from the main flow include the
   following fields: *id*, *first\_name*, *last\_Name* and *age*.

   From the lookup table, the following column is selected: *city*.
3. Place the selected columns from the input tables (*people* and
   *large\_volume*) to the output table.
4. Set up the join between the main and lookup flows.

   Select the *age* column of the main flow
   table (on top) and drag it towards the *age* column of the
   lookup flow table (*large\_volume* in this example).

   A key icon appears next to the linked expression on the lookup
   table. The join is now established.
5. Click the tMap settings button, click the
   [...] button corresponding to Lookup
   Model, and select the Reload at each
   row option from the Options dialog box in order to reload the lookup for each
   row being processed.
6. Set Match Model to
   All matches in the Lookup table in order
   to gather all instances of *age* matches in the output
   flow.
7. Implement the filtering, based on the *age*
   column, in the Lookup table. The GlobalMapKey field is automatically created when you selected the
   Reload at each row option. Indeed, you
   can use this expression to dynamically filter the reference data to load only the
   relevant information when joining with the main flow.

   As mentioned in the introduction of the scenario, the main flow
   data contains only people whose age is either 40 or 60. To avoid the pain of
   loading all lookup rows, including ages that are different from 40 and 60, you can
   use the main flow age as global variable to feed the lookup filtering.
8. Place the *Age* column from the main flow
   table to the Expr. field of the lookup
   table.
9. In the globalMap Key
   field, put in the variable name, using the expression. In this example, it reads:
   "people.Age"

   Click OK to save the
   mapping setting and go back to the design workspace.
10. To finalize the implementation of the dynamic filtering of the
    lookup flow, add a WHERE clause in the query of the database input.
11. At the end of the Query field, following
    the Select statement, type in the following WHERE clause:
    WHERE AGE
    ='"+((Integer)globalMap.get("people.Age"))+"'"
12. Make sure that the type corresponds to the column used as
    variable. In this use case, *Age* is of *Integer* type. Use the variable the way you set in the globalMap key field of the map editor.
13. Double-click the tMysqlOutput component to define its properties.
14. Select the Use an existing connection
    check box to leverage the created DB connection.

    Define the target table name and relevant DB actions.

## Executing the Job

### Procedure

1. Press Ctrl+S to save the
   Job.
2. Click the Run tab at the bottom of the
   design workspace, to display the Job execution tab.
3. From the Debug Run view, click the
   Traces Debug button to view the data
   processing progress.

   For more comfort, you can maximize the Job design view while executing by
   simply double-clicking on the Job name tab.

   The lookup data is reloaded for each of the main flow's rows,
   corresponding to the age constraint. All *age* matches
   are retrieved in the lookup rows and grouped together in the output
   flow.

   Therefore if you check out the data contained in the newly created
   *people\_mixandmatch* table, you will find all the
   *age* duplicates corresponding to different
   individuals whose age equals to 60 or 40 and the city where they have been
   to.

   For examples of how to use dynamic schemas with tMap, see:

   * [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
   * [Writing dynamic columns from a source file to a database](/talend/en-US/components/8.0/mysql/writing-dynamic-columns-from-source-file-to-database).

**Related concepts**  

* [tMap](tmap "Transforms and routes data from single or multiple sources to single or multiple destinations.")

**Related information**  

* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)
* [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput)
* [tMysqlConnection](/talend/en-US/components/8.0/mysql/tmysqlconnection)
* [tMysqlCommit](/talend/en-US/components/8.0/mysql/tmysqlcommit)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-advanced-mapping-using-filters-explicit-joins-and-rejections-standard-component-this -->
# Advanced mapping using filters, explicit joins and rejections

Last updated: 9/30/2026

This scenario introduces a Job that allows you to find BMW owners who have two to
six children (inclusive), for sales promotion purpose for example.

## Linking the components

### Procedure

1. Place three tFileInputDelimited components, a tMap component, and two tFileOutputDelimited components from the Palette onto the design workspace, and label them to best describe
   their functions.
2. Connect the input components to the tMap
   using Row > Main connections. 

   Pay attention to the file you connect first as it will
   automatically be set as Main flow, and all
   the other connections will be Lookup flows.
   In this example, the connection for the input component
   Owners is the Main
   flow.

## Configuring the components

### Procedure

1. Define the properties of each input components in the respective
   Basic settings view. Define the
   properties of Owners.
2. Select Repository from the Property type list and select the component's
   schema, *owners* in this scenario, from the Repository Content dialog box. The rest fields
   are automatically filled.

   Information noteNote:

   In this scenario, the input schemas are stored in the
   Metadata node of the Repository tree view for easy retrieval. For
   further information regarding metadata creation in the Repository, see [Managing metadata in Talend
   Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).

   In the same way, set the properties of the other input
   components: Cars and Resellers.
   These two Lookup flows will fill in
   secondary (lookup) tables in the input area of the Map
   Editor.
3. Double-click the tMap
   component to launch the Map Editor and
   define the mappings and filters.

   Set an explicit join between the Main flow Owner and the Lookup flow Cars by dropping
   the ID\_Owner column of the Owners table
   to the ID\_Owner column of the Cars
   table.

   The explicit join is displayed along with a hash key.
4. In the Expr. Key field of
   the Make column, type in a filter. In this use case, simply
   type in "BMW" as the search is focused on the
   owners of this particular make.
5. Implement a cascading join between the two lookup tables
   Cars and Resellers on the
   ID\_Reseller column in order to retrieve resellers
   information.
6. As you want to reject the null values into a separate table and exclude
   them from the standard output, click the tMap
   settings button and set Join
   Model to Inner Join in each
   of the Lookup tables.
7. In the tMap settings, you can set
   Match Model to Unique match, First
   match, or All matches. In
   this use case, the All matches option is
   selected. Thus if several matches are found in the Inner Join, rows matching the
   explicit join as well as the filter, all of them will be added to the output flow
   (either in rejection or the regular output). 

   Information noteNote:

   The Unique match
   option functions as a Last match. The
   First match and All matches options function as named.
8. On the output area of the Map Editor,
   click the plus button to add two tables, one for the full matches and the
   other for the rejections.
9. Drag all the columns of the Owners table,
   the Registration, Make and
   Color columns of the Cars table, and
   the ID\_Reseller and Name\_Reseller
   columns of the Resellers table to the main output
   table.
10. Drag all the columns of the Owners table
    to the reject output table.
11. Click the Filter button at the top of the
    main output table to display the Filter
    expression area.

    Type in a filter statement to narrow down the number of rows loaded in the
    main output flow. In this use case, the statement reads:
    Owners.Children\_Nr >= 2 && Owners.Children\_Nr <=
    6.
12. In the reject output table, click the tMap
    settings button and set the reject types.

    Set Catch output reject to true to collect data about BMW car owners who
    have less than two or more than six children.

    Set Catch lookup inner join reject to
    true to collect data about owners of
    other car makes and owners for whom the reseller information is not
    found.

    Click OK to validate the mappings and
    close the Map Editor.

    On the design workspace, right-click the tMap and pull the respective output link to the relevant
    output components.
13. Define the properties of the output components in their respective
    Basic settings view.

    In this use case, simple specify the output file paths and select the
    Include Header check box, and leave the
    other parameters as they are.

## Executing the Job

### Procedure

1. Press Ctrl+S to save your
   Job.
2. Press F6 to run it.

   The main output file contains the information related to BMW owners who
   have two to six children, and the reject output file contains the
   information about the rest of the car owners.

   For examples of how to use dynamic schemas with tMap, see:

   * [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
   * [Writing dynamic columns from a source file to a database](/talend/en-US/components/8.0/mysql/writing-dynamic-columns-from-source-file-to-database).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-advanced-mapping-with-filters-and-different-rejections-standard-component-this -->
# Advanced mapping with filters and different rejections

Last updated: 9/30/2026

This scenario is a modified version of the preceding scenario. It describes a Job
that applies filters to limit the search to BMW and Mercedes owners who have two to six
children and divides unmatched data into different reject output flows.

## Linking the components

### Procedure

1. Take the same Job as in [Advanced mapping using filters, explicit joins and rejections](/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-advanced-mapping-using-filters-explicit-joins-and-rejections-standard-component-this).
2. Place a new tFileOutputDelimited component from the Palette on the design workspace, and name it
   `Rejects_BMW_Mercedes` to reflect its function.
3. Connect the tMap component
   to the new output component using a Row
   connection and label the connection according to the output component function. 

   This connection label will appear as the name of the new output
   table in the Map Editor.
4. Relabel the existing output connections and output components to
   reflect their function.

   The existing output tables in the Map
   Editor will be automatically renamed according to the connection
   labels. In this example, relabel the existing output connections
   `BMW_Mercedes_withChildren` and
   `Owners_Other_Makes` respectively.

## Configuring the components

### Procedure

1. Double-click the tMap component to launch
   the Map Editor to change the mappings and
   the filters.

   The output area contains a new, empty output table named
   `Rejects_BMW_Mercedes`. You can adjust the position of the
   table by selecting it and clicking the Up
   or Down arrow button at the top of the
   output area.
2. Remove the Expr. key
   filter ("BMW") from the Cars table in
   the input area.
3. Click the Filters button
   to display the Filter field, and type in a
   new filter to limit the search to BMW or
   Mercedes car makes. The statement reads as follows:
   Cars.Make.equals("BMW") ||
   Cars.Make.equals("Mercedes")
4. Select all the columns of the main output table and drop them down to the
   new output table.

   Alternatively, you can also drag the corresponding columns from
   the relevant input tables to the new output table.
5. Click the tMap settings button at the top
   of the new output table and set Catch output
   reject to true to collect
   data about BMW and Mercedes owners who have less than two or more than six
   children.
6. In the Owners\_Other\_Makes table, set
   Catch lookup inner join reject to
   true to collect data about owners of
   other car makes and owners for whom the reseller information is not found.
7. Click OK to validate the mappings and
   close the Map Editor.
8. Define the properties of the output components in their respective
   Basic settings view.

   In this use case, simple specify the output file paths and
   select the Include Header check box, and
   leave the other parameters as they are.

## Executing the Job

### Procedure

1. Press Ctrl+S to save the
   Job.
2. Press F6 to run it.

   The output files contain content of the main output flow shows
   that the filtered rows have correctly been passed on.

   For examples of how to use dynamic schemas with tMap, see:

   * [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
   * [Writing dynamic columns from a source file to a database](/talend/en-US/components/8.0/mysql/writing-dynamic-columns-from-source-file-to-database).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-how-to-map-data-standard-component -->
# Configuring how to map the data

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component labeled *Cars* to display its Basic settings view.
2. Select Repository from the Property type list and select the component's
   schema, *cars* in this scenario, from the Repository Content dialog box. The rest fields
   are automatically filled.
3. Double-click the component labeled *Owners* and repeat
   the setting operation. Select the appropriate metadata entry,
   *owners* in this scenario.

   Information noteNote:

   In this scenario, the input schemas are stored in the
   Metadata node of the Repository tree view for easy retrieval. For
   further information regarding metadata creation in the Repository, see [Managing metadata in Talend
   Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).
4. Double-click the tMap component to open
   the Map Editor. 

   Note that the input area is already filled with the defined input tables
   and that the top table is the main input table, and the respective row
   connection labels are displayed on the top bar of the table.
5. Create a join between the two tables on the *ID\_Owner*
   column by simply dropping the *ID\_Owner* column from the
   *Cars\_data* table onto the
   *ID\_Owner* column in the
   *Owners\_data* table.
6. Define this join as an inner join by clicking the tMap settings button, clicking in the Value field for Join
   Model, clicking the small button that appears in the field, and
   selecting Inner Join from the Options dialog box.
7. Drag all the columns of the *Cars\_data* table to the
   *Insured* table.
8. Drag the *ID\_Owner*,
   *Registration*, and *ID\_Reseller*
   columns of the *Cars\_data* table and the
   *Name* column of the *Owners\_data*
   table to the *Reject\_NoInsur* table.
9. Drag all the columns of the *Cars\_data* table to the
   *Reject\_OwnerID* table. 

   For more information regarding data mapping, see [Mapping data flows](/talend/r/Lfrx8uSM%7EUd8zWd9BsWB5g/Z%7EDS5lkZdvVq6IJPXFZeZA).
10. Click the plus arrow button at the top of the *Insured*
    table to add a filter row.

    Drag the *ID\_Insurance* column of the
    *Owners\_data* table to the filter condition area and
    enter the formula meaning 'not undefined': Owners\_data.ID\_Insurance !=
    null.

    With this filter, the *Insured* table will
    gather all the records that include an insurance ID.
11. Click the tMap settings button at the top
    of the *Reject\_NoInsur* table and set Catch output reject to true to define the table as a standard reject output flow to
    gather the records that do not include an insurance ID.
12. Click the tMap settings button at the top
    of the *Reject\_OwnerID* table and set Catch lookup inner join reject to true so that this output table will gather the
    records from the *Cars\_data* flow with missing or
    unmatched owner IDs.

    Click OK to validate the mappings and
    close the Map Editor.
13. Double-click each of the output components, one after the other, to
    define their properties.

    If you want a new file to be created, browse to the destination output folder, and
    type in a file name including the extension.

    Select the Include header
    check box to reuse the column labels from the schema as header row in the output
    file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-executing-job-simple-join-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your
   Job.
2. Press F6 to run the
   Job.

   The output files are created, which contain the relevant data
   as defined.

   For examples of how to use
   dynamic schemas with tMap,
   see:

   * [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
   * [Writing dynamic columns from a source file to a database](/talend/en-US/components/8.0/mysql/writing-dynamic-columns-from-source-file-to-database).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Place two tFileInputDelimited
   components, tMap and three tFileOutputDelimited components onto the design
   workspace.
2. Rename the two tFileInputDelimited components as *Cars* and *Owners*, either by double-clicking the label in the design
   workspace or using the View tab of the
   Component view.
3. Connect the two input components to tMap
   using Row > Main connections and label the connections as
   *Cars\_data* and *Owners\_data*
   respectively.
4. Connect tMap to the three output
   components using Row > New Output (Main) connections and name the output
   connections as *Insured*, *Reject\_NoInsur* and *Reject\_OwnerID*
   respectively.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-mapping-data-using-inner-join-rejections-standard-component-this -->
# Mapping data using inner join rejections

Last updated: 9/30/2026

This scenario, based on scenario 1, adds one input file containing details about
resellers and extra fields in the main output table. Two filters on inner joins are added
to gather specific rejections.

## Linking the components

### Procedure

1. Place a tFileInputDelimited
   component and a tFileOutputDelimited
   component to the design workspace, and label the components as
   `Resellers` and `No_Reseller_ID`
   respectively.
2. Connect it to the Mapper using a Row > Main connection,
   and label the connection as `Resellers_data`.
3. Connect the tMap component
   to the new tFileOutputDelimited component by
   using the Row connection named
   `Reject_ResellerID`.

## Configuring the inner join

### Procedure

1. Double-click the Resellers component to
   display its Basic settings view.
2. Select Repository from
   the Property type list and select the
   component's schema, Resellers in this scenario, from the
   Repository Content dialog box. The rest
   fields are automatically filled.

   Information noteNote:

   In this scenario, the input schemas are stored in the
   Metadata node of the Repository tree view for easy retrieval. For
   further information regarding metadata creation in the Repository, see [Managing metadata in Talend
   Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).
3. Double-click the tMap component to open
   the Map Editor. 

   The schema of the new input component is already added in the
   Input area.
4. Create a join between the main input flow and the new input flow
   by dropping the ID\_Reseller column of the
   Cars\_data table to the ID\_Reseller
   column of the Resellers\_data table.
5. Click the tMap settings
   button at the top of the Resellers\_data table and set
   Join Model to Inner Join.
6. Drag all the columns except ID\_Reseller of
   the Resellers\_data table to the main output table
   Insured.

   Information noteNote:

   When two inner joins are defined, you either need to define
   two different inner join reject tables to differentiate the two rejections
   or, if there is only one inner join reject output, both inner join
   rejections will be stored in the same output.
7. Click the [+] button at
   the top of the output area to add a new output table, and name this new output
   table `Reject_ResellerID`.
8. Drag all the columns of the Cars\_data table
   to the Reject\_ResellerID table.
9. Click the tMap settings button and select
   Catch lookup inner join reject to
   true to define this new output table as
   an inner join reject output.

   If the defined inner join cannot be established, the information about
   the relevant cars will be gathered through this output flow.
10. Apply filters on the two Inner Join reject outputs in order for
    to distinguish the two types of rejection.

    In the first Inner Join output table,
    Reject\_OwnerID, click the plus arrow button to add a
    filter line and fill it with the following formula to gather only owner ID related
    rejection: Owners\_data.ID\_Owner==null
11. In the second Inner Join output table,
    Reject\_ResellerID, repeat the same operation using the
    following formula: Resellers\_data.ID\_Reseller==null

    Click OK to validate the
    map settings and close the Mapper Editor.
12. Double-click the No\_Reseller\_ID component
    to display its Basic settings view.

    Specify the output file path and select the Include Header check box, and leave the other
    parameters as they are.
13. To demonstrate the work of the Mapper, in this example, remove
    reseller IDs 5 and 8 from the input
    file Resellers.csv.

## Executing the Job

### Procedure

1. Press Ctrl+S to save your
   Job.
2. Press F6 to run the Job.

### Results

The four output files are all created in the specified folder,
containing information as defined. The output file
No\_Reseller\_ID.csv contains the *cars* information
related to reseller IDs 5 and 8, which
are missing in the input file Resellers.csv.

For examples of how to use dynamic schemas with tMap, see:

* [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
* [Writing dynamic columns from a source file to a database](/talend/en-US/components/8.0/mysql/writing-dynamic-columns-from-source-file-to-database).

As third advanced use scenario, based on the scenario 2, add a
new Input table containing Insurance details for example.

Set up an Inner Join between two lookup input tables (Owners and
Insurance) in the Mapper to create a cascade lookup and hence retrieve Insurance
details using the Owners table data.
