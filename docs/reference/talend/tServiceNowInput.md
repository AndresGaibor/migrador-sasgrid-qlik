<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/servicenow/tservicenowinput · versión 8.0 -->
# tServiceNowInput

Last updated: 9/30/2026

Accesses ServiceNow and retrieves data from it.

tServiceNowInput retrieves data from ServiceNow
according to the specified conditions.

## tServiceNowInput Standard properties

These properties are used to configure tServiceNowInput running in the Standard
Job framework.

The Standard
tServiceNowInput component belongs to the Business and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use Existing Connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| URL | Enter the URL of the ServiceNow instance to be connected. |
| Username and Password | Enter the user authentication data to connect to the ServiceNow instance.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Select the name of the table from which the data will be retrieved or select Use Custom Table and in the Custom Table Name field displayed enter the table name. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Conditions | Specify search conditions to retrieve only the data that matches the criteria by clicking the [+] button to add as many conditions as needed and then setting the following parameters for each condition:   * Input column:   click in the cell and select the column of the input schema on which the   search condition is to be set. * Operator: click in   the cell and select an operator for the search condition. * Value: enter the   value for the corresponding column for the search condition. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Trim all columns | Select this check box to remove the leading and trailing whitespaces from all columns. |
| Limit | Enter the maximum number of records to be retrieved.  Information noteNote:  * This field takes effect only when it holds a positive integer. * There is no limit on the record number if you enter `""`,   `0`, or leave this field empty. In this case, all the   records will be retrieved. |
| Advanced Query | Select this check box to enter filtering conditions combined with AND and OR logical operators. You can enter query statements in this field through copy/paste operations. For information about the logical operators, see [Operators available for filters and queries](https://docs.servicenow.com/bundle/newyork-platform-user-interface/page/use/common-ui-elements/reference/r_OpAvailableFiltersQueries.html) and [Generate an encoded query string through a filter](https://docs.servicenow.com/bundle/newyork-platform-user-interface/page/use/using-lists/task/t_GenEncodQueryStringFilter.html).  The Conditions field in the Basic settings view is not available if you select this check box. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component in a  Talend  flow and it requires an output component. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
