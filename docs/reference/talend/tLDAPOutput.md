<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapoutput · versión 8.0 -->
# tLDAPOutput

Last updated: 9/30/2026

Executes an LDAP query based on the given filter and corresponding to the schema
definition. Then it passes on the field list to the next component via a Row > Main link.

## tLDAPOutput Standard properties

These properties are used to configure tLDAPOutput running in the Standard Job framework.

The Standard
tLDAPOutput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Host | LDAP Directory server IP address. |
| Port | Listening port number of server. |
| Base DN | Path to user's authorized tree leaf. |
| Protocol | Select the protocol type on the list.  LDAP : no encryption is used  LDAPS: secured LDAP. When this option is chosen, the Advanced CA check box appears. Once selected, the advanced mode allows you to specify the directory and the keystore password of the certificate file for storing a specific CA. However, you can still deactivate this certificate validation by selecting the Trust all certs check box.  TLS: certificate is used When this option is chosen, the Advanced CA check box appears and is used the same way as that of the LDAPS type. |
| User and Password | Fill in the User and Password as required by the directory  Note that the login must match the LDAP syntax requirement to be valid. e.g.: "cn=Directory Manager".  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Multi valued field separator | Type in the value separator in multi-value fields. |
| Alias dereferencing | Select the option on the list. Never improves search performance if you are sure that no aliases is to be dereferenced. By default, Always is to be used:  Always: Always dereference aliases  Never: Never dereferences aliases.  Searching:Dereferences aliases only after name resolution.  Finding: Dereferences aliases only during name resolution |
| Referral handling | Select the option on the list:  Ignore: does not handle request redirections  Follow:does handle request redirections |
| Insert mode | Select the editing mode on the list:  Add: add a value in a multi-value attribute,  Insert: insert new data,  Update: updates the existing data,  Delete: remove the selected data from the directory,  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made.  Information noteWarning: When Update is selected, you must go to the Advanced settings view, and select the Use Attribute Options (for update mode) check box to show the Attribute Options table. Then, select the attribute to update under the Attribute name part and the choose Replace under the Option part. |
| DN Column Name | Select in the list the type of the LDAP input entity used. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use Attribute Options (for update mode) | Select this check box to choose the desired attribute (including dn, dc, ou, objectClass, mail and uid) and the corresponding operation (including Add, Replace, Remove Attribute and Remove Value). |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible LDAP queries.  Note: Press Ctrl + Space bar to access the global variable list, including the GetResultName variable to retrieve the relevant DN Base automatically. This component allows you to carry out actions on a table or on the data of a table in an database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For an example of tMysqlOutput in use, see [Retrieving data in error with a Reject link](/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this). |

**Related concepts**  

* [Editing data in a LDAP directory](tldapinput-tldapoutput-tmap-tlogrow-editing-data-in-ldap-directory-standard-component-all-of)
