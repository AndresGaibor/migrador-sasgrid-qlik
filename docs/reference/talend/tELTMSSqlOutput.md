<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-mssql/teltmssqloutput · versión 8.0 -->
# tELTMSSqlOutput

Last updated: 9/30/2026

Executes the SQL Insert, Update and Delete statement to the MSSql
database

The three ELT MSSql components are closely related, in
terms of their operating conditions. These components should be used to handle MSSql DB
schemas to generate Insert statements, including clauses, which are to be executed in
the DB output table defined.

Carries out the action on the table specified and inserts the data
according to the output schema defined the ELT Mapper.

## tELTMSSqlOutput Standard properties

These properties are used to configure tELTMSSqlOutput running in the Standard Job framework.

The Standard
tELTMSSqlOutput component belongs to the ELT family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Action on data | On the data of the table defined, you can perform the following operation:  Insert: Adds new entries to the table. If duplicates are found, Job stops.  Update: Updates entries in the table.  Delete: Deletes the entries which correspond to the entry flow. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created and   stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists   and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Where clauses (for UPDATE and DELETE only) | Enter a clause to filter the data to be updated or deleted during the update or delete operations.  This field is available when Update or Delete is selected from the Action on data drop-down list and Use WHERE conditions table is not selected. |
| Use WHERE conditions table | Select this option to invoke the Where conditions table table, where you can set filter conditions by providing values in the Column, Function, and Value fields of the Where conditions table.  This option is available when Update or Delete is selected from the Action on data drop-down list. |
| Where conditions table | Add rows and enter conditions as prompted to filter the data to be updated or deleted during the update or delete operation. A data record is selected for the update or delete operation only when it matches all the conditions set in this table.  In addition to the commonly used operators (such as =, >=, <>, and so on), the Function column of this table also provides the following operators:  * BETWEEN,   which filters the data using an interval given in the Value field. The interval needs to   be in the format of <start> and   <end>, for example: 10   and 20. * LIKE, which   filters the data using a string given in the Value field. The string needs to be   in the format of sample\_string%. * IN, which   filters the data using the elements in a set given in the Value field. The set needs to be in   the format of (element1, element2, element3,   ...), for example: (1,2,5).  This option is available when the Use WHERE conditions table option is selected. |
| Default Table Name | Enter the default table name, between double quotation marks. |
| Default Schema Name | Enter the default schema name,between double quotation marks. |
| Table name from connection name is variable | Select this check box when the name of the connection to this component is set to a variable, such as a context variable. |
| Use different table name | Select this checkbox to define a different output table name, between double quotation marks, in the Table name field which appears. |
| Mapping | Specify the metadata mapping file for the database to be used. The metadata mapping file is used for the data type conversion between database and Java. For more information about the metadata mapping, see the related documentation for Type mapping. Information noteNote: You can use Hive mapping to support Databricks Delta Lake. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Authenticate using Azure Active Directory | When selected, this option allows you pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate. |
| Use update statement without subqueries | Select this option to generate an UPDATE statement for the MSSql database.  This option is available when Update is selected from the Action on data dropdown list in the Basic settings view. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  QUERY: the query statement populated by the ELT Map component the component connects to. This is an After variable and it returns a string. Information noteNote: This variable is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tELTMSSqlOutput is to be used along with the tELTMSSqlMap. Note that the Output link to be used with these components must correspond strictly to the syntax of the table name.  Information noteNote: Note that the ELT components do not handle actual data flow but only schema information. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
