<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-sharepoint/tsharepointget · versión 8.0 -->
# tSharePointGet

Last updated: 9/30/2026

Downloads one file from a SharePoint folder to the local system.

## tSharePointGet Standard properties

These properties are used to configure tSharePointGet running in the Standard Job framework.

The Standard
tSharePointGet component belongs to the Business and Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Site | Specify or select the SharePoint site. |
| Remote file | Enter the path of the file to download. |
| Local folder | Specify where to save the downloaded file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect the log data at the component level. |
| Overwrite the local file if exists | Select this checkbox to overwrite the local file if it already exists. |

## Static output schema

| Column | Description |
| --- | --- |
| Filename | The file or folder name. |
| Length | The file length. |
| Id | The technical identifier. |
| TimeCreated | The creation time. |
| TimeLastUpdated | The last-updated time. |
| Author | Information about the author. |
| isDirectory | Indicates whether the record represents a directory. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can reuse tSharePointConnection or run standalone. No Close component is needed. |
