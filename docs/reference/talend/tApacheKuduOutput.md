<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tapachekuduoutput · versión 8.0 -->
# tApacheKuduOutput

Last updated: 9/30/2026

Writes data to an Apache Kudu table.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tApacheKuduOutput Standard properties

These properties are used to configure tApacheKuduOutput running in the Standard Job framework.

The Standard
tApacheKuduOutput component belongs to the Big Data family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the R2022-01 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Master addresses | Click the plus button on the bottom of this field to add and configure master addresses.   * Master node host name: Enter the IP address or hostname that identifies the Apache Kudu cluster master node. * Master node port: Enter the port associated with the Apache Kudu cluster master node.   To add multiple master nodes that are of the same Apache Kudu cluster, add them in separate rows. |
| Table name | Enter the name of the Apache Kudu table to write data to. You can also select the name of the Apache Kudu table by clicking the [...] button next to this field. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Write operation | Specify the write operation to perform. Currently, this component only inserts data to Apache Kudu tables. |
| Create if not exist | Select this option to create the table if the table specified in the Table name field does not exist. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |
| Max batch size | Specify the maximum number of lines that can be processed in a batch. |
| Set primary key(s) | Select this option to add primary keys manually. If this option is not selected, the first field is used as the primary key.  If you are creating a new table, the primary key you define cannot be changed once the table is created. |
| Generate default partitioning | Select this option to generate the default partitions when inserting data.  This option is available when Create if not exist is selected in the Basic settings view. |
| Hash partitioning columns | Click the plus button on the bottom of this field to add columns based on which rows are hash-partitioned. The columns specified need to exist in the data and to be defined in the schema.  By default, a newly created table is partitioned. It is recommended to define how a newly created table is partitioned. See [Hash partitioning](https://kudu.apache.org/docs/schema_design.html#hash-partitioning) for related information.  This field is available when Create if not exist is selected in the Basic settings view and Generate default partitioning is not selected. |
| Bucket number | Enter the number of the buckets to be used to store the partitions. Buckets are created on the fly.  At runtime, rows are distributed by hash values as specified in the Hash partitioning columns field in one of these buckets. If you leave the Hash partitioning columns field empty, hash partitioning is not applied during the creation of the table.  This field is available when Create if not exist is selected in the Basic settings view.  See [Hash partitioning](https://kudu.apache.org/docs/schema_design.html#hash-partitioning) for related information. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link. |
