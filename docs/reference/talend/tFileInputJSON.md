<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson · versión 8.0 -->
# tFileInputJSON

Last updated: 9/30/2026

Extracts JSON data from a file and transfers the data to a file, a database table,
etc.

### In this section

* [tFileInputJSON Standard properties](/talend/en-US/components/8.0/json/tfileinputjson-standard-properties)
* [tFileInputJSON properties for Apache Spark Batch](/talend/en-US/components/8.0/json/tfileinputjson-properties-for-apache-spark-batch)
* [tFileInputJSON properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/json/tfileinputjson-properties-for-apache-spark-streaming)

**Related concepts**  

* [Extracting JSON data from a file using JSONPath without setting a loop node](tfileinputjson-tlogrow-extracting-json-data-from-file-using-jsonpath-without-setting-loop-node-standard-component-this)
* [Extracting JSON data from a file using JSONPath](tfileinputjson-extracting-json-data-from-file-using-jsonpath-standard-component "Based on Extracting JSON data from a file using JSONPath without setting a loop node, this scenario extracts data under the book array of the JSON file Store.json by specifying a loop node and the relative JSON path for each node of interest, and then displays the flat data extracted on the console.")
* [Extracting JSON data from a file using XPath](tfileinputjson-extracting-json-data-from-file-using-xpath-standard-component "Based on Extracting JSON data from a file using JSONPath without setting a loop node, this scenario extracts the store name and the book information from the JSON file Store.json using XPath queries and displays the flat data extracted on the console.")
* [Extracting JSON data from a URL](tfileinputjson-textractjsonfields-tlogrow-tlogrow-extracting-json-data-from-url-standard-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-extracting-json-data-from-file-using-jsonpath-standard-component -->
# Extracting JSON data from a file using JSONPath

Last updated: 9/30/2026

Based on [Extracting JSON data from a file using JSONPath without setting a loop
node](/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-extracting-json-data-from-file-using-jsonpath-without-setting-loop-node-standard-component-this), this scenario
extracts data under the *book* array of the JSON file
*Store.json* by specifying a loop node and the relative
JSON path for each node of interest, and then displays the flat data extracted on the
console.

### In this section

* [Extracting JSON data with a loop node](/talend/en-US/components/8.0/json/tfileinputjson-extracting-json-data-with-loop-node-standard-component-in)

**Related concepts**  

* [tFileInputJSON](tfileinputjson "Extracts JSON data from a file and transfers the data to a file, a database table, etc.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-extracting-json-data-from-file-using-xpath-standard-component -->
# Extracting JSON data from a file using XPath

Last updated: 9/30/2026

Based on [Extracting JSON data from a file using JSONPath without setting a loop
node](/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-extracting-json-data-from-file-using-jsonpath-without-setting-loop-node-standard-component-this), this
scenario extracts the store name and the book information from the JSON file *Store.json* using XPath queries and displays the flat data
extracted on the console.

### In this section

* [Procedure](/talend/en-US/components/8.0/json/tfileinputjson-procedure-standard-component-in)

**Related concepts**  

* [tFileInputJSON](tfileinputjson "Extracts JSON data from a file and transfers the data to a file, a database table, etc.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-properties-for-apache-spark-batch -->
# tFileInputJSON properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileInputJSON running in the Spark Batch Job framework.

The Spark Batch
tFileInputJSON component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The fields that come after are pre-filled in using the fetched   data.  For further information about the File Json node, see [Centralizing JSON file metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-json-file-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Read by | Select a way of extracting the JSON data in the file.   * Xpath: Extracts the JSON data based on   the XPath query. * JsonPath: Extracts the JSON data based on   the JSONPath query. Note that it is recommended to read the data by JSONPath in   order to gain better performance. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you entered points to a folder, all files stored in that folder will be read.  If the file to be read is a compressed one, enter the file name with its extension; then tFileInputJSON automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Use S3 Select | Select this check box to use S3 select to improve your query performance. You need to set the following parameters in the corresponding fields:  * Type: select the JSON format between either   Lines or Document from the   drop-down list. * Use GZIP compression: select this check box to use   GZIP compression on your files.   This check box is only available when you use a tS3Configuration component as a storage configuration component and when you run your Job with Spark Universal in either YARN cluster (with an Amazon EMR cluster) or Databricks modes.  This option is available only when you have installed the 8.0.1-R2022-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |
| Loop Jsonpath query | Enter the JSONPath or XPath of the node on which the loop is based.  Note if you have selected Xpath from the Read by drop-down list, the Loop Xpath query field is displayed instead. |
| Mapping | Complete this table to map the columns defined in the schema to the corresponding JSON nodes.   * Column: The Column cells are automatically filled with the defined schema   column names. * Json query/JSONPath query: Specify the JSONPath node that holds the   desired data. For more information about JSONPath expressions, see <http://goessner.net/articles/JsonPath/>.  This column is available only when JsonPath is selected from the Read   By list. * XPath query: Specify the XPath node that   holds the desired data.  This column is available only when Xpath is selected from the Read   By list. * Get Nodes: Select this check box to   extract the JSON data of all the nodes or select the check box next to a   specific node to extract the data of that node.  This column is available only when Xpath is selected from the Read   By list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set minimum partitions | Select this check box to control the number of partitions to be created from the input data over the default partitioning behavior of Spark.  In the displayed field, enter, without quotation marks, the minimum number of partitions you want to obtain.  When you want to control the partition number, you can generally set at least as many partitions as the number of executors for parallelism, while bearing in mind the available memory and the data transfer pressure on your network. |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-standard-properties -->
# tFileInputJSON Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileInputJSON running in the Standard Job framework.

The Standard
tFileInputJSON component belongs to the Internet and the File families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Read By | Select a way of extracting JSON data in the file.   * JsonPath: Extracts JSON data based on the   JSONPath query. With this option selected, you need to select a   JSONPath API version from the API version   drop-down list. It is recommended to read data by JSONPath in order   to gain better performance. * Xpath: Extracts JSON data based on the XPath   query. * JsonPath without loop: Extracts JSON data   based on the JSONPath query without setting a loop node. |
| Use Url | Select this check box to retrieve data directly from the Web. |
| URL | Enter the URL path from which you will retrieve data.  This field is available only when the Use Url check box is selected. |
| Filename | Specify the file from which you will retrieve data.  This field is not visible if the Use Url check box is selected.  Information noteWarning:  * Use absolute path (instead of relative path) to avoid possible   errors. * When using Xpath, make sure the fields in your   JSON file do not start with numbers, to avoid the following error when   running the Job: The content of elements must consist of   well-formed character data or markup. |
| Loop Json query | Enter the JSONPath or XPath of the node on which the loop is based.  Note if you have selected Xpath from the Read by drop-down list, the Loop Xpath query field is displayed instead. |
| Mapping | Complete this table to map the columns defined in the schema to the corresponding JSON nodes.   * Column: The Column cells are automatically filled with the defined schema   column names. * Json query/JSONPath query: Specify the JSONPath node that holds the   desired data. For more information about JSONPath expressions, see <http://goessner.net/articles/JsonPath/>.  This column is available only when JsonPath is selected from the Read   By list. * XPath query: Specify the XPath node that   holds the desired data.  This column is available only when Xpath is selected from the Read   By list. * Get Nodes: Select this check box to   extract the JSON data of all the nodes or select the check box next to a   specific node to extract the data of that node.  This column is available only when Xpath is selected from the Read   By list. |
| Die on error | Select this check box to stop the execution of the Job when an error occurs. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| JDK version | Select the JDK version to be used. Note that a Standalone Nashorn JAR will be imported if you select JDK 11 and above. For JDK 8 to 11, Nashorn dependency is built in the JDK.  This option is available when you select JsonPath without loop from the Read By drop-down list in the Basic settings view.  Information noteNote:  * This option is available only when you have installed the 8.0.1-R2023-01   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. * The JDK version changes from JDK 15 and above to   JDK 11 and above and from JDK 8 -   JDK 14 to JDK 8 to 11 only when you   have installed the 8.0.1-R2023-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Advanced separator (for numbers) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*).  Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| Use the loop node as root | Select this check box to use the loop node as the root for querying the file.  The loop node is set in the Loop Json query text frame in the Basic Settings view. If this option is checked, only the child elements of the loop node are available for querying; otherwise, both the parent elements and the child elements of the loop node can be queried. You can specify a parent element through JSON path syntax.  This check box is available only when JsonPath is selected in the Read By drop-down list of the Basic settings view. |
| Validate date | Select this check box to check the date format strictly against the input schema.  This check box is available only if the Read By XPath check box is selected. |
| Encoding | Select the encoding type from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| Include the Nashorn library | Select this option to include the Nashorn library. This option is necessary if you are using JDK 15 or a higher version.  This option is available when `JsonPath without loop` is selected from the Read By drop-down list in the Basic settings view. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is a start component of a Job and always needs an output link. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-textractjsonfields-tlogrow-tlogrow-extracting-json-data-from-url-standard-component-in-this -->
# Extracting JSON data from a URL

Last updated: 9/30/2026

In this scenario, tFileInputJSON retrieves data of the
*friends* node from the JSON file *facebook.json* on the Web that contains the data of a Facebook
user and tExtractJSONFields extracts the data from the
*friends* node for flat data output.

The JSON file *facebook.json* is deployed on the Tomcat
server, specifically, located in the folder *<tomcat
path>/webapps/docs*, and the content of the file is as follows:

```
{"user": {
    "id": "9999912398",
    "name": "Kelly Clarkson",
    "friends": [
        {
            "name": "Tom Cruise",
            "id": "55555555555555",
            "likes": {"data": [
                {
                    "category": "Movie",
                    "name": "The Shawshank Redemption",
                    "id": "103636093053996",
                    "created_time": "2012-11-20T15:52:07+0000"
                },
                {
                    "category": "Community",
                    "name": "Positiveretribution",
                    "id": "471389562899413",
                    "created_time": "2012-12-16T21:13:26+0000"
                }
            ]}
        },
        {
            "name": "Tom Hanks",
            "id": "88888888888888",
            "likes": {"data": [
                {
                    "category": "Journalist",
                    "name": "Janelle Wang",
                    "id": "136009823148851",
                    "created_time": "2013-01-01T08:22:17+0000"
                },
                {
                    "category": "Tv show",
                    "name": "Now With Alex Wagner",
                    "id": "305948749433410",
                    "created_time": "2012-11-20T06:14:10+0000"
                }
            ]}
        }
    ]
}}
```

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/json/tfileinputjson-textractjsonfields-tlogrow-tlogrow-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/json/tfileinputjson-textractjsonfields-tlogrow-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/json/tfileinputjson-textractjsonfields-tlogrow-tlogrow-executing-job-standard-component-press)

**Related concepts**  

* [tFileInputJSON](tfileinputjson "Extracts JSON data from a file and transfers the data to a file, a database table, etc.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-extracting-json-data-from-file-using-jsonpath-without-setting-loop-node-standard-component-this -->
# Extracting JSON data from a file using JSONPath without setting a loop node

Last updated: 9/30/2026

This scenario describes a two-component Job that extracts data from the JSON file
*Store.json* by specifying the complete JSON path for
each node of interest and displays the flat data extracted on the console.

The JSON file *Store.json* contains information about a
department store and the content of the file is as follows:

```
{"store": {
    "name": "Sunshine Department Store",
    "address": "Wangfujing Street",
    "goods": {
        "book": [
            {
                "category": "Reference",
                "title": "Sayings of the Century",
                "author": "Nigel Rees",
                "price": 8.88
            },
            {
                "category": "Fiction",
                "title": "Sword of Honour",
                "author": "Evelyn Waugh",
                "price": 12.66
            }
        ],
        "bicycle": {
            "type": "GIANT OCR2600",
            "color": "White",
            "price": 276
        }
    }
}}
```

In the following example, we will extract the store name, the store address, and the
bicycle information from this file.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-executing-job-standard-component-press)

**Related concepts**  

* [tFileInputJSON](tfileinputjson "Extracts JSON data from a file and transfers the data to a file, a database table, etc.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-extracting-json-data-with-loop-node-standard-component-in -->
# Extracting JSON data with a loop node

Last updated: 9/30/2026

## Procedure

1. In Talend Studio,
   open the Job used in [Extracting JSON data from a file using JSONPath without setting a loop
   node](/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-extracting-json-data-from-file-using-jsonpath-without-setting-loop-node-standard-component-this) to display it in the design workspace.
2. Double-click the tFileInputJSON component to open
   its Basic settings view.
3. Select JsonPath from the Read By drop-down list.
4. In the Loop Json query field, enter the JSONPath
   query expression between double quotation marks to specify the node on which the
   loop is based. In this example, it is *"$.store.goods.book[\*]"*.
5. Click the [...] button next to Edit schema to open the schema editor.

   Select the five columns added previously and click the x button to remove all of them.

   Click the [+] button to add four columns,
   *book\_title*, *book\_category*, and *book\_author* of
   String type, and *book\_price* of Double type.

   Click OK to close the schema editor. In the
   pop-up dialog box, click Yes to propagate the
   schema to the subsequent component.
6. In the Json query fields of the Mapping table, enter the JSONPath query expressions between double
   quotation marks to specify the nodes that hold the desired data. In this example,
   enter the JSONPath query expressions *"title"*,
   *"category"*, *"author"*, and *"price"* relative to
   the four child nodes of the *book* node
   respectively.
7. Press Ctrl+S to save the Job.
8. Press F6 to execute the Job. 

   As shown above, the book information is extracted from the source JSON data and displayed
   in a flat table on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-procedure-standard-component-in -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. In Talend Studio,
   open the Job used in [Extracting JSON data from a file using JSONPath without setting a loop
   node](/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-extracting-json-data-from-file-using-jsonpath-without-setting-loop-node-standard-component-this) to display it in the design workspace.
2. Double-click the tFileInputJSON component to open
   its Basic settings view.
3. Select Xpath from the Read
   By drop-down list.
4. Click the [...] button next to Edit schema to open the schema editor.

   Select the five columns added previously and click the x button to remove all of them.

   Click the [+] button to add five columns,
   *store\_name*, *book\_title*, *book\_category*, and
   *book\_author* of String type, and *book\_price* of
   Double type.

   Click OK to close the schema editor. In the
   pop-up dialog box, click Yes to propagate the
   schema to the subsequent component.
5. In the Loop XPath query field, enter the XPath
   query expression between double quotation marks to specify the node on which the
   loop is based. In this example, it is *"/store/goods/book"*.
6. In the XPath query fields of the Mapping table, enter the XPath query expressions between
   double quotation marks to specify the nodes that hold the desired data.
   * For the column *store\_name*, enter the
     XPath query *"../../name"* relative to the
     *name* node.
   * For the columns *book\_title*, *book\_category*, *book\_author*, and *book\_price*, enter the XPath query expressions *"title"*, *"category"*, *"author"*, and
     *"price"* relative to the four child
     nodes of the *book* node
     respectively.
7. Press Ctrl+S to save the Job.
8. Press F6 to execute the Job. 

   As shown above, the store name and the book information are extracted from the
   source JSON data and displayed in a flat table on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-textractjsonfields-tlogrow-tlogrow-adding-and-linking-components-standard-component-create -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tFileInputJSON
   component, a tExtractJSONFields component, and
   two tLogRow components by typing their names in
   the design workspace or dropping them from the Palette.
2. Link the tFileInputJSON component to the
   first tLogRow component using a Row > Main
   connection.
3. Link the first tLogRow component to the
   tExtractJSONFields component using a
   Row > Main connection.
4. Link the tExtractJSONFields component to the
   second tLogRow component using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-textractjsonfields-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputJSON component to
   open its Basic settings view.
2. Select JsonPath without
   loop from the Read By
   drop-down list. Then select the Use Url
   check box and in the URL field displayed
   enter the URL of the file facebook.json from which the data
   will be retrieved. In this example, it is
   `http://localhost:8080/docs/facebook.json`.
3. Click the [...] button
   next to Edit schema and in the Schema dialog box define the schema by adding one
   column friends of String type.

   Click OK to close the
   dialog box and accept the propogation prompted by the pop-up dialog box.
4. In the Mapping table,
   enter the JSONPath query `"$.user.friends[*]"` next to the
   friends column to retrieve the entire
   friends node from the source file.
5. Double-click tExtractJSONFields to open its
   Basic settings view.
6. Select Xpath from the Read By drop-down list.
7. In the Loop XPath query
   field, enter the XPath expression between double quotation marks to specify the
   node on which the loop is based. In this example, it is
   `"/likes/data"`.
8. Click the [...] button
   next to Edit schema and in the Schema dialog box define the schema by adding five
   columns of String type,
   id, name,
   like\_id, like\_name, and
   like\_category, which will hold the data of relevant nodes under the JSON field
   friends.

   Click OK to close the
   dialog box and accept the propogation prompted by the pop-up dialog box.
9. In the XPath query
   fields of the Mapping table, type in the
   XPath query expressions between double quotation marks to specify the JSON nodes
   that hold the desired data. In this example:

   * `"../../id"` (querying the
     "/friends/id" node) for the column *id*,
   * `"../../name"` (querying the
     "/friends/name" node) for the column *name*,
   * `"id"` for the column
     like\_id,
   * `"name"` for the column
     like\_name, and
   * `"category"` for the column
     like\_category.
10. Double-click the second tLogRow component to
    open its Basic settings view.

    In the Mode area, select Table (print values in cells of a table) for better
    readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-textractjsonfields-tlogrow-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Click F6 to execute the Job.

   As shown above, the friends data in the JSON file specified using the URL is
   extracted and then the data from the node *friends* is extracted and displayed in a flat table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-adding-and-linking-components-standard-component-create -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tFileInputJSON
   component and a tLogRow component by typing
   their names in the design workspace or dropping them from the Palette.
2. Link the tFileInputJSON component to the
   tLogRow component using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputJSON component to
   open its Basic settings view.
2. Select JsonPath without loop from the
   Read By drop-down list. With this option,
   you need to specify the complete JSON path for each node of interest in the
   JSONPath query fields of the Mapping table.
3. Click the [...] button next to Edit schema to open the schema editor.
4. Click the [+] button to add five columns,
   *store\_name*, *store\_address*, *bicycle\_type*,
   and *bicycle\_color* of String type, and *bicycle\_price* of Double
   type.

   Click OK to close the schema editor. In the
   pop-up dialog box, click Yes to propagate the
   schema to the subsequent component.
5. In the Filename field, specify the path to
   the JSON file that contains the data to be extracted. In this example, it is
   *"E:/Store.json"*.
6. In the Mapping table, the Column fields are automatically filled with the
   schema columns you have defined.

   In the JSONPath query fields, enter the
   JSONPath query expressions between double quotation marks to specify the nodes
   that hold the desired data.

   * For the columns *store\_name* and
     *store\_address*, enter the JSONPath
     query expressions *"$.store.name"* and
     *"$.store.address"* relative to the
     nodes *name* and *address* respectively.
   * For the columns *bicycle\_type*,
     *bicycle\_color*, and *bicycle\_price*, enter the JSONPath query
     expressions *"$.store.goods.bicycle.type"*, *"$.store.goods.bicycle.color"*, and *"$.store.goods.bicycle.price"* relative to
     the child nodes *type*, *color*, and *price* of the *bicycle*
     node respectively.
7. Double-click the tLogRow component to display
   its Basic settings view.
8. In the Mode area, select Table (print values in cells of a table) for better
   readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to execute the Job. 

   As shown above, the store name, the store address, and the bicycle information
   are extracted from the source JSON data and displayed in a flat table on the
   console.
