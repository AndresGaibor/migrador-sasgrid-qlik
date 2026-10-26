<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-wmq/cwmq · versión 8.0 -->
# cWMQ

Last updated: 9/30/2026

Exchanges messages between a Route and a JMS provider using WMQ.

cWMQ sends messages to, or consumes messages from, a
JMS Queue or Topic using the WebSphere broker.

## cWMQ Standard properties

These properties are used to configure cWMQ running in the Standard Job framework.

The Standard
cWMQ component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| URI/Type | Select the messaging type, either queue or topic. |
| URI/Destination | Type in a name for the message queue or topic in the message broker. |
| ConnectionFactory | Select a WMQ connection factory to be used for handling messages from the drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| MQ Properties | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding value field and enter a value. See the site <http://camel.apache.org/jms.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cWMQ can be a start, middle or end component in a Route. It has to be used with the cMQConnectionFactory component, which creates a connection to a MQ server. For more information about cMQConnectionFactory, see [cMQConnectionFactory](/talend/en-US/components/8.0/mediation-amqp/cmqconnectionfactory). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules).  To run the Route using the cWMQ component in Talend Studio, you need to download the *com.ibm.mq.jar*, *com.ibm.mq.commonservices.jar*, *com.ibm.mq.headers.jar*, *com.ibm.mq.jmqi.jar* and *connector.jar* from the IBM web site and add them to the Dependencies list of the cMQConnectionFactory. For more information about cMQConnectionFactory, see [cMQConnectionFactory](/talend/en-US/components/8.0/mediation-amqp/cmqconnectionfactory).  To run the Route using the cWMQ component in *Talend Runtime*, before deploy the Route, you need to download *com.ibm.mq.osgi.java\_7.5.0.5.jar* from the IBM web site and add it to the <TalendRuntimePath>/container/deploy folder. Alternatively, copy the *com.ibm.mq.jar*, *com.ibm.mq.commonservices.jar*, *com.ibm.mq.headers.jar*, *com.ibm.mq.jmqi.jar* and *connector.jar* to the <TalendRuntimePath>/container/lib/ext folder and change <TalendRuntimePath>/container/etc/custom.properties by adding the MQ packages to org.osgi.framework.system.packages.extra:  ``` org.osgi.framework.system.packages.extra = \     com.ibm.mq; \     com.ibm.mq.constants; \     com.ibm.mq.exits; \     com.ibm.mq.headers; \     com.ibm.mq.headers.pcf; \     com.ibm.mq.jmqi; \     com.ibm.mq.pcf; \     ... ``` |
