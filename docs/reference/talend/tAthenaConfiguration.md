<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-athena/tathenaconfiguration · versión 8.0 -->
# tAthenaConfiguration

Last updated: 9/30/2026

Defines the AWS Athena connection settings that other Athena components reuse in
the same Job.

tAthenaConfiguration is a shared connection component. Configure
tAthenaInput to reference this component through the
Connection property.

You can use multiple tAthenaConfiguration components in the same Job
to connect to different Athena environments or work groups.

### In this section

* [tAthenaConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/amazon-athena/tathenaconfiguration-properties-for-apache-spark-batch)

**Related tasks**  

* [Accessing Qlik Open Lakehouse via Amazon Athena](tathenaconfiguration-tathenainput-tlogrow-accessing-qlik-open-lakehouse-via-amazon-athena-standard-component "This Job uses Athena components to query Qlik Open Lakehouse data and display the result in Talend Studio. The same data can be viewed in your AWS tools, such as AWS Glue.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-athena/tathenaconfiguration-properties-for-apache-spark-batch -->
# tAthenaConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tAthenaConfiguration
running in the Spark Batch Job framework.

The Spark Batch
tAthenaConfiguration component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

The AWS account must have permissions to run Athena queries and write query results to the specified S3 output location.

## Basic settings

| Properties | Description |
| --- | --- |
| Region | Select the AWS Region for the Athena service endpoint. The default region is US East (N. Virginia) (us-east-1). |
| Catalog Name | Enter the AWS Glue Data Catalog name or federated catalog name to query. The value defaults to myCatalog. |
| Database Name | Enter the Athena (Glue) database name in the selected catalog. The value defaults to default. |
| S3 Output Location | Enter the Amazon S3 path for Athena query results, for example, `s3://my-bucket/athena-results/`. The AWS principal must have s3:PutObject and s3:GetBucketLocation permissions on this path. |
| Access Key ID | Enter the AWS IAM access key ID for authentication. Leave empty to use the default AWS credential provider chain, such as environment variables or instance profile credentials. |
| Secret Access Key | Enter the AWS IAM secret access key paired with the Access Key ID. The value is stored and transmitted in encrypted form. |
| Session Token | Enter the temporary session token for short-lived AWS STS credentials, for example, AssumeRole. Leave empty for long-lived IAM users. The value is stored and transmitted in encrypted form. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tAthenaConfiguration cannot start or terminate a subJob on its own and has no flow output component. In the tAthenaInput component, select the tAthenaConfiguration component to use from the Connection property.  Only OnSubjobOk and OnSubjobError trigger links are supported.  No data flow components are supported.  This component requires a tSparkConfiguration component in the same Job. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-athena/tathenaconfiguration-tathenainput-tlogrow-accessing-qlik-open-lakehouse-via-amazon-athena-standard-component -->
# Accessing Qlik Open Lakehouse via Amazon Athena

Last updated: 9/30/2026

This Job uses Athena components to query Qlik Open
Lakehouse data and display the result in Talend Studio. The same
data can be viewed in your AWS tools, such as AWS Glue.

## Before you begin

Confirm that your AWS account can run Athena queries and write to your configured S3 output path.

Confirm that your Open Lakehouse environment exposes a view (named
`prices` in this scenario) in the selected catalog and
database.

For Athena component prerequisites, read [Amazon Athena component documentation](https://help.qlik.com/talend/en-US/components/8.0/amazon-athena/amazon-athena-component).

## Linking the components

### Procedure

1. From the Palette, drag tAthenaConfiguration, tAthenaInput, and tLogRow to the workspace.
2. From tAthenaConfiguration to tAthenaInput, create a Trigger > OnSubjobOk link.
3. From tAthenaInput to tLogRow, create a Row > Main link.

## Configuring the components

### Procedure

1. Double-click tAthenaConfiguration to open the Component view.
2. In Basic settings, configure
   Region, AWS Catalog Name, and
   Database Name.
3. In Basic settings, configure
   S3 Output Location, for example,
   s3://<my-bucket>/aws-athena-results/.
4. Enter the S3 credentials to authenticate to your AWS account in the
   Access Key ID and Secret Access
   Key fields.
5. Double-click tAthenaInput to open the Component view.
6. In Basic settings, set Connection to the configured tAthenaConfiguration component.
7. In Query, enter the SQL statement `SELECT *
   FROM prices` to retrieve all data from the view named
   prices.
8. Double-click tLogRow to open the Component view.
9. In Basic settings, click Sync columns and select Basic mode.

## Executing the Job

### Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

### Results

The Run view displays rows returned by the Athena query
against the Qlik
Open Lakehouse view.

In this flow, tAthenaConfiguration defines the Athena
endpoint, catalog, database, and S3 result location. tAthenaInput
reuses that configuration to run SQL on the Open Lakehouse view and return the
result set to tLogRow in the same Job.

This pattern lets teams validate Open Lakehouse data quickly by using the same SQL
access path in both Talend Studio and AWS tools.

Validate the same result set in your AWS tools, such as AWS Glue, for cross-checking.

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tAthenaConfiguration](/talend/en-US/components/8.0/amazon-athena/tathenaconfiguration)
* [tAthenaInput](/talend/en-US/components/8.0/amazon-athena/tathenainput)
