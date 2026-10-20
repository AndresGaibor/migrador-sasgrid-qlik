<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-testing/cdataset · versión 8.0 -->
# cDataset

Last updated: 9/30/2026

Creates a new dataset or reference an existing dataset to send or receive
messages.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cDataset Standard properties

These properties are used to configure cDataset running in the Standard Job framework.

The Standard
cDataset component belongs to the Testing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Id | The ID of the Dataset bean. |
| Produce Delay | Specify a delay in milliseconds to cause producers to pause. |
| Consume Delay | Specify a delay in milliseconds to cause consumers to pause. |
| Preload Size | Specify how many messages should be sent before the Route completes its initialization. |
| Initial Delay | Specify the time in milliseconds to wait before starting sending messages. |
| Minimum Rate | Specify the least number of messages that the dataset should contain before starting sending messages. |
| Register new Bean | Select this check box to register a new bean. |
| Bean Class | Enter the class of the bean. This field appears when the Register new Bean check box is selected. |
| Arguments | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. This table appears when the Register new Bean check box is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cDataset can be a start, middle, or end component of a Route. |
| Limitation | n/a |

**Related concepts**  

* [Using cDataset to create messages](cdataset-csetbody-clog-clog-using-cdataset-to-create-messages)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-testing/cdataset-csetbody-clog-clog-using-cdataset-to-create-messages -->
# Using cDataset to create messages

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cDataset component is
used to create a DataSet instance as a source of messages.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-testing/cdataset-csetbody-clog-clog-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-testing/cdataset-csetbody-clog-clog-configuring-components)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-testing/cdataset-csetbody-clog-clog-viewing-code-and-executing-route)

**Related reference**  

* [cDataset](cdataset "Creates a new dataset or reference an existing dataset to send or receive messages.")

**Related information**  

* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-testing/cdataset-csetbody-clog-clog-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cDataset
   component to open its Basic settings view
   in the Component tab.
2. In the Id field, enter
   `"myDataset"` as the dataset bean ID.
3. In the Arguments table, click [+]
   to add a row and enter `1000` in the
   Value field to create 1000 messages. Keep the default
   settings of the other options.

   In the Bean Class field,
   the default implementation that is shipped by Camel org.apache.camel.component.dataset.SimpleDataSet is set. In this
   use case, a new dataset bean is registered.
4. Double-click the cSetBody
   component to open its Basic settings view
   in the Component tab.
5. Select Constant in the
   Language list and enter
   `"Hello!"` in the Expression field as the message body.
6. Keep the default settings of the cLog components to
   monitor the message exchanges.
7. Press Ctrl+S to save your
   Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-testing/cdataset-csetbody-clog-clog-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Testing folder, drag
   and drop a cDataset component onto the
   design workspace.
2. From the Core folder, drag and
   drop a cSetBody component onto the design
   workspace.
3. From the Miscellaneous folder,
   drag and drop two cLog components onto the
   design workspace.
4. Connect the components using Row > Route
   connections.
5. Label the components to better identify their roles in the Route,
   as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-testing/cdataset-csetbody-clog-clog-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom
   of the design workspace to look at the generated code.

   As shown in the code, the Route is built from the cDataset\_cDataset\_1 endpoint,
   routed .to the cDataset\_cLog\_1, set the message
   body as "Hello!" by the
   cDataset\_cSetBody\_1, and then routed .to the
   cDataset\_cLog\_2.
2. Press F6 to execute the Route.

   A dataset of 1000 messages is created and logged in the execution
   console. The default message body is
   <hello>world!</hello>. It is changed to
   Hello!.
