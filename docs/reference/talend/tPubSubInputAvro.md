<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tpubsubinputavro · versión 8.0 -->
# tPubSubInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Connects to Google Cloud Pub/Sub to receive messages in the Avro format for the
components that run transformations over these messages.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tPubSubInputAvro properties for Apache Spark Streaming

These properties are used to configure tPubSubInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tPubSubInputAvro component belongs to the Messaging family.

If you are using Dataproc 1.4 and onwards as your Spark cluster,
make sure to select the Allow API access to all Google Cloud services in the
same project check box at the cluster creation on Google Cloud Platform to be able
to run PubService.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a Google Cloud configuration component | If you are using Dataproc as your Spark cluster, clear this check box.  Otherwise, select this check box to allow the Pub/Sub component to use the Google Cloud configuration information provided by a tGoogleCloudConfiguration component. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Note that the schema defined here must correspond exactly to the binary Avro schema of the messages received on Pub/Sub. To guarantee this, you can create another Spark Streaming Job to define a given schema using tWriteAvroFields and write the messages with this schema using tPubSubOutput. |
| Topic name | Enter the name of topic from which you want to consume the messages. |
| Subscription name | Enter the name of the subscription that needs to consume the specified topic.  If the subscription exists, it must be connected to the given topic; if the subscription does not exist, it is created and connected to the given topic at runtime. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Storage level | From the Storage level drop-down list that is displayed, select how the cached RDDs are stored, such as in memory only or in memory and on disk.  For further information about each of the storage level, see <https://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence>. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used as a start component and requires an output link. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| PubSub access permissions | When you use Pub/Sub with a Dataproc cluster, ensure that this cluster has the appropriate permissions to access the Pub/Sub service.  To do this, you can create the Dataproc cluster by checking Allow API access to all Google Cloud services in the same project in the advanced options on Google Cloud Platform, or via the command line, assigning the scopes explicitly (the following example is for a low-resource test cluster): ``` gcloud beta dataproc clusters create CLUSTER_ID \     --zone europe-west1-b \     --master-machine-type n1-standard-2 \     --master-boot-disk-size 50 \     --num-workers 2 \     --worker-machine-type n1-standard-2 \     --worker-boot-disk-size 50 \     --scopes 'https://www.googleapis.com/auth/cloud-platform' \     --project PROJECT_ID ``` |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tpubsubinputavro -->
# tPubSubInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Connects to Google Cloud Pub/Sub to receive messages in the Avro format for the
components that run transformations over these messages.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tPubSubInputAvro properties for Apache Spark Streaming

These properties are used to configure tPubSubInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tPubSubInputAvro component belongs to the Messaging family.

If you are using Dataproc 1.4 and onwards as your Spark cluster,
make sure to select the Allow API access to all Google Cloud services in the
same project check box at the cluster creation on Google Cloud Platform to be able
to run PubService.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a Google Cloud configuration component | If you are using Dataproc as your Spark cluster, clear this check box.  Otherwise, select this check box to allow the Pub/Sub component to use the Google Cloud configuration information provided by a tGoogleCloudConfiguration component. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Note that the schema defined here must correspond exactly to the binary Avro schema of the messages received on Pub/Sub. To guarantee this, you can create another Spark Streaming Job to define a given schema using tWriteAvroFields and write the messages with this schema using tPubSubOutput. |
| Topic name | Enter the name of topic from which you want to consume the messages. |
| Subscription name | Enter the name of the subscription that needs to consume the specified topic.  If the subscription exists, it must be connected to the given topic; if the subscription does not exist, it is created and connected to the given topic at runtime. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Storage level | From the Storage level drop-down list that is displayed, select how the cached RDDs are stored, such as in memory only or in memory and on disk.  For further information about each of the storage level, see <https://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence>. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used as a start component and requires an output link. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| PubSub access permissions | When you use Pub/Sub with a Dataproc cluster, ensure that this cluster has the appropriate permissions to access the Pub/Sub service.  To do this, you can create the Dataproc cluster by checking Allow API access to all Google Cloud services in the same project in the advanced options on Google Cloud Platform, or via the command line, assigning the scopes explicitly (the following example is for a low-resource test cluster): ``` gcloud beta dataproc clusters create CLUSTER_ID \     --zone europe-west1-b \     --master-machine-type n1-standard-2 \     --master-boot-disk-size 50 \     --num-workers 2 \     --worker-machine-type n1-standard-2 \     --worker-boot-disk-size 50 \     --scopes 'https://www.googleapis.com/auth/cloud-platform' \     --project PROJECT_ID ``` |
