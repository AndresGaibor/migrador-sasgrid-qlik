<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt · versión 8.0 -->
# tJDBCSCDELT

Last updated: 9/30/2026

Tracks data changes in a source database table using SCD (Slowly Changing Dimensions)
Type 1 method and/or Type 2 method and writes both the current and historical data into a
specified SCD dimension table.

## tJDBCSCDELT Standard properties

These properties are used to configure tJDBCSCDELT running in the Standard Job framework.

The Standard
tJDBCSCDELT component belongs to two families: Business Intelligence and Databases.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`. |
| Driver JAR | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Driver Class | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| Username and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| DB Schema | Specify the name of the database schema. For the database that does not support schema, just leave this field empty. |
| Source table | Specify the name of the source input table whose data changes will be captured by SCD. |
| Table | Specify the name of the dimension table into which the data captured by SCD will be written. |
| Action on table | Select an operation to be performed on the table defined.   * None: No operation is carried out. * Drop and create table: The table is removed   and created again. * Create table: The table does not exist and   gets created. * Create table if does not exist: The table is   created if it does not exist. * Drop table if exist and create: The table is   removed if it already exists and created again. * Clear table: The table content is   deleted. You have the possibility to rollback the operation. * Truncate table: The table content is   deleted. You do not have the possibility to rollback the operation. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Surrogate key | Set the column where the generated surrogate key will be stored. A surrogate key can be generated based on a method selected on the Creation list. |
| Creation | Select any of the following methods to be used for generating the surrogate key.   * Auto   increment: an auto-incrementing integer will be used. * DB   sequence: a sequence will be used. |
| Source keys | Specify one or more columns used as the key(s) that ensure the unicity of the incoming data. |
| Use SCD type 0 fields | Select this check box and in the SCD type 0 fields table displayed, specify the column(s) whose value changes will be tracked using Type 0 SCD.  This option only supports these databases: Exasol, MySql, MSSql, Oracle, Postgresql, and Snowflake. |
| Use SCD type 1 fields | Select this check box and in the SCD type 1 fields table displayed, specify the column(s) whose value changes will be tracked using Type 1 SCD. |
| SCD type 1 fields | Click the [+] button to add as many rows as needed, each row for a column, then click the right side of the cell and from the drop-down list displayed select the column whose value changes will be tracked using Type 1 SCD. |
| Use SCD type 2 fields | Select this check box and in the SCD type 2 fields table displayed, specify the column(s) whose value changes will be tracked using Type 2 SCD. |
| SCD type 2 fields | Click the [+] button to add as many rows as needed, each row for a column. Click the arrow on the right side of the cell and select the column whose value changes will be tracked using Type 2 SCD from the drop-down list displayed .  This table is available only when the Use SCD type 2 fields option is selected. |
| Start date | Specify the column that holds the start date for type 2 SCD.  This list is available only when the Use SCD type 2 fields option is selected. |
| End date | Specify the column that holds the end date for type 2 SCD.  This list is available only when the Use SCD type 2 fields option is selected.  Information noteNote: To avoid duplicated change records, it is recommended to select a column that can identify each change for this field. |
| Log active status | Select this check box and from the Active field drop-down list displayed, select the column that holds the true or false status value, which helps to spot the active record for type 2 SCD.  This option is available only when the Use SCD type 2 fields option is selected. |
| Log versions | Select this check box and from the Version field drop-down list displayed, select the column that holds the version number of the record for type 2 SCD.  This option is available only when the Use SCD type 2 fields option is selected. |
| Mapping | Specify the metadata mapping file for the database to be used. The metadata mapping file is used for the data type conversion between database and Java. For more information about the metadata mapping, see the related documentation for Type mapping. Information noteNote: You can use Hive mapping to support Databricks Delta Lake. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Source fields value include Null | Select this check box to allow the source columns to have Null values. The source columns here refer to the fields defined in the SCD type 1 fields and SCD type 2 fields tables. |
| Debug mode | Select this check box to display each step during processing the data in a database. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component of a Job or subJob. |

**Related concepts**  

* [Tracking data changes in a PostgreSQL table using the tPostgreSQLSCDELT component](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-changes-in-postgresql-table-using-tpostgresqlscdelt-component-standard-component-the "This scenario describes a Job that captures the employee data changes in a PostgreSQL table using SCD (Slowly Changing Dimensions) Type 1 and Type 2 methods implemented by the tPostgreSQLSCDELT component, and writes both the current and historical data in a SCD dimension table.")
* [Tracking data changes in a Snowflake table using the tJDBCSCDELT component](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-changes-in-snowflake-table-using-tjdbcscdelt-component-standard-component-the "This scenario describes a Job that captures the employee data changes in a Snowflake table using SCD (Slowly Changing Dimensions) Type 1 and Type 2 methods implemented by the tJDBCSCDELT component, and writes both the current and historical data in a SCD dimension table.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-changes-in-postgresql-table-using-tpostgresqlscdelt-component-standard-component-the -->
# Tracking data changes in a PostgreSQL table using the tPostgreSQLSCDELT component

Last updated: 9/30/2026

This scenario describes a Job that captures the employee data changes in a PostgreSQL
table using SCD (Slowly Changing Dimensions) Type 1 and Type 2 methods implemented by the
tPostgreSQLSCDELT component, and writes both the current and historical data in a SCD
dimension table.

The input data contains various employee details including `name`,
`role`, `salary`, and another
`id` column is added to help ensuring the unicity of the input
data.

At first, the following employee data is inserted to a new Snowflake table.

```
#id;name;role;salary
1;Mark Smith;tester;11000.00
2;Thomas Johnson;developer;12000.00
3;Teddy Brown;tester;13000.00
```

Later, the table is updated with the following renewed employee data.

```
#id;name;role;salary
1;Mark Smith;tester;15000.00
2;Thomas Johnson;tester;18000.00
3;Teddy Brown;writer;17000.00
4;John Clinton;developer;19000.00
```

You can see the role of Thomas Johnson is changed from
developer to tester, the role of Teddy
Brown is changed from tester to writer, and his
salary is raised from 13000.00 to 17000.00. Besides, a new
employee record with id 4 is inserted. In this scenario,

* the existing name and role data will be overwritten by the new data, so SCD Type 1 method
  will be performed on them, and
* the full history of the salary data will be retained, and a new record with the changed
  data will be always created and the previous record will be closed, so SCD Type 2 method
  will be performed on it.

For more information about SCD types, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology).

### In this section

* [Creating a Job for tracking data changes in a PostgreSQL table using tPostgresqlSCDELT](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-job-for-tracking-data-changes-in-postgresql-table-using-tpostgresqlscdelt-standard-component-create)
* [Opening a connection to a PostgreSQL database](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-opening-connection-to-postgresql-database-standard-component)
* [Creating a PostgreSQL table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-postgresql-table-standard-component)
* [Inserting data into the new PostgreSQL table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-inserting-data-into-new-postgresql-table-standard-component)
* [Tracking inserted data changes and writing the changes into a SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-inserted-data-changes-and-writing-changes-into-scd-dimension-table-standard-component)
* [Retrieving the data updates from the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-updates-from-scd-dimension-table-standard-component)
* [Updating data in the Postgresql table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-updating-data-in-postgresql-table-standard-component)
* [Tracking data update changes and writing the changes into the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-update-changes-and-writing-changes-into-scd-dimension-table-standard-component)
* [Retrieve the data update changes from the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieve-data-update-changes-from-scd-dimension-table-standard-component)
* [Executing the Job to track data changes in a PostgreSQL table using tPostgreSQLSCDELT](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-executing-job-to-track-data-changes-in-postgresql-table-using-tpostgresqlscdelt-press)

**Related reference**  

* [tJDBCSCDELT](tjdbcscdelt "Tracks data changes in a source database table using SCD (Slowly Changing Dimensions) Type 1 method and/or Type 2 method and writes both the current and historical data into a specified SCD dimension table.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tJDBCInput](/talend/en-US/components/8.0/jdbc/tjdbcinput)
* [tJDBCConnection](/talend/en-US/components/8.0/jdbc/tjdbcconnection)
* [tJDBCRow](/talend/en-US/components/8.0/jdbc/tjdbcrow)
* [tJDBCOutput](/talend/en-US/components/8.0/jdbc/tjdbcoutput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-changes-in-snowflake-table-using-tjdbcscdelt-component-standard-component-the -->
# Tracking data changes in a Snowflake table using the tJDBCSCDELT component

Last updated: 9/30/2026

This scenario describes a Job that captures the employee data changes in a Snowflake
table using SCD (Slowly Changing Dimensions) Type 1 and Type 2 methods implemented by the
tJDBCSCDELT component, and writes both the current and historical data in a SCD dimension
table.

The input data contains various employee details including
`name`, `role`, `salary`, and
another `id` column is added to help ensuring the unicity of the input
data.

At first, the following employee data is inserted to a new Snowflake
table.

```
#id;name;role;salary
111;Mark Smith;tester;15000.00
222;Thomas Johnson;developer;18000.00
333;Teddy Brown;tester;16000.00
```

Later, the table is updated with the following renewed employee data.

```
#id;name;role;salary
111;Mark Smith;tester;15000.00
222;Thomas Johnson;tester;18000.00
333;Teddy Brown;writer;17000.00
444;John Clinton;developer;19000.00
```

You can see the role of Thomas Johnson is changed from
developer to tester, the role of Teddy
Brown is changed from tester to writer, and his
salary is raised from 16000.00 to 17000.00. Besides, a new
employee record with id 444 is inserted. In this scenario,

* the existing name and role data will be overwritten by the new data, so
  SCD Type 1 method will be performed on them, and
* the full history of the salary data will be retained, and a new record
  with the changed data will be always created and the previous record will be closed, so
  SCD Type 2 method will be performed on it.

For more information about SCD types, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology).

### In this section

* [Creating a Job for tracking data changes in a Snowflake table using tJDBCSCDELT](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-job-for-tracking-data-changes-in-snowflake-table-using-tjdbcscdelt-standard-component-create)
* [Opening a connection to a Snowflake database](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-opening-connection-to-snowflake-database-standard-component)
* [Creating a Snowflake table and a Snowflake sequence](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-snowflake-table-and-snowflake-sequence-standard-component)
* [Inserting data into the new Snowflake table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-inserting-data-into-new-snowflake-table-standard-component)
* [Tracking data insertion changes and writing the changes into a SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-insertion-changes-and-writing-changes-into-scd-dimension-table-standard-component)
* [Retrieving the data insertion updates from the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-insertion-updates-from-scd-dimension-table-standard-component)
* [Updating data in the Snowflake table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-updating-data-in-snowflake-table-standard-component)
* [Tracking and writing changes into the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-and-writing-changes-into-scd-dimension-table-standard-component)
* [Retrieve changes from the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieve-changes-from-scd-dimension-table-standard-component)
* [Executing the Job to track data changes in a Snowflake table using tJDBCSCDELT](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-executing-job-to-track-data-changes-in-snowflake-table-using-tjdbcscdelt-press)

**Related reference**  

* [tJDBCSCDELT](tjdbcscdelt "Tracks data changes in a source database table using SCD (Slowly Changing Dimensions) Type 1 method and/or Type 2 method and writes both the current and historical data into a specified SCD dimension table.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tJDBCInput](/talend/en-US/components/8.0/jdbc/tjdbcinput)
* [tJDBCConnection](/talend/en-US/components/8.0/jdbc/tjdbcconnection)
* [tJDBCRow](/talend/en-US/components/8.0/jdbc/tjdbcrow)
* [tJDBCOutput](/talend/en-US/components/8.0/jdbc/tjdbcoutput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-job-for-tracking-data-changes-in-postgresql-table-using-tpostgresqlscdelt-standard-component-create -->
# Creating a Job for tracking data changes in a PostgreSQL table using tPostgresqlSCDELT

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tPostgreSQLConnection
   component, a tCreateTable component, two
   tFixedFlowInput components, two
   tPostgreSQL Input components, two
   tPostgreSQLOutput components, two
   tPostgreSQLSCDELT components, and two
   tLogRow components to the Job.
2. Link the first tFixedFlowInput component to the first
   tPostgreSQLOutput component using a Row > Main connection.
3. Do the same to link the first tPostgreSQLInput component
   to the first tLogRow component, the second
   tFixedFlowInput component to the second
   tPostgreSQLOutput component, and the second
   tPostgreSQLInput component to the second
   tLogRow component.
4. Link the tPostgreSQLConnection component to the
   tCreateTable component using a Trigger > On Subjob Ok connection.
5. Do the same to link the first tFixedFlowInput component
   to the first tPostgreSQLSCDELT component, the first
   tPostgreSQLSCDELT component to the first
   tPostgreSQLInput component, the first
   tPostgreSQLInput component to the second
   tFixedFlowInput component, the second
   tFixedFlowInput component to the second
   tPostgreSQLSCDELT component, the second
   tPostgreSQLSCDELT component to the second
   tPostgreSQLInput component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-postgresql-table-standard-component -->
# Creating a PostgreSQL table

Last updated: 9/30/2026

## Procedure

1. Double-click the tCreateTable component to open its
   Basic settings view.
2. In the Basic settings view, and from the
   Database Type list, select Postgresql for this
   scenario.
3. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tPostgreSQLConnection_1` in this example.
4. In the Table Name field, fill in a name for the table to
   be created, `employee` in this example.
5. From the Table Action list, select Create
   table if not exist.
6. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   four columns: `id` of Integer type as the primary key,
   `name` and `role` of String type,
   and `salary` of Double type. 

   In the end, a new table `employee` is created to store
   the employee data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-executing-job-to-track-data-changes-in-postgresql-table-using-tpostgresqlscdelt-press -->
# Executing the Job to track data changes in a PostgreSQL table using tPostgreSQLSCDELT

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save
   the Job.
2. Press F6 to execute the
   Job.

   As shown above, the old role `developer` for
   `Thomas Johnson` is overwritten directly by the new
   role `tester` because SCD Type 1 is performed on the
   `role` column, and a new record with the surrogate
   key value set to `26` is created for `Teddy
   Brown`'s salary update from `13000.00`
   to `17000.00` because SCD Type 2 is performed on the
   `salary` column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-inserting-data-into-new-postgresql-table-standard-component -->
# Inserting data into the new PostgreSQL table

Last updated: 9/30/2026

## Procedure

1. Double-click the first tFixedFlowInput component to open
   its Basic settings view.
2. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   four columns: `id` of Integer type as the primary key,
   `name` and `role` of String type,
   and `salary` of Double type.
3. Click OK to save the schema changes. In the pop-up
   dialog box, click Yes to propagate the
   schema to the next component.
4. Select `Use Inline Content` in the
   Mode area. Then in the Content
   field displayed, enter the following employee data to be inserted.

   ```
   1;Mark Smith;tester;11000.00
   2;Thomas Johnson;developer;12000.00
   3;Teddy Brown;tester;13000.00
   ```
5. Double-click the first tPostgreSQLOutput component to
   open its Basic settings view.
6. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, and then
   select the connection component to reuse the connection created by it,
   `tPostgreSQLConnection_1` in this example.
7. In the Table field, enter the name of the table into
   which the employee data will be written, `employee` in this
   example.
8. In the Action on table drop-down list, select
   `Default`.
9. In the Action on data drop-down list, select
   `Insert` to insert the employee data transferred from
   the first tFixedFlowInput component.
10. Click the [...] button next to Edit
    schema to check whether the schema of tPostgreSQLOutput is the
    same as the schema of tFixedFlowInput.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-opening-connection-to-postgresql-database-standard-component -->
# Opening a connection to a PostgreSQL database

Last updated: 9/30/2026

## Procedure

1. Double-click the tPostgreSQLConnection component to open
   its Basic settings view.
2. In the Host, Port, Database, Schema, Username, and Password fields, enter the information required for the
   connection to the PostgreSQL database.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieve-data-update-changes-from-scd-dimension-table-standard-component -->
# Retrieve the data update changes from the SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the second tPostgreSQLInput component to
   open its Basic settings view.
2. Repeat [2](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-updates-from-scd-dimension-table-standard-component) through [5](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-updates-from-scd-dimension-table-standard-component) in the procedure [Retrieving the data updates from the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-updates-from-scd-dimension-table-standard-component) to configure the second tPostgreSQLInput component.
3. Double-click the second tLogRow component and in the
   Mode area on its Basic
   settings view, select `Table` to display
   the retrieved data in a table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-updates-from-scd-dimension-table-standard-component -->
# Retrieving the data updates from the SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the first tPostgreSQLInput component to
   open its Basic settings view.
2. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tPostgreSQLConnection_1` in this example.
3. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   nine columns: `sk` and `id` of Integer
   type as the primary key, `name` and
   `role` of String type, `salary` of
   Double type, `start_date` and
   `end_date` of Date type with the Date Pattern
   `yyyy-MM-dd`, and `active_status`
   and `version` of Integer type. When done, click
   OK to save the changes and close the dialog
   box.

   The schema of the first tPostgreSQLInput component is
   the same as the schema of the tPostgreSQLSCDELT1
   component, you can just copy and paste it.
4. In the Query field, enter the SQL command used to
   retrieve data from the SCD dimension table, `select * from
   employee_scd` in this example.
5. In the Table Name field, enter the name of the SCD
   dimension table where you will retrieve the data updates,
   `employee_scd` in this example.
6. Double-click the first tLogRow component and in the
   Mode area on its Basic
   settings view, select `Table` to display
   the retrieved data in a table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-update-changes-and-writing-changes-into-scd-dimension-table-standard-component -->
# Tracking data update changes and writing the changes into the SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the second tPostgreSQLSCDELT component to
   open its Basic settings view.
2. Repeat [2](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-inserted-data-changes-and-writing-changes-into-scd-dimension-table-standard-component) through [14](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-inserted-data-changes-and-writing-changes-into-scd-dimension-table-standard-component) in the procedure [Tracking inserted data changes and writing the changes into a SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-inserted-data-changes-and-writing-changes-into-scd-dimension-table-standard-component) to configure the second tPostgreSQLSCDELT
   component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-inserted-data-changes-and-writing-changes-into-scd-dimension-table-standard-component -->
# Tracking inserted data changes and writing the changes into a SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the first tPostgreSQLSCDELT component to
   open its Basic settings view.
2. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tPostgreSQLConnection_1` in this example.
3. In the Source table field, enter the name of the table
   whose data changes will be captured, `employee` in this
   example.
4. In the Table field, enter the name of the SCD dimension
   table that will store both the current and historical employee data,
   `employee_scd` in this example.
5. Select `Create table` from the Action on
   table drop-down list to create the SCD dimension table.
6. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   nine columns: `sk` ( as the primary key) and
   `id` of Integer type, `name` and
   `role` of String type, `salary` of
   Double type, `start_date` and
   `end_date` of Date type with the Date Pattern
   `dd-MM-yyyy`, and `active_status`
   and `version` of Integer type. When done, click
   OK to save the changes and close the dialog
   box.
7. From the Surrogate key drop-down list, select the name
   of the column that will be used as the primary key of the SCD dimension table,
   `sk` in this example.
8. Select `DB sequence` from the
   Creation drop-down list and in the
   Sequence field displayed, enter the name of the
   PostgreSQL sequence used to generate the surrogate key for the SCD Type 2
   method, `employee_sequence` in this example.
9. Click the [+] button below the Source
   keys table to add a new line, and click the
   Name cell and select the key column of the source
   table from the drop-down list, `id` in this example.
10. Select the Use SCD type 1 fields check box, click the
    [+] button below the SCD type 1
    fields table twice to add two lines. Then click each cell and
    from the drop-down list, select the column on which the SCD Type 1 method will
    be performed. In this example, they are `name` and
    `role`.
11. Select the Use SCD type 2 fields check box, click the
    [+] button below the SCD type 2
    fields table to add a line. Then click the cell and select the
    column on which the SCD Type 2 method will be performed. In this example, it is
    `salary`.
12. From the Start date and End date
    drop-down lists, select the columns used to hold the start date and end date
    values for the SCD Type 2 method respectively, `start_date`
    and `end_date` in this example.
13. Select the Log active status check box and from the
    Active field drop-down list displayed, select the
    column used to hold the active status value for the SCD Type 2 method, which
    helps identify the active records, `active_status` in this
    example.
14. Select the Log versions check box and from the
    Version field drop-down list, select the column used
    to hold the version number of the records for the SCD Type 2 method,
    `version` in this example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-updating-data-in-postgresql-table-standard-component -->
# Updating data in the Postgresql table

Last updated: 9/30/2026

## Procedure

1. Double-click the second tFixedFlowInput component to
   open its Basic settings view.
2. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   four columns: `id` of Integer type as the primary key,
   `name` and `role` of String type,
   and `salary` of Double type.

   This schema is the same as the schema of the first
   tFixedFlowInput component, you can just copy and
   paste it.
3. Click OK to save the schema changes. In the pop-up
   dialog box, click Yes to propagate the
   schema to the next component.
4. Select `Use Inline Content` in the
   Mode area. Then in the Content
   field displayed, enter the following employee data to update the existing
   data.

   ```
   1;Mark Smith;tester;15000.00
   2;Thomas Johnson;tester;18000.00
   3;Teddy Brown;writer;17000.00
   4;John Clinton;developer;19000.00
   ```
5. Double-click the second tPostgreSQLOutput component to
   open its Basic settings view.
6. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tPostgreSQLConnection_1` in this example.
7. In the Table field, enter the name of the table, in
   which the data will be updated, `employee` in this
   example.
8. Select `Default` from the Action on
   table drop-down list.
9. Select `Insert or update` from the Action on
   data drop-down list.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-job-for-tracking-data-changes-in-snowflake-table-using-tjdbcscdelt-standard-component-create -->
# Creating a Job for tracking data changes in a Snowflake table using tJDBCSCDELT

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tJDBCConnection component,
   two tJDBCRow components, two
   tFixedFlowInput components, two
   tJDBCOutput components, two
   tJDBCSCDELT components, two
   tJDBCInput components, and two
   tLogRow components to the Job.
2. Link the first tFixedFlowInput component to the first
   tJDBCOutput component using a Row > Main connection.
3. Do the same to link the first tJDBCInput component to
   the first tLogRow component, the second
   tFixedFlowInput component to the second
   tJDBCOutput component, and the second
   tJDBCInput component to the second
   tLogRow component.
4. Link the tJDBCConnection component to the first
   tJDBCRow component using a Trigger > On Subjob Ok connection.
5. Do the same to link the first tJDBCRow component to the
   second tJDBCRow component, the second
   tJDBCRow component to the first
   tFixedFlowInput component, the first
   tFixedFlowInput component to the first
   tJDBCSCDELT component, the first
   tJDBCSCDELT component to the first
   tJDBCInput component, the first
   tJDBCInput component to the second
   tFixedFlowInput component, the second
   tFixedFlowInput component to the second
   tJDBCSCDELT component, the second
   tJDBCSCDELT component to the second
   tJDBCInput component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-creating-snowflake-table-and-snowflake-sequence-standard-component -->
# Creating a Snowflake table and a Snowflake sequence

Last updated: 9/30/2026

## Procedure

1. Double-click the first tJDBCRow component to open its
   Basic settings view.
2. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tJDBCConnection_1` in this example.
3. In the Query field, enter the SQL command used to create
   a new table.

   In this example, the SQL command is `CREATE OR REPLACE TABLE
   employee (id INTEGER, name VARCHAR(50), role VARCHAR(50), salary DOUBLE,
   PRIMARY KEY(id))`, which creates a new table
   `employee` with four columns, `id`
   of INTEGER type as the primary key, `name` and
   `role` of VARCHAR type, and
   `salary` of DOUBLE type. This table will be used to
   store the employee data.
4. Double-click the second tJDBCRow component to open its
   Basic settings view.
5. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tJDBCConnection_1` in this example.
6. In the Query field, enter the SQL command used to create
   a Snowflake sequence.

   In this example, the SQL command is `create or replace sequence
   employee_sequence`, which creates a new sequence
   `employee_sequence`. This sequence will be used by the
   tJDBCSCDELT component to generate the surrogate key
   for SCD Type 2 method.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-executing-job-to-track-data-changes-in-snowflake-table-using-tjdbcscdelt-press -->
# Executing the Job to track data changes in a Snowflake table using tJDBCSCDELT

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save
   the Job.
2. Press F6 to execute the
   Job.

   As shown above, the old role `developer` for
   `Thomas Johnson` is overwritten directly by the new
   role `tester` because SCD Type 1 is performed on the
   `role` column, and a new record with the surrogate
   key value set to `4` is created for `Teddy
   Brown`'s salary update from `16000.00`
   to `17000.00` because SCD Type 2 is performed on the
   `salary` column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-inserting-data-into-new-snowflake-table-standard-component -->
# Inserting data into the new Snowflake table

Last updated: 9/30/2026

## Procedure

1. Double-click the first tFixedFlowInput component to open
   its Basic settings view.
2. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   four columns: `id` of Integer type as the primary key,
   `name` and `role` of String type,
   and `salary` of Double type.
3. Click OK to save the schema changes. In the pop-up
   dialog box, click Yes to propagate the
   schema to the next component.
4. Select `Use Inline Content` in the
   Mode area. Then in the Content
   field displayed, enter the following employee data to be inserted.

   ```
   111;Mark Smith;tester;15000.00
   222;Thomas Johnson;developer;18000.00
   333;Teddy Brown;tester;16000.00
   ```
5. Double-click the first tJDBCOutput component to open its
   Basic settings view.
6. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tJDBCConnection_1` in this example.
7. In the Table field, enter the name of the table into
   which the employee data will be written, `employee` in this
   example.
8. In the Action on data drop-down list, select
   `Insert` to insert the employee data transferred from
   the first tFixedFlowInput component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-opening-connection-to-snowflake-database-standard-component -->
# Opening a connection to a Snowflake database

Last updated: 9/30/2026

## Procedure

1. Double-click the tJDBCConnection component to open its
   Basic settings view.
2. In the JDBC URL field, enter the connection string to
   connect to Snowflake using the JDBC driver.

   For more information about how to use the JDBC driver to connect to Snowflake
   and how to specify the connection string, see [JDBC Driver Connection String](https://docs.snowflake.net/manuals/user-guide/jdbc-configure.html#jdbc-driver-connection-string).
3. Click the [+] button below the Driver
   JAR table to add a line, and in the Jar
   name cell of the new line, enter the name of the jar file for
   the Snowflake JDBC driver, `snowflake-jdbc-3.2.2.jar` in
   this example.
4. In the Driver Class field, enter the Snowflake JDBC
   driver class, `com.snowflake.client.jdbc.SnowflakeDriver`
   in this example.
5. In the Username and Password
   fields, enter the authentication information accordingly.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieve-changes-from-scd-dimension-table-standard-component -->
# Retrieve changes from the SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the second tJDBCInput component to open its
   Basic settings view.
2. Repeat [2](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-insertion-updates-from-scd-dimension-table-standard-component) through [4](tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-insertion-updates-from-scd-dimension-table-standard-component) in the procedure [Retrieving the data insertion updates from the SCD dimension table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-insertion-updates-from-scd-dimension-table-standard-component) to configure the second tJDBCInput component.
3. Double-click the second tLogRow component and in the
   Mode area on its Basic
   settings view, select `Table` to display
   the retrieved data in a table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-retrieving-data-insertion-updates-from-scd-dimension-table-standard-component -->
# Retrieving the data insertion updates from the SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the first tJDBCInput component to open its
   Basic settings view.
2. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tJDBCConnection_1` in this example.
3. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   nine columns: `sk` and `id` of Integer
   type as the primary key, `name` and
   `role` of String type, `salary` of
   Double type, `start_date` and
   `end_date` of Date type with the Date Pattern
   `yyyy-MM-dd`, and `active_status`
   and `version` of Integer type. When done, click
   OK to save the changes and close the dialog
   box.

   The schema of the first tJDBCInput component is the
   same as the schema of the tJDBCSCDELT component, you
   can just copy and paste it.
4. In the Query field, enter the SQL command used to
   retrieve data from the SCD dimension table, `select * from
   employee_scd` in this example.
5. Double-click the first tLogRow component and in the
   Mode area on its Basic
   settings view, select `Table` to display
   the retrieved data in a table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-and-writing-changes-into-scd-dimension-table-standard-component -->
# Tracking and writing changes into the SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the second tJDBCSCDELT component to open
   its Basic settings view.
2. Select None from the Action on table
   dropdown list.
3. For the other settings, repeat the steps in the procedure [Tracking data insertion changes and writing the changes into a SCD dimension
   table](/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-insertion-changes-and-writing-changes-into-scd-dimension-table-standard-component) to configure the second tJDBCSCDELT
   component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-tracking-data-insertion-changes-and-writing-changes-into-scd-dimension-table-standard-component -->
# Tracking data insertion changes and writing the changes into a SCD dimension table

Last updated: 9/30/2026

## Procedure

1. Double-click the first tJDBCSCDELT component to open its
   Basic settings view.
2. Select the Use an existing connection checkbox and from
   the Component List dropdown list displayed, select the
   connection component to reuse the connection created by it,
   `tJDBCConnection_1` in this example.
3. In the Source table field, enter the name of the table
   whose data changes will be captured, `employee` in this
   example.
4. In the Table field, enter the name of the SCD dimension
   table that will store both the current and historical employee data,
   `employee_scd` in this example.
5. Select Drop table if exists and create from the
   Action on table dropdown list to create the SCD
   dimension table.
6. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   nine columns: `sk` and `id` of Integer
   type as the primary key, `name` and
   `role` of String type, `salary` of
   Double type, `start_date` and
   `end_date` of Date type with the Date Pattern
   `yyyy-MM-dd`, and `active_status`
   and `version` of Integer type. When done, click
   OK to save the changes and close the dialog
   box.
7. From the Surrogate key drop-down list, select the name
   of the column that will be used as the primary key of the SCD dimension table,
   `sk` in this example.
8. Select `DB sequence` from the
   Creation dropdown list and in the
   Sequence field displayed, enter the name of the
   Snowflake sequence used to generate the surrogate key for the SCD Type 2
   method.
9. Click the [+] button below the Source
   keys table to add a new line, and click the
   Name cell and select the key column of the source
   table from the dropdown list, `id` in this example.
10. Select the Use SCD type 1 fields checkbox, click the
    [+] button below the SCD type 1
    fields table twice to add two lines. Then click each cell and
    from the dropdown list, select the column on which the SCD Type 1 method will be
    performed. In this example, they are `name` and
    `role`.
11. Select the Use SCD type 2 fields checkbox, click the
    [+] button below the SCD type 2
    fields table to add a line. Then click the cell and select the
    column on which the SCD Type 2 method will be performed. In this example, it is
    `salary`.
12. From the Start date and End date
    drop-down lists, select the columns used to hold the start date and end date
    values for the SCD Type 2 method respectively, `start_date`
    and `end_date` in this example.
13. Select the Log active status checkbox and from the
    Active field dropdown list displayed, select the
    column used to hold the active status value for the SCD Type 2 method, which
    helps identify the active records, `active_status` in this
    example.
14. Select the Log versions checkbox and from the
    Version field dropdown list, select the column used
    to hold the version number of the records for the SCD Type 2 method,
    `version` in this example.
15. Select `Mapping Snowflake` from the
    Mapping dropdown list to use the Snowflake metadata
    mapping file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tjdbcscdelt-tfixedflowinput-tjdbcinput-tlogrow-updating-data-in-snowflake-table-standard-component -->
# Updating data in the Snowflake table

Last updated: 9/30/2026

## Procedure

1. Double-click the second tFixedFlowInput component to
   open its Basic settings view.
2. Click the [...] button next to Edit
   schema and in the pop-up dialog box, define the schema by adding
   four columns: `id` of Integer type as the primary key,
   `name` and `role` of String type,
   and `salary` of Double type.

   This schema is the same as the schema of the first
   tFixedFlowInput component, you can just copy and
   paste it.
3. Click OK to save the schema changes. In the pop-up
   dialog box, click Yes to propagate the
   schema to the next component.
4. Select `Use Inline Content` in the
   Mode area. Then in the Content
   field displayed, enter the following employee data to update the existing
   data.

   ```
   111;Mark Smith;tester;15000.00
   222;Thomas Johnson;tester;18000.00
   333;Teddy Brown;writer;17000.00
   444;John Clinton;developer;19000.00
   ```
5. Double-click the second tJDBCOutput component to open
   its Basic settings view.
6. Select the Use an existing connection check box and from
   the Component List drop-down list displayed, select the
   connection component to reuse the connection created by it,
   `tJDBCConnection_1` in this example.
7. In the Table field, enter the name of the table, in
   which the data will be updated, `employee` in this
   example.
8. Select `Insert or update` from the Action on
   data drop-down list.
