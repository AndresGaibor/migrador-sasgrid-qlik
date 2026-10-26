<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/thivein · versión 8.0 -->
# tHiveInput

Last updated: 9/30/2026

Extracts data from Hive and sends the data to the component that
follows.

Hive allows you to access external tables from Spark but does not support ACID
transactions.

tHiveInput is the
dedicated component to the Hive database (the Hive data warehouse system). It can execute a
given HiveQL query in order to extract the data from Hive.

When ACID is enabled on the Hive side, a Spark Job cannot delete
or update a table and unless data is compacted, this Job cannot correctly read
aggregated data from a Hive table, either. This is a known limitation described in
the [Spark bug tracking system](https://issues.apache.org/jira/browse/SPARK-15348).

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tHiveInput Standard properties](/talend/en-US/components/8.0/hive/thiveinput-standard-properties)
* [tHiveInput properties for Apache Spark Batch](/talend/en-US/components/8.0/hive/thiveinput-properties-for-apache-spark-batch)
* [tHiveInput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/hive/thiveinput-properties-for-apache-spark-streaming)
