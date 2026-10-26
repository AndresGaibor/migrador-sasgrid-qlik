<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatarow · versión 8.0 -->
# tTeradataRow

Last updated: 9/30/2026

Acts on the actual DB structure or on the data (although without handling data).

tTeradataRow is the specific
component for this database query. It executes the SQL query stated onto the specified
database. The row suffix means the component implements a flow in the Job design
although it doesn't provide output.

The SQL Builder tool helps you write easily your SQL statements.

## tTeradataRow Standard properties

These properties are used to configure tTeradataRow running in the Standard Job framework.

The Standard
tTeradataRow component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Query type | Either Built-In or Repository.   * Built-in: Fill in manually the query statement or   build it graphically using SQL Builder. * Repository: Select the relevant   query stored in the Repository. The Query field gets accordingly filled   in. |
| Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition. |
| Commit every | Number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and above all better performance on executions. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error using a Row > Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  This is intended to allow specific character set support. For example: CHARSET=KANJISJIS\_OS to get support of Japanese characters. |
| Propagate QUERY's recordset | Select this check box to insert the result of the query into a COLUMN of the current flow. Select this column from the use column list.  Information noteNote: This option allows the component to have a different schema from that of the preceding component. Moreover, the column that holds the QUERY's recordset should be set to the type of *Object* and this component is usually followed by tParseRecordSet. |
| Use PreparedStatement | Select this check box if you want to query the database using a PreparedStatement. In the Set PreparedStatement Parameter table, define the parameters represented by "?" in the SQL instruction of the Query field in the Basic Settings tab.  Parameter Index: Enter the parameter position in the SQL instruction.  Parameter Type: Enter the parameter type.  Parameter Value: Enter the parameter value.    Information noteNote: This option is very useful if you need to execute the same query several times. Performance levels are increased |
| Commit every | Number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and above all better performance on executions. |
| Query band | Select this check box to use the Teradata Query Banding feature to add metadata to the query to be processed, such as the user running the query. This can help you, for example, identify the origin of this query.  Once selecting the check box, the Query Band parameters table is displayed, in which you need to enter the metadata information to be added. This information takes the form of key/value pairs, for example, *DpID* in the Key column and *Finance* in the Value column.  This check box actually generates the SET QUERY\_BAND FOR SESSION statement with the key/value pairs declared in the Query Band parameters table. For further information about this statement, see the [Teradata documentation](https://docs.teradata.com/search/all?query=End+logging+syntax).  This check box is not available when you have selected the Using an existing connection check box. In this situation, if you need to use the Query Band feature, set it in the Advanced settings tab of the Teradata connection component to be used. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  Note that if the Propagate QUERY's recordset option is selected in the Advanced settings view, this variable returns the number of single ResultSet, which is 1.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query and covers all possible SQL queries. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Loading data into a Teradata database](tteradatatptexec-tteradatainput-tlogrow-loading-data-into-teradata-database-standard-component-this)
