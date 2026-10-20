<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprdbinput · versión 8.0 -->
# tMapRDBInput

Last updated: 9/30/2026

Reads data from a given MapRDB database and extracts columns of
selection.

tMapRDBInput extracts columns
corresponding to schema definition. Then it passes these columns to the
next component via a Main row link.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tMapRDBInput Standard properties](/talend/en-US/components/8.0/maprdb/tmaprdbinput-standard-properties)
* [tMapRDBInput properties for Apache Spark Batch](/talend/en-US/components/8.0/maprdb/tmaprdbinput-properties-for-apache-spark-batch)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprdbinput-properties-for-apache-spark-batch -->
# tMapRDBInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMapRDBInput running in the Spark Batch Job framework.

The Spark Batch
tMapRDBInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Storage configuration | Select the tMapRDBConfiguration component from which the Spark system to be used reads the configuration information to connect to MapRDB. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table name | Type in the name of the table from which you need to extract columns. |
| Table Namespace mappings | Enter the string to be used to construct the mapping between an Apache HBase table and a MapR table.  For the valid syntax you can use, see <http://doc.mapr.com/display/MapR40x/Mapping+Table+Namespace+Between+Apache+HBase+Tables+and+MapR+Tables>. |
| Mapping | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed. |
| Is by filter | Select this check box to use filters to perform fine-grained data selection from your database, such as selection of keys, or values, based on regular expressions.  Once selecting it, the Filter table that is used to define filtering conditions becomes available.  This feature leverages filters provided by HBase and subject to constraints explained in Apache HBase documentation. Therefore, advanced knowledge of HBase is required to make full use of these filters. |
| Logical operation | Select the operator you need to use to define the logical relation between filters. This available operators are:  * And: every defined filtering conditions must   be satisfied. It represents the relationship   FilterList.Operator.MUST\_PASS\_ALL * Or: at least one of the defined filtering   conditions must be satisfied. It represents the relationship:   FilterList.Operator.MUST\_PASS\_ONE |
| Filter | Click the button under this table to add as many rows as required, each row representing a filter. The parameters you may need to set for a filter are:  * Filter type: the drop-down list presents   pre-existing filter types that are already defined by HBase. Select the type of   the filter you need to use. * Filter column: enter the column qualifier on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter family: enter the column family on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter operation: select from the drop-down   list the operation to be used for the active filter. * Filter Value: enter the value on which you   want to use the operator selected from the Filter   operation drop-down list. * Filter comparator type: select the type of   the comparator to be combined with the filter you are using.  Depending on the Filter type you are using, some or each of the parameters become mandatory. For further information, see [HBase filters](/talend/en-US/components/8.0/hbase/thbaseinput-thbaseinput-hbase-filters-standard-component-bigdata-this) |
| Die on HBase error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component uses a tMapRDBConfiguration component present in the same Job to connect to MapR-DB. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprdbinput-standard-properties -->
# tMapRDBInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tMapRDBInput running in the Standard Job framework.

The Standard
tMapRDBInput component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored.  The properties are stored centrally under the Hadoop Cluster node of the Repository tree. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Hadoop version of the distribution | This list is displayed only when you have selected Custom from the distribution list to connect to a cluster not yet officially supported by Talend Studio. In this situation, you need to select the Hadoop version of this custom cluster, that is to say, Hadoop 1 or Hadoop 2. |
| Zookeeper quorum | Type in the name or the URL of the ZooKeeper service you use to coordinate the transaction between your Talend Studio and your database. Note that when you configure the ZooKeeper, you might need to explicitly set the *zookeeper.znode.parent* property to define the path to the root Znode that contains all the Znodes created and used by your database; then select the Set Zookeeper znode parent check box to define this property. |
| Zookeeper client port | Type in the number of the client listening port of the ZooKeeper service you are using. |
| Use kerberos authentication | If the database to be used is running with Kerberos security, select this checkbox, then, enter the principal names in the HBase Master principal and HBase Region Server principal fields. You should be able to find the information in the *hbase-site.xml* file of the cluster to be used.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Set table Namespace mappings | Enter the string to be used to construct the mapping between an Apache HBase table and a MapR table.  For the valid syntax you can use, see <http://doc.mapr.com/display/MapR40x/Mapping+Table+Namespace+Between+Apache+HBase+Tables+and+MapR+Tables>. |
| Table name | Type in the name of the table from which you need to extract columns. |
| Define a row selection | Select this check box and then in the Start row and the End row fields, enter the corresponding row keys to specify the range of the rows you want the current component to extract.  Different from the filters you can set using Is by filter requiring the loading of all records before filtering the ones to be used, this feature allows you to directly select only the rows to be used. |
| Mapping | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Properties | If you need to use custom configuration for your database, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override the corresponding ones used by Talend Studio.  For example, you need to define the value of the *dfs.replication* property as *1* for the database configuration. Then you need to add one row to this table using the plus button and type in the name and the value of this property in this row.  Information noteNote: This table is not available when you are using an existing connection by selecting the Using an existing connection check box in the Basic settings view. |
| Is by filter | Select this check box to use filters to perform fine-grained data selection from your database, such as selection of keys, or values, based on regular expressions.  Once selecting it, the Filter table that is used to define filtering conditions becomes available.  This feature leverages filters provided by HBase and subject to constraints explained in Apache HBase documentation. Therefore, advanced knowledge of HBase is required to make full use of these filters. |
| Logical operation | Select the operator you need to use to define the logical relation between filters. This available operators are:  * And: every defined filtering conditions must   be satisfied. It represents the relationship   FilterList.Operator.MUST\_PASS\_ALL * Or: at least one of the defined filtering   conditions must be satisfied. It represents the relationship:   FilterList.Operator.MUST\_PASS\_ONE |
| Filter | Click the button under this table to add as many rows as required, each row representing a filter. The parameters you may need to set for a filter are:  * Filter type: the drop-down list presents   pre-existing filter types that are already defined by HBase. Select the type of   the filter you need to use. * Filter column: enter the column qualifier on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter family: enter the column family on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter operation: select from the drop-down   list the operation to be used for the active filter. * Filter Value: enter the value on which you   want to use the operator selected from the Filter   operation drop-down list. * Filter comparator type: select the type of   the comparator to be combined with the filter you are using.  Depending on the Filter type you are using, some or each of the parameters become mandatory. For further information, see [HBase filters](/talend/en-US/components/8.0/hbase/thbaseinput-thbaseinput-hbase-filters-standard-component-bigdata-this) |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is a start component of a Job and always needs an output link. |
| Prerequisites | Before starting, ensure that you have met the Loopback IP prerequisites expected by your database.  The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
