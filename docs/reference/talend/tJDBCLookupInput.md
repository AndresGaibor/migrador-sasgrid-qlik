<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tjdbclookupinput · versión 8.0 -->
# tJDBCLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Reads a database and extracts fields based on a query.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

This component also allows you to connect and read data from a RDS MariaDB, a RDS PostgreSQL or a RDS SQLServer database.

## tJDBCLookupInput properties for Apache Spark Streaming

These properties are used to configure tJDBCLookupInput running in the Spark
Streaming Job framework.

The Spark Streaming
tJDBCLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`.  If you are using Spark V1.3, this URL should contain the authentication information, such as:  ``` jdbc:mysql://XX.XX.XX.XX:3306/Talend?user=ychen&password=talend ``` |
| Driver JAR | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Class Name | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| Username and Password | Enter the authentication information to the database you need to connect to.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available only for Spark V1.4. and onwards. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Type in the name of the table from which you need to read data. |
| Query type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Guess schema | Click the Guess schema button to retrieve the table schema. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |
| Trim column | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tJDBCConfiguration component present in the same Job to connect to a database. You need to drop a tJDBCConfiguration component alongside this component and configure the Basic settings of this component to use tJDBCConfiguration.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tjdbclookupinput -->
# tJDBCLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Reads a database and extracts fields based on a query.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

This component also allows you to connect and read data from a RDS MariaDB, a RDS PostgreSQL or a RDS SQLServer database.

## tJDBCLookupInput properties for Apache Spark Streaming

These properties are used to configure tJDBCLookupInput running in the Spark
Streaming Job framework.

The Spark Streaming
tJDBCLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`.  If you are using Spark V1.3, this URL should contain the authentication information, such as:  ``` jdbc:mysql://XX.XX.XX.XX:3306/Talend?user=ychen&password=talend ``` |
| Driver JAR | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Class Name | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| Username and Password | Enter the authentication information to the database you need to connect to.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available only for Spark V1.4. and onwards. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Type in the name of the table from which you need to read data. |
| Query type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Guess schema | Click the Guess schema button to retrieve the table schema. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |
| Trim column | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tJDBCConfiguration component present in the same Job to connect to a database. You need to drop a tJDBCConfiguration component alongside this component and configure the Basic settings of this component to use tJDBCConfiguration.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
