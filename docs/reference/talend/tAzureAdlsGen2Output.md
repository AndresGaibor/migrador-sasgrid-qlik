<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2output · versión 8.0 -->
# tAzureAdlsGen2Output

Last updated: 9/30/2026

Uploads incoming data to an ADLS Gen2 file system of an Azure storage
account in the specified format.

## tAzureAdlsGen2Output Standard properties

These properties are used to configure tAzureAdlsGen2Output running in the Standard Job framework.

The Standard
tAzureAdlsGen2Output component belongs to the Cloud family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection).  Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Sync columns | Click this button to retrieve the schema from the previous component connected in the Job. |
| Authentication method | Select one of the following authentication method from the drop-down list.   * Shared key,   which requires an account access key. See [Manage a storage   account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?toc=%2fazure%2fstorage%2fblobs%2ftoc.json) for related information. * Shared Access   Signature, which requires a shared access signature.   See [Constructing the Account SAS   URI](https://docs.microsoft.com/en-us/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri) for related information. * Azure Active   Directory, Select this option to use Azure Active Directory authentication when   establishing the connection. See [Azure AD Authentication](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication) for related   information.   For more information on how to connect ADLS Gen components to Microsoft OneLake, see [Connecting tAzureAdlsGen2 components to Microsoft Fabric OneLake](tazureadlsgen2-connecting-to-ms-fabric-onelake "Configure the connection settings of tAzureAdlsGen2 components to access files in Microsoft Fabric OneLake."). |
| Account name | Enter the name of the Data Lake Storage account you need to access. Ensure that the administrator of the system has granted you the appropriate access permissions to this account. |
| Endpoint suffix | Enter the Azure Storage service endpoint.  The combination of the account name and the Azure Storage service endpoint forms the endpoint of the storage account. |
| Shared key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. To know how to get your key, read [Manage a storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-manage?toc=%2fazure%2fstorage%2fblobs%2ftoc.json).  To enter the shared key, click the [...] button next to the Shared key field to bring out the Enter a new password dialog box, enter the shared key in the text field, and click OK. Note that you can enter the shared key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter shared keys in the Java mode   only.  This field is available if you select Shared key from Authentication method drop-down list. |
| SAS token | Enter your account SAS token. You can get the SAS token for each allowed service on the Microsoft Azure portal after generating SAS. The SAS token format is `https://<$storagename><$service>.core.windows.net/<$sastoken>`, where `<$storagename>` is the storage account name, `<$service>` is the allowed service name (blob, file, queue or table), and `<$sastoken>` is the SAS token value. For more information, read [Constructing the Account SAS URI](https://docs.microsoft.com/en-us/rest/api/storageservices/Constructing-an-Account-SAS?redirectedfrom=MSDN#constructing-the-account-sas-uri).  This field is available if you select Shared Access Signature from Authentication method drop-down list. |
| Tenant ID | Enter the ID of the Azure AD tenant. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client ID | Enter the client ID of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Client Secret | Enter the client secret of your application. See [Acquire a token from Azure AD for authorizing requests from a client application](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app) for related information.  To enter the client secret, click the [...] button next to the Client secret field to bring out the Enter a new password dialog box, enter the client secret in the text field, and click OK. Note that you can enter the client secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  This option is available if you select Azure Active Directory from the Authentication method drop-down list. |
| Check connection | Click this button to validate the connection parameters provided. |
| Filesystem | Enter the name of the target blob container.  You can also click the [...] button to the right of this field and select the desired Blob container from the list in the dialog box. |
| Blobs path | Enter the path to the target blob. |
| Format | Set the format for the incoming data. Currently, the following formats are supported: CSV, AVRO, JSON, Parquet, and Delta. |
| Field Delimiter | Set the field delimiter. You can select Semicolon, Comma, Tabulation, and Space from the drop-down list; you can also select Other and enter your own in the Custom field delimiter field. |
| Record Separator | Set the record separator. You can select LF, CR, and CRLF from the drop-down list; you can also select Other and enter your own in the Custom Record Separator field. |
| Text Enclosure Character | Enter the character used to enclose text. |
| Escape character | Enter the character of the row to be escaped. |
| Header | Select this check box to insert a header row to the data. The schema column names will be used as column headers. |
| File Encoding | Select the file encoding from the drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Max batch size | Set the maximum number of lines allowed in each batch.  Do not change the default value unless you are facing performance issues. Increasing the batch size can improve the performance but a value too high could cause Job failures. |
| Timeout | Specify a timeout period (in seconds) for creating the connection. An error will be generated if the connection is not created successfully in the timeout period.  Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use date pattern from schema | When selected, this option allows you to keep the date pattern used in the source schema when writing data to Azure. |
| Blob Template Name | Enter a string as the name prefix for the blob files generated. The name of a blob file generated will be the name prefix followed by another string.  This parameter is not available when you select Delta from the Format drop-down list. |
| Partition columns | Enter the name of the columns to be partitioned. This parameter is only available when you select Delta from the Format drop-down list. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows successfully processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as an end component of a Job or subJob and it always needs an input link. |

**Related concepts**  

* [Accessing Azure ADLS Gen2 storage](tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-accessing-azure-adls-gen2-storage-this "This scenario writes data to an Azure ADLS Gen2 file system, retrieves the data, and then displays it.")
* [Applying a preparation on ADLS Gen2 Delta tables](applying-preparation-adls-gen2 "This scenario retrieves data from an Azure ADLS Gen2 file system, prepares the data, and then displays it.")
