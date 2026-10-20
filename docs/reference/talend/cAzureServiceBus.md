<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-azure-service-bus/cazureservicebus · versión 8.0 -->
# cAzureServiceBus

Last updated: 9/30/2026

Sends messages to, or consumes messages from Azure Service Bus.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

Information noteNote: This component is available only if you have installed the
R2025-06 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cAzureServiceBus Standard properties

These properties are used to configure cAzureServiceBus running in
the Standard Route framework.

The Standard
cAzureServiceBus component belongs to the Connectivity family.

## Basic settings

| Connection | Select a connection to be used for handling messages. |
| Topic or Queue name | Type in the topic name or the queue name depending on the Service Bus Type configuration to send message to or consume message from. |
| Service Bus Type | Select the service bus type of connection from Queue and Topic. |

## Advanced settings

| Parameters | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding value field and enter a value. See the site <https://camel.apache.org/components/latest/azure-servicebus-component.html> for available options. |

## Usage

| **Usage rule** | cAzureServiceBus can be a start, middle or end component in a Route. It has to be used with the cAzureConnection component, which creates a connection to Azure Service Bus. For more information about cAzureConnection, see [cAzureConnection](https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-azure-event-hubs/cgooglepubsub). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Sending messages to and receiving messages from Azure Service Bus](sending-messages-to-and-receiving-messages-from-azure-service-bus)
