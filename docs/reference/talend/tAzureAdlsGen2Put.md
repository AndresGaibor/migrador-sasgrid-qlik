<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2put · versión 8.0 -->
# tAzureAdlsGen2Put

Last updated: 9/30/2026

Uploads local files to an ADLS Gen2 file system of an Azure storage account.

## tAzureAdlsGen2Put Standard properties

These properties are used to configure tAzureAdlsGen2Put
running in the Standard Job framework.

The Standard
tAzureAdlsGen2Put component belongs to the Cloud family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0.1-R2022-06 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Authentication method | Select one of the following authentication method from the drop-down list.   * Shared key,   which requires an account access key. See [Manage a storage   account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?toc=%2fazure%2fstorage%2fblobs%2ftoc.json) for related information. * Shared Access   Signature, which requires a shared access signature.   See [Constructing the Account SAS   URI](https://docs.microsoft.com/en-us/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri) for related information. * Azure Active   Directory, Select this option to use Azure Active Directory authentication when   establishing the connection. See [Azure AD Authentication](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication) for related   information.   For more information on how to connect ADLS Gen components to Microsoft OneLake, see [Connecting tAzureAdlsGen2 components to Microsoft Fabric OneLake](tazureadlsgen2-connecting-to-ms-fabric-onelake "Configure the connection settings of tAzureAdlsGen2 components to access files in Microsoft Fabric OneLake."). |
| Account name | Enter the name of the Data Lake Storage account you need to access. Ensure that the administrator of the system has granted you the appropriate access permissions to this account. |
| Endpoint suffix | Enter the Azure Storage service endpoint.  The combination of the account name and the Azure Storage service endpoint forms the endpoint of the storage account. |
| Shared key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. To know how to get your key, read [Manage a storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?toc=%2fazure%2fstorage%2fblobs%2ftoc.json).  To enter the shared key, click the [...] button next to the Shared key field to bring out the Enter a new password dialog box, enter the shared key in the text field, and click OK. Note that you can enter the shared key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  This field is available if you select Shared key from Authentication method drop-down list. |
| SAS token | Enter your account SAS token. You can get the SAS token for each allowed service on the Microsoft Azure portal after generating SAS. The SAS token format is `https://<$storagename><$service>.core.windows.net/<$sastoken>`, where `<$storagename>` is the storage account name, `<$service>` is the allowed service name (blob, file, queue or table), and `<$sastoken>` is the SAS token value. For more information, read [Constructing the Account SAS URI](https://docs.microsoft.com/en-us/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri).  This field is available if you select Shared Access Signature from Authentication method drop-down list. |
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  To enter the client secret, click the [...] button next to the Client secret field to bring out the Enter a new password dialog box, enter the client secret in the text field, and click OK. Note that you can enter the client secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| File system | Enter the name of the desired blob container.  You can also click the [...] button to the right of this field and select the desired blob container from the list in the dialog box. |
| Blobs path | Enter the path to the target blob. |
| Local folder | Enter the path to the folder whose files are to be uploaded. |
| Use file list | Select this option to upload specific files by specifying filemasks in the Files table.  To add a filemask, click the plus button on the bottom of the Files table to add a row in the table, enter the filemask string in the Filemask column, and, optionally, enter a string in the New name column to replace the matched strings in the names of uploaded files. Information noteNote: To prevent undesired files from being uploaded to the container, do not use these characters in the Filemask column: (, ), [, and ]. |
| Overwrite existing files | Select this option to overwrite the existing files whose names are identical to those of uploaded files. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Allow to escape the "+" sign in filemask | Select this option if you want to use + as a normal character in the filemask strings entered in the Files table in the Basic settings view.  If this option is not selected, + serves as a special RegEx character in the filemask strings. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component of a Job or subJob. |
