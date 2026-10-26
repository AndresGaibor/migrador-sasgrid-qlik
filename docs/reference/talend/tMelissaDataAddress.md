<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/melissa-data-address-standardization/tmelissadataaddress · versión 8.0 -->
# tMelissaDataAddress

Last updated: 9/30/2026

Verifies if an address is properly formatted and corrects any formatting or
spelling errors in each row.

This address management component is the result of 
Talend
 collaboration with Melissa Data, one of the world
leaders for global address validation.

For more information about the enterprise and its software tools, visit <http://www.melissadata.com/>.

tMelissaDataAddress validates, corrects and standardizes Canadian and
United States addresses. It iterates on each row and reads all input addresses against a
Melissa Data Data file.

tMelissaDataAddress uses the June 2017 release of the AddressObject library from Melissa Data.

The Data Quality Suite from Melissa Data
and the data used to validate addresses are updated regularly but the AddressObject library has not been modified since June 2017.

Information noteImportant:
tMelissaDataAddress works with data from a Melissa
Data installer of 2023-05 or before. If you installed data from 2023-06 onwards, the Job
fails.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMelissaDataAddress Standard properties

These properties are used to configure tMelissaDataAddress running in the Standard Job framework.

The Standard
tMelissaDataAddress component belongs to the Data Quality family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description, it defines the number of fields to be   processed and passed on to the next component. The schema is either   Built-in or stored remotely in the   Repository. * Built-in: You create the schema and   store it locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already created   the schema and stored it in the Repository. You can reuse it in various   projects and Job designs. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Input address | Click the [+] button to add lines to the table.  Click on Address field and select from the predefined list the fields that hold the input address data.  The component will map the values of these fields to the input columns you set in the table.  Click on Input Column and select from the list the columns from the input schema that hold the input address data. |
| Output address | Use this table to add extra columns to the output.  Click the [+] button to add lines to the table.  Click on Address field and select from the predefined list the fields that hold the output address data.  The component will map the values of these fields to the output columns you set in the table.  Click on Output Column and select from the list the columns from the output schema that will hold the extra information. |
| Specify your MelissaData license | Enter the Melissa Data license key provided by Melissa Data when you order the Data Quality Suite or the Address Object API.  To enter a key, click the […] button next to the field.  This software key unlocks the full functionality of Address Object.  For more information, visit <http://www.melissadata.com/> and download the Reference Guide for Address Object from the Support Center of MelissaData.  If your GeoCoder license has expired, you can use it in demo mode. This means that you can only process records from Nevada. Records from other states return a *GE03 (Demo Mode)* code in the *RESULTS\_CODE* column. |
| Specify your MelissaData DataFile folder | Set the path to the MelissaData Data folder provided by MelissaData and installed locally. You can also enter a path to a shared folder.  You must order and download the Data Quality Suite or the Address Object API from <http://www.melissadata.com/>. |

## Advanced settings

| Properties | Description |
| --- | --- |
| GeoCoder Licensing Agreement | Select the license you purchased:   * No Melissa GeoCoder License Was   Purchased  When you use a license for Address only, select this setting. * The Melissa GeoPoint License Was   Purchased * The Melissa GeoCoder License Was   Purchased   You cannot check the license validity at the initialization of the component. |
| tStat Catcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |

**Related tasks**  

* [Editing addresses against a Melissa Data data file](editing-addresses-against-melissa-data-data-file "This Job uses the tFixedFlowInput component to generate the address data to be analyzed, the tMelissaDataAddress component to analyze the input schema and validate, correct, and standardize the US addresses generated by the tFixedFlowInput component and a tLogRow component to output the correct formatted addresses on the console.")
