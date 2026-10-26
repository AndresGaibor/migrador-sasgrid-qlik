<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/box/tboxv2list · versión 8.0 -->
# tBoxv2List

Last updated: 9/30/2026

Lists the information about the files and/or folders in a specified folder in
Box.

This component lists the metadata and the contents of the files and/or the folders in a Box
folder.

## tBoxv2List Standard properties

These properties are used to configure tBoxv2List running in the
Standard Job framework.

The Standard
tBoxv2List component belongs to the Cloud
family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0.1-R2023-04 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository.   * Built-in: No property data is   stored centrally. * Repository: Select the repository   file where properties are stored. The fields that follow are   completed automatically using the fetched data.   This drop-down list is not available if you select the Use an existing connection option. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Authentication type | Select the authentication type: JWT (short for JSON Web Token) or Developer token.  You need to provide the following parameters in the corresponding fields for the JWT authentication type.  * Client ID and Client secret: Enter   the client key and client secret required by Box to access the Box API. To obtain   the client key and client secret, you need to create an account at <https://developers.box.com/> and then create a Box App under the Box   account to be used. The client key and client secret can be obtained from the   account application settings. * Public key ID * Private key * Private key passphrase * Enterprise ID or User ID  For more information about JWT authentication, see [JWT Auth](https://developer.box.com/guides/authentication/jwt/).  Information noteNote: To enter the client secret, private key, or private key passphrase, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the key in the text field, and click OK. Note that you can enter the key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  If you select Developer token from the drop-down list, type in the developer token in the Developer token field. For more information about developer token, see [Developer Tokens](https://developer.box.com/guides/authentication/tokens/developer-tokens/).  The Authentication type drop-down list is available when Use an existing connection is not selected. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| Box remote path | Type in the Box path. The information about the files and the folders under the Box path will be listed.  You can also specify the Box path by clicking the [...] button next to this field and navigating to the folder.  This option is available when the Get folder by ID option in the Advanced settings view is not selected. |
| Box ID | Type in the Box ID of the folder whose file information is to be listed.  You can also specify the Box ID by clicking the [...] button next to this field and navigating to the folder.  This option is available when the Get folder by ID option in the Advanced settings view is selected. |
| List type | Select the type of the objects whose information is to be listed: Files, Folders, or Both. |
| Include subfolders | Select this option to also list the information about the objects in the subfolders of the specified Box folder. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Fetch more information | Select this option to retrieve more detailed information about the objects in the specified folder. This is achieved by adding extra columns in the schema. If this option is not selected, the schema generated after you click the Guess schema button contains these four columns: ID, NAME, RELATIVE\_PATH, and TYPE; with this option selected, the schema generated contains these columns: ID, NAME, RELATIVE\_PATH, ABSOLUTE\_PATH, LAST\_MODIFIED, MODIFIED\_BY, and SIZE. |
| Get folder by ID | Select this option to specify the folder using its Box ID. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used alone or along with other components via the Iterate link or a trigger link such as OnSubjobOk. |
