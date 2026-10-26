<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapdatasourcereceiver · versión 8.0 -->
# tSAPDataSourceReceiver

Last updated: 9/30/2026

Retrieves data requests stored on the Talend SAP RFC Server and
related to a specific Data Source system.

tSAPDataSourceReceiver connects to the Talend SAP RFC Server, which
acts as a bridge between Talend Studio and an
SAP server, and retrieves data requests stored on the RFC server and related to a specific
Data Source system, then the data requests can be processed later on by Talend Job to
retrieve data from the Data Source system.

## tSAPDataSourceReceiver Standard properties

These properties are used to configure tSAPDataSourceReceiver running in the Standard Job framework.

The Standard
tSAPDataSourceReceiver component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Failover | Select this option to use the RFC server failover feature. The RFC server failover feature is implemented by deploying brokers using the rfc.server.remote.broker.url parameter in Remote broker section of the tsap-rfc-server.properties file. After selecting this option, you need to provide the IP addresses and the port numbers of the brokers in the Host and Port columns in the table that appears. You can find the IP addresses and the port numbers of the brokers by checking the rfc.server.remote.broker.url parameter in Remote broker section of the tsap-rfc-server.properties file. See Configuring the tsap-rfc-server.properties file for related information. |
| Talend SAP RFC Server host | Enter the IP address of the Talend SAP RFC Server, or `localhost` if it is installed on your local machine. |
| Port | Enter the port used by the Talend SAP RFC Server. |
| User and Password | Enter the username and password used to connect to the Talend SAP RFC Server.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use SSL Transport | Select this check box to use the SSL transport mechanism. For more information about SSL transport, see [SSL Transport Reference](http://activemq.apache.org/ssl-transport-reference.html). |
| Datasource name | Specify the name of the Data Source system. |
| Mode | Select one of the following modes for using this component from the drop-down list.  * Keep running forever:   Select this mode if you want this component to keep   listening for the coming data requests until you stop the   execution of the Job. With this mode selected, you can also   specify the following two properties:   + Maximum duration     (seconds): Specify the period of time     (in seconds) for which the Job should continue to     consume any data requests on the RFC Server. Once     this time limit is reached, the Job stops     consuming and closes the connection to the RFC     Server.   + Maximum number of data     to consume: Specify the maximum number     of data requests to be consumed by the Job. Once     this limit is reached, the Job stops consuming and     closes the connection to the RFC Server. * Batch (consume all data available   then terminate): Select this mode if you want   the Job to stop automatically once all data requests   available on the RFC server are consumed. With this mode   selected, you can also specify in the Sleep time (seconds) field the sleeping   time, in seconds, which corresponds to the time the process   will wait for the first message to be read. |
| Queue/Topic name prefix | Enter the prefix for the JMS queue or topic name used to receive BW Datasource messages from the RFC Server. The value must match the jms.datasource.queue.prefix property set in the tsap-rfc-server.properties file. The default value is `TALEND.DATASOURCES.`  This field is available from the 8.0.1-R2026-08 monthly release. To use this feature, both Talend Studio and Talend SAP RFC Server must be updated to R2026-08 or later. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |

## Advanced settings

| Properties | Description |
| --- | --- |
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

**Related concepts**  

* [Consuming Data Source objects using SSL Transport](tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-consuming-data-source-objects-using-ssl-transport-standard-component-enterprise-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-consuming-data-source-objects-using-ssl-transport-standard-component-enterprise-the -->
# Consuming Data Source objects using SSL Transport

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

The following scenario creates a three-component Job that connects to the
Talend SAP RFC Server
to consume Data Source objects using SSL Transport and display them on the console.

Prerequisites:

Talend SAP RFC Server
needs to be running and the SSL transport mechanism has been enabled for it. For more
information about how to install and configure the Talend SAP RFC Server, see
[Configure an SAP RFC server](/talend/r/en-US/Cloud/installation-guide-linux/configuring-rfc-server).

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/sap/tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-adding-and-linking-components-standard-component-enterprise-create)
* [Configuring the components](/talend/en-US/components/8.0/sap/tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-configuring-components-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/sap/tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-saving-and-executing-job-standard-component-enterprise-press)

**Related reference**  

* [tSAPDataSourceReceiver](tsapdatasourcereceiver "Retrieves data requests stored on the Talend SAP RFC Server and related to a specific Data Source system.")

**Related information**  

* [tSetKeystore](/talend/en-US/components/8.0/keystore/tsetkeystore)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-adding-and-linking-components-standard-component-enterprise-create -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tSetKeystore
   component, a tSAPDataSourceReceiver component,
   and a tLogRow component by typing their names
   on the design workspace or dropping them from the Palette.
2. Connect the tSAPDataSourceReceiver component
   to the tLogRow component using a Row > Main
   connection.
3. Connect the tSetKeystore component to the
   tSAPDataSourceReceiver component using a
   Trigger > On
   Subjob Ok connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tSetKeystore component to
   open its Basic settings view.
2. In the TrustStore file field, specify the
   path to the key store for SSL. In this example, it is *D:/Talend/myclient.ks*.

   In the TrustStore password field, specify the
   password for the key store for SSL.
3. Double-click the tSAPDataSourceReceiver
   component to open its Basic settings
   view.
4. In the Talend SAP RFC Server
   host and Port fields, enter the
   IP address of the Talend SAP RFC Server to
   be connected and the port used by the server.

   In the User and Password fields, enter the user authentication
   information if the user authentication feature has been enabled for the Talend SAP RFC Server to
   be connected. For more information, see [Configure an SAP RFC server](/talend/r/en-US/Cloud/installation-guide-linux/configuring-rfc-server).
5. In the Datasource name field, enter the name of the Data
   Source whose objects you want to be consumed. In this exmaple, it is *TDS*.
6. In the Mode drop-down list, select Batch (consume all data available then terminate) to
   consume all objects of the specified Data Source on the server.
7. Double-click the tLogRow component to open
   its Basic settings view.
8. In the Mode area, select Table (print values in cells of a table) for better
   readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapdatasourcereceiver-tsetkeystore-tlogrow-tlogrow-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 or click Run on
   the Run tab to run the Job.

   As shown above, one data source object available is consumed and displayed on
   the console.
