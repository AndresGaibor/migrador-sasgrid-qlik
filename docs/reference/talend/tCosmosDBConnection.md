<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cosmosdb/tcosmosdbconnection · versión 8.0 -->
# tCosmosDBConnection

Last updated: 9/30/2026

Creates a connection to a CosmosDB database and reuse that connection in other
components.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tCosmosDBConnection Standard properties

These properties are used to configure tCosmosDBConnection running in the Standard Job framework.

The Standard
tCosmosDBConnection component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| API | Select the database API to be used. Then the corresponding parameters to be defined are displayed in the Component view.  In the current version of this component, only the MongoDB API is supported. For this reason, MongoDB database is often mentioned in the documentation of the CosmosDB components. |
| Use replica set address or multiple query routers | Select this check box to show the Server addresses table.  In the Server addresses table, define the shared MongoDB databases or the MongoDB replica sets you want to connect to. |
| Server and Port | Enter the IP address and listening port of the database server.  Available when the Use replica set address or multiple query routers check box is not selected. |
| Database | Enter the name of the MongoDB database to be connected to. |
| Authentication mechanism | Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Use authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |
| Apply optional attributes | Select this option to set and apply optional attributes for the connection to be established.  In the Optional attributes table, click the plus button on the bottom to add a row, select the desired attribute from the drop-down list in the Name column, and set a value for the attribute in the Value column. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other CosmosDB components, particularly tCosmosDBClose. |
