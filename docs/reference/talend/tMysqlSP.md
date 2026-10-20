<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlsp · versión 8.0 -->
# tMysqlSP

Last updated: 9/30/2026

Calls a MySQL database stored procedure.

tMysqlSP offers a convenient way to centralize multiple
or complex queries in a database and call them easily.

## tMysqlSP Standard properties

These properties are used to configure tMysqlSP running in the Standard Job framework.

The Standard
tMysqlSP component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| SP Name | Type in the exact name of the Stored Procedure |
| Is Function / Return result in | Select this check box, if a value only is to be returned.  Select on the list the schema column, the value to be returned is based on. |
| Parameters | Click the Plus button and select the various Schema Columns that will be required by the procedures. Note that the SP schema can hold more columns than there are paramaters used in the procedure.  Select the Type of parameter:  IN: Input parameter.  OUT: Output parameter/return value.  IN OUT: Input parameter is to be returned as value, likely after modification through the procedure (function).  RECORDSET: Input parameter is to be returned as a set of values, rather than single value.  Information noteNote: Check [Inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the) if you want to analyze a set of records from a database table or DB query and return single records. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. Information noteTip: You can press Ctrl+Space to access a list of predefined global variables. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as intermediary component. It can be used as start component but only input parameters are thus allowed. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The Stored Procedures syntax should match the Database syntax. |

**Related concepts**  

* [Using tMysqlSP to find a State Label using a stored procedure](tmysqlsp-trowgenerator-tlogrow-tlogrow-using-tmysqlsp-to-find-state-label-using-stored-procedure-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlsp-trowgenerator-tlogrow-tlogrow-using-tmysqlsp-to-find-state-label-using-stored-procedure-standard-component-the -->
# Using tMysqlSP to find a State Label using a stored procedure

Last updated: 9/30/2026

The following Job aims at finding the State labels matching the odd State
IDs in a Mysql two-column table. A stored procedure is used to carry out this operation.

* Drag and drop the following components used in this example:
  tRowGenerator, tMysqlSP, tLogRow.
* Connect the components using the Row
  Main link.
* The tRowGenerator is used
  to generate the odd id number. Double-click on the component to launch the
  editor.

* Click on the Plus button to
  add a column to the schema to generate.
* Select the Key check box
  and define the Type to Int.
* The Length equals to 2
  digits max.
* Use the preset function called sequence but customize the Parameters in the lower part of the
  window.

* Change the Value of
  step from *1* to
  *2* for this example, still starting from 1.
* Set the Number of generated
  rows to 25 in order for all the odd State id (of 50 states) to
  be generated.
* Click OK to validate the
  configuration.
* Then select the tMysqlSP
  component and define its properties.

* Set the Property type
  field to Repository and
  select the relevant entry on the list. The connection details get filled in
  automatically.
* Else, set manually the connection information.
* Click Sync Column to
  retrieve the generated schema from the preceding component.
* Then click Edit Schema
  and add an extra column to hold the State Label to be output, in addition to the
  ID.
* Type in the name of the procedure in the SP Name field as it is called in the Database.
  In this example, *getstate*. The procedure to be executed
  states as follows:

  ```
  DROP PROCEDURE
  IF EXISTS `talend`.`getstate` $$
  CREATE DEFINER=`root`@`localhost` PROCEDURE `getstate`(IN pid INT, OUT
  pstate VARCHAR(50))
  BEGIN
  SELECT LabelState INTO pstate FROM us_states WHERE idState = pid;
  END $$
  ```
* In the Parameters area,
  click the plus button to add a line to the table.
* Set the Column field to
  *ID*, and the Type field to *IN* as it will be given as
  input parameter to the procedure.
* Add a second line and set the Column field to *State* and the Type to *Out* as this is
  the output parameter to be returned.
* Eventually, set the tLogRow component properties.

* Synchronize the schema with the preceding component.
* And select the Print values in cells
  of a table check box for reading convenience.
* Then save your Job and execute it.

The output shows the state labels corresponding to the odd state ids as
defined in the procedure.

Information noteNote:

Check [Inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the) if you want to analyze a set of records from a database table or DB query and
return single records.

**Related reference**  

* [tMysqlSP](tmysqlsp "Calls a MySQL database stored procedure.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
