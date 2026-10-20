<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsaphanaunload · versión 8.0 -->
# tSAPHanaUnload

Last updated: 9/30/2026

Offloads massive data from the SAP HANA database to a third party system.

In this release, the tSAPHanaUnload component is in Technical Preview
and currently hidden. For more information about how to show it on the
Palette, see [Palette settings](/talend/r/en-US/8.0/studio-user-guide/palette-settings).

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSAPHanaUnload Properties

These properties are used to configure tSAPHanaUnload running in
the Standard framework.

The Standard
tSAPHanaUnload component belongs to the Databases family.

## Basic settings

| Property Type | Select either Built-In or Repository:  * Built-In: No property data stored centrally. * Repository: Select the repository file in which the   properties are stored. The database connection fields that follow are completed   automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Host | Enter the IP address or hostname of the database server. |
| Port | Enter the listening port number of the database server. |
| Database Schema | Enter the name of the database schema. |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Enter the name of the table from which the data will be read. |
| Export Location on the SAP HANA host | Enter the path where you want to store the exported data on the SAP HANA server. |

## Advanced Settings

| Additional JDBC Parameters | Specify additional JDBC properties for the connection you are creating. The properties are separated by ampersand & and each property is a key-value pair. For example, *ssl=true & sslfactory=com.amazon.redshift.ssl.NonValidatingFactory*, which means the connection will be created using SSL. |
| Replace the previous exported data | Select the check box if you want to replace previously exported data with a new version. |
| Export database catalog only | Select the check box if you only want to export the database catalog. |
| Do not export underlying dependencies of an export object | Select the check box if you want to ensure that underlying dependencies of an export object are excluded from exporting. |
| Export no statistics | Select the check box if you wish to exclude exporting any data statistics objects. |
| Data & metadata for data statistics objects are exported | Select the check box to export all data and metadata for data statistics objects. |
| Strips attributes that can be reconstructed at input time from the export data | Select the check box to strip attributes, which may reduce the size of the export file. |
| Obfuscate CSV exported data | Select this option to make the string data of the structure of your database export unrecognizable or difficult to interpret. |
| Optional seed (at least 8 to 10 characters) | Specify the character to be scrambled in your data. |
| Thread size | Specify the number of process threads to be used for concurrent exporting. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| **Usage rule** | This component is currently in Technical Preview and hidden. To retrieve it, go to Project Settings > Designer > Palette Settings > Standard > Databases.  tSAPHanaUnload exports data to the SAP HANA server. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
