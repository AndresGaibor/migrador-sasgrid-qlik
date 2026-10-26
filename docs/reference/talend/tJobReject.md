<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/talend-cloud/tjobreject · versión 8.0 -->
# tJobReject

Last updated: 9/30/2026

Receives data rejected after task processing.

## tJobReject Standard properties

These properties are used to configure tJobReject running in the
Standard Job framework.

The Standard
tJobReject component belongs to the Talend Cloud family.

This component is available in Talend Cloud and
Talend Data Fabric
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

## Advanced settings

| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| **Usage rule** | This component is used with other components in the Talend Cloud family, especially with tJobLog to design Jobs. These Jobs (artifacts) can then be published to the web application and used to design task in Talend Management Console. |
