<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thivewarehouseoutput · versión 8.0 -->
# tHiveWarehouseOutput

Last updated: 9/30/2026

Connects to a given Hive database and writes the received data into a given Hive
table or a directory in HDFS using Hive Warehouse Connector.

Hive Warehouse Connector supports Hive internal tables which allow you to access ACID
table data from Spark with Apache Hive 3 tables.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHiveWarehouseOutput properties for Apache Spark Batch

These properties are used to configure tHiveWarehouseOutput
running in the Spark Batch Job framework.

The Spark Batch
tHiveWarehouseOutput component belongs to the Storage family.

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
| Output source | Select the type of the output data you want tHiveWarehouseOutput to change:  * Hive table: the Database field, the Table name field, the Table format list and the Enable   Hive partitions check box are displayed. You need to enter   the related information about the Hive database to be connected to and the   Hive table you need to modify.  By default, the format of the output data is JSON, but you can   change it to ORC or Parquet by selecting the corresponding option from the   Table format list. * ORC file: the Output folder field is displayed and the   Hive storage configuration list is deactivated, because the ORC file should   be stored in your HDFS system hosting Hive. You need to enter the directory   in which the output data is written. |
| Save mode | Select the type of changes you want to make regarding the target Hive table:  * Create: creates the target Hive table and   writes data in this table. * Append: adds data to an existing table. * Overwrite: overwrites the data of the   existing table. * Create if it does not exist: creates a Hive table   and adds data in it if there is no existing table. If there is an existing   table, the input data is not saved. This property is available when you   have installed the 8.0.1-R2024-03 Studio Monthly or a later one provided   by Talend. For more information, check with your administrator. |
| Enable Hive partitions | Select the Enable Hive partitions check box and in the Partition keys table, define partitions for the Hive table you are creating or changing. In the Partition keys table, select columns from the input schema of tHiveOutput to use as partition keys.  Bear in mind that:  * When the Save mode to be used is   `Append`, meaning that you are   adding data to an existing Hive table, the partition columns   you select in the Partition keys   table must be already partition keys of the Hive table to be   updated. * A partitioned Hive table created by tHiveOutput can only be read   by tHiveInput due to Spark specific   limitations. If you need to read your partitioned table   through Hive itself, it is recommended to use   tHiveRow or   tHiveCreateTable in a Standard Job to   create this table and then use tHiveOutput to append data to it. * Defining columns as partition keys does not alter your data   but only create subfolders using the partition keys and put   data in them. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Sort columns alphabetically | Select this check box to sort the schema columns in the alphabetical order. If you leave this check box clear, these columns stick to the order defined in the schema editor. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tHiveWarehouseConfiguration component present in the same Job to connect to Hive.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job. |
