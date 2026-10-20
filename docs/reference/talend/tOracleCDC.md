<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc · versión 8.0 -->
# tOracleCDC

Last updated: 9/30/2026

Extracts source system data that has changed since the last extraction and
transports it to another/other system(s).

tOracleCDC addresses data extraction
and transportation needs. It only extracts the changes done to the source operational
data and makes them available to the target system(s) using database CDC views.

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tOracleCDC Standard properties

These properties are used to configure tOracleCDC running in the Standard Job framework.

The Standard
tOracleCDC component belongs to the Databases family.

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
| Connection Type | Select a connection type from the drop-down list:  * Oracle SID: Select this connection   type to uniquely identify a particular database on a system. * Oracle Service Name: Select this   connection type to use the TNS alias that you give when you connect to   the remote database. * Oracle OCI: Select this connection   type to use Oracle Call Interface with a set of C-language software APIs   that provide an interface to the Oracle database. * Oracle CUSTOM: Select this   connection type to access a clustered database. |
| DB Version | Select the version of the Oracle database being used. |
| Host | Specify the host name or IP address of the Oracle database. This field appears only when Oracle SID or Oracle Service Name is selected from the Connection Type drop-down list. |
| Port | Specify the listening port number of the Oracle database. This field appears only when Oracle SID or Oracle Service Name is selected from the Connection Type drop-down list. |
| Database | Specify the Oracle database name. This field appears only when Oracle SID or Oracle Service Name is selected from the Connection Type drop-down list. |
| Local Service Name | Specify the local service name of the Oracle database. This field appears only when Oracle OCI is selected from the Connection Type drop-down list. |
| URL | Specify the URL of the remote Oracle database. This field appears only when Oracle CUSTOM is selected from the Connection Type drop-down list. |
| Oracle schema | Specify the name of the Oracle schema. |
| Username and Password | Specify the user authentication data of the Oracle database. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema using CDC and Edit schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The schema is set by default according to the CDC mode being   used. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| CDC mode | Select a CDC mode to be used:  * Trigger: the CDC   trigger mode. * Log: the CDC   Redo/Archive log mode. This mode requires Oracle database Enterprise   Editions and is not supported in Oracle   12 or higher versions. * XStream: the CDC   XStream mode. This mode is available only when the Connection Type is Oracle OCI and the DB   Version is Oracle 12-7   (or higher). |
| Generate LCR type | Select a type for the LCR to be generated, either LCR Object or LCR XML Document. This list appears only when the CDC mode is XStream. |
| Table using CDC | Specify the source table from which changes made to data are to be captured. |
| Set data table schema | Select this check box if you want to specify the schema of the CDC table. This check box appears only when the CDC mode is Trigger or Log. |
| Subscriber | Specify the name of the application that will use the change table if you use the Trigger mode to capture changes done on data. This field appears only when the CDC mode is Trigger. |
| Events to catch | Insert: Select this check box to catch the data inserted in the change table since the last extraction. Update: Select this check box to catch the data updated in the change table since the last extraction.  Delete: Select this check box to catch the data deleted in the change table since the last extraction.  These check boxes appear only when the CDC mode is Trigger or Log. |
| Limit | Specify the maximum number of consumed rows a subscriber can recover from the change table, per execution. This field appears only when the CDC mode is Trigger. |
| Outbound server name | Specify the XStream outbound server name. This field appears only when the CDC mode is XStream. |
| Keep listening | Select this check box to keep monitoring the outbound server for data changes. The Job will not stop until you manually stop it when you need to. This check box appears only when the CDC mode is XStream. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Keep data in CDC Table | Select this check box to retain changes in the CDC table, allowing one or more target systems to consult the data even after ingestion. When enabled, this option prevents deletion of the consulted CDC data; instead, it updates the value of the field CDC\_STATE to 'x'. This mechanism lets users recheck previously ingested data by filtering records where CDC\_STATE = 'x' (for example, using a tMysqlInput component), and manage deletion themselves if needed. This option is especially useful for users who need to audit or revisit ingested data without having to re-run Jobs or reverse-engineer the process to understand how the checkbox affects CDC\_STATE. This field appears only when the CDC mode is Trigger or Log. |
| Use cursor | Select this check box to specify the number of rows you want to work with at any given time. This option optimises performance. This field appears only when the CDC mode is Trigger or Log. |
| Trim all the String/Char columns | Select this check box to delete any spaces found at the beginning or end of fields, in all of the columns containing character strings. This field appears only when the CDC mode is Trigger or Log. |
| Trim column | Remove leading and trailing whitespace from defined columns. Information noteNote: Clear Trim all the String/Char columns to enable Trim columns in the table.  This table appears only when the CDC mode is Trigger or Log. |
| Acknowledge interval(seconds) | Specify the value for the OCI\_ATTR\_XSTREAM\_ACK\_INTERVAL attribute for the outbound server. The default value is *30* seconds. For more infomrmation about this attribute, see <http://docs.oracle.com/cd/E18283_01/server.112/e16545/xstrm_oci_intro.htm#CEGDICBB>.  This field appears only when the CDC mode is XStream. |
| Idle timeout(seconds) | Specify the value for the OCI\_ATTR\_XSTREAM\_IDLE\_TIMEOUT attribute for the outbound server. The default value is *1* second. For more information about this attribute, see <http://docs.oracle.com/cd/E18283_01/server.112/e16545/xstrm_oci_intro.htm#CEGDICBB>.  This field appears only when the CDC mode is XStream. |
| tStatCatcher Statistics | Select this check box to collect the log data at component level. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component. It requires an output component and row Main link. |

**Related concepts**  

* [Extracting and synchronizing data changes using XStream mode](toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-extracting-and-synchronizing-data-changes-using-xstream-mode-standard-component-enterprise-this)
* [Retrieving modified data using Oracle CDC Redo log mode](toraclecdc-tlogrow-tmap-toracleoutput-retrieving-modified-data-using-oracle-cdc-redo-log-mode-standard-component-enterprise-before)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-tlogrow-tmap-toracleoutput-retrieving-modified-data-using-oracle-cdc-redo-log-mode-standard-component-enterprise-before -->
# Retrieving modified data using Oracle CDC Redo log mode

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

Information noteWarning:

*Before modifying data in the LEADFACT table and retrieving
these modifications using the tOracleCDC
component, you must activate the Redo log mode
in the Oracle database that holds the table to monitor.*

This scenario is based on the scenario [Populating an Oracle data warehouse](/talend/en-US/components/8.0/oracle/toracleoutput-toracleinput-tmap-toracleinput-tmap-populating-oracle-data-warehouse-standard-component-enterprise). It continuously populates and modifies the data stored in the *LEADFACT* table, and retrieves and saves, every night, these modifications in a
dedicated table using the CDC function. These modifications could be then extracted by the
various concerned departments.

### In this section

* [Step 1: Configuring CDC](/talend/en-US/components/8.0/change-data-capture/toraclecdc-tlogrow-tmap-toracleoutput-step-1-configuring-cdc-standard-component-enterprise-before)
* [Step 2: Modifying the data](/talend/en-US/components/8.0/change-data-capture/toraclecdc-tlogrow-tmap-toracleoutput-step-2-modifying-data-standard-component-enterprise-modify)
* [Step 3: Extracting change data](/talend/en-US/components/8.0/change-data-capture/toraclecdc-tlogrow-tmap-toracleoutput-step-3-extracting-change-data-standard-component-enterprise-after)

**Related reference**  

* [tOracleCDC](toraclecdc "Extracts source system data that has changed since the last extraction and transports it to another/other system(s).")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tOracleOutput](/talend/en-US/components/8.0/oracle/toracleoutput)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-extracting-and-synchronizing-data-changes-using-xstream-mode-standard-component-enterprise-this -->
# Extracting and synchronizing data changes using XStream mode

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

This scenario describes a Job that inserts data into an empty source table *PERSON* in one Oracle database on which the XStream outbound
server is configured, then extracts and synchronizes the data changes into an empty
target table *PERSON\_BAK* in another Oracle database on
which the XStream inbound server is configured using Oracle CDC XStream mode, and
finally displays the data in the source and target tables on the console.

Prerequisites: The Oracle database connections
dedicated to the XStream outbound and inbound servers have been set up in the Repository tree view in Talend Studio, and the
CDC has been added to the empty source and target tables.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-dropping-and-linking-components-standard-component-enterprise-create)
* [Configuring the components](/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-configuring-components-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-saving-and-executing-job-standard-component-enterprise-press)

**Related reference**  

* [tOracleCDC](toraclecdc "Extracts source system data that has changed since the last extraction and transports it to another/other system(s).")
* [tOracleCDCOutput](toraclecdcoutput "Synchronizes data changes in the Oracle XStream CDC mode.")

**Related information**  

* [tOracleInput](/talend/en-US/components/8.0/oracle/toracleinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tOracleOutput](/talend/en-US/components/8.0/oracle/toracleoutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-tlogrow-tmap-toracleoutput-step-1-configuring-cdc-standard-component-enterprise-before -->
# Step 1: Configuring CDC

Last updated: 9/30/2026

## About this task

Before being able to retrieve modified data from the *LEADFACT*
table, you must:

## Procedure

1. first set up the DB connection dedicated to CDC,
2. second, set up a DB connection to the source data and identify the table
   to catch,
3. finally, set the connection between the CDC and the data.

   To do that:
4. In the Repository tree view and under
   Metadata, create a connection to your
   database dedicated to CDC, *cdc\_publisher* in this
   scenario.

   Information noteNote:

   Ensure that the DB connection for CDC is on the same server with the
   source data to which changes are to be captured.
5. In the Repository tree view and under
   Metadata, create a connection to the
   source data warehouse and identify the table to catch,
   *LEADFACT* in this scenario.
6. Right-click the connection to the *orcle* database and
   select Retrieve schema from the drop-down
   menu to retrieve the schema of the table to catch.
7. Right-click CDC Foundation of the
   *cdc-data* connection and select Create CDC in the drop-down menu.

   The Create Change Data Capture dialog
   box displays
8. Click the [...] button next to the Set link
   Connection field and select the connection that corresponds
   to CDC, *cdc\_publisher* in this example.
9. In the Options area, select the Log mode check box.
10. Click Create Subscriber. The Create Subscriber and Execute SQL Script dialog
    box displays.
11. Click Execute and then Close to close the dialog box.
12. Click Finish to validate the creation of
    the subscriber table.

    In the CDC Foundation folder, the
    relevant subscriber table displays.

    You must specify which table the subscriber wants to subscribe to and
    then
13. Right-click the *LEADFACT* schema of the
    *cdc-data* connection and select Add CDC in the drop-down list. The Create Subscriber and Execute SQL Script dialog
    box displays.

    Information noteNote:

    For Oracle databases and in *Talend Studio* version 3.2 or subsequent versions,
    the CDC system creates an alias for the source table(s) monitored. This
    avoids problems relating to identifier length upon creation of the table
    of changes and its associated view. For CDC systems which are already in
    place, the table names are maintained.
14. Click Execute and then Close to validate the subscription.

    In the CDC Foundation folder, the two
    created tables display and the schema node of the catched table is marked
    with a green CDC symbol.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-tlogrow-tmap-toracleoutput-step-2-modifying-data-standard-component-enterprise-modify -->
# Step 2: Modifying the data

Last updated: 9/30/2026

## About this task

Modify the data of your clients in the *LEADFACT* table, for
example, convert all customer names to upper case.

## Procedure

1. Double-click the tMap component and enter
   row1.LASTNAME.toUpperCase()in front of the CLASTNAME column to convert all customer names to
   upper case.
2. Click Ok.
3. Double-click the tOracleOutput
   component.
4. In the Action on table field, select
   None.
5. In the Action on data field, select
   Insert or update to insert or update
   table data.
6. Save your Job and press F6 to execute
   it.

## Results

To view all changes done on data, right-click the *LEADFACT*
table and select View All Changes to open the
relevant dialog box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-tlogrow-tmap-toracleoutput-step-3-extracting-change-data-standard-component-enterprise-after -->
# Step 3: Extracting change data

Last updated: 9/30/2026

## About this task

After setting up the CDC environment, you can now design a Job using the Oracle
CDC component to incrementally extract the change data from the
*LEADFACT* table. To do that:

## Procedure

1. From the Palette, drop the OracleCDC and tLogRow components to the design workspace.
2. Link the two components using a Row Main
   link.
3. Double-click tOracleCDC to open its
   Basic settings view and define its
   properties.
4. Set Property Type to Repository and then select the schema
   corresponding to your Oracle DB table, *cdc\_publisher* in
   this scenario. The connection details will display automatically in the
   corresponding fields

   Information noteNote:

   If you have not stored the data warehouse connection details in the
   Metadata folder in the Repository tree view, select Built-in in the property type list and set
   the connection details manually.
5. In the Schema using CDC field, select
   Repository and then select the schema
   of the *LEADFACT* table stored in the Metadata folder.
6. In the Table using CDC field, enter the
   name of the table captured by the CDC, in this scenario
   *Leadfact*.
7. In the Events to catch field, select the
   check boxes corresponding to the type of the modified data the subscriber
   will extract. In this scenario, select the three check boxes for the three
   subscribers.
8. Double-click tLogRow to display its
   Basic settings view and define its
   properties.
9. Click the Sync columns button to retrieve
   the schema from the preceding component.
10. Click Edit schema to open the schema
    dialog box.
11. In the TALEND\_CDC\_CREATION\_DATE line of
    the Date Pattern column, enter between
    brackets the desired date format: "yyyy-MM-dd".
12. Save your Job and press F6 to execute
    it.

## Results

In the Redo log mode, changes done on data are
indicated in the following way: modifications are equal to first, an "update and
delete" operation (UO), and then to an "update and
insert" operation (UN). Thus, client data displays
twice:

- First, data is deleted (UO).

-Second, data is inserted (UN).

Once these modifications are extracted, they are no more available in the modified
table. To verify their extraction, right-click the *LEADFACT*
table catched by the CDC and then select Views All
Changes. The extracted changes do not display anymore.

For another CDC scenario using the Trigger mode,
see [Retrieving modified data using CDC](/talend/en-US/components/8.0/change-data-capture/tmysqlcdc-tlogrow-tmap-tmysqloutput-retrieving-modified-data-using-cdc-standard-component-enterprise-this).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Inserting data into the source table](/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-inserting-data-into-source-table-standard-component-enterprise)
* [Extracting and synchronizing data changes to the target table](/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-extracting-and-synchronizing-data-changes-to-target-table-standard-component-enterprise)
* [Retrieving data from the source and target table](/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-retrieving-data-from-source-and-target-table-standard-component-enterprise)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-dropping-and-linking-components-standard-component-enterprise-create -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in
   the design workspace or dropping them from the Palette: a tFixedFlowInput
   component, a tOracleOutput component, a
   tOracleCDC component, a tOracleCDCOutput component, two tOracleInput components, and two tLogRow components.
2. Connect tFixedFlowInput to tOracleOutput using a Row > Main link.
3. Do the same to connect tOracleCDC to
   tOracleCDCOutput, the first tOracleInput to the first tLogRow, and the second tOracleInput to the second tLogRow.
4. Connect tFixedFlowInput to tOracleCDC using a Trigger > On Subjob Ok
   connection.
5. Do the same to connect tOracleCDC to the
   first tOracleInput and the first tOracleInput to the second tOracleInput.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, the input data is inserted into the source table and then
   the data changes are synchronized into the target table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-extracting-and-synchronizing-data-changes-to-target-table-standard-component-enterprise -->
# Extracting and synchronizing data changes to the target table

Last updated: 9/30/2026

## Procedure

1. Double-click tOracleCDC to open its
   Basic settings view.
2. Set Property of the CDC connection to Repository and select the connection metadata
   corresponding to the Oracle database on which the XStream outbound server is
   configured, *Oracle12\_XStreamOut* in this
   example. The connection type, database version and other connection details
   information will be completed automatically.
3. Select LCR Object from the Generate LCR type drop-down list.

   In the Table using CDC field, enter the name of the
   source table from which changes made to data are to be captured. In this
   example, it is *PERSON*.

   In the Outbound server name field, enter
   the XStream outbound server name. In this example, it is *xout*.
4. Click the [...] button next to Edit schema to open the schema editor, and you
   will see that the schema has been set by default.
5. Click Advanced settings to open its
   view.

   In the Idle timeout(seconds) field, enter the number of
   seconds of idle time that the outbound server waits for an LCR before
   terminating the call to get or receive an LCR stream. Considering the
   network latency and the database response rate, the idle time is set to
   *60* seconds in this example.
6. Double-click tOracleCDCOutput to open its
   Basic settings view.

   Set Property of the CDC connection to Repository and select the connection metadata
   corresponding to the Oracle database on which the XStream inbound server is
   configured, *Oracle12\_XStreamIn* in this
   example. The database version and other connection details information will
   be completed automatically.
7. In the Inbound server name field, enter
   the XStream inbound server name. In this example, it is *xin*.

   Select the Set data table schema check
   box and specify the schema of the CDC table. In this example, it is
   *TALEND*.

   Select the Set target table check box and
   specify the table to which data changes from the inbound server will be
   replicated. In this example, it is *PERSON\_BAK*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-inserting-data-into-source-table-standard-component-enterprise -->
# Inserting data into the source table

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit schema to open the schema editor.

   Click four times the [+] button to add four columns:
   *id* and *age* of the integer type, *name* and *sex* of the
   string type.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
3. Select Use Inline Content(delimited file) in the
   Mode area, and then enter the following
   input data in the Content field:

   ```
   1;Ford;Male;25
   2;Rose;Female;30
   3;Sabrina;Female;28
   4;Teddy;Male;32
   5;Kate;Male;35
   ```
4. Double-click tOracleOutput to open its
   Basic settings view.
5. Set Property Type to Repository and select the connection metadata corresponding
   to the Oracle database on which the XStream outbound server is configured,
   *Oracle12\_XStreamOut* in this example. The connection
   type, database version and other connection details information will be
   completed automatically.
6. In the Table field, enter the name of the
   table into which the input data will be inserted. In this example, it is
   *PERSON*.
7. Click the [...] button next to Edit schema to open the schema editor to ensure
   the schema has been synced up.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/toraclecdc-toraclecdcoutput-toracleinput-toracleoutput-retrieving-data-from-source-and-target-table-standard-component-enterprise -->
# Retrieving data from the source and target table

Last updated: 9/30/2026

## Procedure

1. Double-click the first tOracleInput to
   open its Basic settings view.
2. Set Property Type to Repository and select the connection metadata corresponding
   to the Oracle database on which the XStream outbound server is configured,
   *Oracle12\_XStreamOut* in this example.
   The connection type, database version and other connection details
   information will be completed automatically.

   Set Schema to Repository and select the source table from the Repository. In this example, it is *PERSON*.
3. In the Query field, enter the following SQL statement to
   retrieve all the data from the source table:

   ```
   select * from PERSON
   ```
4. Double-click the second tOracleInput to
   open its Basic settings view.
5. Set Property Type to Repository and select the connection metadata corresponding
   to the Oracle database on which the XStream inbound server is configured,
   *Oracle12\_XStreamIn* in this example.
   The connection type, database version and other connection details
   information will be completed automatically.

   Set Schema to Repository and select the target table from the Repository. In this example, it is *PERSON\_BAK*.
6. In the Query field, enter the following SQL statement to
   retrieve all the data from the target table:

   ```
   select * from PERSON_BAK
   ```
7. Double-click the first tLogRow to open
   its Basic settings view.

   In the Mode area, select Table (print values in cells of a table) for a
   better display of the result.
8. Do the same to configure the second tLogRow.
