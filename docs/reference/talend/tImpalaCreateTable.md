<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/impala/timpalacreatetable · versión 8.0 -->
# tImpalaCreateTable

Last updated: 9/30/2026

Creates Impala tables that fit a wide range of Impala data formats.

tImpalaCreateTable connects to the Impala database to be
used and creates an Impala table that is dedicated to data of the format you specify.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tImpalaCreateTable Standard properties

These properties are used to configure tImpalaCreateTable running in the Standard Job framework.

The Standard
tImpalaCreateTable component belongs to the Big Data family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Select the way the connections details will be stored:  * Built-in: No property data stored   centrally. * Repository: Select the repository file in which   the properties are stored. The fields that follow are completed   automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Impala Driver | Select the driver you are using from the drop-down list. |
| Host | Enter the database server IP address. |
| Port | Enter the listening port number of the database server. |
| Database | Enter the name of the database. |
| Additional JDBC Settings | Specify additional connection properties for the database connection you are creating.  This option is not available if you have selected the Use an existing connection check box in the Basic settings view. |
| Username and Password | Enter the database user authentication data to authenticate using LDAP.  To enter the password, click the […] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  These parameters are not available when you select the Use kerberos authentication check box. |
| Use Kerberos authentication | If you are accessing an Impala system running with Kerberos security, select this checkbox and then enter the Kerberos principal of this Impala system. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Table Name | Enter the name of the table to be created. |
| Action on table | Select the action to be carried out for creating a table:  * Create table: a table is created. * Create table if not exists: a table is created if   no table exists. |
| Format | Select the data format to which the table to be created is dedicated:  * TEXTFILE * SEQUENCEFILE * RCFILE * PARQUET * AVRO * KUDU (Note that the Kudu format is only available   when you have installed the R2023-02 Talend Studio Monthly update or a later one delivered by Talend.)  Note that when the file format to be used is PARQUET, you might be prompted to find the specific PARQUET JAR file and install it into Talend Studio.  * When the connection mode to Hive is Embedded, the Job is run in your local machine and calls this JAR   installed in Talend Studio. * When the connection mode to Hive is Standalone, the Job is run in the server hosting Hive and this JAR file   is sent to the HDFS system of the cluster you are connecting to. Therefore, ensure that   you have correctly defined the NameNode URI in the corresponding field of the Basic settings view.  This JAR file can be downloaded from Apache's site. For details about how to install external modules, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
| Set partitions | Select this check box to add partition columns to the table to be created. Once selecting it, you need to define the schema of the partition columns you need to add.  When you select KUDU from the Format drop-down list, you can configure the number of partitions to be created with the Kudu partition parameter. The default value is HASH PARTITIONS 3. For more information, see [Partitioning tables](https://kudu.apache.org/docs/kudu_impala_integration.html#partitioning_tables) from Kudu documentation. |
| Set file location | If you want to create an Impala table in a directory other than the default one, select this check box and enter the directory in HDFS you want to use to hold the table content.  This is typical useful when you need to create an external Impala table by selecting the Create an external table check box in the Advanced settings tab. |
| Use S3 endpoint | The Use S3 endpoint check box is displayed when you have selected the Set file location check box to create an external Impala table.  Once this Use S3 endpoint check box is selected, you need to enter the following parameters in the fields that appear:  * S3 bucket: enter the   name of the bucket in which you need to create the table. * Bucket name: enter the name of the bucket in   which you want to store the dependencies of your Job. This bucket must   already exist on S3. * Temporary resource folder: enter the   directory in which you want to store the dependencies of your Job. For   example, enter temp\_resources to write the dependencies in   the /temp\_resources folder in the bucket. If this folder already exists at runtime, its contents are overwritten   by the upcoming dependencies; otherwise, this folder is automatically   created. * Access key and   Secret key:   enter the authentication information required to connect to the Amazon   S3 bucket to be used.  To enter the password, click the [...] button   next to the password field, enter the password in double quotes in the pop-up dialog box,   and click OK to save the settings.  Note that the format of the S3 file is S3N (S3 Native Filesystem).  Since an Impala table created in S3 is actually an external table, this Use S3 endpoint check box must be used with the Create an external table case being selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Like table | Select this check box and enter the name of the Impala table you want to copy. This allows you to copy the definition of an existing table without copying its data. |
| Create an external table | Select this check box to make the table to be created an external Impala table. This kind of Impala table leaves the raw data where it is if the data is in HDFS.  An external table is usually the better choice for accessing shared data existing in a file system. |
| Table comment | Enter the description you want to use for the table to be created. |
| As select | Select this check box and enter the As select statement for creating an Impala table that is based on a Select statement. |
| Table properties | Add any custom Impala table properties you want to override the default ones used by the Hadoop engine of Talend Studio. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component works standalone. |
