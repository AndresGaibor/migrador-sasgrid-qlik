<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/validation/tschemacompliancecheck · versión 8.0 -->
# tSchemaComplianceCheck

Last updated: 9/30/2026

Ensures the data quality of any source data against a reference data source.

tSchemaComplianceCheck validates all input rows against a
reference schema or check types, nullability, length of rows against reference values.
The validation can be carried out in full or partly.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tSchemaComplianceCheck Standard properties](/talend/en-US/components/8.0/validation/tschemacompliancecheck-standard-properties)
* [tSchemaComplianceCheck for Apache Spark Batch](/talend/en-US/components/8.0/validation/tschemacompliancecheck-for-apache-spark-batch)
* [tSchemaComplianceCheck for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/validation/tschemacompliancecheck-for-apache-spark-streaming)

**Related tasks**  

* [Validating data against schema](validating-data-against-schema "This scenario presents a Job that checks the type, nullability, and length of data from an incoming flow against a defined reference schema, and displays the validation results on the Run console.")
* [Validating data using advanced JSON Schema constraints](validating-data-using-advanced-json-schema-constraints "This scenario presents a Job that validates customer records using JSON Schema constraints (pattern, enumeration, range) and outputs structured violations for records that fail validation.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/validation/tschemacompliancecheck-for-apache-spark-batch -->
# tSchemaComplianceCheck for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tSchemaComplianceCheck running in the Spark Batch Job framework.

The Spark Batch
tSchemaComplianceCheck component belongs to the Data Quality family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Base Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  It describes the structure and nature of your data to be processed as   it is. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Base on default schema | Select this option to carry out all checks on all columns against the base schema. |
| Custom defined | Select this option to carry out particular checks on particular columns. When this option is selected, the Columns table shows. |
| Checked Columns | * In this table, define what checks are to be carried out on which   columns. * Column: Displays the columns   names. * Type: Select the type of data   each column is supposed to contain. This validation is mandatory for   all columns. * Date pattern: Define the expected   date format for each column with the data type of   *Date*. * Nullable: Select the check box in   an individual column to define the column to be nullable, that is,   to allow empty rows in this column to go to the output flow   regardless of the base schema definition. To define all columns to   be nullable, select the check box in the table header. * Max length: Select the check box   in an individual column to verify the data length of the column   against the length definition of the base schema. To carry out this   verification on all the columns, select the check box in the table   header. |
| Use another schema for compliance check | Define a reference schema as you expect the data to be, in order to reject the non-compliant data.  It can be restrictive on data type, null values, and/or length. |
| Discard the excess content of column when the actual length is greater than the declared length | With any of the three modes of tSchemaComplianceCheck, select this check box to truncate the data that exceeds the length specified rather than reject it.  Information noteNote: This option is applicable only on data of String type. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Ignore TimeZone when Check Date | Select this check box to ignore the time zone setup upon date check.  Not available when the Check all columns from schema mode is selected. |
| Treat all empty string as NULL | Select this check box to treat any empty fields in any columns as null values, instead of empty strings.  By default, this check box is selected. When it is cleared, the Choose Column(s) table shows to let you select individual columns. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/validation/tschemacompliancecheck-standard-properties -->
# tSchemaComplianceCheck Standard properties

Last updated: 9/30/2026

These properties are used to configure tSchemaComplianceCheck running in the Standard Job framework.

The Standard
tSchemaComplianceCheck component belongs to the Data Quality family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Base Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  It describes the structure and nature of your data to be processed as it is. Used by both Basic Checks and Advanced JSON Schema modes.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs. |
| Check all columns from schema | Select this option to carry out all checks on all columns against the base schema. |
| Custom defined | Select this option to carry out particular checks on particular columns. When this option is selected, the Checked Columns table shows. |
| Checked Columns | In this table, define what checks are to be carried out on which columns. This table appears when you select the Custom defined option.  * Column: Displays the columns   names. * Type: Select the type of data each   column is supposed to contain. This validation is mandatory for all   columns. * Date pattern: Define the expected   date format for each column with the data type of *Date*. * Nullable: Select the checkbox in   an individual column to define the column to be nullable, that is, to   allow empty rows in this column to go to the output flow regardless of   the base schema definition. To define all columns to be nullable, select   the checkbox in the table header. * Max length: Select the checkbox in   an individual column to verify the data length of the column against the   length definition of the base schema. To carry out this verification on   all the columns, select the checkbox in the table header. |
| Use another schema for compliance check | In order to reject the non-compliant data, define a reference schema as you expect the data to be.  It can be restrictive on data type, null values, and length. |
| Check columns from a JSON schema URI | This option is available from Talend Studio 8.0 R2026-05 onwards. Select this option to validate the data against a JSON schema. Enter the JSON schema URI in double quotes. |
| Trim the excess content of column when length checking chosen and the length is greater than defined length | Select this checkbox to truncate the data that exceeds the length specified rather than reject it.  Information noteRestriction: This option is applicable only on data of String type.  This option is not available when Check columns from a JSON schema URI is selected. |

## Advanced settings

The advanced settings depends on the Mode selected in the
Basic settings.

This table describes the advanced settings when Check columns from a
JSON schema URI is selected

| Properties | Description |
| --- | --- |
| Set JSON schema draft version when it's not defined in the schema file | Starting with the 8.0.1-R2026-08 Talend Studio monthly, the component automatically detects the draft version from the $schema declaration in the JSON schema when the declaration is available and supported. Select the checkbox to use the JSON schema draft version dropdown list when $schema is missing or empty, or when its value is unsupported. Existing Jobs without a $schema declaration continue to use the selected draft version.  For more information, see [json-schema.org](https://json-schema.org/specification). |
| JSON schema file encoding | Select the encoding of the schema file. |

This table describes the advanced settings when Check columns from a
JSON schema URI is not selected

| Properties | Description |
| --- | --- |
| Use Fastest Date Check | Select this checkbox to perform a fast date format check using the *TalendDate.isDate()* method of the *Talend Date* system routine if *Date pattern* is not defined. For more information about routines, see [What are routines](/talend/r/en-US/8.0/studio-user-guide/what-are-routines). |
| Use Strict Data Check | Select this checkbox to perform a strict data format check. When selected, the Use Fastest Data Check checkbox is hidden. |
| Ignore TimeZone when Check Date | Select this checkbox to ignore the time zone setup upon date check.  This option is not available when Check all columns from schema is selected. |
| Treat all empty string as NULL | Select this checkbox to treat any empty fields in any columns as null values, instead of empty strings.  By default, this checkbox is selected. When it is cleared, the Choose Column(s) table shows to let you select individual columns. |
| Check string by byte length | Select this checkbox to check the string column with byte length according to the charset set in the Charset text box.  By default, this checkbox is not selected and only character length is checked. |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Schema violations output

When Check columns from a JSON schema URI is selected, the
component validates data against a JSON schema with advanced constraints, invalid rows
are sent to the Rejects flow with structured violation metadata.

| Information | Description |
| --- | --- |
| All input columns | Pass-through from input. All input column values are preserved unchanged in the Rejects flow. |
| ErrorType | Type of the error. |
| ErrorCode | Code identifying the type of schema violation encountered. |
| ErrorMessage | Error message summarizing the violation. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediary step in the flow allowing to exclude from the main flow the non-compliant data. This component cannot be a start component as it requires an input flow. It also requires at least one output component to gather the validated flow, and possibly a second output component for rejected data using Rejects link. For more information, see [Rejects](/talend/r/en-US/8.0/studio-user-guide/rejects). |
