<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/technical/tcollectandcheck · versión 8.0 -->
# tCollectAndCheck

Last updated: 9/30/2026

Shows and validates the result of a component test.

tCollectAndCheck is available only in a test case about a given
component and is added automatically to the test case you are using. For further
information about test cases, see [Testing Spark Jobs using test cases](/talend/r/en-US/8.0/studio-user-guide/testing-spark-jobs-using-test-cases).

tCollectAndCheck
receives output from a component being tested, loads given reference files to be compare
with this output and returns whether the output matches the expected result.

### In this section

* [tCollectAndCheck properties for Apache Spark Batch](/talend/en-US/components/8.0/technical/tcollectandcheck-properties-for-apache-spark-batch)
* [tCollectAndCheck properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/technical/tcollectandcheck-properties-for-apache-spark-streaming)
* [tCollectAndCheck properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/technical/tcollectandcheck-properties-for-apache-spark-structured-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/technical/tcollectandcheck-properties-for-apache-spark-batch -->
# tCollectAndCheck properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tCollectAndCheck running in the Spark Batch Job framework.

The Spark Batch
tCollectAndCheck component belongs to the Technical family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Configuration | Select this check box to retrieve connection information and credentials from a configuration component. You must select this check box for the following type of input data to be checked:  * HBase * JDBC * MySQL * Redshift * Snowflake   In the drop-down list that appears, select the configuration component from which you want Spark to use the configuration details to connect to the database. For example, if you want to check Snowflake data, you have to select the tSnowflakeConfiguration component.  Information noteNote: If you want to retrieve data from S3, you do not have to use tS3Configuration, you only have to enter the full path of the file in the Path or table name field from the Basic settings view. |
| Type of input | Select the type of input data to be checked from the drop-down list. |
| Path or table name | Enter the path to the file or the table to be checked in double quotation marks. |
| Separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Line separator | The separator used to identify the end of a row. |
| Use context variable | If you have already created the context variable representing the reference file to be used, select this check box and enter this variable in the Variable name field that is displayed.  Then syntax to call a variable is *context.VariableName*.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |
| Reference data | If you do not want to use context variables to represent the reference data to be used, enter this reference data directly in this field.  Information noteNote: Due to the migration of the component from RDD to dataset, the pattern for a date can only be `yyyy-MM-dd`, and the pattern for a timestamp can only be `yyyy-MM-dd HH:mm:ss`.  This applies for Spark 2.1 or a higher version. |
| Keep the order from the reference | If the RDDs to be checked are sorted, select this check box to keep your reference data ordered. |

## Advanced settings

| Properties | Description |
| --- | --- |
| When the reference is empty, expect no incoming value | By default, this check box is clear, meaning that when an field in the reference data is empty, the test expects an equally empty field in the incoming datasets being verified in order to validate the test result.  If you want the test to expect no value when the reference is empty, select this check box. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component is added automatically to a test case being created to show the test result in the console of the Run view. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/technical/tcollectandcheck-properties-for-apache-spark-structured-streaming -->
# tCollectAndCheck properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tCollectAndCheck running
in the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tCollectAndCheck component belongs to the Technical family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Configuration | Select this check box to retrieve connection information and credentials from a configuration component. You must select this check box for the following types of input data to be checked:  * HBase * JDBC * MySQL * Redshift   In the drop-down list that appears, select the configuration component from which Spark uses the configuration details to connect to the database. For example, to check Snowflake data, select the tSnowflakeConfiguration component.  Information noteNote: If you want to retrieve data from S3, you do not have to use tS3Configuration. Enter the full path of the file in the Path or table name field instead. |
| Type of input | Select the type of input data to check from the drop-down list. |
| Path or table name | Enter the file path or table name in double quotation marks. |
| Separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Line separator | The separator used to identify the end of a row. |
| Use context variable | If you have already created the context variable representing the reference file to be used, select this check box and enter this variable in the Variable name field that is displayed.  The syntax to call a variable is context.VariableName.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |
| Reference data | If you do not want to use context variables to represent the reference data to be used, enter this reference data directly in this field. |
| Keep the order from the reference | If the RDDs to be checked are sorted, select this check box to keep your reference data ordered. |
| Output mode | Select the output mode from the drop-down list:  * Append: adds new rows to the output table without   modifying existing rows. * Complete: overwrites the entire output table with   the updated result after every trigger. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used as an end component and requires an input link.  This component is added automatically to a test case being created to show the test result in the console of the Run view.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |
