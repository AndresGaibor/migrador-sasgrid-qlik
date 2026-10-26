<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/iceberg/ticebergtable · versión 8.0 -->
# tIcebergTable

Last updated: 9/30/2026

Creates, truncates, or deletes Iceberg tables using Hive or Impala.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tIcebergTable Standard properties](/talend/en-US/components/8.0/iceberg/ticebergtable-standard-properties)
* [tIcebergTable properties for Apache Spark Batch](/talend/en-US/components/8.0/iceberg/ticebergtable-properties-for-apache-spark-batch)

**Related concepts**  

* [Working with Iceberg branches and tags](working-with-iceberg-branches-and-tags "This scenario describes a Standard Job that performs different actions on Iceberg branches and tags such as creating, merging, or deleting.")
* [Working with Iceberg tables](working-with-iceberg-tables "This scenario describes a Standard Job that performs different standard actions with Iceberg tables such as converting, reading, updating, or merging.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/iceberg/ticebergtable-properties-for-apache-spark-batch -->
# tIcebergTable properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tIcebergTable running in the
Spark Batch Job framework.

The Spark Batch
tIcebergTable component belongs to the Big Data family.

The component in this framework is available in all Talend
products.

This component is available when you have installed the 8.0.1-R2024-07 Studio Monthly or a
later one provided by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component. Select the type of schema from the drop-down list:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.  This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list. |
| Catalog and Schema | To retrieve a dataset from Unity Catalog, specify the following parameters:  * Catalog: enter the name of the catalog to be used. * Schema: enter the name of the schema to be used.   These fields are only available when you select Enable Unity Catalog with Databricks in the Spark Configuration view of your Spark Batch Job.  These properties are only available when you have installed the 8.0.1-R2025-10 Studio Monthly or a later one provided by Talend. For more information, confirm with your administrator. |
| Table name | Enter the name of the Iceberg table on which you want to work. |
| Action on table | Select the action you want to perform on the Iceberg table from the drop-down list:  * Alter: makes changes to a table. This action is not available when you select Enable Unity Catalog   with Databricks in the Spark Configuration   view of your Spark Batch Job. * Create: creates a table. * Create if it does not exist: creates a table   only if no table already exists. * Drop: removes table. * Drop if exists: removes a table only if it   already exists. * Replace as select: replaces a table using a SQL   query. This action is not available when you select Enable Unity Catalog   with Databricks in the Spark Configuration   view of your Spark Batch Job. |
| Create as select | Select this check box to create a table at the beginning of a query execution. The query needs to be specified in the As select query parameter. For more information, see [Create table as select](https://iceberg.apache.org/docs/latest/hive/#create-table-as-select) from Apache Iceberg documentation. This parameter is only available when you select Create or Create if it does not exist from the Action on table drop-down list. |
| Set table comment | Select this check box to add a comment to the table. This parameter is only available when you select Create or Create if it does not exist from the Action on table drop-down list. |
| Set table location | Select this check box to specify a location path in which you want the table to be created. This parameter is only available when you select Create or Create if it does not exist from the Action on table drop-down list. |
| Set partitions | Select this check box and click the plus button to create partitions inside the table. This parameter is only available when you select Create or Create if it does not exist from the Action on table drop-down list. |
| Set table properties | Select this check box to enter any extra configuration properties following the key and values format by clicking the plus button. For example, you can add properties such as format-version. For more information on available configuration properties, see [Configuration](https://iceberg.apache.org/docs/latest/configuration/) from Apache Iceberg documentation. This parameter is only available when you select Create or Create if it does not exist from the Action on table drop-down list. |
| Purge | Select this check box to delete the table content. For more information, see  [DROP TABLE PURGE](https://iceberg.apache.org/docs/nightly/spark-ddl/#drop-table-purge)  from the Iceberg documentation. This parameter is only available when you select Drop or Drop if exists from the Action on table drop-down list. |
| As select query | Enter the SQL SELECT query to be performed to replace the table. For more information, see [Create table as select](https://iceberg.apache.org/docs/latest/hive/#create-table-as-select) from Apache Iceberg documentation. This parameter is only available when you select Replace as select from the Action on table drop-down list. |
| Alter table action | Select from the drop-down list the action you want to perform on the table:  * Add columns: adds one or more columns to the   table. * Add partitions: adds a partition to the   table, either a table column or an expression based on a table   column. * Alter columns: modifies the name, the type, and the   comment of altered columns. * Create branch: creates a branch. * Create tag: creates a tag. * Create branch if not exists: creates a branch   if no branch already exists. * Create tag if not exists: creates a tag if no   tag already exists. * Create or replace branch: creates or replaces   a branch. * Create or replace tag: creates or replaces a   tag. * Drop branch: removes a branch. * Drop columns: removes one or more columns. * Drop partitions: removes a partition. * Drop tag: removes a tag. * Drop branch if exists: removes a branch   without failing if the branch does not exist. * Drop tag if exists: removes a tag without   failing if the branch does not exist. * Rename columns: renames one or more columns. * Reorder columns: reorder one or more columns, either   as the first column in the table or after another specific column. * Replace branch: replaces a branch. * Replace partitions: replaces a partition with   a new expression to be used. * Replace tag: replaces a tag.   For more information about branches and tags, see [Branches and tags](https://iceberg.apache.org/docs/nightly/hive/#branches-and-tags) from the Iceberg documentation.  For more information about partitions, see [PARTITIONED BY](https://iceberg.apache.org/docs/nightly/spark-ddl/#partitioned-by) from the Iceberg documentation.  This parameter is only available when you select Alter from the Action on table drop-down list. |
| Set snapshot | Select this check box to specify the snapshot from which you want to create either the branch or the tag. This parameter is only available when you select Alter from the Action on table drop-down list, and when you perform a creation of branches or tags. |
| Set retain | Select this check box to specify a retain duration for the branch or the tag. This parameter is only available when you select Alter from the Action on table drop-down list, and when you perform a creation of branches or tags. |
| Set min snapshots to keep | Select this check box to specify a minimum snapshots to be kept for the branch. This parameter is only available when you select Alter from the Action on table drop-down list, and when you perform a creation of branches. |
| Set max snapshot age | Select this check box to specify the snapshots maximum age for the branch. This parameter is only available when you select Alter from the Action on table drop-down list, and when you perform a creation of branches. |

## Global variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is generally used with other Iceberg components. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/iceberg/ticebergtable-standard-properties -->
# tIcebergTable Standard properties

Last updated: 9/30/2026

These properties are used to configure tIcebergTable running in
the Standard Job framework.

The Standard
tIcebergTable component belongs to the Big Data family.

The component in this framework is available in all Talend
products.

This component is available when you have installed the 8.0.1-R2023-11 Studio Monthly or a
later one provided by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select from the drop-down list the tIcebergConnection component by which the desired connection is established. |
| Table name | Enter the name of the Iceberg table on which you want to work. |
| Action on table | Select the action you want to perform on the Iceberg table from the drop-down list:  * Alter: modifies columns of the table. This   parameter is only available when you have installed the 8.0.1-R2024-01   Studio Monthly or a later one provided by Talend. For more information, check with your administrator. * Create: creates a table. * Create if not exists: creates a table only if no   table already exists. * Drop: removes table. * Drop if exists: removes a table only if it already   exists. * Truncate: deletes the table content. |
| Create like | Select this check to create a table based on an existing table. The existing table name needs to be specified in the Source table parameter. For more information, see [Create table like table](https://iceberg.apache.org/docs/latest/hive/#create-table-like-table) from Apache Iceberg documentation. This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list, and when the Create as select check box is not selected. |
| Create as select | Select this check box to create a table at the beginning of a query execution. The query needs to be specified in the As select query parameter. For more information, see [Create table as select](https://iceberg.apache.org/docs/latest/hive/#create-table-as-select) from Apache Iceberg documentation. This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list, and when the Create like check box is not selected. |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component. Select the type of schema from the drop-down list:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.  This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list. |
| Set format | Select this check box to specify the file format, and then select the format from the drop-down list:  * AVRO * ORC * PARQUET   This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list, and when the Create like and Create as select check boxes are not selected. |
| Create external table | Select this check box to create an external table. This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list. |
| Set partitions | Select this check box to create partitions inside the table, and then specify the new schema in the Schema parameter that appears. This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list. |
| Set catalog | Select this check box to specify a catalog to be used to create the table into. This property is only available when you have installed the 8.0.1-R2024-02 Studio Monthly or a later one provided by Talend. For more information, check with your administrator. |
| Set location | Select this check box to specify a location path in which you want the table to be created. This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list. |
| Table properties | Enter any extra configuration properties following the key and values format by clicking the plus button. For example, you can add properties such as format-version. For more information on available configuration properties, see [Configuration](https://iceberg.apache.org/docs/latest/configuration/) from Apache Iceberg documentation. This parameter is only available when you select Create or Create if not exists from the Action on table drop-down list. |
| Alter table action | Select from the drop-down list the action you want to perform on the table:  * Add columns: adds columns that are in the schema   list from the New columns parameter. You can edit   this schema by clicking Edit schema. * Change columns: updates columns by adding parameters   in the Column mapping table. * Drop columns: removes columns that are not in the   schema list from the Remaining columns parameter. You   can edit this schema by clicking Edit schema. * Set partitions: updates the partitioning schema by   adding parameters in the Partitions table. * Create branch: creates a branch either   Using default properties, At a specific   snapshot ID, Using system time, or   Using specific tag. You can also specify a number   of snapshot retentions when creating a branch by selecting the   Set number of snapshot retentions checkbox. * Drop branch: removes a branch. * Drop branch if exists: removes a branch without   failing if the branch does not exist. * Create tag: creates a tag either Using   default properties, At a specific snapshot   ID, or Using system time. * Drop tag: removes a tag. * Drop tag if exists: removes a tag without failing if   the branch does not exist.   For more information about branches and tags, see [Branches and tags](https://iceberg.apache.org/docs/nightly/hive/#branches-and-tags) from the Iceberg documentation.  This parameter is only available when you select Alter from the Action on table drop-down list.  This parameter is only available when you have installed the 8.0.1-R2024-01 Studio Monthly or a later one provided by Talend. The branch and tag options are only available when you have installed the 8.0.1-R2024-06 Studio Monthly or a later one provided Talend. For more information, check with your administrator. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is generally used with other Iceberg components. |
