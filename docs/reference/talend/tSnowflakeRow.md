<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakerow · versión 8.0 -->
# tSnowflakeRow

Last updated: 9/30/2026

Executes the SQL command stated onto a specified Snowflake database.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSnowflakeRow Standard properties

These properties are used to configure tSnowflakeRow running in the Standard Job framework.

The Standard
tSnowflakeRow component belongs to the Cloud family.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Component list | Select the component that opens the database connection to be reused by this component. |
| Account | In the Account field, enter, in double quotation marks, the account name that has been assigned to you by Snowflake. |
| Authentication Type | Set the authentication type.   * Basic: Select this option if key pair   authentication is not enabled. * Key Pair: Select this option if key pair   authentication is enabled.  See [Using Key Pair Authentication](https://docs.snowflake.net/manuals/user-guide/jdbc-configure.html#using-key-pair-authentication) for related   information. * OAuth 2.0: Select this option to use external   OAuth for data accessing.  See [External OAuth Overview](https://docs.snowflake.com/en/user-guide/oauth-ext-overview.html) for related   information.   Information noteNote: Before selecting the Key Pair option, make sure you have set the key pair authentication data in the Basic settings view of the tSetKeystore component as follows.  1. Leave the TrustStore type field unchanged. 2. Set TrustStore file to    `""`. 3. Clear the TrustStore password field. 4. Select Need Client authentication. 5. Enter the path to the key store file in double quotation marks in the    KeyStore file field (or click the    […] button to the right of the    KeyStore file field and navigate to the key    store file). 6. Enter the key store file password in the KeyStore    password field. 7. Clear the Check server identity option. |
| OAuth token endpoint | Enter OAuth 2.0 token endpoint. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Client ID | Enter the client ID of your application. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Client Secret | Enter the client secret of your application. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Grant type | Set the grant type for retrieving the access token. Two options are provided: Client Credentials and Password. Click [Client Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.4) and [Resource Owner Password Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.3) for related information.  This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| OAuth username | Enter the OAuth username. This option is available when Password is selected from the Grant type dropdown list. |
| OAuth password | Enter the OAuth password. To enter the password, click the [...] button next to the password field, enter the password between double quotes in the pop-up dialog box, and then click OK to save the settings.  This option is available when Password is selected from the Grant type dropdown list.  Information noteNote: OAuth password does not support spaces. |
| Scope | Enter the scope. See [Scopes](https://docs.snowflake.com/en/user-guide/oauth-ext-overview.html#scopes) for related information. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| User Id and Password | Enter, in double quotation marks, your authentication information to log in to Snowflake.   * In the User ID field, enter, in   double quotation marks, your login name that has been defined in Snowflake   using the *LOGIN\_NAME* parameter of   Snowflake. For details, ask the administrator of your Snowflake   system. * To enter the password, click the [...] button   next to the password field, enter the password in double quotes in the pop-up dialog box,   and click OK to save the settings. |
| Warehouse | Enter, in double quotation marks, the name of the Snowflake warehouse to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Schema | Enter, within double quotation marks, the name of the database schema to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Database | Enter, in double quotation marks, the name of the Snowflake database to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Table | Click the [...] button and in the displayed wizard, select the Snowflake table to be used. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  If the Snowflake data type to be handled is VARIANT, OBJECT, or ARRAY, while defining the schema in the component, select `String` for the corresponding data in the Type column of the schema editor wizard.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Guess Query | Click the button to generate the query which corresponds to the table and the schema in the Query field. |
| Query | Specify the SQL command to be executed.  For more information about Snowflake SQL commands, see [SQL Command Reference](https://docs.snowflake.net/manuals/sql-reference-commands.html). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is available only when you select Use this Component from the Connection Component dropdown list and select Internal from the Storage dropdown list in the Basic settings view. |
| Login Timeout | Specify the timeout period (in minutes) of Snowflake login attempts. An error will be generated if no response is received in this period. |
| Role | Enter, in double quotation marks, the default access control role to use to initiate the Snowflake session.  This role must already exist and has been granted to the user ID you are using to connect to Snowflake. If this field is left empty, the PUBLIC role is automatically granted. For information about Snowflake access control model, see [Understanding the Access Control Model](https://docs.snowflake.net/manuals/user-guide/security-access-control.html). |
| URL suffix | Enter, in double quotation marks, the Snowflake custom domain URL of your choice. For more information about Snowflake URL formats, see [Standard account URLs](https://docs.snowflake.com/en/user-guide/organizations-connect#standard-account-urls).  For Snowflake components other than tSnowflakeConnection, this field is available when you select Use This Component from the Connection Component drop-down list in the Basic settings view. |
| Use PreparedStatement | Select this check box if you want to query the database using a prepared statement. In the Set PreparedStatement Parameters table displayed, specify the value for each parameter represented by a question mark `?` in the SQL statement defined in the Query field.   * Parameter Index: the position of the parameter in the SQL   statement. * Parameter Type: the data type of the parameter. * Parameter Value: the value of the parameter.   For a related use case of this property, see [Using PreparedStatement objects to query data](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this). |
| Commit every | Specify the number of rows to be processed before committing batches of rows together into the database.  When used with the tSnowflakeConnection component, tSnowflakeRow ignores the Auto Commit option set in the advanced settings of tSnowflakeConnection and uses this value at runtime instead. |
| Use session timezone | Select this check box to use the time zone of the session instead of the JVM time zone. By default, this option is not selected. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Dynamic settings

| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the database query and covers all possible SQL queries. |

**Related concepts**  

* [Writing data into and reading data from a Snowflake table](tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-writing-data-into-and-reading-data-from-snowflake-table-standard-component "Here is an example of using Talend Snowflake components to connect to Snowflake, create a Snowflake table, write data into the table, then read data from this table, finally close the connection to Snowflake.")
