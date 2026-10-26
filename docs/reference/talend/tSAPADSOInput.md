<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsoinput · versión 8.0 -->
# tSAPADSOInput

Last updated: 9/30/2026

Retrieves data of an active ADSO (Advanced Data Store Object) from an SAP BW system
on an SAP HANA database or through SAP Java Connector.

## tSAPADSOInput Standard properties

These properties are used to configure tSAPADSOInput running in the Standard Job framework.

The Standard
tSAPADSOInput component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: When prompted that this component requires
sapjco.jar, download the module and refer to the instructions at
[SAP Java Connector](https://support.sap.com/en/product/connectors/jco.html).

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Connection type | Select the way to retrieve ADSO data, Hana JDBC or SAP JCO 3.  * Hana JDBC: retrieves ADSO data through a JDBC   connection to an SAP HANA database. * SAP JCO 3: retrieves ADSO data through SAP Java   Connector.   Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Host | Enter the IP address or hostname of the database. This option is available when Hana JDBC is selected from the Connection type drop-down list. |
| Port | Enter the listening port number of the database. This option is available when Hana JDBC is selected from the Connection type drop-down list. |
| Table Schema | Enter the table schema name. This option is available when Hana JDBC is selected from the Connection type drop-down list. |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  These two options are available when Hana JDBC is selected from the Connection type drop-down list. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Name | Enter the name of the active Advanced Data Store Object from which data will be retrieved. This option is available when Hana JDBC is selected from the Connection type drop-down list. |
| Use an existing connection | Select this check box and from the Connection configuration drop-down list displayed, select the component in which the relevant reused database connection is configured. When a Job contains a parent Job and a child Job, the list displayed presents only the connection components in the same Job level.  This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Server Type | Select the type of the SAP server to be connected, either Application Server or Message Server. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Client | Enter the SAP system client ID. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| UserId and Password | Enter the user connection ID and password. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  These two options are available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Language | Enter the language of the SAP system. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Host name | Enter the name or IP address of the host on which the SAP server is running. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| System number | Enter the SAP system number. This option is available when SAP JCO 3 is selected from the Connection type drop-down list and Application Server is selected from the Server Type drop-down list. |
| System ID | Enter the SAP system ID. This field is available when SAP JCO 3 is selected from the Connection type drop-down list and Message Server is selected from the Server Type drop-down list. |
| Group Name | Enter the SAP group name. This field is available when SAP JCO 3 is selected from the Connection type drop-down list and Message Server is selected from the Server Type drop-down list. |
| Service name | Enter the name of the operational delta queue. For more information, see [Introduction to Operational Delta Queues](https://wiki.scn.sap.com/wiki/display/BI/Introduction+to+Operational+Delta+Queues#IntroductiontoOperationalDeltaQueues-TheOperationalDeltaQueue(ODQ)).  This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Subscriber name | Enter the name of the subscriber that consumes data from SAP. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Subscriber process name | Enter the name of the subscriber process. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Execute a full extraction | Select this check box to perform a full extraction to retrieve all data from an SAP system. By default, this check box is cleared and a delta extraction will be performed to retrieve only changed data. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Reset subscriber | Select this check box to reset the subscriber to make an initial load. This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Selection Group | Specify the search condition(s) used to filter data to be retrieved by clicking the [+] button to add as many rows as needed, each row for a search condition, and set the value of the following attributes for each condition. Information noteNote: This component retrieves the data records that meet all the conditions set in this field.   * Column: enter the name of the schema column based   on which retrieved data will be filtered. * Sign: select either `Include`   or `Exclude` from the drop-down list.    + `Include`: the data that meets the condition     will be retrieved.   + `Exclude`: the data that doesn't meet the     condition will be retrieved. * Operator: select from the drop-down list the data   filter operator used to build the search condition. * Value: specify the search value used to build the   search condition. Note that wildcard characters are not supported. * High value: specify another search value used to   build the search condition for the Between   operator.  When using a column of Date type to specify a filter, the date and time   values in the Value and High   Value columns should be in the format   `yyyyMMdd` and `HHMMSS`,   which might be different from the format defined in the schema editor.   Note that wildcard characters are not supported.   This table is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| Specify a shared destination | Select this check box and specify the shared destination in the Shared destination name field displayed. The shared destination allows the SAP components to use the shared destination on the Talend Runtime when they are executed as part of an ESB Route or ESB Data Service within the Talend Runtime container OSGi Environment. Besides specifying the shared destination name in the component, you also need to setup the SAP DataSource for the Talend Runtime. What you need to do to define the SAP DataSource and how to configure it are described in the readme.txt provided in the Talend ESB package in the /add-ons/datasource/sap folder.  Note that if you use the component's own connection configuration, your SAP connection will be closed at the end of the component. To prevent this from happening, use a shared destination with its name specified.  This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Enter additional JDBC parameters in the format of `parameterName1=value1&parameterName2=value2&...`. This field allows you to provide metadata for Advanced DataStore Objects. This option is available when you select Hana JDBC from the Connection type drop-down list. |
| Fetch size | Enter the maximum size of the resultset (in number of rows) that can be returned from the SAP BW database in response to a BAPI call or a request. A value of `-1`, the default, uses the default fetch size, which is determined by the Java code or the BAPI on SAP side.  It is recommended to set this field according to the memory space allocated to your Job and the number of fields requested. With a given memory space, the more fields requested, the smaller the fetch size.  This option is available when SAP JCO 3 is selected from the Connection type drop-down list. |
| SAP Properties | If you need to use custom configuration for the SAP system being used, complete this table with the property or properties to be customized. For example,  * to establish a Unicode connection between the SAP system and Talend Studio, you need to add the property   `jco.server.unicode` and set its value to   `1`. Note that this property works if you are   using SAP Java Connector 2.x and is unnecessary for SAP Java Connector   3.0 and higher versions. * to set up an SAP connection with Secure Network   Communications (SNC), you need to add and set the following properties in   this field.    + jco.client.snc\_mode   + jco.client.snc\_myname   + jco.client.snc\_lib=.../sapcrypto/sapcrypto.dll   + jco.client.snc\_partnername   + jco.client.snc\_qop Information noteNote: The values of the above properties vary with   the system environment. Contact your SAP system administrator if you are   not sure how to set the properties.  For more information about setting the SNC parameters, see [Configuring SNC: External Programs to AS ABAP Using   RFC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/d9e8a740bbaa4d8f8bee6f7b173bd99f.html) and [Communication Paths that Support SNC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/76128150317a47b6a326e63a17017729.html).   This table is available when SAP JCO 3 is selected from the Connection type drop-down list and the Use an existing connection check box is not selected in the Basic settings view. |
| Convert NULL numeric values to zero | Select this check box to allow automatic conversion of NULL numeric fields to zero during data extraction. |
| Set max length for variable length type | Select this check box to define a custom maximum length for variable-length type fields, such as XXL InfoObject fields, when reading data from an SAP BW aDSO. By default, this check box is cleared and a default length of 100 characters is applied, which may result in truncation of longer values. |
| Max length | Enter the maximum number of characters to read for variable-length type fields. The default value is `100`. This field is available when the Set max length for variable length type check box is selected. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as a start component of a Job or subJob and it always needs an output link. |

**Related concepts**  

* [Retrieving ADSO data from SAP BW](tsapadsoinput-tfileoutputdelimited-retrieving-adso-data-from-sap-bw-standard-component-enterprise "This sample scenario shows you how you can use Talend components to retrieve data of an active ADSO (Advanced Data Store Object) from an SAP BW system on an SAP HANA database.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-retrieving-adso-data-from-sap-bw-standard-component-enterprise -->
# Retrieving ADSO data from SAP BW

Last updated: 9/30/2026

This sample scenario shows you how you can use Talend components to retrieve data of an active
ADSO (Advanced Data Store Object) from an SAP BW system on an SAP HANA database.

### In this section

* [Importing SAP BW Metadata](/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-importing-sap-bw-metadata-follow)
* [Creating a Job for retrieving ADSO data from SAP BW](/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-creating-job-for-retrieving-adso-data-from-sap-bw-standard-component-enterprise-naviga)
* [Configuring the Job for retrieving ADSO data from SAP BW](/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-configuring-job-for-retrieving-adso-data-from-sap-bw-standard-component-enterprise)
* [Executing the Job to retrieve ADSO data from SAP BW](/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-executing-job-to-retrieve-adso-data-from-sap-bw-standard-component-enterprise-press)

**Related reference**  

* [tSAPADSOInput](tsapadsoinput "Retrieves data of an active ADSO (Advanced Data Store Object) from an SAP BW system on an SAP HANA database or through SAP Java Connector.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-configuring-job-for-retrieving-adso-data-from-sap-bw-standard-component-enterprise -->
# Configuring the Job for retrieving ADSO data from SAP BW

Last updated: 9/30/2026

## Procedure

1. Double-click the tSAPADSOInput component to open its Basic settings view.
2. Check the authentication details of your SAP BW ADSO metadata.
   These fields are automatically populated after dragging-and-dropping the SAP BW
   ADSO metadata into the design workspace.
3. Click the [...] button
   to open the Schema dialog box, which
   displays the columns of data that you wish to retrieve.

   In this example, nine columns are displayed, `MANDT`, `GJAHR`, `BELNR`,
   `BLDAT`, `BSCHL`, `BSTAT`,
   `BUDAT`, and `HWAER` of String type, and `DMSHB` of BigDecimal type.

   You can also change the schema to the Built-In mode and click
   the [...] button next to Edit schema to update the schema
   definition.
4. Double-click the tFileOutputDelimited component to open its Basic settings view.
5. In the File Name field,
   specify the path to the file in which retrieved data will be written, D:/tsapadsoinput\_out.csv in this example.
6. Select the Include
   Header check box to include the column names in the output
   file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-creating-job-for-retrieving-adso-data-from-sap-bw-standard-component-enterprise-naviga -->
# Creating a Job for retrieving ADSO data from SAP BW

Last updated: 9/30/2026

Design a Job with the SAP BW ADSO metadata that you previously
created and select the tSAPADSOInput component.

## Procedure

1. Navigate to Job Designs >  Standard to create a new Job.
2. Drag-and-drop the SAP ADSO that you previously created into the
   design workspace from Metadata >  SAP Connections.
3. When prompted, select tSAPADSOInput.
4. Add a tFileOutputDelimited component onto its design workspace.
5. Connect the tSAPADSOInput component to the
   tFileOutputDelimited component via a Row > Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-executing-job-to-retrieve-adso-data-from-sap-bw-standard-component-enterprise-press -->
# Executing the Job to retrieve ADSO data from SAP BW

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save your Job.
2. Press F6 to execute your Job.
3. Open the file generated to check the retrieved data.

   You will find only the data of the columns specified in the schema has
   been retrieved and written into the file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-importing-sap-bw-metadata-follow -->
# Importing SAP BW Metadata

Last updated: 9/30/2026

You can create a connection to an SAP BW system and an SAP HANA
database and store this connection in the Repository >  Metadata folder.

## Procedure

1. Follow the procedure in [Setting up an SAP connection](/talend/r/en-US/8.0/studio-user-guide/setting-up-sap-connection)
2. Follow the procedure in Retrieving SAP BW objects
   metadata.

   You can then use the newly created SAP metadata when you
   design the Job.

### In this section

* [Retrieving SAP BW ADSO](/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-retrieving-sap-bw-adso-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsoinput-tfileoutputdelimited-retrieving-sap-bw-adso-in -->
# Retrieving SAP BW ADSO

Last updated: 9/30/2026

Retrieve the metadata of the SAP BW Advanced Data Store Object (ADSO) using the SAP
metadata wizard.

## Procedure

1. In the Repository tree
   view, right-click the newly created SAP connection and select
   Retrieve SAP BW metadata.
2. Select AdvancedDataStoreObject from the Search in drop-down list.
3. Fill in the relevant information on the following fields:

   * Name: enter the filter criterion for the object
     name
   * Description: enter the filter criterion for the
     object description

   Information noteNote: The filter criteria, Name and
   Description, act together as an OR operator.
4. Click Search to list all the objects that match the
   filter criteria.
5. Select the tables that you wish to retrieve by marking the checkbox in the
   Name column.
6. Wait for the Creation Status to display
   Success.

   The tables and their schemas of the selected objects are saved in the
   Repository tree.
7. Click Next to proceed to the next step.

   All tables of the selected objects are listed in the Table
   Name area.

   1. Click Refresh
      Table to display the latest table schema in the
      Current Table area. You can
      modify the schema of the selected table in the Current Table area, if needed.
   2. Click Refresh Preview to preview data in the
      selected table, if needed.
8. Click Finish to save the tables and their schemas in the
   Repository tree view.
