<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tteradatalookupinput · versión 8.0 -->
# tTeradataLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a database query with a strictly defined order which must correspond to
the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tTeradataLookupInput properties for Apache Spark Streaming

These properties are used to configure tTeradataLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tTeradataLookupInput component belongs to the Databases family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be used. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tTeradataConfiguration component present in the same Job to connect to Oracle. You need to select the Use an existing configuration check box and then select the tTeradataConfiguration component to be used.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tteradatalookupinput -->
# tTeradataLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a database query with a strictly defined order which must correspond to
the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tTeradataLookupInput properties for Apache Spark Streaming

These properties are used to configure tTeradataLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tTeradataLookupInput component belongs to the Databases family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be used. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tTeradataConfiguration component present in the same Job to connect to Oracle. You need to select the Use an existing configuration check box and then select the tTeradataConfiguration component to be used.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
