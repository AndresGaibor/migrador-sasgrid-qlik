<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-synapse-analytics/tazuresynapserow · versión 8.0 -->
# tAzureSynapseRow

Last updated: 9/30/2026

Executes an SQL query stated on an Azure Synapse Analytics
database.

## tAzureSynapseRow Standard properties

These properties are used to configure tAzureSynapseRow running in the Standard Job framework.

The Standard
tAzureSynapseRow component belongs to two families: Cloud and Databases.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.   1. In the parent level, register the database connection to be shared    in the Basic settings view of the connection    component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   Information noteWarning: If this component is configured to perform operations to a table, it is strongly recommended that you use an existing connection with the auto-commit function enabled for this component. You can establish a connection of this type using the tAzureSynapseConnection component, with the Auto Commit option selected in the Advanced settings view. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| JDBC Provider | Select the provider of the JDBC driver to be used. |
| Host | Enter the IP address or the hostname of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in this field in the format of `{host_name}\{instance_name}`. In this case, you can leave the Port field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Port | Enter the listening port number of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in the Host field and leave this field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Schema | Enter the name of the Azure Synapse Analytics schema. |
| Database | Specify the name of the Azure Synapse Analytics to be used. |
| Username and Password | Enter the authentication data. To enter the password, click the [...] button next to the Password field, enter the password in double quotes in the pop-up dialog box, and then click OK.  You can use Type 2 integrated authentication on Windows by adding `integratedSecurity=true` in the Additional JDBC Parameters field and leave these two fields empty. See section Connecting with integrated authentication On Windows at [Building the connection URL](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?redirectedfrom=MSDN) for related information. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Table name | Specify the name of the table to be used. |
| Turn on identity insert | Select this checkbox to use your own sequence for the identity value of the inserted records (instead of having the SQL Server pick the next sequential value). |
| Query Type | Select the way the query will be set.  * Built-in: Fill in manually the query statement or   build it graphically using SQLBuilder. * Repository: Select the relevant query stored in   the Repository. The Query field gets accordingly   filled in. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Query | Specify your database query paying particularly attention to properly sequence the fields in order to match the schema definition. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  This checkbox is not available when the Use an existing Connection check box is selected. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair. For example, *encrypt=true;trustServerCertificate=false;* *hostNameInCertificate=\*.database.windows.net;loginTimeout=30;* for Azure SQL database connection. |
| Authenticate using Azure Active Directory | When selected, this option allows you to pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   Read the Usage section of this document for information about Microsoft SQL Server/JDBC encryption requirements. |
| Propagate QUERY's recordset | Select this checkbox to insert the result of the query into a column of the current flow. Select this column from the use column list.  This option allows the component to have a different schema from that of the preceding component. Moreover, the column that holds the QUERY's recordset should be set to the type of Object and this component is usually followed by tParseRecordSet. |
| Use PreparedStatement | Select this checkbox if you want to query the database using a PreparedStatement. In the Set PreparedStatement Parameters table, define the parameters represented by "?" in the SQL instruction of the Query field in the Basic Settings tab.   * Parameter Index: Enter the parameter position in the SQL instruction. * Parameter Type: Enter the parameter type. * Parameter Value: Enter the parameter value.   This option is very useful if you need to execute the same query several times. Performance levels are increased. |
| Commit every | Enter the number of rows to be completed before committing batches of rows together into the database. This option ensures transaction quality (but not rollback) and above all better performance on executions. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. Note that if the Propagate QUERY's recordset option is selected in the Advanced settings view, this variable returns the number of single ResultSet, which is 1. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rules | This component offers the flexibility of the DB query and covers all possible SQL queries.  Information noteImportant: Microsoft SQL Server/JDBC encryption requirements Starting with recent versions of the Microsoft SQL Server JDBC driver, TLS encryption is enabled by default (encrypt=true;trustServerCertificate=false). This enhances security, but if your SQL Server does not support encrypted connections or does not require clients to use TLS, you must set encrypt=false in the JDBC parameters of this component to connect successfully.   * For production or cloud environments using certificates signed by a   trusted authority (e.g., Azure, AWS), no changes are needed, the   default settings will work. * For servers using self-signed certificates, use   encrypt=true;trustServerCertificate=true or   specify the trust store details   (encrypt=true;trustStore=<your\_trust\_store>;trustStorePassword=<your\_trust\_store\_password>). * For non-secure development or test servers, set   encrypt=false in the additional JDBC parameters.   For more information on how to use connections with encryption properties, see [Microsoft SQL JDBC documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-ver17). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Note that some features that are supported by other databases are not supported by Azure Synapse Analytics. For more information, see [Unsupported table features](https://docs.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-tables-overview#unsupported-table-features).  Also note that when creating or deleting a table with this component, it is recommended to use the auto commit function by reusing the database connection created by a tAzureSynapseConnection component and selecting the Auto Commit checkbox on the Advanced settings view of the tAzureSynapseConnection component, instead of using a tAzureSynapseCommit component. |
