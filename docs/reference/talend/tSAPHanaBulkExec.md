<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsaphanabulkexec · versión 8.0 -->
# tSAPHanaBulkExec

Last updated: 9/30/2026

Improves performance while carrying out the Insert operations to an SAP HANA
database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSAPHanaBulkExec Standard Properties

These properties are used to configure tSAPHanaBulkExec running in
the Standard Job framework.

The Standard
tSAPHanaBulkExec component belongs to the Databases family.

If you have installed the 8.0.1-R2023-01 Talend Studio Monthly
update or a later one delivered by Talend, this
component is available in all Talend
subscription-based products; otherwise it is only available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Select either of the following:  * Built-in: No property stored centrally * Repository: Select the repository file in which the   properties are stored. The fields that follow are completed automatically using the   data retrieved |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Add the database server IP address. |
| Port | Add the listening port number of DB server. |
| Schema | Add the table name of the database. |
| Username and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Enter the name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | On the table defined, you can perform one of the following operations:  * None: No operation is carried out. * Drop and create table * Create table: The table does not exist   and gets created. * Create table if not exists: The table is   created if it does not exist. * Drop table if exists and create: The   table is removed if it already exists and created again. * Clear table: The table content is   deleted. You have the possibility to rollback the operation. * Truncate table: The table content is   deleted. You do not have the possibility to rollback the operation. |
| Type of table storage | This option is only available if you create (with or without drop) the database table. This option allows you to define the way the data is stored in the table. The following types of table storage organization are available:  * Row: Data is stored in rows. It   is preferable to use this table type if the majority of table access   involves selecting a few records. With all attributes selected, the   table is removed and created again. * Column: Data is stored in columns. It is   preferable to use this table type if the majority of table access will be   through a large number of tuples, with only a few selected attributes. * History column: Creates a table with a   particular transaction session type called *HISTORY*.   Tables with session type *HISTORY*: The table is support time travel   queries. For more information on *HISTORY* and time travel   queries, see <http://help.sap.com/saphelp_hanaplatform/helpdata/en/20/d56cd075191014b7ea9e4e77477aae/content.htm>. |
| Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| CSV file on the SAP HANA host | Specify the name of the CSV file on the SAP HANA host. |
| Lines terminated by | Specify the character or sequence of characters used to separate lines. |
| Fields terminated by | Specify the character, string or regular expression to separate fields. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| Error log file name | Enter the file path of the log file. |
| Number of rows to skip | Define the specific number of rows in the import file to skip. |
| Date format | Enter the format of the date strings that are encoded in the import data. You can enter the following values:  * Y: year * MM: month * MON: name of the month * DD: day |
| Time format | Enter the format of the timestamp strings that are encoded in the import data. |
| Thread size | Specify the number of threads used for concurrent import. |
| Batch size | Define the number of records to be inserted in a commit. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | Use this component to increase the performance of loading data to an SAP HANA database. |
| **Support** | tSAPHanaBulkExec should be used to interact with the ERP part of SAP, including S4/HANA. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
