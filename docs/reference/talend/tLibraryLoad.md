<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload · versión 8.0 -->
# tLibraryLoad

Last updated: 9/30/2026

Loads useable Java libraries in a Job.

### In this section

* [tLibraryLoad Standard properties](/talend/en-US/components/8.0/library-import/tlibraryload-standard-properties)
* [tLibraryLoad properties for Apache Spark Batch](/talend/en-US/components/8.0/library-import/tlibraryload-properties-for-apache-spark-batch)
* [tLibraryLoad properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/library-import/tlibraryload-properties-for-apache-spark-streaming?id=3052)
* [tLibraryLoad properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/library-import/tlibraryload-properties-for-apache-spark-streaming?id=3053)

**Related concepts**  

* [Checking the format of an e-mail address](tlibraryload-tjava-tjava-checking-format-of-e-mail-address-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-properties-for-apache-spark-batch -->
# tLibraryLoad properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tLibraryLoad running in the Spark Batch Job
framework.

The Spark Batch
tLibraryLoad component belongs to the Custom Code family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Library | Click on the [...] button to open the Module dialog box from which you can import the library to be used.  For more information, see [Importing an external library](/talend/r/en-US/8.0/components/library-import/importing-external-library). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code required to import, if required, the external library used in the code editing field of the Basic settings tab of the components such as tJavaMR in a Map/Reduce Job. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | The library is loaded locally. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-properties-for-apache-spark-streaming -->
# tLibraryLoad properties for Apache Spark Streaming (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

These properties are used to configure tLibraryLoad running in
the Spark Streaming Job framework.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

The Spark Streaming
tLibraryLoad component belongs to the Custom Code family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Library | Click on the [...] button to open the Module dialog box from which you can import the library to be used.  For more information, see [Importing an external library](/talend/r/en-US/8.0/components/library-import/importing-external-library). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code required to import, if required, the external library used in the code editing field of the Basic settings tab of the components such as tJavaMR in a Map/Reduce Job. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | The library is loaded locally. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-standard-properties -->
# tLibraryLoad Standard properties

Last updated: 9/30/2026

These properties are used to configure tLibraryLoad running in the Standard Job
framework.

The Standard
tLibraryLoad component belongs to the Custom Code family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Library | Click on the [...] button to open the Module dialog box from which you can import the library to be used.  For more information, see [Importing an external library](/talend/r/en-US/8.0/components/library-import/importing-external-library). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Dynamic Libs | Lib Paths: Enter the access path to your library, between double quotation marks. |
| Import | Enter the Java code required to import, if required, the external library used in the code editing field of the Basic settings tab of the components such as tJava,or tJavaFlex. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component may be used alone, although it is more logical to use it as part of a Job. |
| Limitation | The library is loaded locally. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-checking-format-of-e-mail-address-standard-component-this -->
# Checking the format of an e-mail address

Last updated: 9/30/2026

This scenario uses two components, a tLibraryLoad and
a tJava. The goal of this scenario is to check the
format of an e-mail address and verify whether the format is valid or not.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-setting-up-job-standard-component-in?id=3055)
* [Configuring the tLibraryLoad component](/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-configuring-tlibraryload-component-standard-component-import?id=3056)
* [Configuring the tJava component](/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-configuring-tjava-component-standard-component?id=3057)
* [Job execution](/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-job-execution-standard-component-press-f6?id=3058)

**Related concepts**  

* [tLibraryLoad](tlibraryload "Loads useable Java libraries in a Job.")

**Related information**  

* [tJava](/talend/en-US/components/8.0/java-custom-code/tjava)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-configuring-tjava-component-standard-component -->
# Configuring the tJava component

Last updated: 9/30/2026

## Procedure

1. Double-click on tJava to display its
   Component view.
2. In the Basic settings tab, enter your
   code, as in the screenshot below. The code allows you to check whether the
   character string pertains to an e-mail address, based on the regular
   expression: "^[\\w\_.-]+@[\\w\_.-]+\\.[\\w]+$".


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-configuring-tlibraryload-component-standard-component-import -->
# Configuring the tLibraryLoad component

Last updated: 9/30/2026

## Procedure

1. Import the external library to be used in the Job.
   1. Double-click on tLibraryLoad to display
      its Basic settings.
   2. Click the [...] button to open the
      Module dialog box.
   3. Select `jakarta-oro-2.0.8.jar` from the
      Platform list.
   4. Click OK to confirm loading the library and clode the
      dialob box.
2. In the Import field of the
   Advanced settings tab, type
   `import org.apache.oro.text.regex.*;`


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-job-execution-standard-component-press-f6 -->
# Job execution

Last updated: 9/30/2026

Press F6 to save and run the Job.

The Console displays the boolean
*false*. Hence, the e-mail address is not valid as the format
is incorrect.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/library-import/tlibraryload-tjava-tjava-setting-up-job-standard-component-in -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. In the Palette, open the Custom\_Code folder, and slide a tLibraryLoad and tJava
   component onto the workspace.
2. Connect tLibraryLoad to tJava using a Trigger > OnSubjobOk
   link.
