<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-documentdb/tamazondocumentdboutput · versión 8.0 -->
# tAmazonDocumentDBOutput

Last updated: 9/30/2026

Executes the action defined on the collection in the Amazon DocumentDB database.

tAmazonDocumentDBOutput inserts, updates, upserts or deletes
documents in an Amazon DocumentDB database collection based on the incoming flow from
the preceding component in the Job.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tAmazonDocumentDBOutput Standard properties

These properties are used to configure tAmazonDocumentDBOutput
running in the Standard Job framework.

The Standard
tAmazonDocumentDBOutput component belongs to the Cloud family.

Talend Studio is
compatible with Amazon DocumentDB 3.6 version.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

Information noteNote: This component is available only when you have installed the 8.0.1-R2022-02 Talend Studio Monthly
update or a later one delivered by Talend.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit Schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in. |
| Address type | Select the address type from the drop-down list:  * Standalone: define the standalone Amazon DocumentDB   database server you want to connect to. * Replica set: define a set of multiple Amazon   DocumentDB database servers you want to connect to in the   ReplicaSet address table. |
| Host and Port | Enter the IP address and listening port of the database server. These fields are available when the Use existing connection or Use replica set address check box are not selected.  These parameters are only available when you select the Standalone from the Address type drop-down list. |
| Database | Enter the name of the Amazon DocumentDB database. This parameter is only available when you select the Standalone from the Address type drop-down list. |
| Need auth | Select this check box to enable the database authentication. Among the mechanisms listed on the Auth mechanism drop-down list, select either Negotiate, which is recommended because it automatically select the most adapted authentication mechanism, or SCRAM-SHA-1 SASL, or SCRAM-SHA-256.  Select the Use auth database check box to enter the name of the authentication database in which the username to be used to connect to Amazon DocumentDB has been created and enter the database user authentication data in the Username and Password fields.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only. |
| Use SSL connection | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| Collection | Enter the name of the collection in the Amazon DocumentDB database. |
| Use query | Select this check box to retrieve data using query statements. You can enter the query statement in the Query field. |
| Mode | Select the type of target data to write between JSON and Text. |
| Set write concern | Select this check box to set the level of acknowledgment requested for write operations from the Write concern drop-down list. |
| Bulk write | Select this check box to insert, update, or remove data in bulk. |
| Data action | The following operations are available:  * Insert: insert documents. * Set: modifies the existing fields of an existing   document and appends a field if it does not exist in this document.  If you need to apply this action on all the documents in the collection to be   used, select the Update all document check box that   is displayed; otherwise, only the first document is updated. * Update: replaces the existing documents with the   incoming data but keeps the technical ID of these documents. * Upsert with set: inserts a document if it does   not exist otherwise it applies the same rules as Set  If you need to apply this action on all the documents in the collection to be   used, select the Update all document check box that   is displayed; otherwise, only the first document is updated. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| Max batch size | Set the maximum number of lines allowed in each batch. Do not change the default value unless you are facing performance issues. Increasing the batch size can improve the performance but a value too high could cause Job failures. |
| Connection parameter | Specify additional connection properties for the Amazon DocumentDB connection you are creating. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tAmazonDocumentDBOutput executes the action defined on the collection in the Amazon DocumentDB database based on the flow incoming from the preceding component in the Job. |
