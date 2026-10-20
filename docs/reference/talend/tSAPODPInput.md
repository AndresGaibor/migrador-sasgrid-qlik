<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapodpinput · versión 8.0 -->
# tSAPODPInput

Last updated: 9/30/2026

Extracts business data from the ERP part of SAP (SAP Business application, SAP on
HANA, SAP R/3, and S4/HANA) through ODP (Operational Data Provisioning).

## tSAPODPInput Standard properties

These properties are used to configure tSAPODPInput running in the Standard Job framework.

The Standard
tSAPODPInput component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: When prompted that this component requires
sapjco.jar, download the module and refer to the instructions at
[SAP Java Connector](https://support.sap.com/en/product/connectors/jco.html).

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and from the Connection configuration drop-down list displayed, select the component in which the relevant reused database connection is configured.  When a Job contains a parent Job and a child Job, the list displayed presents only the connection components in the same Job level. |
| Server Type | Select the type of the SAP server to be connected, either Application Server or Message Server. |
| Client | The SAP system client ID. |
| UserId and Password | The user connection ID and password.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Language | The language of the SAP system. |
| Host name | The name or IP address of the host on which the SAP server is running. |
| System number | The SAP system number.  This property is available only when Application Server is selected from the Server Type drop-down list. |
| System ID | The SAP system ID.  This property is available only when Message Server is selected from the Server Type drop-down list. |
| Group Name | The SAP group name.  This property is available only when Message Server is selected from the Server Type drop-down list. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Service name | The name of the operational delta queue. For more information, see [Introduction to Operational Delta Queues](https://wiki.scn.sap.com/wiki/display/BI/Introduction+to+Operational+Delta+Queues#IntroductiontoOperationalDeltaQueues-TheOperationalDeltaQueue(ODQ)). |
| Subscriber name | The name of the subscriber that consumes data from SAP. |
| Subscriber process name | The name of the subscriber process. |
| Execute a full extraction | Select this check box to perform a full extraction to retrieve all data from an SAP system. By default, this check box is cleared and a delta extraction will be performed to retrieve only changed data. |
| Reset subscriber | Select this check box to reset the subscriber to make an initial load. |
| Selection Group | Specify the search condition(s) used to filter data to be retrieved by clicking the [+] button to add as many rows as needed, each row for a search condition, and set the value of the following attributes for each condition.  Information noteNote: This component retrieves the data records that meet all the conditions set in this field.   * Column: enter the name of the schema column based on which retrieved data will be filtered. * Sign: select either `Include` or `Exclude` from the drop-down list.    + `Include`: the data that meets the condition will be retrieved.   + `Exclude`: the data that doesn't meet the condition will be retrieved. * Operator: select from the drop-down list the data filter operator used to build the search condition. * Value: specify the search value used to build the search condition. Note that wildcard characters are not supported. * High value: specify another search value used to build the search condition for the Between operator.  When using a column of Date type to specify a filter, the date and time values in the Value and High Value columns should be in the format `yyyyMMdd` and `HHMMSS`, which might be different from the format defined in the schema editor. Note that wildcard characters are not supported.   Information noteNote: The Contains pattern operator in the drop-down list of the Operator column is for future extension. |
| Specify a shared destination | Select this check box and specify the shared destination in the Shared destination name field displayed. The shared destination allows the SAP components to use the shared destination on the Talend Runtime when they are executed as part of an ESB Route or ESB Data Service within the Talend Runtime container OSGi Environment.  Besides specifying the shared destination name in the component, you also need to setup the SAP DataSource for the Talend Runtime. What you need to do to define the SAP DataSource and how to configure it are described in the readme.txt provided in the Talend ESB package within the /add-ons/datasource/sap folder.  Note that if you use the component's own connection configuration, your SAP connection will be closed at the end of the component. To prevent this from happening, use a shared destination with its name specified. |
| Use FTP-Batch Options | Select this check box when the size of data to be retrieved is larger than the size specified in the Fetch size field. With this check box selected, the SAP system will generate as many files as needed and write the retrieved data into these files, and this component will then read the files using an FTP connection to retrieve data and transfer the retrieved data to the output component. The following properties need to be specified when this checkbox is selected:   * File Protocol: Select FTP or the secure alternative   SFTP. * Host: The IP address or host name of the FTP   server. * Port: The listening port number of the FTP   server. * User and Password: The user   authentication data required to access the FTP server. * Use the SAP Application Server logical path: The   logical path configured in the SAP Application Server which specify in which   directory the flat files must be created. This option is available only when   you have installed the 8.0.1-R2023-02 Talend Studio Monthly update or a later one delivered by Talend. * Directory: The directory where the files generated by   the SAP system will be saved.  This option is not available if you select the Use the SAP   Application Server logical path check box. * Data filename prefix: The prefix of the files   generated by the SAP system. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Timeout for the generation of the start indicator file (ms) | Specify the time, in milliseconds, to wait for the generation of the start file for SAP batch extraction. This generated file indicates that the data has been successfully extracted to the FTP directory. The default value is 8000 milliseconds. |
| Fetch size | Enter the maximum size of the resultset (in number of rows) that can be returned from the SAP BW database in response to a BAPI call or a request. A value of `-1`, the default, uses the default fetch size, which is determined by the Java code or the BAPI on SAP side.  It is recommended to set this field according to the memory space allocated to your Job and the number of fields requested. With a given memory space, the more fields requested, the smaller the fetch size. |
| SAP Properties | If you need to use custom configuration for the SAP system being used, complete this table with the property or properties to be customized. For example,  * to establish a Unicode connection between the SAP system and Talend Studio, you need to add the property `jco.server.unicode` and set its value to `1`. Note that this property works if you are using SAP Java Connector 2.x and is unnecessary for SAP Java Connector 3.0 and higher versions. * to set up an SAP connection with Secure Network Communications (SNC), you need to add and set the following properties in this field.    + jco.client.snc\_mode   + jco.client.snc\_myname   + jco.client.snc\_lib=.../sapcrypto/sapcrypto.dll   + jco.client.snc\_partnername   + jco.client.snc\_qop Information noteNote: The values of the above properties vary with the system environment. Contact your SAP system administrator if you are not sure how to set the properties.  For more information about setting the SNC parameters, see [Configuring SNC: External Programs to AS ABAP Using RFC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/d9e8a740bbaa4d8f8bee6f7b173bd99f.html) and [Communication Paths that Support SNC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/76128150317a47b6a326e63a17017729.html).  This property is not visible when the Use an existing connection check box is selected. |
| SAP function extraction path | Select this option to specify a directory for the SAP function to generate files that hold the data extracted. You can enter the path to the directory in the text field to the right. If this option is not selected, the files will be generated in the directory specified in the FTP directory field in the Basic settings view.  This option is available when you select the Use FTP-Batch Options option in the Basic settings view. This option is not available if you select the Use the SAP Application Server logical path check box from the Basic settings view.  Because Talend Studio does not synchronize the directories specified by SAP function extraction path and FTP directory fields, make sure these two fields point to the same resource. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as a start component of a Job or subJob and it always needs an output link. |
| Limitation | Specific JAR and DLL files provided by SAP must be added to Talend Studio and the workstation hosting Talend Studio. The exact procedure varies among platforms such as 32-bit or 64-bit Windows or Linux.  * For more information, see [How to install the SAP Java   Connector](/talend/r/en-US/8.0/components/sap/installing-sap-jco) and [Centralizing SAP metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-sap-metadata). |
| **Support** | You can use tSAPODPInput to interact with SAP S4/HANA. |

**Related concepts**  

* [Retrieving data from SAP through ODP](creating-job-for-retrieving-data-from-sap-through-odp "Here is an example of using Talend components to retrieve data from SAP through ODP (Operational Data Provisioning).")
