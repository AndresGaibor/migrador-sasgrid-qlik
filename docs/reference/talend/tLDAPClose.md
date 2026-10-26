<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapclose · versión 8.0 -->
# tLDAPClose

Last updated: 9/30/2026

Disconnects one connection to the LDAP Directory server so as to release occupied
resources.

## tLDAPClose Standard properties

These properties are used to configure tLDAPClose running in the Standard Job framework.

The Standard
tLDAPClose component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Component list | Select the tLDAPConnection component in the list if more than one connection is planned for the current Job. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStat Catcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is to be used along with other LDAP components, especially with tLDAPConnection. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
