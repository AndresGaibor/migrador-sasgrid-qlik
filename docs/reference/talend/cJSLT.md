<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt · versión 8.0 -->
# cJSLT

Last updated: 9/30/2026

Uses [JSLT templates](https://github.com/schibsted/jslt) to transform JSON messages.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cJSLT Standard properties

These properties are used to configure cJSLT running in the
Standard Job framework.

The Standard
cJSLT component belongs to the Transformation
family.

## Basic settings

| Properties | Description |
| --- | --- |
| Type | Select the way the JSLT template will be set.   * Repository: The JSLT template will be selected   from an existing repository resource file. * File Path: The JSLT template will be selected from   the local file system. * Built-In: The JSLT template will be entered directly   within the component. |
| Resource / Version | This field appears when Repository is selected from the Type list. Click [...] and select the resource file containing the JSLT template. Select the version of the resource if more than one version of the resource is available. |
| Resource URI | This field appears when File Path is selected from the Type list. Enter the path to the JSLT template file in your local file system. |
| Cache Resource | This option appears when Repository or File Path is selected from the Type list. Select this check box to cache the resource instead of reloading it for each message. |
| Language | This option appears when Built-In is selected from the Type list. Select the language of the expression you use from None, Bean, Constant, CorrelationID, EL, Groovy, Header, JoSQL, JSonPath, JXPath, MVEL, OGNL, PHP, Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  Select Bean if you want to call a predefined Java Bean to return the JSLT template. |
| Code Style | This option appears when Built-In is selected from the Type list. Select from:  * Java: Java code can be used within JSLT template.   Quotes needs to be escaped, for example, \". * Native: No Java code can be used in JSLT   template. But quotes do not need be escaped, making the JSLT template   more readable. |
| JSLT template | This option appears when Built-In is selected from the Type list. Enter the JSLT template to be applied on incoming JSON messages.  For more information about how to use the languages to create an expression, see the site <http://camel.apache.org/languages.html>. |
| Pretty Print | Select this check box to format and print the output JSON message in a readable way. If you clear this check box, you will have the output in one row. |

## Advanced settings

| Properties | Description |
| --- | --- |
| URI Options | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding value field and enter a value. See the site <https://camel.apache.org/components/3.21.x/jslt-component.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cJSLT  can be a middle or end component in a Route. |
| Limitation | The input content needs to be in JSON format. |

**Related concepts**  

* [Transforming message between JSON formats using JSLT expression](cjslt-transforming-message-between-json-formats-using-jslt-expression)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt-transforming-message-between-json-formats-using-jslt-expression -->
# Transforming message between JSON formats using JSLT expression

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario illustrates how to transform message between JSON formats using a
template from the Studio repository, the local file system, and specified in the cJSLT component.

A JSON template file demo.jslt in the Studio repository and the local
file system with the following content will be used in this scenario:

```
{
  "firstName": .givenName,
  "lastName": .sureName,
  "fullName": .givenName + " " + .sureName,
  "fileName": split(.path, "/")[-1],
  "unixTime": round(now() * 1000),
  "status": $headers.responseCode,
  * - givenName, sureName : .
}
```

For more information on how to create a Resource in the Studio, see [Creating a Route Resource](/talend/en-US/studio-user-guide/8.0/creating-route-resource).

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt-viewing-code-and-executing-route)

**Related reference**  

* [cJSLT](cjslt "Uses JSLT templates to transform JSON messages.")

**Related information**  

* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)
* [cDirect](/talend/en-US/mediation-components/8.0/mediation-direct/cdirect)
* [cMulticast](/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast)
* [cSetHeader](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. In the Basic settings view of the
   cTimer component, enter `1` in the
   Repeat field to generate the message exchange
   one time. Keep the default settings of the other options.
2. In the Basic settings view of the
   cSetBody component, select Constant
   in the Language list and enter the following message in JSON
   format in the Expression field:

   ```
   "{ \"givenName\": \"Mike\", \"sureName\": \"Jonson\", \"employee\": { \"consultant\": true, \"since\": 2011 }, \"path\": \"/etc/talend/runtime.cfg\" }"
   ```
3. In the Basic settings view of the
   cSetHeader component, click [+] in
   the New headers to set area to add a row in the
   Headers table.

   In the Name field, enter the name of the header
   "responseCode".

   In the Language list, select
   Constant.

   In the Value field, enter 200.
4. In the Basic settings view of the
   cMulticast component, click [+] to
   add three rows to the URIS table. Specify the
   URIs of the endpoints where the message will be sent,
   `"direct:repo"`, `"direct:file"`, and
   `"direct:built-in"` in this use case.
5. In the Basic settings view of the
   cDirect component labeled
   `direct_repo`, enter the endpoint URI
   `"repo"` in the Name field.

   Repeat this step to set the Name for
   `direct_file` and `direct_built-in` as
   `"file"` and `"built-in"`
   respectively.
6. In the Basic settings view of the
   cJSLT component labeled
   `Repo_resource`:

   Select Repository in the
   Type list.

   Click [...] next to the Resource
   option and select the JSLT template that will be used to transform the incoming JSON
   message in the dialog box.

   Select the Pretty Print check box to format the output JSON
   message in a readable way.
7. In the Basic settings view of the
   cJSLT component labeled
   `Local_file`:

   Select File Path in the Type
   list.

   In the Resource File field, browse to the path to the JSLT
   template in your local file system that will be used to transform the incoming JSON
   message.
8. In the Basic settings view of the
   cJSLT component labeled
   `Built-in`:

   Select Built-In in the Type
   list.

   Select Constant in the Language list
   and Native as the code style.

   In the JSLT Template box, enter the JSLT template that will
   be used to transform the incoming JSON message.

   Select the Pretty Print check box to format the output JSON
   message in a readable way.
9. Keep the default settings of the cLog component.
10. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drag and drop a
   cTimer, a cSetBody, a
   SetHeader, a cMulticast, three
   cDirect, cJSLT, and cLog components onto the design workspace.
2. Label the components for better identification of their roles and link
   the them using the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjslt-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom
   of the design workspace to have a look at the generated code.
2. Click the Run view to display it
   and click the Run button to launch the execution
   of your Route. You can also press F6 to execute
   it. 

   RESULT: The following log messages are printed in the console. The
   input JSON message is sent to three endpoints and transformed by the same JSLT
   templates from different
   resources.

   ```
   Starting job cjslt at 16:22 21/08/2024.
   [statistics] connecting to socket on port 3661
   [statistics] connected
   [WARN ] 16:22:50 cjslt.cLog_1- Exchange[ExchangePattern: InOnly, BodyType: String, Body: {  "firstName" : "Mike",  "lastName" : "Jonson",  "fullName" : "Mike Jonson",  "fileName" : "runtime.cfg",  "unixTime" : 1724228570506,  "status" : 200,  "employee" : {    "consultant" : true,    "since" : 2011  },  "path" : "/etc/talend/runtime.cfg"}]
   [WARN ] 16:22:50 cjslt.cLog_2- Exchange[ExchangePattern: InOnly, BodyType: String, Body: {"firstName":"Mike","lastName":"Jonson","fullName":"Mike Jonson","fileName":"runtime.cfg","unixTime":1724228570527,"status":200,"employee":{"consultant":true,"since":2011},"path":"/etc/talend/runtime.cfg"}]
   [WARN ] 16:22:50 cjslt.cLog_3- Exchange[ExchangePattern: InOnly, BodyType: String, Body: {  "firstName" : "Mike",  "lastName" : "Jonson",  "fullName" : "Mike Jonson",  "fileName" : "runtime.cfg",  "unixTime" : 1724228570529,  "status" : 200,  "employee" : {    "consultant" : true,    "since" : 2011  },  "path" : "/etc/talend/runtime.cfg"}]
   ```
