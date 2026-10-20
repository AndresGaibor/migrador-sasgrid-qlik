<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazurefsconfiguration · versión 8.0 -->
# tAzureFSConfiguration

Last updated: 9/30/2026

Provides authentication information for Spark to connect to a given Azure file system.

### In this section

* [tAzureFSConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazurefsconfiguration-properties-for-apache-spark-batch?id=379)
* [tAzureFSConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazurefsconfiguration-properties-for-apache-spark-streaming?id=380)
* [tAzureFSConfiguration properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazurefsconfiguration-properties-for-apache-spark-structured-streaming?id=381)

**Related reference**  

* [Creating Hive external tables based on ADLS Databricks](tjava-tazurefsconfiguration-databricks-gen2-file)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazurefsconfiguration-properties-for-apache-spark-batch -->
# tAzureFSConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tAzureFSConfiguration running in the Spark Batch Job framework.

The Spark Batch
tAzureFSConfiguration component belongs to the Storage family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Azure FileSystem | Select the file system to be used. Then the parameters to be defined are displayed accordingly.  This component is designed to store your actual user data or business data in a Data Lake Storage system and it is not compatible with a Data Lake Storage that is defined as primary storage in HDInsight. For this reason, if you are using this component with HDInsight, then when you launch your HDInsight, always set Blob storage, and do not set Data Lake Storage, as primary storage. |

When you use this component with Azure Blob Storage:

| Properties | Description |
| --- | --- |
| Blob storage account | Enter the name of the storage account you need to access. A storage account name can be found in the Storage accounts dashboard of the Microsoft Azure Storage system to be used. Ensure that the administrator of the system has granted you the appropriate access permissions to this storage account. |
| Account key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. Select the component whose connection details will be used to set up the connection to Azure storage from the drop-down list. |
| Container | Enter the name of the blob container you need to use. |

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

When you use this component with Azure Data Lake Storage Gen1:

| Properties | Description |
| --- | --- |
| Data Lake Storage account | Enter the name of the Data Lake Storage account you need to access. Ensure that the administrator of the system has granted you the appropriate access permissions to this account. |
| Client ID and Client key | In the Client ID and the Client key fields, enter, respectively, the authentication ID and the authentication key generated upon the registration of the application that the current Job you are developing uses to access Azure Data Lake Storage.  Ensure that the application to be used has appropriate permissions to access Azure Data Lake. You can check this on the Required permissions view of this application on Azure. For further information, see Azure documentation [Assign the Azure AD application to the Azure Data Lake Storage account file or folder](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-service-to-service-authenticate-using-active-directory#step-3-assign-the-azure-ad-application-to-the-azure-data-lake-store-account-file-or-folder). |
| Token endpoint | In the Token endpoint field, copy-paste the OAuth 2.0 token endpoint that you can obtain from the Endpoints list accessible on the App registrations page on your Azure portal. |

When you use this component with Azure Data Lake Storage Gen2:

| Properties | Description |
| --- | --- |
| Authentication mode | Set the authentication type to connect to Azure ADLS Gen2 storage. The following options are provided:  * Secret Key: Select this option to access   Azure ADLS Gen2 using the key of the file system of your Azure   storage account. * Azure Active Directory: Select this option to   access Azure ADLS Gen2 using your Azure Active Directory (Azure AD)   credentials. |
| Data Lake Storage account | Enter the name of the Data Lake Storage account you need to access. Ensure that the administrator of the system has granted you the appropriate access permissions to this account. |
| Application ID and Directory ID | In the Application ID and Directory ID fields, copy-paste, respectively the Application (client) ID and the Directory (tenant) ID that you can obtain from the Overview tab accessible on the App registrations page on your Azure portal.  These fields are only available if you select Azure Active Directory from the Authentication mode drop-down list. |
| Client Key | In the Client key field, enter the authentication key generated upon the registration of the application that the current Job you are developing uses to access Azure Data Lake Storage.  Ensure that the application to be used has appropriate permissions to access Azure Data Lake. You can check this on the Required permissions view of this application on Azure. For further information, see Azure documentation [Assign the Azure AD application to the Azure Data Lake Storage account file or folder](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-service-to-service-authenticate-using-active-directory#step-3-assign-the-azure-ad-application-to-the-azure-data-lake-store-account-file-or-folder).  This field is only available if you select Azure Active Directory from the Authentication mode drop-down list. |
| Account key | Enter the account key to access the file system of your Azure storage account. This field is only available if you select Secret Key from the Authentication mode drop-down list. |
| File system | In this field, enter the name of the ADLS Gen2 file system to be used.  An ADLS Gen2 file system is hierarchical and so compatible with HDFS. |
| Create remote file system during initialization | If the ADLS Gen2 file system to be used does not exist, select this check box to create it on the fly. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | You can use multiple tAzureFSConfiguration components in a subJob to provide connection configuration to several Azure file systems (ADLS Gen2 only) for the whole Job. For other Azure file systems (ADLS Gen1 and Azure Blob Storage), this component is used standalone in a subJob.  If you are using multiple tAzureFSConfiguration components, make sure you set the same value for the createRemoteFileSystemDuringInitialization property for all the Azure ADLS Gen2 storage.  tAzureFSConfiguration does not support SSL access to Google Cloud Dataproc V1.1.  The output files of Spark cannot be merged into one file on Azure Data Lake Storage, because this function is not supported by Azure Data Lake Storage. In addition, this function has been deprecated in the latest Hadoop API. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * When using HDInsight, specify the blob to be used for Job   deployment in the Windows Azure Storage   configuration area in the Spark   configuration tab. * When using Altus, specify the S3 bucket or the Azure   Data Lake Storage for Job deployment in the Spark   configuration tab.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazurefsconfiguration-properties-for-apache-spark-structured-streaming -->
# tAzureFSConfiguration properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tAzureFSConfiguration
running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tAzureFSConfiguration component belongs to the Storage family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Azure FileSystem | Select the file system to use. The available properties depend on your selection. |

When you use this component with Azure Blob Storage:

| Properties | Description |
| --- | --- |
| Blob storage account | Enter the name of the storage account you need to access. A storage account name can be found in the Storage accounts dashboard of the Microsoft Azure Storage system to be used. Ensure that the administrator of the system has granted you the appropriate access permissions to this storage account. |
| Account key | Enter the key associated with the storage account you need to access. Two keys are available for each account and by default, either of them can be used for this access. Select the component whose connection details will be used to set up the connection to Azure storage from the drop-down list. |
| Container | Enter the name of the blob container you need to use. |

When you use this component with Azure Data Lake Storage Gen2:

| Properties | Description |
| --- | --- |
| Authentication mode | Set the authentication type to connect to Azure ADLS Gen2 storage. The following options are provided:  * Secret Key: Select this option to access   Azure ADLS Gen2 using the key of the file system of your Azure   storage account. * Azure Active Directory: Select this option to   access Azure ADLS Gen2 using your Azure Active Directory (Azure AD)   credentials. |
| Data Lake Storage account | Enter the name of the Data Lake Storage account you need to access. Ensure that the administrator of the system has granted you the appropriate access permissions to this account. |
| Application ID and Directory ID | In the Application ID and Directory ID fields, copy-paste, respectively the Application (client) ID and the Directory (tenant) ID that you can obtain from the Overview tab accessible on the App registrations page on your Azure portal.  These fields are only available if you select Azure Active Directory from the Authentication mode drop-down list. |
| Client Key | In the Client key field, enter the authentication key generated upon the registration of the application that the current Job you are developing uses to access Azure Data Lake Storage.  Ensure that the application to be used has appropriate permissions to access Azure Data Lake. You can check this on the Required permissions view of this application on Azure. For further information, see Azure documentation [Assign the Azure AD application to the Azure Data Lake Storage account file or folder](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-service-to-service-authenticate-using-active-directory#step-3-assign-the-azure-ad-application-to-the-azure-data-lake-store-account-file-or-folder).  This field is only available if you select Azure Active Directory from the Authentication mode drop-down list. |
| Account key | Enter the account key to access the file system of your Azure storage account. This field is only available if you select Secret Key from the Authentication mode drop-down list. |
| File system | In this field, enter the name of the ADLS Gen2 file system to be used.  An ADLS Gen2 file system is hierarchical and so compatible with HDFS. |
| Create remote file system during initialization | If the ADLS Gen2 file system to be used does not exist, select this check box to create it on the fly. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | You can use multiple tAzureFSConfiguration components in a subJob to provide connection configuration to several Azure file systems (ADLS Gen2 only) for the whole Job. For Azure Blob Storage, this component is used standalone in a subJob. If you are using multiple tAzureFSConfiguration components, make sure you set the same value for the createRemoteFileSystemDuringInitialization property for all the Azure ADLS Gen2 storage.  The output files of Spark cannot be merged into one file on Azure Data Lake Storage, because this function is not supported by Azure Data Lake Storage. In addition, this function has been deprecated in the latest Hadoop API.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |
