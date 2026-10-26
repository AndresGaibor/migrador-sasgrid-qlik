<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields · versión 8.0 -->
# tExtractJSONFields

Last updated: 9/30/2026

Extracts the desired data from JSON fields based on the JSONPath or XPath
query.

### In this section

* [tExtractJSONFields Standard properties](/talend/en-US/components/8.0/processing/textractjsonfields-standard-properties)
* [tExtractJSONFields properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/textractjsonfields-properties-for-apache-spark-batch)
* [tExtractJSONFields properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/textractjsonfields-properties-for-apache-spark-streaming)

**Related concepts**  

* [Collecting data from your favorite online social network](textractjsonfields-tfileinputjson-tlogrow-tlogrow-collecting-data-from-your-favorite-online-social-network-standard-component-in-this)
* [Retrieving error messages while extracting data from JSON fields](textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-retrieving-error-messages-while-extracting-data-from-json-fields-standard-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-properties-for-apache-spark-batch -->
# tExtractJSONFields properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tExtractJSONFields running in the Spark Batch Job framework.

The Spark Batch
tExtractJSONFields component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Information noteNote: This component is not supported with the Databricks Serverless runtime.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Read by | Select a way of extracting the JSON data in the file.   * Xpath: Extracts the JSON data based on   the XPath query. * JsonPath: Extracts the JSON data based on   the JSONPath query. Note that it is recommended to read the data by JSONPath in   order to gain better performance. |
| JSON field | List of the JSON fields to be extracted. |
| Loop Jasonpath query | Enter the JSONPath or XPath of the node on which the loop is based.  Note if you have selected Xpath from the Read by drop-down list, the Loop Xpath query field is displayed instead. |
| Mapping | Complete this table to map the columns defined in the schema to the corresponding JSON nodes.   * Column: The Column cells are automatically filled with the defined schema   column names. * Json query/JSONPath query: Specify the JSONPath node that holds the   desired data. For more information about JSONPath expressions, see <http://goessner.net/articles/JsonPath/>.  This column is available only when JsonPath is selected from the Read   By list. * XPath query: Specify the XPath node that   holds the desired data.  This column is available only when Xpath is selected from the Read   By list. * Get Nodes: Select this check box to   extract the JSON data of all the nodes or select the check box next to a   specific node to extract the data of that node.  This column is available only when Xpath is selected from the Read   By list. * Is Array: select this check box when the   JSON field to be extracted is an array instead of an object.  This column is available only when Xpath is selected from the Read   By list. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-standard-properties -->
# tExtractJSONFields Standard properties

Last updated: 9/30/2026

These properties are used to configure tExtractJSONFields running in the Standard Job framework.

The Standard
tExtractJSONFields component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Read By | Select a way of extracting JSON data in the file.   * JsonPath: Extracts JSON data based on the   JSONPath query. With this option selected, you need to select a   JSONPath API version from the API version   drop-down list. It is recommended to read data by JSONPath in order   to gain better performance. * Xpath: Extracts JSON data based on the XPath   query. |
| JSON field | List of the JSON fields to be extracted. |
| Loop Jsonpath query | Enter the JSONPath or XPath of the node on which the loop is based.  Note if you have selected Xpath from the Read by drop-down list, the Loop Xpath query field is displayed instead. |
| Mapping | Complete this table to map the columns defined in the schema to the corresponding JSON nodes.   * Column: The Column cells are automatically filled with the defined schema   column names. * Json query/JSONPath query: Specify the JSONPath node that holds the   desired data. For more information about JSONPath expressions, see <http://goessner.net/articles/JsonPath/>.  This column is available only when JsonPath is selected from the Read   By list. * XPath query: Specify the XPath node that   holds the desired data.  This column is available only when Xpath is selected from the Read   By list. * Get Nodes: Select this check box to   extract the JSON data of all the nodes or select the check box next to a   specific node to extract the data of that node.  This column is available only when Xpath is selected from the Read   By list. * Is Array: select this check box when the   JSON field to be extracted is an array instead of an object.  This column is available only when Xpath is selected from the Read   By list. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use the loop node as root | Select this check box to use the loop node as the root for querying the file.  The loop node is set in the Loop Json query text frame in the Basic Settings view. If this option is checked, only the child elements of the loop node are available for querying; otherwise, both the parent elements and the child elements of the loop node can be queried. You can specify a parent element through JSON path syntax.  This check box is available only when JsonPath is selected in the Read By drop-down list of the Basic settings view. |
| JDK version | Select the JDK version to be used. Note that a Standalone Nashorn JAR will be imported if you select JDK 11 and above. For JDK 8 to 11, Nashorn dependency is built in the JDK.  This option is available when you select Xpath from the Read By drop-down list in the Basic settings view.  Information noteNote:  * This option is available only when you have installed the 8.0.1-R2023-01   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. * The JDK version changes from JDK 15 and above to   JDK 11 and above and from JDK 8 -   JDK 14 to JDK 8 to 11 only when you   have installed the 8.0.1-R2023-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediate component. It needs an input and an output components. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-tfileinputjson-tlogrow-tlogrow-collecting-data-from-your-favorite-online-social-network-standard-component-in-this -->
# Collecting data from your favorite online social network

Last updated: 9/30/2026

In this scenario, tFileInputJSON retrieves the
*friends* node from a JSON file that contains the
data of a Facebook user and tExtractJSONFields extracts
the data from the *friends* node for flat data
output.

### In this section

* [Linking the components](/talend/en-US/components/8.0/processing/textractjsonfields-tfileinputjson-tlogrow-tlogrow-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/processing/textractjsonfields-tfileinputjson-tlogrow-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/processing/textractjsonfields-tfileinputjson-tlogrow-tlogrow-executing-job-standard-component-press)

**Related concepts**  

* [tExtractJSONFields](textractjsonfields "Extracts the desired data from JSON fields based on the JSONPath or XPath query.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputJSON](/talend/en-US/components/8.0/json/tfileinputjson)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-retrieving-error-messages-while-extracting-data-from-json-fields-standard-component-in-this -->
# Retrieving error messages while extracting data from JSON fields

Last updated: 9/30/2026

In this scenario, tWriteJSONField wraps the incoming
data into JSON fields, data of which is then extracted by tExtractJSONFields. Meanwhile, the error messages generated due to
extraction failure, which include the concerned JSON fields and errors, are retrieved
via a Row > Reject
link.

### In this section

* [Linking the components](/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-executing-job-standard-component-press)

**Related concepts**  

* [tExtractJSONFields](textractjsonfields "Extracts the desired data from JSON fields based on the JSONPath or XPath query.")
* [tWriteJSONField](twritejsonfield "Transforms the incoming data into JSON fields and transfers them to a file, a database table, etc.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-tfileinputjson-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputJSON to display
   its Basic settings view.
2. Click Edit schema to open the schema
   editor.

   Click the [+] button to add
   one column, namely *friends*, of the String
   type.

   Click OK to close the editor.
3. Click the [...] button to browse for the
   JSON file, *facebook.json* in this
   case:

   ```
   { "user": { "id": "9999912398",
               "name": "Kelly Clarkson",
               "friends": [
                    { "name": "Tom Cruise",
                      "id": "55555555555555",
                      "likes": {
                          "data": [
                               { "category": "Movie",
                                 "name": "The Shawshank Redemption",
                                 "id": "103636093053996",
                                 "created_time": "2012-11-20T15:52:07+0000"
                               },
                               { "category": "Community",
                                 "name": "Positiveretribution",
                                 "id": "471389562899413",
                                 "created_time": "2012-12-16T21:13:26+0000"
                               }
                                   ]
                               }
                    },
                    { "name": "Tom Hanks",
                      "id": "88888888888888"
                      "likes": {
                           "data": [
                               { "category": "Journalist",
                                 "name": "Janelle Wang",
                                 "id": "136009823148851",
                                 "created_time": "2013-01-01T08:22:17+0000"
                               },
                               { "category": "Tv show",
                                 "name": "Now With Alex Wagner",
                                 "id": "305948749433410",
                                 "created_time": "2012-11-20T06:14:10+0000"
                               }
                               ]
                              }
                     }
                           ]
             }
   }
   ```
4. Select JsonPath without loop
   from the Read By drop-down list.
5. Enter `"$.user.friends[*]"` in the JSONPath
   query column next to the friends column in the
   Mapping table.

   The JSONPath query entered in this table retrieves the entire friends
   nodes from the source file.
6. Double-click tExtractJSONFields to
   display its Basic settings view.
7. Click Edit schema to open the schema
   editor.
8. Click the [+] button in the right panel
   to add five columns, namely *id*, *name*, *like\_id*, *like\_name* and
   *like\_category*, which will hold the
   data of relevant nodes in the JSON field *friends*.

   Click OK to close the editor.
9. In the pop-up Propagate box, click
   Yes to propagate the schema to the
   subsequent components.
10. Enter
    `"/likes/data"` in the Loop XPath query field.
11. In the Mapping area, type in the queries
    of the JSON nodes in the XPath query
    column. The data of those nodes will be extracted and passed to their
    counterpart columns defined in the output schema.
12. Specifically, define the XPath query *"../../id"* (querying the *"/friends/id"* node) for the column *id*, *"../../name"*
    (querying the *"/friends/name"* node) for
    the column *name*, *"id"* for the column *like\_id*, *"name"* for the
    column *like\_name*, and *"category"* for the column *like\_category*.
13. Double-click tLogRow to display its
    Basic settings view.
14. Select Table (print values in cells of a
    table) for a better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-tfileinputjson-tlogrow-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Click F6 to execute the Job.

   As shown above, the friends data of the Facebook user Kelly Clarkson is
   extracted correctly.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-tfileinputjson-tlogrow-tlogrow-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFileInputJSON, tExtractJSONFields and tLogRow.
2. Link tFileInputJSON and tExtractJSONFields using a Row > Main connection.
3. Link tExtractJSONFields and tLogRow using a Row > Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Setting up the tFixedFlowInput](/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-tfixedflowinput-standard-component)
* [Setting up the tWriteJSONField](/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-twritejsonfield-standard-component-click)
* [Setting up the tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-textractjsonfields-standard-component)
* [Setting up the tLogRow components](/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-tlogrow-components-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Click F6 to execute the Job.

   As shown above, the reject row offers such details as the data extracted,
   the JSON fields whose data is not extracted and the cause of the extraction
   failure.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tWriteJSONField, tExtractJSONFields, and tLogRow (X2). The two tLogRow components are renamed as data\_extracted and reject\_info.
2. Link tFixedFlowInput and tWriteJSONField using a Row > Main connection.
3. Link tWriteJSONField and tExtractJSONFields using a Row > Main connection.
4. Link tExtractJSONFields and data\_extracted using a Row > Main connection.
5. Link tExtractJSONFields and reject\_info using a Row > Reject connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-textractjsonfields-standard-component -->
# Setting up the tExtractJSONFields

Last updated: 9/30/2026

## Procedure

1. Double-click tExtractJSONFields to
   display its Basic settings view.
2. Click Edit schema to open the schema
   editor.
3. Click the [+] button in the right panel
   to add three columns, namely *firstname*,
   *lastname* and *dept*, which will hold the data of their counterpart nodes in
   the JSON field *staff*.

   Click OK to close the editor.
4. In the pop-up Propagate box, click
   Yes to propagate the schema to the
   subsequent components.
5. In the Loop XPath query field, enter
   *"/staff"*, which is the root node of
   the JSON data.
6. In the Mapping area, type in the node
   name of the JSON data under the XPath query
   part. The data of those nodes will be extracted and passed to their
   counterpart columns defined in the output schema.
7. Specifically, define the XPath query *"firstname"* for the column *firstname*, *"lastname"* for
   the column *lastname*, and *""* for the column *dept*. Note that *""* is not
   a valid XPath query and will lead to execution errors.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-tfixedflowinput-standard-component -->
# Setting up the tFixedFlowInput

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display
   its Basic settings view.
2. Click Edit schema to open the schema
   editor.

   Click the [+] button to add three
   columns, namely *firstname*, *lastname* and *dept*, with the type of string.

   Click OK to close the editor.
3. Select Use Inline Content and enter the
   data below in the Content box: 

   ```
   Andrew;Wallace;Doc
   John;Smith;R&D
   Christian;Dior;Sales
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-tlogrow-components-standard-component -->
# Setting up the tLogRow components

Last updated: 9/30/2026

## Procedure

1. Double-click data\_extracted to display
   its Basic settings view.
2. Select Table (print values in cells of a
   table) for a better display of the results.
3. Perform the same setup on the other tLogRow component, namely reject\_info.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractjsonfields-twritejsonfield-tfixedflowinput-tlogrow-setting-up-twritejsonfield-standard-component-click -->
# Setting up the tWriteJSONField

Last updated: 9/30/2026

## Procedure

1. Click tWriteJSONField to display its
   Basic settings view.
2. Click Configure JSON Tree to open the XML
   tree editor.

   The schema of tFixedFlowInput appears in
   the Linker source panel.
3. In the Linker target panel, click the
   default rootTag and type in staff, which is the root node of the JSON field
   to be generated.
4. Right-click staff and select Add Sub-element from the context menu.
5. In the pop-up box, enter the sub-node name, namely *firstname*.

   Repeat the steps to add two more sub-nodes, namely *lastname* and *dept*.
6. Right-click firstname and select
   Set As Loop Element from the context
   menu.
7. Drop firstname from the Linker source panel to its counterpart in the
   Linker target panel.

   In the pop-up dialog box, select Add linker to
   target node.

   Click OK to close the dialog box.
8. Repeat the steps to link the two other items.

   Click OK to close the XML tree
   editor.
9. Click Edit schema to open the schema
   editor.
10. Click the [+] button in the right panel
    to add one column, namely *staff*, which
    will hold the JSON data generated.

    Click OK to close the editor.
