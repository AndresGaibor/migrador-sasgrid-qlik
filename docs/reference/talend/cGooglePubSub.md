<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-google-pubsub/cgooglepubsub · versión 8.0 -->
# cGooglePubSub

Last updated: 9/30/2026

Sends messages to, or consumes messages from Google Cloud Pub/Sub
service.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cGooglePubSub Standard properties

These properties are used to configure cGooglePubSub running in the
Standard Route framework.

The Standard
cGooglePubSub component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select a connection to be used for handling messages. |
| Destination name | Type in the subscription name for consumer or the topic name for producer. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Parameters | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding value field and enter a value. See the site <https://camel.apache.org/components/latest/google-pubsub-component.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cGooglePubSub can be a start, middle or end component in a Route. It has to be used with the cGCPConnection component, which creates a connection to Google Cloud Pub/Sub service. For more information about cGCPConnection, see [cGCPConnection](https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-google-pubsub/cgcpconnection). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Sending messages to and receiving messages from Google Cloud Pub/Sub service](sending-messages-to-and-receiving-messages-from-google-pubsub-service)
