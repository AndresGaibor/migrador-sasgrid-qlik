<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/csql · versión 8.0 -->
# cSQL

Last updated: 9/30/2026

Reads from and writes to any database using a SQL connection based on a query.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

Information noteNote: This component is available
only if you have installed the R2022-11 Talend Studio
Monthly update or a later one delivered by Talend. For
more information, check with your administrator.

## cSQL Standard properties

These properties are used to configure cSQL running in the
Standard Route framework.

The Standard
cSQL component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Datasource | Select the component that opens the database connection to be reused by this component. |
| Output Type | Select the type of the output data.  * SelectOne: Make the output as single Java   object. * SelectList: Make the output as list of maps. * StreamList: Use an iterator to stream the   output. |
| Batch Mode | Select this checkbox to execute the statement in batch mode. |
| Use SQL statement from message body | Select this check box if your query statement is specified in the message body. |
| Type | Select the source type of the SQL query. This option is not available if Use SQL statement from message body is enabled.  * Built-In: The query statement will be entered   directly within the component. * Repository: The query statement will be selected   from an existing repository resource file. * File Path: The query statement will be selected from   the local file system. |
| Query | This option appears when Built-In is selected from the Type list. Specify a database query statement, paying particularly attention to the proper sequence of the fields which must correspond to the schema definition. If you have installed the R2025-12 Talend Studio Monthly update or a later one delivered by Talend, you can use multi-lines and format the SQL statement as you want. You can also click [...] next to the Query code box to open the SQL Builder and create a query in it. For more information, see [Creating queries using the SQLBuilder](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/creating-queries-using-sqlbuilder). |
| Resource | This option appears when Repository is selected from the Type list. Select the resource query statement file from the repository. Select the version of the query statement in the Version field if more than one version of the query statement is available. |
| Resource File | This option appears when File Path is selected from the Type list. Enter the path to the query statement file in your local file system. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Return generated keys from Inserts | Select this checkbox to retrieve the generated keys when inserting data into a table configured with an auto-incrementing key using cSQL. The generated keys are contained in the message header CamelSqlGeneratedKeyRows. For more information on the message headers supported by cSQL, see [Message Headers](https://camel.apache.org/components/4.14.x/sql-component.html#_message_headers). To specify which generated columns should be retrieved, click [+] as many times as required to add rows to the Expected keys table and enter the column names.  Information noteNote: This option is available only if you have installed the R2025-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| URI Options | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. In the Name field, you can either select the URI option from the drop-down list, or enter an option name that is not available in the list. Then click the corresponding Value field and enter a value. See the site <https://camel.apache.org/components/latest/sql-component.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSQL can be a start, middle or end component in a Route. It has to be used with the cSQLConnection component, which creates a connection to the database. For more information about cSQLConnection, see [cSQLConnection](/talend/en-US/components/8.0/mediation-database/csqlconnection). |
| Limitation | n/a |

**Related concepts**  

* [Writing and reading data in an H2 database with an SQL statement](csql-writing-and-reading-data-in-an-h2-database-with-an-sql-statement)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/csql-writing-and-reading-data-in-an-h2-database-with-an-sql-statement -->
# Writing and reading data in an H2 database with an SQL statement

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario shows how to:

* declare a reusable database connection,
* create a database table with an SQL statement,
* insert data in a table with an SQL statement extracted from Route message body,
* read data from a database,
* handle transaction for SQL connection and trigger rollback when error occurs in
  Route.

To execute this use case, you need an H2 database engine to be started.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-database/csql-dropping-and-linking-the-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-database/csql-configuring-the-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-database/csql-viewing-code-and-executing-route)

**Related reference**  

* [cSQL](csql "Reads from and writes to any database using a SQL connection based on a query.")
* [cSQLConnection](csqlconnection "Opens a connection to the specified database that can then be reused in the subsequent subRoute.")
* [cTransaction](ctransaction "Handles transaction for multiple cSQLConnection components within the same Camel context.")
* [cRollback](crollback "Triggers rollback when error occurs in Route.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/csql-configuring-the-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cSQLConnection
   component to display its Basic settings view in
   the Component tab.
2. Configure the properties as follows:
   1. In the Driver Class field, enter the class name for
      the H2 database, `"org.h2.Driver"`.
   2. Click the [+] button under the Driver
      JAR table to add a row.
   3. Select the cell and click the [...] button at the
      right side of the cell to open the Module dialog
      box.
   4. Click the Platform option and select the driver JAR
      h2-2.1.214.jar from the list.
   5. Click OK to close the Module
      dialog box.
   6. In the JDBC URL field, enter the JDBC URL of the
      database to be used, `"jdbc:h2:tcp://localhost/~/test"` in
      this example.
   7. Select the Authentication check box and enter the
      database user authentication data.
   8. Select the Use Transaction check box to enable
      transaction.
3. Double-click the cTimer
   component in the first subRoute, to display its Basic
   settings view in the Component
   tab.
4. Set the values for the Period
   (`500`), Repeat
   (`1`) and Delay
   (`100`) fields as shown above to trigger a message exchange
   after a delay of 100 milliseconds in the first subRoute.
5. Repeat this step to configure the other two cTimer
   components to trigger three message exchange after a delay of 500 milliseconds every
   500 milliseconds in the second subRoute and one message exchange after a delay of
   3000 milliseconds in the third subRoute.
6. Double-click the cTransaction component in the first
   subRoute to display its Basic settings view in the
   Component tab.
7. In the Datasource list, select
   cSQLConnection\_1 to use the database connection established
   in it. In Propagation Type list, select
   PROPAGATION\_REQUIRED to reuse an existing transaction or
   create a new one if none exists.
8. Double-click the cSQL component
   in the first subRoute to display its Basic
   settings view in the Component
   tab.
9. In the Datasource list, select
   cSQLConnection\_1 to use the database connection established
   in it. In Query box, enter the following code to
   create a TEST\_TABLE of four columns ID,
   Firstname, Lastname, and RegisterDate
   DATE in the database:

   ```
   "CREATE TABLE IF NOT EXISTS  TEST_TABLE (
     ID INTEGER auto_increment NOT NULL,
     Firstname VARCHAR(25),
     Lastname CHAR(25) NOT NULL,
     RegisterDate DATE DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (ID)
   )"
   ```
10. Double-click the cSetBody component to display its
    Basic settings view in the Component
    tab.
11. Select Constant in the Language list
    and enter `"INSERT INTO TEST_TABLE (Firstname, Lastname) VALUES ('Mike',
    'Jonson')"` in the Expression field.
12. Double-click the cSQL component in the second subRoute to
    display its Basic settings view in the
    Component tab.
13. Select cSQLConnection\_1 in the
    Datasource list and select the Use SQL statement
    from message body check box.
14. Double-click the cSQL component in the third subRoute to
    display its Basic settings view in the
    Component tab.
15. Select cSQLConnection\_1 in the
    Datasource list and enter `"select * from
    TEST_TABLE"` the Query box.
16. Double-click the cProcessor component in the third subRoute
    to display its Basic settings view in the
    Component tab.
17. In Code box, enter the following code to create an
    exception:

    ```
    String nullObject = null;
    int length = nullObject.length();
    ```
18. Double-click the cLog component in the first subRoute, to
    display its Basic settings view in the
    Component tab.
19. Configure the properties as follows:
    1. Select the Format the log output option.
    2. In the Arguments table, click
       [+] to add two rows and enter
       `"multiline"` and `"showheaders"`
       in the Name field. In the value
       field, enter `true` for both the two arguments.
    3. Keep the default settings of the other options.
20. Repeat this step to configure the cLog components in the
    second and third subRoutes in the same way.
21. Double-click the cOnException component in the fourth
    subRoute to display its Basic settings view in the
    Component tab.
22. Configure the properties as follows:
    1. In the Exceptions table, click
       [+] to add two rows and enter
       `java.lang.IllegalArgumentException` and
       `java.lang.Exception` in the
       Exception field.
    2. In the Exceptions behaviour area, select the
       Handle the exceptions option.
23. Double-click the cLog component in the fourth subRoute to
    display its Basic settings view in the
    Component tab.
24. Configure the properties as follows:
    1. Select the Specify output log message option.
    2. In the Message field, enter
       "${exception.message}".
    3. Keep the default settings of the other options.
25. Press Ctrl+S to save your
    Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/csql-dropping-and-linking-the-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cSQLConnection, a
   cTransaction, a cSetBody, a cProcessor, a
   cOnException, a cRollback, three
   cTimer, three cSQL, and four cLog components
   onto the design workspace.
2. Link the components with the Row
   > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/csql-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, three subRoutes are built from
   cTimer to cLog.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your route. You can also press F6 to execute it. 

   RESULT: The log messages in the subRoutes are printed in the
   console. In the first subRoute, a TEST\_TABLE is created in the
   database. In the second subRoute, three rows are written into the
   TEST\_TABLE. In the third subRoute, exception occurs and rollback
   is triggered.
