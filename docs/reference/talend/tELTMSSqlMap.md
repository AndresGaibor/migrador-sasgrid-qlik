<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-mssql/teltmssqlmap · versión 8.0 -->
# tELTMSSqlMap

Last updated: 9/30/2026

Uses the tables provided as input to feed the parameter in the built statement. The
statement can include inner or outer joins to be implemented between tables or between one
table and its aliases.

The three ELT MSSql components are closely related, in
terms of their operating conditions. These components should be used to handle MSSql DB
schemas to generate Insert statements, including clauses, which are to be executed in
the DB output table defined.

Helps you to build the SQL statement graphically, using the table provided as
input.

## tELTMSSqlMap Standard properties

These properties are used to configure tELTMSSqlMap running in the Standard Job framework.

The Standard
tELTMSSqlMap component belongs to the ELT family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| JDBC Provider | Select the provider of the JDBC driver to be used, either Microsoft (the default, recommended) or Open source JTDS.  When Microsoft is selected, you need to download the Microsoft JDBC Driver for SQL Server on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774), unpack the downloaded zip file, choose a jar in the unzipped folder based on your JRE version, rename the jar to *mssql-jdbc.jar* and install it manually. For more information about choosing the jar, see the System Requirements information on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774).  When using this component with Datasource in Talend Runtime, you need to use the Open source JTDS driver. |
| ELT MSSql Map Editor | The ELT Map editor allows you to define the output schema and make a graphical build of the SQL statement to be executed. The column names of schema can be different from the column names in the database.  You can filter schema columns in an input or output table by clicking the Enable/disable column name filter button in the corresponding table and entering the search keyword in the field displayed.  You can click  on the upper left corner and in the Property Settings dialog box displayed, select the Add quotes in columns when generating query check box to add quotes for the column names in the generated SQL query. This check box is displayed as Delimited identifiers if you have not installed the 8.0 R2022-11 Talend Studio monthly update or a later one provided by Talend. |
| Style link | Select the way in which links are displayed.  Auto: By default, the links between the input and output schemas and the Web service parameters are in the form of curves.  Bezier curve: Links between the schema and the Web service parameters are in the form of curve.  Line: Links between the schema and the Web service parameters are in the form of straight lines.  This option slightly optimizes performance. |
| Property type | Either Built-in or Repository.  * Built-in: No property data stored   centrally. * Repository: Select the Repository   file where Properties are stored. The following fields are pre-filled in   using fetched data. |
| Host | Enter the database server IP address. |
| Port | Enter the listening port number of DB server. |
| Database | Enter the name of the database. |
| Username and Password | Enter the DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Dry run | Select this option to populate the QUERY variable of the ELTOutput component connected to the component while not connecting to the database or executing queries.  Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection checkbox in the Basic settings. |
| Authenticate using Azure Active Directory | When selected, this option allows you pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   This option is only available when Microsoft is selected from the JDBC Provider dropdown list in the Basic settings view. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tELTMSSqlMap is used along with a tELTMSSqlInput and tELTMSSqlOutput. Note that the Output link to be used with these components must correspond strictly to the syntax of the table name. Information noteNote: The ELT components do not handle actual data flow but only schema information. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
