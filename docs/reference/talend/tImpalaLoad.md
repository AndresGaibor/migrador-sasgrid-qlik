<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/impala/timpalaload · versión 8.0 -->
# tImpalaLoad

Last updated: 9/30/2026

Writes data of different formats into a given Impala table or to export data from
an Impala table to a directory.

tImpalaLoad connects to a given Impala database and
copies or moves data into an existing Impala table or a directory you specify.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tImpalaLoad Standard properties

These properties are used to configure tImpalaLoad running in the Standard Job framework.

The Standard
tImpalaLoad component belongs to the Big Data family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Impala Driver | Select the driver you are using from the drop-down list. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Fill this field with the name of the database. |
| Additional JDBC Settings | Specify additional connection properties for the database connection you are creating.  This option is not available if you have selected the Use an existing connection check box in the Basic settings view. |
| Username and Password | Enter the database user authentication data to authenticate using LDAP.  To enter the password, click the […] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  These parameters are not available when you select the Use kerberos authentication check box. |
| Use kerberos authentication | If you are accessing an Impala system running with Kerberos security, select this checkbox and then enter the Kerberos principal of this Impala system. |
| Load action | Select the action you need to carry for writing data into the specified destination.   * When you select LOAD, you are moving or copying data from   a directory you specify. Information noteNote: With Cloudera Data Platform (CDP), if you   load a table, the table must be non-ACID to work correctly. * When you select INSERT,   you are moving or copying data based on queries. |
| Target type | This drop-down list appears only when you have selected INSERT from the Load action list.  Select from this list the type of the location you need to write data in.   * If you select Table as destination, you can still   choose to append data to or overwrite the contents in the   specified table. This is the only option in the current   release. |
| Action | Select whether you want to OVERWRITE the old data already existing in the destination or only APPEND the new data to the existing one. |
| Table name | Enter the name of the Hive table you need to write data in.  Note that with the INSERT action, this field is available only when you have selected Table from the Target type list. |
| File path | Enter the directory you need to read data from. |
| Query | This field appears when you have selected INSERT from the Load action list.  Enter the appropriate query for selecting the data to be exported to the specified Impala table or directory. |
| Set partitions | Select this check box to use the Impala Partition clause in loading or inserting data in a Impala table. You need to enter the partition keys and their values to be used in the field that appears.  For example, enter *contry='US', state='CA'*. This makes a partition clause reading Partition (contry='US', state='CA'), that is to say, a *US and CA* partition.  Also, it is recommended to select the Create partition if not exist check box that appears to ensure that you will not create a duplicate partition. |
| Die on error | Select this check box to kill the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component works standalone. |
