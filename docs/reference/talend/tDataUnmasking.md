<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataunmasking · versión 8.0 -->
# tDataUnmasking

Last updated: 9/30/2026

Unmasks data masked with the tDataMasking component to retrieve the original data.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

The tDataUnmasking component can only
unmask data masked with the tDataMasking component,
using the FF1 with AES or FF1 with SHA-2 method combined with a user-defined
password.

In local mode, Apache Spark 3.0.x and later versions are
supported.

For each column to unmask from the input data, select the unmasking function that
corresponds to the related data masking function in the tDataMasking
component.

The following tables list the corresponding functions for the tDataMasking and
tDataUnmasking components.

Corresponding functions for the character handling category

| Function in tDataMasking | Function in tDataUnmasking |
| --- | --- |
| Replace all | Replace all |
| Replace the first n characters | Replace the first n characters |
| Replace the last n characters | Replace the last n characters |
| Replace characters between two positions | Replace characters between two positions |
| Replace all letters | Replace all letters |
| Replace all digits | Replace all digits |
| Keep the first n digits and replace following ones | Keep the first n digits and replace following ones |
| Keep the last n digits and replace previous ones | Keep the last n digits and replace previous ones |

Corresponding functions for the phone masking and unmasking categories

| Function in tDataMasking | Function in tDataUnmasking |
| --- | --- |
| Mask French phone number | Unmask French phone number |
| Mask German phone number | Unmask German phone number |
| Mask Japanese phone number | Unmask Japanese phone number |
| Mask UK phone number | Unmask UK phone number |
| Mask US phone number | Unmask US phone number |

Corresponding functions for the SSN masking and unmasking categories

| Function in tDataMasking | Function in tDataUnmasking |
| --- | --- |
| Mask French SSN | Unmask French SSN |
| Mask German SSN | Unmask German SSN |
| Mask Japanese SSN | Unmask Japanese SSN |
| Mask UK SSN | Unmask UK SSN |
| Mask US SSN | Unmask US SSN |
| Mask Chinese SSN | Unmask Chinese SSN |
| Mask Indian SSN | Unmask Indian SSN |

Corresponding functions for the bank account masking and unmasking
categories

| Function in tDataMasking | Function in tDataUnmasking |
| --- | --- |
| Mask bank code and account number and keep original country | Unmask bank code and account number and keep original country |
| Mask account number and keep original country and bank code | Unmask account number and keep original country and bank code |

Corresponding functions for the credit card masking and unmasking categories

| Function in tDataMasking | Function in tDataUnmasking |
| --- | --- |
| Mask Credit Card and keep bank | Unmask Credit Card and keep bank |
| Mask Credit Card | Unmask Credit Card |

You must also select the values from the Method and Alphabet lists, and
enter the Extra Parameter set when the input
data was masked using tDataMasking.

### In this section

* [tDataUnmasking Standard properties](/talend/en-US/components/8.0/data-privacy/tdataunmasking-standard-properties)
* [tDataUnmasking properties for Apache Spark Batch](/talend/en-US/components/8.0/data-privacy/tdataunmasking-properties-for-apache-spark-batch)
* [tDataUnmasking properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/data-privacy/tdataunmasking-properties-for-apache-spark-streaming)
* [tDataUnmasking properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/data-privacy/tdataunmasking-properties-for-apache-spark-structured-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataunmasking-properties-for-apache-spark-batch -->
# tDataUnmasking properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDataUnmasking running in the Spark Batch Job framework.

The Spark Batch
tDataUnmasking component belongs to the Data Quality family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The output schema of this component contains one read-only column, *ORIGINAL\_MARK*. This column identifies by true or false if the record is an original record or a substitute record respectively. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Modifications | Define in the table what fields to unmask and how to unmask them:  Input Column: Select the column from the input flow that contains the data to be unmasked.  You can unmask all data masked with tDataMasking using the FF1 with AES or FF1 with SHA-2 method combined with a user-defined password.  These modifications are based on the function you select in the Function column.  Category: select a category of unmasking functions from the list.  Function: Select the function that will unmask data.  The functions you can select from the Function list depend on the data type of the input column.  Method: From this list, select the Format-Preserving Encryption (FPE) algorithm that was used to mask data, FF1 with AES or FF1 with SHA-2:  The FF1 with AES method is based on the Advanced Encryption Standard in CBC mode. The FF1 with SHA-2 method depends on the secure hash function HMAC-256.  Java 8u161 is the minimum required version to use the FF1 with AES method. To be able to use this FPE method with Java versions earlier than 8u161, download the Java Cryptography Extension (JCE) unlimited strength jurisdiction policy files from Oracle website.  To unmask data, the FF1 with AES and FF1 with SHA-2 methods require the password specified in Password or 256-bit key for FF1 methods when the data was masked with the tDataMasking component.  When using the Character handling functions, such as Replace all, Replace characters between two positions, Replace all digits with FPE methods, you must select an alphabet.  From the Alphabet list, select the alphabet used to mask data with the tDataMasking component.  Extra Parameter: This field is used by some of the functions, it will be disabled when not applicable. When applicable, enter a number or a letter to decide the behavior of the function you have selected.  Keep format: this function is only used on Strings. Select this check box to keep the input format when using the Bank Account Unmasking, Credit Card Unmasking, Phone Unmasking and SSN Unmasking categories. That is to say, if there are spaces, dots ('.'), hyphens ('-') or slashes ('/') in the input, those characters are kept in the output. If you select this check box when using Phone Unmasking functions, the characters that are not numbers from the input are copied to the output as is. |

## Advanced settings

| Properties | Description |
| --- | --- |
| FF1 settings | Password or 256-bit key for FF1 methods: To unmask data, the FF1 with AES and FF1 with SHA-2 methods require the password or secret key specified in the Password or 256-bit key for FF1 methods when the data was masked with the tDataMasking component.  Use tweaks: If tweaks have been generated while masking the data, select this check box. When selected, the Column containing tweaks list is displayed. A tweak allows to unmask all data of a record.  Column containing the tweaks: Available when the Use tweaks check box is selected. Select the column that contains the tweaks. If you do not see it, make sure you have declared in the input component the tweaks generated by the masking component.  Key derivation function : Select the same key derivation function as to mask the data. By default, PBKDF2 with 300,000 iterations is selected. |
| Output the original row | Select this check box to output masked data rows in addition to the original data. Having both data rows can be useful in debug or test processes. |
| Null input returns null | This check box is selected by default. When selected, the component outputs null when input values are null.  When cleared, and when the input data is null, the masking function applies:  * The Character Handling functions return the default value depending on   the data type:   + String: Empty output.   + Numeric input: `0`. * The validation functions (Phone Unmasking, Credit Card Unmasking, SSN   Unmasking, and Bank Account Unmasking) cannot validate the value. The   data are sent to the "Invalid" output flow.  From Talend Studio R2024-08 onwards, when Null input returns null is selected and the input data is null, the masking function is not applied, null is returned and the input data are sent to the main flow. |
| Empty input returns an empty output | When this check box is selected, the component returns the input values if they are empty. Otherwise, the selected functions are applied to the input data. |
| Send invalid data to "Invalid" output flow | This check box is selected by default.  * Selected: When the data can be unmasked, they are sent to the   main flow. Otherwise, the data are sent to the "Invalid" output flow. * Cleared: The data are sent to the main flow.  The data are considered invalid when:  * The format of the SSN, phone number or email address is incorrect,   regardless of the Method used. * They do not comply to the [FF1 with AES and   FF1 with SHA-2 methods](/talend/r/en-US/8.0/components/data-privacy/data-masking-functions-in-masking-components). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataunmasking-properties-for-apache-spark-structured-streaming -->
# tDataUnmasking properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tDataUnmasking running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tDataUnmasking component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The output schema of this component contains one read-only column, *ORIGINAL\_MARK*. This column identifies by true or false if the record is an original record or a substitute record respectively. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Modifications | Define in the table what fields to unmask and how to unmask them:  Input Column: Select the column from the input flow that contains the data to be unmasked.  You can unmask all data masked with tDataMasking using the FF1 with AES or FF1 with SHA-2 method combined with a user-defined password.  These modifications are based on the function you select in the Function column.  Category: select a category of unmasking functions from the list.  Function: Select the function that will unmask data.  The functions you can select from the Function list depend on the data type of the input column.  Method: From this list, select the Format-Preserving Encryption (FPE) algorithm that was used to mask data, FF1 with AES or FF1 with SHA-2:  The FF1 with AES method is based on the Advanced Encryption Standard in CBC mode. The FF1 with SHA-2 method depends on the secure hash function HMAC-256.  Java 8u161 is the minimum required version to use the FF1 with AES method. To be able to use this FPE method with Java versions earlier than 8u161, download the Java Cryptography Extension (JCE) unlimited strength jurisdiction policy files from Oracle website.  To unmask data, the FF1 with AES and FF1 with SHA-2 methods require the password specified in Password or 256-bit key for FF1 methods when the data was masked with the tDataMasking component.  When using the Character handling functions, such as Replace all, Replace characters between two positions, Replace all digits with FPE methods, you must select an alphabet.  From the Alphabet list, select the alphabet used to mask data with the tDataMasking component.  Extra Parameter: This field is used by some of the functions, it will be disabled when not applicable. When applicable, enter a number or a letter to decide the behavior of the function you have selected.  Keep format: this function is only used on Strings. Select this check box to keep the input format when using the Bank Account Unmasking, Credit Card Unmasking, Phone Unmasking and SSN Unmasking categories. That is to say, if there are spaces, dots ('.'), hyphens ('-') or slashes ('/') in the input, those characters are kept in the output. If you select this check box when using Phone Unmasking functions, the characters that are not numbers from the input are copied to the output as is. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataunmasking-standard-properties -->
# tDataUnmasking Standard properties

Last updated: 9/30/2026

These properties are used to configure tDataUnmasking running in the Standard Job framework.

The Standard
tDataUnmasking component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The output schema of this component contains one read-only column, *ORIGINAL\_MARK*. This column identifies by true or false if the record is an original record or a substitute record respectively. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Modifications | Define in the table what fields to unmask and how to unmask them:  Input Column: Select the column from the input flow that contains the data to be unmasked.  You can unmask all data masked with tDataMasking using the FF1 with AES or FF1 with SHA-2 method combined with a user-defined password.  These modifications are based on the function you select in the Function column.  Category: select a category of unmasking functions from the list.  Function: Select the function that will unmask data.  The functions you can select from the Function list depend on the data type of the input column.  Method: From this list, select the Format-Preserving Encryption (FPE) algorithm that was used to mask data, FF1 with AES or FF1 with SHA-2:  The FF1 with AES method is based on the Advanced Encryption Standard in CBC mode. The FF1 with SHA-2 method depends on the secure hash function HMAC-256.  Java 8u161 is the minimum required version to use the FF1 with AES method. To be able to use this FPE method with Java versions earlier than 8u161, download the Java Cryptography Extension (JCE) unlimited strength jurisdiction policy files from Oracle website.  To unmask data, the FF1 with AES and FF1 with SHA-2 methods require the password specified in Password or 256-bit key for FF1 methods when the data was masked with the tDataMasking component.  When using the Character handling functions, such as Replace all, Replace characters between two positions, Replace all digits with FPE methods, you must select an alphabet.  From the Alphabet list, select the alphabet used to mask data with the tDataMasking component.  Extra Parameter: This field is used by some of the functions, it will be disabled when not applicable. When applicable, enter a number or a letter to decide the behavior of the function you have selected.  Keep format: this function is only used on Strings. Select this check box to keep the input format when using the Bank Account Unmasking, Credit Card Unmasking, Phone Unmasking and SSN Unmasking categories. That is to say, if there are spaces, dots ('.'), hyphens ('-') or slashes ('/') in the input, those characters are kept in the output. If you select this check box when using Phone Unmasking functions, the characters that are not numbers from the input are copied to the output as is. |

## Advanced settings

| Properties | Description |
| --- | --- |
| FF1 settings | Password or 256-bit key for FF1 methods: To unmask data, the FF1 with AES and FF1 with SHA-2 methods require the password or secret key specified in Password or 256-bit key for FF1 methods when the data was masked with the tDataMasking component.  Use tweaks: If tweaks have been generated while masking the data, select this check box. When selected, the Column containing tweaks list is displayed. A tweak allows to unmask all data of a record.  Column containing the tweaks: Available when the Use tweaks check box is selected. Select the column that contains the tweaks. If you do not see it, make sure you have declared in the input component the tweaks generated by the masking component.  Key derivation function : Select the same key derivation function as to mask the data. By default, PBKDF2 with 300,000 iterations is selected. |
| Output the original row | Select this check box to output masked data rows in addition to the original data. Having both data rows can be useful in debug or test processes. |
| Null input returns null | This check box is selected by default. When selected, the component outputs null when input values are null.  When cleared, and when the input data is null, the masking function applies:  * The Character Handling functions return the default value depending on   the data type:   + String: Empty output.   + Numeric input: `0`. * The validation functions (Phone Unmasking, Credit Card Unmasking, SSN   Unmasking, and Bank Account Unmasking) cannot validate the value. The   data are sent to the "Invalid" output flow.  From Talend Studio R2024-07 onwards, when Null input returns null is selected and the input data is null, the masking function is not applied, null is returned and the input data are sent to the main flow. |
| Empty input returns an empty output | When this check box is selected, the component returns the input values if they are empty. Otherwise, the selected functions are applied to the input data. |
| Send invalid data to "Invalid" output flow | This check box is selected by default.  * Selected: When the data can be unmasked, they are sent to the   main flow. Otherwise, the data are sent to the "Invalid" output flow. * Cleared: The data are sent to the main flow.  The data are considered invalid when:  * The format of the SSN, phone number or email address is incorrect,   regardless of the Method used. * They do not comply to the [FF1 with AES and   FF1 with SHA-2 methods](/talend/r/en-US/8.0/components/data-privacy/data-masking-functions-in-masking-components). |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step. It requires an input and output flows. |
