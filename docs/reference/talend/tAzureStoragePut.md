<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestorageput · versión 8.0 -->
# tAzureStoragePut

Last updated: 9/30/2026

Uploads local files into a given container for an Azure storage
account.

## tAzureStoragePut Standard properties

These properties are used to configure tAzureStoragePut running in the Standard
Job framework.

The Standard
tAzureStoragePut component belongs to the Cloud family.

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
| Container name | Enter the name of the container you need to write files in.  This container must exist in the Azure Storage system you are using. |
| Local folder | Enter the path, or browse to the folder from which you need to upload files. |
| Azure storage folder | Enter the path to the virtual blob folder in the remote Azure storage system you want to upload files into.  If you do not put any value in this field but leave this field as it is with only its default quotation marks, tAzureStoragePut writes files directly beneath the container level. |
| Use file list | Select this check box to be able to define file filtering conditions. Once selecting it, the Files table is displayed. |
| Files | Complete this table to select the files to be uploaded into Azure. The parameters to be provided are:  * Filemask: file   names or path to the files to be uploaded. * New name: name   to give to the files after they are uploaded.   Information noteNote: To prevent undesired files from being uploaded to the container, do not use these characters in the Filemask column: (, ), [, and ]. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Allow to escape the '+' sign in filemask | Select this option if you want to use + as a normal character in the filemask strings entered in the Files table in the Basic settings view.  If this option is not selected, + serves as a special RegEx character in the filemask strings. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| CONTAINER | The name of the blob container. This is an After variable and it returns a string. |
| LOCAL\_FOLDER | The local directory used in this component. This is an After variable and it returns a string. |
| REMOTE\_FOLDER | The remote directory used in this component. This is an After variable and it returns a string. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component of a Job or subJob. |
| Prerequisites | Knowledge about Microsoft Azure Storage is required. |

**Related concepts**  

* [Retrieving files from a Azure Storage container](tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-retrieving-files-from-azure-storage-container-standard-component-in-this)
