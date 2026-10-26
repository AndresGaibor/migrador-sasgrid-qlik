<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-ai/clangchainconnection · versión 8.0 -->
# cLangChainConnection

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Manages connection to Large Language Models (LLMs) supported by LangChain4j.

Information noteNote: This component is available only if you have installed the R2025-07 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Standard properties

These properties are used to configure cLangChainConnection running
in the Standard Route framework.

The Standard
cLangChainConnection component belongs to the AI family.

## Basic settings

| Properties | Description |
| --- | --- |
| Language Model | Select the language model from Anthropic, Azure OpenAI, Bedrock, Github Models, Google AI Germini, Ollama, and OpenAI. Information noteNote: As of now, Google AI Gemini and Github Models are not fully supported. |
| Base URL | Type in the base URL address of the API server you want to access, by default it is `http://127.0.0.1/default`. This option is only available for Anthropic, Ollama, and OpenAI language models. |
| API Key | Enter the API key to access the language model. This option is only available for Anthropic, Azure OpenAI, Google AI Germini, and OpenAI language models. |
| Model Name | Enter the name of the model that will be used. This option is only available for Anthropic, Bedrock, Google AI Germini, Ollama, and OpenAI language models. |
| Endpoint | Enter the endpoint to access your language model service API. This option is only available for Azure OpenAI, and Github Models language models. |
| Deployment Name | Enter the deployment name in your language model. This option is only available for Azure OpenAIlanguage model. |
| Service Version | Enter the version of your language model. This option is only available for Azure OpenAI language model. |
| Region | Enter your region between double quotation marks, for example `"us-east-1"`. This option is only available for Bedrock language model. |
| Github Token | Enter the access token to your Github Models. This option is only available for Github Models language model. |
| Timeout (s) | Set the timeout period (in seconds) for the component to establish a connection to the server. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Temperature | Enter sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. |
| Max Retries | Define the number of retries before the Route fails. |
| Max (Completion) Tokens | The maximum number of tokens that can be generated in the chat completion. |
| Log Requests | Select this check box to log the requests to the language model. This option is only available for Anthropic, Ollama, and OpenAI language models. |
| Log Responses | Select this check box to log the responses from the language model. This option is only available for Anthropic, Ollama, and OpenAI language models. |
| Log Requests and Responses | Select this check box to log both the requests and the responses. This option is only available for Azure OpenAI, Github Models, and Google AI Germini language models. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cLangChainConnection can be added directly in a Route without any input or output component linked. |
| Limitation | n/a |

**Related tasks**  

* [Communicating with local MCP server using OpenAI](communicating-with-local-mcp-server-using-openai)
* [Interacting with OpenAI](interacting-with-openai)
* [Querying a user database using OpenAI](querying-a-user-database-using-openai)
