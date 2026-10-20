<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdcoutput · versión 8.0 -->
# tOracleCDCOutput

Last updated: 9/30/2026

Synchronizes data changes in the Oracle XStream CDC mode.

This component replicates data changes from an XStream inbound server to a target table
using CDC.

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tOracleCDCOutput Standard properties

These properties are used to configure tOracleCDCOutput running in the Standard Job framework.

The Standard
tOracleCDCOutput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property of the CDC connection | * Either Built-in or Repository. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Make sure that the connection selected is not of the WALLET type to prevent possible errors.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| DB Version | Select the version of the Oracle database being used. |
| Local Service Name | Specify the local service name of the Oracle database. |
| Oracle schema | Specify the name of the Oracle schema. |
| Username and Password | Specify the user authentication data of the Oracle database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Input field | Select an input field from the drop-down list. |
| Inbound server name | Specify the XStream inbound server name. |
| Set data table schema | Select this check box to specify the schema of the CDC table. |
| Set target table | Select this check box to specify the table to which data changes from the inbound server will be replicated. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Acknowledge interval(seconds) | Specify the value for the OCI\_ATTR\_XSTREAM\_ACK\_INTERVAL attribute for the inbound server. The default value is *30* seconds.  For more information about this attribute, see <http://docs.oracle.com/cd/E18283_01/server.112/e16545/xstrm_oci_intro.htm#CEGDICBB>. |
| tStatCatcher Statistics | Select this check box to collect the log data at component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an output component. It requires an input component and Row > Main link as input. |

**Related concepts**  

* [Extracting and synchronizing data changes using XStream mode](toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-extracting-and-synchronizing-data-changes-using-xstream-mode-standard-component-enterprise-this)
