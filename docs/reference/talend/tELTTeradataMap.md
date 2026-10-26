<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-teradata/teltteradatamap · versión 8.0 -->
# tELTTeradataMap

Last updated: 9/30/2026

Builds the SQL SELECT statement using the table schema(s) provided by one or more
tELTTeradataInput components.

The three ELT Teradata components are closely related,
in terms of their operating conditions. These components should be used to handle
Teradata database table schemas to generate SQL statements, including clauses, which are
to be executed in the database output table defined.

## tELTTeradataMap Standard properties

These properties are used to configure tELTTeradataMap running in the Standard Job framework.

The Standard
tELTTeradataMap component belongs to the ELT family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| ELT Teradata Map editor | The ELT Map editor allows you to define the output schema as well as build graphically the SQL statement to be executed. The column names of schema can be different from the column names in the database.  These operators are used: =, <=, <, >=, >, and <>; the corresponding previous operators, including EQ, LE, LT, GE, GT, and NE, are deprecated.  On the upper left corner of the ELT Map editor, you can click the Setup the configurations of elt map button to open a dialog box Property Settings which contains two options:   * Add quotes in columns when generating query: With   this check box selected, double quotes will be added for all output column   names to support delimited identifiers. By default, this check box is   cleared. This check box is displayed as Delimited   identifiers if you have not installed the 8.0 R2022-11   Talend Studio monthly update or a later one provided by Talend. * Use alias in output   table: With this check box selected, aliases will be   used for all output columns in the SQL query. By default, this check   box is cleared.   You can filter schema columns in an input or output table by clicking the Enable/disable column name filter button in the corresponding table and entering the search keyword in the field displayed. |
| Style link | Select the way in which links are displayed.  Auto: By default, the links between the input and output schemas and the Web service parameters are in the form of curves.  Bezier curve: Links between the schema and the Web service parameters are in the form of curve.  Line: Links between the schema and the Web service parameters are in the form of straight lines.  This option slightly optimizes performance. |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored centrally. * Repository: Select the Repository file where Properties are stored. The following fields are pre-filled in using fetched data. |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Query band | Select this check box to use the Teradata Query Banding feature to add metadata to the query to be processed, such as the user running the query. This can help you, for example, identify the origin of this query.  Once selecting the check box, the Query Band parameters table is displayed, in which you need to enter the metadata information to be added. This information takes the form of key/value pairs, for example, *DpID* in the Key column and *Finance* in the Value column.  This check box actually generates the SET QUERY\_BAND FOR SESSION statement with the key/value pairs declared in the Query Band parameters table. For further information about this statement, see the [Teradata documentation](https://docs.teradata.com/search/all?query=End+logging+syntax).  This check box is not available when you have selected the Using an existing connection check box. In this situation, if you need to use the Query Band feature, set it in the Advanced settings tab of the Teradata connection component to be used. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tELTTeradataMap is used along with a tELTTeradataInput and tELTTeradataOutput. Note that the Output link to be used with these components must faithfully reflect the name of the tables.  Information noteNote: The ELT components do not handle actual data flow but only schema information. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Mapping data using a subquery](teltteradatainput-teltteradatamap-teltteradataoutput-mapping-data-using-subquery-standard-component "The sample Job described in this scenario maps the data from two input tables, PreferredSubject and CourseScore, to the output table, TotalScoreOfPreferredSubject, using a subquery.")
