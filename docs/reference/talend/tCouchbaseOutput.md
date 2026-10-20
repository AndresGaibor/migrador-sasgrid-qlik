<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/couchbase/tcouchbaseoutput · versión 8.0 -->
# tCouchbaseOutput

Last updated: 9/30/2026

Upserts documents in the Couchbase database based on the incoming flat data from
preceding components.

This means that it adds a new document or replaces its value if it already exists.

## tCouchbaseOutput Standard properties

These properties are used to configure tCouchbaseOutput running in the Standard Job framework.

The Standard
tCouchbaseOutput component belongs to
the Databases NoSQL family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Bootstrap nodes | Enter the name or IP of the node to be bootstrapped by Couchbase SDK. As Couchbase recommends to specify multiple nodes to bootstrap, enter the names or IPs of these nodes in this field, separating them using commas (,).  For further information about Couchbase bootstrapping, see [How Couchbase SDKs connect to the cluster](https://developer.couchbase.com/documentation/server/4.1/developer-guide/connection-advanced.html).  You can find the node names on the Servers page in your Couchbase Web Console. If you need further information, contact the administrator of your Couchbase cluster or consult your Couchbase documentation.  Note that the Couchbase servers do not support proxies; for this reason, the Couchbase components from Talend do not support proxies either. |
| Username and Password | Provide the authentication credentials to your Couchbase cluster.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  If you are using Couchbase V5.0 and onwards, enter the same value you put in the Bucket field as password, because since Couchbase V5.0, no password is associated with a bucket. However, on Couchbase, you need to create a user with appropriate role to access the buckets.  For further information about the access control and other important requirements on the Couchbase side, see Couchbase release note of your version.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  When using non-JSON documents, define an `id` column of the String type, then define a `content` column. The type of this `content` column should be String for the string documents and byte[] for the binary documents.  When it comes to JSON documents, define the fields that exist in your JSON documents. |
| Bucket | Enter, within double quotation marks, the name of the data bucket in the Couchbase database.  Ensure that the credentials you are using have the appropriate rights and permissions to access this bucket.  If you are using Couchbase V5.0 and onwards, this bucket name is the user name you have created in the Security tab of your Couchbase UI. |
| Document type | Data stored in a Couchbase database could be JSON, strings or binary. From this drop-down list, select the type of the data you need to use with Couchbase.  Note that it is not recommended to mix JSON, binary and string documents in a same bucket, as this mixture could make the document processing error-prone. |
| Field to use as ID | Enter, without double quotation marks, the name of the column from the schema to provide IDs for the documents to be written to Couchbase. |
| Partial update | Select this check box to update only a subset of a document, without changing any other property that is not provided by the incoming data.  If you leave this check box, when a document already exists in the database, that is to say, when this document and a document from the incoming data have the same ID, the whole existing document is replaced with the incoming one. |
| Use N1QL Query with parameters | Select this check box to apply variables in your N1QL queries. Once selecting it, the Query field and the Query Parameters wraps flat data into documents for storage in the Couchbase database. table are displayed for you to enter your query and define the variables to be used in your query.  Only one query is allowed per tCouchbaseOutput.  For example, enter this query in the Query field: ``` INSERT INTO 'travel-sample' (KEY, VALUE) VALUES  ($nm,     {     "name":$nm,      "type":$tp,      "country":$cnty,      "callsign":$call,       "id":$zid    } ) ```  Then you need to define all of the variables (the strings starting with $) used in this query in the Query Parameters table.  ``` Query Parameter Name     Column nm                       name tp                       type cnty                     countries call                     company zid                      docid ```  This table creates a map between the variables in your query and the columns from the schema you have defined in the component for your data. The values in the Column column are the column names from this schema; the values in the Query Parameter Name column are the variables from your query. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Use custom connection parameters | Select this option to set connection parameters, including Connection timeout, Query timeout, Analytics timeout, and Query threshold.  To set a connection parameter, add a row in the Connection parameters table by clicking the plus button on the bottom of the table, click the Parameter name column and select the desired parameter from the drop-down list, and then enter the parameter value in the Parameter value column. |
| Use TLS | Select this option to enable TLS for securing data transferred. See [Couchbase TLS](https://docs.couchbase.com/operator/current/concept-tls.html) for related information.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Java Truststore | Enter the truststore file name. See [KeyStores and TrustStores](https://docs.oracle.com/cd/E19509-01/820-3503/ggffo/index.html) for related information.  Information noteNote: This option is available only when you select the Use TLS option. |
| Java Truststore password | Enter the password for the truststore file. See [Generating a KeyStore and TrustStore](https://docs.oracle.com/cd/E19509-01/820-3503/6nf1il6er/index.html) for related information.  Information noteNote: This option is available only when you select the Use TLS option. |
| Java Truststore type | Enter the Java truststore type, which defaults to `JKS`.  Information noteNote: This option is available only when you select the Use TLS option. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_SUCCESS: the number of rows successfully processed. This is an After variable and it returns an integer.  NB\_REJECT: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Preceded by an input component, tCouchbaseOutput |
