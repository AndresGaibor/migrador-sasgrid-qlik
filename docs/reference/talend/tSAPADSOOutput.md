<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapadsooutput · versión 8.0 -->
# tSAPADSOOutput

Last updated: 9/30/2026

Writes data to an active Advanced Data Store Object (ADSO) through SAP Java
Connector version 3. Note that data written by this component is actually staged in SAP and
needs to be activated for being retrieved by tSAPADSOInput.

## tSAPADSOOutput Standard properties

These properties are used to configure tSAPADSOOutput running in
the Standard Job framework.

The Standard
tSAPADSOOutput component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote:

* This component is available only when you have installed the 8.0.1-R2022-04 Talend Studio
  Monthly update or a later one delivered by Talend.
  For more information, check with your administrator.
* When prompted that this component requires
  sapjco.jar, download the module and refer to the instructions at
  [SAP Java Connector](https://support.sap.com/en/product/connectors/jco.html).

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and from the Connection configuration drop-down list displayed, select the component in which the relevant reused database connection is configured.  When a Job contains a parent Job and a child Job, the list displayed presents only the connection components in the same Job level. |
| Server Type | Select the type of the SAP server to be connected, either Application Server or Message Server. |
| Client | The SAP system client ID. |
| UserId and Password | The user connection ID and password.  To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Language | The language of the SAP system. |
| Host name | The name or IP address of the host on which the SAP server is running. |
| System number | The SAP system number.  This option is available when Application Server is selected from the Server Type drop-down list. |
| System ID | The SAP system ID.  This field is available when Message Server is selected from the Server Type drop-down list. |
| Group Name | The SAP group name.  This field is available when Message Server is selected from the Server Type drop-down list. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| ADSO name | The name of the active Advanced Data Store Object to write data to. |
| Batch size | The maximum number of records allowed to be written to the active Advanced Data Store Object in one batch. |
| Specify a shared destination | Select this check box and specify the shared destination in the Shared destination name field displayed. The shared destination allows the SAP components to use the shared destination on the Talend Runtime when they are executed as part of an ESB Route or ESB Data Service within the Talend Runtime container OSGi Environment.  Besides specifying the shared destination name in the component, you also need to setup the SAP DataSource for the Talend Runtime. What you need to do to define the SAP DataSource and how to configure it are described in the readme.txt provided in the Talend ESB package in the /add-ons/datasource/sap folder.  Note that if you use the component's own connection configuration, your SAP connection will be closed at the end of the component. To prevent this from happening, use a shared destination with its name specified. |

## Advanced settings

| Properties | Description |
| --- | --- |
| SAP Properties | If you need to use custom configuration for the SAP system being used, complete this table with the property or properties to be customized. For example, to set up an SAP connection with Secure Network Communications (SNC), you need to add and set the following properties in this field.  * jco.client.snc\_mode * jco.client.snc\_myname * jco.client.snc\_lib=.../sapcrypto/sapcrypto.dll * jco.client.snc\_partnername * jco.client.snc\_qop  Information noteNote: The values of the above properties vary with the system environment. Contact your SAP system administrator if you are not sure how to set the properties.  If you are using the 8.0.1-R2024-01 monthly update or a previous one, to enable support for SAP BW on HANA, you need to install the CB4K900207.zip transport and set the api.use\_bw\_on\_hana property to true. Note that currently, ADSO field only supports data that is of Character and Date types. See [SAP function modules shipped with Talend Studio](/talend/en-US/components/8.0/sap/sap-function-modules-shipped-with-talend-studio) for information about the CB4K900207.zip transport.  If you are using the 8.0.1-R2024-02 monthly update or a later one, to enable support for SAP BW on HANA, you need to install the DHBK900344.zip transport and the S4HK902231.zip deletion-transport. Note that more data types are supported, but there is a limitation when writing dynamic length fields STRING and SSTRING. Only the default max string length of 1000 is supported.  SAP Business Warehouse powered by HANA (referred to as BW on HANA or BWoH) and SAP BW/4HANA are two application suites running on SAP HANA. BW on HANA is an SAP tool built on HANA database for data modeling, warehousing, and reporting. It runs on HANA database and therefore is simpler and faster. You can use BW on HANA through two ABAP function modules: Z\_TLDBI\_GET\_ADSO and Z\_TLDBI\_GET\_ADSO\_DETAIL. See [SAP function modules shipped with Talend Studio](/talend/en-US/components/8.0/sap/sap-function-modules-shipped-with-talend-studio) for related information.  BW/4HANA is a data warehouse solution with agile and flexible data modeling. It provides processes and user interfaces highly optimized for the SAP HANA platform. It only requires standard SAP functions.  Information noteNote: The support for SAP BW on HANA is available when you have installed the 8.0.1-R2022-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For more information about setting the SNC parameters, see [Configuring SNC: External Programs to AS ABAP Using RFC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/d9e8a740bbaa4d8f8bee6f7b173bd99f.html) and [Communication Paths that Support SNC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/76128150317a47b6a326e63a17017729.html). |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as an end component of a Job or subJob and it always needs an input link. |
