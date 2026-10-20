<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/talend-cloud/tjoblog · versión 8.0 -->
# tJobLog

Last updated: 9/30/2026

Collects and shows exception data during the execution of the Job in Talend Studio or the task in Talend Management Console.

## tJobLog Standard properties

These properties are used to configure tJobLog running in the Standard Job
framework.

The Standard
tJobLog component belongs to the Talend Cloud family.

This component is available in Talend Cloud and
Talend Data Fabric
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Level | Developer: Select this option to provide log information to the developer to analyze or debug the execution of the Job in Talend Studio.  User: Select this option to provide log information to the web user regarding the execution of the task that uses the Job. |
| Log message | Enter the Javaexpression of the log message you want to show to the developer to debug the execution of the Job, or to the web user to debug the execution of the task in Talend Management Console.  This field also supports HTML tags, which allows for HTML-style messages. The following figure gives an example.    The following gives the log message yielded.  ``` First Line Second Line Third Line ``` |
| Priority | Select the type of the log message from the Priority list.  You can select to display the message as an error message, a fatal error, a warning and so on. |

## Advanced settings

| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| **Usage rule** | This component is used with other components in the Talend Cloud family, especially with tJobLog to design Jobs. These Jobs (artifacts) can then be published to the web application and used to design task in Talend Management Console. |
