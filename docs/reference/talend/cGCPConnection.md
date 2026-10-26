<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-google-pubsub/cgcpconnection · versión 8.0 -->
# cGCPConnection

Last updated: 9/30/2026

Establishes a connection to Google Cloud Pub/Sub service for publishing and
consuming messages.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cGCPConnection Standard properties

These properties are used to configure cGCPConnection running in the
Standard Route framework.

The Standard
cGCPConnection component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Project ID | Enter your Google Cloud project ID. |
| Use Google Cloud Platform credentials file | To use credentials when interacting with Google Cloud Pub/Sub service, select this check box and enter the path to the credentials file in the Credentials file field. You can use classpath:, file:, or http: prefix to load your credential file. For example, ``` "file://D:/Downloads/data-ei-development-bfc76b337660.json" ```  ``` "classpath:data-ei-development-bfc76b337660.json" ``` Alternatively, you can clear the Use Google Cloud Platform credentials file check box and add a system variable named `GOOGLE_APPLICATION_CREDENTIALS` with the value of the path to your credentials file. Note that you need to restart Talend Studio after this system variable is added. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cGCPConnection can be added directly in a Route without any input or output component linked. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Sending messages to and receiving messages from Google Cloud Pub/Sub service](sending-messages-to-and-receiving-messages-from-google-pubsub-service)
