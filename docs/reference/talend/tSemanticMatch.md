<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/semantic/tsemanticmatch · versión 8.0 -->
# tSemanticMatch

Last updated: 9/30/2026

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Enables semantic similarity search against a vector database using an input
column as the query vector.

## Semantic matching and traditional matching

Traditional duplicate detection relies on exact matches or pattern rules. For example,
finding records where "company name" is identical or within a Levenshtein distance of 2.

Semantic matching compares the meaning of data using vector embeddings. Two product
listings, one labeled "32-inch 4K smart television" and another "UltraHD smart TV 32 inch",
are semantically identical even though the text differs completely. Semantic matching
catches these fuzzy duplicates automatically without hard-coded rules.

Benefits of semantic matching:

* Handles synonyms: "car" and "automobile" match despite different words.
* Captures intent: "lightweight laptop" and "portable computer" are semantically
  similar.
* No rule maintenance: Uses learned representations instead of manual
  patterns.
* Scalable: Works with large datasets and complex product hierarchies.

## How tSemanticMatch works

tSemanticMatch performs the following workflow:

1. Takes an input record containing a search column; text or structured data.
2. Uses that column as a query vector to search a vector database for similar records.
3. Returns the closest matches along with similarity scores.
4. Outputs records based on a score threshold: records with scores above the threshold pass
   to the Flow output; records below the threshold are rejected.

The component outputs the original input columns, the matched record details, and a
similarity score for each match.

## Vector database integration

tSemanticMatch currently only integrates with Milvus, a high-performance vector database
optimized for similarity search. Milvus stores and indexes vector embeddings, allowing fast
retrieval of similar records at scale.

## Supported vector types

tSemanticMatch only supports FloatVector for semantic similarity search.
Sparse and binary vectors are not supported. You must provide or generate FloatVector as
input to the component. If you need to use a different vector type, convert it to
FloatVector before passing it to tSemanticMatch.

For example, you can use tEmbeddingAI to generate FloatVector embeddings
from text data for semantic search operations.

## Input and output schema

tSemanticMatch adds two columns to the input and Flow output
schema:

* `MATCH_RESULT`: The text or record content from the matching
  vector, retrieved using the configured text field name.
* `SCORE`: A similarity score (0.0-1.0) where 1.0 is a perfect
  match.

If no match is found or the score falls below the minimum threshold, the record is returned
in the Reject output.

## tSemanticMatch Standard Properties

These properties are used to configure tSemanticMatch running in the
Standard Job framework.

The Standard
tSemanticMatch component belongs to the AI
family.

Information noteNote: This component is available from Talend Studio 8.0
R2026-06.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Search column | The input column used as the query vector for searching. Select a column containing a FloatVector. This column's vector representation must be a FloatVector compatible with the vector field in the database. Sparse and binary vectors are not supported. |
| Vector DB | Select the vector database. |
| URI | Enter the endpoint URI in double quotes. For example, `http://milvus-server:19530` or `https://cloud-milvus.example.com`. |
| Token | Enter the authentication token or API key required by your database. Leave blank if it runs without authentication. |
| Database | Enter the name of the database containing your vector collection. |
| Collection | Select the collection that stores the vector embeddings and associated data. |
| Vector field | Select the field in the collection storing vector embeddings. |
| Text field | This setting is optional.  Select the field in the collection containing human-readable text or content. If specified, this text is returned in the `MATCH_RESULT` output column. If not specified, only the score is returned. |
| Max results | Enter the maximum number of matching records to return per input record. Set to 1 for single match. Increase for multiple matches. |
| Min score | Enter the minimum similarity score threshold. The value must be in the range 0.0-1.0.  Records with scores below this value are returned in the reject output. For example, 0.6 means only records 60% similar or better are accepted. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Primary key | Select the field that uniquely identifies each record in the collection. This value is returned in the output to allow you to trace matches back to source records. |
| Metadata filter | Select the checkbox to define filter conditions with an operator and a value. The available operators depend on the vector database, not Talend Studio.  The IN operator lets you define the exact values your data must match. For example: `price` IN `750,1000,1500` means that the value of the field price must be 750, 1000, or 1500. Any other value will be rejected. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox. |
