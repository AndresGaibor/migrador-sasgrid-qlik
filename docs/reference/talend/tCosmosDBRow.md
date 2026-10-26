<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cosmosdb/tcosmosdbrow · versión 8.0 -->
# tCosmosDBRow

Last updated: 9/30/2026

Executes the commands of the Cosmos database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tCosmosDBRow Standard properties

These properties are used to configure tCosmosDBRow running in the Standard Job framework.

The Standard
tCosmosDBRow component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| API | Select the database API to be used. Then the corresponding parameters to be defined are displayed in the Component view.  In the current version of this component, only the MongoDB API is supported. For this reason, MongoDB database is often mentioned in the documentation of the CosmosDB components. |
| Use replica set address or multiple query routers | Select this check box to show the Server addresses table.  In the Server addresses table, define the shared MongoDB databases or the MongoDB replica sets you want to connect to. |
| Server and Port | Enter the IP address and listening port of the database server.  Available when the Use replica set address or multiple query routers check box is not selected. |
| Database | Enter the name of the MongoDB database to be connected to. |
| Authentication mechanism | Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Use authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Execute command | Select this check box to enter MongoDB commands in the Command field for execution.  * Command: in this field,   enter the command to be executed, if this command contains   one single variable.  For example, if you need to construct the   command ```   {"isMaster": 1}   ``` You   need simply enter `isMaster` within quotation marks. * Construct command from keys and   values: if the command to be executed   contains multiple variables, select this check box and in   the Command keys and values   table, add the variables and their respective values to be   used.  For example, if you need to construct the following   command ```   { renameCollection : "<source_namespace>" , to : "<target_namespace>" , dropTarget : < true | false > }   ``` You   need to add three rows to the Command   keys and values table and enter one   variable-value pair to each row within quotation   marks: ```   "renameCollection"      "old_name"   "to"                    "new_name"   "dropTarget"            "false"   ``` * Construct command from a JSON   string: if you want to directly enter the   command to be used, select this check box and enter this   command in the JSON string   command field that is displayed. Only one   command is allowed per tCosmosDBRow.  For   example: ```   "{createIndexes: 'restaurants', indexes : [{key : {restaurant_id: 1}, name: 'id_index_2', unique: true}]}"   ```  Note that you must use single quotation marks to surround   the string values used in the command and double quotation   marks to surround the command itself.  For further information about the MongoDB commands you can   use in this field, see <https://docs.mongodb.org/manual/reference/command/>. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tCosmosDBRow allows you to manipulate the Cosmos database through the MongoDB commands. |
