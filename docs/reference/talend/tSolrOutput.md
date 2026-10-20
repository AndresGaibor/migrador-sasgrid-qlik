<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/solr/tsolroutput · versión 8.0 -->
# tSolrOutput

Last updated: 9/30/2026

Inserts, upserts, or deletes data in a Solr core.

## tSolrOutput Standard properties

These properties are used to configure tSolrOutput running
in the Standard Job framework.

The Standard
tSolrOutput component belongs to the Business Intelligence family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0.1-R2024-09 Talend Studio monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| URL | Type in the URL address of the Solr server you want to access, for example, `http://localhost:8983/solr/`. |
| Required authentication | Select this check box if an authentication is required to access the Solr server. If so, enter the username and password in the corresponding Login and Password fields. Information noteNote: To enter a password, a token, or a client secret key, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the password, the token, or the secret key in the text field, and click OK. Note that you can enter either a JSON string in the pure password mode or a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. |
| Mode | Select one of the modes of operating the cluster of Solr modes:  * SolrCloud: If you select this automatic centralized   management mode, enter the Collection name (that   contains all cores) in the corresponding field. * User-Managed mode: If you select this manual   management mode, enter the Core name in the   corresponding field. Information noteNote:   + The Collection and     Core field values impact the schema of     this component. It is recommended to update the schema by clicking     the Sync columns button after setting these     fields.   + When retrieving collections, some of them might be displayed with     a .\_designer prefix: it means you must     configure this collection and publish it on Solr side in order for     it to be correctly displayed as a collection.   For more information on Solr clusters and their modes of operating, see [Solr Cluster Types](https://solr.apache.org/guide/solr/latest/deployment-guide/cluster-types.html). |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already created the schema   and stored it in the Repository.   You can reuse it in various projects and Job designs. For more   information about a component schema in its Basic   settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Sync columns | Click this button to retrieve the schema from the previous component. |
| Action | Select one of the following operations to be performed on the data:  * Insert: to insert one or more new records into   the Solr core. This action is rarely used in production environments as   it does not overwrite data, so multiple records with the same identifier   can be added. For more information, see [the Solr documentation](https://solr.apache.org/guide/solr/latest/indexing-guide/documents-screen.html#common-fields). * Upsert: to create new records or update (and   overwrite) existing records in the Solr core. * Delete: to delete one or more records in the Solr   core. For this action, complex queries are not supported. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |
| Max batch size | Set the maximum number of records allowed in each batch. |
| Connection timeout (ms) | Set the timeout period (in milliseconds) for the connector to establish a connection to the server. An error occurs if an attempt to establish a connection fails. |
| Receive timeout (ms) | Set the timeout period (in milliseconds) for receiving response data. An error occurs if no data is received when the read timeout period expires. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox. |
| NB\_LINE | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an end component of a data flow in your Job. It receives data from Row > Main link. |
