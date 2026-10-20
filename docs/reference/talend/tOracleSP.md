<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toraclesp · versión 8.0 -->
# tOracleSP

Last updated: 9/30/2026

Calls an Oracle database stored procedure.

tOracleSP offers a convenient way to
centralize multiple or complex queries in a database and call them easily.

## tOracleSP Standard properties

These properties are used to configure tOracleSP running in the Standard Job framework.

The Standard
tOracleSP component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Make sure that the connection selected is not of the WALLET type to prevent possible errors.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers:  Oracle OCI: Select this connection type to use Oracle Call Interface with a set of C-language software APIs that provide an interface to the Oracle database.  Oracle Service Name: Select this connection type to use the TNS alias that you give when you connect to the remote database.  Oracle SID: Select this connection type to uniquely identify a particular database on a system.  Oracle Custom: Select this connection type to access a clustered database. |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Schema | Name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| SP Name | Type in the exact name of the Stored Procedure (or Function) |
| Is Function / Return result in | Select this check box, if the stored procedure is a function and one value only is to be returned.  Select on the list the schema column, the value to be returned is based on. |
| Parameters | * Click the Plus button and select the various Schema Columns that will be required by the   procedures. Note that the SP schema can hold more columns than there   are parameters used in the procedure. * Select the Type of   parameter:  IN: Input parameter.  OUT: Output parameter/return   value.  IN OUT: Input parameter is to be   returned as value, likely after modification through the procedure   (function).  RECORDSET: Input parameter is to   be returned as a set of values, rather than single value.  Information noteNote: Check [Inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the) if you want to analyze a set   of records from a database table or DB query and return single   records. * The Custom Type is used when a   Schema Column you want to use   is user-defined. Two Custom Type   columns are available in the Parameters table. In the first Custom Type column:  - Select the check box in the Custom Type   column when the corresponding Schema Column you want to use is of user-defined   type.  - If all listed Schema Columns   in the Parameters table are of   custom type, you can select the check box before Custom Type once for them all. * Select a database type from the DB   Type list to map the source database type to the   target database type:  - Auto-Mapping: Map the source   database type to the target database type   automatically.(default)  - CLOB: Character large   object.  - BLOB: Binary large object.  - DECIMAL: Decimal numeric   object.  - NUMERIC: Character 0 to 9.  - XMLTYPE: XML schema   type.  Information noteWarning: When mapping a column selected from the Return result in list box or set to the IN or   OUT type of parameter to XMLTYPE, make sure that the column is   of type String in the schema. * In the second Custom Type column,   you can precise what the custom type is. The type may be:  - STRUCT: used for one element.  - ARRAY: used for a collection   of elements. * In the Custom name column,   specify the name of the custom type that you have given to this   type.  Information noteWarning: *When an OUT parameter uses the custom type, make sure   that its corresponding Schema Column has chosen the Object   type in the schema table.* |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| NLS Language | In the list, select the language used for the data that are not used in Unicode. |
| NLS Territory | Select the conventions used for date and time formats. The default value is that of the operating system. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as intermediary component. It can be used as start component but only input parameters are thus allowed. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The Stored Procedures syntax should match the Database syntax.  When the parameters set in this component are of Custom Type, the tJava family components should be placed before the component in order for users to define values for the custom-type parameters, or after the component so as to read and output the Out-type custom parameters. |

**Related concepts**  

* [Checking number format using a stored procedure](toracleconnection-toracleinput-toraclesp-tlogrow-checking-number-format-using-stored-procedure-standard-component-the)
