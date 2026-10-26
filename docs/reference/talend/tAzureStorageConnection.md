<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-blob/tazurestorageconnection · versión 8.0 -->
# tAzureStorageConnection

Last updated: 9/30/2026

Uses authentication and the protocol information to create a connection to the
Microsoft Azure Storage system that can then be reused by other Azure Storage
components.

## tAzureStorageConnection Standard properties

These properties are used to configure tAzureStorageConnection running in the Standard Job framework.

The Standard
tAzureStorageConnection component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Account Name | Enter the name of the storage account you need to access. A storage account name can be found in the Storage accounts dashboard of the Microsoft Azure Storage system to be used. Ensure that the administrator of the system has granted you the appropriate access permissions to this storage account. |
| Authentication type | Set the authentication type for connecting to Microsoft Azure Blob storage: Basic, Azure Active Directory, or Managed identities.   * Basic: Select   this option if you want to access Microsoft Azure Blob storage using   your storage account access key or a shared access signature. See [Configuring Azure Storage   connection strings](https://docs.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string) and [Using shared access signatures   (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) for related information. * Azure Active   Directory: Select this option to access Microsoft Azure   Blob storage using your Azure Active Directory (Azure AD) credentials.   See [Authorize access to blobs and   queues using Azure Active Directory](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad?toc=/azure/storage/blobs/toc.json) for related   information. * Managed identities: Select this option to use   system-assigned managed identities to access Azure Active   Directory-protected resources. For more information, see [What are managed identities for Azure   resources](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) and [Azure services that can use managed   identities to access other services](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/managed-identities-status).   Information noteNote: The Managed identities option is available only when you have installed the 8.0.1-R2023-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Region | Select one of the following Azure regions from the drop-down list.  * Azure Global * Azure China * Azure Germany * Azure Government * Azure Custom  You can use a customized Azure region by selecting the Azure Custom option and entering the endpoint suffix and the authority host URL in the Endpoint suffix field and the Authority host field. Note that the authority host URL is required when Azure Active Directory is selected from the Authentication type drop-down list. This drop-down list is not available if you select Managed identities from the Authentication type drop-down list.  Information noteNote: The Region drop-down list is available only when you have installed the 8.0.1-R2023-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Account Key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. Select the component whose connection details will be used to set up the connection to Azure storage from the drop-down list.  This option is available if you select Basic from the Authentication type drop-down list. |
| Protocol | Select the protocol for this connection to be created.  This option is available if you select Basic from the Authentication type drop-down list. |
| Use Azure Shared Access Signature | Select this check box to use a shared access signature (SAS) to access the storage resources without need for the account key. For more information, see [Using Shared Access Signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/storage-dotnet-shared-access-signature-part-1).  In the Azure Shared Access Signature field displayed, enter your account SAS URL between double quotation marks. You can get the SAS URL for each allowed service on Microsoft Azure portal after generating SAS. The SAS URL format is https://<$storagename>.<$service>.core.windows.net/<$sastoken>, where <$storagename> is the storage account name, <$service> is the allowed service name (`blob`, `file`, `queue` or `table`), and <$sastoken> is the SAS token value. For more information, see [Constructing the Account SAS URI](https://docs.microsoft.com/fr-fr/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri).  Note that the SAS has valid period, you can set the start time at which the SAS becomes valid and the expiry time after which the SAS is no longer valid when generating it, and you need to make sure your SAS is still valid when running your Job.  This option is available if you select Basic from the Authentication type drop-down list. |
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other Azure Storage components.  Knowledge about Microsoft Azure Storage is required. |

**Related concepts**  

* [Handling data with Microsoft Azure Table storage](tazurestorageconnection-tazurestorageinputtable-tlogrow-handling-data-with-microsoft-azure-table-storage-standard-component-bigdata-the "Here is an example of using Talend components to connect to a Microsoft Azure storage account that gives you access to Azure storage table service, write some employee data into an Azure storage table, and then retrieve the employee data from the table and display it on the console.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-handling-data-with-microsoft-azure-table-storage-standard-component-bigdata-the -->
# Handling data with Microsoft Azure Table storage

Last updated: 9/30/2026

Here is an example of using Talend components to connect to a
Microsoft Azure storage account that gives you access to Azure storage table service, write
some employee data into an Azure storage table, and then retrieve the employee data from the
table and display it on the console.

The employee data used in this example is as follows:

```
#Id;Name;Site;Job;Date;Salary
12000;Gerald Roosevelt;Beijing;Software Developer;2008-01-01;15000.01
12001;Benjamin Harrison;Paris;Software Developer;2008-11-22;13000.11
12002;Bob Clinton;Beijing;Software Tester;2008-05-12;12000.22
12003;James Quincy;Paris;Technical Writer;2009-03-10;12000.33
12004;Gerald Harrison;Beijing;Software Tester;2009-06-20;12500.44
12005;Harry Madison;Paris;Software Developer;2009-10-15;14000.55
12006;Helen Roosevelt;Beijing;Software Tester;2009-03-25;13500.66
12007;Mary Clinton;Beijing;Software Developer;2010-02-20;16000.77
12008;Cathey Quincy;Paris;Software Developer;2010-07-15;14000.88
12009;John Smith;Beijing;Technical Writer;2011-02-10;12500.99
```

### In this section

* [Creating a Job for handling data with Azure Table storage](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-creating-job-for-handling-data-with-azure-table-storage-standard-component-bigdata-create)
* [Connecting to an Azure Storage account](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-connecting-to-azure-storage-account-standard-component-bigdata-the)
* [Writing data into an Azure Storage table](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-writing-data-into-azure-storage-table-standard-component-bigdata)
* [Retrieving data from the Azure Storage table](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-retrieving-data-from-azure-storage-table-standard-component-bigdata)
* [Executing the Job to handle data with Azure Table storage](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-executing-job-to-handle-data-with-azure-table-storage-standard-component-bigdata-press)

**Related reference**  

* [tAzureStorageConnection](tazurestorageconnection "Uses authentication and the protocol information to create a connection to the Microsoft Azure Storage system that can then be reused by other Azure Storage components.")
* [tAzureStorageInputTable](tazurestorageinputtable "Retrieves a set of entities that satisfy the specified filter criteria from an Azure storage table.")
* [tAzureStorageOutputTable](tazurestorageoutputtable "Performs the defined action on a given Azure storage table and inserts, replaces, merges or deletes entities in the table based on the incoming data from the preceding component.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection -->
# tAzureStorageConnection

Last updated: 9/30/2026

Uses authentication and the protocol information to create a connection to the
Microsoft Azure Storage system that can then be reused by other Azure Storage
components.

## tAzureStorageConnection Standard properties

These properties are used to configure tAzureStorageConnection running in the Standard Job framework.

The Standard
tAzureStorageConnection component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Account Name | Enter the name of the storage account you need to access. A storage account name can be found in the Storage accounts dashboard of the Microsoft Azure Storage system to be used. Ensure that the administrator of the system has granted you the appropriate access permissions to this storage account. |
| Authentication type | Set the authentication type for connecting to Microsoft Azure Blob storage: Basic, Azure Active Directory, or Managed identities.   * Basic: Select   this option if you want to access Microsoft Azure Blob storage using   your storage account access key or a shared access signature. See [Configuring Azure Storage   connection strings](https://docs.microsoft.com/en-us/azure/storage/common/storage-configure-connection-string) and [Using shared access signatures   (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) for related information. * Azure Active   Directory: Select this option to access Microsoft Azure   Blob storage using your Azure Active Directory (Azure AD) credentials.   See [Authorize access to blobs and   queues using Azure Active Directory](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad?toc=/azure/storage/blobs/toc.json) for related   information. * Managed identities: Select this option to use   system-assigned managed identities to access Azure Active   Directory-protected resources. For more information, see [What are managed identities for Azure   resources](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) and [Azure services that can use managed   identities to access other services](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/managed-identities-status).   Information noteNote: The Managed identities option is available only when you have installed the 8.0.1-R2023-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Region | Select one of the following Azure regions from the drop-down list.  * Azure Global * Azure China * Azure Germany * Azure Government * Azure Custom  You can use a customized Azure region by selecting the Azure Custom option and entering the endpoint suffix and the authority host URL in the Endpoint suffix field and the Authority host field. Note that the authority host URL is required when Azure Active Directory is selected from the Authentication type drop-down list. This drop-down list is not available if you select Managed identities from the Authentication type drop-down list.  Information noteNote: The Region drop-down list is available only when you have installed the 8.0.1-R2023-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Account Key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. Select the component whose connection details will be used to set up the connection to Azure storage from the drop-down list.  This option is available if you select Basic from the Authentication type drop-down list. |
| Protocol | Select the protocol for this connection to be created.  This option is available if you select Basic from the Authentication type drop-down list. |
| Use Azure Shared Access Signature | Select this check box to use a shared access signature (SAS) to access the storage resources without need for the account key. For more information, see [Using Shared Access Signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/storage-dotnet-shared-access-signature-part-1).  In the Azure Shared Access Signature field displayed, enter your account SAS URL between double quotation marks. You can get the SAS URL for each allowed service on Microsoft Azure portal after generating SAS. The SAS URL format is https://<$storagename>.<$service>.core.windows.net/<$sastoken>, where <$storagename> is the storage account name, <$service> is the allowed service name (`blob`, `file`, `queue` or `table`), and <$sastoken> is the SAS token value. For more information, see [Constructing the Account SAS URI](https://docs.microsoft.com/fr-fr/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri).  Note that the SAS has valid period, you can set the start time at which the SAS becomes valid and the expiry time after which the SAS is no longer valid when generating it, and you need to make sure your SAS is still valid when running your Job.  This option is available if you select Basic from the Authentication type drop-down list. |
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other Azure Storage components.  Knowledge about Microsoft Azure Storage is required. |

**Related concepts**  

* [Handling data with Microsoft Azure Table storage](tazurestorageconnection-tazurestorageinputtable-tlogrow-handling-data-with-microsoft-azure-table-storage-standard-component-bigdata-the "Here is an example of using Talend components to connect to a Microsoft Azure storage account that gives you access to Azure storage table service, write some employee data into an Azure storage table, and then retrieve the employee data from the table and display it on the console.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-connecting-to-azure-storage-account-standard-component-bigdata-the -->
# Connecting to an Azure Storage account

Last updated: 9/30/2026

Configure the tAzureStorageConnection component to open
the connection to an Azure Storage account.

## Before you begin

The Azure Storage account, which allows you to access the Azure Table storage service
and store the provided employee data, has already been created. For more information
about how to create an Azure Storage account, see [About Azure storage accounts](https://docs.microsoft.com/en-us/azure/storage/storage-create-storage-account).

## Procedure

1. Double-click the tAzureStorageConnection component to
   open its Basic settings view on the
   Component tab.
2. In the Account Name field, specify the name of the
   storage account you need to access.
3. In the Account Key field, specify the key associated
   with the storage account you need to access.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-creating-job-for-handling-data-with-azure-table-storage-standard-component-bigdata-create -->
# Creating a Job for handling data with Azure Table storage

Last updated: 9/30/2026

Create a Job to connect to an Azure storage account, write some employee data
into an Azure storage table, and then retrieve that information from the table and
display it on the console.

## Procedure

1. Create a new Job and add a tAzureStorageConnection
   component, a tFixedFlowInput component, a
   tAzureStorageOutputTable component, a
   tAzureStorageInputTable component, and a
   tLogRow component by typing their names in the design
   workspace or dropping them from the Palette.
2. Link the tFixedFlowInput component to the
   tAzureStorageOutputTable component using a
   Row > Main
   connection.
3. Do the same to link the tAzureStorageInputTable
   component to the tLogRow component.
4. Link the tAzureStorageConnection component to the
   tFixedFlowInput component using a
   Trigger > OnSubjobOk
   connection.
5. Do the same to link the tFixedFlowInput component to the
   tAzureStorageInputTable component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-executing-job-to-handle-data-with-azure-table-storage-standard-component-bigdata-press -->
# Executing the Job to handle data with Azure Table storage

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the Job for
handling data with Azure Table storage, you can then execute the Job and verify the Job
execution result.

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

   As shown above, the Job is executed successfully and the employee data is
   displayed on the console, with the timestamp value that indicates when each
   entity was inserted.
3. Optional: 
   Double-check the employee data that has been written into the Azure Storage
   table `employee` using Microsoft Azure Storage Explorer.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-handling-data-with-microsoft-azure-table-storage-standard-component-bigdata-the -->
# Handling data with Microsoft Azure Table storage

Last updated: 9/30/2026

Here is an example of using Talend components to connect to a
Microsoft Azure storage account that gives you access to Azure storage table service, write
some employee data into an Azure storage table, and then retrieve the employee data from the
table and display it on the console.

The employee data used in this example is as follows:

```
#Id;Name;Site;Job;Date;Salary
12000;Gerald Roosevelt;Beijing;Software Developer;2008-01-01;15000.01
12001;Benjamin Harrison;Paris;Software Developer;2008-11-22;13000.11
12002;Bob Clinton;Beijing;Software Tester;2008-05-12;12000.22
12003;James Quincy;Paris;Technical Writer;2009-03-10;12000.33
12004;Gerald Harrison;Beijing;Software Tester;2009-06-20;12500.44
12005;Harry Madison;Paris;Software Developer;2009-10-15;14000.55
12006;Helen Roosevelt;Beijing;Software Tester;2009-03-25;13500.66
12007;Mary Clinton;Beijing;Software Developer;2010-02-20;16000.77
12008;Cathey Quincy;Paris;Software Developer;2010-07-15;14000.88
12009;John Smith;Beijing;Technical Writer;2011-02-10;12500.99
```

### In this section

* [Creating a Job for handling data with Azure Table storage](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-creating-job-for-handling-data-with-azure-table-storage-standard-component-bigdata-create)
* [Connecting to an Azure Storage account](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-connecting-to-azure-storage-account-standard-component-bigdata-the)
* [Writing data into an Azure Storage table](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-writing-data-into-azure-storage-table-standard-component-bigdata)
* [Retrieving data from the Azure Storage table](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-retrieving-data-from-azure-storage-table-standard-component-bigdata)
* [Executing the Job to handle data with Azure Table storage](/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-executing-job-to-handle-data-with-azure-table-storage-standard-component-bigdata-press)

**Related reference**  

* [tAzureStorageConnection](tazurestorageconnection "Uses authentication and the protocol information to create a connection to the Microsoft Azure Storage system that can then be reused by other Azure Storage components.")
* [tAzureStorageInputTable](tazurestorageinputtable "Retrieves a set of entities that satisfy the specified filter criteria from an Azure storage table.")
* [tAzureStorageOutputTable](tazurestorageoutputtable "Performs the defined action on a given Azure storage table and inserts, replaces, merges or deletes entities in the table based on the incoming data from the preceding component.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-retrieving-data-from-azure-storage-table-standard-component-bigdata -->
# Retrieving data from the Azure Storage table

Last updated: 9/30/2026

Configure the tAzureStorageInputTable component and the
tLogRow component to retrieve the employee data from the
Azure Storage table.

## Procedure

1. Double-click the tAzureStorageInputTable component to
   open its Basic settings view.
2. From the connection component drop-down list, select the component whose
   connection details will be used to set up the connection to the Azure Storage
   service, `tAzureStorageConnection_1` in this example.
3. In the Table name field, enter the name of the table
   from which the employee data will be retrieved, `employee`
   in this example.
4. Click  next to Edit schema to open
   the schema dialog box.

   Note that the schema has already been predefined with two read-only columns
   `RowKey` and `PartitionKey` of
   String type, and another column `Timestamp` of Date
   type. The `RowKey` and
   `PartitionKey` columns correspond to the
   `Id` and `Site` columns of the
   tAzureStorageOutputTable schema.
5. Define the schema by adding another four columns that hold other employee data,
   `Name` and `Job` of String type,
   `Date` of Date type, and `Salary`
   of Double type. Then click OK to save the changes and
   accept the propagation prompted by the pop-up dialog box.
6. Click Advanced settings to open its view.
7. Click  under the
   Name mappings table to add one row and set the
   Schema column name cell with the value
   `"Name"` and the Entity property
   name cell with the value `"EmployeeName"`
   to map the schema column name with the property name of each entity in the Azure
   table.

   Note that for the tAzureStorageInputTable component,
   the `PartitionKey` and `RowKey`
   columns have already been added automatically to the schema and you do not
   need to specify the mapping relationship for them.
8. Double-click the tLogRow component to open its
   Basic settings view and in the
   Mode area, select Table (print values in
   cells of a table) for a better display of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-storage-table/tazurestorageconnection-tazurestorageinputtable-tlogrow-writing-data-into-azure-storage-table-standard-component-bigdata -->
# Writing data into an Azure Storage table

Last updated: 9/30/2026

Configure the tFixedFlowInput component and the
tAzureStorageOutputTable component to write the employee data
into an Azure Storage table.

## Procedure

1. Double-click the tFixedFlowInput component to open its
   Basic settings view on the
   Component tab.
2. Click  next to Edit schema to open the
   schema dialog box and define the schema by adding six columns:
   `Id`, `Name`,
   `Site`, and `Job` of String type,
   `Date` of Date type, and `Salary`
   of Double type. Then click OK to save the changes and
   accept the propagation prompted by the pop-up dialog box.

   Note that in this example, the `Site` and
   `Id` columns are used to feed the values of the
   `PartitionKey` and `RowKey`
   system properties of each entity and they should be of String type, and the
   `Name` column is used to feed the value of the
   `EmployeeName` property of each entity.
3. In the Mode area, select Use Inline
   Content(delimited file) and in the
   Content field displayed, enter the employee data that
   will be written into the Azure Storage table.
4. Double-click the tAzureStorageOutputTable component to
   open its Basic settings view on the
   Component tab
5. From the connection component drop-down list, select the component whose
   connection details will be used to set up the connection to the Azure Storage
   service, `tAzureStorageConnection_1` in this example.
6. In the Table name field, enter the name of the table
   into which the employee data will be written, `employee` in
   this example.
7. From the Action on table drop-down list, select the
   operation to be performed on the specified table, `Drop table if exist
   and create` in this example.
8. Click Advanced settings to open its view.
9. Click  under the
   Name mappings table to add three rows and map the
   schema column name with the property name of each entity in the Azure table. In
   this example,

   * the `Site` column is used to feed the value of the
     `PartitionKey` system property, in the first
     row you need to set the Schema column name cell
     with the value `"Site"` and the Entity
     property name cell with the value
     `"PartitionKey"`.
   * the `Id` column is used to feed the value of the
     `RowKey` system property, in the second row you
     need to set the Schema column name cell with the
     value `"Id"` and the Entity property
     name cell with the value
     `"RowKey"`.
   * the `Name` column is used to feed the value of the
     `EmployeeName` property, in the third row you
     need to set the Schema column name cell with the
     value `"Name"` and the Entity property
     name cell with the value
     `"EmployeeName"`.
