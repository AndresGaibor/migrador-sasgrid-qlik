<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-jdbc/teltoutput · versión 8.0 -->
# tELTOutput

Last updated: 9/30/2026

Carries out the action on the table specified and inserts the data according to the
output schema defined in the ELT Mapper.

The three ELT components are closely related, in terms of
their operating conditions. These components should be used to handle DB schemas to
generate Insert statements, including clauses, which are to be executed in the DB output
table defined.

## tELTOutput Standard properties

These properties are used to configure tELTOutput running in the Standard Job framework.

The Standard
tELTOutput component belongs to the ELT
family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Action on table | Select an operation to be performed on the table defined.   * None: No operation is carried out. * Drop and create table: The table is removed   and created again. * Create table: The table does not exist and   gets created. * Create table if does not exist: The table is   created if it does not exist. * Drop table if exist and create: The table is   removed if it already exists and created again. * Clear table: The table content is   deleted. You have the possibility to rollback the operation. * Truncate table: The table content is   deleted. You do not have the possibility to rollback the operation. |
| Action on data | On the data of the table defined, you can perform the following operation:   * Insert: Adds new entries to the table. If duplicates are found, Job stops. * Update: Updates entries in the table. * Delete: Deletes the entries which correspond to the entry flow. |
| Schema and Edit schema | * A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either built-in or remotely stored in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Where clauses (for UPDATE and DELETE only) | Enter a clause to filter the data to be updated or deleted during the update or delete operations.  This field is available when Update or Delete is selected from the Action on data drop-down list and Use WHERE conditions table is not selected. |
| Use WHERE conditions table | Select this option to invoke the Where conditions table table, where you can set filter conditions by providing values in the Column, Function, and Value fields of the Where conditions table.  This option is available when Update or Delete is selected from the Action on data drop-down list. |
| Where conditions table | Add rows and enter conditions as prompted to filter the data to be updated or deleted during the update or delete operation. A data record is selected for the update or delete operation only when it matches all the conditions set in this table.  In addition to the commonly used operators (such as =, >=, <>, and so on), the Function column of this table also provides the following operators:  * BETWEEN,   which filters the data using an interval given in the Value field. The interval needs to   be in the format of <start> and   <end>, for example: 10   and 20. * LIKE, which   filters the data using a string given in the Value field. The string needs to be   in the format of sample\_string%. * IN, which   filters the data using the elements in a set given in the Value field. The set needs to be in   the format of (element1, element2, element3,   ...), for example: (1,2,5).  This option is available when the Use WHERE conditions table option is selected. |
| Default Table Name | Enter the default table name, between double quotation marks. |
| Default Schema Name | Enter the default schema name, between double quotation marks. |
| Table name from connection name is variable | Select this check box when the name of the connection to this component is set to a variable, such as a context variable. |
| Use different table name | Select this check box to define a different output table name, between double quotation marks, in the Table name field which appears. |
| Mapping | Specify the metadata mapping file for the database to be used. The metadata mapping file is used for the data type conversion between database and Java. For more information about the metadata mapping, see the related documentation for Type mapping. Information noteNote: You can use Hive mapping to support Databricks Delta Lake. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use update statement without subqueries | Select this option to generate an UPDATE statement for the database.  This option is available when Update is selected from the Action on data drop-down list in the Basic settings view. |
| Clause SET | Select the column names that will be used to generate the SET clauses.  SET clauses will not be generated for the columns that are not selected.  This field appears when Update is selected from the Action on data drop-down list in the Basic settings view. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  QUERY: the query statement populated by the ELT Map component the component connects to. This is an After variable and it returns a string. Information noteNote: This variable is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tELTOutput is to be used along with the tELTMap. Note that the Output link to be used with these components must correspond strictly to the syntax of the table name.  Note that the ELT components do not handle actual data flow but only schema information. |
| Limitation | Avoid using any keyword for the database as the table/column name or using any special character in the table/column name. If you want to, you can enclose the table/column name in a pair of `\"` to see whether it works. For example, when you want to use the keyword `number` as an Oracle database column name, you can have the Db Column value in the schema editor set to `\"number\"`. But note that this solution does not always work. |

**Related concepts**  

* [Aggregating Snowflake data using ELT components](teltinput-teltmap-tsnowflakeinput-tlogrow-aggregating-snowflake-data-using-context-variables-as-table-and-connection-names "This scenario shows you an example of aggregating Snowflake data from two source tables STUDENT and TEACHER to one target table FULLINFO using the ELT components.")
