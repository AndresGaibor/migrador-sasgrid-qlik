<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser · versión 8.0 -->
# cJsonParser

Last updated: 9/30/2026

Extracts the desired data from JSON format.

Information noteNote: This component is available only if you have installed the R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cJsonParser Standard properties

These properties are used to configure cJsonParser running in
the Standard Route framework.

The Standard
cJsonParser component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| JSON Library | Select the JSON library from Gson, Jackson, Fastjson, and Custom to extract the incoming data. |
| Mapping Class | This option appears when Gson, Jackson, or Fastjson is selected in the JSON Library list. Enter the mapping class to be used for parsing the data into a map. |
| Bean Reference ID | This option appears when Custom is selected in the JSON Library list. Select the ID of the Bean where your custom JSON structure is defined. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cJsonParser can be a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Extracting a JSON string into a map and converting the map back to JSON](cjsonparser-cjsonwriter-extracting-a-json-string-into-a-map-and-converting-the-map-back-to-json)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser-cjsonwriter-extracting-a-json-string-into-a-map-and-converting-the-map-back-to-json -->
# Extracting a JSON string into a map and converting the map back to JSON

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario shows how to parse a JSON string into a Java map and writes the map back into
a JSON schema.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser-cjsonwriter-dropping-and-linking-the-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser-cjsonwriter-configuring-the-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser-cjsonwriter-viewing-code-and-executing-route)

**Related reference**  

* [cJsonParser](cjsonparser "Extracts the desired data from JSON format.")
* [cJsonWriter](cjsonwriter "Transforms the incoming data into JSON format.")

**Related information**  

* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser-cjsonwriter-configuring-the-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cTimer
   component to display its Basic settings view in
   the Component tab.
2. In the Repeat field, enter
   `1` to trigger a message. Keep the default settings of the
   other options.
3. Double-click the cSetBody component to display its
   Basic settings view in the Component
   tab.
4. Select Constant in the Language list
   and enter the JSON string `"{\"firstName\": \"Mike\", \"lastName\":
   \"Jonson\", \"age\": 74, \"job\": \"artist\" }"` in the
   Expression field.
5. Double-click the cJsonParser
   component to display its Basic settings view in
   the Component tab.
6. Select Gson in the JSON
   Library list and enter `java.util.Map.class` in
   the Mapping Class field to parse the JSON string into a Java
   map.
7. Double-click a cLog component to display its
   Basic settings view in the Component
   tab.
8. Configure the properties as follows:
   1. Select the Format the log output option.
   2. In the Arguments table, click
      [+] to add a row. Enter
      `"multiline"` in the Name field
      and `true` in the value
      field.
   3. Keep the default settings of the other options.
9. Repeat this step to configure the other cLog component in
   the same way.
10. Double-click the cJsonWriter
    component to display its Basic settings view in
    the Component tab.
11. In the JSON Library list, select
    `Jackson` to write the Java map into JSON using the Jackson
    library.
12. Press Ctrl+S to save your
    Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser-cjsonwriter-dropping-and-linking-the-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cTimer, a cSetBody, a cJsonParser, a
   cJsonWriter, and two cLog components onto the design workspace.
2. Link the components with the Row
   > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonparser-cjsonwriter-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your route. You can also press F6 to execute it. 

   RESULT: The log messages are printed in the console. The JSON string
   is extracted into a Java map and then the map is converted back to a JSON
   string.
