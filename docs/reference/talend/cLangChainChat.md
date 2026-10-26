<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-ai/clangchainchat · versión 8.0 -->
# cLangChainChat

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Interacts with Large Language Models (LLMs) supported by LangChain4j.

Information noteNote: This component is available only if you have installed the R2025-07 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Standard properties

These properties are used to configure cLangChainChat running in the
Standard Route framework.

The Standard
cLangChainChat component belongs to the AI
family.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select the cLangChainConnection component that connects to the language model. |
| Chat with Memory | Select this check box to enable memory management. |
| Type | Select the memory backend type. This option is available when Chat with Memory is selected. Supported values are MessageWindowChatMemory, EnhancedChatMemory (Relational Database), and EnhancedChatMemory (NoSQL). |
| Max Messages | Set the maximum number of messages retained in MessageWindowChatMemory. This option is available when Type is MessageWindowChatMemory. For more information, see <https://docs.langchain4j.dev/tutorials/chat-memory>. |
| Conversation Retention (Turns, 0 = All) | Specify how many conversation turns are retained. Set `0` to retain all turns. This option is available when Type is EnhancedChatMemory (Relational Database) or EnhancedChatMemory (NoSQL). |
| Enable Session TTL | Select this check box to enable session expiration. This option is available when Type is EnhancedChatMemory (Relational Database) or EnhancedChatMemory (NoSQL). |
| Session TTL (Minutes) | Set the session time-to-live in minutes. This option is available when Enable Session TTL is selected. |
| Touch Session On Write | Select whether writes refresh the session TTL. This option is available when Enable Session TTL is selected. |
| Lazy Cleanup Batch Size | Set the maximum number of expired sessions processed per lazy cleanup trigger. This option is available when Enable Session TTL is selected. |
| SQL Connection | Select the external SQL connection used by enhanced relational memory. This option is available when Type is EnhancedChatMemory (Relational Database). |
| DB Type | Select the NoSQL database type. This option is available when Type is EnhancedChatMemory (NoSQL). |
| MongoDB Connection | Enter the MongoDB connection URI. This option is available when Type is EnhancedChatMemory (NoSQL) and DB Type is MongoDB. |
| Memory ID Header Name | Specify the request header name used as the session or memory identifier. The default value is X-Session-Id. This option is available when Chat with Memory is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cLangChainChat can be a start, middle or end component in a Route. It has to be used with the cLangChainConnection component, which creates a connection to the language model. For more information about cLangChainConnection, see [cLangChainConnection](/talend/en-US/components/8.0/mediation-database/clangchainconnection). |
| Limitation | n/a |

**Related tasks**  

* [Interacting with OpenAI](interacting-with-openai)
