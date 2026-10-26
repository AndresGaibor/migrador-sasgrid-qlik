<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageoutputtable · versión 8.0 -->
# tAzureStorageOutputTable

Last updated: 9/30/2026

Performs the defined action on a given Azure storage table and inserts, replaces,
merges or deletes entities in the table based on the incoming data from the preceding
component.

## tAzureStorageOutputTable Standard properties

These properties are used to configure tAzureStorageOutputTable
running in the Standard Job framework.

The Standard
tAzureStorageOutputTable component belongs to the Cloud family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Connection Component | Select the component whose connection details will be used to set up the connection to Azure storage from the drop-down list. |
| Account Name | Enter the name of the storage account you need to access. A storage account name can be found in the Storage accounts dashboard of the Microsoft Azure Storage system to be used. Ensure that the administrator of the system has granted you the appropriate access permissions to this storage account. |
| Authentication type | Set the authentication type for connecting to Microsoft Azure Blob storage: Basic, Azure Active Directory, or Managed identities.   * Basic: Select   this option if you want to access Microsoft Azure Blob storage using   your storage account access key or a shared access signature. See [Configuring Azure Storage   connection strings](https://docs.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string) and [Using shared access signatures   (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) for related information. * Azure Active   Directory: Select this option to access Microsoft Azure   Blob storage using your Azure Active Directory (Azure AD) credentials.   See [Authorize access to blobs and   queues using Azure Active Directory](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad?toc=/azure/storage/blobs/toc.json) for related   information. * Managed identities: Select this option to use   system-assigned managed identities to access Azure Active   Directory-protected resources. For more information, see [What are managed identities for Azure   resources](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) and [Azure services that can use managed   identities to access other services](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/managed-identities-status).   Information noteNote: The Managed identities option is available only when you have installed the 8.0.1-R2023-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Region | Select one of the following Azure regions from the drop-down list.  * Azure Global * Azure China * Azure Germany * Azure Government * Azure Custom  You can use a customized Azure region by selecting the Azure Custom option and entering the endpoint suffix and the authority host URL in the Endpoint suffix field and the Authority host field. Note that the authority host URL is required when Azure Active Directory is selected from the Authentication type drop-down list. This drop-down list is not available if you select Managed identities from the Authentication type drop-down list.  Information noteNote: The Region drop-down list is available only when you have installed the 8.0.1-R2023-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Account Key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. Select the component whose connection details will be used to set up the connection to Azure storage from the drop-down list.  This option is available if you select Basic from the Authentication type drop-down list. |
| Protocol | Select the protocol for this connection to be created.  This option is available if you select Basic from the Authentication type drop-down list. |
| Use Azure Shared Access Signature | Select this check box to use a shared access signature (SAS) to access the storage resources without need for the account key. For more information, see [Using Shared Access Signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/storage-dotnet-shared-access-signature-part-1).  In the Azure Shared Access Signature field displayed, enter your account SAS URL between double quotation marks. You can get the SAS URL for each allowed service on Microsoft Azure portal after generating SAS. The SAS URL format is https://<$storagename>.<$service>.core.windows.net/<$sastoken>, where <$storagename> is the storage account name, <$service> is the allowed service name (`blob`, `file`, `queue` or `table`), and <$sastoken> is the SAS token value. For more information, see [Constructing the Account SAS URI](https://docs.microsoft.com/fr-fr/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri).  Note that the SAS has valid period, you can set the start time at which the SAS becomes valid and the expiry time after which the SAS is no longer valid when generating it, and you need to make sure your SAS is still valid when running your Job.  This option is available if you select Basic from the Authentication type drop-down list. |
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list.  Information noteNote: Azure Storage Table does not support Azure Active Directory authentication yet. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list.  Information noteNote: Azure Storage Table does not support Azure Active Directory authentication yet. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list.  Information noteNote: Azure Storage Table does not support Azure Active Directory authentication yet. |
| Table name | Specify the name of the table into which the entities will be written. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Partition Key | Select the schema column that holds the partition key value from the drop-down list. |
| Row Key | Select the schema column that holds the row key value from the drop-down list. |
| Action on data | Select an action to be performed on data of the table defined.   * Insert: insert a new entity into the table. * Insert or replace: replace an existing entity or insert a   new entity if it does not exist. When replace an entity, any properties from the   previous entity will be removed if the new entity does not define them. * Insert or merge: merge an existing entity or insert a new   entity if it does not exist. When merge an entity, any properties from the previous   entity will be retained if the new entity does not define or include them. * Merge: update an existing entity without removing the   property value of the previous entity if the new entity does not define its   value. * Replace: update an existing entity and remove the property   value of the previous entity if the new entity does not define its value. * Delete: delete an existing entity.   For performance reasons, the incoming data is processed in parallel and in random order. Therefore, it is not recommended to perform any order-sensitive data operation (for example, insert or replace) if there are duplicated rows in your data. |
| Action on table | Select an operation to be performed on the table defined.   * Default: No operation is carried out. * Drop and create table: The table is removed   and created again. * Create table: The table does not exist and   gets created. * Create table if does not exist: The table is   created if it does not exist. * Drop table if exist and create: The table is   removed if it already exists and created again. |
| Process in batch | Select this check box to process the input entities in batch.  Note that the entities to be processed in batch should belong to the same partition group, which means, they should have the same partition key value. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Name mappings | Complete this table to map the column name of the component schema with the property name of the Azure table entity if they are different.   * Schema column name:   enter the column name of the component schema between double quotation   marks. * Entity property name:   enter the property name of the Azure table entity between double quotation   marks.   For example, if there are three schema columns `CompanyID`, `EmployeeID`, and `EmployeeName` that are used to feed the values for the `PartitionKey`, `RowKey`, and `Name` entity properties respectively, then you need to add the following rows for the mapping when writing data into the Azure table.   * the Schema column name cell with the value   `"CompanyID"` and the Entity property   name cell with the value `"PartitionKey"`. * the Schema column name cell with the value   `"EmployeeID"` and the Entity property   name cell with the value `"RowKey"`. * the Schema column name cell with the value   `"EmployeeName"` and the Entity property   name cell with the value `"Name"`. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| NB\_SUCCESS | The number of rows successfully processed. This is an After variable and it returns an integer. |
| NB\_REJECT | The number of rows rejected. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as an end component of a Job or subJob and it always needs an input link. |

**Related concepts**  

* [Handling data with Microsoft Azure Table storage](tazurestorageconnection-tazurestorageinputtable-tlogrow-handling-data-with-microsoft-azure-table-storage-standard-component-bigdata-the "Here is an example of using Talend components to connect to a Microsoft Azure storage account that gives you access to Azure storage table service, write some employee data into an Azure storage table, and then retrieve the employee data from the table and display it on the console.")
