<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/databricks/tdbfsput · versión 8.0 -->
# tDBFSPut

Last updated: 9/30/2026

Connects to a given DBFS (Databricks Filesystem) system, copies files from an
user-defined directory, pastes them in this system and if needs be, renames these files.

The DBFS (Databricks Filesystem) components
are designed for quick and straightforward data transferring with Databricks. If you
need to handle more sophisticated scenarios for optimal performance, use Spark Jobs with
Databricks.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDBFSPut Standard properties

These properties are used to configure tDBFSPut running in the Standard Job framework.

The Standard
tDBFSPut component belongs to the Big Data and the File families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| *Use an existing connection* | Select this check box and in the Component List click the HDFS connection component from which you want to reuse the connection details already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Endpoint | In the Endpoint field, enter the URL address of your Azure Databricks workspace. This URL can be found in the Overview blade of your Databricks workspace page on your Azure portal. For example, this URL could look like https://adb-$workspaceId.$random.azuredatabricks.net. |
| Token | Click the [...] button next to the Token field to enter the authentication token generated for your Databricks user account. You can generate or find this token on the User settings page of your Databricks workspace. For further information, see [Personal access tokens](https://docs.databricks.com/sql/user/security/personal-access-tokens.html#generate-a-personal-access-token) from the official Azure documentation. |
| DBFS directory | In the DBFS directory field, enter the path pointing to the data to be used in the DBFS file system. |
| Local directory | Local directory where are stored the files to be loaded into DBFS. |
| Overwrite file | Options to overwrite or not the existing file with the new one. |
| Include subdirectories | Select this check box if the selected input source type includes sub-directories. |
| Files | In the Files area, the fields to be completed are:  - File mask: type in the file name to be selected from the local directory. Regular expression is available.  - New name: give a new name to the loaded file. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component combines DBFS connection and data extraction, thus usually used as a single-component subJob to copy data from a user-defined local directory to DBFS.  It runs standalone and does not generate input or output flow for the other components. It is often connected to the Job using OnSubjobOk or OnComponentOk link, depending on the context. |
