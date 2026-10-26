<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/samba/tsambaoutput · versión 8.0 -->
# tSambaOutput

Last updated: 9/30/2026

Creates a file in a directory under a shared directory and writes data to the file.
If the file already exists, this component overwrites the file. This component supports
Samba version 2 and Samba version 3.

## tSambaOutput Standard properties

These properties are used to configure tSambaOutput running in the Standard Job framework.

The Standard
tSambaOutput component belongs to the Internet family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0 R2022-02 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This option is not available when you select the Use an existing connection option and select a component from the Component List dropdown list. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Host | The IP address or hostname of the Samba host.  This field is not available if you select the Use an existing connection option. |
| Username and Password | Enter the authentication information required to access the Samba host.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only.  These two fields are not available if you select the Use an existing connection option. |
| Domain | Enter the Samba host domain name.  This field is not available if you select the Use an existing connection option. |
| Share directory | Enter the share name of the shared directory where the desired file resides. The shared directory will be the parent directory of the remote file. |
| Remote file | Enter the relative path to the file to write data to. If the file already exists, it will be overwritten. |
| File type | Select the file type, JSON or CSV. |
| Line separator type | Select the line separator: Windows type, Linux type, or Other. If you select Other, specify the line separator in the Line separator string field.  This option is available if you select CSV from the File type drop-down list. |
| Encoding type | Select the encoding type from the drop-down list: UTF 8, ISO-8859-15 or Other.  If you select Other, specify the encoding in the Custom encoding field.  This option is available if you select CSV from the File type drop-down list. |
| Set header | Select this option to treat the beginning lines as the header. You can specify the number of lines that will be treated as the header in the Number of lines field.  This option is available if you select CSV from the File type drop-down list. |
| Field separator type | Select the field separator from the drop-down list.  If you select Other, enter the character that will be treated as the separator in the Field separator field.  This option is available if you select CSV from the File type drop-down list.  Information noteNote: Currently, `Space` cannot be used as the field separator. |
| Create directory | Select this option to create the directories specified in the Remote file field before writing data to the file if the directories do not exist. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Max batch size | Specify the maximum number of lines that can be written in a batch. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to write a CSV or a JSON file using Samba v2 or v3 and separate fields using a field separator value. |
