<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput · versión 8.0 -->
# tFixedFlowInput

Last updated: 9/30/2026

### In this section

* [tFixedFlowInput component](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-component -->
# tFixedFlowInput component

Last updated: 9/30/2026

| [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput) | Generates a fixed flow from internal variables. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput -->
# tFixedFlowInput

Last updated: 9/30/2026

Generates a fixed flow from internal variables.

### In this section

* [tFixedFlowInput Standard properties](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
* [tFixedFlowInput properties for Apache Spark Batch](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-properties-for-apache-spark-batch)
* [tFixedFlowInput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-properties-for-apache-spark-batch -->
# tFixedFlowInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFixedFlowInput running in the Spark Batch Job framework.

The Spark Batch
tFixedFlowInput component belongs to the Misc family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields that will be processed and passed on to the next component. The schema is either built-in or remote in the Repository.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Built-in: The schema will be created and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).  Repository: You have already created the schema and stored it in the Repository, hence can be reused in various projects and Job designs. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Mode | From the three options, select the mode that you want to use.  Use Single Table : Enter the data that you want to generate in the relevant value field.  Use Inline Table : Add the row(s) that you want to generate.  Use Inline Content : Enter the data that you want to generate, separated by the separators that you have already defined in the Row and Field Separator fields. |
| Number of rows | Enter the number of lines to be generated. |
| Values | Between inverted commas, enter the values corresponding to the columns you defined in the schema dialog box using the Edit schema button. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set the number of partitions | Select this check box and then enter the number of partitions into which you want to dispatch the input rows.  If you leave this check box clear, each input row forms a partition. For example, with *5* in the Number of rows field, each row is handled as one partition and thus they make 5 partitions in total. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties -->
# tFixedFlowInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tFixedFlowInput running in the Standard Job framework.

The Standard
tFixedFlowInput component belongs to the Misc family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields that will be processed and passed on to the next component. The schema is either built-in or remote in the Repository.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Built-in: The schema will be created and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).  Repository: You have already created the schema and stored it in the Repository, hence can be reused in various projects and Job designs. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Mode | From the three options, select the mode that you want to use.  Use Single Table : Enter the data that you want to generate in the relevant value field.  Use Inline Table : Add the row(s) that you want to generate.  Use Inline Content : Enter the data that you want to generate, separated by the separators that you have already defined in the Row and Field Separator fields. |
| Number of rows | Enter the number of lines to be generated. |
| Values | Between inverted commas, enter the values corresponding to the columns you defined in the schema dialog box using the Edit schema button. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStat Catcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a start or intermediate component and thus requires an output component. |
