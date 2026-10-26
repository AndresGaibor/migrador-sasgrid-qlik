<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-seda/cvm · versión 8.0 -->
# cVM

Last updated: 9/30/2026

Produces and consumes messages asynchronously in different threads across
CamelContext. You can use this mechanism to communicate across Web
applications.

cVM provides asynchronous SEDA behavior, so that
messages are exchanged on a BlockingQueue and consumers are invoked
in a separate thread from the producer across CamelContext
instances.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cVM Standard properties

These properties are used to configure cVM running in the Standard Job framework.

The Standard
cVM component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| When using as a start component in a Route: |  |
| Name | Type in any string that uniquely identifies the endpoint. |
| Specify maximum capacity size | Select this check box to set the maximum number of messages that the SEDA queue can hold. Specify the number in the Size field. |
| Concurrent consumers | Specify the number of concurrent threads processing exchanges. |
| Wait for task to complete | Specify whether the caller should wait for the asynchronous task to complete or not before continuing. Select from Always, Never or IfReplyExpected. The default option is IfReplyExpected which means the caller will only wait if the message is Request-Reply based. For more information about this option, see the site <http://camel.apache.org/async.html>. |
| Timeout | Specify the time in milliseconds before a SEDA producer will stop waiting for an asynchronous task to complete. You can disable this option by using 0 or a negative value. |
| Use multiple consumers | Specifies whether multiple consumers are allowed. If enabled, you can use cVM for Publish-Subscribe messaging, which means you can send a message to the SEDA queue and have each consumer receive a copy of the message. When enabled, this option should be specified on every consumer endpoint. |
| Limit concurrent consumers | Whether to limit the number of concurrent consumers to the maximum of 500. By default, an exception will be thrown if a SEDA endpoint is configured with a greater number. |
| Block when full | Whether a thread that sends messages to a full SEDA queue will block until the queue's capacity is no longer exhausted. By default, an exception will be thrown stating that the queue is full. By enabling this option, the calling thread will block instead and wait until the message can be accepted. |
| Poll timeout | Specify the timeout in milliseconds used when polling. When a timeout occurs, the consumer can check whether it is allowed to continue running. Setting a lower value allows the consumer to react more quickly upon shutdown. |
| When using as a middle or end component in a Route: |  |
| Input endpoint name | Select this check box to enter the name of the corresponding consumer in the Name field. |
| Use Exist cVM | This option appears when the Input endpoint name check box is cleared. Click [...] and select the corresponding consumer in the dialog box. |
| Name | This option appears when the Input endpoint name check box is selected. Enter the name of the consumer in this field directly. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Arguments | This option is available only when cVM is used as a start component in the Route. Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/vm.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cVM is used as a start, middle, or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Using cSEDA, cVM and cDirect to produce and consume messages separately](cseda-cvm-ctimer-clog-using-cseda-cvm-and-cdirect-to-produce-and-consume-messages-separately)
