<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi · versión 8.0 -->
# tSAPBapi

Last updated: 9/30/2026

Extracts data from or loads data to an SAP server using multiple input/output
parameters or the document type parameter.

tSAPBapi connects to an SAP server and calls a BAPI function to extract
data from or load data to the SAP server.

## tSAPBapi Standard properties

These properties are used to configure
tSAPBapi running in the Standard Job framework.

The Standard
tSAPBapi
component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: When prompted that this component requires
sapjco.jar, download the module and refer to the instructions at
[SAP Java Connector](https://support.sap.com/en/product/connectors/jco.html).

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | * Either Built-in or Repository. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Use an existing connection | Select this check box and from the list displayed select the relevant connection component to reuse the connection details you have already defined.  When a Job contains a parent Job and a child Job, the list displayed presents only the connection components in the same Job level. |
| Server Type | Select the type of the server to be connected, either Application Server or Message Server. |
| Client | Specify the SAP system client ID. |
| UserId and Password | Specify the user connection ID and password.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Language | Specify the language of the SAP system. |
| Host name | Enter the name or IP address of the host on which the SAP server is running. |
| System number | Enter the system number.  This field appears only when Application Server is selected from the Server Type drop-down list. |
| System ID | Enter the system ID.  This field appears only when Message Server is selected from the Server Type drop-down list. |
| Group Name | Enter the group name.  This field appears only when Message Server is selected from the Server Type drop-down list. |
| SAP Function | Specify the name of the BAPI function to be called. |
| tick it to enable multiple input/output;not tick it to enable document | Select this check box to use multiple input and output parameters when calling the SAP function.  Clear this check box to use the document type input and output parameters when calling the SAP function. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   The Schema list and the Edit schema button appear only when the tick it to enable multiple input/output;not tick it to enable document check box is cleared. |
| Input | Click the [+] button below the table to add as many rows as needed, each row for an input parameter, and set the following attributes for each input parameter:   * Name: Enter the input parameter   name between double quotation marks. * Type: Click the cell and select   an input parameter type Single, Structure, or   Table from the drop-down list. * Schema: Select the cell and   click the [...] button in the cell to open the schema   editor to define the input parameter's schema. For the input   parameter of Single or Structure type, the value for   each column is defined in the Value column in the schema   editor. * Source Row: For the input   parameter of Table type, click the cell and from the   drop-down list select an incoming link through which the input   data for the parameter is transferred. * Changing: select this check box   if the input parameter is a changing parameter.   This table appears only when the tick it to enable multiple input/output;not tick it to enable document check box is selected. |
| Output | Click the [+] button below the table to add as many rows as needed, each row for an output parameter, and set the following attributes for each output parameter:   * Name: Enter the output   parameter name between double quotation marks. * Type: Click the cell and select   the output parameter type Single, Structure, or   Table from the drop-down list. * Schema: Select the cell and   click the [...] button in the cell to open the schema   editor to define the output parameter's schema.   This table appears only when the tick it to enable multiple input/output;not tick it to enable document check box is selected. |
| Die on error | Select this option to stop the execution of the Job when an error occurs to the component.  If this option is not selected, errors occur to the component are logged and the Job continues.  By default, this option is not selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| SAP Properties | If you need to use custom configuration for the SAP system being used, complete this table with the property or properties to be customized. For example,  * to establish a Unicode connection between the SAP system and Talend Studio, you need to add the property `jco.server.unicode` and set its value to `1`. Note that this property works if you are using SAP Java Connector 2.x and is unnecessary for SAP Java Connector 3.0 and higher versions. * to set up an SAP connection with Secure Network Communications (SNC), you need to add and set the following properties in this field.    + jco.client.snc\_mode   + jco.client.snc\_myname   + jco.client.snc\_lib=.../sapcrypto/sapcrypto.dll   + jco.client.snc\_partnername   + jco.client.snc\_qop Information noteNote: The values of the above properties vary with the system environment. Contact your SAP system administrator if you are not sure how to set the properties.  For more information about setting the SNC parameters, see [Configuring SNC: External Programs to AS ABAP Using RFC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/d9e8a740bbaa4d8f8bee6f7b173bd99f.html) and [Communication Paths that Support SNC](https://help.sap.com/viewer/10977ac76c531014a966b3f130d4f853/7.0.36/en-US/76128150317a47b6a326e63a17017729.html).  This property is not visible when the Use an existing connection check box is selected. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component together with other output component(s) or an intermediate component together with other input and output components. |
| **Support** | tSAPBapi should be used to interact with the ERP part of SAP, including S4/HANA. |
| Connections | * Outgoing links (from this component to another):   + Row: Main   + Trigger: On Subjob Ok, On Subjob     Error * Incoming links   (from one component to this one):    + Row: Main, Iterate   + Trigger: On Subjob Ok, On Subjob Error,     On ComponentOK, On Component Error   For further information about connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Limitation | Specific JAR and DLL files provided by SAP must be added to Talend Studio and the workstation hosting Talend Studio. The exact procedure varies among platforms such as 32-bit or 64-bit Windows or Linux.  * For more information, see [How to install the SAP Java   Connector](/talend/r/en-US/8.0/components/sap/installing-sap-jco) and [Centralizing SAP metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-sap-metadata). |

**Related concepts**  

* [Retrieving data from an SAP system by calling a BAPI function using document type parameters](tsapbapi-txmlmap-tlogrow-tfixedflowinput-retrieving-data-from-sap-system-by-calling-bapi-function-using-document-type-parameters-standard-component-enterprise-this)
* [Retrieving data from an SAP system by calling a BAPI function using multiple input/output parameters](tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-retrieving-data-from-sap-system-by-calling-bapi-function-using-multiple-input-output-parameters-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-retrieving-data-from-sap-system-by-calling-bapi-function-using-multiple-input-output-parameters-standard-component-enterprise-this -->
# Retrieving data from an SAP system by calling a BAPI function using multiple input/output parameters

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

This scenario describes a Job that retrieves data from a table named *VBRK* in an SAP system by calling the BAPI function *RFC\_READ\_TABLE* with multiple input and output parameters
defined.

Prerequisites:

An SAP connection has been set up in the Repository tree view, with the *RFC\_READ\_TABLE*
function and *VBRK* table retrieved. For more information about how to
set up an SAP connection and retrieve SAP functions and tables, see [Centralizing SAP metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-sap-metadata).

### In this section

* [Adding and linking components](/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-adding-and-linking-components-standard-component-enterprise-create)
* [Configuring the components](/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-components-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-saving-and-executing-job-standard-component-enterprise-press)

**Related reference**  

* [tSAPBapi](tsapbapi "Extracts data from or loads data to an SAP server using multiple input/output parameters or the document type parameter.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-retrieving-data-from-sap-system-by-calling-bapi-function-using-document-type-parameters-standard-component-enterprise-this -->
# Retrieving data from an SAP system by calling a BAPI function using document type parameters

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

This scenario describes a Job that retrieves data from a table named *SFLIGHT* in an SAP system by calling the BAPI function *RFC\_READ\_TABLE* with defined input and output parameters of
type Document.

Prerequisites:

The SAP connection has been set up in the Repository
tree view, with

* the *RFC\_READ\_TABLE* function retrieved
  and saved under the SAP Bapi folder of the
  SAP connection,
* and the XML metadata for the input and output schemas of the *RFC\_READ\_TABLE* function retrieved and saved
  under the File xml node.

For more information about how to set up an SAP connection and retrieve SAP
functions and SAP function schemas as XML metadata, see [Managing metadata in Talend Studio](/talend/r/en-US/8.0/studio-user-guide/managing-metadata-in-studio).

### In this section

* [Adding the components](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-adding-components-standard-component-enterprise-create)
* [Configuring the components](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-components-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-saving-and-executing-job-standard-component-enterprise-press)

**Related reference**  

* [tSAPBapi](tsapbapi "Extracts data from or loads data to an SAP server using multiple input/output parameters or the document type parameter.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-adding-and-linking-components-standard-component-enterprise-create -->
# Adding and linking components

Last updated: 9/30/2026

## Procedure

1. Create a Job and drop the node *RFC\_READ\_TABLE* in the
   SAP Bapi folder of the SAP connection
   onto the design workspace as a tSAPBapi
   component to reuse the connection to the SAP system and the input and output
   schemas of the SAP function *RFC\_READ\_TABLE*.
2. Add the following components to the Job by typing theirs names in the
   design workspace or dropping them from the Palette: 
   * two tFixedFlowInput components: to generate two input
     data flows for the *FIELDS* and
     *OPTIONS* input parameters of
     table type respectively.

     Note that there is no input data flow for the *DATA*
     input parameter of table type, since it does not need an input value
     in this example.
   * three tLogRow components: to display the output data
     corresponding to the *DATA*,
     *FIELDS*, and *OPTIONS* output parameters
     respectively.
3. Connect the first tFixedFlowInput to tSAPBapi using a Row > Main
   connection.
4. Connect the second tFixedFlowInput to tSAPBapi using a Row > Main
   connection.
5. Connect tSAPBapi to the first tLogRow using the Row >
   row\_DATA\_1 connection.
6. Connect tSAPBapi to the second tLogRow using the Row >
   row\_FIELDS\_1 connection.
7. Connect tSAPBapi to the third tLogRow using the Row >
   row\_OPTIONS\_1 connection.
8. Label the components to better identify their roles in the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Configuring the input components](/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-input-components-standard-component-enterprise)
* [Configuring the tSAPBapi component](/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-tsapbapi-component-standard-component-enterprise)
* [Configuring the output components](/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-output-components-standard-component-enterprise)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, ten rows of data from the *VBRK* table
   is retrieved and displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-adding-components-standard-component-enterprise-create -->
# Adding the components

Last updated: 9/30/2026

## Procedure

1. Create a Job and drop the node *RFC\_READ\_TABLE* in the
   SAP Bapi folder of the SAP connection
   onto the design workspace as a tSAPBapi
   component to reuse the connection to the SAP system.
2. Add the following components to the Job by typing theirs names in the
   design workspace or dropping them from the Palette: 
   * a tFixedFlowInput component: to
     generate the input data flow.
   * two tXMLMap components: to map and transform the input
     and output data flows respectively.
   * three tLogRow components: to display the output data
     corresponding to the *DATA*,
     *FIELDS*, and *OPTIONS* output parameters
     respectively.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Configuring the input component](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-input-component-standard-component-enterprise)
* [Configuring the tSAPBapi component](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-tsapbapi-component-standard-component-enterprise)
* [Mapping the input data flow](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-mapping-input-data-flow-standard-component-enterprise)
* [Mapping the output data flow](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-mapping-output-data-flow-standard-component-enterprise)
* [Configuring the output components](/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-output-components-standard-component-enterprise)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, ten rows of data from the *SFLIGHT*
   table is retrieved and displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-input-components-standard-component-enterprise -->
# Configuring the input components

Last updated: 9/30/2026

## Procedure

1. Double-click the first tFixedFlowInput to
   open its Basic settings view on the
   Component tab.
2. Select Repository from the Schema drop-down list and click the [...] button next to it to open the Repository Content dialog box.
3. Select the schema of the *FIELDS* input parameter from
   the Repository Content dialog box, then
   click OK to close the dialog box and
   propagate the schema to the next component.
4. In the Mode area, select Use
   Inline Content(delimited file) and then enter the following
   input data for the *FIELDS* input parameter
   in the Content field.

   ```
   MANDT;000000;000003;C;Client
   VBELN;000003;000010;C;Billing document
   ```
5. Double-click the second tFixedFlowInput
   to open its Basic settings view on the
   Component tab.
6. Select Repository from the Schema drop-down list and click the [...] button next to it to open the Repository Content dialog box.
7. Select the schema of the *OPTIONS* input parameter from
   the Repository Content dialog box, then
   click OK to close the dialog box and
   propagate the schema to the next component.
8. In the Mode area, select the Use
   Single Table option, and enter the value of the parameter in
   the Value field. In this example, it is
   *MANDT = '800'*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-output-components-standard-component-enterprise -->
# Configuring the output components

Last updated: 9/30/2026

## Procedure

1. Double-click the first tLogRow to open
   its Basic settings view on the Component tab.
2. In the Mode area, select Table (print values in cells of a table) for a
   better display of the result.
3. Do the same to configure the second and the third tLogRow components.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-tlogrow-tfixedflowinput-tfixedflowinput-configuring-tsapbapi-component-standard-component-enterprise -->
# Configuring the tSAPBapi component

Last updated: 9/30/2026

## Procedure

1. Double-click tSAPBapi to open its
   Basic settings view on the Component tab.

   The SAP Function field has already been
   filled automatically with the name of the function to be called. In this
   example, it is *RFC\_READ\_TABLE*.

   The Input and Output tables have already been filled automatically with
   the input and output schemas of the function *RFC\_READ\_TABLE*.
2. In the Input table, click in the Schema field for the *QUERY\_TABLE* input parameter and click the [...] button in the cell. In the pop-up dialog
   box, enter the value for the *QUERY\_TABLE*
   input parameter between double quotation marks in the Value column. In this example, the table to be queried is
   *VBRK*.
3. Do the same to set the value for the *ROWCOUNT* and *ROWSKIPS*
   input parameters to *10* and *0* respectively.
4. Click in the Source Row field for the *FIELDS* input parameter and select *row1* from the drop-down list.
5. Do the same to select *row2* for the *OPTIONS* input parameter.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-input-component-standard-component-enterprise -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view on the Component tab.
2. Click the [...] button next to Edit schema to open the schema editor to define the input
   schema. In this example, the input schema is composed of four columns:
   *DELIMITER* and *QUERY\_TABLE* of string type, and *ROWCOUNT* and *ROWSKIPS* of
   integer type.
3. In the Mode area, select the Use
   Single Table option and specify the value for each column. In
   this example, *";"* for the *DELIMITER* column, *"SFLIGHT"* for the *QUERY\_TABLE* column, *10*
   for the *ROWCOUNT* column, and *-1* for the *ROWSKIPS* column.
4. Connect tFixedFlowInput to the first tXMLMap using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-output-components-standard-component-enterprise -->
# Configuring the output components

Last updated: 9/30/2026

## Procedure

1. Double-click the first tLogRow to open
   its Basic settings view on the Component tab.
2. Click the Sync columns button to retrieve
   the schema from the preceding component.
3. In the Mode area, select Table (print values in cells of a table) for a
   better display of the result.
4. Do the same to configure the second and the third tLogRow components.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-configuring-tsapbapi-component-standard-component-enterprise -->
# Configuring the tSAPBapi component

Last updated: 9/30/2026

## Procedure

1. Double-click tSAPBapi to open its
   Basic settings view on the Component tab.
2. Clear the tick it to enable multiple input/output;not tick it to
   enable document check box to allow using input and output
   parameters of type Document.
3. Click the [...] button next to Edit schema to open the schema editor.
4. Click the [+] button to add a column *doc* of type Document.

   When done, click OK to close the schema
   editor.
5. Right-click the first tXMLMap, select Row > \*New Output\*
   (Main) from the contextual menu and click tSAPBapi. In the pop-up dialog box, enter
   *in* and then click OK and accept schema propagation from the target
   component tSAPBapi. The first tXMLMap will be connected to tSAPBapi using a link named *in (Merge order:1)*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-mapping-input-data-flow-standard-component-enterprise -->
# Mapping the input data flow

Last updated: 9/30/2026

## Procedure

1. Double-click the first tXMLMap to open its map editor.
   In the *in* table on the right side,
   right-click the node *doc* and select
   Import From Repository from the
   contextual menu.
2. In the pop-up Metadata dialog box, select Input\_Schema in the folder *RFC\_READ\_TABLE* and click OK to close the dialog box. The schema is added to the XML
   tree.
3. Drag and drop all columns in the input table *main:row1*
   on the left side to the corresponding elements in the *in* table on the right side. Then in the
   *in* table, delete the other elements
   that do not need an input value.
4. Click OK to save the settings and close
   the map editor.
5. Connect tSAPBapi to the second tXMLMap using a Row >
   Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapbapi-txmlmap-tlogrow-tfixedflowinput-mapping-output-data-flow-standard-component-enterprise -->
# Mapping the output data flow

Last updated: 9/30/2026

## Procedure

1. Right-click the second tXMLMap, select Row > \*New Output\*
   (Main) from the contextual menu and click the first tLogRow. In the pop-up dialog box, enter
   *DATA* and then click OK. The second tXMLMap will be connected to the first tLogRow using a connection named *DATA (Main order:1)*.
2. Do the same to connect the second tXMLMap to the second
   tLogRow using a connection named
   *FIELDS (Main order:2)*, and to the
   third tLogRow using a connection named
   *OPTIONS (Main order:3)*.
3. Double-click the second tXMLMap to open its map editor.
   In the *main:row2* table on the left side,
   right-click the node *doc* and select
   Import From Repository from the
   contextual menu. In the pop-up Metadata
   dialog box, select Output\_Schema in the
   folder *RFC\_READ\_TABLE* and click OK to close the dialog box. The schema is added
   to the XML tree.
4. Drag and drop the node *WA* under the *DATA* element in the input table *main:row2* on the left side into the *DATA* table on the right side.
5. Do the same to drag and drop the nodes *FIELDNAME*,
   *OFFSET*, *LENGTH*, *TYPE*, and
   *FIELDTEXT* under the *FIELDS* element in the input table *main:row2* on the left side into the *FIELDS* table on the right side, and drag and
   drop the node *TEXT* under the *OPTIONS* element in the input table *main:row2* on the left side into the *OPTIONS* table on the right side.
6. Right-click the *item* node under the *DATA* node and select *As
   loop element* from the contextual menu to set it as the loop
   element.
7. Do the same to set the *item* nodes under
   the *FIELDS* and *OPTIONS* nodes as the loop element.
8. Click the set Loop Function button on the
   upper-right corner in the *DATA* table to
   configure the source loop.

   Click the [+] button to add a row, and then click in the
   Xpath field and select the source loop
   *row2.doc:/RFC\_READ\_TABLE/TABLES/DATA/item* from the drop-down
   list. When done, click OK to close the
   dialog box.
9. Do the same to set the source loop for the *FIELDS* and
   *OPTIONS* tables to *row2.doc:/RFC\_READ\_TABLE/TABLES/FIELDS/item* and
   *row2.doc:/RFC\_READ\_TABLE/TABLES/OPTIONS/item*
   respectively.
10. Click OK to close the map editor.
