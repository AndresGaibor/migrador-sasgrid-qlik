<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapattributesinput · versión 8.0 -->
# tLDAPAttributesInput

Last updated: 9/30/2026

Analyses each object found via the LDAP query and lists a collection of attributes
associated with the object.

tLDAPAttributesInput executes an LDAP query based
on the given filter and corresponding to the schema definition. Then it passes on the
field list to the next component via a Main row
link.

## tLDAPAttributesInput Standard properties

These properties are used to configure tLDAPAttributesInput running in the Standard Job framework.

The Standard
tLDAPAttributesInput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and click the relevant tLDAPConnection component on the Component list to reuse the connection details you already defined. |
| Host | LDAP Directory server IP address. |
| Port | Listening port number of server. |
| Base DN | Path to user's authorised tree leaf. |
| Protocol | Select the protocol type on the list.  LDAP : no encryption is used  LDAPS: secured LDAP. When this option is chosen, the Advanced CA check box appears. Once selected, the advanced mode allows you to specify the directory and the keystore password of the certificate file for storing a specific CA. However, you can still deactivate this certificate validation by selecting the Trust all certs check box.  TLS: certificate is used. When this option is chosen, the Advanced CA check box appears and is used the same way as that of the LDAPS type. |
| Authentication User and Password | Select the Authentication check box if LDAP login is required. Note that the login must match the LDAP syntax requirement to be valid. e.g.: "cn=Directory Manager".  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Filter | Type in the filter as expected by the LDAP directory db. |
| Multi valued field separator | Type in the value separator in multi-value fields. |
| Alias dereferencing | Select the option on the list. Never improves search performance if you are sure that no alias is to be dereferenced. By default, Always is to be used:  Always: Always dereference aliases  Never: Never dereferences aliases.  Searching:Dereferences aliases only after name resolution.  Finding: Dereferences aliases only during name resolution |
| Referral handling | Select the option on the list:  Ignore: does not handle request redirections  Follow:does handle request redirections |
| Limit | Fill in a limit number of records to be read If needed. |
| Time Limit | Fill in a timeout period for the directory. access |
| Paging | Specify the number of entries returned at a time by the LDAP server. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row > Rejects link. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).  Information noteWarning: *As this component is intended to list the attributes   associated with a LDAP object, its schema is then   pre-defined. You should retain these established columns,   even though you may need to add some new columns. Hence you   should use the Built-in mode.* * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * The pre-defined schema lists:  - *objectclass*: list of object classes  - *mandatoryattributes*: list of mandatory   attributes to these classes  - *optionalattributes*: list of optional   attributes to these classes  - *objectattribute*s: list of attributes that   are essential for the analysed object. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Class Definition Root | Specify the root of the object class definition namespace. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  RESULT\_NAME: the name of the current LDAP entry satisfying the search filter. This is a flow variable, and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible LDAP queries.  Note: Press Ctrl + Space bar to access the global variable list, including the GetResultName variable to retrieve automatically the relevant Base |
