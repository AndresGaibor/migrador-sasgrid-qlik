<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail · versión 8.0 -->
# tVerifyEmail

Last updated: 9/30/2026

Verifies if email addresses comply with specific rules and corrects addresses that do not match the rules by using the content from specific columns.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tVerifyEmail Standard properties](/talend/en-US/components/8.0/email-validation/tverifyemail-standard-properties)
* [tVerifyEmail properties for Apache Spark Batch](/talend/en-US/components/8.0/email-validation/tverifyemail-properties-for-apache-spark-batch)
* [tVerifyEmail properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/email-validation/tverifyemail-properties-for-apache-spark-streaming)
* [tVerifyEmail properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/email-validation/tverifyemail-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Verifying email addresses against column content and domain names](tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-verifying-email-addresses-against-column-content-and-domain-names-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-properties-for-apache-spark-batch -->
# tVerifyEmail properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tVerifyEmail running in the Spark Batch Job framework.

The Spark Batch
tVerifyEmail component belongs to the Data Quality family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.  The output schema of tVerifyEmail has different read-only columns depending on the options you select in the component Basic settings view. Read-only output columns include:  VerificationLevel: provides you with the verification status of the processed email addresses as the following:  -*VALID*: means that the email address comply with the defined rule.  -*INVALID*: means that the email address does not comply with the defined rule.  -*CORRECTED*: means that the input email does not comply with the defined rule and has been corrected by using the content of the selected columns. This column is available only when you select the Use column content option in the LOCAL Part Options section.  -*VERIFIED*: means that the email address does exist at the domain. This column is available only when you select the Check with mail server callback option.  -*REJECTED*: means that the email address does not exist at the domain. This column is available only when you select the Check with mail server callback option.  Suggested\_Email: provides you with a suggested content for the email part before the @ sign. The email string is built up from the columns you select from the Use column content view. |
| Column to validate | Select from the list the column you want to validate with tVerifyEmail. |
| Check the entire email with regular expression | Select this check box if you want to match the complete email address against a specific regular expression.  Complete regular expression: enter the regular expression against which you want to match email addresses.  This match is done as a first step to optimize the matching process and exclude addresses that have problems before going any further to match the local and domain parts of email addresses. |
| LOCAL Part Options | Fields in this section will vary according to what option you select. "LOCAL part" in an email address refers to the string before the @ sign.  -Use regular expression: enter in the Pattern field the expression against which you want to check the local part of the email address.  -Use simplified pattern: enter in the Pattern field the simplified pattern against which you want to check the local part of the email address. Select the Show syntax of simplified pattern option to display the syntax to use for simplified patterns. For more information about the syntax, see [Simplified pattern syntax for tVerifyEmail](/talend/r/en-US/8.0/components/email-validation/simplified-pattern-syntax-for-tverifyemail).  -Use column content: use the fields in this view to decide the content against which you want to check the local part of the email. If the local part does not match what you have defined, it will be rewritten by using the content of the fields.  -Enable case-sensitive pattern matching: select this check box to enable a case sensitive pattern matching of the local part of email addresses. You can use case sensitive pattern matching with each of the above options. |
| DOMAIN Part Options | Fields in this view will vary according to what option you select.  -Check the Top-level Domains and the following ones: select this check box to verify the part of the email address which follows the last dot. You can use the Additional Top-level Domains table to add additional top-level domains against which you want to validate email addresses.  -Check domains with a black list: select this option to verify the domains you define in the Domain list table as black listed.  -Check domains with a white list: select this option to verify the domains you define in the Domain List table as white listed. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-properties-for-apache-spark-structured-streaming -->
# tVerifyEmail properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tVerifyEmail running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tVerifyEmail component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.  The output schema of tVerifyEmail has different read-only columns depending on the options you select in the component Basic settings view. Read-only output columns include:  VerificationLevel: provides you with the verification status of the processed email addresses as the following:  -*VALID*: means that the email address comply with the defined rule.  -*VALID*: means that the email address comply with the defined rule.  -*INVALID*: means that the email address does not comply with the defined rule.  -*INVALID*: means that the email address does not comply with the defined rule.  -*CORRECTED*: means that the input email does not comply with the defined rule and has been corrected by using the content of the selected columns. This column is available only when you select the Use column content option in the LOCAL Part Options section.  -*VERIFIED*: means that the email address does exist at the domain. This column is available only when you select the Check with mail server callback option.  -*REJECTED*: means that the email address does not exist at the domain. This column is available only when you select the Check with mail server callback option.  Suggested\_Email: provides you with a suggested content for the email part before the @ sign. The email string is built up from the columns you select from the Use column content view. |
| Column to validate | Select from the list the column you want to validate with tVerifyEmail. |
| Check the entire email with regular expression | Select this check box if you want to match the complete email address against a specific regular expression.  Complete regular expression: enter the regular expression against which you want to match email addresses.  This match is done as a first step to optimize the matching process and exclude addresses that have problems before going any further to match the local and domain parts of email addresses. |
| LOCAL Part Options | Fields in this section will vary according to what option you select. "LOCAL part" in an email address refers to the string before the @ sign.  -Use regular expression: enter in the Pattern field the expression against which you want to check the local part of the email address.  -Use simplified pattern: enter in the Pattern field the simplified pattern against which you want to check the local part of the email address. Select the Show syntax of simplified pattern option to display the syntax to use for simplified patterns. For more information about the syntax, see [Simplified pattern syntax for tVerifyEmail](/talend/r/en-US/8.0/components/email-validation/simplified-pattern-syntax-for-tverifyemail).  -Use column content: use the fields in this view to decide the content against which you want to check the local part of the email. If the local part does not match what you have defined, it will be rewritten by using the content of the fields.  -Enable case-sensitive pattern matching: select this check box to enable a case sensitive pattern matching of the local part of email addresses. You can use case sensitive pattern matching with each of the above options. |
| DOMAIN Part Options | Fields in this view will vary according to what option you select.  -Check the Top-level Domains and the following ones: select this check box to verify the part of the email address which follows the last dot. You can use the Additional Top-level Domains table to add additional top-level domains against which you want to validate email addresses.  -Check domains with a black list: select this option to verify the domains you define in the Domain list table as black listed.  -Check domains with a white list: select this option to verify the domains you define in the Domain List table as white listed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-standard-properties -->
# tVerifyEmail Standard properties

Last updated: 9/30/2026

These properties are used to configure tVerifyEmail running in the Standard Job framework.

The Standard
tVerifyEmail component belongs to the Data Quality family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.  The output schema of tVerifyEmail has different read-only columns depending on the options you select in the component Basic settings view. Read-only output columns include:  VerificationLevel: provides you with the verification status of the processed email addresses as the following:  -*VALID*: means that the email address comply with the defined rule.  -*INVALID*: means that the email address does not comply with the defined rule.  -*CORRECTED*: means that the input email does not comply with the defined rule and has been corrected by using the content of the selected columns. This column is available only when you select the Use column content option in the LOCAL Part Options section.  -*VERIFIED*: means that the email address does exist at the domain. This column is available only when you select the Check with mail server callback option.  -*REJECTED*: means that the email address does not exist at the domain. This column is available only when you select the Check with mail server callback option.  Suggested\_Email: provides you with a suggested content for the email part before the @ sign. The email string is built up from the columns you select from the Use column content view. |
| Column to validate | Select from the list the column you want to validate with tVerifyEmail. |
| Check the entire email with regular expression | Select this check box if you want to match the complete email address against a specific regular expression.  Complete regular expression: enter the regular expression against which you want to match email addresses.  This match is done as a first step to optimize the matching process and exclude addresses that have problems before going any further to match the local and domain parts of email addresses. |
| LOCAL Part Options | Fields in this section will vary according to what option you select. "LOCAL part" in an email address refers to the string before the @ sign.  -Use regular expression: enter in the Pattern field the expression against which you want to check the local part of the email address.  -Use simplified pattern: enter in the Pattern field the simplified pattern against which you want to check the local part of the email address. Select the Show syntax of simplified pattern option to display the syntax to use for simplified patterns. For more information about the syntax, see [Simplified pattern syntax for tVerifyEmail](/talend/r/en-US/8.0/components/email-validation/simplified-pattern-syntax-for-tverifyemail).  -Use column content: use the fields in this view to decide the content against which you want to check the local part of the email. If the local part does not match what you have defined, it will be rewritten by using the content of the fields.  -Enable case-sensitive pattern matching: select this check box to enable a case sensitive pattern matching of the local part of email addresses. You can use case sensitive pattern matching with each of the above options. |
| DOMAIN Part Options | Fields in this view will vary according to what option you select.  -Check the Top-level Domains and the following ones: select this check box to verify the part of the email address which follows the last dot. You can use the Additional Top-level Domains table to add additional top-level domains against which you want to validate email addresses.  -Check domains with a black list: select this option to verify the domains you define in the Domain list table as black listed.  -Check domains with a white list: select this option to verify the domains you define in the Domain List table as white listed. |
| Check with mail server callback | Select this check box to enable the verification of email addresses by the SMTP server.  With this technique, the mail server verifies the complete address (parts before and after the @ sign). It establishes a successful SMTP connection to the mail exchanger (MX) of the email address. Then it queries the exchanger, and make sure that it accepts the address as a valid one. This is done in the same way as sending an email to the address, however the process is stopped after the mail exchanger accepts or rejects the address.  It is not advisable to enable the SMTP verification when you have a lot of email addresses with different domains to check as some mail servers may not reply correctly and even black list your IP address.  The following is a list of cases when the SMTP verification will not work properly:  * When the mail server requires authentication, * When the mail server has a security policy that may put your IP put into   a black list and reject your queries, * When the mail server is taking too long to reply (time out), * Any other unexpected exception generated by the mail server.  When the mail server accepts all emails from a domain, the component cannot verify whether the email address exists or not.  In all these cases, the component results will only take into account the results from the other rules you set in the component settings. |
| Mail server connection timeout (s) | This field is available when Check with mail server callback is selected. Only positive integers are supported. The default value is 10.  For performance reasons, when you enter 0, the timeout is set to 10 seconds. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-verifying-email-addresses-against-column-content-and-domain-names-standard-component-enterprise-this -->
# Verifying email addresses against column content and domain names

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes a Job which uses:

* the tFixedFlowInput component to generate the
  email addresses to be analyzed,
* the tverifyEmail component to format the email
  addresses through *Talend* email API,
* the tFileOutputExcel component to output the
  formatted addresses in an .xls file.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise)
* [Verifying and formatting email addresses](/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-verifying-and-formatting-email-addresses-standard-component-enterprise)
* [Configuring the output component and executing the Job](/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise)

**Related concepts**  

* [tVerifyEmail](tverifyemail "Verifies if email addresses comply with specific rules and corrects addresses that do not match the rules by using the content from specific columns.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view in the Component tab.
2. Create the schema through the Edit Schema
   button.

   In the open dialog box, click the [+] button
   and add the columns that will hold input address data. For this example, add
   *firstname*, *lastname* and
   *email*.
3. Click OK.
4. In the Number of rows field, enter
   *1*.
5. In the Mode area, select the Use Inline Table option.
6. In the Inline table, use the [+] button to add lines to the table and then enter the
   address data you want to analyze.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise -->
# Configuring the output component and executing the Job

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileOutputExcel component
   to display the Basic settings view and define
   the component properties.
2. Set the destination file name as well as the sheet name and then select the
   Define all columns auto size check box.
3. Save your Job and press F6 to execute
   it.

   The tVerifyEmail component analyzes email
   addresses and corrects those that do not match what you have defined in the
   local and domain part options.
4. Right-click the output component and select Data
   Viewer to display the formatted email addresses.

   tVerifyEmail matches input addresses against
   the rule you set in the LOCAL part options
   section and the parameters you set for the domain names.

   The VerificationLevel output column returns
   the status as *VALID*, *INVALID*,
   *CORRECTED* and *REJECTED* according
   to what you set/selected in tVerifyEmail basic
   settings.

   All email addresses labeled as *CORRECTED* have a suggested
   address in the SuggestedEmail output column.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tVerifyEmail and
   tFileOutputExcel.
2. Connect the three components together using the Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/email-validation/tverifyemail-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-verifying-and-formatting-email-addresses-standard-component-enterprise -->
# Verifying and formatting email addresses

Last updated: 9/30/2026

## Procedure

1. Double-click tVerifyEmail to display the
   Basic settings view and define the component
   properties.
2. If required, click Sync columns to retrieve
   the schema defined in the input component.
3. Click the Edit schema button to open the
   schema dialog box.

   tVerifyEmail proposes predefined read-only
   address columns as shown in the below capture.

   The VerificationLevel column returns the
   verification status of input email addresses. The SuggestedEmail column returns a suggested content for the email part
   before the @ sign. This column is shown in the output schema only if you select
   theUse column content option in the Local Part Options section. For further information about
   output columns, see [tVerifyEmail Standard properties](/talend/en-US/components/8.0/email-validation/tverifyemail-standard-properties).
4. Move any of the input columns to the output schema if you want to show them in
   the verification results, click OK and accept
   to propagate the changes.
5. From the Column to validate list, select the
   *email* column.
6. In the LOCAL Part Options section, select the
   Use column content option.

   In this example, you want to check the email part before the @ sign to see if
   it starts with the first letter of the first name followed by the family name,
   all in lower case. If the local part does not match what you have defined,
   tVerifyEmail will rewrite it by using the
   parameters you define.
7. In the DOMAIN Part Options, select:
   * the Check the default Top-level Domains and the
     following ones check box and define in the table the
     additional top-level domain against which you want to validate email
     addresses.
   * the Check domains with a black list
     check box and define in the Domain list
     table the domain to consider as black listed.
8. Select the Check with mail server callback
   check box to enable the mail server to verify the complete address and accept or
   reject the email.
