<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-queue/tazurestoragequeuecreate · versión 8.0 -->
# tAzureStorageQueueCreate

Last updated: 9/30/2026

Creates a new queue under a given Azure storage account.

## tAzureStorageQueueCreate Standard properties

These properties are used to configure tAzureStorageQueueCreate
running in the Standard Job framework.

The Standard
tAzureStorageQueueCreate component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

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
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Queue name | Specify the name of the Azure queue to be created. For more information about the queue naming rules, see [Naming Queues and Metadata](https://docs.microsoft.com/fr-fr/rest/api/storageservices/fileservices/naming-queues-and-metadata). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| QUEUE\_NAME | The name of the Azure queue. This is an After variable and it returns a string. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component of a Job or subJob. |
