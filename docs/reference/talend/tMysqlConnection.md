<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection · versión 8.0 -->
# tMysqlConnection

Last updated: 9/30/2026

Opens a connection to the specified MySQL database for reuse in the subsequent
subJob or subJobs.

## tMysqlConnection Standard properties

These properties are used to configure tMysqlConnection running in the Standard Job framework.

The Standard
tMysqlConnection component belongs to the Databases and the ELT families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The fields that follow are completed   automatically using the data retrieved. |
| DB version | Select the version of the database to be used.  When the database to be used is RDS Aurora, you need to select Mysql 5 (deprecated).  Information noteNote: MySQL 5 has been removed from Talend Studio 8.0 R2026-04. Use MySQL 8.0 or later. |
| Host | Enter the IP address of the database server. |
| Port | Enter the listening port number of the database server. |
| Database | Select or enter the name of the database to be used. |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail.  This checkbox is not available when the Specify a data source alias checkbox is selected. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tMysql\* components, especially with the tMysqlCommit and tMysqlRollback components. |

**Related concepts**  

* [Checking customer table against a given DQ rule to select customer records](tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-checking-customer-table-against-given-dq-rule-to-select-customer-records-standard-component-enterprise-this)
* [Getting the ID for the last inserted record with tMysqlLastInsertId](tmysqlconnection-tmysqllastinsertid-tlogrow-getting-id-for-last-inserted-record-with-tmysqllastinsertid-standard-component-the)
* [Inserting data in mother/daughter tables](tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the)
* [Iterating on a DB table and listing its column names](tmysqltablelist-tmysqlconnection-tlogrow-iterating-on-db-table-and-listing-its-column-names-standard-component-the)
* [Iterating on DB tables and deleting their content using a user-defined SQL template](tmysqlconnection-tmysqltablelist-tmysqltablelist-iterating-on-db-tables-and-deleting-their-content-using-user-defined-sql-template-standard-component-the)
* [Sharing a database connection between a parent Job and child Job](tmysqlconnection-tmysqlinput-tlogrow-sharing-database-connection-between-parent-job-and-child-job-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-sharing-database-connection-between-parent-job-and-child-job-standard-component-this -->
# Sharing a database connection between a parent Job and child Job

Last updated: 9/30/2026

This scenario shows how a database connection is shared between a parent Job and a
child Job. The parent Job first calls the child Job to write some randomly generated
data to a MySQL database, and then reads the data from the MySQL database and displays
it on the console. A connection to the MySQL database is set up only once and used in
both Jobs.

### In this section

* [Setting up the child Job](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-setting-up-child-job-standard-component)
* [Setting up the parent Job](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-setting-up-parent-job-standard-component)

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")
* [tMysqlInput](tmysqlinput "Executes a DB query with a strictly defined order which must correspond to the schema definition.")

**Related reference**  

* [tMysqlConnection](tmysqlconnection "Opens a connection to the specified MySQL database for reuse in the subsequent subJob or subJobs.")
* [tMysqlCommit](tmysqlcommit "Commits in one go, using a unique connection, a global transaction instead of doing that on every row or every batch and thus provides gain in performance.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tRunJob](/talend/en-US/components/8.0/orchestration/trunjob)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-checking-customer-table-against-given-dq-rule-to-select-customer-records-standard-component-enterprise-this -->
# Checking customer table against a given DQ rule to select customer records

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This example is a three-component Job that checks a MySQL customer table
against a given data quality rule so as to query specific customer records.

The components used in the Job are:

* tMysqlConnection: this component creates the
  connection to the MySQL database so that the other components can reuse it.
* tMySQLInvalidRows: this component reuses the
  connection created by tMysqlConnection and
  query the customer records against the given data quality rule.
* tLogRow: this component presents the result of
  running this Job.

  Information noteRemember: The connection components, including
  tMysqlConnection and tMySQLInvalidRows, have been regrouped into the
  tDBConnection component. They are automatically converted into
  this component when you place them on the workspace.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-dropping-and-linking-components-standard-component-enterprise-from?id=3545)
* [Configuring the connection to the database](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-configuring-connection-to-database-standard-component-enterprise-to?id=3546)
* [Configuring the query of the customer records](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-configuring-query-of-customer-records-of-interest-standard-component-enterprise?id=3547)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-executing-job-standard-component-enterprise-the?id=3548)

**Related reference**  

* [tMysqlConnection](tmysqlconnection "Opens a connection to the specified MySQL database for reuse in the subsequent subJob or subJobs.")
* [tMySQLInvalidRows](tmysqlinvalidrows "Checks MySQL database rows against specific Data Quality patterns (regular expression) or Data Quality rules (business rule).")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqllastinsertid-tlogrow-getting-id-for-last-inserted-record-with-tmysqllastinsertid-standard-component-the -->
# Getting the ID for the last inserted record with tMysqlLastInsertId

Last updated: 9/30/2026

The following Java scenario creates a Job that opens a connection to Mysql
database, writes the defined data into the database, and finally fetches the last
inserted ID on the existing connection.

* Drop the following components from the Palette onto the design workspace: tMysqlConnection, tMysqlCommit, tFileInputDelimited, tMysqlOutput, tMysqlLastInsertId, and tLogRow.
* Connect tMysqlConnection to
  tFileInputDelimited using an
  OnSubjobOk link.
* Connect tFileInputDelimited
  to tMysqlCommit using an
  OnSubjobOk link.
* Connect tFileInputdelimited
  to the three other components using Row
  Main links.

* In the design workspace, select tMysqlConnection.
* Click the Component tab
  to define the basic settings for tMysqlConnection.
* In the Basic settings view,
  set the connection details manually or select them from the
  context variable list, through a Ctrl+Space
  click in the corresponding field if you stored them locally as Metadata DB
  connection entries. For more information about metadata, see [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio)
  .

* In the design workspace, select tMysqlCommit and click the Component tab to define its basic settings.
* On the Component List,
  select the relevant tMysqlConnection if
  more than one connection is used.
* In the design workspace, select tFileInputDelimited.
* Click the Component tab
  to define the basic settings of tFileInputDelimited.

* Fill in a path to the processed file in the File Name field. The file used in this example is *Customers*.
* Define the Row separator that
  allow to identify the end of a row. Then define the Field
  separator used to delimit fields in a row.
* Set the header, the footer and the number of processed rows as
  necessary. In this scenario, we have one header.
* Click the [...] button next to Edit Schema to define the data to pass on to the next
  component.

In this scenario, the schema consists of two columns, *name* and *age*. The first holds three employees' names and
the second holds the corresponding age for each.

* In the design workspace, select tMysqlOutput.
* Click the Component tab
  to define the basic settings of tMysqlOuptput.

* Select the Use an existing
  connection check box.
* In the Table field, enter
  the name of the table where to write the employees' list, in this example: *employee*.
* Select relevant actions on the Action
  on table and Action on
  data lists. In this example, no action is carried out on table,
  and the action carried out on data is *Insert*.
* Click Sync columns to
  synchronize columns with the previous component. In this example, the schema to
  be inserted into the MySql database table consists of the two columns *name* and *age*.

* In the design workspace, select tMysqlLastInsertId.
* Click the Component tab
  to define the basic settings of tMysqlLastInserId.

* On the Component List,
  select the relevant tMysqlConnection, if
  more than one connection is used.
* Click Sync columns to
  synchronize columns with the previous component. In the output schema of
  tMysqlLastInsertId, you can see the
  read-only column *last\_insert\_id* that will fetch the last
  inserted ID on the existing connection.

You can select the data type *Long* from the
Type drop-down list in case of a huge number
of entries.

* In the design workspace, select tLogRow and click the Component tab to define its basic settings. For more
  information, see [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow).
* Save your Job and press F6 to execute it.

tMysqlLastInsertId fetched the last inserted ID
for each line on the existing connection.

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related reference**  

* [tMysqlConnection](tmysqlconnection "Opens a connection to the specified MySQL database for reuse in the subsequent subJob or subJobs.")
* [tMysqlLastInsertId](tmysqllastinsertid "Obtains the primary key value of the record that was last inserted in a Mysql table by a user.")
* [tMysqlCommit](tmysqlcommit "Commits in one go, using a unique connection, a global transaction instead of doing that on every row or every batch and thus provides gain in performance.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the -->
# Inserting data in mother/daughter tables

Last updated: 9/30/2026

The following Job is dedicated to advanced database users, who want to carry
out multiple table insertions using a parent table id to feed a child table.

As a prerequisite to this Job, follow the steps described below to create the
relevant tables using an engine such as *innodb*:

1. In a command line editor, connect to your Mysql server.
2. Once connected to the relevant database, type in the following command to
   create the parent table:

   ```
   create table f1090_mum(id int not null auto_increment, name varchar(10), primary key(id)) engine=innodb;
   ```
3. Then create the second table:

   ```
   create table f1090_baby (id_baby int not null, years int) engine=innodb;
   ```

Back in *Talend Studio*, the Job requires seven components including tMysqlConnection and tMysqlCommit.

### In this section

* [Linking the components](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-linking-components-standard-component-drag)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-configuring-components-standard-component-set)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-executing-job-standard-component-press)
* [Rollback from inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-rollback-from-inserting-data-in-mother-daughter-tables-standard-component-based-on)

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related reference**  

* [tMysqlConnection](tmysqlconnection "Opens a connection to the specified MySQL database for reuse in the subsequent subJob or subJobs.")
* [tMysqlCommit](tmysqlcommit "Commits in one go, using a unique connection, a global transaction instead of doing that on every row or every batch and thus provides gain in performance.")
* [tMysqlRollback](tmysqlrollback "Cancels the transaction commit in the connected MySQL database to avoid committing part of a transaction involuntarily.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tFileList](/talend/en-US/components/8.0/tfilelist/tfilelist)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqltablelist-tmysqltablelist-iterating-on-db-tables-and-deleting-their-content-using-user-defined-sql-template-standard-component-the -->
# Iterating on DB tables and deleting their content using a user-defined SQL template

Last updated: 9/30/2026

The following Java scenario creates a three-component Job that iterates on
given table names from a MySQL database using a WHERE clause. It then deletes the content
of the tables directly on the DBMS using a user-defined SQL template.

For advanced use, start with creating a connection to the database that
contains the tables you want to empty of their content.

* In the Repository tree view,
  expand Metadata and right click DB Connections to create a connection to the relevant
  database and to store the connection information locally.

  For more information about Metadata, see [Managing metadata in Talend Studio](/talend/r/Lfrx8uSM%7EUd8zWd9BsWB5g/dd4mXJkGs_3Ny4Aamc784g).

  Otherwise, drop a tMysqlConnection component in the design workspace and fill the
  connection details manually.
* Drop the database connection you created from the Repository onto the design workspace.

  The Components dialog box
  displays.
* Select tMysqlConnection and
  click OK.

  The tDBConnection\_1 components
  displays on the design workspace with all connection details automatically filled in
  its Basic settings view.
* Drop the following two components from the Palette onto the design workspace: tMysqlTableList (displayed as tDBTableList\_1)
  and tSQLTemplate.
* Connect tDBConnection\_1 to
  tDBTableList\_1 using an OnSubjobOk link.

* Connect tDBTableList\_1 to
  tSQLTemplate using an Iterate link.
* If needed, double-click tDBConnection\_1 to display its Basic
  settings view and verify the connection details.

In this example, we want to connect to a MySQL database called *examples*.

* In the design workspace, double-click tDBTableList\_1 to display its Basic
  settings view and define its settings.

* On the Component list, select
  the relevant MySQL connection component if more than one connection is used.
* Enter a WHERE clause using the right syntax in the corresponding
  field to iterate on the table name(s) you want to delete the content of.

  In this scenario, we want the Job to iterate on all the tables whose
  names start with ex.
* In the design workspace, double-click tSQLTemplate\_1 to display its Basic
  settings view and define its settings.

* In Database Name field, enter
  the name of the database containing the tables you want to process.
* From the Component list
  drop-down list, select the relevant MySQL connection component if more than one
  connection is used.
* Click in the Table name field
  and press Ctrl + Space to access the global
  variable list.
* From the global variable list, select *tDBTableList\_1\_CURRENT\_TABLE*.

To create the user-defined SQL template:

* In the Repository tree view,
  expand SQL Templates and MySQL in succession.

* Right-click UserDefined and
  select Create SQLTemplate from the drop-down
  list.

  The New SQLTemplate wizard
  opens.

* Enter a name for the new SQL template and fill in the other fields
  If needed and then click Finish to close the
  wizard.

  An SQL pattern editor opens on the design workspace.
* Delete the existing code and enter the code necessary to carry out
  the desired action, deleting the content of all tables which names start with "ex" in
  this example.

Information noteNote:

In the SQL template code, you must use the correct variable name
attached to the table name parameter (\_\_TABLE-NAME\_\_ in this example). To
display the variable name used, put your pointer in the Table
Name field in the basic settings of the tSQLTemplate\_1 component.

* Press Ctrl + S to save the
  new user-defined SQL template.

The next step is to add the new user-defined SQL template to the SQL
template list of the tSQLTemplate\_1 component.

To add the user-defined SQL template to the SQL template
list:

* In the Component view of
  tSQLTemplate\_1, click the SQL Templates tab to display the SQL Template List.

* Click the Add button and add
  two SQL template lines.
* Click in the first line to display a drop-down arrow and then click
  the arrow to display the SQL template list.

* Select in the list the user-defined SQL template you already
  created.
* Make sure that the SQL template in the second line is Commit.
* Save your Job and press F6 to
  execute it.

All tables in the MySQL examples database
whose names begin with ex are emptied from their content.

**Related reference**  

* [tMysqlConnection](tmysqlconnection "Opens a connection to the specified MySQL database for reuse in the subsequent subJob or subJobs.")
* [tMysqlTableList](tmysqltablelist "Lists the names of a given set of Mysql tables using a select statement based on a Where clause.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-setting-up-child-job-standard-component -->
# Setting up the child Job

Last updated: 9/30/2026

### In this section

* [Adding and linking components](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-adding-and-linking-components-standard-component-add)
* [Configuring the database connection](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-database-connection-standard-component)
* [Configuring the input data](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-input-data-standard-component)
* [Configuring the database output](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-database-output-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-setting-up-parent-job-standard-component -->
# Setting up the parent Job

Last updated: 9/30/2026

### In this section

* [Arranging data flow for the parent Job](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-arranging-data-flow-for-parent-job-standard-component-add)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-components-standard-component)
* [Execute the Job](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-execute-job-standard-component-press)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-configuring-connection-to-database-standard-component-enterprise-to -->
# Configuring the connection to the database

Last updated: 9/30/2026

## About this task

Information noteRemember: The connection components, including
tMysqlConnection and tMySQLInvalidRows, have been regrouped into the
tDBConnection component. They are automatically converted into
this component when you place them on the workspace.

## Procedure

1. Double-click tDBConnection
   to open its Component view.
2. In the DB version field,
   select the version of your MySQL database, Mysql
   8 in this example.
3. In the Host field, type in the server IP
   address of the database to which you want to connect, *localhost* in this example.
4. In the Port field, type in the port
   number of the database to which you want to connect, *3306* in this example.
5. In the Database field, enter the name of
   the database in which you need to check the customer table, *crm* in this example.
6. In the Username and the
   Password fields, enter the authentication
   information to connect to the database.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-configuring-query-of-customer-records-of-interest-standard-component-enterprise -->
# Configuring the query of the customer records

Last updated: 9/30/2026

## Procedure

1. Double-click tDBInvalidRows to open its
   Component view.
2. In the Validation type field, select
   DQ rule validation in order to use the
   given data quality rule.
3. Select Use an existing
   connection to reuse the connection that tDBConnection creates.
4. Click the [...] button next to Edit schema to open the schema editor.
5. Click the [+] button three
   times to add throw rows and rename them as `Name`,
   `DOB` and `Email`, respectively.
6. In the `DOB` row, select VARCHAR in the DB
   type column, enter `19` in the Length column and `0` in the
   Precision column.
7. Click OK to validate these
   changes and propagate the changes.
8. In the Table name field,
   browse to or enter the database table to be checked, *customers*
   in this example.
9. In the Where clause field,
   enter the clause to be used, in addition to the given data quality rule, to query the
   customer data. 

   In this example, enter `customers`.`Email` like
   's%' in quotation marks to retrieve the email records beginning with the
   letter *s* or *S*.
10. In the DQ rule list field,
    select the data quality rule to be used. In this example, select *customers\_age*. This rule is a demo rule reading 
    18<=((TO\_DAYS(NOW())-TO\_DAYS(DOB))/365).

    You can check the available data quality rules in the
    DQ Repository, Libraries > Rules > SQL.

    For further information, see [Importing a data quality demo project](/talend/r/en-US/8.0/studio-user-guide/importing-data-quality-demo-project).
11. Click Guess Query to generate the
    corresponding query clause that uses the Not clause.
12. In the Query field, change
    `18` to `20` to modify the clause as the
    following:

    ```
    "SELECT `Name`, `DOB`, `Email` FROM `crm`.`cust` 
    WHERE (NOT ( 20>((TO_DAYS(NOW())-TO_DAYS(DOB))/365) )
    AND `cust`.`Email` like 's%')"
    ```

    This clause lets you select the customers whose age is *20* or more.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-dropping-and-linking-components-standard-component-enterprise-from -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drop tMysqlConnection, tMySQLInvalidRows and tLogRow onto the design workspace.

   Information noteRemember: The connection components, including
   tMysqlConnection and tMySQLInvalidRows, have been regrouped into the
   tDBConnection component. They are automatically converted into
   this component when you place them on the workspace.
2. Right-click tDBConnection and
   select the Trigger > OnSubjobOk link to connect this component to tDBInvalidRows.
3. Right-click tDBInvalidRows
   and select the Row > Main link to connect to tLogRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-executing-job-standard-component-enterprise-the -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. To present the results in a table, double-click tLogRow and select Table (print values in
   cells of a table) in the Mode
   area.
2. To execute this Job, press F6.

## Results

Once done, the Run view is opened
automatically, where you can check the execution result.

You can read that the customer records beginning with the letter S are
retrieved and their ages are all more than 20.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-configuring-components-standard-component-set -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Set the tFileList component properties,
   such as the directory name where files will be fetched from.
2. In the tMysqlConnection
   Component view, set the connection details manually or fetch them from the Repository
   if you centrally stored them as a Metadata DB connection entry. For more information
   about Metadata, see [Managing metadata in Talend Studio](/talend/r/Lfrx8uSM%7EUd8zWd9BsWB5g/dd4mXJkGs_3Ny4Aamc784g).
3. On the tFileInputDelimited component's
   Basic settings panel, press Ctrl+Space bar to access the variable list. Set
   the File Name field to the global variable:
   *tFileList\_1.CURRENT\_FILEPATH*
4. Set the rest of the fields as usual, defining the row and field
   separators according to your file structure.
5. Then set the schema manually through the Edit
   schema feature or select the schema from the Repository. In
   Java version, make sure the data type is correctly set, in accordance with
   the nature of the data processed.
6. In the tMap Output area, add two output
   tables, one called mum for the parent table, the second called baby, for the
   child table.

   Drag the *Name* column from the Input area, and drop it to the mum table.

   Drag the *Years* column from the Input area and drop it to the baby table.
7. Make sure the mum table is on the top of the baby table as the order is
   determining for the flow sequence hence the DB insert to perform
   correctly.

   Connect the output row link to distribute correctly the flow to the
   relevant DB output component.
8. In the Basic settings
   tab of the two tMysqlOutput components,
   select the Use an existing connection
   check box to retrieve the tMysqlConnection details.
9. Set the Table name,
   making sure it corresponds to the correct table, in this example either *f1090\_mum* or *f1090\_baby*.

   There is no action on the table as they are already
   created.

   Select Insert as
   Action on data for both output
   components.

   Click on Sync columns to retrieve the schema set in the
   tMap.
10. Switch to the Advanced
    settings tab of the DB output component corresponding to the
    child table (that is, *f1090\_baby*). 

    * In the *id-baby* row of the Additional
      columns table, fill the SQL
      expression field with `"(Select
      Last_Insert_id())"`.
    * Set the Position field to
      `Before`.
    * Set the Reference column field to
      `years`.

    These settings allow the *f1090\_baby* table to use the ID key of the
    *f1090\_mum* as its key.
11. Clear the Extend insert
    check box of both database output components.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save your Job.
2. Press F6 to execute it.

   The parent table *id* has been reused to feed the
   *id\_baby* column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-linking-components-standard-component-drag -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drag and drop the following components from the Palette: a tFileList, a
   tFileInputDelimited, a tMap, a tMysqlConnection, a tMysqlCommit and two tMysqlOutput.
2. Connect tMysqlConnection to tFileList using an OnComponentOk link.
3. Connect tFileList to tMysqlCommit using an OnComponentOk link.
4. Connect the tFileList component to the
   input file component using an Iterate link
   as the name of the file to be processed will be dynamically filled in from
   the tFileList directory using a global
   variable.
5. Connect the tFileInputDelimited component
   to the tMap and dispatch the flow between
   the two output Mysql DB components. Use a Row link for each for these connections representing the
   main data flow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-rollback-from-inserting-data-in-mother-daughter-tables-standard-component-based-on -->
# Rollback from inserting data in mother/daughter tables

Last updated: 9/30/2026

## About this task

Based on [Inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the), insert a rollback function in order to prevent
unwanted commit.

## Procedure

1. Drag and drop tMysqlRollback to the design
   workspace. tMysqlRollback ensures that the transaction will not
   be partly committed.
2. Connect tFileList to tMysqlRollback with an OnSubjobError trigger.
3. Double-click tMysqlRollback to enter its
   Basic settings view.
4. From the Component List, select the
   connection component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-adding-and-linking-components-standard-component-add -->
# Adding and linking components

Last updated: 9/30/2026

## Procedure

1. Add the following components by typing the component names on the design
   workspace or dropping them from the Palette: 
   * a tMysqlConnection
     component (displayed as tDBConnection\_1), to open a
     connection to the MySQL database,
   * a tRowGenerator, to generate
     random input data,
   * a tMysqlOutput component
     (displayed as tDBOutput\_1), to write data to the MySQL
     database.
2. Connect the tRowGenerator
   component to tDBOutput\_1 component using a
   Row > Main connection.
3. Connect the tDBConnection\_1
   component to the tRowGenerator using a
   Trigger > OnSubjobOk connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-database-connection-standard-component -->
# Configuring the database connection

Last updated: 9/30/2026

## Procedure

1. Double-click the tDBConnection\_1 component to open its Basic settings view.
2. With the Property Type set to Built-In, specify the connection details in the
   relevant fields, including: 
   * the host name or IP address of your database server
   * the listening port number
   * the database name
   * the user name and password for your database
     authentication.

   If you have stored your connection details under the Metadata node in the Repository tree view, you can simply drop your centralized
   metadata item onto the tMysqlConnection
   component. For information on how to centralize a database connection, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata).
3. Select the Use or register a shared DB
   Connection check box so that the database connection open by
   this component can be shared across different Jobs. Then, enter a name for
   the shared connection between double quotes in the Shared DB Connection Name field, *shared\_mysql\_connection* in this example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-database-output-standard-component -->
# Configuring the database output

Last updated: 9/30/2026

## Procedure

1. Double-click the tDBOutput\_1
   component to open its Basic settings
   view.
2. Select the Use an existing connection
   check box and, in case you have more than one connection component in the
   Job, select the connection component to be used from the Component List drop-down list.
3. In the Table field, enter the name of the
   database table you are going to write data to, *customers* in this example.
4. From the Action on table list, select the
   Drop table if exists and create option
   to ensure a clean table is created.
5. From the Action on data list, select
   Insert.
6. Click the [...] button next to Edit schema to check the output schema. If
   needed, click Sync columns to retrieve the
   schema from the preceding component.
7. Press Ctrl+S to save the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-input-data-standard-component -->
# Configuring the input data

Last updated: 9/30/2026

## Procedure

1. Double-click the tRowGenerator component
   to open the Row Generator editor.
2. Click the [+] button to add four columns
   and set their properties:
   * *id*, type Integer, 2 characters
     long.
   * *firstName*, type String, 15
     characters long
   * *lastName*, type String, 15
     characters long
   * *city*, type String, 15
     characters long
3. Define the function for each column:
   * For the *id* column, select
     Numeric.sequence from the
     Function list to generate
     sequence numbers.
   * For the *firstName* column,
     select TalendDataGenerator.getFirstName from the Function list to generate random first
     names.
   * For the *lastName* column, select
     TalendDataGenerator.getLastName
     from the Function list to generate
     random family names.
   * For the *city* column, select
     TalendDataGenerator.getUsCity
     from the Function list to generate
     random city names.
4. In the Number of Rows for RowGenerator
   field, specify the number of data rows you want to generate, *10* in this example.
5. Click the Preview button on the Preview tab to validate the generator
   settings.
6. When done, click OK to close the editor
   and click Yes when prompted to propagate
   the schema to the next component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-arranging-data-flow-for-parent-job-standard-component-add -->
# Arranging data flow for the parent Job

Last updated: 9/30/2026

## Procedure

1. Add the following components by typing the component names on the design
   workspace or dropping them from the Palette: 
   * a tRunJob component, to call the
     child Job,
   * a tMysqlConnection
     component (displayed as tDBConnection\_1), to open the
     MySQL database connection,
   * a tMysqlInput component
     (displayed as tDBInput\_1), to read the data written to
     the MySQL database by the child Job.
   * a tLogRow component to display
     the data on the console,
   * a tMysqlCommit component
     (displayed as tDBCommit\_1) to commit data upon
     transaction and close the database connection.
2. Connect the tRunJob
   component to the tMysqlConnection component
   using a Trigger > OnSubjobOk connection.
3. Connect the tMysqlConnection component to
   the tMysqlInput component using a Trigger > OnSubjobOk connection.
4. Connect the tMysqlInput component to the
   tLogRow component using a Row > Main
   connection.
5. Connect the tMysqlInput component to the
   tMysqlCommit component using a
   Trigger > OnSubjobOk connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tRunJob component to
   open its Basic settings view.

   If a child Job has been already specified in the component, you
   can open its Basic settings view by
   right-clicking it and selecting Settings from
   the contextual menu, or by clicking the component and then selecting the Component tab.
2. Click the [...] button next to the
   Job field and select the child Job from
   the Repository Content dialog box. Leave
   all the other parameters as default.
3. In the Basic settings view of the
   tMysqlConnection component, select the
   Use or register a shared DB Connection
   check box. Then, in the Shared DB Connection
   Name field, enter the name of the shared connection defined
   in the child Job, *shared\_mysql\_connection*
   in this example.

   Leave all the other parameters blank or as default.
4. Double-click the tMysqlInput component to
   open its Basic settings view.
5. Select the Use an existing connection
   check box and, in case you have more than one connection component in the
   Job, select the connection component to be used from the Component List drop-down list.
6. Click the [...] button next to Edit schema to open the Schema editor, and define the same data structure as in
   the child Job. 

   When done, click OK to close the dialog
   and click Yes when prompted to propagate
   the schema to the next component.
7. Specify the table name in the Table
   Name list, and click Guess
   Query to get the query statement automatically filled in the
   Query field.
8. In the Basic settings view of the
   tLogRow component, select the Table mode to display the execution result in
   table cells.

   Leave the settings of the tMysqlCommit
   component unchanged.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinput-tlogrow-execute-job-standard-component-press -->
# Execute the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 or click the Run button on the Run console to execute the Job.

   The Job first calls the child Job to write data to the database and then
   reads the data from the database and displays it on the console.
