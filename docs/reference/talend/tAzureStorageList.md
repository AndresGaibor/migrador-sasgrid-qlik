<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist · versión 8.0 -->
# tAzureStorageList

Last updated: 9/30/2026

Lists blobs in a given container according to the specified blob
filters.

## tAzureStorageList Standard properties

These properties are used to configure tAzureStorageList running in the Standard
Job framework.

The Standard
tAzureStorageList component belongs to the Cloud family.

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
| Account Key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. Select the component whose connection details will be used to set up the connection to Azure storage from the drop-down list.  This option is available if you select Basic from the Authentication type drop-down list. |
| Protocol | Select the protocol for this connection to be created.  This option is available if you select Basic from the Authentication type drop-down list. |
| Use Azure Shared Access Signature | Select this check box to use a shared access signature (SAS) to access the storage resources without need for the account key. For more information, see [Using Shared Access Signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/storage-dotnet-shared-access-signature-part-1).  In the Azure Shared Access Signature field displayed, enter your account SAS URL between double quotation marks. You can get the SAS URL for each allowed service on Microsoft Azure portal after generating SAS. The SAS URL format is https://<$storagename>.<$service>.core.windows.net/<$sastoken>, where <$storagename> is the storage account name, <$service> is the allowed service name (`blob`, `file`, `queue` or `table`), and <$sastoken> is the SAS token value. For more information, see [Constructing the Account SAS URI](https://docs.microsoft.com/fr-fr/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri).  Note that the SAS has valid period, you can set the start time at which the SAS becomes valid and the expiry time after which the SAS is no longer valid when generating it, and you need to make sure your SAS is still valid when running your Job.  This option is available if you select Basic from the Authentication type drop-down list. |
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Container name | Enter the name of the container from which you need to select blobs to be listed. |
| Blob filter | Complete this table to select the blobs to be listed. The parameters to be provided are:  * Prefix: enter   the common prefix of the names of the blobs you need to list. This   prefix allows you to filter the blobs which have the specified prefix   in their names in the given container.  A blob name contains the virtual hierarchy of the blob   itself. This hierarchy is a virtual path to that blob and is relative to the   container where that blob is stored. For example, in a container named *photos*, the name of a photo blob might be *2014/US/Oakland/Talend.jpg*.  For this reason, when you define a prefix, you are actually   designating a directory level as the blob filter, for example, *2014/* or *2014/US/*.  If you want to select the blobs stored directly beneath the   container level, that is to say, the blobs without virtual path in their names,   remove quotation marks and enter null. * Include   sub-directories: select this check box to select all of   the sub-folders and the blobs in those folders beneath the designated   directory level. If you leave this check box clear, tAzureStorageList   returns only the blobs, if any, directly beneath that directory   level. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   The schema of this component is predefined with a single column `BlobName` of String type, which indicates the name of each blob to be listed.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| CONTAINER | The name of the blob container. This is an After variable and it returns a string. |
| CURRENT\_BLOB | The blob name being processed by this component. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component of a Job or subJob. |
| Prerequisites | Knowledge about Microsoft Azure Storage is required. |

**Related concepts**  

* [Retrieving files from a Azure Storage container](tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-retrieving-files-from-azure-storage-container-standard-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-retrieving-files-from-azure-storage-container-standard-component-in-this -->
# Retrieving files from a Azure Storage container

Last updated: 9/30/2026

In this scenario, a five-component Job uses Azure Storage components to write
files in a given Azure Storage system and then retrieve selected files (blobs in terms of
Azure Storage) from that system.

Before replicating this scenario, you must have appropriate rights and
permissions to read and write files in the Azure storage account to be used. For further
information, see Microsoft's documentation for Azure Storage: <http://azure.microsoft.com/en-us/documentation/services/storage/>.

The *talendcontainer* container used in this scenario
was created using tAzureStorageContainerCreate in the
scenario [Creating a container in Azure Storage](/talend/en-US/components/8.0/azure-storage-blob/tazurestorageconnection-tazurestoragecontainerexist-tazurestoragecontainercreate-tjava-creating-container-in-azure-storage-standard-component-in-this).

### In this section

* [Linking the components](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-linking-components-standard-component-in)
* [Connecting to an Azure storage account](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-connecting-to-azure-storage-account-standard-component)
* [Writing files in Azure Storage](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-writing-files-in-azure-storage-standard-component)
* [Verifying the file transfer](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-verifying-file-transfer-standard-component)
* [Retrieving selected files](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-retrieving-selected-files-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-executing-job-standard-component-press-f6)

**Related reference**  

* [tAzureStorageConnection](tazurestorageconnection "Uses authentication and the protocol information to create a connection to the Microsoft Azure Storage system that can then be reused by other Azure Storage components.")
* [tAzureStorageContainerCreate](tazurestoragecontainercreate "Creates a new storage container used to hold Azure blobs (Binary Large Object) for a given Azure storage account.")
* [tAzureStorageList](tazurestoragelist "Lists blobs in a given container according to the specified blob filters.")
* [tAzureStoragePut](tazurestorageput "Uploads local files into a given container for an Azure storage account.")
* [tAzureStorageGet](tazurestorageget "Retrieves blobs from a given container for an Azure storage account according to the specified filters applied on the virtual hierarchy of the blobs and then write selected blobs in a local folder.")

**Related information**  

* [tJava](/talend/en-US/components/8.0/java-custom-code/tjava)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-connecting-to-azure-storage-account-standard-component -->
# Connecting to an Azure storage account

Last updated: 9/30/2026

## Procedure

1. Double-click tAzureStorageConnection to open its Component view.
2. In the Account name
   field, enter the name of the storage account to be connected to. In this
   example, it is
   `talendstorage`,
   an account that has been created for demonstration purposes.
3. In the Account key field, paste the
   primary or the secondary key associated with the storage account to be used.
   These keys can be found in the Manage Access Key dashboard in the Azure
   Storage system to be connected to.
4. From the Protocol list,
   select the protocol for the endpoint of the storage account to be used. In this
   example, it is
   `HTTPS`.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-executing-job-standard-component-press-f6 -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press F6 to run this
   Job.
2. Check the execution result on the Run console.

   You can read that the Job returns the list of the blobs with
   the `photos` prefix in the container.
3. Double-check the resut in the web console of the Azure storage account.
4. Check the retrieved files in the specified local folder. 

   You can see the blobs with the `photos/mongodb/` prefix
   have been retrieved and their prefix transformed to directories.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-linking-components-standard-component-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective of Talend Studio,
   create an empty Job, named `azureTalend` for example, from the
   Job Designs node in the Repository tree view.
2. Drop tAzureStoragePut, tAzureStorageList, tJava and tAzureStorageGet
   onto the workspace.
3. Connect the Azure Storage components using the Trigger > OnSubjobOk link while connect tAzureStorageList to tJava using the Row > Iterate link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-retrieving-selected-files-standard-component -->
# Retrieving selected files

Last updated: 9/30/2026

## Procedure

1. Double-click tAzureStorageGet to open its Component view.
2. Select
   the component whose connection details will be used to set up the Azure storage
   connection. In this example, it is
   `tAzureStorageConnection_1`.
3. In the Container name
   field, enter the name of the container from which you need to retrieve files. In
   this scenario, it is
   `talendcontainer`.
4. In the Local folder
   field, enter the path, or browse, to the directory where you want to put the
   retrieved files. In this example, it is
   `E:/screenshots`.
5. Under the Blob table, click the [+] button to add one row in the table.
6. In the Prefix column,
   enter the common name prefix of the files (blobs) to be retrieved. In this
   example, it is
   `photos/mongodb/`.
7. In the Include
   sub-directories column, select the check box in the newly added
   row. This allows tAzureStorageGet to
   retrieve all the files (blobs) beneath the
   `photos/mongodb/`
   level.
8. In the Create parent
   directories column, select the check box in the newly added row
   to create the same directory in the specified local folder as the retrieved
   blobs have in the container.

   Note that having this same directory is necessary for successfully retrieving
   blobs. If you leave this check box clear, then you need to create the same
   directory yourself in the target local folder.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-verifying-file-transfer-standard-component -->
# Verifying the file transfer

Last updated: 9/30/2026

### In this section

* [Configuring tAzureStorageList](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-configuring-tazurestoragelist-standard-component)
* [Configuring tJava](/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-configuring-tjava-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-writing-files-in-azure-storage-standard-component -->
# Writing files in Azure Storage

Last updated: 9/30/2026

## Procedure

1. Double-click tAzureStoragePut to open its Component view.
2. Select
   the component whose connection details will be used to set up the Azure storage
   connection. In this example, it is
   `tAzureStorageConnection_1`.
3. In the Container name
   field, enter the name of the container you need to write files in. In this
   example, it is
   `talendcontainer`,
   a container created in the scenario [Creating a container in Azure Storage](/talend/en-US/components/8.0/azure-storage-blob/tazurestorageconnection-tazurestoragecontainerexist-tazurestoragecontainercreate-tjava-creating-container-in-azure-storage-standard-component-in-this).
4. In the Local folder
   field, enter the path, or browse, to the directory where the files to be used
   are stored. In this scenario, they are some pictures showing technical process
   and stored locally in
   `E:/photos`.
   Therefore, put
   `E:/photos`;
   this allows tAzureStoragePut to upload
   all the files of this folder and its sub-folders into the
   `talendcontainer`
   container.

   For demonstration purposes, the example photos are organized as follows in
   the `E:/photos` folder.

   * Directly beneath the
     `E:/photos`
     level:

     |  |
     | --- |
     | *components-use\_case\_triakinput\_1.png*  *components-use\_case\_triakinput\_2.png*  *components-use\_case\_triakinput\_3.png*  *components-use\_case\_triakinput\_4.png* |
   * In the
     `E:/photos/mongodb/step1`
     directory:

     |  |
     | --- |
     | *components-use\_case\_tmongodbbulkload\_1.png*  *components-use\_case\_tmongodbbulkload\_2.png*  *components-use\_case\_tmongodbbulkload\_3.png*  *components-use\_case\_tmongodbbulkload\_4.png* |
   * In the
     `E:/photos/mongodb/step2`
     directory:

     |  |
     | --- |
     | *components-use\_case\_tmongodbbulkload\_5.png*  *components-use\_case\_tmongodbbulkload\_6.png*  *components-use\_case\_tmongodbbulkload\_7.png*  *components-use\_case\_tmongodbbulkload\_8.png* |
5. In the Azure Storage
   folder field, enter the directory where you want to write files.
   This directory will be created in the container to be used if it does not exist.
   In this example, enter
   `photos`.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-configuring-tazurestoragelist-standard-component -->
# Configuring tAzureStorageList

Last updated: 9/30/2026

## Procedure

1. Double-click tAzureStorageList to open its Component view.
2. Select
   the component whose connection details will be used to set up the Azure storage
   connection. In this example, it is
   `tAzureStorageConnection_1`.
3. In the Container name
   field, enter the name of the container in which you need to check whether the
   given files exist. In this scenario, it is
   `talendcontainer`.
4. Under the Blob filter table, click the
   [+] button to add one row in the
   table.
5. In the Prefix column,
   enter the common prefix of the names of the files (blobs) to be checked. This
   prefix represents a virtual directory level you designate as the starting point
   down from which files (blobs) are checked. In this example, it is
   `photos/`.

   For further information about blob names, see <http://msdn.microsoft.com/en-us/library/dd135715.aspx>.
6. In the Include sub-directories column,
   select the check box in the newly added row. This allows tAzureStorageList to check all the files at any
   hierarchical level beneath the designated starting point.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestoragelist-tazurestorageconnection-tazurestoragecontainercreate-tjava-configuring-tjava-standard-component -->
# Configuring tJava

Last updated: 9/30/2026

## Procedure

1. Double-click tJava to
   open its Component view.
2. In the Code field, enter
   System.out.println();
3. In the Outline panel,
   which, by default, is found to the left side of the Component view, expand the tAzureStorageList node.
4. From the Outline panel, drop the
   CONTAINER\_BLOB global variable into the
   parentheses in the code in the Component
   view so as to make the code read:
   System.out.println(((Boolean)globalMap.get("tAzureStorageList\_1\_CURRENT\_BLOB")));
