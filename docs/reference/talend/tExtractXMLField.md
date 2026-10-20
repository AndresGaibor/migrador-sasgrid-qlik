<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractxmlfield · versión 8.0 -->
# tExtractXMLField

Last updated: 9/30/2026

Reads the XML structured data from an XML field and sends the data as defined in
the schema to the following component.

### In this section

* [tExtractXMLField Standard properties](/talend/en-US/components/8.0/processing/textractxmlfield-standard-properties?id=4021)
* [tExtractXMLField properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/textractxmlfield-properties-for-apache-spark-batch?id=4022)
* [tExtractXMLField properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/textractxmlfield-properties-for-apache-spark-streaming?id=4023)

**Related concepts**  

* [Extracting correct and erroneous data from an XML field in a delimited file](textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-extracting-correct-and-erroneous-data-from-xml-field-in-delimited-file-standard-component "This scenario describes a four-component Job that reads an XML structure from a delimited file, outputs the main data and rejects the erroneous data.")
* [Extracting XML data from a field in a database table](textractxmlfield-tmysqlinput-tfileoutputdelimited-tfileoutputdelimited-extracting-xml-data-from-field-in-database-table-standard-component "This three-component scenario allows to read the XML structure included in the fields of a database table and then extracts the data.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractxmlfield-properties-for-apache-spark-batch -->
# tExtractXMLField properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tExtractXMLField running in the Spark Batch Job framework.

The Spark Batch
tExtractXMLField component belongs to the XML family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Information noteNote: This component is not supported with the Databricks Serverless runtime.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  When this file is selected, the fields that   follow are pre-filled in using fetched data. |
| Schema type and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| XML field | Name of the XML field to be processed. |
| Loop XPath query | Node of the XML tree, which the loop is based on. |
| Mapping | Column: reflects the schema as defined by the Schema type field.  XPath Query: Enter the fields to be extracted from the structured input.  Get nodes: Select this check box to recuperate the XML content of all current nodes specified in the Xpath query list or select the check box next to specific XML nodes to recuperate only the content of the selected nodes. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Ignore the namespaces | Select this check box to ignore namespaces when reading and extracting the XML data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractxmlfield-standard-properties -->
# tExtractXMLField Standard properties

Last updated: 9/30/2026

These properties are used to configure tExtractXMLField running in the Standard Job framework.

The Standard
tExtractXMLField component belongs to the Processing and the XML families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  When this file is selected, the fields that   follow are pre-filled in using fetched data. |
| Schema type and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| XML field | Name of the XML field to be processed. |
| Loop XPath query | Node of the XML tree, which the loop is based on. |
| Mapping | Column: reflects the schema as defined by the Schema type field.  XPath Query: Enter the fields to be extracted from the structured input.  Get nodes: Select this check box to recuperate the XML content of all current nodes specified in the Xpath query list or select the check box next to specific XML nodes to recuperate only the content of the selected nodes. |
| Limit | Maximum number of rows to be processed. If Limit is 0, no rows are read or processed. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Ignore the namespaces | Select this check box to ignore namespaces when reading and extracting the XML data. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediate component. It needs an input and an output components. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-extracting-correct-and-erroneous-data-from-xml-field-in-delimited-file-standard-component -->
# Extracting correct and erroneous data from an XML field in a delimited file

Last updated: 9/30/2026

This scenario describes a four-component Job that reads an XML structure from a
delimited file, outputs the main data and rejects the erroneous data.

### In this section

* [Procedure](/talend/en-US/components/8.0/processing/textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-procedure-standard-component-drop?id=4145)

**Related concepts**  

* [tExtractXMLField](textractxmlfield "Reads the XML structured data from an XML field and sends the data as defined in the schema to the following component.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractxmlfield-tmysqlinput-tfileoutputdelimited-tfileoutputdelimited-extracting-xml-data-from-field-in-database-table-standard-component -->
# Extracting XML data from a field in a database table

Last updated: 9/30/2026

This three-component scenario allows to read the XML structure included in the fields
of a database table and then extracts the data.

### In this section

* [Procedure](/talend/en-US/components/8.0/processing/textractxmlfield-tmysqlinput-tfileoutputdelimited-tfileoutputdelimited-procedure-standard-component-drop?id=4137)

**Related concepts**  

* [tExtractXMLField](textractxmlfield "Reads the XML structured data from an XML field and sends the data as defined in the schema to the following component.")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette to the design workspace: tFileInputDelimited, tExtractXMLField, tFileOutputDelimited and tLogRow.

   Connect the first three components using Row
   Main links.

   Connect tExtractXMLField to tLogRow using a Row
   Reject link.
2. Double-click tFileInputDelimited to open its
   Basic settings view and define the
   component properties.
3. Select Built-in in the Schema list and fill in the file metadata manually in the
   corresponding fields.

   Click the [...] button next to Edit
   schema to display a dialog box where you can define the structure
   of your data.

   Click the plus button to add as many columns as needed to your data structure.
   In this example, we have one column in the schema:
   *xmlStr*.

   Click OK to validate your changes and close
   the dialog box.

   Information noteNote:

   If you have already stored the schema in the Metadata folder under File
   delimited, select Repository
   from the Schema list and click the
   [...] button next to the field to display the Repository Content dialog box where you can select the
   relevant schema from the list. Click Ok to
   close the dialog box and have the fields automatically filled in with the
   schema metadata.

   For more information about storing schema metadata in the
   Repository tree view, see [Managing metadata in Talend
   Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).
4. In the File Name field, click the [...]
   button and browse to the input delimited file you want to process,*CustomerDetails\_Error* in this example.

   This delimited file holds a number of simple XML lines separated by double
   carriage return.

   Set the row and field separators used in the input file in the corresponding
   fields, double carriage return for the first and nothing for the second in this
   example.

   If needed, set Header, Footer and Limit. None is used
   in this example.
5. In the design workspace, double-click tExtractXMLField to display its Basic
   settings view and define the component properties.
6. Click Sync columns to retrieve the schema
   from the preceding component. You can click the [...] button next to
   Edit schema to view/modify the
   schema.

   The Column field in the Mapping table will be automatically populated with the defined
   schema.
7. In the Xml field list, select the column from
   which you want to extract the XML data. In this example, the filed holding the
   XML data is called *xmlStr*.

   In the Loop XPath query field, enter the node
   of the XML tree on which to loop to retrieve data.
8. In the design workspace, double-click tFileOutputDelimited to open its Basic
   settings view and display the component properties.
9. In the File Name field, define or browse to
   the output file you want to write the correct data in,
   *CustomerNames\_right.csv* in this example.

   Click Sync columns to retrieve the schema of
   the preceding component. You can click the [...] button next to Edit schema to view/modify the schema.
10. In the design workspace, double-click tLogRow
    to display its Basic settings view and define
    the component properties.

    Click Sync Columns to retrieve the schema of
    the preceding component. For more information on this component, see [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow).
11. Save your Job and press F6 to execute it.

## Results

tExtractXMLField reads and extracts in the output
delimited file, *CustomerNames\_right*, the client information for
which the XML structure is correct, and displays as well erroneous data on the console
of the Run view.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/textractxmlfield-tmysqlinput-tfileoutputdelimited-tfileoutputdelimited-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tMysqlInput, tExtractXMLField,
   and tFileOutputDelimited.

   Connect the three components using Main
   links.
2. Double-click tMysqlInput to display its
   Basic settings view and define its
   properties.
3. If you have already stored the input schema in the Repository tree view, select Repository first from the Property
   Type list and then from the Schema list to display the Repository
   Content dialog box where you can select the relevant metadata. 

   For more information about storing schema metadata in the
   Repository tree view, [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).

   If you have not stored the input schema locally, select Built-in in the Property Type
   and Schema fields and enter the database
   connection and the data structure information manually. For more information
   about tMysqlInput properties, see [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput).
4. In the Table Name field, enter the name of
   the table holding the XML data, *customerdetails* in this
   example.

   Click Guess Query to display the query
   corresponding to your schema.
5. Double-click tExtractXMLField to display its
   Basic settings view and define its
   properties.
6. Click Sync columns to retrieve the schema
   from the preceding component. You can click the [...] button next to
   Edit schema to view/modify the
   schema.

   The Column field in the Mapping table will be automatically populated with the defined
   schema.
7. In the Xml field list,
   select the column from which you want to extract the XML data. In this example, the
   field holding the XML data is called *CustomerDetails*.

   In the Loop XPath query
   field, enter the node of the XML tree on which to loop to retrieve data.

   In the Xpath query column,
   enter between inverted commas the node of the XML field holding the data you want to
   extract, *CustomerName* in this example.
8. Double-click tFileOutputDelimited to display
   its Basic settings view and define its
   properties.
9. In the File Name field, define or browse to
   the path of the output file you want to write the extracted data in.

   Click Sync columns to retrieve the schema
   from the preceding component. If needed, click the [...] button next to
   Edit schema to view the schema.
10. Save your Job and click F6 to execute
    it.

## Results

tExtractXMLField read and extracted the clients names
under the node CustomerName of the *CustomerDetails*
field of the defined database table.
