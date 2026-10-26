<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseinput · versión 8.0 -->
# tHBaseInput

Last updated: 9/30/2026

Reads data from a given HBase database and extracts columns of
selection.

HBase is a distributed, column-oriented database that hosts very large,
sparsely populated tables on clusters.

tHBaseInput extracts columns corresponding to schema
definition. Then it passes these columns to the next component via a Main row link.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tHBaseInput Standard properties](/talend/en-US/components/8.0/hbase/thbaseinput-standard-properties)
* [tHBaseInput properties for Apache Spark Batch](/talend/en-US/components/8.0/hbase/thbaseinput-properties-for-apache-spark-batch)

**Related concepts**  

* [Exchanging customer data with HBase](thbaseconnection-thbaseinput-tfileinputdelimited-exchanging-customer-data-with-hbase-standard-component-bigdata-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseinput-properties-for-apache-spark-batch -->
# tHBaseInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tHBaseInput running in the Spark Batch Job framework.

The Spark Batch
tHBaseInput component belongs to the Databases family.

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
| Table name | Type in the name of the table from which you need to extract columns. |
| Mapping | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed. |
| Is by filter | Select this check box to use filters to perform fine-grained data selection from your database, such as selection of keys, or values, based on regular expressions.  Once selecting it, the Filter table that is used to define filtering conditions becomes available.  This feature leverages filters provided by HBase and subject to constraints explained in Apache HBase documentation. Therefore, advanced knowledge of HBase is required to make full use of these filters. |
| Logical operation | Select the operator you need to use to define the logical relation between filters. This available operators are:  * And: every defined filtering conditions must   be satisfied. It represents the relationship   FilterList.Operator.MUST\_PASS\_ALL * Or: at least one of the defined filtering   conditions must be satisfied. It represents the relationship:   FilterList.Operator.MUST\_PASS\_ONE |
| Filter | Click the button under this table to add as many rows as required, each row representing a filter. The parameters you may need to set for a filter are:  * Filter type: the drop-down list presents   pre-existing filter types that are already defined by HBase. Select the type of   the filter you need to use. * Filter column: enter the column qualifier on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter family: enter the column family on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter operation: select from the drop-down   list the operation to be used for the active filter. * Filter Value: enter the value on which you   want to use the operator selected from the Filter   operation drop-down list. * Filter comparator type: select the type of   the comparator to be combined with the filter you are using.  Depending on the Filter type you are using, some or each of the parameters become mandatory. For further information, see [HBase filters](/talend/en-US/components/8.0/hbase/thbaseinput-thbaseinput-hbase-filters-standard-component-bigdata-this) |
| Partition by table regions | Select this check box to read in parallel the data from an HBase table using its number of regions. |
| Die on HBase error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component uses a tHBaseConfiguration component present in the same Job to connect to HBase.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseinput-standard-properties -->
# tHBaseInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tHBaseInput running in the Standard Job framework.

The Standard
tHBaseInput component belongs to the Big Data and the Databases NoSQL families.

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
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Specify namespace | Select this check box if you want to specify a namespace, and enter the name of the namespace you want to create in the Namespace parameter. |
| Table name | Type in the name of the table from which you need to extract columns. |
| Define a row selection | Select this check box and then in the Start row and the End row fields, enter the corresponding row keys to specify the range of the rows you want the current component to extract.  Different from the filters you can set using Is by filter requiring the loading of all records before filtering the ones to be used, this feature allows you to directly select only the rows to be used. |
| Mapping | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Properties | If you need to use custom configuration for your database, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override the corresponding ones used by Talend Studio.  For example, you need to define the value of the *dfs.replication* property as *1* for the database configuration. Then you need to add one row to this table using the plus button and type in the name and the value of this property in this row.  Information noteNote: This table is not available when you are using an existing connection by selecting the Using an existing connection check box in the Basic settings view. |
| Is by filter | Select this check box to use filters to perform fine-grained data selection from your database, such as selection of keys, or values, based on regular expressions.  Once selecting it, the Filter table that is used to define filtering conditions becomes available.  This feature leverages filters provided by HBase and subject to constraints explained in Apache HBase documentation. Therefore, advanced knowledge of HBase is required to make full use of these filters. |
| Logical operation | Select the operator you need to use to define the logical relation between filters. This available operators are:  * And: every defined filtering conditions must   be satisfied. It represents the relationship   FilterList.Operator.MUST\_PASS\_ALL * Or: at least one of the defined filtering   conditions must be satisfied. It represents the relationship:   FilterList.Operator.MUST\_PASS\_ONE |
| Filter | Click the button under this table to add as many rows as required, each row representing a filter. The parameters you may need to set for a filter are:  * Filter type: the drop-down list presents   pre-existing filter types that are already defined by HBase. Select the type of   the filter you need to use. * Filter column: enter the column qualifier on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter family: enter the column family on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter operation: select from the drop-down   list the operation to be used for the active filter. * Filter Value: enter the value on which you   want to use the operator selected from the Filter   operation drop-down list. * Filter comparator type: select the type of   the comparator to be combined with the filter you are using.  Depending on the Filter type you are using, some or each of the parameters become mandatory. For further information, see [HBase filters](/talend/en-US/components/8.0/hbase/thbaseinput-thbaseinput-hbase-filters-standard-component-bigdata-this) |
| Retrieve timestamps | Select this check box to load the timestamps of an HBase column into the data flow.  * Retrieve from an HBase column: select   the HBase column which is tracked for changes in order to   retrieve its corresponding timestamps. * Write to a schema column: select the column you have defined   in the schema to store the retrieved timestamps.  The type of this column must be   Long. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is a start component of a Job and always needs an output link. |
| Prerequisites | Before starting, ensure that you have met the Loopback IP prerequisites expected by your database.  For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseinput-thbaseinput-hbase-filters-standard-component-bigdata-this -->
# HBase filters

Last updated: 9/30/2026

This table presents the HBase filters available in *Talend Studio* and the
parameters required by those filters.

| Filter type | Filter column | Filter family | Filter operation | Filter value | Filter comparator type | Objective |
| --- | --- | --- | --- | --- | --- | --- |
| Single Column Value Filter | Yes | Yes | Yes | Yes | Yes | It compares the values of a given column against the value defined for the Filter value parameter. If the filtering condition is met, all columns of the row will be returned. |
| Family filter |  | Yes | Yes |  | Yes | It returns the columns of the family that meets the filtering condition. |
| Qualifier filter | Yes |  | Yes |  | Yes | It returns the columns whose column qualifiers match the filtering condition. |
| Column prefix filter | Yes | Yes |  |  |  | It returns all columns of which the qualifiers have the prefix defined for the Filter column parameter. |
| Multiple column prefix filter | Yes (Multiple prefixes are separated by comma, for example, *id,id\_1,id\_2*) | Yes |  |  |  | It works the same way as a Column prefix filter does but allows specifying multiple prefixes. |
| Column range filter | Yes (The ends of a range are separated by comma. ) | Yes |  |  |  | It allows intra row scanning and returns all matching columns of a scanned row. |
| Row filter |  |  | Yes | Yes | Yes | It filters on row keys and returns all rows that matches the filtering condition. |
| Value filter |  |  | Yes | Yes | Yes | It returns only columns that have a specific value. |

The use explained above of the listed HBase filters is subject to revisions made by
Apache in its Apache HBase project; therefore, in order to fully understand how to use
these HBase filters, we recommend reading Apache's HBase documentation.
