<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomconnection · versión 8.0 -->
# tMomConnection

Last updated: 9/30/2026

Opens a connection to the MQ Server for communication.

## tMomConnection Standard properties

These properties are used to configure tMomConnection running in
the Standard Job framework.

The Standard
tMomConnection component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Failover | Select this check box to use the ActiveMQ failover transport. For more information about the failover transport, see [Failover Transport Reference](http://activemq.apache.org/failover-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server drop-down list and the Static Discovery check box is cleared. |
| Static Discovery | Select this check box to use the ActiveMQ static transport discovery mechanism. For more information about the static transport, see [Static Transport Reference](http://activemq.apache.org/static-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list and the Failover check box is cleared. |
| URI parameters | Enter the URI parameters.  This field is available only when the Failover or Static Discovery check box is selected. |
| MQ server | Select the type of the MQ server(s) to be connected from the drop-down list, either ActiveMQ or WebSphere MQ. |
| Use SSL Transport | Select this check box to use the ActiveMQ SSL transport. For more information about the SSL transport, see [SSL Transport Reference](http://activemq.apache.org/ssl-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list. |
| Host | The host name or IP address of the MQ server. |
| Port | The listening port of the MQ server. |
| Username and Password | User authentication credentials.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use Transacted | Select this check box to set the session created to be transacted.  This check box is available only when ActiveMQ is selected from the MQ server drop-down list. |
| Channel | Specify the name of the channel through which the connection is established. The default value is *DC.SVRCONN*.  This field is available only when WebSphere MQ is selected from the MQ server drop-down list. |
| QueueManager | Specify the name of the queue manager to which the connection is established.  This field is available only when WebSphere MQ is selected from the MQ server drop-down list. |
| Use or register a shared Connection | Select this check box to share your connection or use a connection shared by a parent or child Job. This allows you to share one single connection among several connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail. |
| Shared Connection Name | Enter the shared connection name.  This field is available only when the Use or register a shared Connection check box is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional options | Define the additional transport options in the table. This table is available only when the Failover or Static Discovery check box in the Basic settings view is selected.   * Option name: the name of the   option. * Option value: the value of the   option.   For example, enter *maxReconnectAttempts* in the Option name field and then *0* in the Option value field so that no attempt is made to retry the connection when no server is available.  For more information about the failover transport options, see [Failover Transport Reference](http://activemq.apache.org/failover-transport-reference.html).  For more information about the static discovery transport options, see [Static Transport Reference](http://activemq.apache.org/static-transport-reference.html). |
| Set Cipher Suite | Select this check box to enable the Cipher Suite list from which you can specify the Cipher Suite to be used with WebSphere MQ SSL.  For further information about Cipher Suite, see [CipherSpecs and their equivalent CipherSuites supported by IBM WebSphere MQ](https://www.ibm.com/support/knowledgecenter/SSFKSJ_7.1.0/com.ibm.mq.doc/ja34740_.htm).  Available when WebSphere MQ is selected in the MQ Server list. |
| Custom Cipher Suite | Select this check box to allow you to customize Cipher Suite.  IBM Cipher Mappings: Use the IBM Java Cipher Suite to IBM MQ Cipher Spec Mappings.  Oracle Cipher Mappings: Use the Oracle Cipher Suite to IBM MQ Cipher Spec Mappings. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tMom\* components, especially with the tMomCommit and tMomRollback components. |
| Limitation | This component supports ActiveMQ and WebSphere MQ servers. |
