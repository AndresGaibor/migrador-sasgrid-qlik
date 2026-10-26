<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/couchbase/tcouchbaseinput · versión 8.0 -->
# tCouchbaseInput

Last updated: 9/30/2026

Queries the documents from the Couchbase database.

## tCouchbaseInput Standard properties

These properties are used to configure tCouchbaseInput running in the Standard Job framework.

The Standard
tCouchbaseInput component belongs to the Databases NoSQL family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Bootstrap nodes | Enter the name or IP of the node to be bootstrapped by Couchbase SDK. As Couchbase recommends to specify multiple nodes to bootstrap, enter the names or IPs of these nodes in this field, separating them using commas (,).  For further information about Couchbase bootstrapping, see [How Couchbase SDKs connect to the cluster](https://developer.couchbase.com/documentation/server/4.1/developer-guide/connection-advanced.html).  You can find the node names on the Servers page in your Couchbase Web Console. If you need further information, contact the administrator of your Couchbase cluster or consult your Couchbase documentation.  Note that the Couchbase servers do not support proxies; for this reason, the Couchbase components from Talend do not support proxies either. |
| Username and Password | Provide the authentication credentials to your Couchbase cluster.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  If you are using Couchbase V5.0 and onwards, enter the same value you put in the Bucket field as password, because since Couchbase V5.0, no password is associated with a bucket. However, on Couchbase, you need to create a user with appropriate role to access the buckets.  For further information about the access control and other important requirements on the Couchbase side, see Couchbase release note of your version.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  When using non-JSON documents, define an `id` column of the String type, then define a `content` column. The type of this `content` column should be String for the string documents and byte[] for the binary documents.  When it comes to JSON documents, define the fields that exist in your JSON documents. |
| Bucket | Enter, within double quotation marks, the name of the data bucket in the Couchbase database.  Ensure that the credentials you are using have the appropriate rights and permissions to access this bucket.  If you are using Couchbase V5.0 and onwards, this bucket name is the user name you have created in the Security tab of your Couchbase UI. |
| Document type | Data stored in a Couchbase database could be JSON, strings or binary. From this drop-down list, select the type of the data you need to use with Couchbase.  Note that it is not recommended to mix JSON, binary and string documents in a same bucket, as this mixture could make the document processing error-prone.  If you need to use N1QL to query string or binary documents, the only possible way is to use the document ID to get the document. For example, if you need to get a document for which the ID number is 2, the N1QL query should be ``` SELECT meta().id as `_meta_id_` FROM `bucket_name` where meta().id = '2'; ```  Note that the quotations marks around \_meta\_id\_ and bucket\_name are backticks (`). |
| Query Type | Select the type of queries to be used from the following options:  * Select All: select all the contents of a given   bucket. * N1QL: use an N1QL statement to perform fine-tuned   queries. * N1QL for Analytics: use an N1QL for Analytics   statement to perform queries. N1QL for Analytics is a language for   querying semistructured data. * Document ID: use the document IDs to select   documents. You need to enter the ID to be used in theDocument   ID field that is displayed. Only one document ID is   allowed per component.   Information noteNote:  * See [N1QL for Analytics Language Reference](https://docs.couchbase.com/server/current/analytics/1_intro.html) for information about N1QL for Analytics. * See [N1QL for Analytics vs. N1QL for Query](https://docs.couchbase.com/server/current/analytics/6_n1ql.html) for a comparison between N1QL for Analytics and N1QL for Query. |
| Query | Enter an N1QL query statement or an N1QL for Analytics statement to perform complex actions.  Only one statement is allowed. Do not put quotation marks around the statement.   * When you use wildcards in your query such as SELECT \*, the returned result of this query is wrapped   in the bucket name used in this query. In this situation, define only one column   for the result in the schema of this component.  For example, when performing this query ```   SELECT * FROM `travel_sample` limit 3   ``` The   returned result is wrapped in the `travel_sample` bucket, reading like this: ```   [     {       "travel_sample": {         "callsign": "MILE-AIR",         "country": "United States",         "iata": "Q5",         "icao": "MLA",         "id": 10,         "name": "40-Mile Air",         "type": "airline"       }     },     {       "travel_sample": {         "callsign": "TXW",         "country": "United States",         "iata": "TQ",         "icao": "TXW",         "id": 10123,         "name": "Texas Wings",         "type": "airline"       }     },     {       "travel_sample": {         "callsign": "atifly",         "country": "United States",         "iata": "A1",         "icao": "A1F",         "id": 10226,         "name": "Atifly",         "type": "airline"       }     }   ]   ```  In the schema, define one single column called, for example,   `travel_sample` to store the result and   select String as its type. * If you use a query without wildcards, such as ```   SELECT callsign, country, iata, icao, id, name, type FROM `travel_sample` limit 3;   ``` The   returned result is not wrapped, reading like this: ```   [     {       "callsign": "MILE-AIR",       "country": "United States",       "iata": "Q5",       "icao": "MLA",       "id": 10,       "name": "40-Mile Air",       "type": "airline"     },     {       "callsign": "TXW",       "country": "United States",       "iata": "TQ",       "icao": "TXW",       "id": 10123,       "name": "Texas Wings",       "type": "airline"     },     {       "callsign": "atifly",       "country": "United States",       "iata": "A1",       "icao": "A1F",       "id": 10226,       "name": "Atifly",       "type": "airline"     }   ]   ```  In this situation, define the columns that represent the   structure of the actual business data, such as the following columns, in the   component schema: `callsign`, `country`, `iata`, `icao`, `id`, `name` and   `airline`.   Information noteNote: This field is available when you select `N1QL` or `N1QL Analytics` from the Query type drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Use custom connection parameters | Select this option to set connection parameters, including Connection timeout, Query timeout, Analytics timeout, and Query threshold.  To set a connection parameter, add a row in the Connection parameters table by clicking the plus button on the bottom of the table, click the Parameter name column and select the desired parameter from the drop-down list, and then enter the parameter value in the Parameter value column. |
| Use TLS | Select this option to enable TLS for securing data transferred. See [Couchbase TLS](https://docs.couchbase.com/operator/current/concept-tls.html) for related information.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Java Truststore | Enter the truststore file name. See [KeyStores and TrustStores](https://docs.oracle.com/cd/E19509-01/820-3503/ggffo/index.html) for related information.  Information noteNote: This option is available only when you select the Use TLS option. |
| Java Truststore password | Enter the password for the truststore file. See [Generating a KeyStore and TrustStore](https://docs.oracle.com/cd/E19509-01/820-3503/6nf1il6er/index.html) for related information.  Information noteNote: This option is available only when you select the Use TLS option. |
| Java Truststore type | Enter the Java truststore type, which defaults to `JKS`.  Information noteNote: This option is available only when you select the Use TLS option. |
| Limit rows | Enter the maximum number of rows to be read. This field is not available when you use a N1QL query. |
| Create primary index | Select this check box to let the component create a primary index of your database, or create a new primary index if one already exists. By default, this check box is cleared, as the creation of primary index can be optional if secondary index exists.  For more information about primary index, see [Create primary index](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/createprimaryindex.html) from the official Couchbase documentation. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | As a start component, tCouchbaseInput reads the documents from the Couchbase database. |

**Related concepts**  

* [Querying JSON documents from a Couchbase database with a N1QL query](tcouchbaseinput-tlogrow-querying-json-documents-from-couchbase-database-with-n1ql-query "In this scenario, you query JSON documents with a N1QL query. It uses the travel-sample sample bucket data provided by Couchbase. Specifically, it retrieves the 5 first airlines located in the United States from the sample data.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/couchbase/tcouchbaseinput-tlogrow-querying-json-documents-from-couchbase-database-with-n1ql-query -->
# Querying JSON documents from a Couchbase database with a N1QL query

Last updated: 9/30/2026

In this scenario, you query JSON documents with a N1QL query. It uses the
travel-sample sample bucket data provided by Couchbase.
Specifically, it retrieves the 5 first airlines located in the United States from the sample
data.

Prerequisites: You created a centralized connection to your Couchbase database
and installed the travel-sample sample bucket.

This scenario applies only to subscription-based Talend Platform
products with Big Data and Talend Data Fabric.

### In this section

* [Linking the components](/talend/en-US/components/8.0/couchbase/tcouchbaseinput-tlogrow-linking-components-in)
* [Configuring the components](/talend/en-US/components/8.0/couchbase/tcouchbaseinput-tlogrow-configuring-components)
* [Executing the Job](/talend/en-US/components/8.0/couchbase/tcouchbaseinput-tlogrow-executing-job-press)

**Related reference**  

* [tCouchbaseInput](tcouchbaseinput "Queries the documents from the Couchbase database.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/couchbase/tcouchbaseinput-tlogrow-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tCouchbaseConnection to open its Basic settings view.
2. Click the Edit schema button to open the schema editor.
   Define the following columns:

   * `callsign` of type
     String
   * `country` of type
     String
   * `iata` of type String
   * `icao` of type String
   * `id` of type Integer
   * `name` of type String
   * `type` of type String

   Make sure the column names are propagated to the Db
   column.
3. Click OK to save the schema.
4. In the Bucket field, enter the name of the bucket to
   query: `travel-sample`.
5. Select the Use N1QL query
   check box to define a complex query.
6. In the Query field, enter the following query:
   `` SELECT callsign, country, iata, icao, id, name, type FROM
   `travel-sample` WHERE country = "United States" and type = "airline" LIMIT
   5; ``
7. Double-click tLogRow to
   open its Basic settings view.
8. Next to Edit schema, click Sync
   columns.
9. In the Mode section, select Table (print
   values in cells of a table) to make the results easier to read
   in the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/couchbase/tcouchbaseinput-tlogrow-executing-job-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, the first 5 JSON documents where the
   country is `United States` and
   the type is `airline` are
   retrieved.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/couchbase/tcouchbaseinput-tlogrow-linking-components-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In Metadata, select your Couchbase connection and drop
   it onto the workspace.
2. In the Components dialog, select the
   tCouchbaseInput component. Note that the connection
   information in the component is automatically filled.
3. Drop tLogRow onto the workspace.
4. Link tCouchbaseInput to tLogRow
   using a Row > Main connection.
