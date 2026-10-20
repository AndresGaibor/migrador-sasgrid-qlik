<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapinfoobjectinput · versión 8.0 -->
# tSAPInfoObjectInput

Last updated: 9/30/2026

Retrieves InfoObject data from an SAP BW system.

## tSAPInfoObjectInput Standard properties

These properties are used to configure tSAPInfoObjectInput running in the Standard Job framework.

The Standard
tSAPInfoObjectInput component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and from the list displayed select the relevant connection component to reuse the connection details you have already defined.  When a Job contains a parent Job and a child Job, the list displayed presents only the connection components in the same Job level. |
| Server Type | Select the type of the SAP server to be connected, either Application Server or Message Server. |
| Client | The SAP system client ID. |
| UserId and Password | The user connection ID and password.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Language | The language of the SAP system. |
| Host name | The name or IP address of the host on which the SAP server is running. |
| System number | The SAP system number.  This property is available only when Application Server is selected from the Server Type drop-down list. |
| System ID | The SAP system ID.  This property is available only when Message Server is selected from the Server Type drop-down list. |
| Group Name | The SAP group name.  This property is available only when Message Server is selected from the Server Type drop-down list. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table | Enter the name of the table from which the data will be retrieved. |
| Info object type | Select the type of the InfoObject data to be retrieved. |
| Specify a shared destination | Select this check box and specify the shared destination in the Shared destination name field displayed. The shared destination allows the SAP components to use the shared destination on the Talend Runtime when they are executed as part of an ESB Route or ESB Data Service within the Talend Runtime container OSGi Environment.  Besides specifying the shared destination name in the component, you also need to setup the SAP DataSource for the Talend Runtime. What you need to do to define the SAP DataSource and how to configure it are described in the readme.txt provided in the Talend ESB package within the /add-ons/datasource/sap folder.  Note that if you use the component's own connection configuration, your SAP connection will be closed at the end of the component. To prevent this from happening, use a shared destination with its name specified. |

## Advanced settings

| Properties | Description |
| --- | --- |
| SAP Properties | If you need to use custom configuration for the SAP system being used, complete this table with the property or properties to be customized. For example,  * to establish a Unicode connection between the SAP system and Talend Studio, you need to add the property `jco.server.unicode` and set its value to `1`. Note that this property works if you are using SAP Java Connector 2.x and is unnecessary for SAP Java Connector 3.0 and higher versions. * to set up an SAP connection with Secure Network Communications (SNC), you need to add and set the following properties in this field.    + jco.client.snc\_mode   + jco.client.snc\_myname   + jco.client.snc\_lib=.../sapcrypto/sapcrypto.dll   + jco.client.snc\_partnername   + jco.client.snc\_qop Information noteNote: The values of the above properties vary with the system environment. Contact your SAP system administrator if you are not sure how to set the properties.  For more information about setting the SNC parameters, see [Configuring SNC: External Programs to AS ABAP Using RFC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/d9e8a740bbaa4d8f8bee6f7b173bd99f.html) and [Communication Paths that Support SNC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/76128150317a47b6a326e63a17017729.html).  This property is not visible when the Use an existing connection check box is selected. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component of a Job or subJob and it always needs an output link. |
| Limitation | Specific JAR and DLL files provided by SAP must be added to Talend Studio and the workstation hosting Talend Studio. The exact procedure varies among platforms such as 32-bit or 64-bit Windows or Linux.  * For more information, see [How to install the SAP Java   Connector](/talend/r/en-US/8.0/components/sap/installing-sap-jco) and [Centralizing SAP metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-sap-metadata). |
