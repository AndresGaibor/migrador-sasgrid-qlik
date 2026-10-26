<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapconnection · versión 8.0 -->
# tSAPConnection

Last updated: 9/30/2026

Commits a whole Job data in one go to the SAP system as one
transaction.

tSAPConnection opens a connection
to the SAP system for the current transaction.

## tSAPConnection Standard properties

These properties are used to configure tSAPConnection running in
the Standard Job framework.

The Standard
tSAPConnection component belongs to the Business family.

The component in this framework is available in all Talend
products.

Information noteNote: When prompted that this component requires
sapjco.jar, download the module and refer to the instructions at
[SAP Java Connector](https://support.sap.com/en/product/connectors/jco.html).

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository. * Built-in: No property data is stored   centrally. * Repository: Select the Repository file   where Properties are stored. The fields that follow are pre-filled in using   fetched data. |
| SAP API Version | Select a version from the drop-down list:  * talend sap api: a custom business layer above the   SAP JCO driver. * sap jco 3.\* (Deprecated): a driver that enables   Talend Studio to communicate with the SAP system through SAP's RFC protocol.  Note that the opened SAP connection can be reused by tSAPBapi and tSAPTableInput only if talend sap api is selected.  Information noteDeprecation: sap jco 3.\* is deprecated when you have installed the 8.0.1-R2022-05 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Connection configuration | Client type: enter your usual SAP connection.  Userid : enter user login.  Password: enter password.  Language: specify the language.  Host name: enter the IP address of the SAP system.  System number: enter the system number.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Specify a shared destination | Select this check box and specify the shared destination in the Shared destination name field displayed. The shared destination allows the SAP components to use the shared destination on the Talend Runtime when they are executed as part of an ESB Route or ESB Data Service within the Talend Runtime container OSGi Environment.  Besides specifying the shared destination name in the component, you also need to setup the SAP DataSource for the Talend Runtime. What you need to do to define the SAP DataSource and how to configure it are described in the readme.txt provided in the Talend ESB package within the /add-ons/datasource/sap folder.  Note that if you use the component's own connection configuration, your SAP connection will be closed at the end of the component. To prevent this from happening, use a shared destination with its name specified. |
| SAP Properties | If you need to use custom configuration for the SAP system being used, complete this table with the property or properties to be customized. For example,  * to establish a Unicode connection between the SAP system and Talend Studio, you need to add the property `jco.server.unicode` and set its value to `1`. Note that this property works if you are using SAP Java Connector 2.x and is unnecessary for SAP Java Connector 3.0 and higher versions. * to set up an SAP connection with Secure Network Communications (SNC), you need to add and set the following properties in this field.    + jco.client.snc\_mode   + jco.client.snc\_myname   + jco.client.snc\_lib=.../sapcrypto/sapcrypto.dll   + jco.client.snc\_partnername   + jco.client.snc\_qop Information noteNote: The values of the above properties vary with the system environment. Contact your SAP system administrator if you are not sure how to set the properties.  For more information about setting the SNC parameters, see [Configuring SNC: External Programs to AS ABAP Using RFC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/d9e8a740bbaa4d8f8bee6f7b173bd99f.html) and [Communication Paths that Support SNC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/76128150317a47b6a326e63a17017729.html).  This property is not visible when the Use an existing connection check box is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| ftp and http based programs | To invoke from the SAP server a function which requires document downloading, select this check box and make sure that SAPGUI has been installed with the SAP system.  If this check box is selected but SAPGUI has not been installed, errors will occur.  This check box will not be available if you select Use an existing connection check box in the Basic settings tab. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tSAP\* components, especially with the tSAPCommit and tSAPRollback components. |
| **Support** | tSAPConnection should be used to interact with the ERP part of SAP, including S4/HANA. |
| Limitation | Specific JAR and DLL files provided by SAP must be added to Talend Studio and the workstation hosting Talend Studio. The exact procedure varies among platforms such as 32-bit or 64-bit Windows or Linux.  * For more information, see [How to install the SAP Java   Connector](/talend/r/en-US/8.0/components/sap/installing-sap-jco) and [Centralizing SAP metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-sap-metadata). |

**Related concepts**  

* [Extracting Data using tSAPInfoCubeInput](tsapinfocubeinput-tsapconnection-tfileoutputdelimited-tlogrow-extracting-data-using-tsapinfocubeinput-about "You can retrieve data from an SAP application table using the tSAPInfoCubeInput component.")
