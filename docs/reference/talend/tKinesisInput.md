<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkinesisinput · versión 8.0 -->
# tKinesisInput

Last updated: 9/30/2026

Acts as consumer of an Amazon Kinesis stream to pull messages from this Kinesis
stream.

Using the Kinesis Client Library (KCL) provided by Amazon, tKinesisInput consumes data from a given
Amazon Kinesis stream (an ordered sequence of data records), constructs
an RDD out of this data and sends the RDD to its following
components.

### In this section

* [tKinesisInput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/kinesis/tkinesisinput-properties-for-apache-spark-streaming)
* [tKinesisInput properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/kinesis/tkinesisinput-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Working with Amazon Kinesis and Big Data Streaming Jobs](tkinesisinput-tkinesisoutput-treplicate-thdfsconfiguration-working-with-amazon-kinesis-and-big-data-streaming-jobs-this "This scenario shows how to work with Amazon Kinesis and Big Data Streaming Jobs using the Spark Streaming framework.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkinesisinput-tkinesisoutput-treplicate-thdfsconfiguration-working-with-amazon-kinesis-and-big-data-streaming-jobs-this -->
# Working with Amazon Kinesis and Big Data Streaming Jobs

Last updated: 9/30/2026

This scenario shows how to work with Amazon Kinesis and Big Data Streaming Jobs using
the Spark Streaming framework.

This scenario applies only to Talend Real-Time Big Data Platform and
Talend Data Fabric.

This example uses Talend Real-Time Big Data Platform v6.1. In
addition, it uses these licensed products provided by Amazon: Amazon EC2, Amazon
Kinesis, and Amazon EMR.

In this example, you will build the following Job, to read and and write data to an
Amazon Kinesis stream and display results in the Console.

tHDFSConfiguration is used in this scenario by Spark to connect
to the HDFS system where the jar files dependent on the Job are transferred.

In the Spark
Configuration tab in the Run
view, define the connection to a given Spark cluster for the whole Job. In
addition, since the Job expects its dependent jar files for execution, you must
specify the directory in the file system to which these jar files are
transferred so that Spark can access these files:

* Yarn mode (Yarn client or Yarn cluster):
  + When using Google Dataproc, specify a bucket in the
    Google Storage staging bucket
    field in the Spark configuration
    tab.
  + When using HDInsight, specify the blob to be used for Job
    deployment in the Windows Azure Storage
    configuration area in the Spark
    configuration tab.
  + When using Altus, specify the S3 bucket or the Azure
    Data Lake Storage for Job deployment in the Spark
    configuration tab.
  + When using on-premises distributions, use
    the configuration component corresponding to the file system
    your cluster is using. Typically, this system is HDFS and so
    use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
* Standalone mode: use the
  configuration component corresponding to the file system your cluster is
  using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

  If you are using Databricks without any configuration component present
  in your Job, your business data is written directly in DBFS (Databricks
  Filesystem).

### In this section

* [Launching an Amazon Kinesis Stream](/talend/en-US/components/8.0/kinesis/tkinesisinput-tkinesisoutput-treplicate-thdfsconfiguration-launching-amazon-kinesis-stream-from)
* [Writing data to an Amazon Kinesis Stream](/talend/en-US/components/8.0/kinesis/tkinesisinput-tkinesisoutput-treplicate-thdfsconfiguration-writing-data-to-amazon-kinesis-stream-in-this)
* [Reading Data from an Amazon Kinesis Stream](/talend/en-US/components/8.0/kinesis/tkinesisinput-tkinesisoutput-treplicate-thdfsconfiguration-reading-data-from-amazon-kinesis-stream-to-read)
* [Configuring a Big Data Streaming Job using the Spark Streaming Framework](/talend/en-US/components/8.0/kinesis/tkinesisinput-tkinesisoutput-treplicate-thdfsconfiguration-configuring-big-data-streaming-job-using-spark-streaming-framework-because)

**Related concepts**  

* [tKinesisInput](tkinesisinput "Acts as consumer of an Amazon Kinesis stream to pull messages from this Kinesis stream.")
* [tKinesisOutput](tkinesisoutput "Acts as data producer to put data to an Amazon Kinesis stream for real-time ingestion.")

**Related information**  

* [tReplicate](/talend/en-US/components/8.0/orchestration/treplicate)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tWriteDelimitedFields](/talend/en-US/components/8.0/processing/twritedelimitedfields)
* [tExtractDelimitedFields](/talend/en-US/components/8.0/processing/textractdelimitedfields)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
