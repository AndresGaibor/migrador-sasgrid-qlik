<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tpatternunmasking · versión 8.0 -->
# tPatternUnmasking

Last updated: 9/30/2026

Unmasks data masked with the tPatternMasking component to retrieve the original data.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

The tPatternUnmasking component can only
unmask data masked with the tPatternMasking component,
using the FF1 with AES or FF1 with SHA-2 method combined with a user-defined
password.

For each column to unmask from the input data, select the value from the
Field type list, and enter the Values, Path,
Range and Date
Range values set when the input data was masked using tPatternMasking.

In local mode, Apache Spark 3.0.x and later versions are
supported.

### In this section

* [tPatternUnmasking Standard properties](/talend/en-US/components/8.0/data-privacy/tpatternunmasking-standard-properties)
* [tPatternUnmasking properties for Apache Spark Batch](/talend/en-US/components/8.0/data-privacy/tpatternunmasking-properties-for-apache-spark-batch)
* [tPatternUnmasking properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/data-privacy/tpatternunmasking-properties-for-apache-spark-streaming)
* [tPatternUnmasking properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/data-privacy/tpatternunmasking-properties-for-apache-spark-structured-streaming)

**Related tasks**  

* [Unmasking Australian phone numbers](unmasking-australian-phone-numbers "The Job in this scenario uses the tPatternUnmasking component to retrieve the original Australian phone numbers masked with the tPatternMasking component.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tpatternunmasking-properties-for-apache-spark-batch -->
# tPatternUnmasking properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tPatternUnmasking running in the Spark
Batch Job framework.

The Spark Batch
tPatternUnmasking component belongs to the Data Quality family.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The output schema of this component   contains one read-only column, ORIGINAL\_MARK. This column identifies by   true or false if the record is an   masked or and original respectively. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Modifications | Define in the table what fields to unmask and how to unmask them:  Use the same settings for the Field type, Values, Path, Range and Date Range columns as the ones used for masking the input data with the tPatternMasking component.  Column to unmask: Select the column from the input flow that contains the data to be unmasked.  Each column is processed sequentially, meaning that data unmasking operations will be performed on the data from the first column, the second column, and so on.  In a colum, each data field is a fixed length field, except the last data field.  For fixed length fields, each value must contain the same number of characters, for example: `"30001,30002,30003"` or `"FR,EN"`.  In a column, the last Enumeration or Enumeration from file data field is a variable length field.  For variable length fields, each value might not always contain the same number of characters, for example: `"30001,300023,30003"` or `"FR,ENG"`.  Field type: Select the field type the data belongs to.  * Interval: When selected, set a range of   numeric values used for masking purposes in the Range field, using the   following syntax: `"<min>,<max>"`.  The number of unmasked characters from the   input data corresponds to the number of characters of the   maximum value.  For example, `"1,999"` will be interpreted as `"001,999"`, which means that   three characters from the input data will be masked by a   value randomly selected from the defined range of   values. * Enumeration: When selected, enter a   comma-separated list of values to be used for masking data   in the Values field,   using the following syntax: `"value1,value2,value3"`. * Enumeration from file: When   selected, set the path to the CSV file containing a list of   values used for masking data in the Path field. The file must contain one value per   row and each value must be unique. You can select a file on:   + The local system.   + Amazon S3, in local Spark mode or connected to EMR, using     tS3Configuration. S3N and S3A file     systems are supported.   + Azure Blob Storage, in local Spark mode or connected to Azure HDInsight or     Databricks, using tAzureFSConfiguration.   + Azure Data Lake Storage, in local Spark mode or connected to Azure HDInsight,     using tAzureFSConfiguration.   + Google Cloud Storage, in local Spark mode or connected to Dataproc, using     tGSConfiguration.   + HDFS, in local Spark mode or connected to Azure HDInsight, using     tHDFSConfiguration.  Set the file path as follows:   + In local mode:     - Apache Spark 3.1 and earlier: prefix://file path or       file:///file path.     - Apache Spark 3.2 and later: file:///file path.   + In Standalone and Yarn modes: prefix://file path.   + If the file is on a cluster, hdfs://hdpnameservice1/file     path.   + If the file is on Azure Blob Storage and you are connected to Azure HDInsight or     Databricks,     wasbs://<container\_name>@<storage\_account\_name>.blob.core.windows.net/<folder>/<file\_name>"     . * Date pattern   (YYYYMMDD): When selected, set a range of   years in the Date   Range field, using the following syntax:   `"<min_year>,<max_year>"`.  Years can only have four digits, for example:   `"1900,2100"`.  The input dates to be masked must follow the   YYYYMMDD pattern, for example: `20180101`.  For example, if the input date is `20180101` and the value in   the Date Range is   `"1900,2100"`,   19221221 could be the   output date.  In the Values, Path, Range and Date Range, values must be enclosed in double quotes.  When the input data is invalid, meaning that a value does not match the pattern defined in the component, the generated value is null. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Method | From this list, select the Format-Preserving Encryption (FPE) algorithm that was used to mask data, FF1 with AES or FF1 with SHA-2:  The FF1 with AES method is based on the Advanced Encryption Standard in CBC mode. The FF1 with SHA-2 method depends on the secure hash function HMAC-256.  Java 8u161 is the minimum required version to use the FF1 with AES method. To be able to use this FPE method with Java versions earlier than 8u161, download the Java Cryptography Extension (JCE) unlimited strength jurisdiction policy files from Oracle website. |
| FF1 settings | Password or 256-bit key for FF1 methods: To unmask data, the FF1 with AES and FF1 with SHA-2 methods require the password or secret key specified in Password or 256-bit key for FF1 methods when the data was masked with the tPatternMasking component.  Use tweaks: If tweaks have been generated while masking the data, select this check box. When selected, the Column containing tweaks list is displayed. A tweak allows to unmask all data of a record.  Column containing the tweaks: Available when the Use tweaks check box is selected. Select the column that contains the tweaks. If you do not see it, make sure you have declared in the input component the tweaks generated by the masking component.  Key derivation function : Select the same key derivation function as to mask the data. By default, PBKDF2 with 300,000 iterations is selected. |
| Seed for random generator | Set a random number if you want to generate the same sample of substitute data in each execution of the Job. The seed is not set by default.  If you do not set the seed, the component creates a new random seed for each Job execution. Repeating the execution with a different seed will result in a different sample being generated. |
| Encoding | Select the encoding from the list or select Custom and define it manually. If you select Custom and leave the field empty, the supported encodings depend on the JVM that you are using. This field is compulsory for the file encoding. |
| Output the original row | Select this check box to output original data rows in addition to the substitute data. Outputting both the original and substitute data can be useful in debug or test processes. |
| Null input returns null | This check box is selected by default. When selected, the component outputs null when input values are null.  When cleared, and when the input data is null, the input data are sent to the "Invalid" output flow.  From Talend Studio R2024-08 onwards, when Null input returns null is selected and the input data is null, the masking function is not applied, null is returned and the input data are sent to the main flow. |
| Empty input returns an empty output | When this check box is selected, empty values are left unchanged in the output data. Otherwise, the selected functions are applied to the input data. |
| Send invalid data to "Invalid" output flow | This check box is selected by default.  * Selected: When the data can be unmasked, they are sent to the main flow.   Otherwise, the data are sent to the "Invalid" output flow. * Cleared: The data are sent to the main flow.  Invalid data are any values that do not match the pattern. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tpatternunmasking-properties-for-apache-spark-structured-streaming -->
# tPatternUnmasking properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tPatternUnmasking running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tPatternUnmasking component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The output schema of this component contains one   read-only column, ORIGINAL\_MARK. This column identifies by true or false if the record is an masked or and original   respectively. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Modifications | Define in the table what fields to unmask and how to unmask them:  Use the same settings for the Field type, Values, Path, Range and Date Range columns as the ones used for masking the input data with the tPatternMasking component.  Column to unmask: Select the column from the input flow that contains the data to be unmasked.  Each column is processed sequentially, meaning that data unmasking operations will be performed on the data from the first column, the second column, and so on.  In a colum, each data field is a fixed length field, except the last data field.  For fixed length fields, each value must contain the same number of characters, for example: `"30001,30002,30003"` or `"FR,EN"`.  In a column, the last Enumeration or Enumeration from file data field is a variable length field.  For variable length fields, each value might not always contain the same number of characters, for example: `"30001,300023,30003"` or `"FR,ENG"`.  Field type: Select the field type the data belongs to.  * Interval: When selected, set a range of   numeric values used for masking purposes in the Range field, using the   following syntax: `"<min>,<max>"`.  The number of unmasked characters from the   input data corresponds to the number of characters of the   maximum value.  For example, `"1,999"` will be interpreted as `"001,999"`, which means that   three characters from the input data will be masked by a   value randomly selected from the defined range of   values. * Enumeration: When selected, enter a   comma-separated list of values to be used for masking data   in the Values field,   using the following syntax: `"value1,value2,value3"`. * Enumeration from file: When   selected, set the path to the CSV file containing a list of   values used for masking data in the Path field. The file must contain one value per   row and each value must be unique. You can select a file on:   + The local system.   + Amazon S3, in local Spark mode or connected to EMR, using     tS3Configuration. S3N and S3A file     systems are supported.   + Azure Blob Storage, in local Spark mode or connected to Azure HDInsight or     Databricks, using tAzureFSConfiguration.   + Azure Data Lake Storage, in local Spark mode or connected to Azure HDInsight,     using tAzureFSConfiguration.   + Google Cloud Storage, in local Spark mode or connected to Dataproc, using     tGSConfiguration.   + HDFS, in local Spark mode or connected to Azure HDInsight, using     tHDFSConfiguration.  Set the file path as follows:   + In local mode:     - Apache Spark 3.1 and earlier: prefix://file path or       file:///file path.     - Apache Spark 3.2 and later: file:///file path.   + In Standalone and Yarn modes: prefix://file path.   + If the file is on a cluster, hdfs://hdpnameservice1/file     path.   + If the file is on Azure Blob Storage and you are connected to Azure HDInsight or     Databricks,     wasbs://<container\_name>@<storage\_account\_name>.blob.core.windows.net/<folder>/<file\_name>"     . * Date pattern   (YYYYMMDD): When selected, set a range of   years in the Date   Range field, using the following syntax:   `"<min_year>,<max_year>"`.  Years can only have four digits, for example:   `"1900,2100"`.  The input dates to be masked must follow the   YYYYMMDD pattern, for example: `20180101`.  For example, if the input date is `20180101` and the value in   the Date Range is   `"1900,2100"`,   19221221 could be the   output date.  In the Values, Path, Range and Date Range, values must be enclosed in double quotes.  When the input data is invalid, meaning that a value does not match the pattern defined in the component, the generated value is null. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tpatternunmasking-standard-properties -->
# tPatternUnmasking Standard properties

Last updated: 9/30/2026

These properties are used to configure tPatternUnmasking running in the Standard Job framework.

The Standard
tPatternUnmasking component belongs to the Data Quality family.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The output schema of this component   contains one read-only column, ORIGINAL\_MARK. This column identifies by   true or false if the record is an   masked or and original respectively. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Modifications | Define in the table what fields to unmask and how to unmask them:  Use the same settings for the Field type, Values, Path, Range and Date Range columns as the ones used for masking the input data with the tPatternMasking component.  Column to unmask: Select the column from the input flow that contains the data to be unmasked.  Each column is processed sequentially, meaning that data unmasking operations will be performed on the data from the first column, the second column, and so on.  In a colum, each data field is a fixed length field, except the last data field.  For fixed length fields, each value must contain the same number of characters, for example: `"30001,30002,30003"` or `"FR,EN"`.  In a column, the last Enumeration or Enumeration from file data field is a variable length field.  For variable length fields, each value might not always contain the same number of characters, for example: `"30001,300023,30003"` or `"FR,ENG"`.  Field type: Select the field type the data belongs to.  * Interval: When selected, set a range of   numeric values used for masking purposes in the Range field, using the   following syntax: `"<min>,<max>"`.  The number of unmasked characters from the   input data corresponds to the number of characters of the   maximum value.  For example, `"1,999"` will be interpreted as `"001,999"`, which means that   three characters from the input data will be masked by a   value randomly selected from the defined range of   values. * Enumeration: When selected, enter a   comma-separated list of values to be used for masking data   in the Values field,   using the following syntax: `"value1,value2,value3"`. * Enumeration from file: When   selected, set the path to the CSV file containing a list of   values used for masking data in the Path field. The file must contain one value per   row and each value must be unique. * Date pattern   (YYYYMMDD): When selected, set a range of   years in the Date   Range field, using the following syntax:   `"<min_year>,<max_year>"`.  Years can only have four digits, for example:   `"1900,2100"`.  The input dates to be masked must follow the   YYYYMMDD pattern, for example: `20180101`.  For example, if the input date is `20180101` and the value in   the Date Range is   `"1900,2100"`,   19221221 could be the   output date.  In the Values, Path, Range and Date Range, values must be enclosed in double quotes.  When the input data is invalid, meaning that a value does not match the pattern defined in the component, the generated value is null. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Method | From this list, select the Format-Preserving Encryption (FPE) algorithm that was used to mask data, FF1 with AES or FF1 with SHA-2:  The FF1 with AES method is based on the Advanced Encryption Standard in CBC mode. The FF1 with SHA-2 method depends on the secure hash function HMAC-256.  Java 8u161 is the minimum required version to use the FF1 with AES method. To be able to use this FPE method with Java versions earlier than 8u161, download the Java Cryptography Extension (JCE) unlimited strength jurisdiction policy files from Oracle website. |
| FF1 settings | Password or 256-bit key for FF1 methods: To unmask data, the FF1 with AES and FF1 with SHA-2 methods require the password or secret key specified in Password or 256-bit key for FF1 methods when the data was masked with the tPatternMasking component.  Use tweaks: If tweaks have been generated while masking the data, select this check box. When selected, the Column containing tweaks list is displayed. A tweak allows to unmask all data of a record.  Column containing the tweaks: Available when the Use tweaks check box is selected. Select the column that contains the tweaks. If you do not see it, make sure you have declared in the input component the tweaks generated by the masking component.  Key derivation function : Select the same key derivation function as to mask the data. By default, PBKDF2 with 300,000 iterations is selected. |
| Seed for random generator | Set a random number if you want to generate the same sample of substitute data in each execution of the Job. The seed is not set by default.  If you do not set the seed, the component creates a new random seed for each Job execution. Repeating the execution with a different seed will result in a different sample being generated. |
| Encoding | Select the encoding from the list or select Custom and define it manually. If you select Custom and leave the field empty, the supported encodings depend on the JVM that you are using. This field is compulsory for the file encoding. |
| Output the original row | Select this check box to output original data rows in addition to the substitute data. Outputting both the original and substitute data can be useful in debug or test processes. |
| Null input returns null | This check box is selected by default. When selected, the component outputs null when input values are null.  When cleared, and when the input data is null, the input data are sent to the "Invalid" output flow.  From Talend Studio R2024-08 onwards, when Null input returns null is selected and the input data is null, the masking function is not applied, null is returned and the input data are sent to the main flow. |
| Empty input returns an empty output | When this check box is selected, empty values are left unchanged in the output data. Otherwise, the selected functions are applied to the input data. |
| Send invalid data to "Invalid" output flow | This check box is selected by default.  * Selected: When the data can be unmasked, they are sent to the main flow.   Otherwise, the data are sent to the "Invalid" output flow. * Cleared: The data are sent to the main flow.  Invalid data are any values that do not match the pattern. |
| tStat Catcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediary step. It requires an input and output flows. |
