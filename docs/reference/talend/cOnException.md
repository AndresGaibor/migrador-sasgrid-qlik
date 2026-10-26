<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception · versión 8.0 -->
# cOnException

Last updated: 9/30/2026

Catches the exceptions defined and triggers certain actions which are then
performed on these exceptions and the message routing.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cOnException Standard properties

These properties are used to configure cOnException running in the Standard Job framework.

The Standard
cOnException component belongs to the Exception Handling family.

## Basic settings

| Properties | Description |
| --- | --- |
| Exceptions | Click the plus button to add as many lines as needed in the table to define the exceptions to be caught. |
| Set a redelivering tries count | Select this check box to set the maximum redelivering tries in the Maximum redelivering tries field. |
| Non blocking asynchronous behavior | Select this check box to enable asynchronous delayed redelivery.  For details, go to <http://camel.apache.org/exception-clause.html>. |
| Exception behavior | None: select this option to take no action on the original route.  Handle the exceptions: select this option to handle exceptions and break out the original route.  Ignore the exceptions: select this option to ignore the exceptions and continue routing in the original route. |
| Route the original input body instead of the current body | Select this check box to route the original message instead of the current message that might be changed during the routing. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cOnException is used as a separate component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Using cOnException to ignore exceptions and continue message routing](conexception-cbean-cfile-cprocessor-using-conexception-to-ignore-exceptions-and-continue-message-routing)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception-cbean-cfile-cprocessor-using-conexception-to-ignore-exceptions-and-continue-message-routing -->
# Using cOnException to ignore exceptions and continue message routing

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cOnException component is used to
ignore an IO exception thrown by a Java bean so that the message is successfully routed
to the destination in spite of the exception.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception-cbean-cfile-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception-cbean-cfile-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception-cbean-cfile-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cOnException](conexception "Catches the exceptions defined and triggers certain actions which are then performed on these exceptions and the message routing.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cBean](/talend/en-US/mediation-components/8.0/mediation-bean/cbean)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception-cbean-cfile-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cOnException
   component, which is labeled `Ignore_exception`, to open its
   Basic settings view in the Component tab.
2. Click the plus button to add a line in the Exceptions table, and define the exception to catch. In this example,
   enter `java.io.IOException` to handle IO exceptions.

   In the Exception behavior area,
   select the Ignore the exceptions option to
   ignore exceptions and let message routing continue. Leave the other parameters as
   they are.
3. Double-click the cFile
   component, which is labeled `Source`, to open its Basic settings view in the Component tab.
4. In the Path field, enter the path of the
   message source, and leave the other parameters as they are.
5. Double-click the cBean
   component, which is labeled `Throw_exception`, to open its
   Basic settings view in the Component tab.
6. Select New Instance and in the
   Bean class field, enter the name of the bean
   to throw an IO exception, `beans.throwIOException.class` in this
   scenario.

   Note that this bean has already been defined in the Code node of the Repository and it looks like
   this:

   ```
   package beans;

   import java.io.IOException;

   import org.apache.camel.Exchange;

   public class throwIOException {

       /**

        * @throws IOException 
        */
       public static void helloExample(String message, Exchange exchange) throws IOException {
           throw new IOException("An IOException has been caught");
       }
   }
   ```

   For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).
7. Double-click the cProcessor
   component, which is labeled `Monitor`, to open its Basic settings view in the Component tab.
8. In the Code area, customize the code to
   display the file name of the consumed message on the Run console:

   ```
   System.out.println("Message consumed: "+ 
   exchange.getIn().getHeader("CamelFileName"));
   ```
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception-cbean-cfile-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drag and drop these components from the Palette onto the workspace: a cOnException component, a cFile component, a cBean
   component, and cProcessor component.
2. Link cFile to cBean using a Row >
   Route connection.
3. Link cBean to cProcessor using a Row >
   Route connection.
4. Label the components to better identify their roles in the Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception-cbean-cfile-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, Ignore\_exception handles any IO exception
   thrown by .bean(beans.throwIOException.class) invoked by
   cBean\_1, so that messages from the endpoint
   Source can be successfully routed onwards
   (continued(true)) in spite of the exception.
2. Press F6 to execute the Route.

   The route gets executed successfully and the files from the source are
   successfully routed to the destination.
3. Change the exception handling option in the cOnException component or deactivate the component and run
   the Route again.

   The exception thrown by the Java bean prevents the messages from being
   routed successfully.
