<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmaprdblookupinput · versión 8.0 -->
# tMapRDBLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Provides lookup data to the main flow of a streaming Job.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

tMapRDBLookupInput
extracts columns corresponding to schema definition. Then it passes the extracted data
to the next component.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tMapRDBLookupInput properties for Apache Spark Streaming

These properties are used to configure tMapRDBLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tMapRDBLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Storage configuration | Select the tMapRDBConfiguration component from which the Spark system to be used reads the configuration information to connect to MapRDB. |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table name | Type in the name of the table from which you need to extract columns. |
| Table Namespace mappings | Enter the string to be used to construct the mapping between an Apache HBase table and a MapR table.  For the valid syntax you can use, see <http://doc.mapr.com/display/MapR40x/Mapping+Table+Namespace+Between+Apache+HBase+Tables+and+MapR+Tables>. |
| Define a row selection | Select this check box and then in the Start row and the End row fields, enter the corresponding row keys to specify the range of the rows you want the current component to extract.  Different from the filters you can set using Is by filter requiring the loading of all records before filtering the ones to be used, this feature allows you to directly select only the rows to be used. |
| Mapping | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed. |
| Is by filter | Select this check box to use filters to perform fine-grained data selection from your database, such as selection of keys, or values, based on regular expressions.  Once selecting it, the Filter table that is used to define filtering conditions becomes available.  This feature leverages filters provided by HBase and subject to constraints explained in Apache HBase documentation. Therefore, advanced knowledge of HBase is required to make full use of these filters. |
| Logical operation | Select the operator you need to use to define the logical relation between filters. This available operators are:  * And: every defined filtering conditions must   be satisfied. It represents the relationship   FilterList.Operator.MUST\_PASS\_ALL * Or: at least one of the defined filtering   conditions must be satisfied. It represents the relationship:   FilterList.Operator.MUST\_PASS\_ONE |
| Filter | Click the button under this table to add as many rows as required, each row representing a filter. The parameters you may need to set for a filter are:  * Filter type: the drop-down list presents   pre-existing filter types that are already defined by HBase. Select the type of   the filter you need to use. * Filter column: enter the column qualifier on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter family: enter the column family on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter operation: select from the drop-down   list the operation to be used for the active filter. * Filter Value: enter the value on which you   want to use the operator selected from the Filter   operation drop-down list. * Filter comparator type: select the type of   the comparator to be combined with the filter you are using.  Depending on the Filter type you are using, some or each of the parameters become mandatory. For further information, see [HBase filters](/talend/en-US/components/8.0/hbase/thbaseinput-thbaseinput-hbase-filters-standard-component-bigdata-this) |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component uses a tMapRDBConfiguration component present in the same Job to connect to MapR-DB.  However, if you need to use tMapRDBLookupInput with Kerberos keytab, configure keytab in the Spark configuration tab instead of in a tMapRDBConfiguration component.  You must drop tMapRDBConfiguration along with the MapRDB-related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmaprdblookupinput -->
# tMapRDBLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Provides lookup data to the main flow of a streaming Job.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

tMapRDBLookupInput
extracts columns corresponding to schema definition. Then it passes the extracted data
to the next component.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tMapRDBLookupInput properties for Apache Spark Streaming

These properties are used to configure tMapRDBLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tMapRDBLookupInput component belongs to the Databases family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Storage configuration | Select the tMapRDBConfiguration component from which the Spark system to be used reads the configuration information to connect to MapRDB. |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table name | Type in the name of the table from which you need to extract columns. |
| Table Namespace mappings | Enter the string to be used to construct the mapping between an Apache HBase table and a MapR table.  For the valid syntax you can use, see <http://doc.mapr.com/display/MapR40x/Mapping+Table+Namespace+Between+Apache+HBase+Tables+and+MapR+Tables>. |
| Define a row selection | Select this check box and then in the Start row and the End row fields, enter the corresponding row keys to specify the range of the rows you want the current component to extract.  Different from the filters you can set using Is by filter requiring the loading of all records before filtering the ones to be used, this feature allows you to directly select only the rows to be used. |
| Mapping | Complete this table to map the columns of the table to be used with the schema columns you have defined for the data flow to be processed. |
| Is by filter | Select this check box to use filters to perform fine-grained data selection from your database, such as selection of keys, or values, based on regular expressions.  Once selecting it, the Filter table that is used to define filtering conditions becomes available.  This feature leverages filters provided by HBase and subject to constraints explained in Apache HBase documentation. Therefore, advanced knowledge of HBase is required to make full use of these filters. |
| Logical operation | Select the operator you need to use to define the logical relation between filters. This available operators are:  * And: every defined filtering conditions must   be satisfied. It represents the relationship   FilterList.Operator.MUST\_PASS\_ALL * Or: at least one of the defined filtering   conditions must be satisfied. It represents the relationship:   FilterList.Operator.MUST\_PASS\_ONE |
| Filter | Click the button under this table to add as many rows as required, each row representing a filter. The parameters you may need to set for a filter are:  * Filter type: the drop-down list presents   pre-existing filter types that are already defined by HBase. Select the type of   the filter you need to use. * Filter column: enter the column qualifier on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter family: enter the column family on   which you need to apply the active filter. This parameter becomes mandatory   depending on the type of the filter and of the comparator you are using. For   example, it is not used by the Row Filter type   but is required by the Single Column Value   Filter type. * Filter operation: select from the drop-down   list the operation to be used for the active filter. * Filter Value: enter the value on which you   want to use the operator selected from the Filter   operation drop-down list. * Filter comparator type: select the type of   the comparator to be combined with the filter you are using.  Depending on the Filter type you are using, some or each of the parameters become mandatory. For further information, see [HBase filters](/talend/en-US/components/8.0/hbase/thbaseinput-thbaseinput-hbase-filters-standard-component-bigdata-this) |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component uses a tMapRDBConfiguration component present in the same Job to connect to MapR-DB.  However, if you need to use tMapRDBLookupInput with Kerberos keytab, configure keytab in the Spark configuration tab instead of in a tMapRDBConfiguration component.  You must drop tMapRDBConfiguration along with the MapRDB-related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
