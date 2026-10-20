<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2connection · versión 8.0 -->
# tAzureAdlsGen2Connection

Last updated: 9/30/2026

Creates a connection to an ADLS Gen2 file system using an Azure storage account for
other Azure ADLS Gen2 components.

* This component is available only when you have installed the R2022-01 Talend Studio
  Monthly update or a later one delivered by Talend.
  For more information, check with your administrator.
* This component is not shipped with your Talend Studio by
  default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tAzureAdlsGen2Connection Standard properties

These properties are used to configure tAzureAdlsGen2Connection
running in the Standard Job framework.

The Standard
tAzureAdlsGen2Connection component belongs to the Cloud family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Authentication method | Select one of the following authentication method from the drop-down list.   * Shared key,   which requires an account access key. See [Manage a storage   account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?toc=%2fazure%2fstorage%2fblobs%2ftoc.json) for related information. * Shared Access   Signature, which requires a shared access signature.   See [Constructing the Account SAS   URI](https://docs.microsoft.com/en-us/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri) for related information. * Azure Active   Directory, Select this option to use Azure Active Directory authentication when   establishing the connection. See [Azure AD Authentication](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication) for related   information.   For more information on how to connect ADLS Gen components to Microsoft OneLake, see [Connecting tAzureAdlsGen2 components to Microsoft Fabric OneLake](tazureadlsgen2-connecting-to-ms-fabric-onelake "Configure the connection settings of tAzureAdlsGen2 components to access files in Microsoft Fabric OneLake."). |
| Account name | Enter the name of the Data Lake Storage account you need to access. Ensure that the administrator of the system has granted you the appropriate access permissions to this account. |
| Endpoint suffix | Enter the Azure Storage service endpoint.  The combination of the account name and the Azure Storage service endpoint forms the endpoint of the storage account. |
| Shared key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. To know how to get your key, read [Manage a storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?toc=%2fazure%2fstorage%2fblobs%2ftoc.json).  To enter the shared key, click the [...] button next to the Shared key field to bring out the Enter a new password dialog box, enter the shared key in the text field, and click OK. Note that you can enter the shared key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter shared keys in the Java mode   only.  This field is available if you select Shared key from Authentication method drop-down list. |
| SAS token | Enter your account SAS token. You can get the SAS token for each allowed service on the Microsoft Azure portal after generating SAS. The SAS token format is `https://<$storagename><$service>.core.windows.net/<$sastoken>`, where `<$storagename>` is the storage account name, `<$service>` is the allowed service name (blob, file, queue or table), and `<$sastoken>` is the SAS token value. For more information, read [Constructing the Account SAS URI](https://docs.microsoft.com/en-us/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri).  This field is available if you select Shared Access Signature from Authentication method drop-down list. |
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  To enter the client secret, click the [...] button next to the Client secret field to bring out the Enter a new password dialog box, enter the client secret in the text field, and click OK. Note that you can enter the client secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Authenticate using Azure Active Directory | When selected, this option allows you pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Timeout | Specify a timeout period (in seconds) for creating the connection. An error will be generated if the connection is not created successfully in the timeout period. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows successfully processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is more commonly used with other Azure ADLS Gen2 components and it creates a connection that can be reused by them. |
