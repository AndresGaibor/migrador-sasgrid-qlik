<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob · versión 8.0 -->
# cTalendJob

Last updated: 9/30/2026

Exchanges messages between a Data Integration Job and a Mediation
Route.

cTalendJob calls a Data Integration Job either from
the repository or exported as an OSGI Bundle For ESB. For more information on how to build
a Job and how to export a Job as an OSGI Bundle for ESB, see [Building a Job as an OSGI Bundle For ESB](/talend/r/en-US/8.0/studio-user-guide/building-job-as-osgi-bundle-for-esb).

## cTalendJob Standard properties

These properties are used to configure cTalendJob running in the Standard Job framework.

The Standard
cTalendJob component belongs to the Talend family.

## Basic settings

| Properties | Description |
| --- | --- |
| Repository | Select this option to call a Job from the Repository. |
| External | Select this option to call a Job that is exported as an OSGI Bundle For ESB. |
| Repository/Use Selected Job Context | This field appears when Repository is selected. Select this check box to use the context that is selected in the Context list when executing the Job. |
| Repository/Use Route Context Name | This field appears when Repository is selected. Select this check box to use the Job context that has the same name as the one that is used in the Route when executing the Job.  Information noteNote: If context does not exist in the Job, null values of the context parameters will be used during the Job execution. Make sure that you have the needed context in the Job. |
| Repository/Use Job Context | This field appears when Repository is selected. Select this check box to use the selected context on the Job side when executing the Job. |
| Repository/Job | This field appears when Repository is selected. Click [...] to show the Assign Job wizard. Choose between Create a new Job and Assign it to this cTalendJob component and Assign an existing Job to this cTalendJob component and follow the prompts. Information noteWarning: When assigning an existing Job to cTalendJob, only the Jobs with the tRouteInput component can be selected.  You can double-click cTalendJob to open the referenced Job, or right-click cTalendJob and select Open Job in Integration in the context menu open it. |
| Repository/Version | This field appears when Repository is selected. Select the version of the Job if more than one version of the Job is available. |
| Repository/Context | This field appears when Repository is selected. Select from the list the context to use to execute the referenced Job.  Information noteWarning: This option works only when Use Selected Job Context is selected. |
| External Jar/Library | This field appears when External is selected. Select the library you want to import from the list, or click on the [...] button to import the jar library of your Job. |
| External Jar/Job | This field appears when External is selected. Type in the name of the package and the name of your Job separated by a point. For example: `route_project.txmlmap_0_1.tXMLMap`. To get this naming, you can open the jar library of your Job, go to OSGI-INF > blueprint and edit the job.xml file, the naming is available in a bean node like <bean id="job" class="route\_project.txmlmap\_0\_1.tXMLMap"/>. |
| External Jar/Context | This field appears when External is selected. Type in the name of the context to use to execute the referenced Job. |
| Context Param | Use this table to change the variable values of the specified context in the referenced Job.  Click [+] to add as many rows as required to the table. Select the context variable that you want to change in the Parameters list of each row, and enter the value you want to give it in the Values field. This value will replace the one that is defined on the Job side. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Propagate Header | Select this check box to pass the message header to the referenced Job as a context variable. |
| Fast Job Invocation | Select this check box to bind the life cycle of the embedded Talend Job to the start and stop state changes of the connected Talend Camel Endpoint. When the Route is started, the endpoint for the embedded Job is also started, and the Job instance is created and ready for receiving message exchanges. With this option enabled, while the Route is active, the embedded Job keeps long-living resources and refreshes short-living resources between invocations. In this case the database access objects are only kept connected while data are sent or received, which avoids overhead and performance loss with Jobs containing database assess resources that are expensive on creation. Information noteWarning: Due to the variety of possible Jobs, there is no warranty that a specific Job will work as expected with the Fast Job Invocation option activated. Therefore, Jobs using this option need to be tested well for proper execution, and in failure case this option needs to be de-activated.  Information noteWarning: In combination with the Fast Job Invocation option, the Propagate Header option may not work as expected. The combination needs to be tested well for the specific Job, and in failure case the Fast Job Invocation option needs to be de-activated. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cTalendJob can be a start, middle, or end component in a Route. It is mandatory that a tRouteInput component is used in the Data Integration Job. The reason for it is that this will prevent the referenced Job from starting automatically when deployed in Talend Runtime. Instead it will only start when it gets called by the Route. |
| Limitation | n/a |

**Related concepts**  

* [Using cTalendJob to call a DI Job](ctalendjob-csetheader-ctimer-ctimer-using-ctalendjob-to-call-di-job)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-using-ctalendjob-to-call-di-job -->
# Using cTalendJob to call a DI Job

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, we will build a Data Integration Job with context first. Then, we will
create a Route with a cTalendJob component to call the
Job and set the context variables in the Job.

### In this section

* [Creating an Data Integration Job](/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-creating-data-integration-job)
* [Creating a Mediation Route](/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-creating-mediation-route)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-viewing-code-and-executing-route)

**Related reference**  

* [cTalendJob](ctalendjob "Exchanges messages between a Data Integration Job and a Mediation Route.")

**Related information**  

* [cSetHeader](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-creating-data-integration-job -->
# Creating an Data Integration Job

Last updated: 9/30/2026

In this section, we will build a Job named *RouteCommunication* to accept the message from a Route. For more information on how
to build a Job, see [Building Jobs](/talend/r/en-US/8.0/studio-user-guide/building-jobs).

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-configuring-components)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-creating-mediation-route -->
# Creating a Mediation Route

Last updated: 9/30/2026

In this section, we will create a Route to send a message to the Job.

### In this section

* [Arranging the flow of the message](/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-arranging-flow-of-message)
* [Configuring how the message is processed](/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-configuring-how-message-is-processed)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, a message route is built from the Starter,
   set a message header by the cSetHeader, and then
   sent to cTalendJob for the execution of the Job.
2. Press F6 to execute the Route.

   As shown above, the header and body of the message is printed in the
   execution console by the tLogRow. The
   header value is FileName. It is defined by the cSetHeader and passed to the Job as a context
   variable. The body value is Hello World!. It is defined by
   tRouteInput using the context variable
   body of the Job. The value for this variable is set as
   world in the Job, but changed to Hello World!
   in cTalendJob.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Create two variables, header and body in the
   Default context group. Give the value
   world to the body variable. The
   header variable will receive its value propagated from
   the Route. For more information about context setup, see
   [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).
2. Double-click the tRouteInput
   component to open its Basic settings
   view in the Component tab.
3. Click [...] next to Edit Schema. In the schema dialog box, click
   [+] to add two lines of String type and name them header
   and body respectively. Click OK to close the dialog box.
4. In the Simple Expression field for
   the header element, enter context.header to
   use the variable header in the context group which will be
   propagated from the Route.

   In the same field for the body element, enter
   context.body to use the variable body in
   the context group as the message body.
5. The tLogRow component will monitor
   the message exchanges and does not need any configuration.
6. Press Ctrl+S to save your Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. Drag and drop a tRouteInput and a
   tLogRow from the Palette onto the design workspace.
2. Right-click the tRouteInput
   component, select Row > Main from the contextual menu and click the
   tLogRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-arranging-flow-of-message -->
# Arranging the flow of the message

Last updated: 9/30/2026

## About this task

## Procedure

1. Drag and drop a cTimer, a cSetHeader, and a cTalendJob from the Palette onto the design workspace.
2. Link the components with the Row >
   Route connection as shown
   above.
3. Label the components for better identification of their roles.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-route/ctalendjob-csetheader-ctimer-ctimer-configuring-how-message-is-processed -->
# Configuring how the message is processed

Last updated: 9/30/2026

## Procedure

1. Double-click the cTimer component to
   open its Basic settings view in the
   Component tab.
2. Set the values for the Period
   (`200`), Repeat
   (`1`) and Delay
   (`1000`) fields as shown above to trigger a message exchange
   after a delay of 1000 milliseconds.
3. Double-click the cSetHeader component
   to display its Basic settings view in
   the Component tab.
4. Click [+] to add a row to the
   Headers table.

   In the Name field, type in
   `"header"` as the header name.

   Select Constant in the
   Language list, and enter
   `"FileName"` in the Value field.
5. Double-click the cTalendJob component
   to display its Basic settings view in
   the Component tab.
6. Select Repository to call a Job from
   the repository.
7. In the Repository Job area, select
   Use Selected Context.

   Click [...] next to the Job field to open the Assign
   Job wizard. Select Assign an
   existing Job to this cTalendJob component and click
   Next.

   In the Job selection view,
   select RouteCommunication that was just created in the
   Job designs tree view and click Finish.

   RouteCommunication is displayed in the Job field. By default, the latest version and the
   default context of it is selected.
8. Click [+] under the Context Param to add a row to it. 

   The Parameters list contains
   the variables in the default context group of the referenced Job. Select
   body in the list.

   Enter `"Hello World!"` in the Values field. It will replace the value world that is defined in the Job context.
9. Click the Advanced settings view.
   Select the Propagate Header check box
   to pass the header that is defined in cSetHeader to the Job as a context variable.
10. Press Ctrl+S to save your
    Route.
