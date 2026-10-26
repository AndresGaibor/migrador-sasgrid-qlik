<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry · versión 8.0 -->
# cTry

Last updated: 9/30/2026

Offers the Java equivalent exception handling abilities by building
Try/Catch/Finally blocks to isolate the part of your Route likely to generate an error,
catch the errors, and execute final instructions regardless of the errors.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cTry Standard properties

These properties are used to configure cTry running in the
Standard Job framework.

The Standard
cTry component belongs to the Exception Handling
family.

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cTry is used as a middle component in a Route. |
| Connections | * Try: Select this link to isolate the part   of your Route that is likely to throw an exception or exceptions.  Information noteNote: When the Try link is followed by multiple components,   a compile error may occur showing "The method doCatch() is undefined   for the type ExpressionNode". In this case, use a   cJavaDSLProcessor component to end the Try block   with the code .endDoTry() as a workaround. * Catch: Select this link to catch any   exception thrown in the Route.  In the Exceptions field,   type in an expression to filter the type of exception to catch.  Information noteNote: This link can be used only when a Try link is present. * Finally: Select link to execute final   instructions regardless of any exceptions that may occur in the Route.  Information noteNote: This link can be used only when a Try link is present. * Route: Select this link to route all the messages   from the sender to the next endpoint. |
| Limitation | n/a |

**Related concepts**  

* [Using cTry to build Try/Catch/Finally blocks for exception handling](ctry-cprocessor-cfile-cfile-using-ctry-to-build-try-catch-finally-blocks-for-exception-handling)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry-cprocessor-cfile-cfile-using-ctry-to-build-try-catch-finally-blocks-for-exception-handling -->
# Using cTry to build Try/Catch/Finally blocks for exception handling

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, the content of each file sent from the message sender to the receiver is
checked and if any file does not meet the content requirement, an exception is thrown
and the relevant information is displayed on the console.

### In this section

* [Dropping and linking components](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry-cprocessor-cfile-cfile-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry-cprocessor-cfile-cfile-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry-cprocessor-cfile-cfile-viewing-code-and-executing-route)

**Related reference**  

* [cTry](ctry "Offers the Java equivalent exception handling abilities by building Try/Catch/Finally blocks to isolate the part of your Route likely to generate an error, catch the errors, and execute final instructions regardless of the errors.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry-cprocessor-cfile-cfile-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile
   component labeled `Sender` to open its Basic settings view in the Component tab.
2. In the Path field, fill in or browse to
   the path to the folder that holds the source files.
3. From the Encoding list, select the
   encoding type of your source files. Leave the other parameters as they
   are.
4. Repeat these step to define the output file path and encoding type
   in the Basic settings view of the other
   cFile component, which is labeled
   `Receiver`.
5. Double-click the cProcessor
   component labeled `Throw_exception` to open its Basic settings view in the Component tab, and customize the code in the Code area to throw an exception and display relevant
   information if any file coming using the try
   connection does not meet the content requirement, as follows:

   ```
   String body = exchange.getIn().getBody(String.class);
   System.out.println("\nTrying: "+body);
   Exception e = new Exception("Only 'Talend Integration Solutions' is acceptable. Please check the file:");
   if(!"Talend Integration Solutions".equals(body)){
   	throw e;
   }else{
       System.out.println("File is good.");
   }
   ```
6. Click the catch connection and then the Component tab to open its Basic settings view, and fill the Expression field with an expression to specify the type of
   exception to catch.

   In this scenario, enter `Exception.class` to
   catch any exception thrown.
7. Double-click cProcessor
   component labeled `Show_exception` to open its Basic settings view in the Component tab, and customize the code in the Code area to display the exception information and the
   related file name, as follows:

   ```
   System.out.println(exchange.getProperty("CamelExceptionCaught")+
   " " + exchange.getIn().getHeader("CamelFileName"));
   ```
8. Click Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry-cprocessor-cfile-cfile-dropping-and-linking-components -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. From the Connectivity folder of the Palette, drop twocFile components onto the design workspace, one as the
   message sender and the other as the message receiver.
2. From the Exception Handling folder, drop a cTry component onto the design workspace to build
   Try, Catch and Finally blocks.
3. From the Custom folder, drop two cProcessor components onto the design workspace.
4. Link the cFile component serving as
   message sender to the cTry component using
   a Row > Route connection.
5. Link the cTry component to one cProcessor using a Row > Try connection. This
   cProcessor component will throw an
   exception if any file coming via this connection does not contain the
   required content.
6. Link the cTry component to the other
   cProcessor component using a Row > Catch
   connection to catch the exception. This cProcessor component will display the information related to
   the exception and the file name that does not contain the required
   content.
7. Link the cTry component to the receiving
   cFile component using a Row > Finally
   connection.
8. Label the components according to their roles in the Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/ctry-cprocessor-cfile-cfile-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, while messages are routed from the sender
   .to the receiver, .doTry(),
   .doCatch() and .doFinally() blocks are built
   by cTry\_1. Thus, when any file does not meet the content
   requirement, an exception is thrown and caught, before each file is finally
   routed to the receiver.
2. Press F6 to execute the Route.

   RESULT: When a file that does not meet the content requirement is detected, an exception
   is thrown, and the exception information is displayed on the console.
   Regardless of the exception, all the files from the sender are sent to the
   receiver.
