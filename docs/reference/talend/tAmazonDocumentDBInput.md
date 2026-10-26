<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-documentdb/tamazondocumentdbinput · versión 8.0 -->
# tAmazonDocumentDBInput

Last updated: 9/30/2026

Retrieves records from a collection in the Amazon DocumentDB database and transfers them to
the following component for display or storage.

tAmazonDocumentDBInput retrieves certain
documents from an Amazon DocumentDB database collection by supplying a query document containing
the fields the desired documents should match.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tAmazonDocumentDBInput Standard properties

These properties are used to configure tAmazonDocumentDBInput running in the Standard Job framework.

The Standard
tAmazonDocumentDBInput component belongs to the Cloud family.

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
| Schema and Edit Schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.  Click Guess schema to retrieve the table schema. |
| Address type | Select the address type from the drop-down list:  * Standalone: Define the standalone Amazon DocumentDB   database server you want to connect to. * Replica set: Define a set of multiple Amazon   DocumentDB database servers you want to connect to in the   ReplicaSet address table. |
| Host and Port | Enter the IP address and listening port of the database server. |
| Database | Enter the name of the Amazon DocumentDB database. |
| Need auth | Select this check box to enable the database authentication. Among the mechanisms listed on the Auth mechanism drop-down list, select either Negotiate, which is recommended because it automatically select the most adapted authentication mechanism, or SCRAM-SHA-1 SASL, or SCRAM-SHA-256.  Select the Use auth database check box to enter the name of the authentication database in which the username to be used to connect to Amazon DocumentDB has been created and enter the database user authentication data in the Username and Password fields.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only. |
| Use SSL connection | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you must specify the encryption information using one of these methods:  * If you want to centralize the connection information, set up the SSL   connection in Windows > Preferences >    Talend    > SSL and check the Enable SSL field in   the MongoDB connection configuration in   Metadata. * If you want to keep this information within the scope of this Job, use   the tSetKeystore component in the same Job. |
| Collection | Enter the name of the collection in the Amazon DocumentDB database. |
| Use query | Select this check box to retrieve data using query statements. You can enter the query statement in the Query field. |
| Mode | Select the type of target data to read between JSON and Text. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| Connection parameter | Specify additional connection properties for the Amazon DocumentDB connection you are creating. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | As a start component, tAmazonDocumentDBInput allows you to retrieve records from a collection in the Amazon DocumentDB database and transfer them to the following component for display or storage. |
