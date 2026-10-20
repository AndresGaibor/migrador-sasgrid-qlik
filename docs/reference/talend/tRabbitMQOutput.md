<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/rabbitmq/trabbitmqoutput · versión 8.0 -->
# tRabbitMQOutput

Last updated: 9/30/2026

Receives data from the preceding component as messages and adds the
messages to queues in the specified way.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tRabbitMQOutput Standard properties

These properties are used to configure tRabbitMQOutput running in the Standard Job framework.

The Standard
tRabbitMQOutput component belongs to the Internet family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file in which the properties are stored. The database connection related fields that follow are completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List click the relevant connection component to reuse the connection details you already defined. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component can have only one column with the name of message and the type of String. You need to add the column manually in the schema. |
| Host name | Enter the host name, for example, `localhost`. |
| Port | Enter the port number. The default is `5672`. |
| Username and Password | Enter the username and the password for accessing the message queue.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only. |
| Use TLS | Select this option to use TLS for the connection. |
| Exchange type | Select the exchange type from the drop-down list. Five options are provided: `Default`, `Direct`, `Topic`, `Fanout`, and `Headers`. See Exchanges and Exchange Types section of [AMQP 0-9-1 Model Explained](https://www.rabbitmq.com/tutorials/amqp-concepts.html) for related information. |
| Exchange name | Enter the exchange name in double quotation marks. |
| Routing key | Enter the routing key in double quotation marks. |
| Header properties | Add and customize message header properties.  To add a message header property, add a row in this field by clicking the plus button under the field and set the property values (that is, header key, header value, and header type) in the corresponding columns of the new row. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |
| Use virtual host | Select this option to use a virtual host for publishing messages. Specify the virtual host to be used by entering the virtual host name in the Virtual host name field.  Information noteNote: This option is available only when you have installed the 8.0.1-R2023-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Durable | Select this option to declare the durable property for the queues. See Queues section of [AMQP 0-9-1 Model Explained](https://www.rabbitmq.com/tutorials/amqp-concepts.html) for related information. |
| Auto Delete | Select this option to declare the Auto-delete property for the queues. See Queues section of [AMQP 0-9-1 Model Explained](https://www.rabbitmq.com/tutorials/amqp-concepts.html) for related information. |
| Use alternate exchange | Select this option to enable alternate exchange. In this case, you need to enter the alternate exchange name in the Alternate exchange name field.  This option is available if you select Direct, Topic, or Headers from the Exchange type drop-down list in the Basic settings view. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an output component and it always needs an incoming link. |
| Limitation | n/a |
