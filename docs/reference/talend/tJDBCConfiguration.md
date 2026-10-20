<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcconfiguration · versión 8.0 -->
# tJDBCConfiguration

Last updated: 9/30/2026

Stores connection information and credentials to be reused by other JDBC
components.

You configure the connection to a given database in
tJDBCConfiguration and configure the other JDBC related components to
reuse this configuration. At runtime, the Spark executors read this configuration in order
to connect to this database.

If you use JDBC with Databricks on Azure, you must have a
Premium pricing workspace for your Databricks cluster. For further information about Azure
Databricks pricing, see [Azure Databricks pricing](https://azure.microsoft.com/en-us/pricing/details/databricks/).

### In this section

* [tJDBCConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/jdbc/tjdbcconfiguration-properties-for-apache-spark-batch)
* [tJDBCConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/jdbc/tjdbcconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcconfiguration-properties-for-apache-spark-batch -->
# tJDBCConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJDBCConfiguration running in the Spark
Batch Job framework.

The Spark Batch
tJDBCConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`.   * If you are using Spark V1.3, this URL should contain the authentication information, such as:    ```   jdbc:mysql://XX.XX.XX.XX:3306/Talend?user=ychen&password=talend   ``` * If you are using Databricks, this JDBC URL value can be found on the JDBC/ODBC tab of the Web UI of your Databricks cluster. To access this tab, on the Configuration tab of your Databricks cluster page, scroll down to the bottom of the page and click the JDBC/ODBC tab. |
| Driver JAR | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Driver Class | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| Username and Password | Enter the authentication information to the database you need to connect to.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  If you are using Databricks, enter `token` in the Username field and your Databricks token in the Password field. This token is the authentication token generated for your Databricks user account. You can generate or find this token on the User settings page of your Databricks workspace. For more information, see [Manage personal access tokens](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/access-control/tokens) from the Azure documentation.  Available only for Spark V1.4. and onwards. |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  The configuration in a tJDBCConfiguration component applies only on the JDBC related components in the same Job. In other words, the JDBC components used in a child or a parent Job that is called via tRunJob cannot reuse this configuration. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
