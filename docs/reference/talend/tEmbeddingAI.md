<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/tembeddingai · versión 8.0 -->
# tEmbeddingAI

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Leverages embedding models to efficiently process data with
AI.

For a quick introduction on using this component in your Job, see the
following video:

## tEmbeddingAI Standard properties

These properties are used to configure tEmbeddingAI running in
the Standard Job framework.

The Standard
tEmbeddingAI component belongs to the AI
family.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| Platform | Select the platform used to embed your input data.  * If you are using Amazon Bedrock, only the [Amazon Titan Text Embedding v1 and   v2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) models are supported, and [the default credentials provider   chain](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-chain.html) authentication method is used, which means the access to the   AWS Service can be configured in a chain. * If you are using Google Vertex AI, the [Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)   authentication method is used, which means no additional parameters need to   be defined as credentials are automatically found based on the application   environment. * If you are using Hugging Face, the server exception   "Model thenlper/gte-large is currently loading" might   occasionally happen and is due to the fact that the model used is a [cold model](https://huggingface.co/docs/api-inference/supported-models). The error will   disappear at the next retry. * If you are using ONNX, you may get out-of-memory   errors as ONNX models are local and therefore memory-consuming. It is   recommended to set the JVM parameters to 2GB minimum in [the Job run profile](https://help.qlik.com/talend/en-US/remote-engine-user-guide-windows/cloud/job-run-profile). |
| Ali Bailian (DashScope) parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Dashscope platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| Amazon Bedrock parameters | * Model name: Click the [...] button next to the field to select the embedding model   of your choice. * Region: Click the [...]   button next to the field to select one of the Amazon multi-regional   locations you want to use. |
| Azure OpenAI parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Azure OpenAI platform. * Azure endpoint: Enter the endpoint to access your   Azure OpenAI service API. |
| Cohere parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Cohere platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| Google Vertex AI parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Location: Enter one of the Google Cloud   multi-regional locations you want to use. See [Vertex AI locations](https://cloud.google.com/vertex-ai/docs/general/locations) for more   information. * Google endpoint: Enter the appropriate regional   endpoint corresponding to your location. See [Vertex AI locations](https://cloud.google.com/vertex-ai/docs/general/locations) for more   information. * Google project ID: Enter your Google Cloud project   ID. See [Find your Google Cloud project ID](https://cloud.google.com/vertex-ai/docs/tutorials/tabular-bq-prediction/prerequisites#find-project-id)   for more information. Example:   `my-sample-project-370819` |
| Hugging Face parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Hugging Face platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| Mistral AI parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the [...]   button next to the field to enter the access token to your Mistral AI   platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| ONNX parameters | Select the Use local ONNX file checkbox to use a local tokenizer file. Specify the model and tokenizer paths, as well as the pooling mode to apply. If unselected, the default embedded tokenizer file will be used.  See [Introduction to ONNX](https://onnx.ai/onnx/intro/index.html) for more information. |
| Column for embedding | Select or enter the schema column you want to apply the embedding model on. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Base URL | Type in the base URL address of the API server you want to access. This option is available for the Ali Bailian, Cohere, Hugging Face, and Mistral AI platforms. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component or as a start component of a Job or subJob. |

**Related tasks**  

* [Indexing phone reviews with embeddings and vector database](tembeddingai-tpineconeclient-tmap-indexing-phone-reviews-with-embeddings-and-vector-db "This Job reads phone review text files from a folder, splits the content into smaller chunks for better analysis, generates vector embeddings using Azure OpenAI, and stores them in a Pinecone vector database to enable semantic search.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/tembeddingai-tpineconeclient-tmap-indexing-phone-reviews-with-embeddings-and-vector-db -->
# Indexing phone reviews with embeddings and vector database

Last updated: 9/30/2026

This Job reads phone review text files from a folder, splits the content into smaller chunks for better analysis, generates vector embeddings using Azure OpenAI, and stores them in a Pinecone vector database to enable semantic search.

## Before you begin

Before running this Job, ensure you have:

* An active Azure OpenAI account with access to the text-embedding-3-small model.
* Your Azure OpenAI API key and endpoint configured.
* A Pinecone account with an index created for storing embeddings.
* Your Pinecone API key and host endpoint configured.
* Downloaded the archive file
  [[tembeddingai-tpineconeclient\_phone-review-files.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tembeddingai-tpineconeclient_phone-review-files.zip)](/talend/en-US/components/8.0/Content/Resources/attachments/tembeddingai-tpineconeclient_phone-review-files.zip) and
  extracted the LG.txt and Iphones.txt
  files.
* Created the directory <folder\_path>/phone-reviews/ with the
  phone review text files.

## Linking the components

### Procedure

1. Drag and drop the following components from the Palette:
   tFileList, tFileInputRaw,
   tJavaFlex, tEmbeddingAI,
   tMap, tPineconeClient, and three
   tLogRow components.
2. Connect tFileList to tFileInputRaw
   using a Trigger > Iterate
   connection.
3. Connect tFileInputRaw to tJavaFlex
   using a Row > Main
   connection.
4. Connect tJavaFlex to the first
   tLogRow using a Row >
   Main connection.
5. Connect the tLogRow to
   tEmbeddingAI using a Row >
   Main connection.
6. Connect tEmbeddingAI to the second
   tLogRow using a Row >
   FLOW connection.
7. Connect tLogRow to tMap using a
   Row > Main connection.
8. Connect tMap to tPineconeClient
   using a Row > Main
   connection.
9. Connect tPineconeClient to the last
   tLogRow using a Row >
   FLOW connection.

## Configuring the components

### About this task

This Job processes phone review text files from a folder, splits the content into smaller chunks for better analysis and more precise semantic search, generates embeddings for each chunk, and stores them with metadata in Pinecone.

### Procedure

1. Double-click the tFileList component to open its
   Component view.
2. In the Basic settings tab, configure the following parameters:

   * In the Directory field, enter or select:
     `"<folder_path>/phone-reviews/"`
   * In the Files field, add a line and enter:
     `"*.txt"` to list all text files in the directory
     (LG.txt and Iphones.txt).
3. Click OK to close the component view.
4. Double-click the tFileInputRaw component to open its
   Component view.
5. In the Basic settings tab, configure the following parameters:

   * In the Filename field, enter: `((String)globalMap.get("tFileList_1_CURRENT_FILEPATH"))` to read each phone review file from the list.
6. Click Edit schema and verify the schema has the following column:

   * `chunk` (String)
7. Click OK to close the schema editor and OK to close the component view.
8. Double-click the tJavaFlex component to open its
   Component view.
9. In the Basic settings tab, configure the following:

   * Click Sync columns to retrieve the column schema
     from the previous component.
   * In the Start code field, enter the following code:

     ```
     //String regex = "(?:\\d(?:\\.\\d)?[A-Z]{5})\\b";
     //Pattern pattern = Pattern.compile(regex);
     int nbParts=2;
     ```
   * In the Main code field, enter the following code to
     convert byte content to string and split into smaller chunks:

     ```
      //System.out.println(part);
     String input = row7.content.toString();
     String[] lines = input.split("\\r?\\n");
     int nbLines=lines.length;
     int linesPerPart = nbLines / nbParts;
     int remainder = nbLines % nbParts;
     int linesProcessed = 0;
     //System.out.println("nb lines:"+nbLines); 
      for (int i = 0; i < nbParts; i++) {
                 StringBuilder partBuilder = new StringBuilder();
                 int linesInThisPart = linesPerPart + (remainder > 0 ? 1 : 0);
                 remainder--;
                 for (int j = 0; j < linesInThisPart; j++) {
                 partBuilder.append(lines[linesProcessed]).append(" ");
                 linesProcessed++;
                 }
                                
                 String body=partBuilder.toString();
                 row8.chunk=body;
                 //System.out.println("text:"+body);
                 globalMap.put("id",((String)globalMap.get("tFileList_1_CURRENT_FILE"))+i);
                 globalMap.put("chunk",body);
     ```

     Information noteNote: This code splits the phone
     review text into smaller chunks to facilitate better analysis and more
     precise semantic search in the vector database.
   * In the End code field, enter the following code:

     ```
     }
     ```
10. Click OK to close the component view.
11. Double-click the first tLogRow component to open its
    Component view.
12. Select Table in the Mode
    area.

    This component displays the chunked phone review text in the console as a
    table.
13. Double-click the tEmbeddingAI component to open its
    Component view.
14. In the Basic settings tab, configure the following parameters:

    * Click Edit schema and verify the schema has the
      following column: `embedding` (List).
    * In the Platform list, select Azure OpenAI.
    * In the Model name field, click the [...] button and select `text-embedding-3-small`.
    * In the Token/API Key field, click the [...] button and enter your Azure OpenAI API key, then click OK.
    * In the Azure endpoint field, enter your Azure OpenAI
      endpoint (for example:
      `https://your-resource-name.openai.azure.com/`).
    * In the Column for embedding list, select
      `chunk`.

    This component generates vector embeddings for each phone review text chunk.
15. Click OK to close the component view.
16. Double-click the second tLogRow component to open its
    Component view.
17. Select Table in the Mode
    area.

    This component displays the generated embeddings in the console.
18. Double-click the tMap component to open the Map
    Editor.
19. In the Map Editor, create the output schema with the following columns:

    * `id` (String)
    * `vector` (List) - Map it with the
      `embedding` input column
    * `text` (String)

    This mapping verifies that all metadata are correctly transferred to
    tPineconeClient. The `id` and
    `values` columns are required by Pinecone for upsert operations.
20. Click OK to close the Map Editor.
21. Double-click the tPineconeClient component to open its
    Component view.
22. In the Basic settings tab, configure the following parameters:

    * Click Edit schema and verify the schema has the
      following column: `upsertedCount` (Int).
    * In the API Key field, click the [...] button and enter your Pinecone API key, then click OK.
    * In the Host field, enter your Pinecone index host (for example: `"your-index-name.svc.environment.pinecone.io"`).
    * In the Operation list, select Upsert to load the vectorized phone review data into the Pinecone index.
    * In the Namespace field, enter the namespace name
      (for example: `phones"`) or leave empty to use the
      default namespace.
23. Click OK to close the component view.
24. Double-click the last tLogRow component to open its
    Component view.
25. Select Table in the Mode
    area.

    This component displays the upserted records in the console, confirming
    successful loading into Pinecone.

## Executing the Job

### Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to execute the Job.

### Results

The Job reads the phone review files, chunks the text, generates embeddings using Azure OpenAI, verifies metadata transfer through tMap, and upserts the vectorized data into Pinecone for semantic search.

The phone review embeddings stored in Pinecone enable semantic search queries, allowing users to find relevant reviews based on meaning and context rather than exact keyword matches. The text chunking ensures more precise search results and better analysis capabilities.

**Related reference**  

* [tPineconeClient](tpineconeclient "Upserts, queries, fetches, updates, or deletes records in Pinecone index namespaces.")

**Related information**  

* [tEmbeddingAI](/talend/en-US/components/8.0/embeddings-management-systems/tembeddingai)
* [tFileList](/talend/en-US/components/8.0/tfilelist/tfilelist)
* [tFileInputRaw](/talend/en-US/components/8.0/raw/tfileinputraw)
* [tJavaFlex](/talend/en-US/components/8.0/java-custom-code/tjavaflex)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/embeddings-management-systems/tembeddingai -->
# tEmbeddingAI

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Leverages embedding models to efficiently process data with
AI.

For a quick introduction on using this component in your Job, see the
following video:

## tEmbeddingAI Standard properties

These properties are used to configure tEmbeddingAI running in
the Standard Job framework.

The Standard
tEmbeddingAI component belongs to the AI
family.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| Platform | Select the platform used to embed your input data.  * If you are using Amazon Bedrock, only the [Amazon Titan Text Embedding v1 and   v2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) models are supported, and [the default credentials provider   chain](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-chain.html) authentication method is used, which means the access to the   AWS Service can be configured in a chain. * If you are using Google Vertex AI, the [Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)   authentication method is used, which means no additional parameters need to   be defined as credentials are automatically found based on the application   environment. * If you are using Hugging Face, the server exception   "Model thenlper/gte-large is currently loading" might   occasionally happen and is due to the fact that the model used is a [cold model](https://huggingface.co/docs/api-inference/supported-models). The error will   disappear at the next retry. * If you are using ONNX, you may get out-of-memory   errors as ONNX models are local and therefore memory-consuming. It is   recommended to set the JVM parameters to 2GB minimum in [the Job run profile](https://help.qlik.com/talend/en-US/remote-engine-user-guide-windows/cloud/job-run-profile). |
| Ali Bailian (DashScope) parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Dashscope platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| Amazon Bedrock parameters | * Model name: Click the [...] button next to the field to select the embedding model   of your choice. * Region: Click the [...]   button next to the field to select one of the Amazon multi-regional   locations you want to use. |
| Azure OpenAI parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Azure OpenAI platform. * Azure endpoint: Enter the endpoint to access your   Azure OpenAI service API. |
| Cohere parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Cohere platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| Google Vertex AI parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Location: Enter one of the Google Cloud   multi-regional locations you want to use. See [Vertex AI locations](https://cloud.google.com/vertex-ai/docs/general/locations) for more   information. * Google endpoint: Enter the appropriate regional   endpoint corresponding to your location. See [Vertex AI locations](https://cloud.google.com/vertex-ai/docs/general/locations) for more   information. * Google project ID: Enter your Google Cloud project   ID. See [Find your Google Cloud project ID](https://cloud.google.com/vertex-ai/docs/tutorials/tabular-bq-prediction/prerequisites#find-project-id)   for more information. Example:   `my-sample-project-370819` |
| Hugging Face parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the   [...] button next to the field to enter the access   token to your Hugging Face platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| Mistral AI parameters | * Model name: Click the [...]   button next to the field to select the embedding model of your choice. * Token/API Key: Click the [...]   button next to the field to enter the access token to your Mistral AI   platform.   You can fill the API server URL in the Base URL parameter of the Advanced settings. |
| ONNX parameters | Select the Use local ONNX file checkbox to use a local tokenizer file. Specify the model and tokenizer paths, as well as the pooling mode to apply. If unselected, the default embedded tokenizer file will be used.  See [Introduction to ONNX](https://onnx.ai/onnx/intro/index.html) for more information. |
| Column for embedding | Select or enter the schema column you want to apply the embedding model on. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Base URL | Type in the base URL address of the API server you want to access. This option is available for the Ali Bailian, Cohere, Hugging Face, and Mistral AI platforms. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component or as a start component of a Job or subJob. |

**Related tasks**  

* [Indexing phone reviews with embeddings and vector database](tembeddingai-tpineconeclient-tmap-indexing-phone-reviews-with-embeddings-and-vector-db "This Job reads phone review text files from a folder, splits the content into smaller chunks for better analysis, generates vector embeddings using Azure OpenAI, and stores them in a Pinecone vector database to enable semantic search.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/embeddings-management-systems/tembeddingai-tpineconeclient-tmap-indexing-phone-reviews-with-embeddings-and-vector-db -->
# Indexing phone reviews with embeddings and vector database

Last updated: 9/30/2026

This Job reads phone review text files from a folder, splits the content into smaller chunks for better analysis, generates vector embeddings using Azure OpenAI, and stores them in a Pinecone vector database to enable semantic search.

## Before you begin

Before running this Job, ensure you have:

* An active Azure OpenAI account with access to the text-embedding-3-small model.
* Your Azure OpenAI API key and endpoint configured.
* A Pinecone account with an index created for storing embeddings.
* Your Pinecone API key and host endpoint configured.
* Downloaded the archive file
  [[tembeddingai-tpineconeclient\_phone-review-files.zip](/talend/en-US/components/8.0/Content/Resources/attachments/tembeddingai-tpineconeclient_phone-review-files.zip)](/talend/en-US/components/8.0/Content/Resources/attachments/tembeddingai-tpineconeclient_phone-review-files.zip) and
  extracted the LG.txt and Iphones.txt
  files.
* Created the directory <folder\_path>/phone-reviews/ with the
  phone review text files.

## Linking the components

### Procedure

1. Drag and drop the following components from the Palette:
   tFileList, tFileInputRaw,
   tJavaFlex, tEmbeddingAI,
   tMap, tPineconeClient, and three
   tLogRow components.
2. Connect tFileList to tFileInputRaw
   using a Trigger > Iterate
   connection.
3. Connect tFileInputRaw to tJavaFlex
   using a Row > Main
   connection.
4. Connect tJavaFlex to the first
   tLogRow using a Row >
   Main connection.
5. Connect the tLogRow to
   tEmbeddingAI using a Row >
   Main connection.
6. Connect tEmbeddingAI to the second
   tLogRow using a Row >
   FLOW connection.
7. Connect tLogRow to tMap using a
   Row > Main connection.
8. Connect tMap to tPineconeClient
   using a Row > Main
   connection.
9. Connect tPineconeClient to the last
   tLogRow using a Row >
   FLOW connection.

## Configuring the components

### About this task

This Job processes phone review text files from a folder, splits the content into smaller chunks for better analysis and more precise semantic search, generates embeddings for each chunk, and stores them with metadata in Pinecone.

### Procedure

1. Double-click the tFileList component to open its
   Component view.
2. In the Basic settings tab, configure the following parameters:

   * In the Directory field, enter or select:
     `"<folder_path>/phone-reviews/"`
   * In the Files field, add a line and enter:
     `"*.txt"` to list all text files in the directory
     (LG.txt and Iphones.txt).
3. Click OK to close the component view.
4. Double-click the tFileInputRaw component to open its
   Component view.
5. In the Basic settings tab, configure the following parameters:

   * In the Filename field, enter: `((String)globalMap.get("tFileList_1_CURRENT_FILEPATH"))` to read each phone review file from the list.
6. Click Edit schema and verify the schema has the following column:

   * `chunk` (String)
7. Click OK to close the schema editor and OK to close the component view.
8. Double-click the tJavaFlex component to open its
   Component view.
9. In the Basic settings tab, configure the following:

   * Click Sync columns to retrieve the column schema
     from the previous component.
   * In the Start code field, enter the following code:

     ```
     //String regex = "(?:\\d(?:\\.\\d)?[A-Z]{5})\\b";
     //Pattern pattern = Pattern.compile(regex);
     int nbParts=2;
     ```
   * In the Main code field, enter the following code to
     convert byte content to string and split into smaller chunks:

     ```
      //System.out.println(part);
     String input = row7.content.toString();
     String[] lines = input.split("\\r?\\n");
     int nbLines=lines.length;
     int linesPerPart = nbLines / nbParts;
     int remainder = nbLines % nbParts;
     int linesProcessed = 0;
     //System.out.println("nb lines:"+nbLines); 
      for (int i = 0; i < nbParts; i++) {
                 StringBuilder partBuilder = new StringBuilder();
                 int linesInThisPart = linesPerPart + (remainder > 0 ? 1 : 0);
                 remainder--;
                 for (int j = 0; j < linesInThisPart; j++) {
                 partBuilder.append(lines[linesProcessed]).append(" ");
                 linesProcessed++;
                 }
                                
                 String body=partBuilder.toString();
                 row8.chunk=body;
                 //System.out.println("text:"+body);
                 globalMap.put("id",((String)globalMap.get("tFileList_1_CURRENT_FILE"))+i);
                 globalMap.put("chunk",body);
     ```

     Information noteNote: This code splits the phone
     review text into smaller chunks to facilitate better analysis and more
     precise semantic search in the vector database.
   * In the End code field, enter the following code:

     ```
     }
     ```
10. Click OK to close the component view.
11. Double-click the first tLogRow component to open its
    Component view.
12. Select Table in the Mode
    area.

    This component displays the chunked phone review text in the console as a
    table.
13. Double-click the tEmbeddingAI component to open its
    Component view.
14. In the Basic settings tab, configure the following parameters:

    * Click Edit schema and verify the schema has the
      following column: `embedding` (List).
    * In the Platform list, select Azure OpenAI.
    * In the Model name field, click the [...] button and select `text-embedding-3-small`.
    * In the Token/API Key field, click the [...] button and enter your Azure OpenAI API key, then click OK.
    * In the Azure endpoint field, enter your Azure OpenAI
      endpoint (for example:
      `https://your-resource-name.openai.azure.com/`).
    * In the Column for embedding list, select
      `chunk`.

    This component generates vector embeddings for each phone review text chunk.
15. Click OK to close the component view.
16. Double-click the second tLogRow component to open its
    Component view.
17. Select Table in the Mode
    area.

    This component displays the generated embeddings in the console.
18. Double-click the tMap component to open the Map
    Editor.
19. In the Map Editor, create the output schema with the following columns:

    * `id` (String)
    * `vector` (List) - Map it with the
      `embedding` input column
    * `text` (String)

    This mapping verifies that all metadata are correctly transferred to
    tPineconeClient. The `id` and
    `values` columns are required by Pinecone for upsert operations.
20. Click OK to close the Map Editor.
21. Double-click the tPineconeClient component to open its
    Component view.
22. In the Basic settings tab, configure the following parameters:

    * Click Edit schema and verify the schema has the
      following column: `upsertedCount` (Int).
    * In the API Key field, click the [...] button and enter your Pinecone API key, then click OK.
    * In the Host field, enter your Pinecone index host (for example: `"your-index-name.svc.environment.pinecone.io"`).
    * In the Operation list, select Upsert to load the vectorized phone review data into the Pinecone index.
    * In the Namespace field, enter the namespace name
      (for example: `phones"`) or leave empty to use the
      default namespace.
23. Click OK to close the component view.
24. Double-click the last tLogRow component to open its
    Component view.
25. Select Table in the Mode
    area.

    This component displays the upserted records in the console, confirming
    successful loading into Pinecone.

## Executing the Job

### Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to execute the Job.

### Results

The Job reads the phone review files, chunks the text, generates embeddings using Azure OpenAI, verifies metadata transfer through tMap, and upserts the vectorized data into Pinecone for semantic search.

The phone review embeddings stored in Pinecone enable semantic search queries, allowing users to find relevant reviews based on meaning and context rather than exact keyword matches. The text chunking ensures more precise search results and better analysis capabilities.

**Related reference**  

* [tPineconeClient](tpineconeclient "Upserts, queries, fetches, updates, or deletes records in Pinecone index namespaces.")

**Related information**  

* [tEmbeddingAI](/talend/en-US/components/8.0/embeddings-management-systems/tembeddingai)
* [tFileList](/talend/en-US/components/8.0/tfilelist/tfilelist)
* [tFileInputRaw](/talend/en-US/components/8.0/raw/tfileinputraw)
* [tJavaFlex](/talend/en-US/components/8.0/java-custom-code/tjavaflex)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
