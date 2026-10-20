<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marklogic/tmarklogicoutput · versión 8.0 -->
# tMarkLogicOutput

Last updated: 9/30/2026

Creates, updates or deletes document content in a MarkLogic database.

tMarkLogicOutput allows you to maintain document content in a MarkLogic
database according to the predefined operation and the input flow from the preceding
component.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMarkLogicOutput Standard properties

These properties are used to configure tMarkLogicOutput running in the Standard Job framework.

The Standard
tMarkLogicOutput component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data   stored centrally. * Repository: Select the   repository file in which the properties are stored. The database   connection fields that follow are completed automatically using   the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the IP address or hostname of the MarkLogic server. |
| Port | Enter the listening port number of the MarkLogic server. |
| Database | Enter the name of the MarkLogic database you want to use. |
| Username and Password | Enter the user authentication data to access the MarkLogic database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Authentication | Select an authentication type from the list, either DIGEST or BASIC. For more information about the types of authentication, see <http://docs.marklogic.com/guide/security/authentication#id_56266>. |
| Action | Select an operation to be performed:   * UPSERT: create documents if they do not exist or   update the content of existing documents. * PATCH: perform a partial update to the content of the   documents. * DELETE: delete documents   corresponding to the input flow.   Note that when DELETE is selected from the Action list, the input schema should contain one column docId that describes the URI of the documents to be deleted, and other columns will be ignored if there is any. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is read-only. You can click the [...] button next to Edit schema to view the predefined schema that contains the following two columns:  * docId: the URI of the   document. * docContent: the content   of the document. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Doc Type | Select the type of the documents to be processed: MIXED, PLAIN TEXT, JSON, XML, or BINARY. |
| Auto Generate Doc ID | Select this check box to generate automatically the document URIs and in the Doc Id Prefix field displayed enter the prefix used to construct the document URIs.  This check box is available only when UPSERT is selected from the Action list and MIXED is not selected from the Doc Type list.   * If this check box is selected, the input schema should contain   one column docContent that   describes the document content, and other columns will be   ignored if there is any. * If this check box is clear, the input schema should contain two columns docId and docContent that describe the document URI and   the document content correspondingly. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an end component and it always needs an input flow. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
