<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/splunk/tsplunkeventcollector · versión 8.0 -->
# tSplunkEventCollector

Last updated: 9/30/2026

Sends the event data to Splunk through Splunk HTTP Event Collector.

tSplunkEventCollector collects and
sends the event data to Splunk.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSplunkEventCollector Standard properties

These properties are used to configure tSplunkEventCollector running in the Standard Job framework.

The Standard
tSplunkEventCollector component belongs to the Business Intelligence family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables.  Note that the schema of this component is empty by default, and   you need to click the [...] button next   to Edit schema to manually add fields.   The default metadata event fields needed for Splunk are the following:   + time (Date/Long/String type):     the event time. Note that the input data is in Java Date format, and     it will be transformed to the epoch time format required by Splunk     before sending to Splunk HTTP Event Collector.   + source (String type): the     source value of the event data. Usually the file or directory path,     network port, or script from which the event originated.   + sourcetype (String type): the     source type of the event data. It tells what kind of data it is.   + host (String type): the host of     the event data. Usually the host name, IP address, or fully qualified     domain name of the network machine from which the event     originated.   + index (String type): the name     of the index by which the event data is to be indexed. It must be     within the list of allowed indexes if the token has the *indexes* parameter set.The fields event metadata is not supported. For   more information about the format of the event data sent to Splunk HTTP Event   Collector, see [Format events for HTTP Event   Collector](https://docs.splunk.com/Documentation/Splunk/9.1.0/Data/FormateventsforHTTPEventCollector). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Server URL | Enter the URL used to access the Splunk Web Server. |
| Token | Specify the Event Collector token used to authenticate the event data. For more information, see [HTTP Event Collector token management](http://dev.splunk.com/view/event-collector/SP-CAAAE7C). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Max batch size | Enter the number of events to be processed in each batch.  By default, the number of events to be processed in each batch is `100`. If you do not want to process several events, enter `1`. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  RESPONSE\_CODE: the response code from Splunk. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an end component of a Job or subJob and it always needs an input link. |
