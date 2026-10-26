<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput · versión 8.0 -->
# tOracleInput

Last updated: 9/30/2026

Reads an Oracle database and extracts fields based on a query.

tOracleInput executes a database query with a strictly defined order
which must correspond to the schema definition. Then it passes on the field list to the
next component via a Main row link.

### In this section

* [tOracleInput Standard properties](/talend/en-US/components/8.0/oracle/toracleinput-standard-properties)
* [tOracleInput properties for Apache Spark Batch](/talend/en-US/components/8.0/oracle/toracleinput-properties-for-apache-spark-batch)

**Related concepts**  

* [Checking number format using a stored procedure](toracleconnection-toracleinput-toraclesp-tlogrow-checking-number-format-using-stored-procedure-standard-component-the)
* [Populating an Oracle data warehouse](toracleoutput-toracleinput-tmap-toracleinput-tmap-populating-oracle-data-warehouse-standard-component-enterprise "The following Java scenario creates a three-component Job that populates a data warehouse. A tOracleInput component reads your client data stored in the CLIENT table. A tMap component allows you to modify this data and the modifications are transmitted to the Leadfact table in the database through a tOracleOutput component.")
* [Truncating and inserting file data into an Oracle database](toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-truncating-and-inserting-file-data-into-oracle-database-standard-component-this)
* [Using context parameters when reading a table from an Oracle database](toracleinput-tlogrow-using-context-parameters-when-reading-table-from-oracle-database-standard-component-in-this)

**Related tasks**  

* [Using Oracle as a vector database](toracleconnection-toracleinput-toracleoutput-toracleclose-tfileinputdelimited-tmap-tlogrow-using-oracle-as-vector-db-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-properties-for-apache-spark-batch -->
# tOracleInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tOracleInput running in
the Spark Batch Job framework.

The Spark Batch
tOracleInput component belongs to the Databases family.

This component also allows you to connect and read data from a RDS Oracle
database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | The available drivers are:   * Oracle OCI: Select this connection type   to use Oracle Call Interface with a set of C-language software APIs that provide   an interface to the Oracle database. * Oracle Custom: Select this connection   type to access a clustered database. With this type of connection, the   Username and the Password fields are deactivated and you need to   enter the connection URL in the URL field   that is displayed.  For further information about the valid form of this URL, see [JDBC Connection   strings](http://www.dba-resources.com/oracle/jdbc-connection-strings-for-oracle-thin-driver/) from the Oracle documentation. * Oracle Service Name: Select this   connection type to use the TNS alias that you give when you connect to the   remote database. * WALLET: Select this connection type to   store credentials in an Oracle wallet. * Oracle SID: Select this connection type   to uniquely identify a particular database on a system. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Oracle schema | Oracle schema name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to be   processed and passed on to the next component. The schema is either   Built-in or stored remotely in the   Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table Name | Type in the name of the table from which you need to read data. |
| Query type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  If you are using Spark V2.0 onwards, the Spark SQL does not recognize the prefix of a database table anymore. This means that you must enter only the table name without adding any prefix that indicates for example the schema this table belongs to.  For example, if you need to perform a query in a table *system.mytable*, in which the *system* prefix indicates the schema that the *mytable* table belongs to, in the query, you must enter *mytable* only. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Spark SQL JDBC parameters | Add the JDBC properties supported by Spark SQL to this table. For a list of the user configurable properties, see [JDBC to other database](https://spark.apache.org/docs/latest/sql-programming-guide.html#jdbc-to-other-databases).  This component automatically set the *url*, *dbtable* and *driver* properties by using the configuration from the Basic settings tab. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Enable partitioning | Select this check box to read data in partitions.  Define, in double quotation marks, the following parameters to configure the partitioning:  * Partition column: the numeric column   used as partition key. * Lower bound of the partition stride   and Upper bound of the partition   stride: enter the upper bounds and the lower bound to determine   the partition stride. These bounds do not filter the table rows. All rows in   the table are partitioned and returned. * Number of partitions: the number of   partitions into which the table rows are split. Each Spark worker handles only   one of the partitions at a time.  The average size of the partitions is the result of the difference between the upper bound and the lower bound divided by the number of partitions, that is to say, (upperBound - lowerBound)/partitionNumber, while the first and the last partitions also include all the other rows that are not contained in the other partitions.  For example, to partition 1000 rows into 4 partitions, if you enter 0 for the lower bound and 1000 for the upper bound, each partition will contain 250 rows and so the partitioning is even. If you enter 250 for the lower bound and 750 for the upper bound, the second and the third partition will each contain 125 rows and the first and the last partitions each 375 rows. With this configuration, the partitioning is skewed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tOracleConfiguration component present in the same Job to connect to Oracle. You need to select the Use an existing connection check box and then select the tOracleConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties -->
# tOracleInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tOracleInput running in
the Standard Job framework.

The Standard
tOracleInput component belongs to the Databases family.

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
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers:  Oracle OCI: Select this connection type to use Oracle Call Interface with a set of C-language software APIs that provide an interface to the Oracle database.  Oracle Custom: Select this connection type to access a clustered database.  Oracle Service Name: Select this connection type to use the TNS alias that you give when you connect to the remote database.  WALLET: Select this connection type to store credentials in an Oracle wallet.  Oracle SID: Select this connection type to uniquely identify a particular database on a system. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Oracle schema | Oracle schema name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table name | Database table name. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This checkbox is not available when the Use an existing connection checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Covert XML type to Java Type | Select this check box and then use the table to convert the types of the defined columns to Java types. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Use fetch size | Select this check box and in the Fetch size field displayed, specify the number of rows to fetch in one go from the database. The performance can be improved by tuning this fetch size to an appropriate value. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| No null values | Check this box to improve the performance if there are no null values. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for Oracle databases. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-using-context-parameters-when-reading-table-from-oracle-database-standard-component-in-this -->
# Using context parameters when reading a table from an Oracle database

Last updated: 9/30/2026

In this scenario, we will read a table from an Oracle database using a context parameter to
refer to the table name.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-dropping-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-saving-and-executing-job-standard-component-press)
* [Related scenarios](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-related-scenarios-standard-component-for)

**Related concepts**  

* [tOracleInput](toracleinput "Reads an Oracle database and extracts fields based on a query.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-truncating-and-inserting-file-data-into-oracle-database-standard-component-this -->
# Truncating and inserting file data into an Oracle database

Last updated: 9/30/2026

This scenario describes how to truncate the content of an Oracle database and
load the content of an input file. The related Job is composed of three components that
respectively creates the content, output this content into a file to be loaded into the Oracle
database after the database table has been truncated.

### In this section

* [Building the Job](/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-building-job-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-executing-job-standard-component-press)

**Related concepts**  

* [tOracleInput](toracleinput "Reads an Oracle database and extracts fields based on a query.")

**Related reference**  

* [tOracleBulkExec](toraclebulkexec "Offers gains in performance during operations performed on data of an Oracle database.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tOracleInput to open its
   Basic Settings view in the Component tab.
2. Select a connection type from the Connection
   Type drop-down list. In this example, it is *Oracle SID*.

   Select the version of the Oracle database to be used from the DB Version drop-down list. In this example, it is
   *Oracle 12-7*.

   In the Host field, enter the Oracle
   database server's IP address. In this example, it is *192.168.31.32*.

   In the Database field, enter the database
   name. In this example, it is *TALEND*.

   In the Oracle schema field, enter the
   Oracle schema name. In this example, it is *TALEND*.

   In the Username and Password fields, enter the authentication details.
3. Click the [...] button next to Edit schema to open the schema editor.
4. Click the [+] button to add four
   columns: *ID* and *AGE* of the integer type, *NAME* and *SEX* of the
   string type.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
5. Put the cursor in the Table Name field
   and press F5 for context parameter setting.
   The dialog box New Context Parameter pops
   up.

   For more information about context settings, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).
6. In the Name field, enter the context
   parameter name. In this example, it is *TABLE*.

   In the Default value field, enter the
   name of the Oracle database table to be queried. In this example, it is
   *PERSON*.
7. Click Finish to validate the setting. 

   The context parameter *context.TABLE*
   automatically appears in the Table Name
   field.
8. In the Query Type list, select Built-In. Then, click Guess
   Query to get the query statement. 

   ```
   "SELECT 
     "+context.TABLE+".\"ID\", 
     "+context.TABLE+".NAME, 
     "+context.TABLE+".SEX, 
     "+context.TABLE+".AGE
   FROM "+context.TABLE
   ```
9. Double-click tLogRow to open its
   Basic settings view in the Component tab.
10. In the Mode area, select Table (print values in cells of a table) for a
    better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-dropping-and-linking-components-standard-component-create -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in the design
   workspace or dropping them from the Palette: a tOracleInput
   component and a tLogRow component.
2. Connect tOracleInput to tLogRow using a Row > Main
   link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, the data in the Oracle database table *PERSON* is displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-building-job-standard-component-drop -->
# Building the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components: tOracleInput, tFileOutputDelimited and tOracleBulkExec from the Palette to the design workspace.
2. Connect the tOracleInput to the tFileOutputDelimited using a Row > Main link.
3. Connect the tOracleInput to the tOracleBulkExec using a OnSubjobOk trigger link.

## Results


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tOracleInput to open its
   Basic settings view.
2. Define the Oracle connection details. It is recommended to store the
   database connection details in the Metadata
   folder of the Repository tree view in order
   to retrieve them easily at any time in any Job.
3. Define the schema, if it is not stored in the Repository. In this example, the schema contains four
   columns as follows: *ID\_Contract*,
   *ID\_Client*, *Contract\_type* and
   *Contract\_Value*.
4. Define the tFileOutputDelimited component
   parameters, including output File Name,
   Row separator and Fields delimiter.
5. Double-click on the tOracleBulkExec to
   define the database populating properties.
6. In the Property Type list, select
   Repository if you stored the database
   connection details under the Metadata node
   of the Repository or select Built-in to define them manually. In this
   scenario, use the Built-in mode.
7. Set the connection parameters in the following fields: Host, Port,
   Database, Schema, Username, and
   Password.
8. Fill in the name of the Table to be
   populated and the Action on data to be
   carried out. In this use case, select insert.
9. In the Schema list, select Built-in, and click the [...] button next to the Edit
   schema field to define the structure of the data to be passed
   to the next component.
10. Click the Advanced settings view to
    configure the advanced settings of the component.
11. Select the Use existing control
    file check box if you want to use a control file (.ctl) storing the
    status of the physical structure of the database. Or, fill in the following fields
    manually: Record format, Specify .ctl file's INTO TABLE clause manually,
    Field terminated by, Use field enclosure, Use
    schema's Date Pattern to load Date field, Specify field condition, Preserve
    blanks, Trailing null columns,
    Load options, NLS Language and Set Parameter
    NLS\_TERRITORY according to your database.
12. In the Encoding list, select the
    encoding, or enter the encoding between double quotes if it does not exist
    in the list.
13. In the Output list, select to console to output the standard output of the
    database in the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 to run the Job. The log is shown
   in the console of the Run view and the
   table is populated with the parameter file data.

## Results

Related topic: see [Inserting data in bulk in MySQL database](/talend/en-US/components/8.0/mysql/tmysqloutputbulkexec-trowgenerator-inserting-data-in-bulk-in-mysql-database-standard-component-this).
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties · versión 8.0 -->
# tOracleInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tOracleInput running in
the Standard Job framework.

The Standard
tOracleInput component belongs to the Databases family.

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
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers:  Oracle OCI: Select this connection type to use Oracle Call Interface with a set of C-language software APIs that provide an interface to the Oracle database.  Oracle Custom: Select this connection type to access a clustered database.  Oracle Service Name: Select this connection type to use the TNS alias that you give when you connect to the remote database.  WALLET: Select this connection type to store credentials in an Oracle wallet.  Oracle SID: Select this connection type to uniquely identify a particular database on a system. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Oracle schema | Oracle schema name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table name | Database table name. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This checkbox is not available when the Use an existing connection checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Covert XML type to Java Type | Select this check box and then use the table to convert the types of the defined columns to Java types. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Use fetch size | Select this check box and in the Fetch size field displayed, specify the number of rows to fetch in one go from the database. The performance can be improved by tuning this fetch size to an appropriate value. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| No null values | Check this box to improve the performance if there are no null values. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for Oracle databases. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput -->
# tOracleInput

Last updated: 9/30/2026

Reads an Oracle database and extracts fields based on a query.

tOracleInput executes a database query with a strictly defined order
which must correspond to the schema definition. Then it passes on the field list to the
next component via a Main row link.

### In this section

* [tOracleInput Standard properties](/talend/en-US/components/8.0/oracle/toracleinput-standard-properties)
* [tOracleInput properties for Apache Spark Batch](/talend/en-US/components/8.0/oracle/toracleinput-properties-for-apache-spark-batch)

**Related concepts**  

* [Checking number format using a stored procedure](toracleconnection-toracleinput-toraclesp-tlogrow-checking-number-format-using-stored-procedure-standard-component-the)
* [Populating an Oracle data warehouse](toracleoutput-toracleinput-tmap-toracleinput-tmap-populating-oracle-data-warehouse-standard-component-enterprise "The following Java scenario creates a three-component Job that populates a data warehouse. A tOracleInput component reads your client data stored in the CLIENT table. A tMap component allows you to modify this data and the modifications are transmitted to the Leadfact table in the database through a tOracleOutput component.")
* [Truncating and inserting file data into an Oracle database](toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-truncating-and-inserting-file-data-into-oracle-database-standard-component-this)
* [Using context parameters when reading a table from an Oracle database](toracleinput-tlogrow-using-context-parameters-when-reading-table-from-oracle-database-standard-component-in-this)

**Related tasks**  

* [Using Oracle as a vector database](toracleconnection-toracleinput-toracleoutput-toracleclose-tfileinputdelimited-tmap-tlogrow-using-oracle-as-vector-db-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-properties-for-apache-spark-batch -->
# tOracleInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tOracleInput running in
the Spark Batch Job framework.

The Spark Batch
tOracleInput component belongs to the Databases family.

This component also allows you to connect and read data from a RDS Oracle
database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | The available drivers are:   * Oracle OCI: Select this connection type   to use Oracle Call Interface with a set of C-language software APIs that provide   an interface to the Oracle database. * Oracle Custom: Select this connection   type to access a clustered database. With this type of connection, the   Username and the Password fields are deactivated and you need to   enter the connection URL in the URL field   that is displayed.  For further information about the valid form of this URL, see [JDBC Connection   strings](http://www.dba-resources.com/oracle/jdbc-connection-strings-for-oracle-thin-driver/) from the Oracle documentation. * Oracle Service Name: Select this   connection type to use the TNS alias that you give when you connect to the   remote database. * WALLET: Select this connection type to   store credentials in an Oracle wallet. * Oracle SID: Select this connection type   to uniquely identify a particular database on a system. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Oracle schema | Oracle schema name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to be   processed and passed on to the next component. The schema is either   Built-in or stored remotely in the   Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table Name | Type in the name of the table from which you need to read data. |
| Query type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  If you are using Spark V2.0 onwards, the Spark SQL does not recognize the prefix of a database table anymore. This means that you must enter only the table name without adding any prefix that indicates for example the schema this table belongs to.  For example, if you need to perform a query in a table *system.mytable*, in which the *system* prefix indicates the schema that the *mytable* table belongs to, in the query, you must enter *mytable* only. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Spark SQL JDBC parameters | Add the JDBC properties supported by Spark SQL to this table. For a list of the user configurable properties, see [JDBC to other database](https://spark.apache.org/docs/latest/sql-programming-guide.html#jdbc-to-other-databases).  This component automatically set the *url*, *dbtable* and *driver* properties by using the configuration from the Basic settings tab. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Enable partitioning | Select this check box to read data in partitions.  Define, in double quotation marks, the following parameters to configure the partitioning:  * Partition column: the numeric column   used as partition key. * Lower bound of the partition stride   and Upper bound of the partition   stride: enter the upper bounds and the lower bound to determine   the partition stride. These bounds do not filter the table rows. All rows in   the table are partitioned and returned. * Number of partitions: the number of   partitions into which the table rows are split. Each Spark worker handles only   one of the partitions at a time.  The average size of the partitions is the result of the difference between the upper bound and the lower bound divided by the number of partitions, that is to say, (upperBound - lowerBound)/partitionNumber, while the first and the last partitions also include all the other rows that are not contained in the other partitions.  For example, to partition 1000 rows into 4 partitions, if you enter 0 for the lower bound and 1000 for the upper bound, each partition will contain 250 rows and so the partitioning is even. If you enter 250 for the lower bound and 750 for the upper bound, the second and the third partition will each contain 125 rows and the first and the last partitions each 375 rows. With this configuration, the partitioning is skewed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tOracleConfiguration component present in the same Job to connect to Oracle. You need to select the Use an existing connection check box and then select the tOracleConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-using-context-parameters-when-reading-table-from-oracle-database-standard-component-in-this -->
# Using context parameters when reading a table from an Oracle database

Last updated: 9/30/2026

In this scenario, we will read a table from an Oracle database using a context parameter to
refer to the table name.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-dropping-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-saving-and-executing-job-standard-component-press)
* [Related scenarios](/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-related-scenarios-standard-component-for)

**Related concepts**  

* [tOracleInput](toracleinput "Reads an Oracle database and extracts fields based on a query.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-truncating-and-inserting-file-data-into-oracle-database-standard-component-this -->
# Truncating and inserting file data into an Oracle database

Last updated: 9/30/2026

This scenario describes how to truncate the content of an Oracle database and
load the content of an input file. The related Job is composed of three components that
respectively creates the content, output this content into a file to be loaded into the Oracle
database after the database table has been truncated.

### In this section

* [Building the Job](/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-building-job-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-executing-job-standard-component-press)

**Related concepts**  

* [tOracleInput](toracleinput "Reads an Oracle database and extracts fields based on a query.")

**Related reference**  

* [tOracleBulkExec](toraclebulkexec "Offers gains in performance during operations performed on data of an Oracle database.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tOracleInput to open its
   Basic Settings view in the Component tab.
2. Select a connection type from the Connection
   Type drop-down list. In this example, it is *Oracle SID*.

   Select the version of the Oracle database to be used from the DB Version drop-down list. In this example, it is
   *Oracle 12-7*.

   In the Host field, enter the Oracle
   database server's IP address. In this example, it is *192.168.31.32*.

   In the Database field, enter the database
   name. In this example, it is *TALEND*.

   In the Oracle schema field, enter the
   Oracle schema name. In this example, it is *TALEND*.

   In the Username and Password fields, enter the authentication details.
3. Click the [...] button next to Edit schema to open the schema editor.
4. Click the [+] button to add four
   columns: *ID* and *AGE* of the integer type, *NAME* and *SEX* of the
   string type.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
5. Put the cursor in the Table Name field
   and press F5 for context parameter setting.
   The dialog box New Context Parameter pops
   up.

   For more information about context settings, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).
6. In the Name field, enter the context
   parameter name. In this example, it is *TABLE*.

   In the Default value field, enter the
   name of the Oracle database table to be queried. In this example, it is
   *PERSON*.
7. Click Finish to validate the setting. 

   The context parameter *context.TABLE*
   automatically appears in the Table Name
   field.
8. In the Query Type list, select Built-In. Then, click Guess
   Query to get the query statement. 

   ```
   "SELECT 
     "+context.TABLE+".\"ID\", 
     "+context.TABLE+".NAME, 
     "+context.TABLE+".SEX, 
     "+context.TABLE+".AGE
   FROM "+context.TABLE
   ```
9. Double-click tLogRow to open its
   Basic settings view in the Component tab.
10. In the Mode area, select Table (print values in cells of a table) for a
    better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-dropping-and-linking-components-standard-component-create -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in the design
   workspace or dropping them from the Palette: a tOracleInput
   component and a tLogRow component.
2. Connect tOracleInput to tLogRow using a Row > Main
   link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, the data in the Oracle database table *PERSON* is displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-building-job-standard-component-drop -->
# Building the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components: tOracleInput, tFileOutputDelimited and tOracleBulkExec from the Palette to the design workspace.
2. Connect the tOracleInput to the tFileOutputDelimited using a Row > Main link.
3. Connect the tOracleInput to the tOracleBulkExec using a OnSubjobOk trigger link.

## Results


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tOracleInput to open its
   Basic settings view.
2. Define the Oracle connection details. It is recommended to store the
   database connection details in the Metadata
   folder of the Repository tree view in order
   to retrieve them easily at any time in any Job.
3. Define the schema, if it is not stored in the Repository. In this example, the schema contains four
   columns as follows: *ID\_Contract*,
   *ID\_Client*, *Contract\_type* and
   *Contract\_Value*.
4. Define the tFileOutputDelimited component
   parameters, including output File Name,
   Row separator and Fields delimiter.
5. Double-click on the tOracleBulkExec to
   define the database populating properties.
6. In the Property Type list, select
   Repository if you stored the database
   connection details under the Metadata node
   of the Repository or select Built-in to define them manually. In this
   scenario, use the Built-in mode.
7. Set the connection parameters in the following fields: Host, Port,
   Database, Schema, Username, and
   Password.
8. Fill in the name of the Table to be
   populated and the Action on data to be
   carried out. In this use case, select insert.
9. In the Schema list, select Built-in, and click the [...] button next to the Edit
   schema field to define the structure of the data to be passed
   to the next component.
10. Click the Advanced settings view to
    configure the advanced settings of the component.
11. Select the Use existing control
    file check box if you want to use a control file (.ctl) storing the
    status of the physical structure of the database. Or, fill in the following fields
    manually: Record format, Specify .ctl file's INTO TABLE clause manually,
    Field terminated by, Use field enclosure, Use
    schema's Date Pattern to load Date field, Specify field condition, Preserve
    blanks, Trailing null columns,
    Load options, NLS Language and Set Parameter
    NLS\_TERRITORY according to your database.
12. In the Encoding list, select the
    encoding, or enter the encoding between double quotes if it does not exist
    in the list.
13. In the Output list, select to console to output the standard output of the
    database in the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 to run the Job. The log is shown
   in the console of the Run view and the
   table is populated with the parameter file data.

## Results

Related topic: see [Inserting data in bulk in MySQL database](/talend/en-US/components/8.0/mysql/tmysqloutputbulkexec-trowgenerator-inserting-data-in-bulk-in-mysql-database-standard-component-this).
