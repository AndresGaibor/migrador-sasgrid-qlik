<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/matching-with-machine-learning/tmatchpairing · versión 8.0 -->
# tMatchPairing

Last updated: 9/30/2026

Enables you to compute pairs of suspect duplicates from any source data including
large volumes in the context of machine learning on Spark.

This component reads a data set row by row, excludes unique rows and exact
duplicates in separate files, computes pairs of suspect records based on a blocking key
definition and creates a sample of suspect records representative of the data set.

You can label suspect pairs manually or load them into a Grouping campaign which is already defined in Talend Data Stewardship.

In local mode, Apache Spark 2.4.0 and later versions are supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMatchPairing properties for Apache Spark Batch

These properties are used to configure tMatchPairing running in the Spark Batch Job framework.

The Spark Batch
tMatchPairing component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. The output schema of this component has read-only columns   in its output links:  PAIR\_ID and   SCORE: used only with the Pairs and Pairs sample output links. The first column holds the   identifiers of the suspect pairs, and the second holds the similarities   between the records in each pair.  LABEL: used only with the *Pairs sample* output link. You must fill in this   column manually in the Job using the tMatchModel component.  COUNT: used only with the *Exact duplicates* output link. This column gives   the occurrences of the records which exactly match. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Blocking key | Select the columns with which you want to construct the blocking key.  This blocking key is used to generate suffixes which are used to group records. |
| Suffix array blocking parameters | Min suffix length: Set the minimum suffix length you want to reach or stop at in each group.  Max block size: Set the maximum number of the records you want to have in each block. This helps in filtering in large blocks where the suffix is too common, as with *tion* and *ing* for example. |
| Pairing model location | Folder: Set the path to the local folder where you want to generate the model files.  If you want to store the model in a specific file system, for example S3 or HDFS, you must use the corresponding component in the Job and select the Define a storage configuration component check box in the component basic settings.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Integration with Data Stewardship | Select this check box to set the connection parameters to the Talend Data Stewardship server.  If you select this check box, tMatchPairing loads the suspect pairs into a Grouping campaign, which means this component is used as an end component. |
| Data Stewardship Configuration | * URL:  Enter the address to access the Talend Data Stewardship server suffixed with   */data-stewardship/*, for example   `http://<server_address>:19999/data-stewardship/`. * If you are working with Talend Cloud Data Stewardship, use the URL for the   corresponding data center suffixed with */data-stewardship/* to access the   application, for example, `https://tds.us.cloud.talend.com/data-stewardship` for the AWS US   data center.  For the URLs of available data   centers, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). * Username and   Password:  Enter the authentication information to log in to Talend Data Stewardship.  If you are working with Talend Cloud Data Stewardship and if:   + SSO is enabled, enter an access     token in the field.   + SSO is not enabled, enter either     an access token or your password in the field. * Campaign:  Displays the technical name of the campaign once it is selected   in the basic settings. However, you can modify the field value to replace it with a   context parameter for example and pass context variables to the Job at runtime. This   technical name is always used to identify a campaign when the Job communicates with   Talend Data Stewardship whatever is the value in the Campaign   field.  Click Find a Campaign to open a dialog box   which lists the grouping campaigns on the server for which you   are the Campaign owner or you have the   access rights.  Click the refresh button to retrieve the campaign details from   the    Talend Data Stewardship    server. * Assignee:  Specify the campaign participant whose tasks you want to   create. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Filtering threshold | Enter a value between 0.2 and 0.85 to filter the pairs of suspect records based on the calculated scores. This value helps to exclude the pairs which are not very similar.  0.3 is the default value. The higher the value is, the more similar the records will be. |
| Pairs sample | Number of pairs: Enter a size for the sample of the suspect pairs you want to generate. The default value is set to 10000.  Set a random seed: Select this check box and in the Seed field that is displayed, enter a random number if you want to have the same pairs sample in different executions of the Job. Repeating the execution with a different value for the seed will result in different pairs samples and the scores of the pairs could be different as well depending whether the total number of the suspect pairs is greater than 10 000 or not. |
| Data Stewardship Configuration | Campaign ID:  Displays the technical name of the campaign once it is selected in the basic settings. However, you can modify the field value to replace it with a context parameter for example and pass context variables to the Job at runtime. This technical name is always used to identify a campaign when the Job communicates with Talend Data Stewardship whatever is the value in the Campaign field.  Max tasks per commit: Set the number of lines you want to have in each commit.  Do not change the default value unless you are facing performance issues. Increasing the commit size can improve the performance but setting a too high value could cause Job failures. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job. |
| Spark Batch Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/matching-with-machine-learning/tmatchpairing-matching-on-spark-spark-batch-component -->
# Matching on Spark

Last updated: 9/30/2026

Matching on Spark applies only to a subscription-based Talend Platform
solution with Big data or Talend Data Fabric.

Using Talend Studio, you can match very high volume of data using machine learning on
Spark. This feature helps you to match very big number of records with a minimal human
intervention.

Machine learning with Spark is usually two phases: the first phase computes
a model (i.e. teaches the machine) based on historical data and mathematical heuristics,
and the second phase applies the model on new data. In Talend Studio, the
first phase is implemented by two Jobs, one with the tMatchPairing component and the second with the tMatchModel component. While the second phase is implemented by a third Job
with the tMatchPredict component.

Two workflows are possible when matching on Spark with Talend Studio.

In the first workflow, tMatchPairing:

* Computes pairs of suspect records based on a blocking key
  definition.
* Creates a sample of suspect records representative of the
  dataset.
* Can optionally write this sample of suspect records into a Grouping campaign
  defined on the Talend Data Stewardship
  server.
* Separates unique records from exact match records.
* Generates a pairing model to be used with tMatchPredict.

You can then manually label the sample suspect records by resolving tasks
in a Grouping campaign defined on the Talend Data Stewardship server, which is the
recommended method, or by editing the files manually.

Next, you can use the sample suspect records you labeled with tMatchModel in the second Job where tMatchModel:

* Computes similarities between the records in each suspect
  pair,
* Trains a classification model based on the Random Forest
  algorithm.

tMatchPredict labels suspect records automatically
and groups suspect records which match the labels set in the component properties.

While in the second workflow, tMatchPredict uses directly on the new dataset the pairing model generated
by tMatchPairing and the matching model generated by
tMatchModel, and:

* Labels suspect records automatically.
* Groups suspect records which match the labels set in the component
  properties.
* Separates the exact duplicates from unique records.
