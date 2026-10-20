<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/talend-cloud/tjobfailure · versión 8.0 -->
# tJobFailure

Last updated: 9/30/2026

Throws an exception and prompts a message when an error
occurs.

## tJobFailure Standard properties

These properties are used to configure tJobFailure running in the Standard Job framework.

The Standard
tJobFailure component belongs to the Talend Cloud family.

This component is available in Talend Cloud and
Talend Data Fabric
products.

Information noteNote: tJobFailure is not supported in Jobs deployed in ESB Runtime.

## Basic settings

| Properties | Description |
| --- | --- |
| Error Type | You can define the error type according to your needs and the value you define in this field will be displayed when you run the task in Talend Management Console. |
| Error Message | Set the java expression of the error message in this field. The error message you define here should correspond to the error type you set in the Error Type field. |

## Advanced settings

| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| **Usage rule** | This component is used with other components in the Talend Cloud family, especially with tJobLog to design Jobs. These Jobs (artifacts) can then be published to the web application and used to design task in Talend Management Console. |
