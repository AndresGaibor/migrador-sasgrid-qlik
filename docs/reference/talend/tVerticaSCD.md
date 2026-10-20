<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tverticascd · versión 8.0 -->
# tVerticaSCD

Last updated: 9/30/2026

Tracks and reflects data changes in a dedicated Vertica SCD table.

## tVerticaSCD Standard properties

These properties are used to configure tVerticaSCD running in
the Standard Job framework.

The Standard
tVerticaSCD component belongs to the Business Intelligence and the Databases
families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| DB Version | Select the version of the database. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  When a Job contains the parent Job and the child Job, if you need to share an existing connection between the two levels, for example, to share the connection created by the parent Job with the child Job, you have to:   1. In the parent level, register the database connection to be shared    in the Basic settings view of the connection    component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the IP address or hostname of the database. |
| Port | Enter the listening port number of the database. |
| Database | Enter the name of the database. |
| Schema | Enter the schema of the database. |
| Username and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Enter the name of the table into which data will be written. |
| Action on table | Select an operation to be performed on the table defined.   * None: No operation is carried out. * Create table: The table does not exist and   gets created. * Create table if does not exist: The table is   created if it does not exist. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| SCD Editor | Click the [...] button and in the SCD component editor dialog box displayed, configure the data flow for slowly changing dimension outputs.  For more information, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology). |
| Use memory saving mode | Select this check box to maximize system performance. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. This property is not available when the Use an existing connection check box in the Basic settings view is selected. |
| End date time details | Specify the time value of the SCD end date time setting in the format of HH:mm:ss. The default value is `12:00:00`.  This property is available only when the SCD Type 2 method is used and `Fixed year value` is selected for creating the SCD Type 2 end date in the SCD editor. |
| Debug mode | Select this check box to display each step during processing entries in a database. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE\_INSERTED | The number of rows inserted. This is an After variable and it returns an integer. |
| NB\_LINE\_UPDATED | The number of rows updated. This is an After variable and it returns an integer. |
| NB\_LINE\_REJECTED | The number of rows rejected. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an end component of a Job or subJob and it always needs an input link.  Talend Studio and the Vertica database create very fast and affordable data warehouse and data mart applications. For more information about how to configure *Talend Studio* to connect to Vertica, see [Talend and HP Vertica Tips and Techniques](https://www.vertica.com/kb/Vertica-Integration-with-Talend-Connection-Guide/Content/Partner/Vertica-Integration-with-Talend-Connection-Guide.htm). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | This component does not support using SCD type 0 together with other SCD types. |
