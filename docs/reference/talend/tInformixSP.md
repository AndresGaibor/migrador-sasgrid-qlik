<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/informix/tinformixsp · versión 8.0 -->
# tInformixSP

Last updated: 9/30/2026

Centralises and calls multiple and complex queries in a database.

tInformixSP calls procedures stored in a database.

## tInformixSP Standard properties

These properties are used to configure tInformixSP running in the Standard Job framework.

The Standard
tInformixSP component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository   . * Built-in: No properties stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Schema | Name of the schema. |
| Username and Password | User authentication information.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Instance | Name of the Informix instance to be used. This information can generally be found in the *SQL hosts* file. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| SP Name | Enter the exact name of the stored procedure (SP). |
| Is Function / Return result in | Select this check box if only one value must be returned.  From the list, select the the schema column upon which the value to be obtained is based. |
| Parameters | Click the Plus button and select the various Schema Columns that will be required by the procedures. Note that the SP schema can hold more columns than there are parameters used in the procedure.  Select the Type of parameter:  IN: Input parameter.  OUT: Output parameter/return value.  IN OUT: Input parameter is to be returned as value, likely after modification through the procedure (function).  RECORDSET: Input parameter is to be returned as a set of values, rather than single value.  Information noteNote: Check [Inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the), if you want to analyze a set of records from a database table or DB query and return single records. |
| Use Transaction | Clear this check box if the database is configured in the NO\_LOG mode. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| tStatCatcher Statistics | Select this check box to collect log data at a component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This is an intermediary component. It can also be used as an entry component. In this case, only the entry parameters are authorized. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The stored procedure syntax must correspond to that of the database.  This component requires installation of its related jar files. |
