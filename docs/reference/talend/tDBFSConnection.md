<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/databricks/tdbfsconnection · versión 8.0 -->
# tDBFSConnection

Last updated: 9/30/2026

Connects to a given DBFS (Databricks Filesystem) system so that the other DBFS components can reuse the
connection it creates to communicate with this DBFS.

The DBFS (Databricks Filesystem) components
are designed for quick and straightforward data transferring with Databricks. If you
need to handle more sophisticated scenarios for optimal performance, use Spark Jobs with
Databricks.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDBFSConnection Standard properties

These properties are used to configure tDBFSConnection running in the Standard Job framework.

The Standard
tDBFSConnection component belongs to the Big Data and the File families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Endpoint | In the Endpoint field, enter the URL address of your Azure Databricks workspace. This URL can be found in the Overview blade of your Databricks workspace page on your Azure portal. For example, this URL could look like https://adb-$workspaceId.$random.azuredatabricks.net. |
| Token | Click the [...] button next to the Token field to enter the authentication token generated for your Databricks user account. You can generate or find this token on the User settings page of your Databricks workspace. For further information, see [Personal access tokens](https://docs.databricks.com/sql/user/security/personal-access-tokens.html#generate-a-personal-access-token) from the official Azure documentation. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other DBFS components. |
