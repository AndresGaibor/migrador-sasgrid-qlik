<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tdqrules · versión 8.0 -->
# tDQRules / tDataQualityRules

Last updated: 9/30/2026

Validates data using data quality rules by connecting Talend Studio to
Qlik Talend Data Integration, or to a Talend
app.

Information noteAttention: From Talend Studio 8.0 R2025-06, the tDataQualityRules Standard component is
replaced by tDQRules. This component lets you use the rules from:

* Qlik Talend Data Integration.
* Talend Cloud Data Inventory.
* Talend Cloud Data Stewardship.
* The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater.

For Apache Spark Jobs, you can only use
tDataQualityRules with the Talend apps.

For more information on each app, see the corresponding documentation:

* For Qlik Talend Data Integration, see
  [Working with validation rules](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Working-with-validation-rules.htm) in Qlik Cloud
  documentation.
* For Talend Cloud Data Stewardship, see
  [What is a data quality rule?](/talend/r/en-US/Cloud/data-stewardship-user-guide/tds-dqr) in the Talend Cloud Data Stewardship User
  Guide.
* For the hybrid version of Talend Data Stewardship 8.0
  R2022-07 and greater, see the [What is a data quality rule?](/talend/r/en-US/8.0/data-stewardship-user-guide/tds-dqr) in the Talend Data Stewardship User
  Guide. For more information on the hybrid version, see [What is hybrid for Talend Cloud?](/talend/r/en-US/Cloud/hybrid-installation-guide-windows/what-is-hybrid-for-talend-cloud).
* For Talend Cloud Data Inventory, see
  the [What is a data quality rule?](/talend/r/en-US/Cloud/data-inventory-user-guide/data-quality-rules) in the Talend Cloud Data Inventory User
  Guide. You can connect to this app in Talend Studio 8.0
  R2023-06 and greater.

A data quality rule is a set of business requirements which defines the values your data
must comply with.

To retrieve the data quality rules into a `JAR` file,
tDQRules connects Talend Studio to one of
the app listed above. Talend Studio uses the
retrieved library so you can apply data quality rules to your data. For more information on
how the component works with Talend apps,
see [Description of the local and
Cloud/hybrid process](tdqrules-local-cloud-process "You can retrieve data quality rules by connecting Talend Studio to Qlik Talend Data Integration, or a Talend app.").

The following table describes the categories and subcategories into which the component
returns the data:

| Output categories | tDataQualityRules | tDQRules |
| --- | --- | --- |
| Valid These data follow the Main flow. | * Valid: The data fulfill the condition and the validation expression   or the data fulfill the alternative validation expression only. * Not applicable (NA): The data do not fulfill the condition. The rule   cannot be applied to the data. | The data fulfill the condition and the validation expression or the data fulfill the alternative validation expression only. |
| Invalid These data follow the Reject flow. | * Invalid: The data fulfill the condition but not the validation   expression. * Not executable (NE): The rule cannot be executed on the data. For   example, when the data types do not match. | * Invalid: The data fulfill the condition but not the validation   expression. * Not executable (NE): The rule cannot be executed on the data. For   example, when the data types do not match. * When there is no result, it means there is no result to return   . |
| Not Applicable These data follow the Not\_Applicable flow. | Not applicable to this component | The data do not fulfill the condition. The rule cannot be applied to the data. |

When two or more rules are used, the data is categorized depending on the results of each
rule and the component you are using. The following tables describe the results of the
validation logic:

Validation logic of tDQRules

|  | Valid | Invalid | Not Applicable |
| --- | --- | --- | --- |
| Valid | Valid | Invalid | Valid |
| Invalid | Invalid | Invalid | Invalid |
| Not applicable | Valid | Invalid | Not applicable |

Validation logic of tDataQualityRules

|  | Valid | Invalid | Not Applicable |
| --- | --- | --- | --- |
| Valid | Valid | Invalid | Valid |
| Invalid | Invalid | Invalid | Invalid |
| Not applicable | Valid | Invalid | Valid |

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

You need the Qlik Talend Cloud Enterprise Edition to use
the tDQRules / tDataQualityRules component.

Apache Spark tDataQualityRules supports:

* In local mode, Apache Spark 3.0 and greater.
* Cloudera Data Engineering service with Apache Spark 3.1 or 3.2.

## Standard properties

These properties are used to configure tDQRules and
tDataQualityRules running in the standard Job framework.

The standard tDQRules and tDataQualityRules
components belong to the Data Quality family.

Information noteImportant:

If you are using tDataQualityRules, see [Basic settings for
tDataQualityRules](#basic-tdataqualityrules). This component has been combined
with tDQRules from Talend Studio 8.0
R2025-06 but the properties of tDataQualityRules are the same.
They do not depend on the version you are using.

## Basic settings for tDQRules

| Properties | Description |
| --- | --- |
| Cloud | Select the app from which you want to retrieve the rules:  * Qlik Talend Cloud Data Integration * Talend Cloud Data Inventory or Stewardship   Click Apply to enable more settings.  If you selected Talend Cloud Data Inventory or Stewardship, you are using tDataQualityRules, see [Basic settings for tDataQualityRules](#basic-tdataqualityrules). |
| Property Type | Select the way the file path and the schema will be set.   * Built-In: The file path and the schema will be   set locally for this component. * Repository: The file details stored centrally   in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   file to be reused, and all related properties will be automatically   filled in. |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Click Sync columns to retrieve the schema from the previous component connected in the Job.  Select the Schema type:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:  View schema: choose this option to view the schema only.  Change to built-in property: choose this option to change the schema to Built-in for local changes.  Update repository connection: choose this option to change the schema stored in the repository and decide whether to propagate the changes to all the Jobs upon completion.  The supported types are: Boolean, Date, Double, Dynamic, Float, Integer, Long, Short, and String. |
| URL | Information noteImportant: You need the Rules - View permission to retrieve the rules.  Enter the URL of the app. For example, `https://qcs.us.qlikcloud.com/`. |
| API key | Enter your API key. To generate one, see [Generating an API key](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-generate-api-keys.htm). |
| Rule library timestamp | After you entered the URL and token, click Fetch rules. If the URL and token are correct, the rules are retrieved into Talend Studio: `yyyy-MM-dd hh:mm:ss (library_number)`.  When you click Fetch rules, a `JAR` file containing the rule definition is created in: ``` studio-path\configuration\.m2\repository\org\talend\libraries\rule-number ```  When you update the rules in the app, click Fetch rules to retrieve the latest version. |
| Rule name | This option is available until Talend Studio 8.0 R2025-12.  Select the rule from the list and click Refresh table. |
| Rules | This option is available from Talend Studio 8.0 R2026-01. Select one or more rules and click Refresh table. |
| Rule content | Associate the variables of the rule with the input data.  The rule is retrieved from the library:  * Rule name (from Talend Studio 8.0 R2026-01): The rule name retrieved from the Cloud app. * Rule variable: The variable from the Cloud   app. * Input column: The input column from Talend Studio. * Fact column: The input column from Talend Studio when the column is dynamic. When no rules or input columns are available, verify that:  * Rules have been retrieved in Rule library   timestamp. * The input schema is correct. |

## Basic settings for tDataQualityRules

| Properties | Description |
| --- | --- |
| Cloud | This option is available from Talend Studio 8.0 R2025-06. Select the app from which you want to retrieve the rules:  * Qlik Talend Cloud Data Integration * Talend Cloud Data Inventory or Stewardship   Click Apply to enable more settings.  If you selected Qlik Talend Cloud Data Integration, you are using tDQRules, see [Basic settings for tDQRules](#basic-tdqrules). |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Click Sync columns to retrieve the schema from the previous component connected in the Job.  Select the Schema type:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:  View schema: choose this option to view the schema only.  Change to built-in property: choose this option to change the schema to Built-in for local changes.  Update repository connection: choose this option to change the schema stored in the repository and decide whether to propagate the changes to all the Jobs upon completion.  The supported types are: Boolean, Date, Double, Dynamic, Float, Integer, Long, Short, and String. |
| Application | Select the application from which you want to retrieve the data quality rules. You can select one or more rules. |
| URL | Information noteImportant: You need the Rules - View permission to retrieve the rules.  Enter the URL of the selected app. For example, `https://qcs.us.qlikcloud.com/` for Qlik Talend Data Integration.  For Talend apps, the following URLs are supported:  * Talend Cloud Data Stewardship, or the hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater: ```   https://tds.<env>.cloud.talend.com/rulerepository/api/v1   https://tds.<env>.cloud.talend.com/rulerepository/api/v1/   https://tds.<env>.cloud.talend.com/rulerepository   https://tds.<env>.cloud.talend.com/rulerepository/   https://tds.<env>.cloud.talend.com (Only for Talend Cloud Data Stewardship)   https://tds.<env>.cloud.talend.com/ (Only for Talend Cloud Data Stewardship)   ```  When you use the hybrid version, you can use a URL with the   IP address or the hostname:  ```   https://ip:19999/rulerepository/api/v1   https://ip:19999/rulerepository/api/v1/   https://ip:19999/rulerepository   https://ip:19999/rulerepository/   https://hostname:19999/rulerepository/api/v1   https://hostname:19999/rulerepository/api/v1/            https://hostname:19999/rulerepository   https://hostname:19999/rulerepository/   ``` * Talend Cloud Data Inventory, from Talend Studio 8.0   R2023-06: ```   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1/   https://tdc.<env>.cloud.talend.com/rulerepository   https://tdc.<env>.cloud.talend.com/rulerepository/   https://tdc.<env>.cloud.talend.com   https://tdc.<env>.cloud.talend.com/   ``` |
| Token | Enter your token. To generate one, see [Generating a Personal Access Token](/talend/r/en-US/Cloud/management-console-user-guide/cloud-access-token). |
| DQ rule library timestamp | After you entered the URL and token, click Refresh. If the URL and token are correct, the rules are retrieved into Talend Studio: `yyyy-MM-dd hh:mm:ss (library_number)`.  When you click Fetch rules, a `JAR` file containing the rule definition is created in: ``` studio-path\configuration\.m2\repository\org\talend\libraries\rule-number ```  When you update the rules in the Cloud or hybrid application, click Refresh to retrieve the latest version. |
| Configure DQ rules | Associate the variables of the rule with the input data. The rules are retrieved from the library:  * DQ Rule: Select the rule. * Rule variable: The variables of the rule are   automatically retrieved. * Input column: Select the column that contains the   values that must replace the variable. * Dynamic column selection: When you selected a   dynamic column as Input column, enter the column   name between double quotes. Information noteRestriction: You can associate a rule   variable to one column only. Enter one column only in Dynamic column   selection.  If no rules or input columns are available, verify that:  * Data quality rules have been retrieved in DQ rule library   timestamp. * The input schema is correct.  You can associate the data types from Talend Studio with some data types from the apps. See [Associating data types](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules#associating-data-types) below.  To apply more rules, click . |

## Associating data types

The following table describes the data types you can associate.

| Rule variable from the app\* | Input column (from Talend Studio) |
| --- | --- |
| Number | Double, Float, Integer, Long, Short, and String |
| Boolean | Boolean |
| Text | String |
| Date | Date |
| Any data types supported in the application | Dynamic |
| \* You can enter the URL of:  * Talend Cloud Data Stewardship. * The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater. * Talend Cloud Data Inventory, from Talend Studio 8.0 R2023-06. | |

For Qlik Talend Data Integration, see
the types supported on the app in [Working with data quality rules](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Working-with-validation-rules.htm#operators).

When using the date/time operators in the tDQRules component, you
cannot use some words as the column names because they are reserved keywords. For more
information, see [Language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md).

## Advanced Settings

| Properties | Description |
| --- | --- |
| tStatCatcher statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tdqrules-local-cloud-process -->
# Description of the local and Cloud/hybrid process

Last updated: 9/30/2026

You can retrieve data quality rules by connecting Talend Studio to
Qlik Talend Data Integration, or a Talend
app.

* Qlik Talend Data Integration, from Talend Studio 8.0
  R2025-06.
* Talend Cloud Data Inventory, from Talend Studio 8.0
  R2023-06.
* Talend Cloud Data Stewardship
* Hybrid Talend Data Stewardship 8.0
  R2022-07 and greater.

Information noteAttention: From Talend Studio 8.0 R2025-06, the tDataQualityRules Standard component is
replaced by tDQRules. This component lets you use the rules from:

* Qlik Talend Data Integration.
* Talend Cloud Data Inventory.
* Talend Cloud Data Stewardship.
* The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater.

For Apache Spark Jobs, you can only use
tDataQualityRules with the Talend apps.

The process for retrieving the rules is the same either you are using Talend Studio 8.0
R2025-06 or a previous version, only the prerequisites change.

## Prerequisites from Talend Studio 8.0 R2025-06

Information noteRestriction: These prerequisites only apply to the Standard component. The
Apache Spark components work as before. See [Prerequisites before Talend Studio 8.0 R2025-06](#prereq-before-202506).

When you
want to retrieve rules from a Talend app,
you need the Rules - View permission. As data quality rules are
centralized and therefore shared between the apps, you can use the URLs of any Talend app,
as long as you have the correct permission on the app, the same data quality rules are
retrieved.

When you want to retrieve rules from Qlik Talend Data Integration, you need:

* The permission on the space in which the rule is stored.
* The Rules - View.

## Prerequisites before Talend Studio 8.0 R2025-06

Data quality rules are centralized and therefore shared between apps. You can use the
URLs of any app, as long as you have the correct permission on the app, the same data
quality rules are retrieved.  You need the Rules - View
permission to retrieve the rules. For more information, see the [predefined user roles](/talend/r/en-US/Cloud/management-console-user-guide/tmc-predefined-roles) for the
app you are using.

The following diagram describes when the component is connected to an app.

## Process description

1. When you click Fetch rules, the component lets Talend Studio
   connect to the app to retrieve the data quality rules into a
   `JAR` file. When the `is of type`
   operator is used in a data quality rule, one more `JAR` file is
   retrieved. The file contains the semantic types.
2. The `JAR` file is retrieved. Talend Studio
   is no longer connected to the app.
3. You can apply data quality rules to your data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules-local-cloud-process -->
# Description of the local and Cloud/hybrid process

Last updated: 9/30/2026

You can retrieve data quality rules by connecting Talend Studio to
Qlik Talend Data Integration, or a Talend
app.

* Qlik Talend Data Integration, from Talend Studio 8.0
  R2025-06.
* Talend Cloud Data Inventory, from Talend Studio 8.0
  R2023-06.
* Talend Cloud Data Stewardship
* Hybrid Talend Data Stewardship 8.0
  R2022-07 and greater.

Information noteAttention: From Talend Studio 8.0 R2025-06, the tDataQualityRules Standard component is
replaced by tDQRules. This component lets you use the rules from:

* Qlik Talend Data Integration.
* Talend Cloud Data Inventory.
* Talend Cloud Data Stewardship.
* The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater.

For Apache Spark Jobs, you can only use
tDataQualityRules with the Talend apps.

The process for retrieving the rules is the same either you are using Talend Studio 8.0
R2025-06 or a previous version, only the prerequisites change.

## Prerequisites from Talend Studio 8.0 R2025-06

Information noteRestriction: These prerequisites only apply to the Standard component. The
Apache Spark components work as before. See [Prerequisites before Talend Studio 8.0 R2025-06](#prereq-before-202506).

When you
want to retrieve rules from a Talend app,
you need the Rules - View permission. As data quality rules are
centralized and therefore shared between the apps, you can use the URLs of any Talend app,
as long as you have the correct permission on the app, the same data quality rules are
retrieved.

When you want to retrieve rules from Qlik Talend Data Integration, you need:

* The permission on the space in which the rule is stored.
* The Rules - View.

## Prerequisites before Talend Studio 8.0 R2025-06

Data quality rules are centralized and therefore shared between apps. You can use the
URLs of any app, as long as you have the correct permission on the app, the same data
quality rules are retrieved.  You need the Rules - View
permission to retrieve the rules. For more information, see the [predefined user roles](/talend/r/en-US/Cloud/management-console-user-guide/tmc-predefined-roles) for the
app you are using.

The following diagram describes when the component is connected to an app.

## Process description

1. When you click Fetch rules, the component lets Talend Studio
   connect to the app to retrieve the data quality rules into a
   `JAR` file. When the `is of type`
   operator is used in a data quality rule, one more `JAR` file is
   retrieved. The file contains the semantic types.
2. The `JAR` file is retrieved. Talend Studio
   is no longer connected to the app.
3. You can apply data quality rules to your data.
