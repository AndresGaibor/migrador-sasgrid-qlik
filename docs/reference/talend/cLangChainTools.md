<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-ai/clangchaintools · versión 8.0 -->
# cLangChainTools

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Facilitates function calling from Large Language Models (LLMs) supported by
LangChain4j.

Information noteNote: This component is available only if you have installed the R2025-07 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Standard properties

These properties are used to configure cLangChainTools running in the
Standard Route framework.

The Standard
cLangChainTools component belongs to the AI family.

## Basic settings

| Properties | Description |
| --- | --- |
| Name | Enter a name for the tool. |
| Tags | Enter the tags for the tool. Routes that have the same tool tags will be grouped together. |
| Description | Enter a description for the tool. This option is only available for consumer Routes. |
| Connection | Select the cLangChainConnection component that connects to the language model. |

## Advanced settings

| Properties | Description |
| --- | --- |
| System Message | Enter the system messages to be sent to the language model. This option is only available for producer Routes. |
| Parameters | Set the optional parameters in the table. Click [+] as many times as required to add parameters to the table. Then click the corresponding Value field and enter a value. See the site <https://camel.apache.org/components/4.14.x/langchain4j-tools-component.html#_endpoint_options> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cLangChainTools can be a start, middle or end component in a Route. It has to be used with the cLangChainConnection component, which creates a connection to the language model. For more information about cLangChainConnection, see [cLangChainConnection](/talend/en-US/components/8.0/mediation-database/clangchainconnection). |
| Limitation | n/a |

**Related tasks**  

* [Querying a user database using OpenAI](querying-a-user-database-using-openai)
