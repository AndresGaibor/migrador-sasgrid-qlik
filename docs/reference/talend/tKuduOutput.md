<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduoutput · versión 8.0 -->
# tKuduOutput

Last updated: 9/30/2026

Creates, updates or deletes data in a Cloudera Kudu table.

## tKuduOutput properties for Apache Spark Batch

These properties are used to configure tKuduOutput running in the Spark Batch Job framework.

The Spark Batch
tKuduOutput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Server connection | Click the [+] button to add as many rows as the Kudu masters you need to use, each row for a master. Then enter the locations and the listening ports of the master nodes of the Kudu service to be used.  This component supports only the Apache Kudu service installed on Cloudera.  For compatibility information between Apache Kudu and Cloudera, see the related Cloudera documentation: [Compatibility Matrix for Apache Kudu](https://www.cloudera.com/documentation/enterprise/release-notes/topics/rn_consolidated_pcm.html#pcm_kudu). |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. * Information noteNote: The schema of a Kudu table must declare a   primary key comprised of one or more columns. These columns must be   non-nullable, and may not be of type boolean, float or double.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Kudu version | Select the version of Kudu used by your cluster from the drop-down list. |
| Kudu table | Enter the name of the table to be created, changed, or removed. |
| Action on table | Select an operation to be performed on the table defined.   * None: No operation is carried out. * Drop and create table: The table is removed   and created again. * Create table: The table does not exist and   gets created. * Create table if does not exist: The table is   created if it does not exist. * Drop table if exist and create: The table is   removed if it already exists and created again. |
| Action on data | Select an action to be performed on data of the table defined.   * Insert: Add   new entries to the table. If duplicates are found, the Job stops. * Update:   Make changes to existing entries. * Upsert: Update the   record with the given reference. If the record does not exist, a new record would be   inserted. * Delete:   Remove entries corresponding to the input flow. |
| Replicas | Enter, without double quotation marks, the replication factor of this table to create copies of your table and its tablets. For more information about Kudu tablets and Kudu replication policies, see [Distribution and Fault Tolerance](https://kudu.apache.org/overview.html#distribution-and-fault-tolerance). |
| Hash partitions | When you are creating a Kudu table, it is recommended to define how this table is partitioned. By default, your table is not partitioned.  1. Click the [+] button to add the columns based on    which rows are hash-partitioned, for example, add a    `host` column and a `metric`    column. These columns must exist in your data and in the schema you    have defined in tKuduOutput. 2. In Number of buckets, enter, without double    quotation marks, the number of the buckets to be used to store the    partitions. These buckets are created on the fly.   At runtime, rows are distributed by hash value in one of those buckets. If you leave this Hash partitions table empty, hash partitioning is not applied during the creation of the table.  For more information about hash partitioning in Kudu, see [Hash partitioning](https://kudu.apache.org/docs/schema_design.html#hash-partitioning). |
| Range partitions | When you are creating a Kudu table, it is recommended to define how this table is partitioned. By default, your table is not partitioned.  1. Click the [+] button to add the primary key columns    based on which rows are partitioned to contiguous segments, for example, add    a `time` column. These columns must exist in your    data and in the schema you have defined in    tKuduOutput. 2. In N. Partition, enter, without double quotation    marks, a number to be used as the ID number of the partition to be created.    For example, enter `1` to create Partition 1. 3. In Lower boundary and Upper    boundary, enter the boundaries between which rows are    partitioned. The upper boundary is excluded and only the data between the    boundaries (including the lower boundary) is written to the Kudu    table. For example, if you are partitioning your data based on a    `time` column of Date type    and the format of your time data is yyyy-mm-dd, you can set the lower    boundary to be `2016-01-01` by entering, without    double quotation marks, `TalendDate.parseDate("yyyy-MM-dd",    "2016-01-01")` and do the same to set the upper boundary to    be `2018-01-01`, then only rows with dates between    the two boundaries enter this partition.   At runtime, rows of these columns are distributed using the values of the columns you have added to this Range partitions table. If you leave this table empty, range partitioning is not applied during the creation of the table.  For more information about range partitioning in Kudu, see [Range partitioning](https://kudu.apache.org/docs/schema_design.html#range-partitioning). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |

**Related concepts**  

* [Writing and reading data from Cloudera Kudu using a Spark Batch Job](tkuduoutput-tkuduconfiguration-tmap-writing-and-reading-data-from-cloudera-kudu-using-spark-batch-job-the "In this scenario, you create a Spark Batch Job using the Kudu components to partition and write data in a Kudu table and then read some of the data from Kudu.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-writing-and-reading-data-from-cloudera-kudu-using-spark-batch-job-the -->
# Writing and reading data from Cloudera Kudu using a Spark Batch Job

Last updated: 9/30/2026

In this scenario, you create a Spark Batch Job using the Kudu components to partition and write data in a Kudu table and then read some of the data from Kudu.

This scenario applies only to subscription-based Talend products
with Big Data.

The sample data reads as
follows:

```
01;ychen;30
02;john;40
03;yoko;20
04;tom;60
05;martin;50
```

This data contains the names of some persons, the ID numbers distributed to
these persons and their ages.

The ages are made distinct one from another on purpose because this column is the primary key column and is used for range partitioning in this scenario.

Note that the sample data is created for demonstration purposes only.

Prerequisites:

* Ensure that the Spark cluster and the
  Cloudera Kudu database to be used have been properly installed and are running.

* Ensure that the client machine on which the Talend Jobs are
  executed can recognize the host names of the nodes of the Hadoop cluster to be
  used. For this purpose, add the IP address/hostname mapping entries for the
  services of that Hadoop cluster in the `hosts`
  file of the client machine.

  For example, if the host name of the Hadoop Namenode server is `talend-cdh550.weave.local` and its IP address is `192.168.x.x`, the mapping entry reads `192.168.x.x
  talend-cdh550.weave.local`.
* If the cluster to be used is secured with Kerberos, ensure
  that you have properly installed and configured Kerberos on the machine on
  which your Talend Job is
  executed. Depending on the Kerberos mode being used, the Kerberos kinit
  ticket or keytab must be available on that machine.

  For further information, search for how to use Kerberos in Talend Studio with Big Data on Talend Help Center.

Recommendation:

* Define the Hadoop connection metadata from the Hadoop cluster node in Repository. This way, you can not only reuse
  this connection in different Jobs but also ensure that the connection to
  your Hadoop cluster has been properly set up and is working well when you
  use this connection in your Jobs.

  For further information about setting up a reusable Hadoop connection, see
  [Centralizing Hadoop connection
  metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-hadoop-connection)

### In this section

* [Design the data flow of the Kudu Job](/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-design-data-flow-of-kudu-job-in)
* [Defining the Cloudera connection parameters](/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-defining-cloudera-connection-parameters-spark-batch-component-enter?id=3003)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/kudu/configuring-connection-to-file-system-to-be-used-by-spark?id=3004)
* [Configuring the connection to the Kudu database to be used by Spark](/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-configuring-connection-to-kudu-database-to-be-used-by-spark)
* [Partition the sample data and writing it to Kudu](/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-partition-sample-data-and-writing-it-to-kudu)
* [Scanning data from Kudu](/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-scanning-data-from-kudu)

**Related reference**  

* [tKuduOutput](tkuduoutput "Creates, updates or deletes data in a Cloudera Kudu table.")
* [tKuduConfiguration](tkuduconfiguration "Enables the reuse of the connection configuration to Cloudera Kudu in the same Job.")
* [tKuduInput](tkuduinput "Retrieves data from a Cloudera Kudu table and sends them to the component that follows for transformation.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMongoDBInput](/talend/en-US/components/8.0/mongodb/tmongodbinput)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-configuring-connection-to-kudu-database-to-be-used-by-spark -->
# Configuring the connection to the Kudu database to be used by Spark

Last updated: 9/30/2026

## Procedure

1. Double-click tKuduConfiguration to open its
   Component view.

   ### Example
2. Click the [+] button to add one row to the Server connection table.
3. Enter the node name of your Kudu master within double quotation marks and its
   listening port.

   If your Kudu cluster has multiple masters, add them all to this table, each in
   one row.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-defining-cloudera-connection-parameters-spark-batch-component-enter -->
# Defining the Cloudera connection parameters

Last updated: 9/30/2026

Complete the Cloudera connection configuration in the Spark
configuration tab of the Run view of your Job.
This configuration is effective on a per-Job basis.

If you cannot find the Cloudera or
Hortonworks version to be used from the Version drop-down list, you
can add your distribution via some dynamic distribution settings in Talend Studio.

* On the version list of the distributions, some versions are labeled
  Builtin. These versions were added by Talend
  via the Dynamic distribution mechanism and delivered with Talend Studio
  when Talend Studio was
  released. They are certified by Talend,
  thus officially supported and ready to use.

The information in this section is only for users who have subscribed to
Talend Data Fabric
or to any Talend product
with Big Data.

## Procedure

1. Enter the Knox configuration information:

   | Use Knox | If you are using Knox, you need to set the following parameters in their corresponding fields: * Knox URL: enter the Knox URL respecting the   following format   https://<host>/<datahub>/cdp-proxy-api. You   can find the Knox URL on the Cloudera Management Console in the   Endpoints section of your Data Hub under   Livy Server. Information noteImportant: The URL should not include /livy   or any other suffix after cdp-proxy-api. * Knox user: enter your Workload User Name from   Cloudera Management Console. * Knox password: enter your Workload Password   from Cloudera Management Console. * Knox directory: type in the location storing   the loaded file in HDFS. * Knox session timeout: specify the amount of   time to wait for the Job to reconnect to the cluster via Knox. * Webhdfs directory: type in the location storing   the loaded file in HDFS. * Poll interval when retrieving Job status (in   ms): enter, without the quotation marks, the time   interval (in milliseconds) at the end of which you want Talend Studio to ask Spark for the status of your Job. For example, this status   can be Pending or Running. The default value is   30000, meaning 30 seconds * Maximum number of consecutive statuses missing:   enter the maximum number of times Talend Studio should retry to get a status when there is no status   response. The default value is 10. These options are available for CDP 7.1 and onwards in YARN cluster mode for Spark Batch and Spark Streaming Jobs. |
2. Enter the basic configuration information:

   | Use local timezone | Select this check box to let Spark use the local time zone provided by the system. Information noteNote: * If you clear this check box, Spark use UTC time zone. * Some components also have the Use local timezone for   date check box. If you clear the check box from the   component, it inherits time zone from the Spark configuration. |
   | Use dataset API in migrated components | Select this check box to let the components use Dataset (DS) API instead of Resilient Distributed Dataset (RDD) API: * If you select the check box, the components inside the Job run with   DS which improves performance. * If you clear the check box, the components inside the Job run with   RDD which means the Job remains unchanged. This ensures the backwards   compatibility. This check box is selected by default, but if you import a Job from 7.3 backwards, the check box will be cleared as those Jobs run with RDD.  Information noteImportant: If your Job contains tDeltaLakeInput and tDeltaLakeOutput components, you must select this check box. |
   | Use timestamp for dataset components | Select this check box to use java.sql.Timestamp for dates. Information noteNote: If you leave this check box clear, java.sql.Timestamp or java.sql.Date can be used depending on the pattern. |
3. Select the type of the Spark cluster you need to connect to.

   | Standalone | Talend Studio connects to a Spark-enabled cluster to run the Job from this cluster.  If you are using the Standalone mode, you need to set the following parameters:  * In the Spark host field, enter the URI   of the Spark Master of the Hadoop cluster to be used. * In the Spark home field, enter the   location of the Spark executable installed in the Hadoop cluster to be used. * If the Spark cluster cannot recognize the machine in which the Job is   launched, select this Define the driver hostname or IP   address check box and enter the host name or the IP address of   this machine. This allows the Spark master and its workers to recognize this   machine to find the Job and thus its driver.  Note that in this situation, you also need to add the name and the IP   address of this machine to its *host* file. |
   | Yarn client | Talend Studio runs the Spark driver to orchestrate how the Job should be performed and then send the orchestration to the Yarn service of a given Hadoop cluster so that the Resource Manager of this Yarn service requests execution resources accordingly.  If you are using the Yarn client mode, you need to set the following parameters in their corresponding fields (if you leave the check box of a service clear, then at runtime, the configuration about this parameter in the Hadoop cluster to be used will be ignored):  * In the Resource managerUse datanode   field, enter the address of the ResourceManager service of the Hadoop cluster to   be used. * Select the Set resourcemanager   scheduler address check box and enter the Scheduler address in   the field that appears. * Select the Set jobhistory   address check box and enter the location of the JobHistory   server of the Hadoop cluster to be used. This allows the metrics information of   the current Job to be stored in that JobHistory server. * Select the Set staging   directory check box and enter this directory defined in your   Hadoop cluster for temporary files created by running programs. Typically, this   directory can be found under the *yarn.app.mapreduce.am.staging-dir* property in the configuration files   such as *yarn-site.xml* or *mapred-site.xml* of your distribution. * If you are accessing the Hadoop cluster running with Kerberos security,   select this checkbox, then, enter the Kerberos principal names for the Resource   Manager service and the Job History service in the displayed fields. This enables   you to use your username to authenticate against the credentials stored in Kerberos.   These principals can be found in the configuration files of your distribution, such   as in *yarn-site.xml* and in *mapred-site.xml*.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains   pairs of Kerberos principals and encrypted keys. You need to enter the principal to   be used in the Principal field and the access   path to the keytab file itself in the Keytab   field. This keytab file must be stored in the machine in which your Job actually   runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily   the one a principal designates but must have the right to read the keytab file being   used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this   situation, ensure that *user1* has the right to read the keytab   file to be used. * The User name field is available when you   are not using Kerberos to authenticate. In the User   name field, enter the login username for your distribution. If you leave   it empty, the username of the machine hosting Talend Studio will   be used. * If the Spark cluster cannot recognize the machine in which the Job is   launched, select this Define the driver hostname or IP   address check box and enter the host name or the IP address of   this machine. This allows the Spark master and its workers to recognize this   machine to find the Job and thus its driver.  Note that in this situation, you also need to add the name and the IP   address of this machine to its *host* file. |
   | Yarn cluster | The Spark driver runs in your Yarn cluster to orchestrate how the Job should be performed.  If you are using the Yarn cluster mode, you need to define the following parameters in their corresponding fields (if you leave the check box of a service clear, then at runtime, the configuration about this parameter in the Hadoop cluster to be used will be ignored):  * In the Resource managerUse datanode   field, enter the address of the ResourceManager service of the Hadoop cluster to   be used. * Select the Set resourcemanager   scheduler address check box and enter the Scheduler address in   the field that appears. * Select the Set jobhistory   address check box and enter the location of the JobHistory   server of the Hadoop cluster to be used. This allows the metrics information of   the current Job to be stored in that JobHistory server. * Select the Set staging   directory check box and enter this directory defined in your   Hadoop cluster for temporary files created by running programs. Typically, this   directory can be found under the *yarn.app.mapreduce.am.staging-dir* property in the configuration files   such as *yarn-site.xml* or *mapred-site.xml* of your distribution. * Set path to custom Hadoop   configuration JAR: if you are using   connections defined in Repository to   connect to your Cloudera or Hortonworks cluster, you can   select this check box in the   Repository wizard and in the   field that is displayed, specify the path to the JAR file   that provides the connection parameters of your Hadoop   environment. Note that this file must be accessible from the   machine where you Job is launched.  This kind of Hadoop configuration JAR file is   automatically generated when you build a big data Job from Talend Studio. This JAR file is by default named with this   pattern: ```   hadoop-conf-[name_of_the_metadata_in_the_repository]_[name_of_the_context].jar   ``` You   can also download this JAR file from the web console of your cluster or   simply create a JAR file yourself by putting the configuration files in   the root of your JAR file. For example: ```   hdfs-sidt.xml   core-site.xml   ```  The parameters from your custom JAR file override the parameters   you put in the Spark configuration field.   They also override the configuration you set in the   configuration components such as   tHDFSConfiguration or   tHBaseConfiguration when the related   storage system such as HDFS, HBase or Hive are native to Hadoop.   But they do not override the configuration set in the   configuration components for the third-party storage system such   as tAzureFSConfiguration. * If you are accessing the Hadoop cluster running with Kerberos security,   select this checkbox, then, enter the Kerberos principal names for the Resource   Manager service and the Job History service in the displayed fields. This enables   you to use your username to authenticate against the credentials stored in Kerberos.   These principals can be found in the configuration files of your distribution, such   as in *yarn-site.xml* and in *mapred-site.xml*.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains   pairs of Kerberos principals and encrypted keys. You need to enter the principal to   be used in the Principal field and the access   path to the keytab file itself in the Keytab   field. This keytab file must be stored in the machine in which your Job actually   runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily   the one a principal designates but must have the right to read the keytab file being   used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this   situation, ensure that *user1* has the right to read the keytab   file to be used. * The User name field is available when you   are not using Kerberos to authenticate. In the User   name field, enter the login username for your distribution. If you leave   it empty, the username of the machine hosting Talend Studio will   be used. * Select the Wait for the Job to   complete check box to make Talend Studio or,   if you use Talend JobServer,   your Job JVM keep monitoring the Job until the execution of the Job is over. By   selecting this check box, you actually set the   spark.yarn.submit.waitAppCompletion property to be true.   While it is generally useful to select this check box when running a Spark Batch Job,   it makes more sense to keep this check box clear when running a Spark Streaming   Job. |

   Ensure that the username in the Yarn
   client mode is the same one you put in
   tHDFSConfiguration, the component used to provide HDFS
   connection information to Spark.
4. With the Yarn client mode, the Property type list is displayed to allow you to select an
   established Hadoop connection from the Repository, on
   the condition that you have created this connection in the Repository. Then Talend Studio will
   reuse that set of connection information for this Job.
5. If you need to launch from Windows, it is recommended to specify where
   the *winutils.exe* program to be used is stored.

   * If you know where to find your *winutils.exe* file and you want to use it, select the Define the Hadoop home directory check box
     and enter the directory where your *winutils.exe* is
     stored.
   * Otherwise, leave this check box clear, Talend Studio generates one by itself and automatically uses it for this Job.
6. In the Spark "scratch" directory
   field, enter the directory in which Talend Studio
   stores in the local system the temporary files such as the jar files to be
   transferred. If you launch the Job on Windows, the default disk is *C:*. As a result, if you leave */tmp* in this field, this
   directory is *C:/tmp*.

## Results

* After the connection is configured, you can tune
  the Spark performance, although not required, by following the process explained in:
  + [Tuning Spark for Apache Spark Batch Jobs](/talend/r/en-US/8.0/components/spark-batch/tuning-spark-for-apache-spark-batch-jobs-spark-batch-component) for Spark Batch Jobs.
  + [Tuning Spark for Apache Spark Streaming Jobs](/talend/r/en-US/8.0/components/spark-streaming/tuning-spark-for-apache-spark-streaming-jobs-spark-stream-component) for Spark Streaming Jobs.
* It is recommended to activate the Spark logging and
  checkpointing system in the Spark configuration tab of the Run view of your Spark
  Job, in order to help debug and resume your Spark Job when issues arise:
  + [Logging and checkpointing the activities of your Apache Spark Job](/talend/r/en-US/8.0/components/spark-batch/logging-and-checkpointing-activities-of-your-apache-spark-job-spark-batch-component-if-you).
* If you are using Cloudera V5.5+ to run your MapReduce or Apache Spark Batch
  Jobs, you can make use of Cloudera Navigator to trace the lineage of given
  data flow to discover how this data flow was generated by a Job.
  + [Defining data lineage with Cloudera Navigator](/talend/en-US/components/8.0/cloudera/defining-data-lineage-with-cloudera-navigator-mapreduce-component-in).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-design-data-flow-of-kudu-job-in -->
# Design the data flow of the Kudu Job

Last updated: 9/30/2026

## Procedure

1. In the Integration
   perspective of Talend Studio,
   create an empty Spark Batch Job from the Job Designs node in
   the Repository tree view.

   For further information about how to create a Spark Batch Job, see [Creating a Spark Job](/talend/r/en-US/8.0/studio-user-guide/creating-spark-job).
2. In the workspace, enter the name of the component to be used and select this
   component from the list that appears. In this scenario, the components are
   tHDFSConfiguration, tKuduConfiguration, tFixedFlowInput, tKuduOutput,
   tKuduInput and tLogRow.

   The tFixedFlowInput component is used to load the
   sample data into the data flow. In the real-world practice, you can use other
   components such as tFileInputDelimited, alone or even
   with a tMap, in the place of
   tFixedFlowInput to design a sophisticated process to
   prepare your data to be processed.
3. Connect tFixedFlowInput to tKuduOutput using the Row > Main link.
4. Connect tMongoDBInput to tLogRow using the Row > Main link.
5. Connect tFixedFlowInput to tMongoDBInput using the Trigger > OnSubjobOk link.
6. Leave tHDFSConfiguration and tKuduConfiguration alone without any
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-partition-sample-data-and-writing-it-to-kudu -->
# Partition the sample data and writing it to Kudu

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowIput component to
   open its Component view.

   ### Example
2. Click the [...] button next to Edit schema to open the schema editor.
3. Click the [+] button to add the schema
   columns as shown in this image.

   ### Example
4. In the Type column, select
   Integer for the `age` column.
5. In the Key column, select the check box for the
   `age` column to define this column as key primary key
   column.
6. Click OK to validate these changes and accept
   the propagation prompted by the pop-up dialog box.
7. In the Mode area, select the Use Inline
   Content radio button and paste the previously mentioned sample data
   into the Content field that is displayed.
8. In the Field separator field, enter a
   semicolon (*;*).
9. Double-click the tKuduOutput component to
   open its Component view.

   ### Example
10. Select the Use an existing configuration check box and
    then select the Kudu configuration you configured in the previous steps from the
    Component list drop-down list.
11. Click Sync columns to ensure that
    tKuduOutput has the same schema as
    tFixedFlowInput.
12. In the Table field, enter the name of the table you want
    to create in Kudu.
13. From the Action on table drop-down list, select
    Drop table if exists and create.
14. In Range partitions, add one row by clicking the
    [+] button and do the following:
    1. In Partition No, enter, without double quotation
       marks, the number to be used as the ID of the partition to be created.
       For example, enter `1` to create Partition 1.
    2. In Partition column, select the primary key
       column to be used for partitioning. In this scenario, select
       `age`.
    3. In Lower boundary, enter
       `20` without double quotation marks because the
       type of the age data is integer.
    4. In Upper boundary, do the same to set it to
       `60`.

    This partitioning definition creates the partition schema reading as
    follows:

    ```
    RANGE (age) (
        PARTITION 20 <= VALUES < 60
    )
    ```

    According
    to this partition schema, the record falling on the lower boundary, the age
    `20`, is included in this partition and thus is written in
    Kudu but the record falling on the upper boundary, the age
    `60`, is excluded and is not written in Kudu.

    In the
    real-world practice, if you need to write all the data in the Kudu table, define
    more partitions to receive the data with proper boundaries.
15. From the Action on data drop-down list, select
    Insert.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduoutput-tkuduconfiguration-tmap-scanning-data-from-kudu -->
# Scanning data from Kudu

Last updated: 9/30/2026

## Procedure

1. Double-click tKuduInput to open its
   Component view.

   ### Example
2. Click the [...] button next to Edit
   schema to open the schema editor.
3. Click the [+] button to add the schema columns for
   output as shown in this image.

   ### Example
4. In the Type field, select Integer
   as data type for the `age` column.
5. In the Key column, select the check box for the
   `age` column because this is the primary key
   column.
6. Click OK to validate these changes and accept the
   propagation prompted by the pop-up dialog box.
7. In the Table name field, enter the name of the table
   from which you need to read data. In this scenario, it is
   `ychen_kudu`.
8. In the Query mode area, select the Use
   scan radio button to read all the data from the Kudu
   table.
9. Double-click tLogRow to open its
   Component view and select the Table radio button to present the result in a
   table.
10. Press 
    F6
     to run this Job.

## Results

Once done, in the console of the Run view, you
can check the data read from the Kudu table.

The record 04;tom;60 is not written in the table because it is out
of the partition boundaries.

In the real-world practice, upon the success of the
execution, you can deploy and launch your Job on a Talend JobServer if you
have one.
