<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/tpineconeclient · versión 8.0 -->
# tPineconeClient

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Upserts, queries, fetches, updates, or deletes records in Pinecone index
namespaces.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

For a quick introduction on using this component in your Job, see the
following video:

## tPineconeClient Standard properties

These properties are used to configure tPineconeClient running
in the Standard Job framework.

The Standard
tPineconeClient component belongs to the AI family.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its   Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Sync columns | Click this button to retrieve the schema from the preceding component. |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| API Key | Enter the Pinecone API key in this field.  To enter the raw key, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the key in the text field, and click OK. You can also use a context variable in that field.  For more information on how to find your Pinecone API Key, see [Authentication](https://docs.pinecone.io/guides/get-started/authentication). |
| Host | Enter the IP address of the Pinecone database in this field, or click the [...] button next to the corresponding field to retrieve it.  You can also use a context variable in that field. |
| Operation | Select the operation you want to perform to the incoming data and data records in the Pinecone database table:  * Upsert: Creates new records and overwrites   existing records in the specified index namespace. * Query: Retrieves the IDs of the most similar   records in the index, along with their similarity scores. You need to   specify the number of results to return in the Top   K field, knowing that this number is linked to the number   of existing records: if you enter 7 in that field and the database only   contains 5 records, you will get 5 records. * Fetch: Fetches records by ID from the specified   index namespace. * Update: Updates existing records in the specified   index namespace. * Delete: Removes records from the specified index   namespace. If you need to apply this action on all the records of the   specified namespace, select the Delete all check   box that is displayed. * Get index stats: Gets the details of a Pinecone   index.  For more information on these data operations, see [Data](https://docs.pinecone.io/guides/data/upsert-data). |
| Namespace | Enter the name of the Pinecone index namespace on which you want to apply the data operations. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |
| Max batch size | Set the maximum number of records allowed in each batch.  For more information on these data operations, see [Upsert limits](https://docs.pinecone.io/guides/data/upsert-data#upsert-limits). |
| API version | Specify the version of the Pinecone API to be used in your requests.  For more information on API versioning, see [Specifying an API version](https://docs.pinecone.io/reference/api/versioning#specifying-an-api-version). |
| Filter | Specify a filter expression to be used when querying the Pinecone index.  For more information on filter expressions, see [Filter with metadata](https://docs.pinecone.io/guides/data/filter-with-metadata). |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer. |

**Related tasks**  

* [Indexing phone reviews with embeddings and vector database](tembeddingai-tpineconeclient-tmap-indexing-phone-reviews-with-embeddings-and-vector-db "This Job reads phone review text files from a folder, splits the content into smaller chunks for better analysis, generates vector embeddings using Azure OpenAI, and stores them in a Pinecone vector database to enable semantic search.")
