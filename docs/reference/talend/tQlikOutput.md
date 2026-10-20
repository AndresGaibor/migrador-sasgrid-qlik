<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/qlik-cloud/tqlikoutput · versión 8.0 -->
# tQlikOutput

Last updated: 9/30/2026

Creates, updates, or deletes data files in Qlik Cloud.

## tQlikOutput Standard properties

These properties are used to configure tQlikOutput running in the Standard Job framework.

The Standard
tQlikOutput component belongs to the Cloud family.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Tenant URL | Enter the URL address of your Qlik Cloud account. |
| API key | Enter the Qlik Cloud API key in this field. To enter the raw key, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the key in the text field, and click OK. You can also use a context variable in that field. |
| Action | Select the action to be performed from the dropdown list:  * Create: Creates the data file in   Qlik Cloud. * Overwrite: Creates or updates an   existing data file in Qlik Cloud. * Delete: Deletes the data file in   Qlik Cloud. |
| File upload mode | Select the mode used to upload files. This field is available when Action is set to Create or Overwrite:  * Single file (default): Upload one file.   Use the Local file and   Remote file name fields. * Directory: Upload all valid files from a   local directory. Use the Directory path field.   Files in subdirectories are ignored. Invalid files are ignored and logged   as warnings.   When Action is set to Delete, only single-file deletion is supported. |
| Local file | Enter the path, or browse to the local file you want to upload, update, or delete in Qlik Cloud, or click the [...] button to browse to the file. This field is available in Single file mode. |
| Directory path | Enter the path to the local directory that contains the files to upload, or click the [...] button to browse to the directory. This field is available in Directory mode. |
| Specify ID | Select this checkbox to specify the identifier of the file you want to update or delete in the File ID field. If unselected, the Remote file name will be used. This field is only available if you select Overwrite or Delete from the Action dropdown list. |
| Remote file name | Enter the name of the file that will be uploaded in Qlik Cloud. The remote file name must include a file extension. If you do not set a Knowledge base, any file extension is accepted, but a file name without extension is rejected. If you set a Knowledge base, the extension must match the supported source file types for Qlik Answers knowledge bases. For more information, read [Qlik Answers](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Qlik-Answers.htm).  * If you select Overwrite in   Action, the remote file name can include a   folder, like some/folder/data.csv for example. * If you select Overwrite in   Action, the remote file name can include a   folder, like some/folder/data.csv for example. * If you select Delete in   Action, the remote file name can be either a   file or a folder path, as you can delete both files and folders.  This field is available in Single file mode. In Directory mode, each uploaded file keeps its local file name. |
| Space | To select one of the available spaces associated with your Qlik Cloud account, click the [...] button next to the field. In the dialog box displayed, select the space in which the file will be modified, or select the Use custom value checkbox and specify the space identifier in the Custom value field. After you select a space name from the list, its identifier will be displayed in the field.  For more information on spaces in Qlik Cloud, read [Working in spaces](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/Spaces.htm).  From the 8.0.1-R2025-12 Talend Studio monthly update onwards, spaces are displayed along with their associated environment, shown as "<space\_name> (<environment\_name>)", making it easier to identify spaces that exist in multiple Qlik Cloud environments that may have the same name. |
| Knowledge base | To select one of the available knowledge bases in Qlik Cloud and manage the files in it, click the [...] button next to the field. In the dialog box displayed, select the knowledge base that will be used, or select the Use custom value checkbox and specify the knowledge base identifier in the Custom value field. After you select a knowledge base name from the list, its identifier will be displayed in the field.  For more information on knowledge bases in Qlik Cloud, read [Working with knowledge bases](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/knowledge-bases.htm). |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect the log data at the component level. |
| Index file in knowledge base | This checkbox is selected by default and allows you to index new or updated files in Qlik Cloud:  * Number of indexation retries: Set the number of   times the component will attempt to index the file if the initial attempt   fails. * Indexation retry delay (seconds): Set the amount of   time (in seconds) to wait between each indexation retry attempt.   Note that two indexation operations cannot be performed in parallel in Qlik Cloud and can cause your Job to fail. For more information on indexing in Qlik Cloud, read [Indexing knowledge base data sources](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/indexing-knowledge-bases.htm). |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| FILE\_ID | The identifier of the file/folder. This is an After variable and it returns a string. In Directory mode, this variable contains the identifier of the last processed file. |

**Related tasks**  

* [Asking Qlik Answers assistant about password policies and updating its knowledge base with tQlikOutput to change its answers](tqlikoutput-asking-qlik-answers-assistant-about-password-policies-and-updating-kb-with-tqlikoutput-standard-component)
* [Generating a QVD file and uploading it to Qlik Cloud](tqvdoutput-trowgenerator-tqlikoutput-generating-qvd-and-uploading-it-to-qlik-cloud-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/qlik-cloud/tqlikoutput-asking-qlik-answers-assistant-about-password-policies-and-updating-kb-with-tqlikoutput-standard-component -->
# Asking Qlik Answers assistant about password policies and updating its knowledge base with tQlikOutput to change its answers

Last updated: 9/30/2026

The following Job aims at updating a knowledge base with a new password policy file using
the tQlikOutput component. This knowledge base is located in a specific space in Qlik Cloud and is
used in an AI-based Qlik Answers assistant to get answers to questions regarding password
policies and other company guidelines.

## Before you begin

This scenario uses Qlik Answers capabilities and its AI-based assistant. For more
information, read the corresponding [Qlik Answers documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Qlik-Answers.htm).

## Prerequisites

### Procedure

1. In Qlik Cloud: Make sure you have:
   1. created a knowledge base that contains the company policies.

      Knowledge bases provide the unstructured data that assistants use
      to generate responses to user questions. For more information, see [Working with knowledge
      bases](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/knowledge-bases.htm).
   2. created an assistant that uses the data in the knowledge base.

      Assistants offer an interface to interact with a range of data
      sources through natural language questions. For more information, see
      [Working with assistants](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/assistants.htm).
2. In Talend Studio:
   Drag and drop the following component from the Palette:
   tQlikOutput.

   The tQlikOutput component is a standalone component that
   does not require input components in the Job.

## Asking a question to the assistant about password guidelines in Qlik Cloud

### Procedure

1. In Qlik Cloud, go to the space where you have created your knowledge base and open the
   assistant.
2. Ask the assistant about the password guidelines: `How often should I
   change my password?`.

   The assistant answers that passwords should be changed every 90 days according
   to the company policy.
3. Click View 1 source below the answer to display the data
   used by the assistant to answer the question.

   In this use case, the PasswordGuidelines.txt file has been
   used to answer the question.

## Updating password guidelines using the tQlikOutput component in the Studio

### Procedure

1. Double-click the tQlikOutput component to display its
   Component view.
2. Enter the URL address of your Qlik Cloud
   account in the Tenant URL field, as well as the API key to
   access it in the API key field.
3. In the Action list, select
   Overwrite, as you want to overwrite the previous
   password policy with a new one.
4. In the Local file field, enter the path to the updated
   password policy file you want to upload in your Qlik Cloud
   account. In this scenario it is called
   PasswordGuidelinesV2.txt.
5. In the Remote file name field, enter the name of the
   existing file as it is displayed in Qlik Cloud. In this scenario it is called PasswordGuidelines.txt.
6. Click … next to the Space field to
   display the available spaces in your Qlik Cloud
   account, and select the space in which the file to be updated is located. In this
   scenario it is called Company policies. 

   After you select the space name from the list, its identifier will be displayed
   in the field.
7. Click … next to the Knowledge base
   field to display the available knowledge bases in your Qlik Cloud
   account, and select the knowledge base that contains the file to be updated. In
   this scenario it is called Company policies KB. 

   After you select the knowledge base name from the list, its identifier will be
   displayed in the field.

## Executing the Job in the Studio and testing the updated knowledge base file on Qlik Cloud

### Procedure

1. In Talend Studio:
   Press Ctrl + S to save your Job, then press
   F6 to execute it.

   The Run console shows that the Job has been executed
   successfully.
2. In Qlik Cloud: Open the assistant again, and check that the
   PasswordGuidelines.txt file in the Company
   policies KB knowledge base has been updated and re-indexed.
3. Open the corresponding assistant again, and ask the same question you previously
   asked: `How often should I change my password?`.

   The assistant takes the updated information into account, and this time it
   answers that passwords should be changed every 60 days.

**Related reference**  

* [tQlikOutput](tqlikoutput "Creates, updates, or deletes data files in Qlik Cloud.")
