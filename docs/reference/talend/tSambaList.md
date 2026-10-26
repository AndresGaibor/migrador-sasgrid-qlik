<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/samba/tsambalist · versión 8.0 -->
# tSambaList

Last updated: 9/30/2026

Lists files in a directory under a shared directory and passes the file information
to the subsequent component. This component supports Samba version 2 and Samba version
3.

## tSambaList Standard properties

These properties are used to configure tSambaList running in the
Standard Job framework.

The Standard
tSambaList component belongs to the Internet
family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This option is not available when you select the Use an existing connection option and select a component from the Component List dropdown list. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Guess schema | Click this button to generate the schema using the following columns.   * FileName, type String * FileName\_with\_Path, type   String * Length, type Long * Change\_Time, type Date * Creation\_Time, type Date * Last\_Access\_Time, type Date * Last\_Write\_Time, type Date |
| Host | The IP address or hostname of the Samba host.  This field is not available if you select the Use an existing connection option. |
| Username and Password | Enter the authentication information required to access the Samba host.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only.  These two fields are not available if you select the Use an existing connection option. |
| Domain | Enter the Samba host domain name.  This field is not available if you select the Use an existing connection option. |
| Share directory | Enter the share name of the shared directory where the desired directory resides. The shared directory will be the parent directory of the desired directory. |
| Remote path | Enter the relative path to the directory whose files will be listed. |
| Includes subdirectories | Select this option to also list the files under all the subdirectories of the directory specified by the Remote path field. |
| File mask | Add a line by clicking the plus button on the bottom and type in a file mask in the line to filter the files to be listed.  You can enter multiple file masks by adding a line for each of the file masks. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component passes file information to the subsequent component through a Row > Main connection. It can also be used to trigger other components or subJobs. |
