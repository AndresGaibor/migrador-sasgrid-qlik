<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc · versión 8.0 -->
# tMysqlCDC

Last updated: 9/30/2026

Extracts only the changes made to the source operational data and makes them
available to the target system(s) using database CDC views.

tMysqlCDC extracts source system data
that has changed since the last extraction and transports it to another system(s).

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tMysqlCDC Standard properties

These properties are used to configure tMysqlCDC running in the Standard Job framework.

The Standard
tMysqlCDC component belongs to the Databases family.

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
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved.  Information noteWarning: *Reset the database type by clicking the relevant   button to select the CDC connection.* |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | Database server listening port number. |
| Database | Name of the database. |
| Username and Password | Database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema using CDC and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Information noteWarning: *Reset the database type by clicking the relevant   button to select the schema of the CDC   connection.* * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table using CDC | Select the source table from which changes made to data are to be captured. |
| Subscriber | Enter the name of the application that will use the change table. |
| Events to catch | Insert: Select this check box to catch the data inserted in the change table since the last extraction.  Update: Select this check box to catch the data updated in the change table since the last extraction.  Delete: Select this check box to catch the data deleted in the change table since the last extraction. |
| Limit | Maximum number of consumed rows a subscriber can recover from the change table, per execution. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. Not available when the Use an existing connection check box is selected. |
| Keep data in CDC Table | Select this check box to retain changes in the CDC table, allowing one or more target systems to consult the data even after ingestion. When enabled, this option prevents deletion of the consulted CDC data; instead, it updates the value of the field CDC\_STATE to 'x'. This mechanism lets users recheck previously ingested data by filtering records where CDC\_STATE = 'x' (for example, using a tMysqlInput component), and manage deletion themselves if needed. This option is especially useful for users who need to audit or revisit ingested data without having to re-run Jobs or reverse-engineer the process to understand how the checkbox affects CDC\_STATE. |
| Enable Streaming Result | Select this check box to enables streaming over buffering which allows the code to read from a large table without consuming a large amount of memory in order to optimize the performance. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. Information noteNote: Select Trim all the String/Char columns to enable Trim columns in this field. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component. It requires an output component and row Main link. |

**Related concepts**  

* [Retrieving modified data using CDC](tmysqlcdc-tlogrow-tmap-tmysqloutput-retrieving-modified-data-using-cdc-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-retrieving-modified-data-using-cdc-standard-component-enterprise-this -->
# Retrieving modified data using CDC

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

This scenario is based on [Populating a MySQL data warehouse](/talend/en-US/components/8.0/mysql/tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-populating-mysql-data-warehouse-standard-component-enterprise-the). It continuously populates and
modifies the data stored in the CRM warehouse, and retrieves and saves, every night, these
modifications in a dedicated table using the CDC function. These modifications could be then
extracted by the various concerned departments.

### In this section

* [Configuring CDC](/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-configuring-cdc-standard-component-enterprise-before)
* [Modifying the CRM data](/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-modifying-crm-data-standard-component-enterprise-modify)
* [Extracting change data](/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-extracting-change-data-standard-component-enterprise-after)

**Related reference**  

* [tMysqlCDC](tmysqlcdc "Extracts only the changes made to the source operational data and makes them available to the target system(s) using database CDC views.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-configuring-cdc-standard-component-enterprise-before -->
# Configuring CDC

Last updated: 9/30/2026

Before being able to retrieve modified data from the CRM data warehouse, you
must:

1. Set up the database connection dedicated to CDC,
2. Set up a database connection to the source data and identify the table to
   catch,
3. Set the connection between the CDC and the data.

### In this section

* [Create connections and subscribers](/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-create-connections-and-subscribers-standard-component-enterprise-in)
* [Specify which table the subscriber wants to subscribe to and then activate the subscription](/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-specify-which-table-subscriber-wants-to-subscribe-to-and-then-activate-subscription-standard-component-enterprise)
* [Create the new subscribers Sub\_Finance and Sub\_Sales for the Treasury and Sales departments respectively](/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-create-new-subscribers-sub-finance-and-sub-sales-for-treasury-and-sales-departments-respectively-standard-component-enterprise)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-extracting-change-data-standard-component-enterprise-after -->
# Extracting change data

Last updated: 9/30/2026

## About this task

After setting up the CDC environment, you can now design a Job using the Mysql CDC
component to incrementally extract the change data from the
*Leadfact* table. To do that:

## Procedure

1. From the Palette, drop the tMysqlCDC and tLogRow components to the design workspace.
2. Link the two components using a Row Main
   link.
3. Double-click the tMysqlCDC component to
   define its properties.
4. Set Property Type to Repository and then select the select the schema
   corresponding to your Mysql database table,
   *CDC\_connection* in this scenario. The connection
   details will display automatically in the corresponding fields

   Information noteNote:

   If you have not stored the CRM data warehouse connection details in
   the Metadata entry in the Repository,
   select Built-in in the property type
   list and set the connection details manually.
5. In the Schema using CDC field, select
   Repository and then select the schema
   of the *Leadfact* table stored in the Metadata entry.
6. In the Table using CDC field, enter the
   name of the table captured by the CDC, in this scenario
   *Leadfact*.
7. In the Subscriber field, enter the name
   of the subscriber that will extract modified data,
   *Sub\_Mktg,*
   *Sub\_Sales*, and *Sub\_Finance* for the
   Marketing, Sales and Treasury Departments respectively.
8. In the Events to catch field, select the
   check boxes corresponding to the type of the modified data the subscriber
   will extract. In this scenario, select the three check boxes for the three
   subscribers.
9. Double-click the tLogRow component to
   set is properties.
10. Click the Sync columns button to
    retrieve the schema from the preceding component.
11. Save your Job and press F6 to execute
    it.

## Results

The customer names are converted to upper case and the modification type displays
here is *U* to stand for Update.

Once these modifications are extracted, they are no more available in the modified
table. To verify their extraction, right-click the *Leadfact*
table catched by the CDC and then select Views All
Changes. The extracted changes do not display anymore.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-modifying-crm-data-standard-component-enterprise-modify -->
# Modifying the CRM data

Last updated: 9/30/2026

## About this task

Modify the data of your customers in your CRM, for example, convert all customer
names to upper case.

## Procedure

1. Double-click the tMap component and
   enter row1.CustomerName.toUpperCase()in front of the CustomerName column to convert all customer names
   to upper case.
2. Click Ok.
3. Double-click the tMysqlOutput
   component.
4. In the Action on table field, select
   None.
5. In the Action on data field, select
   Insert or update to insert or update
   table data.
6. Save your Job and press F6 to execute
   the job.

## Results

To view all changes done on data, right-click the *Leadfact*
table and select View All Changes to open the
relevant dialog box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-create-connections-and-subscribers-standard-component-enterprise-in -->
# Create connections and subscribers

Last updated: 9/30/2026

## Procedure

1. In the Repository tree view and under
   Metadata, create a connection to your
   database dedicated to CDC, in this scenario
   *CDC\_connection*.

   Information noteNote:

   Ensure that the database connection for CDC is on the same server with
   the source data to which changes are to be captured.
2. In the Repository tree view and under
   Metadata, create a connection to the
   source data warehouse and identify the table to catch, in this scenario
   *CRM\_connection*.
3. Right-click the *CRM* connection and select Retrieve schema from the drop-down menu to
   retrieve the schema of the table to catch.
4. Right-click CDC Foundation of
   *CRM* and select Create
   CDC in the drop-down menu.

   The Create Change Data Capture dialog
   box displays
5. In the Set link Connection field, select
   *CDC\_connection*.
6. Click Create Subscriber. The Create Subscriber and Execute SQL Script dialog
   box displays.
7. Click Execute and then Close.
8. Click Finish to validate the creation of
   the subscriber table.

   In the CDC Foundation folder, the
   relevant subscriber table displays.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-create-new-subscribers-sub-finance-and-sub-sales-for-treasury-and-sales-departments-respectively-standard-component-enterprise -->
# Create the new subscribers *Sub\_Finance* and *Sub\_Sales* for the Treasury and Sales departments respectively

Last updated: 9/30/2026

## Procedure

1. Right-click *Leadfact* and select Edit CDC Subscribers from the drop-down list. The
   Edit CDC dialog box displays.
2. Click Add. The Input subscriber name dialog box displays.
3. Enter the name of the subscriber, in this scenario
   *Sub\_Finance* and
   *Sub\_Sales*.
4. Click Execute and then Close to validate the creation operation.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-specify-which-table-subscriber-wants-to-subscribe-to-and-then-activate-subscription-standard-component-enterprise -->
# Specify which table the subscriber wants to subscribe to and then activate the subscription

Last updated: 9/30/2026

## Procedure

1. Right-click the *Leafact* schema in the source CRM and
   select Add CDC in the drop-down list. The
   Create Subscriber and Execute SQL
   Script dialog box displays.
2. In the Events to catch check boxes,
   select Insert, Update and Delete to catch
   inserted, updated or deleted data.
3. In the Subscriber Name field, enter the
   name of the subscriber that will have access to the modifications, in this
   scenario *Sub\_Mktg* for the Marketing department.
4. Click Execute and then Close to validate the subscription.

   In the CDC Foundation folder, the two
   created tables display and the schema node of the catched table is marked
   with a green CDC symbol.
