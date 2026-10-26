<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput · versión 8.0 -->
# tMysqlInput

Last updated: 9/30/2026

Executes a DB query with a strictly defined order which must correspond to the
schema definition.

tMysqlInput reads a database and extracts fields based on a query. Then
it passes on the field list to the next component via a Main row link.

### In this section

* [tMysqlInput Standard properties](/talend/en-US/components/8.0/mysql/tmysqlinput-standard-properties)
* [tMysqlInput properties for Apache Spark Batch](/talend/en-US/components/8.0/mysql/tmysqlinput-properties-for-apache-spark-batch)

**Related concepts**  

* [Populating a MySQL data warehouse](tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-populating-mysql-data-warehouse-standard-component-enterprise-the)
* [Sharing a database connection between a parent Job and child Job](tmysqlconnection-tmysqlinput-tlogrow-sharing-database-connection-between-parent-job-and-child-job-standard-component-this)
* [Writing columns from a MySQL database to an output file using tMysqlInput](tmysqlinput-tfileoutputdelimited-writing-columns-from-mysql-database-to-output-file-using-tmysqlinput-standard-component-in-this)
* [Controlling the data definition language via tMysqlOutput when creating a table](controlling-data-definition-language-via-tmysqloutput "This scenario shows how to create a MySQL table with an AUTO_INCREMENT column and a UNIQUE one with tMysqlOutput component.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-properties-for-apache-spark-batch -->
# tMysqlInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMysqlInput running in
the Spark Batch Job framework.

The Spark Batch
tMysqlInput component belongs to the Databases family.

This component also allows you to connect and read data from a RDS Aurora or a RDS MySQL
database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| DB version | Select the version of the database to be used.  When the database to be used is RDS Aurora, you need to select Mysql 5 (deprecated).  Information noteNote: MySQL 5 has been removed from Talend Studio 8.0 R2026-04. Use MySQL 8.0 or later. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Type in the name of the table from which you need to read data.  This field is only available when you select Table from the Read from drop-down list. |
| Read from | Select the type of the source of the data to be read.  * Table: tMysqlInput reads the data   of the table you specify in the Table name field. * Query: tMysqlInput reads the   result of the query you write in the Query   field. |
| Query type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  If you are using Spark V2.0 onwards, the Spark SQL does not recognize the prefix of a database table anymore. This means that you must enter only the table name without adding any prefix that indicates for example the schema this table belongs to.  For example, if you need to perform a query in a table *system.mytable*, in which the *system* prefix indicates the schema that the *mytable* table belongs to, in the query, you must enter *mytable* only.  You can use pushdown predicate in the query to filter the data from the database. Spark supports the following operators:  * `Filter` * `Limit`  These fields are only available when you select Query from the Read from drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Spark SQL JDBC parameters | Add the JDBC properties supported by Spark SQL to this table. For a list of the user configurable properties, see [JDBC to other database](https://spark.apache.org/docs/latest/sql-programming-guide.html#jdbc-to-other-databases).  This component automatically set the *url*, *dbtable* and *driver* properties by using the configuration from the Basic settings tab. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns.  Information noteNote: Clear Trim all the String/Char columns to enable Trim columns in this field. |
| Enable partitioning | Select this check box to read data in partitions.  Define, in double quotation marks, the following parameters to configure the partitioning:  * Partition column: the numeric column   used as partition key. * Lower bound of the partition stride   and Upper bound of the partition   stride: enter the upper bounds and the lower bound to determine   the partition stride. These bounds do not filter the table rows. All rows in   the table are partitioned and returned. * Number of partitions: the number of   partitions into which the table rows are split. Each Spark worker handles only   one of the partitions at a time.  The average size of the partitions is the result of the difference between the upper bound and the lower bound divided by the number of partitions, that is to say, (upperBound - lowerBound)/partitionNumber, while the first and the last partitions also include all the other rows that are not contained in the other partitions.  For example, to partition 1000 rows into 4 partitions, if you enter 0 for the lower bound and 1000 for the upper bound, each partition will contain 250 rows and so the partitioning is even. If you enter 250 for the lower bound and 750 for the upper bound, the second and the third partition will each contain 125 rows and the first and the last partitions each 375 rows. With this configuration, the partitioning is skewed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tMysqlConfiguration component present in the same Job to connect to MySQL. You need to select the Use an existing connection check box and then select the tMysqlConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-standard-properties -->
# tMysqlInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tMysqlInput running in
the Standard Job framework.

The Standard
tMysqlInput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| DB version | Select the version of the database to be used. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the database server IP address. |
| Port | Enter the listening port number of DB server. |
| Database | Enter the name of the database. |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Enter the name of the table to be read. |
| Query type and Query | Enter your database query, paying particularly attention to properly sequence the fields in order to match the schema definition. *If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected.* |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  Information noteWarning: If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This checkbox is not available when the Use an existing connection checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. Information noteNote: When you need to handle data of the time-stamp type *0000-00-00 00:00:00* using this component, set the parameter as: noDatetimeStringSync=true&zeroDa­teTimeBehavior=convertToNull. |
| Enable stream | This check box is available only when MySQL is selected from the Database drop-down list. Select this check box to enables streaming over buffering which allows the code to read from a large table without consuming a large amount of memory in order to optimize the performance. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. Information noteNote: Clear Trim all the String/Char columns to enable Trim columns in this field. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for Mysql databases. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tfileoutputdelimited-writing-columns-from-mysql-database-to-output-file-using-tmysqlinput-standard-component-in-this -->
# Writing columns from a MySQL database to an output file using tMysqlInput

Last updated: 9/30/2026

In this scenario we will read certain columns from a MySQL database, and then
write them to a table in a local output file.

### In this section

* [Dragging and dropping components and linking them together](/talend/en-US/components/8.0/mysql/tmysqlinput-tfileoutputdelimited-dragging-and-dropping-components-and-linking-them-together-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlinput-tfileoutputdelimited-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlinput-tfileoutputdelimited-executing-job-standard-component-the)

**Related concepts**  

* [tMysqlInput](tmysqlinput "Executes a DB query with a strictly defined order which must correspond to the schema definition.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-populating-mysql-data-warehouse-standard-component-enterprise-the -->
# Populating a MySQL data warehouse

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

The following Java scenario creates a three-component Job that populates a data
warehouse. A tMysqlInput component reads your customer
data stored in the Customer base. A tMap component
allows you to modify this data and the modifications are transmitted to the
*Leadfact* table in the CRM database through a tMysqlOutput component.

### In this section

* [Linking the components](/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-linking-components-standard-component-enterprise-drop)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-configuring-components-standard-component-enterprise-in)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-executing-job-standard-component-enterprise-press)

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")
* [tMysqlInput](tmysqlinput "Executes a DB query with a strictly defined order which must correspond to the schema definition.")

**Related information**  

* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tfileoutputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tMysqlInput to open its
   Basic Settings view in the Component tab.
2. From the Property Type list, select
   Repository if you have already stored
   the connection to database in the Metadata
   node of the Repository tree view. The
   property fields that follow are automatically filled in.

   For more information about how to store a database connection, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata).

   If you have not defined the database connection locally in the Repository, fill in the details manually after
   selecting Built-in from the Property Type list.
3. Set the Schema as Built-in and click Edit
   schema to define the desired schema.

   The schema editor opens:
4. Click the [+] button to add the rows
   that you will use to define the schema, four columns in this example
   *id*, *first\_name*,
   *city* and *salary*.

   Under Column, click in the fields to
   enter the corresponding column names.

   Click the field under Type to define the
   type of data.

   Click OK to close the schema
   editor.
5. Next to the Table Name field, click
   the [...] button to select the database
   table of interest.

   A dialog box displays a tree diagram of all the tables in the selected
   database:
6. Click the table of interest and then click OK to close the dialog box.
7. Set the Query Type as Built-In.
8. In the Query box, enter the query
   required to retrieve the desired columns from the table.
9. Double-click tFileOutputDelimited to set
   its Basic settings in the Component tab.
10. Next to the File Name field, click the
    [...] button to browse your directory
    to where you want to save the output file, then enter a name for the
    file.

    Select the Include Header check box to
    retrieve the column names as well as the data.
11. Save the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tfileoutputdelimited-dragging-and-dropping-components-and-linking-them-together-standard-component-drop -->
# Dragging and dropping components and linking them together

Last updated: 9/30/2026

## Procedure

1. Drop tMysqlInput and tFileOutputDelimited from the Palette onto the workspace.
2. Link tMysqlInput to tFileOutputDelimited using a Row > Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tfileoutputdelimited-executing-job-standard-component-the -->
# Executing the Job

Last updated: 9/30/2026

The results below can be found after F6 is
pressed to run the Job.

As shown above, the output file is written with the desired column names and
corresponding data, retrieved from the database:

Information noteNote:

The Job can also be run in the Traces Debug
mode, which allows you to view the rows as they are being written to the output
file, in the workspace.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-configuring-components-standard-component-enterprise-in -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tMysqlInput and click the Component tab to define its basic settings.
2. Set Property Type to Repository and then select the connection to the
   Customer database that holds the information about your clients. The
   connection details will display automatically in the corresponding
   fields.

   Information noteNote:

   If you have not stored the database connection details in the
   Metadata entry in the Repository,
   select Built-in in the property type
   list and set the connection details manually.
3. Set Schema to Repository and click the [...] button to select the
   schema of the Customer database stored in the Metadata entry.
4. In the Table Name field, enter the name
   of the table holding the information you want to modify, in this example:
   *customers*.
5. Click Guess Query to retrieve all data
   from your table.
6. Double-click the tMap component to open
   the Map Editor. Notice that the Input area
   is already filled with the metadata of the input component.
7. Drag the fields in the input zone to the fields in the *Leadfact*table in the output zone.
8. Click OK to validate the
   operation.
9. In the design workspace, select tMysqlOutput and click the Component tab to define its basic settings.
10. Set Property Type to Repository and then select the connection to the
    CRM data warehouse. The connection details will display automatically in the
    corresponding fields

    Information noteNote:

    If you have not stored the CRM data warehouse connection details in
    the Metadata entry in the Repository,
    select Built-in in the property type
    list and set the connection details manually.
11. In the Table Name field, enter the name
    of the table you want to populate with modified data, in this example:
    *leadfact*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-executing-job-standard-component-enterprise-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save your Job.
2. Press F6 to run the Job to create and
   populate the table *Leadfact* in the CRM data
   warehouse.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-linking-components-standard-component-enterprise-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tMysqlInput, tMap, and
   tMysqlOutput.
2. Connect the three components using Row > Main
   links.
