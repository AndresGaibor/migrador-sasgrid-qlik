<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprstreams/tmaprstreamsinput · versión 8.0 -->
# tMapRStreamsInput

Last updated: 9/30/2026

Transmits messages to the Job that runs transformations over these messages. Only
MapR V5.2 onwards is supported by this component.

### In this section

* [tMapRStreamsInput Standard properties](/talend/en-US/components/8.0/maprstreams/tmaprstreamsinput-standard-properties)
* [tMapRStreamsInput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/maprstreams/tmaprstreamsinput-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprstreams/tmaprstreamsinput-standard-properties -->
# tMapRStreamsInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tMapRStreamsInput running in the Standard Job framework.

The Standard
tMapRStreamsInput component belongs to the Internet family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Note that the schema of this component is read-only. It stores the messages sent from the message producer. |
| Output type | Select the type of the data to be sent to the next component.  Typically, using String is recommended, because tMapRStreamsInput can automatically translate the MapR Streams byte[] messages into strings to be processed by the Job. However, in case that the format of MapR Streams messages is not known to tMapRStreamsInput, such as *Protobuf*, you can select byte and then use a Custom code component such as tJavaRow to deserialize the messages into strings so that the other components of the same Job can process these messages. |
| Use an existing connection | Select this check box and from the list displayed select the relevant connection component to reuse the connection details you have already defined. |
| Distribution and Version | Select the MapR distribution to be used. Only MapR V5.2 onwards is supported by the MapRDB components.  If the distribution you need to use with your MapRDB database is not officially supported by this MapRBD component, that is to say, this distribution is MapR but is not listed in the Version drop-down list of this components or this distribution is not MapR at all, select Custom.   1. Select Import from existing    version to import an officially supported distribution as base    and then add other required jar files which the base distribution does not    provide. 2. Select Import from zip to    import the configuration zip for the custom distribution to be used. This zip    file should contain the libraries of the different Hadoop elements and the index    file of these libraries.  Note that custom versions are not officially supported by    Talend    .     Talend     and its community provide you with the opportunity to connect to    custom versions from Talend Studio but cannot guarantee that the configuration of whichever version you choose    will be easy, due to the wide range of different Hadoop distributions and    versions that are available. As such, you should only attempt to set up such a    connection if you have sufficient Hadoop experience to handle any issues on your    own.  Information noteNote: In this dialog box, the active check box must be kept    selected so as to import the jar files pertinent to the connection to be    created between the custom distribution and this component.  For a step-by-step example about how to connect to a custom    distribution and share this connection, see [Hortonworks](/talend/r/en-US/8.0/hortonworks). |
| Topic name | Enter the name of the topic from which tMapRStreamsInput receives the feed of messages. You must enter the name of the stream to which this topic belongs. The syntax is *path\_to\_the\_stream:topic\_name*. |
| Consumer group ID | Enter the name of the consumer group to which you want the current consumer (the tMapRStreamsInput component) to belong.  This consumer group will be created at runtime if it does not exist at that moment. |
| Reset offsets on consumer group | Select this check box to clear the offsets saved for the consumer group to be used so that this consumer group is handled as a new group that has not consumed any messages. |
| New consumer group starts from | Select the starting point from which the messages of a topic are consumed.  In MapR Streams, the increasing ID number of a message is called *offset*. When a new consumer group starts, from this list, you can select beginning to start consumption from the oldest message of the entire topic, or select latest to wait for a new message.  Note that the consumer group takes into account only the offset-committed messages to start from.  Each consumer group has its own counter to remember the position of a message it has consumed. For this reason, once a consumer group starts to consume messages of a given topic, a consumer group recognizes the latest message only with regard to the position where this group stops the consumption, rather than to the entire topic. Based on this principle, the following behaviors can be expected:   * If you are resuming an existing consumer group, this option determines the   starting point for this consumer group only if it does not already have a committed   starting point. Otherwise, this consumer group starts from this committed starting   point. For example, a topic has *100* messages. If   an existing consumer group has successfully processed 50 messages, and has committed   their offsets, then the same consumer group restarts from the offset *51*. * If you create a new consumer group or reset an existing consumer group, which, in   either case, means this group has not consumed any message of this topic, then when   you start it from latest, this new group starts and waits for the offset *101*. |
| Auto-commit offsets | Select this check box to make tMapRStreamsInput automatically save its consumption state at the end of each given time interval. You need to define this interval in the Interval field that is displayed.  Note that the offsets are committed only at the end of each interval. If your Job stops in the middle of an interval, the message consumption state within this interval is not committed. |
| Stop after a maximum total duration (ms) | Select this check box and in the pop-up field, enter the duration (in milliseconds) at the end of which tMapRStreamsInput stops running. |
| Stop after receiving a maximum number of messages | Select this check box and in the pop-up field, enter the maximum number of messages you want tMapRStreamsInput to receive before it automatically stops running. |
| Stop after maximum time waiting between messages (ms) | Select this check box and in the pop-up field, enter the waiting time (in milliseconds) by tMapRStreamsInput for a new message. If tMapRStreamsInput does not receive any new message when this waiting time meets its end, it automatically stops running. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Consumer properties | Add the MapR Streams consumer properties you need to customize to this table. |
| Timeout precision(ms) | Enter the time duration in millisecond at the end of which you want a timeout exception to be returned if no message is available for consumption.  The value *-1* indicates that no timeout is set. |
| Load the offset with the message | Select this check box to output the offsets of the consumed messages to the next component. When selecting it, a read-only column called *offset* is added to the schema. |
| Custom encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link. When the MapR Streams topic it needs to use does not exist, you can first create this topic using either the tMapRStreamsCreateTopic component or your MapR command-line interface. |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
