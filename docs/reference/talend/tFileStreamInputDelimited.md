<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfilestreaminputdelimited · versión 8.0 -->
# tFileStreamInputDelimited (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Reads data continuously, row by row, to split it into fields, then sends fields
defined in its schema to the next Job component, via a Row >
Main link.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tFileStreamInputDelimited properties for Apache Spark Streaming

These properties are used to configure tFileStreamInputDelimited running in the Spark Streaming Job framework.

The Spark Streaming
tFileStreamInputDelimited component belongs to the File family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit schema to make changes to   the schema. If you make changes, the schema automatically becomes built-in. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will only read the newly created files stored in that folder, for example, /user/talend/in; if sub-folders exist, the sub-folders are automatically ignored unless you define the property spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive to be true in the Advanced properties table in the Spark configuration tab.  * Depending on the filesystem to be used, properly   configure the corresponding configuration component placed in your Job,   for example, a tHDFSConfiguration   component for HDFS, a tS3Configuration   component for S3 and a tAzureFSConfiguration for Azure Storage and Azure Data Lake   Storage.  If you want to specify more than one files or directories in this field, separate each path using a comma (,).  If the file to be read is a compressed one, enter the file name with its extension; then this component automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |
| Row separator | The separator used to identify the end of a row. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Header | Enter the number of rows to be skipped in the beginning of file. |
| CSV options | Select this check box to include CSV specific parameters such as Escape char and Text enclosure. Information noteImportant: With Spark version 2.0 and onward, special characters must be escaped, that is `"\\"` and `"\""` instead of `"\"` and `"""`. |
| Skip empty rows | Select this checkbox to skip the empty rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Custom Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Then select the encoding to be used from the list or select Custom and define it manually. |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Trim all columns | Select this check box to remove the leading and trailing whitespaces from all columns. When this check box is cleared, the Check column to trim table is displayed, which lets you select particular columns to trim. |
| Check column to trim | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |
| Check each row structure against schema | Select this check box to check whether the total number of columns in each row is consistent with the schema. If not consistent, an error message will be displayed on the console. |
| Check date | Select this check box to check the date format strictly against the input schema. |
| Decode String for long, int, short, byte Types | Select this check box if any of your numeric types (long, integer, short, or byte type), will be parsed from a hexadecimal or octal string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfilestreaminputdelimited -->
# tFileStreamInputDelimited (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Reads data continuously, row by row, to split it into fields, then sends fields
defined in its schema to the next Job component, via a Row >
Main link.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tFileStreamInputDelimited properties for Apache Spark Streaming

These properties are used to configure tFileStreamInputDelimited running in the Spark Streaming Job framework.

The Spark Streaming
tFileStreamInputDelimited component belongs to the File family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit schema to make changes to   the schema. If you make changes, the schema automatically becomes built-in. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will only read the newly created files stored in that folder, for example, /user/talend/in; if sub-folders exist, the sub-folders are automatically ignored unless you define the property spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive to be true in the Advanced properties table in the Spark configuration tab.  * Depending on the filesystem to be used, properly   configure the corresponding configuration component placed in your Job,   for example, a tHDFSConfiguration   component for HDFS, a tS3Configuration   component for S3 and a tAzureFSConfiguration for Azure Storage and Azure Data Lake   Storage.  If you want to specify more than one files or directories in this field, separate each path using a comma (,).  If the file to be read is a compressed one, enter the file name with its extension; then this component automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |
| Row separator | The separator used to identify the end of a row. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Header | Enter the number of rows to be skipped in the beginning of file. |
| CSV options | Select this check box to include CSV specific parameters such as Escape char and Text enclosure. Information noteImportant: With Spark version 2.0 and onward, special characters must be escaped, that is `"\\"` and `"\""` instead of `"\"` and `"""`. |
| Skip empty rows | Select this checkbox to skip the empty rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Custom Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Then select the encoding to be used from the list or select Custom and define it manually. |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Trim all columns | Select this check box to remove the leading and trailing whitespaces from all columns. When this check box is cleared, the Check column to trim table is displayed, which lets you select particular columns to trim. |
| Check column to trim | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |
| Check each row structure against schema | Select this check box to check whether the total number of columns in each row is consistent with the schema. If not consistent, an error message will be displayed on the console. |
| Check date | Select this check box to check the date format strictly against the input schema. |
| Decode String for long, int, short, byte Types | Select this check box if any of your numeric types (long, integer, short, or byte type), will be parsed from a hexadecimal or octal string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
