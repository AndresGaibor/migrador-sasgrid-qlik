<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow · versión 8.0 -->
# tJavaRow

Last updated: 9/30/2026

Provides a code editor that lets you enter the Java code to be applied to each row
of the flow.

tJavaRow allows you to enter customized
code which you can integrate in a Talend program.

### In this section

* [tJavaRow Standard properties](/talend/en-US/components/8.0/java-custom-code/tjavarow-standard-properties)
* [tJavaRow properties for Apache Spark Batch](/talend/en-US/components/8.0/java-custom-code/tjavarow-properties-for-apache-spark-batch)
* [tJavaRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/java-custom-code/tjavarow-properties-for-apache-spark-streaming)

**Related concepts**  

* [Transforming data line by line using tJavaRow](tjavarow-tfileinputdelimited-transforming-data-line-by-line-using-tjavarow-standard-component-in-this)
* [Using tJavaRow to handle file content based on a dynamic schema](tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-using-tjavarow-to-handle-file-content-based-on-dynamic-schema-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-properties-for-apache-spark-batch -->
# tJavaRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJavaRow running in the Spark Batch Job framework.

The Spark Batch
tJavaRow component belongs to the Custom Code family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Note that the input schema and the output schema of this component can   be different. |
| Map type | Select the type of the Map transformation you need to write. This allows the component to automatically select the method accordingly and declare the variables to be used in your custom code.  The available types are:  * Map: it returns only one   output record for each input record. It uses Spark's   *PairFunction*   method * FlatMap: it returns 0 or   more output records for each input record. It uses Spark's   *FlatMapFunction*   method.  For further information about these methods, see Apache Spark's documentation about its Java API in <https://spark.apache.org/docs/latest/api/java/index.html>. |
| Generate code | Click this button to automatically generate the code in the Code field to map the columns of the input schema with those of the output schema. This generation does not change anything in your schema.  The generated sample code shows what the pre-defined variables are for the input and the output RDDs and how these variables can be used. |
| Code | Write the custom body of the method you have selected from the Map type drop-down list. You need to use the input schema and the output schema to manage the columns of the input and the output RDD records. This custom code is applied on a row-by-row basis in the RDD records.  For example, the input schema contains a *user* column, then you need to use the *input.user* variable to get the *user* column of each input record.  For further information about the available variables in writing the custom code, see the default comment displayed in this field. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code to import, if necessary, external libraries used in the Code field of the Basic settings view. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  To enter a global variable (for example *COUNT* of tFileRowCount) in the Code box, you need to type in the entire piece of code manually, that is to say *((Integer)globalMap.get("tFileRowCount\_COUNT"))*. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Knowledge of Spark and Java language is necessary. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-standard-properties -->
# tJavaRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tJavaRow running in the Standard Job framework.

The Standard
tJavaRow component belongs to the Custom Code family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job. |
| Generate code | Click this button to automatically generate the code in the Code field to map the columns of the input schema with those of the output schema. This generation does not change anything in your schema.  The principle of this mapping is to relate the columns that have the same column name. Then you can adapt the generated code depending on the actual map you need. |
| Code | Enter the Java code to be applied to each line of the data flow. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code to import, if necessary, external libraries used in the Code field of the Basic settings view. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level.. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  To enter a global variable (for example *COUNT* of tFileRowCount) in the Code box, you need to type in the entire piece of code manually, that is to say *((Integer)globalMap.get("tFileRowCount\_COUNT"))*. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediary between two other components. It must be linked to both an input and an output component. |
| Function | tJavaRow allows you to enter customized code which you can integrate in a Talend programme. With tJavaRow, you can enter the Java code to be applied to each row of the flow. |
| Purpose | tJavaRow allows you to broaden the functionality of  Talend  Jobs, using the Java language. |
| Limitation | Knowledge of Java language is necessary. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-using-tjavarow-to-handle-file-content-based-on-dynamic-schema-standard-component-enterprise-this -->
# Using tJavaRow to handle file content based on a dynamic schema

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

This scenario describes a three-component Job that uses Java code through a tJavaRow component to display the content of an input file
and pass it to the output component. As all the components in this Job support the
dynamic schema feature, we can leverage this feature to save the time of configuring
each column of the schema.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input and output components](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-and-output-components-standard-component-enterprise)
* [Configuring the tJavaRow component](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-tjavarow-component-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-saving-and-executing-job-standard-component-enterprise-press)

**Related concepts**  

* [tJavaRow](tjavarow "Provides a code editor that lets you enter the Java code to be applied to each row of the flow.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-transforming-data-line-by-line-using-tjavarow-standard-component-in-this -->
# Transforming data line by line using tJavaRow

Last updated: 9/30/2026

In this scenario, the information of a few cities read from an input delimited file is
transformed using Java code through the tJavaRow
component and printed on the console.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-setting-up-job-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tJavaRow](tjavarow "Provides a code editor that lets you enter the Java code to be applied to each row of the flow.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-and-output-components-standard-component-enterprise -->
# Configuring the input and output components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component, which is labeled *Source*, to
   display its Basic settings view. 

   Information noteWarning:

   *The dynamic schema feature is only supported in Built-In mode and requires the input file
   to have a header row.*
2. In the File name/Stream field, type in
   the path to the input file in double quotation marks, or browse to the path
   by clicking the [...] button.
3. In the Header field, type in *1* to define the first line of the file as the
   header.
4. Click the [...] button next to Edit schema to open the Schema dialog box.
5. Click the [+] button to add a column,
   give a name to the column, *dyna* in this
   example, and select Dynamic from the
   Type list. This dynamic column will
   retrieve the three columns, *FirstName*,
   *LastName* and *Address*, of the input file.
6. Click OK to validate the setting and
   close the dialog box.
7. Double-click the tFileOutputDelimited
   component, which is labeled *Target*, to
   display its Basic settings view.
8. Define the output file path in the File
   Name field.
9. Select the Include Header check box to
   include the header in the output file. Leave all the other settings are they
   are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-tjavarow-component-standard-component-enterprise -->
# Configuring the tJavaRow component

Last updated: 9/30/2026

## Procedure

1. Double-click tJavaRow to display its
   Basic settings view and define the
   components properties.
2. Click Sync columns to make sure that the
   schema is correctly retrieved from the preceding component.
3. In the Code field, enter the following
   code to display the content of the input file and pass the data to the next
   component based on the defined dynamic schema column:

   ```
   System.out.println(input_row.dyna);
   output_row.dyna = input_row.dyna;
   ```

   Information noteNote:

   In the Code field, input\_row and output\_row correspond to the links to and from tJavaRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Pressing F6, or click Run on the Run
   tab to execute the Job.

   The content of the input file is displayed on the console and written to
   the output file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop tFileInputDelimited, tJavaRow, and tFileOutputDelimited from the Palette onto the design workspace, and label them according
   to their roles in the Job.
2. Connect the components in a series using Row > Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to display its Basic settings
   view in the Component tab.
2. In the File name/Stream field, type in
   the path to the input file in double quotation marks, or browse to the path
   by clicking the [...] button, and define
   the first line of the file as the header.

   In this example, the input file has the following content:

   ```
   City;Population;LandArea;PopDensity
   Beijing;10233000;1418;7620
   Moscow;10452000;1081;9644
   Seoul;10422000;605;17215
   Tokyo;8731000;617;14151
   New York;8310000;789;10452
   ```
3. Click the [...] button next to Edit
   schema to open the Schema dialog box, and
   define the data structure of the input file. Then, click OK to validate the schema setting and close the
   dialog box.
4. Double-click the tJavaRow component to
   display its Basic settings view in the
   Component tab.
5. Click Sync columns to make sure that the
   schema is correctly retrieved from the preceding component.
6. In the Code field, enter the code to be
   applied on each line of data based on the defined schema columns.

   In this example, we want to transform the city names to upper case, group
   digits of numbers larger than 1000 using the thousands separator for ease of
   reading, and print the data on the console:

   ```
   System.out.print("\n" + input_row.City.toUpperCase() + ":");
   System.out.print("\n - Population: " 
   + FormatterUtils.format_Number(String.valueOf(input_row.Population), ',', '.') + " people");
   System.out.print("\n - Land area: " 
   + FormatterUtils.format_Number(String.valueOf(input_row.LandArea), ',', '.') 
   + " km2");
   System.out.print("\n - Population density: " 
   + FormatterUtils.format_Number(String.valueOf(input_row.PopDensity), ',', '.') + " people/km2\n");
   ```

   Information noteNote:

   In the Code field, input\_row refers to the link that connects to
   tJavaRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The city information is transformed by the Java code set through tJavaRow and displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop a tFileInputDelimited component and
   a tJavaRow component from the Palette onto the design workspace, and label them
   to better identify their roles in the Job.
2. Connect the two components using a Row >
   Main connection.
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-standard-properties · versión 8.0 -->
# tJavaRow Standard properties

Last updated: 9/30/2026

These properties are used to configure tJavaRow running in the Standard Job framework.

The Standard
tJavaRow component belongs to the Custom Code family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job. |
| Generate code | Click this button to automatically generate the code in the Code field to map the columns of the input schema with those of the output schema. This generation does not change anything in your schema.  The principle of this mapping is to relate the columns that have the same column name. Then you can adapt the generated code depending on the actual map you need. |
| Code | Enter the Java code to be applied to each line of the data flow. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code to import, if necessary, external libraries used in the Code field of the Basic settings view. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level.. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  To enter a global variable (for example *COUNT* of tFileRowCount) in the Code box, you need to type in the entire piece of code manually, that is to say *((Integer)globalMap.get("tFileRowCount\_COUNT"))*. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediary between two other components. It must be linked to both an input and an output component. |
| Function | tJavaRow allows you to enter customized code which you can integrate in a Talend programme. With tJavaRow, you can enter the Java code to be applied to each row of the flow. |
| Purpose | tJavaRow allows you to broaden the functionality of  Talend  Jobs, using the Java language. |
| Limitation | Knowledge of Java language is necessary. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow -->
# tJavaRow

Last updated: 9/30/2026

Provides a code editor that lets you enter the Java code to be applied to each row
of the flow.

tJavaRow allows you to enter customized
code which you can integrate in a Talend program.

### In this section

* [tJavaRow Standard properties](/talend/en-US/components/8.0/java-custom-code/tjavarow-standard-properties)
* [tJavaRow properties for Apache Spark Batch](/talend/en-US/components/8.0/java-custom-code/tjavarow-properties-for-apache-spark-batch)
* [tJavaRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/java-custom-code/tjavarow-properties-for-apache-spark-streaming)

**Related concepts**  

* [Transforming data line by line using tJavaRow](tjavarow-tfileinputdelimited-transforming-data-line-by-line-using-tjavarow-standard-component-in-this)
* [Using tJavaRow to handle file content based on a dynamic schema](tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-using-tjavarow-to-handle-file-content-based-on-dynamic-schema-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-properties-for-apache-spark-batch -->
# tJavaRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJavaRow running in the Spark Batch Job framework.

The Spark Batch
tJavaRow component belongs to the Custom Code family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Note that the input schema and the output schema of this component can   be different. |
| Map type | Select the type of the Map transformation you need to write. This allows the component to automatically select the method accordingly and declare the variables to be used in your custom code.  The available types are:  * Map: it returns only one   output record for each input record. It uses Spark's   *PairFunction*   method * FlatMap: it returns 0 or   more output records for each input record. It uses Spark's   *FlatMapFunction*   method.  For further information about these methods, see Apache Spark's documentation about its Java API in <https://spark.apache.org/docs/latest/api/java/index.html>. |
| Generate code | Click this button to automatically generate the code in the Code field to map the columns of the input schema with those of the output schema. This generation does not change anything in your schema.  The generated sample code shows what the pre-defined variables are for the input and the output RDDs and how these variables can be used. |
| Code | Write the custom body of the method you have selected from the Map type drop-down list. You need to use the input schema and the output schema to manage the columns of the input and the output RDD records. This custom code is applied on a row-by-row basis in the RDD records.  For example, the input schema contains a *user* column, then you need to use the *input.user* variable to get the *user* column of each input record.  For further information about the available variables in writing the custom code, see the default comment displayed in this field. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code to import, if necessary, external libraries used in the Code field of the Basic settings view. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  To enter a global variable (for example *COUNT* of tFileRowCount) in the Code box, you need to type in the entire piece of code manually, that is to say *((Integer)globalMap.get("tFileRowCount\_COUNT"))*. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Knowledge of Spark and Java language is necessary. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-using-tjavarow-to-handle-file-content-based-on-dynamic-schema-standard-component-enterprise-this -->
# Using tJavaRow to handle file content based on a dynamic schema

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

This scenario describes a three-component Job that uses Java code through a tJavaRow component to display the content of an input file
and pass it to the output component. As all the components in this Job support the
dynamic schema feature, we can leverage this feature to save the time of configuring
each column of the schema.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input and output components](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-and-output-components-standard-component-enterprise)
* [Configuring the tJavaRow component](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-tjavarow-component-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-saving-and-executing-job-standard-component-enterprise-press)

**Related concepts**  

* [tJavaRow](tjavarow "Provides a code editor that lets you enter the Java code to be applied to each row of the flow.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-transforming-data-line-by-line-using-tjavarow-standard-component-in-this -->
# Transforming data line by line using tJavaRow

Last updated: 9/30/2026

In this scenario, the information of a few cities read from an input delimited file is
transformed using Java code through the tJavaRow
component and printed on the console.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-setting-up-job-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tJavaRow](tjavarow "Provides a code editor that lets you enter the Java code to be applied to each row of the flow.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-input-and-output-components-standard-component-enterprise -->
# Configuring the input and output components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component, which is labeled *Source*, to
   display its Basic settings view. 

   Information noteWarning:

   *The dynamic schema feature is only supported in Built-In mode and requires the input file
   to have a header row.*
2. In the File name/Stream field, type in
   the path to the input file in double quotation marks, or browse to the path
   by clicking the [...] button.
3. In the Header field, type in *1* to define the first line of the file as the
   header.
4. Click the [...] button next to Edit schema to open the Schema dialog box.
5. Click the [+] button to add a column,
   give a name to the column, *dyna* in this
   example, and select Dynamic from the
   Type list. This dynamic column will
   retrieve the three columns, *FirstName*,
   *LastName* and *Address*, of the input file.
6. Click OK to validate the setting and
   close the dialog box.
7. Double-click the tFileOutputDelimited
   component, which is labeled *Target*, to
   display its Basic settings view.
8. Define the output file path in the File
   Name field.
9. Select the Include Header check box to
   include the header in the output file. Leave all the other settings are they
   are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-configuring-tjavarow-component-standard-component-enterprise -->
# Configuring the tJavaRow component

Last updated: 9/30/2026

## Procedure

1. Double-click tJavaRow to display its
   Basic settings view and define the
   components properties.
2. Click Sync columns to make sure that the
   schema is correctly retrieved from the preceding component.
3. In the Code field, enter the following
   code to display the content of the input file and pass the data to the next
   component based on the defined dynamic schema column:

   ```
   System.out.println(input_row.dyna);
   output_row.dyna = input_row.dyna;
   ```

   Information noteNote:

   In the Code field, input\_row and output\_row correspond to the links to and from tJavaRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Pressing F6, or click Run on the Run
   tab to execute the Job.

   The content of the input file is displayed on the console and written to
   the output file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-tfileoutputdelimited-tfileoutputdelimited-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop tFileInputDelimited, tJavaRow, and tFileOutputDelimited from the Palette onto the design workspace, and label them according
   to their roles in the Job.
2. Connect the components in a series using Row > Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to display its Basic settings
   view in the Component tab.
2. In the File name/Stream field, type in
   the path to the input file in double quotation marks, or browse to the path
   by clicking the [...] button, and define
   the first line of the file as the header.

   In this example, the input file has the following content:

   ```
   City;Population;LandArea;PopDensity
   Beijing;10233000;1418;7620
   Moscow;10452000;1081;9644
   Seoul;10422000;605;17215
   Tokyo;8731000;617;14151
   New York;8310000;789;10452
   ```
3. Click the [...] button next to Edit
   schema to open the Schema dialog box, and
   define the data structure of the input file. Then, click OK to validate the schema setting and close the
   dialog box.
4. Double-click the tJavaRow component to
   display its Basic settings view in the
   Component tab.
5. Click Sync columns to make sure that the
   schema is correctly retrieved from the preceding component.
6. In the Code field, enter the code to be
   applied on each line of data based on the defined schema columns.

   In this example, we want to transform the city names to upper case, group
   digits of numbers larger than 1000 using the thousands separator for ease of
   reading, and print the data on the console:

   ```
   System.out.print("\n" + input_row.City.toUpperCase() + ":");
   System.out.print("\n - Population: " 
   + FormatterUtils.format_Number(String.valueOf(input_row.Population), ',', '.') + " people");
   System.out.print("\n - Land area: " 
   + FormatterUtils.format_Number(String.valueOf(input_row.LandArea), ',', '.') 
   + " km2");
   System.out.print("\n - Population density: " 
   + FormatterUtils.format_Number(String.valueOf(input_row.PopDensity), ',', '.') + " people/km2\n");
   ```

   Information noteNote:

   In the Code field, input\_row refers to the link that connects to
   tJavaRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The city information is transformed by the Java code set through tJavaRow and displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjavarow-tfileinputdelimited-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop a tFileInputDelimited component and
   a tJavaRow component from the Palette onto the design workspace, and label them
   to better identify their roles in the Job.
2. Connect the two components using a Row >
   Main connection.
