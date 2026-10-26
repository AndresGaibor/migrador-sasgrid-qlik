<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput · versión 8.0 -->
# tCassandraInput

Last updated: 9/30/2026

Extracts the desired data from a standard or super column family of a Cassandra
keyspace so as to apply changes to the data.

tCassandraInput allows you to read data from a Cassandra keyspace and
send data in the Talend
flow.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tCassandraInput Standard properties](/talend/en-US/components/8.0/cassandra/tcassandrainput-standard-properties)
* [tCassandraInput properties for Apache Spark Batch](/talend/en-US/components/8.0/cassandra/tcassandrainput-properties-for-apache-spark-batch)

**Related concepts**  

* [Handling data with Cassandra](tcassandrainput-tcassandraoutput-tlogrow-handling-data-with-cassandra-standard-component-bigdata-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-properties-for-apache-spark-batch -->
# tCassandraInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tCassandraInput running
in the Spark Batch Job framework.

The Spark Batch
tCassandraInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   The schema of this component does not support the Object type and the List type. |
| Keyspace | Type in the name of the keyspace from which you want to read data. |
| Column family | Type in the name of the column family from which you want to read data. |
| Selected column function | Select the columns about which you need to retrieve the *TTL* (time to live) or the *writeTime* property.  The TTL property determines the time for records in a column to expire; the writeTime property indicates the time when a record was created.  For further information about these properties, see Datastax's documentation for Cassandra CQL. |
| Filter function | Define the filters you need to use to select the records to be processed.  The component generates the WHERE ALLOW FILTERING clause using the filters you put and thus this filter function is subject to the limit of this Cassandra clause. |
| Order by clustering column | Select how you need to sort the retrieved records. You can select NONE so as not to sort the data. |
| Use limit | Select this check box to display the Limit per partition field, in which you enter the number of the rows to be retrieved starting from the first row. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use one and only one tCassandraConfiguration component present in the same Job to connect to Cassandra. More than one tCassandraConfiguration components present in the same Job fail the execution of the Job.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-standard-properties -->
# tCassandraInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tCassandraInput running in the Standard Job framework.

The Standard
tCassandraInput component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| DB Version | Select the Cassandra version you are using from the drop-down list. |
| Host | Enter the hostname or IP address of the Cassandra server. |
| Port | Enter the listening port number of the Cassandra server. |
| Datacenter | Enter the name of the Cassandra datacenter. |
| Required authentication | Select this check box to provide credentials for the Cassandra authentication.  This check box appears only if you do not select the Use existing connection check box. |
| Username | Fill in this field with the username for the Cassandra authentication.  This field is only available when you select the Required authentication check box. |
| Password | Fill in this field with the password for the Cassandra authentication.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This field is only available when you select the Required authentication check box. |
| Use SSL | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| Keyspace | Type in the name of the keyspace from which you want to read data. |
| Column family | Type in the name of the column family from which you want to read data. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Query | Enter the query statements to be used to read data from the Cassandra database.  By default, the query is not case-sensitive. This means that at runtime, the column names you put in the query are always taken in lower case. If you need to make the query case-sensitive, put the column names in double quotation marks.  The [...] button next to this field allows you to generate the sample code that shows what the pre-defined variables are for the data to be read and how these variables can be used. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component always needs an output link. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-handling-data-with-cassandra-standard-component-bigdata-this -->
# Handling data with Cassandra

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

This scenario describes a simple Job that reads the employee data from a CSV file,
writes the data to a Cassandra keyspace, then extracts the personal information of some
employees and displays the information on the console.

This scenario requires six components, which are:

* tCassandraConnection: opens a connection
  to the Cassandra server.
* tFileInputDelimited: reads the input
  file, defines the data structure and sends it to the next component.
* tCassandraOutput: writes the data it
  receives from the preceding component into a Cassandra keyspace.
* tCassandraInput: reads the data from the
  Cassandra keyspace.
* tLogRow: displays the data it receives
  from the preceding component on the console.
* tCassandraClose: closes the connection to
  the Cassandra server.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-dropping-and-linking-components-standard-component-bigdata-drop)
* [Configuring the components](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-configuring-components-standard-component-bigdata)
* [Saving and executing the Job](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-saving-and-executing-job-standard-component-bigdata-press)

**Related concepts**  

* [tCassandraInput](tcassandrainput "Extracts the desired data from a standard or super column family of a Cassandra keyspace so as to apply changes to the data.")
* [tCassandraOutput](tcassandraoutput "Writes data into or deletes data from a column family of a Cassandra keyspace.")

**Related reference**  

* [tCassandraConnection](tcassandraconnection "Enables the reuse of the connection it creates to a Cassandra server.")
* [tCassandraClose](tcassandraclose "Disconnects a connection to a Cassandra server so as to release occupied resources.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-configuring-components-standard-component-bigdata -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Opening a Cassandra connection](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-opening-cassandra-connection-standard-component-bigdata)
* [Reading the input data](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-reading-input-data-standard-component-bigdata)
* [Writing data to a Cassandra keyspace](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-writing-data-to-cassandra-keyspace-standard-component-bigdata)
* [Reading data from the Cassandra keyspace](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-reading-data-from-cassandra-keyspace-standard-component-bigdata)
* [Displaying the information of interest](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-displaying-information-of-interest-standard-component-bigdata)
* [Closing the Cassandra connection](/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-closing-cassandra-connection-standard-component-bigdata)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-dropping-and-linking-components-standard-component-bigdata-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tCassandraConnection, tFileInputDelimited, tCassandraOutput, tCassandraInput, tLogRow
   and tCassandraClose.
2. Connect tFileInputDelimited to tCassandraOutput using a Row > Main link.
3. Do the same to connect tCassandraInput to
   tLogRow.
4. Connect tCassandraConnection to tFileInputDelimited using a Trigger > OnSubjobOk
   link.
5. Do the same to connect tFileInputDelimited to tCassandraInput and tCassandraInput to tCassandraClose.
6. Label the components to better identify their functions.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-saving-and-executing-job-standard-component-bigdata-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Execute the Job by pressing F6 or
   clicking Run on the Run tab.

   The personal information of three employees is displayed on the
   console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-closing-cassandra-connection-standard-component-bigdata -->
# Closing the Cassandra connection

Last updated: 9/30/2026

## Procedure

1. Double-click the tCassandraClose
   component to open its Component
   view.
2. Select the connection to be closed from the Component List.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-displaying-information-of-interest-standard-component-bigdata -->
# Displaying the information of interest

Last updated: 9/30/2026

## Procedure

1. Double-click the tLogRow component to
   open its Component view.
2. In the Mode area, select Table (print values in cells of a table).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-opening-cassandra-connection-standard-component-bigdata -->
# Opening a Cassandra connection

Last updated: 9/30/2026

## Procedure

1. Double-click the tCassandraConnection component to open its Basic settings view in the Component tab.
2. Select the Cassandra version that you are using from the DB Version list.

   Information noteNote: With Cassandra version 4.0.x, the default value for the
   datastax-java-driver.basic.request.timeout driver parameter is
   set at 2 seconds. If the default value is too short for your data operation, you
   can update it in the Advanced settings tab of your Job as
   follow:

   For more information, see [DataStax Java Driver 4.13](https://docs.datastax.com/en/developer/java-driver/4.13/manual/core/configuration/) from DataStax
   documentation.
3. In the Server field, type in the hostname
   or IP address of the Cassandra server. In this example, it is *localhost*.
4. In the Port field, type in the listening
   port number of the Cassandra server.
5. If required, select the Required
   authentication check box and type in the authentication information
   for the Cassandra connection: Username and
   Password.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-reading-data-from-cassandra-keyspace-standard-component-bigdata -->
# Reading data from the Cassandra keyspace

Last updated: 9/30/2026

## Procedure

1. Double-click the tCassandraInput
   component to open its Component
   view.
2. Type in required information for the connection or use the existing
   connection you have configured before. In this scenario, the Use existing connection check box is
   selected.
3. In the Keyspace configuration area, type
   in the name of the keyspace: *Employee* in
   this example.
4. In the Column family configuration area,
   type in the name of the column family: *Employee\_Info* in this example.
5. Select Edit schema to define the data
   structure to be read from the Cassandra keyspace. In this example, three
   columns *id*, *name* and *age* are
   defined.
6. If needed, select the Include key in output
   columns check box, and then select the key column of the
   column family you want to include from the Key
   column list.
7. From the Row key type list, select
   *Integer* because *id* is of integer type in this example.

   Keep the Default option for the row key
   Cassandra type because its value will become the corresponding Cassandra
   type *Int32* automatically.
8. In the Query configuration area, select
   the Specify row keys check box and specify
   the row keys directly. In this example, three rows will be read. Next,
   select the Specify columns check box and
   specify the column names of the column family directly. This scenario will
   read three columns from the keyspace: *id*,
   *name* and *age*.
9. If needed, the Key start and the
   Key end fields allow you to define the
   range of rows, and the Key limit field
   allows you to specify the number of rows within the range of rows to be
   read. Similarly, the Columns range start
   and the Columns range end fields allow you
   to define the range of columns of the column family, and the Columns range limit field allows you to specify
   the number of columns within the range of columns to be read.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-reading-input-data-standard-component-bigdata -->
# Reading the input data

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Component view.
2. Click the [...] button next to the
   File Name/Stream field to browse to the
   file that you want to read data from. In this scenario, the directory is
   *D:/Input/Employees.csv*. The CSV file
   contains four columns: *id*, *age*, *name*
   and *ManagerID*.id;age;name;ManagerID
   1;20;Alex;1
   2;40;Peter;1
   3;25;Mark;1
   4;26;Michael;1
   5;30;Christophe;2
   6;26;Stephane;3
   7;37;Cedric;3
   8;52;Bill;4
   9;43;Jack;2
   10;28;Andrews;4
3. In the Header field, enter *1* so that the first row in the CSV file will be
   skipped.
4. Click Edit schema to define the data to
   pass on to the tCassandraOutput component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cassandra/tcassandrainput-tcassandraoutput-tlogrow-writing-data-to-cassandra-keyspace-standard-component-bigdata -->
# Writing data to a Cassandra keyspace

Last updated: 9/30/2026

## Procedure

1. Double-click the tCassandraOutput
   component to open its Basic settings view
   in the Component tab.
2. Type in required information for the connection or use the existing
   connection you have configured before. In this scenario, the Use existing connection check box is
   selected.
3. In the Keyspace configuration area, type
   in the name of the keyspace: *Employee* in
   this example, and select *Drop keyspace if exists and
   create* from the Action on
   keyspace list.
4. In the Column family configuration area,
   type in the name of the column family: *Employee\_Info* in this example, and select *Drop column family if exists and create* from
   the Action on column family list.
5. In the Action on data list, select the
   action you want to carry on, *Update* in
   this example.
6. Click Sync columns to retrieve the schema
   from the preceding component.
7. Select the key column of the column family from the Key column list. In this example, it is *id*.

   If needed, select the Include key in
   columns check box.
