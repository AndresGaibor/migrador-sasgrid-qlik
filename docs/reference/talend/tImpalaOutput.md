<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/impala/timpalaoutput · versión 8.0 -->
# tImpalaOutput

Last updated: 9/30/2026

Executes the action defined on the data contained in the table, based on the flow
incoming from the preceding component in the Job.

tImpalaOutput connects to an Impala database (the Impala
data warehouse system) and writes data in an Impala table.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tImpalaOutput Standard properties

These properties are used to configure tImpalaOutput running in the Standard Job framework.

The Standard
tImpalaOutput component belongs to the Big Data family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository : Select the   repository file in which the properties are stored. The fields that   follow are completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Impala Driver | Select the driver you are using from the drop-down list. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Fill this field with the name of the database. |
| Additional JDBC Settings | Specify additional connection properties for the database connection you are creating.  This option is not available if you have selected the Use an existing connection check box in the Basic settings view. |
| Username and Password | Enter the database user authentication data to authenticate using LDAP.  To enter the password, click the […] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  These parameters are not available when you select the Use kerberos authentication check box. |
| Use kerberos authentication | If you are accessing an Impala system running with Kerberos security, select this checkbox and then enter the Kerberos principal of this Impala system. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Table Name | Name of the table you need to write data in. |
| Action | Select whether you want to OVERWRITE the old data already existing in the destination or only APPEND the new data to the existing one. |
| Extended insert | Select this check box to combine multiple rows of data into one single INSERT action. This can speed up the insert operation. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the benefit of flexible DB queries and covers all possible Impala SQL queries. |
