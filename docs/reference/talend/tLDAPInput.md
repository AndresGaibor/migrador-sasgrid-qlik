<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput · versión 8.0 -->
# tLDAPInput

Last updated: 9/30/2026

Executes an LDAP query based on the given filter and corresponding to the schema
definition. Then it passes on the field list to the next component via a Row > Main link.

## tLDAPInput Standard properties

These properties are used to configure tLDAPInput running in the Standard Job framework.

The Standard
tLDAPInput component belongs to the Databases family.

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
| Base DN | Path to the user's authorized tree leaf.  Information noteNote: To retrieve the full DN information, enter a field named *DN* in the schema, in either upper case or lower case. |
| Protocol | Select the protocol type on the list.  LDAP : no encryption is used  LDAPS: secured LDAP. When this option is chosen, the Advanced CA check box appears. Once selected, the advanced mode allows you to specify the directory and the keystore password of the certificate file for storing a specific CA. However, you can still deactivate this certificate validation by selecting the Trust all certs check box.  TLS: certificate is used When this option is chosen, the Advanced CA check box appears and is used the same way as that of the LDAPS type. |
| Authentication User and Password | Select the Authentication check box if LDAP login is required. Note that the login must match the LDAP syntax requirement to be valid. e.g.: "cn=Directory Manager".  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Filter | Type in the filter as expected by the LDAP directory db. |
| Multi valued field separator | Type in the value separator in multi-value fields. |
| Alias dereferencing | Select the option on the list. Never improves search performance if you are sure that no alias is to be dereferenced. By default, Always is to be used:  Always: Always dereference aliases  Never: Never dereferences aliases.  Searching:Dereferences aliases only after name resolution.  Finding: Dereferences aliases only during name resolution |
| Referral handling | Select the option on the list:  Ignore: does not handle request redirections  Follow:does handle request redirections |
| Limit | Fill in a limit number of records to be read If needed. |
| Time Limit | Fill in a timeout period for the directory. access |
| Paging | Specify the number of entries returned at a time by the LDAP server. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row > Rejects link. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables.  Information noteWarning: Only three data types are supported here: String, byte[], and   List. tMap can be used for data   type conversion if needed. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use field options (for binary setting) | Select this check box to specify the binary-encoded columns. |
| Field options | This option is available when Use field options (for binary setting) is selected. Select the Binary check box for the columns you want to be binary-encoded. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  RESULT\_NAME: the name of the current LDAP entry satisfying the search filter. This is a flow variable, and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible LDAP queries.  Note: Press Ctrl + Space bar to access the global variable list, including the GetResultName variable to retrieve automatically the relevant Base. |

**Related concepts**  

* [Displaying LDAP directory's filtered content](tldapinput-tlogrow-displaying-ldap-directory-s-filtered-content-the-job)
* [Editing data in a LDAP directory](tldapinput-tldapoutput-tmap-tlogrow-editing-data-in-ldap-directory-standard-component-all-of)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput-tldapoutput-tmap-tlogrow-editing-data-in-ldap-directory-standard-component-all-of -->
# Editing data in a LDAP directory

Last updated: 9/30/2026

Information noteNote:

All of the database output components have the Parallelize option in their Advanced
settings tab. This option allows you to improve data processing
performances by handling several data flows simultaneously. For more information, see
[Writing data in parallel](/talend/r/en-US/8.0/studio-user-guide/writing-data-in-parallel).

The following scenario describes a Job that reads an LDAP directory, updates
the email of a selected entry and displays the output before writing the LDAP directory. To
keep it simple, no alias dereferencing nor referral handling is performed. This scenario is
based on [Displaying LDAP directory's filtered content](/talend/en-US/components/8.0/ldap/tldapinput-tlogrow-displaying-ldap-directory-s-filtered-content-the-job). The result returned was a single entry, related to an organisational person, whom email
is to be updated.

The output shows the following fields: *dn*, *uid* and *mail* as defined in the Job.

### In this section

* [Dropping the components](/talend/en-US/components/8.0/ldap/tldapinput-tldapoutput-tmap-tlogrow-dropping-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/ldap/tldapinput-tldapoutput-tmap-tlogrow-configuring-components-standard-component-in)
* [Executing the Job](/talend/en-US/components/8.0/ldap/tldapinput-tldapoutput-tmap-tlogrow-executing-job-standard-component-press)

**Related reference**  

* [tLDAPInput](tldapinput "Executes an LDAP query based on the given filter and corresponding to the schema definition. Then it passes on the field list to the next component via a Row > Main link.")
* [tLDAPOutput](tldapoutput "Executes an LDAP query based on the given filter and corresponding to the schema definition. Then it passes on the field list to the next component via a Row > Main link.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput-tlogrow-displaying-ldap-directory-s-filtered-content-the-job -->
# Displaying LDAP directory's filtered content

Last updated: 9/30/2026

The Job described below simply filters the LDAP directory and displays the result on the
console.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/ldap/tldapinput-tlogrow-adding-and-linking-components-drop)
* [Configuring the components](/talend/en-US/components/8.0/ldap/tldapinput-tlogrow-configuring-components-set)

**Related reference**  

* [tLDAPInput](tldapinput "Executes an LDAP query based on the given filter and corresponding to the schema definition. Then it passes on the field list to the next component via a Row > Main link.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput-tldapoutput-tmap-tlogrow-configuring-components-standard-component-in -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. In the tLDAPInput
   Component view, set the connection details
   to the LDAP directory server as well as the filter as described in [Displaying LDAP directory's filtered content](/talend/en-US/components/8.0/ldap/tldapinput-tlogrow-displaying-ldap-directory-s-filtered-content-the-job).

   Change the schema to make it simpler, by removing the unused fields:
   *dc*, *ou*,
   *objectclass*.
2. Then open the mapper to set the edit to be carried out.

   Drag & drop the uid column from the input table to the output as no
   change is required on this column.
3. In the Expression field of the
   *dn* column (output), fill in with the exact
   expression expected by the LDAP server to reach the target tree leaf and
   allow directory writing only if you haven't set it already in
   the Base DN field of the tLDAPOutput component.
4. In this use case, the GetResultName
   global variable is used to retrieve this path automatically. Press Ctrl+Space bar to access the variable list and
   select tLDAPInput\_1\_RESULT\_NAME.
5. In the *mail* column's expression field, type in the
   new email that will overwrite the current data in the LDAP directory. In
   this example, we change to
   *Pierre.Dupont@talend.com*.

   Click OK to validate the changes.
6. Then select the tLDAPOutput component to
   set the directory writing properties.
7. Set the Port and Host details manually if they aren't stored in the Repository.
8. In Base DN field, set the highest tree
   leaf you have the rights to access. If you have not set previously the exact
   and full path of the target DN you want to access, then fill in it here. In
   this use case, the full DN is provided by the *dn* output
   from the tMap component, therefore only the
   highest accessible leaf is given:
   *o=directoryRoot*.
9. Select the relevant protocol to be used: LDAP for this example.

   Fill in the User and Password as expected by the LDAP
   directory.

   Fill in Multi-valued field separator with
   a comma as some fields may hold more than one value, separated by a comma.
10. Use the default setting of Alias
    Dereferencing and Referral
    Handling fields, respectively Always and Ignore.

    The Insert mode for this use case is
    Update (the email address).

    The schema was provided by the previous component through the propagation
    operation.
11. In the Advanced settings view, select the
    Use Attribute Options (for update mode)
    check box to show the Attribute Options
    table. 

    Select the attribute mail under the
    Attribute Name part and the choose
    Replace under the Option part.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput-tldapoutput-tmap-tlogrow-dropping-components-standard-component-drop -->
# Dropping the components

Last updated: 9/30/2026

## Procedure

1. Drop the tLDAPInput, tLDAPOutput, tMap and tLogRow components
   from the Palette to the design
   workspace.
2. Link tLDAPInput to tMap using the Row >
   Main connection.
3. Link tMap to tLogRow using the Row >
   Main connection.
4. Link tLogRow to tLDAPOutput using the Row >
   Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput-tldapoutput-tmap-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput-tlogrow-adding-and-linking-components-drop -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

Drop the tLDAPInput component along with
a tLogRow from the Palette to the design workspace.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapinput-tlogrow-configuring-components-set -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Set the tLDAPInput properties.
2. Set the Property type on
   Repository if you stored the LDAP connection details in
   the Metadata Manager in the
   Repository. Then select the relevant entry on the
   list.
3. In Built-In mode, fill in the Host and Port
   information manually. Host can be the IP address of the LDAP directory server or
   its DNS name.
4. No particular Base DN is to be set.
5. Then select the relevant Protocol on the
   list. In this example: a simple LDAP
   protocol is used.
6. Select the Authentication check box and
   fill in the login information if required to read the directory. In this use
   case, no authentication is needed.
7. In the Filter area, type in the command,
   the data selection is based on. In this example, the filter is: (&(objectClass=inetorgperson)&(uid=PIERRE
   DUPONT)).
8. Fill in Multi-valued field separator
   with a comma as some fields may hold more than one value, separated
   by a comma.
9. As we do not know if some aliases are used in the LDAP directory, select
   Always on the list.
10. Set Ignore as Referral handling.
11. Set the limit to 100 for this use
    case.
12. Set the Schema as required by your LDAP
    directory. In this example, the schema is made of 6 columns including the
    objectClass and 
    uid
    columns which get filtered on.
13. In the tLogRow component, no particular
    setting is required.

## Results

Only one entry of the directory corresponds to the filter criteria
given in the tLDAPInput component.

For an example of the use of dynamic
schemas in Input components, see [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).
