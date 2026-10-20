<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleconnection · versión 8.0 -->
# tOracleConnection

Last updated: 9/30/2026

Information noteImportant: Support for Oracle 12-7 is removed from 8.0.1-R2024-12 onwards.
Use Oracle 18 instead.

Opens a connection to the specified Oracle database for reuse in the subsequent
subJob or subJobs.

## tOracleConnection Standard properties

Information noteImportant: Support for Oracle 12-7 is removed from 8.0.1-R2024-12 onwards.
Use Oracle 18 instead.

These properties are used to configure tOracleConnection running in the Standard Job framework.

The Standard
tOracleConnection component belongs to the Databases and the ELT families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in   or Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Connection Type | Drop-down list of available drivers:   * Oracle OCI: Select this   connection type to use Oracle Call Interface with a set of C-language   software APIs that provide an interface to the Oracle database. * Oracle Custom: Select this   connection type to access a clustered database. * Oracle Service Name: Select this   connection type to use the TNS alias that you give when you connect to   the remote database. * WALLET: Select this connection   type to store credentials in an Oracle wallet. * Oracle SID: Select this   connection type to uniquely identify a particular database on a   system.   Information noteNote: Connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Errors may occur if connections of the WALLET type are used by any other components. |
| DB Version | Select the Oracle version in use. |
| Use tns file | Select this check box to use the metadata of a context included in a tns file.  Information noteNote: One tns file may have many contexts.  TNS File: Enter the path to the tns file manually or browse to the file by clicking the [...] button next to the filed.  Select a DB Connection in Tns File: Click the [...] button to display all the contexts held in the tns file and select the desired one. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Schema | Name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use SSL | Select this checkbox to use the SSL protocol to protect the communication with your database server.  This property is available only when `ORACLE CUSTOM` is selected from the Connection Type dropdown list and `Oracle 12-7` or `Oracle 18 and above` is selected from the DB Version dropdown list. |
| TrustStore file | Enter the path to the TrustStore file used to authenticate your database server in SSL authentication.  This property is available only when the Use SSL checkbox is selected. |
| TrustStore password | Enter the password for the TrustStore file.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This property is available only when the Use SSL checkbox is selected. |
| Need Client authentication | Select this checkbox if SSL client authentication is needed.  This property is available only when the Use SSL checkbox is selected. |
| KeyStore file | Enter the path to the keystore file used for SSL client authentication.  This property is available only when the Need Client authentication checkbox is selected. |
| KeyStore password | Enter the password for the KeyStore file.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This property is available only when the Need Client authentication checkbox is selected. |
| Disable CBC protection | Select this checkbox to disable the use of CBC (Cipher Block Chaining) in SSL authentication.  This property is available only when the Use SSL checkbox is selected. |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating.  Information noteNote: You can set the encoding parameters through this field. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail.  This checkbox is not available when the Specify a data source alias checkbox is selected. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other Oracle components, especially with the tOracleCommit and tOracleRollback components. |

**Related concepts**  

* [Checking number format using a stored procedure](toracleconnection-toracleinput-toraclesp-tlogrow-checking-number-format-using-stored-procedure-standard-component-the)

**Related tasks**  

* [Using Oracle as a vector database](toracleconnection-toracleinput-toracleoutput-toracleclose-tfileinputdelimited-tmap-tlogrow-using-oracle-as-vector-db-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleconnection-toracleinput-toracleoutput-toracleclose-tfileinputdelimited-tmap-tlogrow-using-oracle-as-vector-db-standard-component -->
# Using Oracle as a vector database

Last updated: 9/30/2026

The following Job aims at connecting to an Oracle Database 23ai, creating a table for
similarity search, inserting some data about famous statements into it, and performing
similarity search by vector type.

## Before you begin

This scenario uses Oracle AI vector search capabilities. For more information, read
the corresponding [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/sql-quick-start-using-vector-embedding-model-uploaded-database.html).

## Linking the components

### Procedure

1. Drag and drop the following components from the Palette: tPrejob, tOracleConnection,
   tFileInputDelimited, 2 tLogRow,
   tMap,
   tOracleOutput, tOracleInput, tPostjob, and
   tOracleClose.
2. Link the tPrejob to the
   tOracleConnection and the
   tPostjob to the tOracleClose
   using an OnComponentOk connection as no data
   is handled here.
3. Connect the other components using a Row
   > Main connection.
4. Connect the main Job to the sub-Job using the trigger link
   OnSubjobOk.

## Configuring the components

### Procedure

1. Double-click the tOracleConnection
   component to display its Component view.
2. Configure the connection to your Oracle 23ai database.
3. Double-click the tFileInputDelimited component to display
   its Component view.
4. Set the path and properties of the sample file you want to insert in the Oracle
   database. 

   In this scenario, a TXT sample of famous quotes, with authors, years, and
   countries, is used.
5. Double-click the first tLogRow component to display its
   Component view.

   Click Sync columns to retrieve the schema structure from
   the previous component if needed.

   In the Mode area, select Table,
   and click Print content with log4j to display the Job
   result in the console.
6. Double-click the tMap
   component to open the Map Editor.
7. Drag the following columns from the input table to the
   out1 table: id,
   statement, author,
   year, and country. 

   Add a column `statement_clone`, to the end of the
   out1 table, and drag the
   statement column from the input table to this one. This
   new column will be used as the reference column in the Oracle vector table.
8. Click OK to validate the changes and close
   the editor.
9. Double-click the tOracleOutput component to display its
   Component view.
10. In the Basic settings view, enter the name of the Oracle
    table that will be used as a vector table (in this use case it is called
    `vectable`).

    Select Drop table if exists and create in the
    Action on table list, and select
    Insert in the Action on data
    list.

    For more information on vector tables, read the corresponding [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/create-tables-using-vector-data-type.html).
11. In the Advanced settings view, add a line in the
    Additional columns table to enter the SQL expression
    allowing you to insert the sample data into the selected vector column.

    Set the Data type to VECTOR,
    select statement\_clone as the Reference
    column, select Replace in the
    Position list, and enter the following SQL expression:

    ```
    "TO_VECTOR(VECTOR_EMBEDDING(ALL_MINILM_L12_V2 USING ? as data))"
    ```
12. Double-click the tOracleInput component to display its
    Component view.
13. In the Basic settings view, enter the following query in
    the Query field to fetch the sample data from the vector
    table previously created:

    ```
    "
    SELECT statement 
    FROM vectable 
    ORDER BY VECTOR_DISTANCE(vec, TO_VECTOR(VECTOR_EMBEDDING(ALL_MINILM_L12_V2 USING '" + context.query + "' as data)), EUCLIDEAN_SQUARED)
    FETCH FIRST 5 ROWS ONLY
    "
    ```
14. In the Advanced settings view, add a column named
    `result` in the Trim column table.
    This column will be displayed in the console when you execute the Job.
15. Double-click the second tLogRow component to display its
    Component view.

    Click Sync columns to retrieve the schema structure from
    the previous component if needed.

    In the Mode area, select Table,
    and click Print content with log4j to display the Job
    result in the console.

## Executing the Job

### Procedure

1. Press Ctrl + S to save your Job.
2. Press F6 to execute it.

### Results

The Run console displays the
result of the SQL query that fetches the sample data from the vector table. Only the
first 5 rows of the query result are displayed.

Once the vector table is created, you can do some similarity search on this table.
For example, with the query `"Matter of work"`, you will get the
following
result:

```
.-----------------------------------------------------.
|                      tLogRow_2                      |
|=---------------------------------------------------=|
|result                                               |
|=---------------------------------------------------=|
|The only way to do great work is to love what you do.|
|The only way to do great work is to love what you do.|
|Knowledge is power.                                  |
|To do nothing is the way to be nothing.              |
|With great power comes great responsibility.         |
'-----------------------------------------------------'
```

For more information on how to perform vector search with Oracle, read the
corresponding [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/query-data-similarity-and-hybrid-searches.html).

**Related concepts**  

* [tOracleInput](toracleinput "Reads an Oracle database and extracts fields based on a query.")
* [tOracleOutput](toracleoutput "Writes, updates, makes changes or suppresses entries in an Oracle database.")

**Related reference**  

* [tOracleConnection](toracleconnection "Opens a connection to the specified Oracle database for reuse in the subsequent subJob or subJobs.")
* [tOracleClose](toracleclose "Closes the transaction committed in the connected Oracle database.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleconnection-toracleinput-toraclesp-tlogrow-checking-number-format-using-stored-procedure-standard-component-the -->
# Checking number format using a stored procedure

Last updated: 9/30/2026

The following Job aims at connecting to an Oracle Database containing
Social Security Numbers and their holders' name, calling a stored procedure that checks
the SSN format of against a standard ###-##-#### format. Then the verification output
results, 1 for valid format and 0 for wrong format get displayed onto the execution
console.

* Drag and drop the following components from the Palette: tOracleConnection, tOracleInput, tOracleSP
  and tLogRow.
* Link the tOracleConnection
  to the tOracleInput using a Then Run connection as no data is handled here.
* And connect the other components using a Row Main link as rows are to be passed on as
  parameter to the SP component and to the console.
* In the tOracleConnection,
  define the details of connection to the relevant Database. You will then be able
  to reuse this information in all other DB-related components.
* Then select the tOracleInput and define its properties.

* Select the Use an existing
  connection check box and select the tOracleConnection component in the list in order to reuse the
  connection details that you already set.
* Select Repository as
  Property type as the Oracle schema is
  defined in the DB Oracle connection entry of the Repository. If you haven't
  recorded the Oracle DB details in the Repository, then fill in the Schema name manually.
* Then select Repository as
  Schema, and retrieve the relevant
  schema corresponding to your Oracle DB table.

* In this example, the SSN table has a four-column schema that
  includes *ID*, *NAME*, *CITY* and *SSNUMBER*.
* In the Query field, type
  in the following Select query or select it in the list, if you stored it in the
  Repository.

  select ID, NAME, CITY, SSNUMBER from SSN
* Then select the tOracleSP
  and define its Basic settings.

* Like for the tOracleInput
  component, select Repository in the
  Property type field and select the
  Use an existing connection check box,
  then select the relevant entries in the respective list.
* The schema used for the tOracleSP slightly differs from the input schema. Indeed, an
  extra column (*SSN\_Valid*) is added to the Input schema.
  This column will hold the format validity status (*1* or *0*) produced by the procedure.

* In the SP Name field,
  type in the exact name of the stored procedure (or function) as called in the
  Database. In this use case, the stored procedure name is *is\_ssn*.
* The basic function used in this particular example is as
  follows:

  ```
  CREATE OR REPLACE FUNCTION is_ssn(string_in VARCHAR2)
  RETURN PLS_INTEGER
  IS
  -- validating ###-##-#### format
  BEGIN
    IF TRANSLATE(string_in, '0123456789A', 'AAAAAAAAAAB') =
       'AAA-AA-AAAA' THEN
      RETURN 1;
    END IF;
    RETURN 0;
  END is_ssn;
  /
  ```
* As a return value is expected in this use case, the procedure
  acts as a function, so select the Is
  function check box.
* The only return value expected is based on the *ssn\_valid* column, hence select the relevant list
  entry.
* In the Parameters area,
  define the input and output parameters used in the procedure. In this use case,
  only the *SSNumber* column from the schema is used in the
  procedure.
* Click the plus sign to add a line to the table and select the
  relevant column (*SSNumber*) and type (*IN*).
* Then select the tLogRow
  component and click Sync Column to make sure the schema is passed on from the
  preceding tOracleSP component.

* Select the Print values in cells of a
  table check box to facilitate the output reading.
* Then save your Job and press F6 to run it.

On the console, you can read the output results. All input schema columns
are displayed even though they are not used as parameters in the stored procedure.

The final column shows the expected return value, whether the SS Number
checked is valid or not.

Information noteNote:

Check [Inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the) if you want to analyze a set of records from a database table or DB query and
return single records.

**Related concepts**  

* [tOracleInput](toracleinput "Reads an Oracle database and extracts fields based on a query.")

**Related reference**  

* [tOracleConnection](toracleconnection "Opens a connection to the specified Oracle database for reuse in the subsequent subJob or subJobs.")
* [tOracleSP](toraclesp "Calls an Oracle database stored procedure.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
