<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolinput · versión 8.0 -->
# tExasolInput

Last updated: 9/30/2026

Retrieves data from an Exasol database based on a query with
a strictly defined order which corresponds to the schema definition, and passes the data
to the next component.

## tExasolInput Standard properties

These properties are used to configure tExasolInput running in the Standard
Job framework.

The Standard
tExasolInput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Either Built-In or Repository.   * Built-In: No property data   stored centrally. * Repository: Select the   repository file in which the properties are stored. The database   connection fields that follow are completed automatically using   the data retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and from the list displayed select the relevant connection component to reuse the connection details you have already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host name | Enter the host or host list of the Exasol database servers. Exasol can run in a cluster environment. The valid value can be a simple IP address (for example, *172.16.173.128*), an IP range list (for example, *172.16.173.128..130* that represents three servers *172.16.173.128*, *172.16.173.129*, and *172.16.173.130*), or a comma-separated host list (for example, *server1,server2,server3*) of the Exasol database cluster. |
| Port | Enter the listening port number of the Exasol database cluster. |
| Schema name | Enter the name of the schema you want to use. |
| Username and Password | Enter the user authentication data to access the Exasol database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Enter the name of the table to be queried. |
| Query Type and Query | Enter the database query, paying particularly attention to the proper sequence of the fields in order to match the schema definition. |
| Guess Query | Click the button to generate the query that corresponds to the table schema in the Query field. |
| Guess schema | Click the button to retrieve the schema from the table. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Change fetch size | Select this check box to change the fetch size which specifies the amount of resultset data sent during one single communication step with the database. In the Fetch size field displayed, you need to enter the size in KB. |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespaces from all the String/Char columns. |
| Trim column | Select the check box in the Trim column to remove leading and trailing whitespaces from the corresponding field.  This table is not available if the Trim all the String/Char columns check box is selected. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component of a Job or subJob and it needs an output link. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Importing data into an Exasol database table from a local CSV file](texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-importing-data-into-exasolution-database-table-from-local-csv-file-standard-component-this)
