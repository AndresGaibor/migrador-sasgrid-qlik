<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tdataqualityrules · versión 8.0 -->
# tDataQualityRules properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDataQualityRules
running in the Spark Batch Job framework.

The Spark Batch tDataQualityRules component belongs to the Data Quality family.

Information noteAttention: From Talend Studio 8.0 R2025-06, the tDataQualityRules Standard component is
replaced by tDQRules. This component lets you use the rules from:

* Qlik Talend Data Integration.
* Talend Cloud Data Inventory.
* Talend Cloud Data Stewardship.
* The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater.

For Apache Spark Jobs, you can only use
tDataQualityRules with the Talend apps.

## Basic settings

| Properties | Description |
| --- | --- |
| Output schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Click Sync columns to retrieve the schema from the previous component connected in the Job.  Select the Schema type:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:  View schema: choose this option to view the schema only.  Change to built-in property: choose this option to change the schema to Built-in for local changes.  Update repository connection: choose this option to change the schema stored in the repository and decide whether to propagate the changes to all the Jobs upon completion.  The supported types are: Boolean, Date, Double, Float, Integer, Long, Short, and String. |
| Application | Select the application from which you want to retrieve the data quality rules. This option is available from Talend Studio 8.0 R2024-01 onwards. |
| URL | Information noteImportant:  You need the Rules - View permission to retrieve the rules. For more information, see the [predefined user roles](/talend/r/en-US/Cloud/management-console-user-guide/tmc-predefined-roles) for the app you are using.  Enter the URL of the selected app. When the URL does not match the selected app, the Job may fail. The following URLs are supported:  * Talend Cloud Data Stewardship, or the hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater: ```   https://tds.<env>.cloud.talend.com/rulerepository/api/v1   https://tds.<env>.cloud.talend.com/rulerepository/api/v1/   https://tds.<env>.cloud.talend.com/rulerepository   https://tds.<env>.cloud.talend.com/rulerepository/   https://tds.<env>.cloud.talend.com (Only for Talend Cloud Data Stewardship)   https://tds.<env>.cloud.talend.com/ (Only for Talend Cloud Data Stewardship)   ```  When you use the hybrid version, you can use a URL with the   IP address or the hostname:  ```   https://ip:19999/rulerepository/api/v1   https://ip:19999/rulerepository/api/v1/   https://ip:19999/rulerepository   https://ip:19999/rulerepository/   https://hostname:19999/rulerepository/api/v1   https://hostname:19999/rulerepository/api/v1/            https://hostname:19999/rulerepository   https://hostname:19999/rulerepository/   ``` * Talend Cloud Data Inventory, from Talend Studio 8.0   R2023-06: ```   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1/   https://tdc.<env>.cloud.talend.com/rulerepository   https://tdc.<env>.cloud.talend.com/rulerepository/   https://tdc.<env>.cloud.talend.com   https://tdc.<env>.cloud.talend.com/   ```  where <env> part is the name of your Cloud region. See [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Token | Enter your personal access token. To generate one, see [https://help.talend.com/r/en-US/Cloud/management-console-user-guide/cloud-access-token](/talend/r/en-US/Cloud/management-console-user-guide/cloud-access-token). |
| DQ rule library timestamp | After you entered the URL and token, click Refresh. If the URL and token are correct, the data quality rules are retrieved into Talend Studio: `yyyy-MM-dd hh:mm:ss (library_number)`.  When you click Refresh, a `JAR` file containing the rule definition is created in: ``` studio-path\configuration\.m2\repository\org\talend\libraries\rule-number ```  When you update the data quality rules in the Cloud or hybrid application, click Refresh to retrieve the latest version. |
| Configure DQ rules | Associate the variables of the rule with the input data. The rules are retrieved from the library:  * DQ Rule: Select the rule. * Rule variable: The variables of the rule are   automatically retrieved. * Input column: Select the column that contains   the values that must replace the variable.  If no rules or input columns are available, verify that:  * Data quality rules have been retrieved in DQ rule library   timestamp. * The input schema is correct.  You can associate the data types from Talend Studio with some data types from the apps. See [Associating data types](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules#associating-data-types) below.  To apply more rules, click . |

## Associating data types

The following table describes the data types you can associate.

| Rule variable from the app\* | Input column (from Talend Studio) |
| --- | --- |
| Number | Double, Float, Integer, Long, Short, and String |
| Boolean | Boolean |
| Text | String |
| Date | Date |
| \* You can enter the URL of:  * Talend Cloud Data Stewardship. * The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater. * Talend Cloud Data Inventory, from Talend Studio 8.0 R2023-06. | |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/validation/tdataqualityrules-for-apache-spark-batch -->
# tDataQualityRules properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDataQualityRules
running in the Spark Batch Job framework.

The Spark Batch tDataQualityRules component belongs to the Data Quality family.

Information noteAttention: From Talend Studio 8.0 R2025-06, the tDataQualityRules Standard component is
replaced by tDQRules. This component lets you use the rules from:

* Qlik Talend Data Integration.
* Talend Cloud Data Inventory.
* Talend Cloud Data Stewardship.
* The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater.

For Apache Spark Jobs, you can only use
tDataQualityRules with the Talend apps.

## Basic settings

| Properties | Description |
| --- | --- |
| Output schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Click Sync columns to retrieve the schema from the previous component connected in the Job.  Select the Schema type:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:  View schema: choose this option to view the schema only.  Change to built-in property: choose this option to change the schema to Built-in for local changes.  Update repository connection: choose this option to change the schema stored in the repository and decide whether to propagate the changes to all the Jobs upon completion.  The supported types are: Boolean, Date, Double, Float, Integer, Long, Short, and String. |
| Application | Select the application from which you want to retrieve the data quality rules. This option is available from Talend Studio 8.0 R2024-01 onwards. |
| URL | Information noteImportant:  You need the Rules - View permission to retrieve the rules. For more information, see the [predefined user roles](/talend/r/en-US/Cloud/management-console-user-guide/tmc-predefined-roles) for the app you are using.  Enter the URL of the selected app. When the URL does not match the selected app, the Job may fail. The following URLs are supported:  * Talend Cloud Data Stewardship, or the hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater: ```   https://tds.<env>.cloud.talend.com/rulerepository/api/v1   https://tds.<env>.cloud.talend.com/rulerepository/api/v1/   https://tds.<env>.cloud.talend.com/rulerepository   https://tds.<env>.cloud.talend.com/rulerepository/   https://tds.<env>.cloud.talend.com (Only for Talend Cloud Data Stewardship)   https://tds.<env>.cloud.talend.com/ (Only for Talend Cloud Data Stewardship)   ```  When you use the hybrid version, you can use a URL with the   IP address or the hostname:  ```   https://ip:19999/rulerepository/api/v1   https://ip:19999/rulerepository/api/v1/   https://ip:19999/rulerepository   https://ip:19999/rulerepository/   https://hostname:19999/rulerepository/api/v1   https://hostname:19999/rulerepository/api/v1/            https://hostname:19999/rulerepository   https://hostname:19999/rulerepository/   ``` * Talend Cloud Data Inventory, from Talend Studio 8.0   R2023-06: ```   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1/   https://tdc.<env>.cloud.talend.com/rulerepository   https://tdc.<env>.cloud.talend.com/rulerepository/   https://tdc.<env>.cloud.talend.com   https://tdc.<env>.cloud.talend.com/   ```  where <env> part is the name of your Cloud region. See [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Token | Enter your personal access token. To generate one, see [https://help.talend.com/r/en-US/Cloud/management-console-user-guide/cloud-access-token](/talend/r/en-US/Cloud/management-console-user-guide/cloud-access-token). |
| DQ rule library timestamp | After you entered the URL and token, click Refresh. If the URL and token are correct, the data quality rules are retrieved into Talend Studio: `yyyy-MM-dd hh:mm:ss (library_number)`.  When you click Refresh, a `JAR` file containing the rule definition is created in: ``` studio-path\configuration\.m2\repository\org\talend\libraries\rule-number ```  When you update the data quality rules in the Cloud or hybrid application, click Refresh to retrieve the latest version. |
| Configure DQ rules | Associate the variables of the rule with the input data. The rules are retrieved from the library:  * DQ Rule: Select the rule. * Rule variable: The variables of the rule are   automatically retrieved. * Input column: Select the column that contains   the values that must replace the variable.  If no rules or input columns are available, verify that:  * Data quality rules have been retrieved in DQ rule library   timestamp. * The input schema is correct.  You can associate the data types from Talend Studio with some data types from the apps. See [Associating data types](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules#associating-data-types) below.  To apply more rules, click . |

## Associating data types

The following table describes the data types you can associate.

| Rule variable from the app\* | Input column (from Talend Studio) |
| --- | --- |
| Number | Double, Float, Integer, Long, Short, and String |
| Boolean | Boolean |
| Text | String |
| Date | Date |
| \* You can enter the URL of:  * Talend Cloud Data Stewardship. * The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater. * Talend Cloud Data Inventory, from Talend Studio 8.0 R2023-06. | |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/validation/tdataqualityrules-for-apache-spark-structured-streaming -->
# tDataQualityRules properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tDataQualityRules
running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming tDataQualityRules component belongs to the Data Quality family.

This component is supported on Local Spark 3.5.x and Databricks/EMR with Spark 3.x.

Information noteImportant: Before you run this component, manually upload the semantic JAR to the cluster because it is too large for automatic upload.

## Basic settings

| Properties | Description |
| --- | --- |
| Output schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Click Sync columns to retrieve the schema from the previous component connected in the Job.  Select the Schema type:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:  View schema: choose this option to view the schema only.  Change to built-in property: choose this option to change the schema to Built-in for local changes.  Update repository connection: choose this option to change the schema stored in the repository and decide whether to propagate the changes to all the Jobs upon completion.  The supported types are: Boolean, Date, Double, Float, Integer, Long, Short, and String. |
| Application | Select the application from which you want to retrieve the data quality rules. |
| URL | Information noteImportant:  You need the Rules - View permission to retrieve the rules. For more information, see the [predefined user roles](/talend/r/en-US/Cloud/management-console-user-guide/tmc-predefined-roles) for the app you are using.  Enter the URL of the selected app. When the URL does not match the selected app, the Job may fail. The following URLs are supported:  * Talend Cloud Data Stewardship, or the hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater: ```   https://tds.<env>.cloud.talend.com/rulerepository/api/v1   https://tds.<env>.cloud.talend.com/rulerepository/api/v1/   https://tds.<env>.cloud.talend.com/rulerepository   https://tds.<env>.cloud.talend.com/rulerepository/   https://tds.<env>.cloud.talend.com (Only for Talend Cloud Data Stewardship)   https://tds.<env>.cloud.talend.com/ (Only for Talend Cloud Data Stewardship)   ```  When you use the hybrid version, you can use a URL with the   IP address or the hostname:  ```   https://ip:19999/rulerepository/api/v1   https://ip:19999/rulerepository/api/v1/   https://ip:19999/rulerepository   https://ip:19999/rulerepository/   https://hostname:19999/rulerepository/api/v1   https://hostname:19999/rulerepository/api/v1/            https://hostname:19999/rulerepository   https://hostname:19999/rulerepository/   ``` * Talend Cloud Data Inventory, from Talend Studio 8.0   R2023-06: ```   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1   https://tdc.<env>.cloud.talend.com/rulerepository/api/v1/   https://tdc.<env>.cloud.talend.com/rulerepository   https://tdc.<env>.cloud.talend.com/rulerepository/   https://tdc.<env>.cloud.talend.com   https://tdc.<env>.cloud.talend.com/   ```  where <env> part is the name of your Cloud region. See [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Token | Enter your personal access token. To generate one, see [https://help.talend.com/r/en-US/Cloud/management-console-user-guide/cloud-access-token](/talend/r/en-US/Cloud/management-console-user-guide/cloud-access-token). |
| DQ rule library timestamp | After you enter the URL and token, click Refresh. If the URL and token are correct, the data quality rules are retrieved into Talend Studio: `yyyy-MM-dd hh:mm:ss (library_number)`.  When you click Refresh, a `JAR` file containing the rule definition is created in: ``` studio-path\configuration\.m2\repository\org\talend\libraries\rule-number ```  When you update the data quality rules in the Cloud or hybrid application, click Refresh to retrieve the latest version. |
| Configure DQ rules | Associate the variables of the rule with the input data. The rules are retrieved from the library:   * DQ Rule: Select the rule. * Rule variable: The variables of the rule are automatically retrieved. * Input column: Select the column that contains the values that must replace the variable.   If no rules or input columns are available, verify that:  * Data quality rules have been retrieved in DQ rule library   timestamp. * The input schema is correct.  You can associate the data types from Talend Studio with some data types from the apps. See [Associating data types](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules#associating-data-types) below. |

## Associating data types

The following table describes the data types you can associate.

| Rule variable from the app\* | Input column (from Talend Studio) |
| --- | --- |
| Number | Double, Float, Integer, Long, Short, and String |
| Boolean | Boolean |
| Text | String |
| Date | Date |
| \* You can enter the URL of:  * Talend Cloud Data Stewardship. * The hybrid version of Talend Data Stewardship 8.0 R2022-07 and greater. * Talend Cloud Data Inventory, from Talend Studio 8.0 R2023-06. | |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
