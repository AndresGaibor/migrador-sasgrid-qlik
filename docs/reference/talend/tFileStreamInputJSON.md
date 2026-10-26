<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfilestreaminputjson · versión 8.0 -->
# tFileStreamInputJSON (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Extracts JSON data from a file, then transfers the data to, for instance, a file or a
database table.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tFileStreamInputJSON properties for Apache Spark Streaming

These properties are used to configure tFileStreamInputJSON running in the Spark Streaming Job framework.

The Spark Streaming
tFileStreamInputJSON component belongs to the File family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The fields that come after are pre-filled in using the fetched   data.  For further information about the File   Json node, see [Centralizing JSON file metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-json-file-metadata). |
| Schema et Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Read by | Select a way of extracting the JSON data in the file.   * Xpath: Extracts the JSON data based on   the XPath query. * JsonPath: Extracts the JSON data based on   the JSONPath query. Note that it is recommended to read the data by JSONPath in   order to gain better performance. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you entered points to a folder, all files stored in that folder will be read.  If the file to be read is a compressed one, enter the file name with its extension; then tFileInputJSON automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |
| Loop Jsonpath query | Enter the JSONPath or XPath of the node on which the loop is based.  Note if you have selected Xpath from the Read by drop-down list, the Loop Xpath query field is displayed instead. |
| Mapping | Complete this table to map the columns defined in the schema to the corresponding JSON nodes.   * Column: The Column cells are automatically filled with the defined schema   column names. * Json query/JSONPath query: Specify the JSONPath node that holds the   desired data. For more information about JSONPath expressions, see <http://goessner.net/articles/JsonPath/>.  This column is available only when JsonPath is selected from the Read   By list. * XPath query: Specify the XPath node that   holds the desired data.  This column is available only when Xpath is selected from the Read   By list. * Get Nodes: Select this check box to   extract the JSON data of all the nodes or select the check box next to a   specific node to extract the data of that node.  This column is available only when Xpath is selected from the Read   By list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tfilestreaminputjson -->
# tFileStreamInputJSON (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Extracts JSON data from a file, then transfers the data to, for instance, a file or a
database table.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tFileStreamInputJSON properties for Apache Spark Streaming

These properties are used to configure tFileStreamInputJSON running in the Spark Streaming Job framework.

The Spark Streaming
tFileStreamInputJSON component belongs to the File family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The fields that come after are pre-filled in using the fetched   data.  For further information about the File   Json node, see [Centralizing JSON file metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-json-file-metadata). |
| Schema et Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Read by | Select a way of extracting the JSON data in the file.   * Xpath: Extracts the JSON data based on   the XPath query. * JsonPath: Extracts the JSON data based on   the JSONPath query. Note that it is recommended to read the data by JSONPath in   order to gain better performance. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you entered points to a folder, all files stored in that folder will be read.  If the file to be read is a compressed one, enter the file name with its extension; then tFileInputJSON automatically decompresses it at runtime. The supported compression formats and their corresponding extensions are:   * DEFLATE: *\*.deflate* * gzip: *\*.gz* * bzip2: *\*.bz2* * LZO: *\*.lzo*   The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |
| Loop Jsonpath query | Enter the JSONPath or XPath of the node on which the loop is based.  Note if you have selected Xpath from the Read by drop-down list, the Loop Xpath query field is displayed instead. |
| Mapping | Complete this table to map the columns defined in the schema to the corresponding JSON nodes.   * Column: The Column cells are automatically filled with the defined schema   column names. * Json query/JSONPath query: Specify the JSONPath node that holds the   desired data. For more information about JSONPath expressions, see <http://goessner.net/articles/JsonPath/>.  This column is available only when JsonPath is selected from the Read   By list. * XPath query: Specify the XPath node that   holds the desired data.  This column is available only when Xpath is selected from the Read   By list. * Get Nodes: Select this check box to   extract the JSON data of all the nodes or select the check box next to a   specific node to extract the data of that node.  This column is available only when Xpath is selected from the Read   By list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for numbers. By default, the thousands separator is a comma (*,*) and the decimal separator is a period (*.*). |
| Encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
