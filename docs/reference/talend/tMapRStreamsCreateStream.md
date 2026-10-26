<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprstreams/tmaprstreamscreatestream · versión 8.0 -->
# tMapRStreamsCreateStream

Last updated: 9/30/2026

Creates a MapR Streams stream or topic that the other MapR Streams components can
use.

This component allows you to visually issue the command to create or
update a stream or a topic.

## tMapRStreamsCreateStream Standard properties

These properties are used to configure tMapRStreamsCreateStream running in the Standard Job framework.

The Standard
tMapRStreamsCreateStream component belongs to the Internet family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored.  The properties are stored centrally under the Hadoop Cluster node of the Repository tree. |
| tMapRStreamsConnection | Select the tMapRStreamsConnection component to reuse the connection details you already defined. This parameter is mandatory for this component to connect to MapR Streams. |
| Action | Select how a stream or a topic is created. The related parameters to each action are displayed only when this action is selected.   * Create stream: it creates a   stream. If this stream exists already, the entire Job is   stopped. * Create stream if not exists:   it creates a stream when this stream does not exist. If this   stream exists, the Job skip the creation to move to the next   step. * Alter stream: it changes the   configuration of a stream. * Create topic: it creates a   topic. If this topic exists already, the entire Job is   stopped.  Note that the stream to which this topic belongs must already   exist. * Create topic if not exists:   it creates a topic when this topic does not exist. If this topic   exists, the Job skip the creation to move to the next   step.  Note that the stream to which this topic belongs must already   exist. * Alter topic: it changes the   configuration of a topic. |
| Stream path | Enter the path to the stream to be created or updated in MapR-FS. |
| Stream permissions | Grant the permissions to a user account over the stream to be created or updated. These permissions are about  * Adminperm * Consumeperm * Copyperm * Produceperm * Topicperm  The syntax you need to use is *u:username\_or\_userid\_of\_the\_account* within double quotation marks.  When you have selected Alter stream from the Action list, a list of check boxes are displayed in the Stream permissions area so that you can select the check box corresponding to each permission to be changed and then grant this permission to a different user account.  For details about these permissions, see MapR documentation at [MapR Streams Security](http://maprdocs.mapr.com/51/MapR_Streams/security.html). |
| Stream settings | Define the configuration of the stream to be created or updated. The parameters to be set are  * Automatic topic creation:   select the Enable automatic topic   creation check box to allow a topic to be   automatically created when a producer creates the first   message for it and this topic does not already exist.  For further information about this automatic creation, see MapR documentation at   [Topic Creation](http://maprdocs.mapr.com/51/MapR_Streams/creating_topics.html). * Default number of partitions:   this parameter defines how many partitions are created in each   new topic in a stream.  For further information about the default number of partitions, see MapR documentation at   [Default Partitions](http://maprdocs.mapr.com/51/MapR_Streams/default_number_of_partitions_in_new_topics.html). * Message time to live: this   parameters defines the length of time (in seconds) messages   persist in a stream.  For further information about this message survival time, see MapR documentation at   [Time-to-live for Messages](http://maprdocs.mapr.com/51/MapR_Streams/time_to_live_for_messages.html). * Compression: this is the type   of the compression algorithms MapR provides to compress files   stored in the MapR cluster.  For further information about MapR compression, see MapR documentation at   [Compression](http://maprdocs.mapr.com/home/AdministratorGuide/Compression.html).  When you have selected Alter stream from the Action list, a list of check boxes are displayed in the Stream settings area so that you can select the check box corresponding to each parameter to be changed and then update this parameter. |
| Topic name | Enter the name of the topic to be created.  This field is displayed when you have selected one of the actions about topics from the Action list. |
| Number of partitions or Set number of partitions | Enter the number of partitions to be created for the topic.  This field is displayed when you have selected one of the actions about topics from the Action list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used standalone to create or update a topic or a stream to be used by the other MapR Streams components. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
