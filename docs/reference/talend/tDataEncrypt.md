<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataencrypt · versión 8.0 -->
# tDataEncrypt

Last updated: 9/30/2026

Protects data by transforming it into unreadable cipher text.

Information noteImportant: The minimum required Java version for this component is Java
8u161.

Encrypting the cipher text and reading the original data require either:

* A user-defined password and a cryptographic file.
* A 256-bit secret key encoded with base64.

  You can get the 256-bit key using:
  + Online tools
  + OpenSSL: openssl rand -base64 32

To decrypt the data, you will need the secret key or the password with the
cryptographic file.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## Why encrypting data?

Encryption is used to protect your assets, your organization, or customers' sensitive data. Encryption can protect data from internal or external leakage.

In big data environments, large volumes of data from many sources are collected,
manipulated, and stored in various formats. Encryption helps reduce the risk of
sensitive data exposure.

Encryption is also recommended or required for compliance with data protection laws.

## Considerations for data encryption

* Define the type of the data to be protected: data in transit or
  data at rest.
* Identify the scope of the data to be protected: purpose,
  ownership, access, etc.
* Provide strong passwords for the cryptographic file.
* Do not reuse passwords for different data encryption
  operations.
* Store passwords in a secure password management system.
* Store the secret key in a secure system.
* Make sure only authorized users get access to the password and
  the cryptographic file necessary to decrypt back data.
* Strong encryption methods generally increase required
  resources.
* Separate the cryptographic file from the encrypted data to keep
  your data secure.
* It is advised to use different cryptographic files to encrypt
  different datasets.
* Data encryption is not a complete security approach. Combining
  different security layers help address concerns about sensitive data. Security
  layers include vulnerability assessment and management or anti-malware
  solutions.

## Data encryption methods

The tDataEncrypt component encrypts data using the AES-GCM and Blowfish encryption methods:

| AES-256 | Blowfish |
| --- | --- |
| GCM mode of operation | CBC mode of operation |
| Uses a randomly generated 256-bit key | Uses a randomly generated 256-bit key |
| Integrity check | No integrity check |
| Faster on modern CPUs | Computationally faster |
| Patented | Unpatented |
| Standardized by the National Institute of Standards and Technology (NIST) | - |
| Used by SSL/TLS | - |

## The data encryption process

When you use a cryptographic file, the data encryption process includes the following steps:

1. Generating the cryptographic file. It contains:
   * A randomly generated salt used to derive a cryptographic key from the
     user-defined password using the PBKDF2 key derivation function.
   * A randomly generated 256-bit key encrypted with AES and the user-defined
     password.
   * The encryption method encrypted with AES and the user-defined
     password.
2. Accessing the encrypted data from the cryptographic file by:
   1. Using the randomly generated salt to derive the cryptographic key from the
      user-defined password.
   2. Using the cryptographic key and the AES method to decrypt the randomly
      generated 256-bit key and the encryption method.

   During the decryption, if the password is correct, the component can access the
   encryption method and the randomly generated 256-bit key. Otherwise, the access
   is denied.
3. Encrypting the data using:
   * The randomly generated 256-bit key from the cryptographic file
   * The encryption method
   * A random initialization vector (IV) generated for each data

### In this section

* [tDataEncrypt Standard properties](/talend/en-US/components/8.0/data-privacy/tdataencrypt-standard-properties)
* [tDataEncrypt properties for Apache Spark Batch](/talend/en-US/components/8.0/data-privacy/tdataencrypt-properties-for-apache-spark-batch)
* [tDataEncrypt properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/data-privacy/tdataencrypt-properties-for-apache-spark-streaming)
* [tDataEncrypt properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/data-privacy/tdataencrypt-properties-for-apache-spark-structured-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataencrypt-properties-for-apache-spark-batch -->
# tDataEncrypt properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDataEncrypt running in the Spark Batch Job framework.

The Standard
tDataEncrypt component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Secret method | Select a secret method:  * Cryptographic file * 256-bit key (encoded with base64) You can get the 256-bit key using:   + Online tools   + OpenSSL: openssl rand -base64 32 |
| Password | Available when Cryptographic file is selected as secret method.  This value must be enclosed in double quotes.  When using an existing cryptographic file, enter the password required to use this file.  When generating a cryptographic file, enter the password used to encrypt this file.  This password is required to decrypt back data using the tDataDecrypt component. |
| Cryptographic file path | Available when Cryptographic file is selected as secret method.  When using an existing cryptographic file, enter the path to the cryptographic file. It must be enclosed in double quotes.  When generating a cryptographic file, enter the destination file path. You can enter different types of values:  * A context: `context.mycontext` * To generate the file in local, enclose the path in double quotes:   `"C:/user/cryptofiles/mycryptofile"` * To generate the file on a cluster, enclose the HDFS path in double   quotes:   `"hdfs://repository/cryptofiles/mycryptofile"`  This cryptographic file is encrypted using AES-GCM.  This cryptographic file is required to decrypt back data using the tDataDecrypt component.  For more information about the cryptographic file, see the [data encryption process](tdataencrypt). |
| Generate cryptographic file | Available when Cryptographic file is selected as secret method.  Click this button to generate the cryptographic file.  In the dialog box, select the cryptographic method used to encrypt the input data:  * AES, which is a 128-bit block cipher standardized by   the National Institute of Standards and Technology (NIST). * Blowfish, which is a 64-bit unpatented block cipher   developed by Bruce Schneier. |
| Secret key | Available when 256-bit key (encoded with base64) is selected as secret method.  This value must be enclosed in double quotes.  This key is required to decrypt back data using the tDataDecrypt component. |
| Cryptographic method | Available when 256-bit key (encoded with base64) is selected as secret method.  Select the cryptographic method:  * AES, which is a 128-bit block cipher standardized by   the National Institute of Standards and Technology (NIST). * Blowfish, which is a 64-bit unpatented block cipher   developed by Bruce Schneier. |
| Columns to encrypt | Select the corresponding Encrypt check boxes to encrypt input columns.  You can encrypt all column data types, except `Dynamic`, but the output encrypted data is of `String` type.  Configure the output schema of the component to set the type of the columns to be encrypted to `String`.When the input data type is `Dynamic` or `String`, the output column is automatically set to `Dynamic` or `String` respectively.  The columns that are not selected will not be encrypted and be returned as-is by the component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Key derivation function | Select the key derivation function. Jobs created from Talend Studio 8.0 R2022-04 run using PBKDF2 with 300,000 iterations. When you import a Job prior to Talend Studio 8.0 R2022-04, you can run the Job using 300,000 iterations. The results will be different than using 65,536 iterations. |
| tStat Catcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataencrypt-properties-for-apache-spark-structured-streaming -->
# tDataEncrypt properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tDataEncrypt running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tDataEncrypt component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Secret method | Select a secret method:  * Cryptographic file * 256-bit key (encoded with base64) You can get the 256-bit key using:   + Online tools   + OpenSSL: openssl rand -base64 32 |
| Password | Available when Cryptographic file is selected as secret method.  This value must be enclosed in double quotes.  When using an existing cryptographic file, enter the password required to use this file.  When generating a cryptographic file, enter the password used to encrypt this file.  This password is required to decrypt back data using the tDataDecrypt component. |
| Cryptographic file path | Available when Cryptographic file is selected as secret method.  When using an existing cryptographic file, enter the path to the cryptographic file. It must be enclosed in double quotes.  When generating a cryptographic file, enter the destination file path. This must be a local file path. You can enter two types of values:  * A context: `context.mycontext` * A file path enclosed in double quotes: `"C:/user/cryptofiles/mycryptofile"`  This cryptographic file is encrypted using AES-GCM.  This cryptographic file is required to decrypt back data using the tDataDecrypt component.  For more information about the cryptographic file, see the [data encryption process](tdataencrypt). |
| Generate cryptographic file | Available when Cryptographic file is selected as secret method.  Click this button to generate the cryptographic file.  In the dialog box, select the cryptographic method used to encrypt the input data:  * AES, which is a 128-bit block cipher standardized by   the National Institute of Standards and Technology (NIST). * Blowfish, which is a 64-bit unpatented block cipher   developed by Bruce Schneier. |
| Secret key | Available when 256-bit key (encoded with base64) is selected as secret method.  This value must be enclosed in double quotes.  This key is required to decrypt back data using the tDataDecrypt component. |
| Cryptographic method | Available when 256-bit key (encoded with base64) is selected as secret method.  Select the cryptographic method:  * AES, which is a 128-bit block cipher standardized by   the National Institute of Standards and Technology (NIST). * Blowfish, which is a 64-bit unpatented block cipher   developed by Bruce Schneier. |
| Columns to encrypt | Select the corresponding Encrypt check boxes to encrypt input columns.  You can encrypt all column data types, except `Dynamic`, but the output encrypted data is of `String` type.  Configure the output schema of the component to set the type of the columns to be encrypted to `String`.When the input data type is `Dynamic` or `String`, the output column is automatically set to `Dynamic` or `String` respectively.  The columns that are not selected will not be encrypted and be returned as-is by the component. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tdataencrypt-standard-properties -->
# tDataEncrypt Standard properties

Last updated: 9/30/2026

These properties are used to configure tDataEncrypt running in the Standard Job framework.

The Standard
tDataEncrypt component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Secret method | Select a secret method:  * Cryptographic file * 256-bit key (encoded with base64) You can get the 256-bit key using:   + Online tools   + OpenSSL: openssl rand -base64 32 |
| Password | Available when Cryptographic file is selected as secret method.  This value must be enclosed in double quotes.  When using an existing cryptographic file, enter the password required to use this file.  When generating a cryptographic file, enter the password used to encrypt this file.  This password is required to decrypt back data using the tDataDecrypt component. |
| Cryptographic file path | Available when Cryptographic file is selected as secret method.  When using an existing cryptographic file, enter the path to the cryptographic file. It must be enclosed in double quotes.  When generating a cryptographic file, enter the destination file path. You can enter two types of values:  * A context: `context.mycontext` * A file path enclosed in double quotes:   `"C:/user/cryptofiles/mycryptofile"`  This cryptographic file is encrypted using AES-GCM.  This cryptographic file is required to decrypt back data using the tDataDecrypt component.  For more information about the cryptographic file, see the [data encryption process](tdataencrypt). |
| Generate cryptographic file | Available when Cryptographic file is selected as secret method.  Click this button to generate the cryptographic file.  In the dialog box, select the cryptographic method used to encrypt the input data:  * AES, which is a 128-bit block cipher standardized by   the National Institute of Standards and Technology (NIST). * Blowfish, which is a 64-bit unpatented block cipher   developed by Bruce Schneier. |
| Secret key | Available when 256-bit key (encoded with base64) is selected as secret method.  This value must be enclosed in double quotes.  This key is required to decrypt back data using the tDataDecrypt component. |
| Cryptographic method | Available when 256-bit key (encoded with base64) is selected as secret method.  Select the cryptographic method:  * AES, which is a 128-bit block cipher standardized by   the National Institute of Standards and Technology (NIST). * Blowfish, which is a 64-bit unpatented block cipher   developed by Bruce Schneier. |
| Columns to encrypt | Select the corresponding Encrypt check boxes to encrypt input columns.  You can encrypt all column data types but the output encrypted data is of string type. `Dynamic` data type is only supported when it is the last row and when it comes from the input component. If you add it to the schema of tDataEncrypt, it is not supported. For more information, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  Configure the output schema of the component to set the type of the columns to be encrypted to `String`.When the input data type is `Dynamic` or `String`, the output column is automatically set to `Dynamic` or `String` respectively. When the input data type is `Dynamic` or `String`, the output column is automatically set to `Dynamic` or `String` respectively. When the input data is a null value, it will not be encrypted.  The columns that are not selected will not be encrypted and be returned as-is by the component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Key derivation function | Select the key derivation function. Jobs created from Talend Studio 8.0 R2022-04 run using PBKDF2 with 300,000 iterations. When you import a Job prior to Talend Studio 8.0 R2022-04, you can run the Job using 300,000 iterations. The results will be different than using 65,536 iterations. |
| tStat Catcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |
