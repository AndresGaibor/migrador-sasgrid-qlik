<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ingres/tingresbulkexec · versión 8.0 -->
# tIngresBulkExec

Last updated: 9/30/2026

Inserts data in bulk to a table in the Ingres DBMS for performance
gain.

tIngresOutputBulk and tIngresBulkExec
are generally used together in a two step process. In the first step, an output file is
generated. In the second step, this file is used in the INSERT operation used to feed a
database. These two steps are fused together in the
tIngresOutputBulkExec component. The advantage of using two
components is that data can be transformed before it is loaded in the database.

Information noteNote:

* This component is available only when you have installed the 8.0.1-R2023-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.
* If you plan to upgrade from an earlier version of Talend Studio
  that has Ingres components, please make sure you apply the 8.0.1-R2023-02 Talend Studio
  Monthly update before starting the upgrade process.

## tIngresBulkExec Standard properties

These properties are used to configure tIngresBulkExec running in the Standard Job framework.

The Standard
tIngresBulkExec component belongs to the Databases family.

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
| VNode | Name of the virtual node. |
| Database | Name of the database. |
| Action on table | Actions that can be taken on the table defined:  None: No operation made to the table.  Truncate: Delete all the rows in the table and release the file space back to the operating system. |
| File name | Name of the file to be loaded.  Information noteWarning: This file should be located on the same machine as the database server. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Delete Working Files After Use | Select this check box to delete the files that are created during the execution. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Field Separator | Character, string or regular expression to separate fields. |
| Row Separator | String (ex: "\n"on Unix) to separate rows |
| Null Indicator | Value of the null indicator. |
| Session User | User of the defined session (the connection to the database). |
| Rollback | Enable or disable rollback. |
| On Error | Policy of error handling:  Continue: Continue the execution.  Terminate: Terminate the execution. |
| Reject Row File | Path and name of the file that holds the rejected rows.  Available when Continue is selected from the On Error list. |
| Error Count | Number of errors to trigger the termination of the execution.  Available when Terminate is selected from the On Error list. |
| Allocation | Number of pages initially allocated to the table or index. |
| Extend | Number of pages by which a table or index grows. |
| Fill Factor | Specify the percentage (from 1 to 100) of each primary data page that must be filled with rows, under ideal conditions. For example, if you specify a fillfactor of 40, the DBMS Server fills 40% of each of the primary data pages in the restructured table with rows. |
| Min Pages/Max Pages | Specify the minimum/maximum number of primary pages a hash table must have. The Min. pages and Max. pages must be at least 1. |
| Leaf Fill | A bulk copy from can specify a leaffill value. This clause specifies the percentage (from 1 to 100) of each B-tree leaf page that must be filled with rows during the copy. This clause can be used only on tables with a B-tree storage structure. |
| Non Leaf Fill | A bulk copy from can specify a nonleaffill value. This clause specifies the percentage (from 1 to 100) of each B-tree non-leaf index page that must be filled with rows during the copy. This clause can be used only on tables with a B-tree storage structure. |
| Row Estimate | Specify the estimated number of rows to be copied from a file to a table during a bulk copy operation. |
| Trailing WhiteSpace | Selected by default, this check box is designed to trim the trailing white spaces and applies only to such data types as VARCHAR, NVARCHAR and TEXT. |
| Encoding | List of the encoding schemes. |
| Output | Where to output the error message:  to console: Message output to the console.  to global variable: Message output to the global variable. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_DATA: the number of rows read. This is an After variable and it returns an integer.  NB\_LINE\_BAD: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Deployed along with tIngresOutputBulk, tIngresBulkExec feeds the given data in bulk to the Ingres database for performance gain. |
| Limitation | The database server/client must be installed on the same machine where Talend Studio is installed or where the Job using tIngresBulkExec is deployed, so that the component functions properly.  Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
