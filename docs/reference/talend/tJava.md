<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava · versión 8.0 -->
# tJava

Last updated: 9/30/2026

Extends the functionalities of a Talend Job using custom Java
commands.

tJava enables you to enter personalized
code in order to integrate it in Talend program. You can execute
this code only once.

### In this section

* [tJava Standard properties](/talend/en-US/components/8.0/java-custom-code/tjava-standard-properties)
* [tJava properties for Apache Spark Batch](/talend/en-US/components/8.0/java-custom-code/tjava-properties-for-apache-spark-batch)
* [tJava properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/java-custom-code/tjava-properties-for-apache-spark-streaming)
* [tJava properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/java-custom-code/tjava-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Checking the format of an e-mail address](tlibraryload-tjava-tjava-checking-format-of-e-mail-address-standard-component-this)
* [Printing out a variable content](tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-printing-out-variable-content-standard-component-the)
* [Redirecting the standard output to a file for the entire Job](tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-redirecting-standard-output-to-file-for-entire-job-standard-component "Here is an example of how to redirect the standard output to a file for the entire Job run.")

**Related reference**  

* [Creating Hive external tables based on ADLS Databricks](tjava-tazurefsconfiguration-databricks-gen2-file)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-properties-for-apache-spark-batch -->
# tJava properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJava running in the Spark Batch Job framework.

The Spark Batch
tJava component belongs to the Custom Code family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema et Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Note that if the input value of any non-nullable primitive field is   null, the row of data including that field will be rejected. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Code | Type in the Java code you want to execute to process the incoming RDD from the input link or even create new RDDs out of this input one.  You need to leverage the schema, the link and the component name to write the custom code. For example, if this component is labeled *tJava\_1* and the connection to it is labeled *row1*, then the class of the input RDD is *row1Struct* and the input RDD itself is available with the *rdd\_tJava\_1* variable.  For more detailed instructions, see the default comment provided in the Code field of this component.  For further information about Spark's Java API, see Apache's Spark documentation in <https://spark.apache.org/docs/latest/api/java/index.html>. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Classes | Define the classes that you need to use in the code written in the Code field in the Basic settings view.  It is recommended to define new classes in this field, instead of in the Code field, so as to avoid eventual exceptions in serialization. |
| Import | Enter the Java code to import, if necessary, external libraries used in the Code field of the Basic settings view. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link. |
| Code example | In the Code field of the Basic settings view, enter the following code to create an output RDD by using custom transformations on the input RDD. mapInToOut is a class to be defined in the Classes field in the Advanced settings view. ``` outputrdd_tJava_1 = rdd_tJava_1.map(new mapInToOut(job)); ```  In the Classes field of the Advanced settings view, enter the following code to define the mapInToOut class: ``` public static class mapInToOut implements   org.apache.spark.api.java.function.Function<inputStruct,RecordOut_tJava_1>{       private ContextProperties context = null;      private java.util.List<org.apache.avro.Schema.Field> fieldsList; 		      public mapInToOut(JobConf job) { 	   this.context = new ContextProperties(job);      } 		      @Override      public RecordOut_tJava_1 call(inputStruct origStruct) {		 			 	 if (fieldsList == null) { 	     this.fieldsList = (new inputStruct()).getSchema() 			.getFields(); 	 }  	 RecordOut_tJava_1 value = new RecordOut_tJava_1();  	 for (org.apache.avro.Schema.Field field : fieldsList) { 	      value.put(field.pos(), origStruct.get(field.pos())); 	 }  	 return value;		 			       } } ``` |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Knowledge of Spark and Java language is required. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-properties-for-apache-spark-structured-streaming -->
# tJava properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tJava running in the
Spark Structured Streaming Job framework.

The Spark Structured Streaming
tJava component belongs to the Custom Code family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed by the component. Depending on your Java code, tJava can pass the input dataset as-is or produce a transformed output dataset.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Code | Enter the Java code to process the incoming DataFrame. The DataFrame is available using the variable name composed of the component label and the connection label. For information about the Spark Java API, see the [Apache Spark Java API documentation](https://spark.apache.org/docs/latest/api/java/index.html). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Classes code | Define the classes that you need to use in the code written in the Code field in the Basic settings view.  It is recommended to define new classes in this field, instead of in the Code field, so as to avoid eventual exceptions in serialization. |
| Import | Enter the Java code to import, if necessary, external libraries used in the Code field of the Basic settings view. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Code example | The input dataset is available as ds\_input\_tJava\_1, and the output dataset is available as ds\_output\_tJava\_1. You can modify the input data and pass the modified output dataset to downstream components.  ``` // Print the input stream to the console.       // ds_input_tJava_1.writeStream()       //     .outputMode("append")       //     .format("console")       //     .option("truncate", "false")       //     .option("numRows", 50)       //     .start().awaitTermination();        // Add a column containing the uppercase value of newColumn1 and pass the result downstream.       // Add import static org.apache.spark.sql.functions.*; to the IMPORT section.       ds_output_tJava_1 = ds_input_tJava_1.withColumn(          "newColumn1",          upper(col("newColumn1"))       ); ``` |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-standard-properties -->
# tJava Standard properties

Last updated: 9/30/2026

These properties are used to configure tJava running in the Standard Job framework.

The Standard
tJava component belongs to the Custom Code family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Code | Type in the Java code you want to execute according to the task you need to perform. For further information about Java functions syntax specific to  Talend , see  Talend Studio  Help Contents (Help > Developer Guide > API Reference).  For a complete Java reference, check <http://docs.oracle.com/javaee/6/api/>  Information noteNote: This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source with­out mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  Information noteNote: If your custom Java code references org.talend.transform.runtime.api.ExecutionStatus, change it to org.talend.transform.runtime.common.MapExecutionStatus. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code to import, if necessary, external libraries used in the Code field of the Basic settings view. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used as a one-component subJob. |
| Limitation | You should know Java language. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-databricks-gen2-file -->
# Creating Hive external tables based on ADLS Databricks

Last updated: 9/30/2026

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-setting-up-job?id=2764)
* [Configuring tJava](/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-configuring-tjava?id=2765)
* [Configuring tAzureFSConfiguration](/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-?id=2766)
* [Executing the Job](/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-executing-job?id=2767)

**Related concepts**  

* [tJava](tjava "Extends the functionalities of a Talend Job using custom Java commands.")

**Related information**  

* [tAzureFSConfiguration](/talend/en-US/components/8.0/azure-data-lake-storage-gen2/tazurefsconfiguration)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-printing-out-variable-content-standard-component-the -->
# Printing out a variable content

Last updated: 9/30/2026

The following scenario is a simple demo of the extended application of the
tJava component. The Job aims at printing out the
number of lines being processed using a Java command and the global variable provided in *Talend Studio*.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-select)
* [Configuring the input component](/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-set)
* [Configuring the output component](/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-configuring-output-component-standard-component-set)
* [Configuring the tJava component](/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-configuring-tjava-component-standard-component-then)
* [Executing the Job](/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-executing-job-standard-component-press)

**Related concepts**  

* [tJava](tjava "Extends the functionalities of a Talend Job using custom Java commands.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-redirecting-standard-output-to-file-for-entire-job-standard-component -->
# Redirecting the standard output to a file for the entire Job

Last updated: 9/30/2026

Here is an example of how to redirect the standard output to a file for the entire
Job run.

### In this section

* [Creating a Job for redirecting the standard output to a file](/talend/en-US/components/8.0/java-custom-code/tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-creating-job-for-redirecting-standard-output-to-file-standard-component-create)
* [Configuring the Job for redirecting the standard output to a file](/talend/en-US/components/8.0/java-custom-code/tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-configuring-job-for-redirecting-standard-output-to-file-standard-component)
* [Executing the Job to redirect the standard output to a file](/talend/en-US/components/8.0/java-custom-code/tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-executing-job-to-redirect-standard-output-to-file-standard-component-press)

**Related concepts**  

* [tJava](tjava "Extends the functionalities of a Talend Job using custom Java commands.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration- -->
# Configuring tAzureFSConfiguration

Last updated: 9/30/2026

## Procedure

1. Double-click the component to open its settings.
2. Select Azure Data Lake Storage (Gen2) as
   Azure FileSystem.
3. Select Secret Key as Authentication
   mode.
4. In the Configuration part, enter your Data Lake account
   parameters.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-configuring-tjava -->
# Configuring tJava

Last updated: 9/30/2026

## Before you begin

You have an ADLS Databricks file in your cluster. For
example: abfss://filelocationpath.dfs.core.windows.net/ems/

## Procedure

1. Double-click the component to open its settings.
2. Enter the code in the Code field. For example:

   ss.sql("CREATE EXTERNAL TABLE if not exists talend.test (id int, email
   string)ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'lines terminated by '\n'
   STORED AS TEXTFILE LOCATION
   \'abfss://filelocationpath.dfs.core.windows.net/ems/\'");


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-executing-job -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Save the Job and press F6 to execute it. The table is
   created in your cluster.
2. To check the content, use select \* from
   talend.test in the notebook.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tazurefsconfiguration-setting-up-job -->
# Setting up the Job

Last updated: 9/30/2026

## About this task

* This procedure is specific to ADLS Databricks Gen2.
* You can create this Job in the Big Data Batch or Big Data Streaming node.

## Procedure

1. Drop the following components from the **Palette** onto the design
   workspace: tJava and
   tAzureFSConfiguration.
2. Go to your Databricks account.
3. On the **Configuration** tab of your Databricks cluster page, expand the
   **Advanced options**.
4. In the **Spark** tab, add the following Spark properties: 

   ```
   spark.hadoop.fs.azure.account.key.<storage_account>.dfs.core.windows.net <key>
   ```

   This key is associated with the storage account to be used. You can
   find it in the **Access keys** blade of this storage account. Two
   keys are available for each account and by default, either of them
   can be used for this access.

   Ensure that the account to be used has the appropriate read/write
   rights and permissions.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-set -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Set the Basic settings of the tFileInputDelimited component.
2. Define the path to the input file in the File
   name field.

   The input file used in this example is a simple text file made of two
   columns: *Names* and their respective
   *Emails*.
3. Click the Edit Schema button, and set the
   two-column schema. Then click OK to close
   the dialog box.
4. When prompted, click OK to accept the
   propagation, so that the tFileOutputExcel
   component gets automatically set with the input schema.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-configuring-output-component-standard-component-set -->
# Configuring the output component

Last updated: 9/30/2026

Set the output file to receive the input content without changes. If the file does
not exist already, it will get created.

In this example, the Sheet name is
*Email* and the Include
Header box is selected.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-configuring-tjava-component-standard-component-then -->
# Configuring the tJava component

Last updated: 9/30/2026

## Procedure

1. Then select the tJava component to set
   the Java command to execute.
2. In the Code area, type in the following
   command:

   ```
   String var = "Nb of line processed: ";
   var = var + globalMap.get("tFileInputDelimited_1_NB_LINE");
   System.out.println(var);
   ```

   In this use case, we use the *NB\_Line* variable. To
   access the global variable list, press Ctrl + Space bar on your keyboard and
   select the relevant global parameter.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save
   your Job.
2. Press F6 to execute
   it.

## Results

The content gets passed on to the Excel file defined and the Number of lines
processed are displayed on the Run
console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfileinputdelimited-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-select -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Select and drop the following components from the Palette onto the design workspace: tFileInputDelimited, tFileOutputExcel, tJava.
2. Connect the tFileInputDelimited to the
   tFileOutputExcel using a Row Main connection. The content from a delimited
   txt file will be passed on through the connection to an xls-type of file
   without further transformation.
3. Then connect the tFileInputDelimited
   component to the tJava component using a
   Trigger > On
   Subjob Ok link. This link sets a sequence ordering tJava to be executed at the end of the main
   process.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-configuring-job-for-redirecting-standard-output-to-file-standard-component -->
# Configuring the Job for redirecting the standard output to a file

Last updated: 9/30/2026

## Procedure

1. Double-click the tJava component and in the
   Code field on its Basic
   settings view, enter the following code:

   ```
   java.io.File file = new java.io.File("d:/mytalend.log");
   java.io.PrintStream log_java = new java.io.PrintStream(new java.io.FileOutputStream(file));
   System.setOut(log_java);
   ```

   The standard output of the entire Job will be redirected to the file
   d:/mytalend.log.
2. Double-click the first tFixedFlowInput component to open
   its Basic settings view.
3. Click the […] button next to Edit
   schema and in the dialog box displayed, define the schema by
   adding three columns: `id` of Integer type,
   `name` and `team` of String
   type.
4. In the Mode area, select Use Inline Content
   (delimited file) and in the Content
   field, enter the following input data for the first
   tFixedFlowInput component:

   ```
   1;Lily;QA
   2;Kevin;DEV
   3;Daniel;DEV
   ```
5. Double-click the tFileOutputDelimited component and on
   its Basic settings view, select the Use Output
   Stream check box and enter `System.out` in
   the Output Stream field.
6. Click the Sync columns button to retrieve the schema
   from the previous component.
7. Double-click the second tFixedFlowInput component to
   open its Basic settings view.
8. Define the schema by adding three columns, same as the first
   tFixedFlowInput component.
9. In the Mode area, select Use Inline Content
   (delimited file) and in the Content
   field, enter the following input data for the second
   tFixedFlowInput component:

   ```
   4;Allen;DOC
   5;Judy;DOC
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-creating-job-for-redirecting-standard-output-to-file-standard-component-create -->
# Creating a Job for redirecting the standard output to a file

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tPrejob component, a
   tJava component, two
   tFixedFlowInput components, a
   tFileOutputDelimited component, and a
   tLogRow component to the Job.
2. Link the tPrejob component to the
   tJava component using a Trigger > On Component Ok connection.
3. Link the first tFixedFlowInput component to the
   tFileOutputDelimited component using a Row > Main connection.
4. Link the second tFixedFlowInput component to the
   tLogRow component using a Row > Main connection.
5. Link the first tFixedFlowInput component to the second
   tFixedFlowInput component using a Trigger > On Subjob Ok connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/java-custom-code/tjava-tfixedflowinput-tfileoutputdelimited-tlogrow-executing-job-to-redirect-standard-output-to-file-standard-component-press -->
# Executing the Job to redirect the standard output to a file

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   You will see the input data from the two
   tFixedFlowInput components are written into the file
   d:/mytalend.log.
