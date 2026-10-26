<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseoutput · versión 8.0 -->
# tHBaseOutput

Last updated: 9/30/2026

Writes columns of data into a given HBase database.

tHBaseOutput receives
data from its preceding component, creates a table in a given HBase database and writes the
received data into this HBase table.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tHBaseOutput Standard properties](/talend/en-US/components/8.0/hbase/thbaseoutput-standard-properties)
* [tHBaseOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/hbase/thbaseoutput-properties-for-apache-spark-batch)
* [tHBaseOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/hbase/thbaseoutput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Exchanging customer data with HBase](thbaseconnection-thbaseinput-tfileinputdelimited-exchanging-customer-data-with-hbase-standard-component-bigdata-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseoutput-properties-for-apache-spark-batch -->
# tHBaseOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tHBaseOutput running in the Spark Batch Job framework.

The Spark Batch
tHBaseOutput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Storage configuration | Select the tHBaseConfiguration component from which the Spark system to be used reads the configuration information to connect to HBase. |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table name | Type in the name of the HBase table in which you need to write data. This table must already exist. |
| Row key column | Select the column used as the row key column of the HBase table.  Then if needs be, select the Store row key column to HBase column check box to make the row key column an HBase column belonging to a specific column family. |
| Custom Row Key | Select this check box to use the customized row keys. Once selected, the corresponding field appears. Then type in the user-defined row key to index the rows of the HBase table being created.  For example, you can type in "France"+Numeric.sequence("s1",1,1) to produce the row key series: `France1`, `France2`, `France3` and so on. |
| Families | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed.  The Column column of this table is automatically filled once you have defined the schema; in the Family name column, enter the column families you want to create or use to group the columns in the Column column. For more information about a column family, see [Column families](http://hbase.apache.org/0.94/book/columnfamily.html) from Apache documentation. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use batch mode | Select this check box to activate the batch mode for data processing. |
| Batch size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Use local timezone for date | Select this check box to use the local date of the machine in which your Job is executed. If leaving this check box clear, UTC is automatically used to format the Date-type data. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component uses a tHBaseConfiguration component present in the same Job to connect to HBase.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseoutput-standard-properties -->
# tHBaseOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure tHBaseOutput running in the Standard Job framework.

The Standard
tHBaseOutput component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| HBase version | Select the HBase version of the distribution you are using. |
| Hadoop version | Select the Hadoop version of the distribution you are using. |
| Zookeeper quorum | Type in the name or the URL of the ZooKeeper service you use to coordinate the transaction between your Talend Studio and your database. Note that when you configure the ZooKeeper, you might need to explicitly set the *zookeeper.znode.parent* property to define the path to the root Znode that contains all the Znodes created and used by your database; then select the Set Zookeeper znode parent check box to define this property. |
| Zookeeper client port | Type in the number of the client listening port of the ZooKeeper service you are using. |
| Use kerberos authentication | If the database to be used is running with Kerberos security, select this checkbox, then, enter the principal names in the HBase Master principal and HBase Region Server principal fields. You should be able to find the information in the *hbase-site.xml* file of the cluster to be used.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Specify namespace | Select this check box if you want to specify a namespace, and enter the name of the namespace you want to create in the Namespace parameter. |
| Table name | Type in the name of the HBase table you need create. |
| Action on table | Select the action you need to take for creating an HBase table. |
| Custom Row Key | Select this check box to use the customized row keys. Once selected, the corresponding field appears. Then type in the user-defined row key to index the rows of the HBase table being created.  For example, you can type in "France"+Numeric.sequence("s1",1,1) to produce the row key series: `France1`, `France2`, `France3` and so on. |
| Families | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed.  The Column column of this table is automatically filled once you have defined the schema; in the Family name column, enter the column families you want to create or use to group the columns in the Column column. For more information about a column family, see [Column families](http://hbase.apache.org/0.94/book/columnfamily.html) from Apache documentation. |
| Custom timestamp column | Select a Long column from your schema to provide timestamps for the HBase columns to be created or updated by tHBaseOutput. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use batch mode | Select this check box to activate the batch mode for data processing. |
| Batch size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Properties | If you need to use custom configuration for your database, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override the corresponding ones used by Talend Studio.  For example, you need to define the value of the *dfs.replication* property as *1* for the database configuration. Then you need to add one row to this table using the plus button and type in the name and the value of this property in this row.  Information noteNote: This table is not available when you are using an existing connection by selecting the Using an existing connection check box in the Basic settings view. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Family parameters | Type in the names and, when needs be, the custom performance options of the column families to be created. These options are all attributes defined by the HBase data model. For more information about a column family, see [Column families](http://hbase.apache.org/0.94/book/columnfamily.html) from Apache documentation. Information noteNote: The parameter Compression type allows you to select the format for output data compression. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is normally an end component of a Job and always needs an input link. |
| Prerequisites | Before starting, ensure that you have met the Loopback IP prerequisites expected by your database.  For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
