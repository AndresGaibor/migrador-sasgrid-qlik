<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd · versión 8.0 -->
# tMysqlSCD

Last updated: 9/30/2026

Reflects and tracks changes in a dedicated MySQL SCD table.

tMysqlSCD addresses Slowly Changing Dimension needs,
reading regularly a source of data and logging the changes into a dedicated SCD table.

## tMysqlSCD Standard properties

These properties are used to configure tMysqlSCD running in the Standard Job framework.

The Standard
tMysqlSCD component belongs to the Business Intelligence and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository. * Built-in: No property data stored   centrally. * Repository: Select the Repository file   where properties are stored. The following fields are pre-filled in using   fetched data. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| DB Version | Select the Mysql version you are using. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created and   stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists   and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| SCD Editor | The SCD editor helps to build and configure the data flow for slowly changing dimension outputs.  For more information, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology). |
| Use memory saving mode | Select this check box to maximize system performance. |
| Source keys include Null | Select this check box to allow the source key columns to have Null values.  Information noteWarning: Special attention should be paid to the uniqueness of the source key(s) values when this option is selected. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| End date time details | Specify the time value of the SCD end date time setting in the format of *HH:mm:ss*. The default value for this field is *12:00:00*.  This field appears only when SCD Type 2 is used and Fixed year value is selected for creating the SCD end date. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Debug mode | Select this check box to display each step during processing entries in a database. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as Output component. It requires an Input component and Row main link as input. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | This component does not support using SCD type 0 together with other SCD types. |

**Related concepts**  

* [Tracking data changes using Slowly Changing Dimensions (type 0 through type 3)](tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-tracking-data-changes-using-slowly-changing-dimensions-type-0-through-type-3-standard-component-the "This scenario describes a Job that stores and manages both the current and historical employee data in a MySQL table using SCD (Slowly Changing Dimensions).")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-tracking-data-changes-using-slowly-changing-dimensions-type-0-through-type-3-standard-component-the -->
# Tracking data changes using Slowly Changing Dimensions (type 0 through type 3)

Last updated: 9/30/2026

This scenario describes a Job that stores and manages both the current
and historical employee data in a MySQL table using SCD (Slowly Changing
Dimensions).

The input data contains various employee details including *name*, *age*, *role*, and *salary*, and another *id* column is added to help ensuring the
unicity of the input data.

At first, the following employee data is inserted to a new MySQL table using
SCD:

```
id;name;age;role;salary
1;Mark Smith;30;tester;11000.00
2;Thomas Johnson;32;developer;12000.00
3;Teddy Brown;33;tester;13000.00
```

Then the table is updated using SCD with the following renewed employee
data.

```
id;name;age;role;salary
1;Mark Smith;31;tester;11000.00
2;Thomas Johnson;32;developer;12000.00
3;Teddy Brown;33;writer;13500.00
```

You can see the age of *Mark Smith* is updated from *30* to *31*, the role of *Teddy
Brown* is changed from *tester* to *writer*, and
his salary is raised from *13000.00* to *13500.00*. In
this scenario,

* we don't want to track the data changes for the *name*
  field, so we will perform Type 0 SCD on it,
* we want the new *age* data to overwrite the existing
  data, so we will perform Type 1 SCD on it,
* we want to retain the full history of the *role* data,
  and always create a new record with the changed data and close the previous record, so we
  will perform Type 2 SCD on it,
* we want to keep the current and previous dimension values for the *salary* field, so we will perform Type 3 SCD on it.

For more information about SCD types, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology).

### In this section

* [Creating a Job for tracking data changes in MySQL using SCD](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-creating-job-for-tracking-data-changes-in-mysql-using-scd-standard-component-create?id=4528)
* [Opening a connection to a MySQL database](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-opening-connection-to-mysql-database-standard-component?id=4529)
* [Inserting the employee data into a MySQL table using SCD](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-inserting-employee-data-into-mysql-table-using-scd-standard-component?id=4530)
* [Retrieving the inserted employee data from MySQL](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-inserted-employee-data-from-mysql-standard-component?id=4531)
* [Updating the employee data in MySQL using SCD](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-updating-employee-data-in-mysql-using-scd-standard-component?id=4532)
* [Retrieving the updated employee data from MySQL](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-updated-employee-data-from-mysql-standard-component-repeat?id=4533)
* [Closing the connection to the MySQL database](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-closing-connection-to-mysql-database-standard-component?id=4534)
* [Executing the Job to track data changes in MySQL using SCD](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-executing-job-to-track-data-changes-in-mysql-using-scd-standard-component-press?id=4535)

**Related information**  

* [tMysqlSCD](/talend/en-US/components/8.0/scd/tmysqlscd)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)
* [tMysqlConnection](/talend/en-US/components/8.0/mysql/tmysqlconnection)
* [tMysqlClose](/talend/en-US/components/8.0/mysql/tmysqlclose)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-closing-connection-to-mysql-database-standard-component -->
# Closing the connection to the MySQL database

Last updated: 9/30/2026

Configure the tMysqlClose
component to close the connection to the MySQL database.

## Procedure

1. Double-click the tMysqlClose component
   to open its Basic settings view.
2. From the Component List drop-down
   list, select the connection component that opens the connection you want to close.
   In this example, it is *tMysqlConnection\_1*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-creating-job-for-tracking-data-changes-in-mysql-using-scd-standard-component-create -->
# Creating a Job for tracking data changes in MySQL using SCD

Last updated: 9/30/2026

Create a Job to open a connection to a MySQL database, insert the
employee data into a MySQL database table using SCD (Slowly Changing Dimensions)

This Job retrieves
and displays the inserted data on the console, then updates the employee data in MySQL using
SCD, retrieves and displays the updated data on the console, finally closes the connection to
the MySQL database.

## Procedure

1. Create a new Job and add a tMysqlConnection component, two tFixedFlowInput components, two tMysqlSCD components, two tMysqlInput components, two tLogRow
   components, and a tMysqlClose component by typing
   their names in the design workspace or dropping them from the Palette.
2. Link the first tFixedFlowInput
   component to the first tMysqlSCD component using a
   Row > Main
   connection.
3. Do the same to link the first tMysqlInput component to the first tLogRow component, the second tFixedFlowInput component to the second tMysqlSCD component, and the second tMysqlInput component to the second tLogRow component.
4. Link the tMysqlConnection component to
   the first tFixedFlowInput component using a
   Trigger > OnSubjobOk connection.
5. Do the same to link the first tFixedFlowInput component to the first tMysqlInput component, the first tMysqlInput component to the second tFixedFlowInput component, the second tFixedFlowInput component to the second tMysqlInput component, and the second tMysqlInput component to the tMysqlClose component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-executing-job-to-track-data-changes-in-mysql-using-scd-standard-component-press -->
# Executing the Job to track data changes in MySQL using SCD

Last updated: 9/30/2026

After setting up the Job and configuring the components used in
the Job for tracking data changes in MySQL using SCD, you can then execute the Job and
verify the Job execution result.

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

   As shown above, the new *age* data *31* for *Mark Smith*
   the old *age* data *30*, a new record with the *SK* value set to *4* is created for
   the *role* change for *Teddy
   Brown* from *tester* to *writer*, and the values of the previous salary and the
   current salary for *Teddy Brown* are both kept in
   the newly created record.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-inserting-employee-data-into-mysql-table-using-scd-standard-component -->
# Inserting the employee data into a MySQL table using SCD

Last updated: 9/30/2026

Configure the first tFixedFlowInput component and the first tMysqlSCD component to insert the employee data into a MySQL database table
using SCD (Slowly Changing Dimensions).

## Procedure

1. Double-click the first tFixedFlowInput
   component to open its Basic settings view.
2. Click the
   button next to Edit schema and
   in the pop-up window define the schema by adding five columns: *id* and *age* of
   Integer type, *name* and *role* of String type, and *salary*
   of Double type.

   When done, click OK to save the changes. In the
   pop-up dialog box, click Yes to propagate the
   schema to the next component.
3. In the Mode area, select Use Inline Content (delimited file). Then in the
   Content field displayed, enter the following
   input employee data.

   ```
   1;Mark Smith;30;tester;11000.00
   2;Thomas Johnson;32;developer;12000.00
   3;Teddy Brown;33;tester;13000.00
   ```
4. Click the first tMysqlSCD component to
   open its Basic settings view.
5. Select the Use an existing connection
   check box and from the Component List drop-down
   list displayed, select the connection component you have configured.
6. In the Table field, enter the name of
   *employee\_scd*.
7. Click the
   button next to SCD Editor to
   open the SCD editor. All schema columns are listed on the Unused panel.
8. In the name field on the Surrogate keys panel, enter the name for the surrogate
   key, *SK* in this example.
9. From the Unused panel, drag and
   drop
   * `id` to the Source keys panel to use it as the key to
     ensure the unicity of the input data,
   * `name` to the Type
     0 fields panel and no special action will be performed upon
     dimension changes of it,
   * `age` to the Type 1
     fields panel to perform Type 1 SCD on it,
   * `role` to the Type
     2 fields panel to perform Type 2 SCD on it, and
   * `salary` to the Type 3 fields panel to perform Type 3 SCD on it.
10. In the Versioning panel, select the
    version check box to hold the version numbers
    for the historical and current records in the SCD table, and select also the
    active check box to add the column that will
    hold the True value for the current active record
    or the False value for the historical records in
    the SCD table.

    When done, click OK to save the changes and close
    the SCD editor.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-opening-connection-to-mysql-database-standard-component -->
# Opening a connection to a MySQL database

Last updated: 9/30/2026

Configure the tMysqlConnection component to open a connection to a MySQL
database.

## Procedure

1. Double-click the tMysqlConnection
   component to open its Basic settings view.
2. In the Host, Port, Database, Username, and Password
   fields, enter the information required for the connection to the MySQL
   database.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-inserted-employee-data-from-mysql-standard-component -->
# Retrieving the inserted employee data from MySQL

Last updated: 9/30/2026

Configure the first tMysqlInput component and the first tLogRow component to retrieve the inserted employee data from the MySQL SCD
table and display it on the console.

## Procedure

1. Double-click the tMysqlInput component
   to open its Basic settings view.
2. Select the Use an existing connection
   check box and from the Component List drop-down
   list displayed, select the connection component you have configured.
3. In the Table Name field, enter the
   name of the table from which the employee data will be retrieved. In this example,
   it is *employee\_scd*.
4. Open the schema editor of the tMysqlSCD component, select and copy all its schema columns, then
   open the schema editor of the tMysqlInput
   component, define its schema by pasting those schema columns you have copied from
   the tMysqlSCD component.

   When done, click OK to save the changes. In the
   pop-up dialog box, click Yes to propagate the
   schema to the next component.
5. Click the Guess Query button to fill
   the Query field with the automatically generated
   SQL query that will extract data of all columns from the specified table.
6. Double-click the first tLogRow
   component to open its Basic settings view. In the
   Mode area, select Table
   (print values in cells of a table) for better readability of the
   result displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-updated-employee-data-from-mysql-standard-component-repeat -->
# Retrieving the updated employee data from MySQL

Last updated: 9/30/2026

Configure the second tMysqlInput component and the second tLogRow component to retrieve the updated employee data from the MySQL SCD
table and display it on the console.

## Procedure

1. Repeat [1](tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-inserted-employee-data-from-mysql-standard-component) through
   [5](tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-inserted-employee-data-from-mysql-standard-component) in the procedure [Retrieving the inserted employee data from MySQL](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-inserted-employee-data-from-mysql-standard-component) to configure the second tMysqlInput component.
2. Repeat [6](tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-inserted-employee-data-from-mysql-standard-component) in the procedure
   [Retrieving the inserted employee data from MySQL](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-retrieving-inserted-employee-data-from-mysql-standard-component) to configure the second
   tLogRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-updating-employee-data-in-mysql-using-scd-standard-component -->
# Updating the employee data in MySQL using SCD

Last updated: 9/30/2026

Configure the second tFixedFlowInput component and the second tMysqlSCD component to update the employee data in MySQL using SCD (Slowly
Changing Dimensions).

## Procedure

1. Double-click the second tFixedFlowInput component to open its Basic
   settings view.
2. Click the
   button next to Edit schema and
   in the pop-up window define the schema by copying and pasting the schema of the
   first tFixedFlowInput component.
3. In the Mode area, select Use Inline Content (delimited file). Then in the
   Content field displayed, enter the following
   updated employee data.

   ```
   1;Mark Smith;31;tester;11000.00
   2;Thomas Johnson;32;developer;12000.00
   3;Teddy Brown;33;writer;13500.00
   ```
4. Repeat [4](tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-inserting-employee-data-into-mysql-table-using-scd-standard-component) through
   [10](tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-inserting-employee-data-into-mysql-table-using-scd-standard-component) in the procedure [Inserting the employee data into a MySQL table using SCD](/talend/en-US/components/8.0/scd/tmysqlscd-tfixedflowinput-tmysqlinput-tmysqlclose-inserting-employee-data-into-mysql-table-using-scd-standard-component) to configure the second tMysqlSCD component.
