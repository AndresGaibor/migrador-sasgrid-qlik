<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cosmosdb/tcosmosdbsqlapioutput · versión 8.0 -->
# tCosmosDBSQLAPIOutput

Last updated: 9/30/2026

Inserts, updates, upserts, or deletes documents in a Cosmos database collection
based on the incoming flow from the preceding component through SQL API.

## tCosmosDBSQLAPIOutput Standard properties

These properties are used to configure tCosmosDBSQLAPIOutput running in the Standard Job framework.

The Standard
tCosmosDBSQLAPIOutput component belongs to the Databases NoSQL family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository.   * Built-in: No property data is stored   centrally. * Repository: Select the repository file   in which the properties are stored. The fields that follow are completed   automatically using the data retrieved. |
| Edit Schema | Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component supports dynamic schema when inserting documents to a collection. To use the dynamic schema feature, make sure the collection does not have any partition keys, and the schema contains only one column, with the DB column set to `*` and Type set to `String` (if the input type is String) or `Object` (if the input type is Object).  Information noteNote:  * The dynamic schema feature is available only when   `Insert` is selected from the Action   on data drop-down list. * The dynamic schema feature is available only when you have installed the   8.0.1-R2024-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| URI | Enter the URI of your Cosmos user account. As the field prompts, the URI of a Cosmos DB user account is in the format of `https://{your_account}.document.azure.com:443`. You can obtain the URI on the Keys pane of Azure portal. Click [Create an Azure Cosmos DB account](https://docs.microsoft.com/en-us/azure/cosmos-db/create-cosmosdb-resources-portal) for related information. |
| Primary key | Enter the primary key of your CosmosDB user account. You can obtain the primary key on the Keys pane of Azure portal. Click [Create an Azure Cosmos DB account](https://docs.microsoft.com/en-us/azure/cosmos-db/create-cosmosdb-resources-portal) for related information.  To enter the primary key, click the [...] button next to the Primary key field to bring out the Enter a new password dialog box, enter the primary key in the text field, and click OK. Note that you can enter the primary key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter primary keys in the Java mode   only. |
| Database ID | Enter the database name. |
| Collection ID | Enter the collection name. |
| Create collection if not exist | Select this option to have the collection specified in the Collection ID field created if it does not exist. This option is not available if Update or Delete is selected from the Data action drop-down list. |
| Data action | Select one of the following options.   * Insert: inserts documents. * Update: replaces the existing documents with the   incoming data but keeps the technical ID of these documents. * Upsert: inserts a document if it does not exist   otherwise it applies the same rules as Update. * Delete: deletes documents. |
| Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated) This content is deprecated. Auto ID generation | Select this option to generate IDs for the documents processed. Information noteDeprecation: This option is deprecated since the 8.0.1-R2024-03 monthly release. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| Connection mode | Specify the connection mode to be used. Two options are available: `Gateway` and `DirectHttps`. Click [ConnectionMode](https://docs.microsoft.com/en-us/java/api/com.microsoft.azure.cosmosdb.connectionmode?view=azure-java-legacy) for related information. |
| Max connection pool size | Set the maximum connection pool size. The default is 1000. |
| Consistency level | Set the consistency level. Click [Consistency levels](https://docs.microsoft.com/en-us/azure/cosmos-db/consistency-levels) for related information. |
| Partition key | Enter the key of the partition whose documents will be removed. The partition key is recommended to be a non-null value.  With the 8.0.1-R2024-03 monthly release, you can enter three different types of partition keys: Boolean, Double, and String. The partition keys can also be configured up to a three level hierarchy. For more information, see [Hierarchical partition keys in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/hierarchical-partition-keys?tabs=java-v4%2Cbicep) from the Microsoft documentation.  This option is available when you select the Create collection if not exsist check box. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tCosmosDBSQLAPIOutput executes the action defined on the collection in the database based on the flow incoming from the preceding component in the Job. |
| **Cosmos DB limitation for HTTPS proxies with authentication** | HTTP proxies and HTTPS proxies work with the tSetProxy component, however:  * HTTPS proxies with authentication do not work with the Use   authorization option in tSetProxy   for this component. This is because the Cosmos DB SDK does not use Java’s   Authenticator for HTTPS proxy tunneling and instead   relies on JVM system properties. * For this component to work with an authenticated HTTPS proxy, you must   manually configure proxy credentials as JVM arguments in Run > Advanced Settings > JVM arguments: ```   -Dhttps.proxyUser=<username>   -Dhttps.proxyPassword=<password>   ```  Additional limitation: Proxy configuration is managed through global JVM system properties, so using multiple, different proxy settings for different components in the same Job is not recommended, as the configuration will not work as intended. |
