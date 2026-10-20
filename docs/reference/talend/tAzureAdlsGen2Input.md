<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input · versión 8.0 -->
# tAzureAdlsGen2Input

Last updated: 9/30/2026

Retrieves data from an ADLS Gen2 file system of an Azure storage
account and passes the data to the subsequent component connected to it through a Main>Row link.

## tAzureAdlsGen2Input Standard properties

These properties are used to configure tAzureAdlsGen2Input running in the Standard Job framework.

The Standard
tAzureAdlsGen2Input component belongs to the Cloud family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection).  Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema from the data object specified. |
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
| Header | Select this check box to insert a header row to the data retrieved.  Information noteNote:  * Select this option if the data to be retrieved has   a header row. In this case, you need also to make sure that the   column names in the schema are consistent with the column headers of   the data. * Clear this option if the data to be retrieved does not   have a header row. In this case, you need to name the columns in the   schema as `field0`, `field1`, `field2`, and so on. |
| File Encoding | Select the file encoding from the drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Timeout | Specify a timeout period (in seconds) for creating the connection. An error will be generated if the connection is not created successfully in the timeout period.  Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use date pattern from schema | When selected, this option allows you to use the date pattern that is used in the file stored in Azure. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows successfully processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as a start component of a Job or subJob and it always needs an output link. |

**Related concepts**  

* [Accessing Azure ADLS Gen2 storage](tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-accessing-azure-adls-gen2-storage-this "This scenario writes data to an Azure ADLS Gen2 file system, retrieves the data, and then displays it.")
* [Applying a preparation on ADLS Gen2 Delta tables](applying-preparation-adls-gen2 "This scenario retrieves data from an Azure ADLS Gen2 file system, prepares the data, and then displays it.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-accessing-azure-adls-gen2-storage-this -->
# Accessing Azure ADLS Gen2 storage

Last updated: 9/30/2026

This scenario writes data to an Azure ADLS Gen2 file system, retrieves
the data, and then displays it.

This scenario comprises two subJobs. The first subJob contains a
tFixedFlowInput and a tAzureADLSGen2Output
components. It writes data to an Azure ADLS Gen2 file system. The second one contains a
tAzureADLSGen2Input and a tLogRow components. It
retrieves and displays the data.

This scenario connects to Microsoft Azure through Shared Access Signature
(SAS) authentication. It assumes that you have an Azure ADLS account and you have created a
file system under the account.

Information noteNote: You can monitor the data using Microsoft Azure Storage
Explorer, a utility for managing your Azure storage resources. Check [Azure Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/) for related information.

### In this section

* [Obtaining the SAS token](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-obtaining-sas-token-log-into)
* [Creating the Job](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-creating-job-launch)
* [Setting up the Job](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-setting-up-job)
* [Executing the Job](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-executing-job-switch)

**Related reference**  

* [tAzureAdlsGen2Input](tazureadlsgen2input "Retrieves data from an ADLS Gen2 file system of an Azure storage account and passes the data to the subsequent component connected to it through a Main>Row link.")
* [tAzureAdlsGen2Output](tazureadlsgen2output "Uploads incoming data to an ADLS Gen2 file system of an Azure storage account in the specified format.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-creating-job-launch -->
# Creating the Job

Last updated: 9/30/2026

## Procedure

1. Launch Talend Studio and
   create an empty Job.
2. Drag and drop these four components on the workspace: tFixedFlowInput, tAzureADLSGen2Input, tAzureADLSGen2Output, and tLogRow.
3. Connect tFixedFlowInput to
   tAzureADLSGen2Output using a Row >
   Main connection.
4. Connect tAzureADLSGen2Input to tLogRow using
   a Row > Main connection.
5. Connect tFixedFlowInput to
   tAzureADLSGen2Input using a Trigger >
   OnSubjobOK connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-executing-job-switch -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Switch to the Run view.
2. Click the Run button.

   The Job writes data to the Azure ADLS Gen2 file system, and then reads the
   data from the Azure ADLS Gen2 file system as displayed in the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-obtaining-sas-token-log-into -->
# Obtaining the SAS token

Last updated: 9/30/2026

## Procedure

1. Log into Microsoft Azure portal using your Azure user account.
2. Select the Azure ADLS Gen2 resource to be used and click
   Shared access signature on the left pane.
3. Select Service,
   Container, and Object in the
   Allowed resource types section in the right pane.
4. Set the period in which the SAS token will be valid by setting the start and
   end date in the Start and End field.

   Information noteNote: You need also to set the time zone under the End field.
5. Select other options as needed.
6. Click Generate SAS and connection
   string.

   Information noteNote:
   * You may need to scroll down the right pane to have the Generate SAS and connection
     string button displayed.
   * The SAS token string will be generated after your click Generate SAS and connection
     string.
7. Copy the SAS token string generated and store it in a safe
   place for later use.

   Information noteNote: The SAS token string will be used for configuring tAzureADLSGen2Output and
   tAzureADLSGen2Input.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazureadlsgen2input-tazureadlsgen2output-tfixedflowinput-tlogrow-setting-up-job -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowInput component to open the Basic settings view. 
   1. Click the […]
      button next to Edit schema and
      add four columns in the schema editor: `ID`, type `Integer`; `Name`, type
      `String`; `Address`, type `String`, and `Date`, type `Date` and
      format of `dd-MM-yyyy`.
   2. Click Yes when
      prompted to propagated the changes. 

      This propagates the schema to the tAzureADLSGen2Input component.
   3. Select the Use Inline
      Content (delimited file) option.
   4. Enter the following in the Content field.

      ```
      1;Bill's Dive Shop;511 Maple Ave;07-07-2020
      2;Facelift Kitchen and Bath;220 Vine Ave.;04-23-2019
      3;Kermit the Pet Shop;1860 Parkside Ln.;05-29-2020
      4;Nirabi Auto Service;1915 Lewis Ln. Apt 13;06-19-2018
      5;Darcy Frame and Matting Servic;1633 McGovern place;01-07-2020
      6;Gourmet the Frog;788 Tennyson Ave.;01-31-2019
      							
      ```
   5. Leave other options as they are.
2. In the Basic settings
   view of the tAzureADLSGen2Output
   component:
   1. Check the schema and make sure the schema has the same
      columns as those for the tFixedFlowInput component.
   2. Select `Shared Access
      Signature` from the Authentication method drop-down list.
   3. Enter your account name and the SAS token string in
      the Account name and SAS token fields.
   4. Click the [...] button to the right of the Filesystem field and select the desired
      file system.
   5. Enter the desired Blobs path in the Blobs Path field.
   6. Select `CSV` from
      the Format drop-down list.
   7. Leave the other options as they are.
3. In the Basic settings
   view of the tAzureADLSGen2Input
   component:
   1. Click the […]
      button next to Edit schema and
      add the same four columns as those for the tFixedFlowInput component in the schema editor.
   2. Click Yes when
      prompted to propagated the changes. 

      This propagates the schema to the tLogRow component.
   3. Perform the same configuration as that of the tAzureADLSGen2Output component.
4. In the Basic settings
   view of the tLogRow component:
   1. Check the schema and make sure the schema has the same
      columns as those for the tAzureADLSGen2Input component.
   2. Select the Table (print
      values in cells of a table) option.
   3. Leave other options as they are.
5. Save the Job.
