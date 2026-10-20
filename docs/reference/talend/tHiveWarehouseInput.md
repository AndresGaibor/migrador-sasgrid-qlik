<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thivewarehouseinput · versión 8.0 -->
# tHiveWarehouseInput

Last updated: 9/30/2026

Extracts data from Hive and sends the data to the component that follows using
Hive Warehouse Connector.

Hive Warehouse Connector supports Hive internal tables which allow you to access ACID
table data from Spark with Apache Hive 3 tables.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHiveWarehouseInput properties for Apache Spark Batch

These properties are used to configure tHiveWarehouseInput
running in the Spark Batch Job framework.

The Spark Batch
tHiveWarehouseInput component belongs to the Storage family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Hive Storage Configuration | Select the tHiveWarehouseConfiguration component from which you want Spark to use the configuration details to connect to Hive. |
| HDFS Storage Configuration | Select the tHDFSConfiguration component from which you want Spark to use the configuration details to connect to a given HDFS system and transfer the dependent jar files to this HDFS system. This field is relevant only when you are using an on-premises distribution. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Always use lowercase when naming a field because the processing behind the scene could force the field names to be lowercase.  Select the type of schema you want to use from the Schema drop-down list:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Input source | Select the type of the input data you want tHiveWarehouseInput to read:  * Hive Query: the   Database and Hive   query fields are displayed. You need to enter the related   information about the Hive database to be connected to, and the Hive   query statement you want to use to select the data to be used * ORC file: the Input file name field is displayed and the   Hive storage configuration list is deactivated, because the ORC file should   be stored in your HDFS system hosting Hive. You need to enter the directory   where the file to be used is stored.   For further information, see the [Hive query language manual](https://cwiki.apache.org/confluence/display/Hive/LanguageManual).  Information noteNote: Compressed data in the form of Gzip or Bzip2 can be processed through the query statements. For details, see [Compressed Data Storage](https://cwiki.apache.org/confluence/display/Hive/CompressedStorage). Hadoop provides different compression formats that help reduce the space needed for storing files and speed up data transfer. When reading a compressed file, Talend Studio needs to extract it before being able to feed it to the input flow. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Register Hive UDF jars | Add the Hive user-defined function (UDF) jars you want tHiveInput to use. Note that you must define a function alias for each UDF to be used in the Temporary UDF functions table.  Once you add one row to this table, click it to display the [...] button and then click this button to display the jar import wizard. Through this wizard, import the UDF jar files you want to use.  A registered function is often used in a Hive query that you edit in the Hive Query field in the Basic settings view. Note that this Hive Query field is displayed only when you select Hive query from the Input source list. |
| Temporary UDF functions | Complete this table to give each imported UDF class a temporary function name to be used in the Hive query in the current tHiveInput component. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tHiveWarehouseConfiguration component present in the same Job to connect to Hive.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job. |
