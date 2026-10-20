<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ingres/tingresoutputbulkexec · versión 8.0 -->
# tIngresOutputBulkExec

Last updated: 9/30/2026

Inserts data in bulk to a table in the Ingres DBMS for performance
gain.

tIngresOutputBulk and tIngresBulkExec
are generally used together in a two step process. In the first step, an output file is
generated. In the second step, this file is used in the INSERT operation used to feed a
database. These two steps are fused together in the
tIngresOutputBulkExec component.

tIngresOutputBulkExec prepares an output file and uses
it to feed a table in the Ingres DBMS.

Information noteNote:

* This component is available only when you have installed the 8.0.1-R2023-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.
* If you plan to upgrade from an earlier version of Talend Studio
  that has Ingres components, please make sure you apply the 8.0.1-R2023-02 Talend Studio
  Monthly update before starting the upgrade process.

## tIngresOutputBulkExec Standard properties

These properties are used to configure tIngresOutputBulkExec running in the Standard Job framework.

The Standard
tIngresOutputBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Table | Name of the table to be filled. |
| VNode | Name of the virtual node.  The database server must be installed on the same machine where Talend Studio is installed or where the Job using tIngresOutputBulkExec is deployed. |
| Database | Name of the database. |
| Action on table | Actions that can be taken on the table defined:  None: No operation made to the table.  Truncate: Delete all the rows in the table and release the file space back to the operating system. |
| File name | Name of the file to be generated and loaded.  Information noteWarning: This file is generated on the machine specified by the VNode field so it should be on the same machine as the database server. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Delete Working Files After Use | Select this check box to delete the files that are created during the execution. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Field Separator | Character, string or regular expression to separate fields. |
| Row Separator | String (ex: "\n"on Unix) to separate rows |
| On Error | Policy of error handling:  Continue: Continue the execution.  Terminate: Terminate the execution. |
| Reject Row File | Path and name of the file that holds the rejected rows.  Available when Continue is selected from the On Error list. |
| Error Count | Number of errors to trigger the termination of the execution.  Available when Terminate is selected from the On Error list. |
| Rollback | Enable or disable rollback. |
| Null Indicator | Value of the null indicator. |
| Session User | User of the defined session (the connection to the database). |
| Allocation | Number of pages initially allocated to the table or index. |
| Extend | Number of pages by which a table or index grows. |
| Fill Factor | Specify the percentage (from 1 to 100) of each primary data page that must be filled with rows, under ideal conditions. For example, if you specify a fillfactor of 40, the DBMS Server fills 40% of each of the primary data pages in the restructured table with rows. |
| Min Pages/Max Pages | Specify the minimum/maximum number of primary pages a hash table must have. The Min. pages and Max. pages must be at least 1. |
| Leaf Fill | A bulk copy from can specify a leaffill value. This clause specifies the percentage (from 1 to 100) of each B-tree leaf page that must be filled with rows during the copy. This clause can be used only on tables with a B-tree storage structure. |
| Non Leaf Fill | A bulk copy from can specify a nonleaffill value. This clause specifies the percentage (from 1 to 100) of each B-tree non-leaf index page that must be filled with rows during the copy. This clause can be used only on tables with a B-tree storage structure. |
| Row Estimate | Specify the estimated number of rows to be copied from a file to a table during a bulk copy operation. |
| Trailing WhiteSpace | Selected by default, this check box is designed to trim the trailing white spaces and applies only to such data types as VARCHAR, NVARCHAR and TEXT. |
| Output | Where to output the error message:  to console: Message output to the console.  to global variable: Message output to the global variable. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Usually deployed along with tIngresConnection or tIngresRow, tIngresOutputBulkExec prepares an output file and feeds its data in bulk to the Ingres DBMS for performance gain. |
| Limitation | The database server/client must be installed on the same machine where Talend Studio is installed or where the Job using tIngresOutputBulkExec is deployed, so that the component functions properly.  Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Loading data to a table in the Ingres DBMS](tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-loading-data-to-table-in-ingres-dbms-standard-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ingres/tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-loading-data-to-table-in-ingres-dbms-standard-component-in-this -->
# Loading data to a table in the Ingres DBMS

Last updated: 9/30/2026

In this scenario, a tIngresOutputBulkExec
component is deployed to prepare an output file with the employee data from a .csv file and
then use that output file to feed a table in an Ingres database.

### In this section

* [Dragging and dropping components](/talend/en-US/components/8.0/ingres/tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-dragging-and-dropping-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/ingres/tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/ingres/tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-executing-job-standard-component-press)

**Related reference**  

* [tIngresOutputBulkExec](tingresoutputbulkexec "Inserts data in bulk to a table in the Ingres DBMS for performance gain.")
* [tIngresConnection](tingresconnection "Opens a connection to the specified database that can then be reused in the subsequent subJob or subJobs.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ingres/tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tIngresConnection to open
   its Basic settings view in the Component tab.
2. In the Server field, enter the address of
   the server where the Ingres DBMS resides, for example *"localhost"*.

   Keep the default settings of the Port
   field.
3. In the Database field, enter the name of
   the Ingres database, for example *"research"*.
4. In the Username and Password fields, enter the authentication
   credentials.

   A context variable is used for the password here. For more information on context
   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).
5. Double-click tFileInputDelimited to open
   its Basic settings view in the Component tab.
6. Select the source file by clicking the [...] button next to the File
   name/Stream field.
7. Click the [...] button next to the
   Edit schema field to open the schema
   editor.
8. Click the [+] button to add four columns,
   for example *name*, *age*,
   *job* and *dept*, with the data
   type as *string*, *Integer*, *string* and
   *string* respectively.

   Click OK to close the schema
   editor.

   Click Yes on the pop-up window that asks
   whether to propagate the changes to the subsequent component.

   Leave other default settings unchanged.
9. Double-click tIngresOutputBulkExec to
   open its Basic settings view in the
   Component tab.
10. In the Table field, enter the name of the
    table for data insertion.
11. In the VNode and Database fields, enter the names of the VNode and the
    database.
12. In the File Name field, enter the full
    path of the file that will hold the data of the source file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ingres/tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-dragging-and-dropping-components-standard-component-drop -->
# Dragging and dropping components

Last updated: 9/30/2026

## Procedure

1. Drop tIngresConnection, tFileInputDelimited and tIngresOutputBulkExec from the Palette onto the workspace.
2. Rename tIngresOutputBulkExec as save\_a\_copy\_and\_load\_to\_DB.
3. Link tIngresConnection to tFileInputDelimited using an OnSubjobOk trigger.
4. Link tFileInputDelimited to tIngresOutputBulkExec using a Row > Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ingres/tingresoutputbulkexec-tingresconnection-tfileinputdelimited-tingresconnection-tfileinputdelimited-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.

   As shown above, the employee data is written to the table *employee* in the database *research* on the node *talendbj*. Meanwhile, the output file *employee\_research.csv* has been generated at *C:/Users/talend/Desktop*.
