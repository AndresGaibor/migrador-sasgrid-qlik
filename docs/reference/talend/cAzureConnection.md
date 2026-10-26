<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-azure-event-hubs/cazureconnection · versión 8.0 -->
# cAzureConnection

Last updated: 9/30/2026

Establishes a connection to Azure Portal.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cAzureConnection Standard properties

These properties are used to configure cAzureConnection running in
the Standard Route framework.

The Standard
cAzureConnection component belongs to the Connectivity family.

## Basic settings

| Connection Type | Select the authentication type to connect to Azure Portal from:  * Connection String: Provide the namespace created   in Azure Portal, the shared access key name and its value for your Azure   account. The shared access key can be generated through the Azure portal. * Passwordless: Provide the namespace only. |
| Namespace Name | Enter the name of the namespace created in Azure Portal. |
| Shared Access Key Name | Enter the name you chose for your SAS key. |
| Shared Access Key | Enter the generated value for your SAS key. |

## Usage

| **Usage rule** | cAzureConnection can be added directly in a Route without any input or output component linked. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Sending messages to and receiving messages from Azure Service Bus](sending-messages-to-and-receiving-messages-from-azure-service-bus)
