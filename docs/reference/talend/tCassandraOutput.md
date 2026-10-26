<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandraoutput · versión 8.0 -->
# tCassandraOutput

Last updated: 9/30/2026

Writes data into or deletes data from a column family of a Cassandra
keyspace.

tCassandraOutput receives data from
the preceding component, and writes data into Cassandra.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tCassandraOutput Standard properties](/talend/en-US/components/8.0/cassandra/tcassandraoutput-standard-properties)
* [tCassandraOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/cassandra/tcassandraoutput-properties-for-apache-spark-batch)
* [tCassandraOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/cassandra/tcassandraoutput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Handling data with Cassandra](tcassandrainput-tcassandraoutput-tlogrow-handling-data-with-cassandra-standard-component-bigdata-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandraoutput-properties-for-apache-spark-batch -->
# tCassandraOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tCassandraOutput running in the Spark Batch Job framework.

The Spark Batch
tCassandraOutput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Sync columns | Click this button to retrieve schema from the previous component connected in the Job. |
| Keyspace | Type in the name of the keyspace into which you want to write data. |
| Action on keyspace | Select the operation you want to perform on the keyspace to be used:   * None: No operation is carried out. * Drop and create keyspace: The keyspace is removed   and created again. * Create keyspace: The keyspace does not exist and   gets created. * Create keyspace if not exists: A keyspace gets   created if it does not exist. * Drop keyspace if exists and create: The keyspace   is removed if it already exists and created again. |
| Column family | Type in the name of the keyspace into which you want to write data. |
| Action on column family | Select the operation you want to perform on the column family to be used:   * None: no operation is carried out. * Create column family if not exists: a column   family gets created if it does not exist. * Drop column family if exists and create: the   column family is removed if it already exists and created again. * Truncate column family: all data from the column   family is permanently removed.   This list is available only when you have selected Update, Upsert or Insert from the Action on data drop-down list. |
| Action on data | On the data of the table defined, you can perform:   * Upsert: insert the columns if they do not exist   or update the existing columns.  With this action, the columns to be defined in the schema must use lower case in   their names, while the names you put in the DB   column column of the schema must be identical with their equivalents   in the target table, including the letter cases. * Insert: insert the columns if they do not exist.   This action also updates the existing ones. * Update: update the existing columns or add the   columns that do not exist. This action does not support the *Counter* Cassandra data type. * Delete: remove columns corresponding to the input   flow.   For more advanced actions, use the Advanced settings view. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The schema of this component does not support the Object type and the List type. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Configuration | Add the Cassandra properties you need to customize in upserting data into Cassandra.  * For example, if you need to define the Cassandra consistency level for   writing, select the *output\_consistency\_level*   property in the Property name column and enter   the numeric level value in the Value   column.  The following list presents the numerical values you can put and the consistency levels they signify:  * 0: ANY, * 1: ONE, * 2: TWO, * 3: THREE, * 4: QUORUM, * 5: ALL, * 6: LOCAL\_QUORUM, * 7: EACH\_QUORUM, * 8: SERIAL, * 9: LOCAL\_SERIAL, * 10: LOCAL\_ONE  For further details about each of the consistency policies, see Datastax documentation about Cassandra.  When a row is added to the table, you need to click the new row in the Property name column to display the list of the available properties and select the property or properties to be customized. For further information about each of these properties, see the Tuning section in the following link: <https://github.com/datastax/spark-cassandra-connector/blob/master/doc/5_saving.md>. |
| Use unlogged batch | Select this check box to handle data in batch but with Cassandra's UNLOGGED approach. This feature is available to the following three actions: Insert, Update and Delete.  Then you need to configure how the batch mode works:  * Batch size: enter the number of lines in each   batch to be processed. * Group batch method: select how to group rows   into batches:   1. Partition: rows sharing the same      partition keys are grouped.   2. Replica: rows to be written to      the same replica are grouped.   3. None: rows are grouped randomly.      This option is suitable for a single node Cassandra. * Cache batch group: select this check box to   load rows into memory before grouping them. This way, grouping is not impacted   by the order of the rows.  If you leave this check box clear, only successive rows that meet the same   criteria are grouped. * Async execute: select this check box if you   want tCassandraOutput to send batches in parallel.   If you leave it clear, tCassandraOutput waits for   the result of a batch before sending another batch to Cassandra. * Maximum number of batches executed in   parallel: once you have selected Async   execute, enter the number of batches to be sent in parallel to   Cassandra.  This number should not be a negative number or 0 and it is also recommended   not to use too large a value.  The ideal situation to use batches with Cassandra is when a small number of tables must synchronize the data to be inserted or updated.  In this UNLOGGED approach, the Job does not write batches into Cassandra's batchlog system and thus avoids the performance issue incurred by this writing. For further information about Cassandra BATCH statement and UNLOGGED approach, see [Batches](https://docs.datastax.com/en/dse/6.7/cql/cql/cql_reference/cql_commands/cqlBatch.html). |
| Insert if not exists | Select this check box to insert rows. This row insertion takes place only when they do not exist in the target table.  This feature is available to the Insert action only. |
| Delete if exists | Select this check box to remove from the target table only the rows that have the same records in the incoming flow.  This feature is available only to the Delete action. |
| Use TTL | Select this check box to write the TTL data in the target table. In the column list that is displayed, you need to select the column to be used as the TTL column. The DB type of this column must be Int.  This feature is available to the Insert action and the Update action only. |
| Use Timestamp | Select this check box to write the timestamp data in the target table. In the column list that is displayed, you need to select the column to be used to store the timestamp data. The DB type of this column must be BigInt.  This feature is available to the following actions: Insert, Update and Delete. |
| IF condition | Add the condition to be met for the Update or the Delete action to take place. This condition allows you to be more precise about the columns to be updated or deleted. |
| Special assignment operation | Complete this table to construct advanced SET commands of Cassandra to make the Update action more specific. For example, add a record to the beginning or a particular position of a given column.  In the Update column column of this table, you need to select the column to be updated and then select the operations to be used from the Operation column. The following operations are available:  * Append: it adds incoming records to the end   of the column to be updated. The Cassandra data types it can handle are Counter,   List, Set and Map. * Prepend: it adds incoming records to the   beginning of the column to be updated. The only Cassandra data type it can   handle is List. * Remove: it removes records from the target   table when the same records exist in the incoming flow. The Cassandra data types   it can handle are Counter, List, Set and Map. * Assign based on position/key: it adds records   to a particular position of the column to be updated. The Cassandra data types   it can handle are List and Map.  Once you select this operation, the Map key/list   position column becomes editable. From this column, you need to   select the column to be used as reference to locate the position to be   updated.  For more details about these operations, see Datastax's related documentation in <http://docs.datastax.com/en/cql/3.1/cql/cql_reference/update_r.html?scroll=reference_ds_g4h_qzq_xj__description_unique_34>. |
| Row key in the List type | Select the column to be used to construct the WHERE clause of Cassandra to perform the Update or the Delete action on only selected rows. The column(s) to be used in this table should be from the set of the Primary key columns of the Cassandra table. |
| Delete collection column based on postion/key | Select the column to be used as reference to locate the particular row(s) to be removed.  This feature is available only to the Delete action. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use one and only one tCassandraConfiguration component present in the same Job to connect to Cassandra. More than one tCassandraConfiguration components present in the same Job fail the execution of the Job.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandraoutput-standard-properties -->
# tCassandraOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure tCassandraOutput running in the Standard Job framework.

The Standard
tCassandraOutput component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| DB Version | Select the Cassandra version you are using. |
| Host | Enter the hostname or IP address of the Cassandra server. |
| Port | Enter the listening port number of the Cassandra server. |
| Datacenter | Enter the name of the Cassandra datacenter. |
| Required authentication | Select this check box to provide credentials for the Cassandra authentication.  This check box appears only if you do not select the Use existing connection check box. |
| Username | Fill in this field with the username for the Cassandra authentication.  This field is only available when you select the Required authentication check box. |
| Password | Fill in this field with the password for the Cassandra authentication.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This field is only available when you select the Required authentication check box. |
| Use SSL | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| Keyspace | Type in the name of the keyspace into which you want to write data. |
| Action on keyspace | Select the operation you want to perform on the keyspace to be used:   * None: No operation is carried out. * Drop and create keyspace: The keyspace is removed   and created again. * Create keyspace: The keyspace does not exist and   gets created. * Create keyspace if not exists: A keyspace gets   created if it does not exist. * Drop keyspace if exists and create: The keyspace   is removed if it already exists and created again. |
| Column family | Type in the name of the keyspace into which you want to write data. |
| Action on column family | Select the operation you want to perform on the column family to be used:   * None: no operation is carried out. * Drop and create column family: the column family   is removed and created again. * Create column family: the column family does not   exist and gets created. * Create column family if not exists: a column   family gets created if it does not exist. * Drop column family if exists and create: the   column family is removed if it already exists and created again.   This field is only available when you select either Insert or Update from the Action on data drop-down list. |
| Action on data | On the data of the table defined, you can perform:   * Insert: insert the columns if they do not exist.   This action also updates the existing ones. * Update: update the existing columns or add the   columns that do not exist. This action does not support the *Counter* Cassandra data type. * Delete: remove columns corresponding to the input   flow.   For more advanced actions, use the Advanced settings view. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Batch Size | Number of lines in each processed batch.  When you are using the Datastax API, this feature is displayed only when you have selected the Use unlogged batch check box. |
| Use unlogged batch | Select this check box to handle data in batch but with Cassandra's UNLOGGED approach. This feature is available to the following three actions: Insert, Update and Delete.  Then you need to configure how the batch mode works:  * Batch size: enter the number of lines in each   batch to be processed. * Group batch method: select how to group rows   into batches:   1. Partition: rows sharing the same      partition keys are grouped.   2. Replica: rows to be written to      the same replica are grouped.   3. None: rows are grouped randomly.      This option is suitable for a single node Cassandra. * Cache batch group: select this check box to   load rows into memory before grouping them. This way, grouping is not impacted   by the order of the rows.  If you leave this check box clear, only successive rows that meet the same   criteria are grouped. * Async execute: select this check box if you   want tCassandraOutput to send batches in parallel.   If you leave it clear, tCassandraOutput waits for   the result of a batch before sending another batch to Cassandra. * Maximum number of batches executed in   parallel: once you have selected Async   execute, enter the number of batches to be sent in parallel to   Cassandra.  This number should not be a negative number or 0 and it is also recommended   not to use too large a value.  The ideal situation to use batches with Cassandra is when a small number of tables must synchronize the data to be inserted or updated.  In this UNLOGGED approach, the Job does not write batches into Cassandra's batchlog system and thus avoids the performance issue incurred by this writing. For further information about Cassandra BATCH statement and UNLOGGED approach, see [Batches](https://docs.datastax.com/en/dse/6.7/cql/cql/cql_reference/cql_commands/cqlBatch.html). |
| Insert if not exists | Select this check box to insert rows. This row insertion takes place only when they do not exist in the target table.  This feature is available to the Insert action only. |
| Delete if exists | Select this check box to remove from the target table only the rows that have the same records in the incoming flow.  This feature is available only to the Delete action. |
| Use TTL | Select this check box to write the TTL data in the target table. In the column list that is displayed, you need to select the column to be used as the TTL column. The DB type of this column must be Int.  This feature is available to the Insert action and the Update action only. |
| Use Timestamp | Select this check box to write the timestamp data in the target table. In the column list that is displayed, you need to select the column to be used to store the timestamp data. The DB type of this column must be BigInt.  This feature is available to the following actions: Insert, Update and Delete. |
| IF condition | Add the condition to be met for the Update or the Delete action to take place. This condition allows you to be more precise about the columns to be updated or deleted. |
| Special assignment operation | Complete this table to construct advanced SET commands of Cassandra to make the Update action more specific. For example, add a record to the beginning or a particular position of a given column.  In the Update column column of this table, you need to select the column to be updated and then select the operations to be used from the Operation column. The following operations are available:  * Append: it adds incoming records to the end   of the column to be updated. The Cassandra data types it can handle are Counter,   List, Set and Map. * Prepend: it adds incoming records to the   beginning of the column to be updated. The only Cassandra data type it can   handle is List. * Remove: it removes records from the target   table when the same records exist in the incoming flow. The Cassandra data types   it can handle are Counter, List, Set and Map. * Assign based on position/key: it adds records   to a particular position of the column to be updated. The Cassandra data types   it can handle are List and Map.  Once you select this operation, the Map key/list   position column becomes editable. From this column, you need to   select the column to be used as reference to locate the position to be   updated.  For more details about these operations, see Datastax's related documentation in <http://docs.datastax.com/en/cql/3.1/cql/cql_reference/update_r.html?scroll=reference_ds_g4h_qzq_xj__description_unique_34>. |
| Row key in the List type | Select the column to be used to construct the WHERE clause of Cassandra to perform the Update or the Delete action on only selected rows. The column(s) to be used in this table should be from the set of the Primary key columns of the Cassandra table. |
| Delete collection column based on position/key | Select the column to be used as reference to locate the particular row(s) to be removed.  This feature is available only to the Delete action. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an output component and it always needs an incoming link. |
