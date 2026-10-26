<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-ai/clangchainmcpclient · versión 8.0 -->
# cLangChainMCPClient

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Connects and communicates with MCP servers using Large Language Models
(LLMs).

Information noteNote: This component is available only if you have installed the R2025-10 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Standard properties

These properties are used to configure cLangChainMCPClient running in
the Standard Route framework.

The Standard
cLangChainMCPClient component belongs to the AI family.

## Basic settings

| Properties | Description |
| --- | --- |
| Transport / Type | Select the transport type from:  * Stdio: The STDIO (Standard Input/Output) transport   method launches an MCP server as a sub-process and communicates with it   through standard input/output streams. This method is most suitable for   local execution. * Streamable HTTP: The Streamable HTTP transport   replaces the traditional HTTP+SSE transport for remote MCP server   communication. It operates over HTTP/HTTPS and allows for more flexible   server implementations. Information noteNote: This option is available only if you have   installed the R2025-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. * SSE: The SSE (Server-Sent Events) transport method   establishes a persistent connection with the MCP server over HTTP using SSE   for streaming communication. This method is suitable for remote execution. |
| Executable (for Stdio transport type only) | Enter the path to the executable on your local file system to launch the MCP server. |
| Arguments (for Stdio transport type only) | Enter the arguments for the executable as needed. |
| Event Streaming URL (for SSE transport type only) | Enter the URL of the MCP server. |
| Timeout(s) (for SSE transport type only) | Set a timeout period for the connection to the MCP server in seconds. |
| Connection | Select the cLangChainConnection component that connects to the language model. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Environments (for Stdio transport type only) | Set the environment variables in the table. Click [+] as many times as required to add parameters to the table. Then click the corresponding Value field and enter a value. |
| Log Events (for Stdio transport type only) | Select this checkbox to log the communications with the MCP server. |
| Headers (for SSE and Streamable HTTP transport types only) | Click the [+] button to add lines as needed and define the key and value for HTTP headers. For example, to include authentication information for MCP requests, you can add a line with `Authorization` in the key field and your credentials in the Value field. Information noteNote: This option is available only if you have installed the R2025-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Log Requests (for SSE and Streamable HTTP transport types only) | Select this checkbox to log requests to the MCP server. |
| Log Responses (for SSE and Streamable HTTP transport types only) | Select this checkbox to log responses from the MCP server. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cLangChainMCPClient can be a middle or end component in a Route. It has to be used with the cLangChainConnection component, which creates a connection to the language model. For more information about cLangChainConnection, see [cLangChainConnection](/talend/en-US/components/8.0/mediation-database/clangchainconnection). |
| Limitation | n/a |

**Related tasks**  

* [Communicating with local MCP server using OpenAI](communicating-with-local-mcp-server-using-openai)
