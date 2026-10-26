<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tdynamodblookupinput · versión 8.0 -->
# tDynamoDBLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a database query with a strictly defined order which must correspond to
the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDynamoDBLookupInput properties for Apache Spark Streaming

These properties are used to configure tDynamoDBLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tDynamoDBLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Access Key | Enter the access key ID that uniquely identifies an AWS Account. For further information about how to get your Access Key and Secret Key, see [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html). |
| Secret Key | Enter the secret access key, constituting the security credentials in combination with the access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Region | Specify the AWS region by selecting or entering a region name between double quotation marks (e.g. *"us-east-1"*). For more information about the AWS Region, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region). |
| Use End Point | Select this check box and in the Server URL field displayed, specify the Web service URL of the DynamoDB database service. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Specify the name of the table from which the lookup data is extracted. |
| Advanced key condition expression | Enter the key condition expressions used to determine the items to be read from the table or index.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |
| Value mapping | Specify the placeholders for the expression attribute values.   * value: Enter the expression attribute   value. * placeholder: Specify the placeholder for the   corresponding value.   For more information, see [Expression Attribute Values](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ExpressionPlaceholders.html#ExpressionAttributeValues). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced properties | Add properties to define extra operations you need tDynamoDBInput to perform when reading data.  This table is present for future evolution of the component and using it requires the high-level knowledge of DynamoDB development. Currently, there are no interesting user configurable properties. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tDynamoDBConfiguration component present in the same Job to connect to a DynamoDB database. You need to drop a tDynamoDBConfiguration component alongside this component and configure the Basic settings of this component to use tDynamoDBConfiguration.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tdynamodblookupinput -->
# tDynamoDBLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a database query with a strictly defined order which must correspond to
the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDynamoDBLookupInput properties for Apache Spark Streaming

These properties are used to configure tDynamoDBLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tDynamoDBLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Access Key | Enter the access key ID that uniquely identifies an AWS Account. For further information about how to get your Access Key and Secret Key, see [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html). |
| Secret Key | Enter the secret access key, constituting the security credentials in combination with the access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Region | Specify the AWS region by selecting or entering a region name between double quotation marks (e.g. *"us-east-1"*). For more information about the AWS Region, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region). |
| Use End Point | Select this check box and in the Server URL field displayed, specify the Web service URL of the DynamoDB database service. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Specify the name of the table from which the lookup data is extracted. |
| Advanced key condition expression | Enter the key condition expressions used to determine the items to be read from the table or index.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |
| Value mapping | Specify the placeholders for the expression attribute values.   * value: Enter the expression attribute   value. * placeholder: Specify the placeholder for the   corresponding value.   For more information, see [Expression Attribute Values](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ExpressionPlaceholders.html#ExpressionAttributeValues). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced properties | Add properties to define extra operations you need tDynamoDBInput to perform when reading data.  This table is present for future evolution of the component and using it requires the high-level knowledge of DynamoDB development. Currently, there are no interesting user configurable properties. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tDynamoDBConfiguration component present in the same Job to connect to a DynamoDB database. You need to drop a tDynamoDBConfiguration component alongside this component and configure the Basic settings of this component to use tDynamoDBConfiguration.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
