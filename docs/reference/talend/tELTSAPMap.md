<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/teltsapmap · versión 8.0 -->
# tELTSAPMap

Last updated: 9/30/2026

Builds the SQL SELECT statement using the table schema(s) provided by one or more
tELTSAPInput components.

## tELTSAPMap Standard properties

These properties are used to configure tELTSAPMap running in the Standard Job framework.

The Standard
tELTSAPMap component belongs to the ELT family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and from the list displayed select the relevant connection component to reuse the connection details you have already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| SAP Map Editor | The ELT Map editor allows you to define the output schema and build graphically the SQL statement to be executed. The column names of schema can be different from the column names in the SAP system. Information noteNote:  * The ELT Map editor supports context variables and global variables if   you have installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Server Type | Select the type of the SAP server to be connected, either Application Server or Message Server. |
| Client | The SAP system client ID. |
| UserId and Password | The user connection ID and password.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Language | The language of the SAP system. |
| Host name | The name or IP address of the host on which the SAP server is running. |
| System number | The SAP system number.  This property is available only when Application Server is selected from the Server Type drop-down list. |
| System ID | The SAP system ID.  This property is available only when Message Server is selected from the Server Type drop-down list. |
| Group Name | The SAP group name.  This property is available only when Message Server is selected from the Server Type drop-down list. |
| CDS view | Select this option to retrieve data from an SAP CDS view. You can set parameters for the SAP CDS view in the CDS View parameters table. To set a CDS view parameter, add a row in the table by clicking the plus button on the bottom of the table, type in the parameter name in the Parameter column of the newly added row, and type in the parameter value in the Value column of the newly added row.  This option is unavailable if Use RFC server in the Advanced settings view is selected.  Information noteNote:  * If you retrieve data from an SAP CDS view with Use FTP-Batch   Options selected in the Basic   settings view, note that the SAP API only provides   security extraction and cannot specify the path for FTP. The parameters   related to the FTP path will be hidden. Other parameters will be the same   as those of table extraction. * Because the SAP API only supports retrieving data from one CDS view at a   time, this feature does not support data extraction from multiple CDS   views joined together. * This option is available only when you have installed the 8.0.1-R2023-06   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Start row number | Specify the sequence number of the row from which data retrieval starts. The sequence number of the row in an SAP table starts from *0*. The default value for this field is *-1*, which means to read all rows in the specified table.  This option is unavailable if Use RFC server in the Advanced settings view is selected.  Information noteNote: This option is available only when you have installed the 8.0.1-R2023-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Max row number | Specify the maximum number of rows to retrieve data from. The default value for this field is *-1*, which means to retrieve all rows that meet the filter condition.  This option is unavailable if Use RFC server in the Advanced settings view is selected.  Information noteNote: This option is available only when you have installed the 8.0.1-R2023-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Batch size | Specify the maximum number of records that can be written in each file generated by the SAP system. |
| File protocol | Select either FTP or the secure alternative SFTP. |
| FTP host | Specify the IP address or the host name of the FTP server. |
| FTP port | Specify the listening port number of the FTP server. |
| FTP user and FTP password | Specify the user authentication data to access the FTP server. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use the SAP Application Server logical path | Select this check box to enter the logical path configured in the SAP Application Server which specify in which directory the flat files must be created. Information noteNote: This option is available only when you have installed the 8.0.1-R2023-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| FTP directory | Specify the directory where the files generated by the SAP system will be saved. This option is not available if you select the Use the SAP Application Server logical path check box. |
| Data filename prefix | Specify the prefix of the files generated by the SAP system. |
| Specify a shared destination | Select this check box and specify the shared destination in the Shared destination name field displayed. The shared destination allows the SAP components to use the shared destination on the Talend Runtime when they are executed as part of an ESB Route or ESB Data Service within the Talend Runtime container OSGi Environment.  Besides specifying the shared destination name in the component, you also need to setup the SAP DataSource for the Talend Runtime. What you need to do to define the SAP DataSource and how to configure it are described in the readme.txt provided in the Talend ESB package within the /add-ons/datasource/sap folder.  Note that if you use the component's own connection configuration, your SAP connection will be closed at the end of the component. To prevent this from happening, use a shared destination with its name specified. |
| RFC server url | Enter your RFC server URL in the field provided. Talend Studio uses the RFC server as the streaming proxy to support high volume of data extraction without the need to store information on a third-party transfer protocol such as FTP or SFTP.  This field becomes visible when you select Use the RFC server in the Advanced settings view. |
| Package size | Specify the number of records for each package. By default, the value displays 10000. In case you have a value higher than 10000, for example, 12000, Talend Studio creates two packages: one contains 10000 records and the other contains 2000 records.  This field becomes visible when you select Use the RFC server in the Advanced settings view. |
| Connection id | Enter the ID of the connection established by the Talend SAP RFC Server, that is, the name of the SAP connection configuration file (the extension not included). An SAP RFC server can establish multiple SAP connections based on the SAP connection configuration files. By default, the SAP connection configuration files are stored in $TSAPS\_HOME/conf/named-connectiond, where $TSAPS\_HOME is the directory where the Talend SAP RFC Server has been installed. If you cannot find the desired SAP connection configuration file in the default directory, check the directory specified by the named.connections parameter in the tsap-rfc-server.properties file.  This field is available when Use the RFC server is checked in Advanced settings view. |
| Number of threads to extract the data from SAP | Set the number of threads for data extraction. The default is 2. This option is available when you select the Use the RFC server option in the Advanced settings view. |
| Kafka topic partition count | Set the Kafka topic partition count. The default is 2. This option is available when you select the Use the RFC server option in the Advanced settings view. |
| Max time to wait for more data | Set the maximum time period (in seconds) for the client to wait for more data of a Kafka topic when an error occurs. If no data is received when the period expires, the stream will be canceled. The default is 60. This option is available when you select the Use the RFC server option in the Advanced settings view. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Timeout for the generation of the start indicator file (ms) | Specify the time, in milliseconds, to wait for the generation of the start file for SAP batch extraction. This generated file indicates that the data has been successfully extracted to the FTP directory. The default value is 8000 milliseconds. |
| Timeout for the data file polling (ms) | Specify the time, in milliseconds, to wait for the polling of the data files from the FTP server. If you leave this field empty, or set it to `0`, there will be no timeout during file polling. |
| Abort background Job and remove generated files on error | When you select this option, in case the component catches an exception, running background Jobs for the FTP batch extraction will be aborted and the useless files generated on the FTP side will be cleaned. |
| Use the RFC server | Select this check box if you want to directly extract high volumes of data from an SAP application. When you select this option, the Connection configuration section displays the fields for the RFC server url and Package size. For more information, see the corresponding description of those fields in the Basic settings view. |
| Kafka Properties | When you select the Use the RFC server option, the window displays the Kafka Properties table. Kafka, or Apache Kafka, is an open-source distributed streaming platform. For more information about Kafka, refer to <https://kafka.apache.org/>. Enter your Kafka information in the fields provided. |
| Use space to replace the control characters in data | Select this option to replace special characters in data with spaces. Some characters in data (for example, \n) may affect data parsing because they are treated as control characters. This option prevents this by replacing the special characters with spaces. This option is selected by default. |
| SAP Properties | If you need to use custom configuration for the SAP system being used, complete this table with the property or properties to be customized. For example,  * to establish a Unicode connection between the SAP system and Talend Studio, you need to add the property `jco.server.unicode` and set its value to `1`. Note that this property works if you are using SAP Java Connector 2.x and is unnecessary for SAP Java Connector 3.0 and higher versions. * to set up an SAP connection with Secure Network Communications (SNC), you need to add and set the following properties in this field.    + jco.client.snc\_mode   + jco.client.snc\_myname   + jco.client.snc\_lib=.../sapcrypto/sapcrypto.dll   + jco.client.snc\_partnername   + jco.client.snc\_qop Information noteNote: The values of the above properties vary with the system environment. Contact your SAP system administrator if you are not sure how to set the properties.  For more information about setting the SNC parameters, see [Configuring SNC: External Programs to AS ABAP Using RFC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/d9e8a740bbaa4d8f8bee6f7b173bd99f.html) and [Communication Paths that Support SNC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/76128150317a47b6a326e63a17017729.html).  This property is not visible when the Use an existing connection check box is selected. |
| SAP function extraction path | Select this option to specify a directory for the SAP function to generate files that hold the data extracted. You can enter the path to the directory in the text field to the right. If this option is not selected, the files will be generated in the directory specified in the FTP directory field in the Basic settings view.  This option is not available if you select the Use the SAP Application Server logical path check box from the Basic settings view.  Because Talend Studio does not synchronize the directories specified by SAP function extraction path and FTP directory fields, make sure these two fields point to the same resource. |
| Trim spaces | Select this option to trim spaces in data retrieved from SAP servers. You can clear this option in cases where spaces in data are for specific purposes and need to be kept unchanged. This option applies to data that is of STRING type or RAW type only. For data of other types, spaces are trimmed before type conversion.  Information noteNote: This option is available only when you have installed the 8.0.1-R2023-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | The tELTSAPMap component is more commonly used along with the tELTSAPInput component. The name of the link from tELTSAPInput to tELTSAPMap should be same as the table name specified in the Default Table Name field of tELTSAPInput. |
| **Support** | tELTSAPMap should be used to interact with the ERP part of SAP, including S4/HANA. |

**Related concepts**  

* [Aggregating and filtering data in multiple SAP tables](teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-aggregating-and-filtering-data-in-multiple-sap-tables "This example demonstrates how to use the tELTSAPInput and tELTSAPMap components to aggregate data from two SAP tables and filter the columns and rows of data, finally write the filtered data into a local CSV file using a tFileOutputDelimited component.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-aggregating-and-filtering-data-in-multiple-sap-tables -->
# Aggregating and filtering data in multiple SAP tables

Last updated: 9/30/2026

This example demonstrates how to use the tELTSAPInput and
tELTSAPMap components to aggregate data from two SAP tables and
filter the columns and rows of data, finally write the filtered data into a local CSV file
using a tFileOutputDelimited component.

### In this section

* [Creating a Job for aggregating and filtering data in multiple SAP tables](/talend/en-US/components/8.0/sap/teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-creating-job-for-aggregating-and-filtering-data-in-multiple-sap-tables-the)
* [Configuring the Job for aggregating and filtering data in multiple SAP tables](/talend/en-US/components/8.0/sap/teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-configuring-job-for-aggregating-and-filtering-data-in-multiple-sap-tables-click)
* [Executing the Job to aggregate and filter data in multiple SAP tables](/talend/en-US/components/8.0/sap/teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-executing-job-to-aggregate-and-filter-data-in-multiple-sap-tables-press)

**Related reference**  

* [tELTSAPMap](teltsapmap "Builds the SQL SELECT statement using the table schema(s) provided by one or more tELTSAPInput components.")
* [tELTSAPInput](teltsapinput "Provides the SAP table schema that will be used by the tELTSAPMap component to generate the SQL SELECT statement.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-configuring-job-for-aggregating-and-filtering-data-in-multiple-sap-tables-click -->
# Configuring the Job for aggregating and filtering data in multiple SAP tables

Last updated: 9/30/2026

## Procedure

1. Click the tELTSAPMap component and then the
   Component tab to open its Basic
   settings view.
2. Select `Repository` from the Property
   Type drop-down list and click the [...]
   button near to Property Type and in the pop-up dialog box
   select the SAP connection node that has been created in the
   Repository tree view. When done, click
   OK and all SAP connection configuration fields will
   be automatically filled.
3. In the FTP host, FTP port,
   FTP user, FTP password and
   FTP directory fields, enter the FTP connection
   information. The tELTSAPMap component will read all data
   files generated by the SAP system via this FTP connection.
4. In the Data filename prefix field, specify the prefix of
   the files generated by the SAP system.
5. Click the [...] button next to SAP Map
   Editor to open its map editor.
6. On the top left panel, drag and drop the node `LFNINDX` in
   the `ZTAL_VBRK` table onto the node
   `LFNINDX` in the `ZTAL_VBRP` table
   to create an inner join between the two tables.
7. Drag and drop the nodes `MANDT`,
   `LFNINDX`, `VBELN`,
   `FKART`, `FKTYP`,
   `VBTYP`, `WAERK`,
   `VKORG`, `VTWEG` in the
   `ZTAL_VBRK` table on the top left panel onto the
   `out` table on the top right panel, and only the data
   of those columns will be retrieved and written into the output CSV file.
8. Click the Add clause row button on the top right corner
   of the `out` table and then click Add a WHERE
   clause. In the Additional WHERE clauses
   field displayed, enter the clause used to filter the rows of data to be
   retrieved. In this example, it is `ZTAL_VBRK~VKORG = '1000' AND
   ZTAL_VBRK~VTWEG = '10'`, which will filter only the rows of data
   with the value of `VKORG` set to
   `1000` and the value of `VTWEG`
   set to `10`.
9. Click Generated SQL Select query for "" output at the
   bottom and you will see the generated SQL SELECT query used to aggregate and
   filter the data from the two tables.

   When done, click OK to close the map editor.
10. Double-click the tFileOutputDelimited component to open
    its Basic settings view. In the File
    Name field, specify the path to the file into which the
    aggregated and filtered data will be written, `D:/out.csv`
    in this example. Then click the Sync columns button to
    retrieve the schema from its previous component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-creating-job-for-aggregating-and-filtering-data-in-multiple-sap-tables-the -->
# Creating a Job for aggregating and filtering data in multiple SAP tables

Last updated: 9/30/2026

## Before you begin

* The corresponding SAP transport that performs the SAP table join function
  needs to be installed on your SAP system. For more information, see the
  related documentation on how to install a Talend function
  module for SAP.
* The FTP connection has been set up on the SAP server side to allow the
  tELTSAPMap component to download all data files
  generated by the SAP system.
* The connection dedicated to your SAP server has been set up in the
  Repository tree view and the two SAP tables
  `ZTAL_VBRK` and `ZTAL_VBRP` to
  be joined and their schemas have been retrieved and saved under the SAP
  connection node.

## Procedure

1. Create a new Job and add a tELTSAPMap component and a
   tFileOutputDelimited component onto the design
   workspace.
2. Drag and drop the table node `ZTAL_VBRK` in the
   Repository tree view onto the design workspace, in
   the pop-up dialog box, select tELTSAPInput and click
   OK, a tELTSAPInput component
   labeled to `ZTAL_VBRK` will be added.
3. Do the same to drag and drop the table node `ZTAL_VBRP` in
   the Repository tree view onto the design workspace to add
   another tELTSAPInput component labeled to
   `ZTAL_VBRP`.
4. Link the tELTSAPInput component labeled to
   `ZTAL_VBRK` to the tELTSAPMap
   component using a Link > ZTAL\_VBRK (Table) connection.
5. Link the tELTSAPInput component labeled to
   `ZTAL_VBRP` to the tELTSAPMap
   component using a Link > ZTAL\_VBRP (Table) connection.
6. Link the tELTSAPMap component to the
   tFileOutputDelimited component using a Row > \*New Output\* (Main) connection, in the pop-up dialog box, enter the output name
   `out` in the field and click OK.
   The tELTSAPMap component will be linked to the
   tFileOutputDelimited component using a connection
   labeled to `out (Main)`.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/teltsapmap-teltsapinput-tfileoutputdelimited-teltsapinput-tfileoutputdelimited-executing-job-to-aggregate-and-filter-data-in-multiple-sap-tables-press -->
# Executing the Job to aggregate and filter data in multiple SAP tables

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 or click
   Run on the Run tab to execute
   the Job.

   Note that the execution of the Job might take a long time if there is a large
   amount of data in the source tables.
3. Open the generated CSV file to check the filtered data.

   As shown above, only the selected nine columns of data with the value of
   `VKORG` set to `1000` and the
   value of `VTWEG` set to `10` is
   filtered and written into the output CSV file.
