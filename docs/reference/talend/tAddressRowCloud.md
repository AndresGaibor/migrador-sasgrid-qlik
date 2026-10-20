<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud · versión 8.0 -->
# tAddressRowCloud

Last updated: 9/30/2026

Verifies and formats international addresses in the Cloud by using online
services.

tAddressRowCloud enables you to parse address data and get formatted
addresses quickly, accurately and without installing any software.

Address data is corrected against the latest online reference data from several providers
including Loqate, MelissaData, Google or QAS. tAddressRowCloud
proposes alternatives for missing address data such as country or postal code, and
addresses are enriched with other elements such as latitude longitude.

For further information about the terms of services of Google
Places API, see [Terms of Service](https://developers.google.com/maps/terms?hl=en).

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tAddressRowCloud Standard properties

These properties are used to configure tAddressRowCloud running in the Standard Job framework.

The Standard
tAddressRowCloud component belongs to the Data Quality family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click the [...] button and define the input and output schema of the address data.  The output schema of tAddressRowCloud proposes several read-only address columns including a VerificationLevel column which provides you with a verification status of the processed address. The verification levels in this column are defined by  Talend . For further information, see [Address verification levels in tAddressRowCloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the).  As the output schema depends on the address provider, visit its website for further information.  Also some of the output columns could be empty depending on what address provider you select in the component basic settings when executing the Job. |
| Address Provider | Select from the list the provider of the reference data against which you want to validate and format input addresses.  The list of address providers includes Google, Loqate, QAS and MelissaData. |
| License/API key | Enter the license or the API key provided by the address provider you select from the list. You must visit the provider website, register and get the license/API key.  To enter a key, click the […] button next to the field.  When you select Google as a provider, the component uses the Google Places API. You must generate the key from the Google Developer Console at <https://developers.google.com/console/help/new/> and set the key in this field. |
| Processing Mode | This option is applied only to the Loqate provider.  Select from the list the mode of address validation you want to have:  * Verify and Geocode   (selected by default): with this mode, the component   standardizes and corrects addresses and enriches them with   latitude and longitude information. You must define the   address and country columns in the input schema and add them   to the Mapping table. * Verify   only: with this mode, the component   standardizes and corrects addresses without enriching them   with latitude and longitude information.  You must define the address column in the input schema and   add it to the Mapping table.  Information noteNote: These processing modes cost extra credits. For further information, see the [Loqate website](https://www.loqate.com/). |
| Country | This option is applied only to the QAS provider.  Select from the list the country corresponding to your input addresses.  When you select QAS as a provider, the component uses the QAS Pro OnDemand service. For further information about Experian address verification, see the product sheet at <https://www.edq.com/globalassets/product-sheets/address-verification.pdf>. |
| QAS OnDemand username | This option is applied only to the QAS provider.  Enter the username you can find in the license provided by QAS.  You can check your username from the QAS OnDemand portal. |
| Password | This option is applied only to the QAS provider.  Enter the password you can find in the license provided by QAS.  You can check your password from the QAS OnDemand portal. |
| Use security mode to connect | Select this check box to connect to the Cloud in a secure mode. This may have a slight impact on performance.  This check box is not available with all address providers. |
| Mapping | Address field: add lines to the table and select from a predefined address list the fields that will hold input addresses.  The address list includes the following columns for all address providers: Address, PostalCode, Locality, AdministrativeArea and Country.  Input Column: add lines to the table and select from the list the columns that hold addresses from input schema. The input schema can have one or multiple columns and can have columns that do not represent address data. |
| Use Additional Output | This option is not available for the QAS provider.  Select this check box and use the Output Mapping table to add more address columns to the output schema:  Address field: add lines to the table and select from a predefined address list the fields of the extra information you want to output.  These predefined address fields vary according to the provider you select from the Address Provider list. For further information about the additional address fields, check the provider website.  Output Column: select from the list the columns that will hold the additional addresses information. You must first add these additional columns to the tAddressRowCloud output schema through the Edit Schema button.  tAddressRowCloud maps the values of the address fields to the output columns in the Output Column.  If you select to have an output column in the Output Address table that has the exact name of an input column, the input column value will be overwritten by the value given by the component. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component.  This component enables you to create a data flow, using a Row > Main link, and to create a reject flow with a Row > Reject link filtering the data in error. |

**Related concepts**  

* [Parsing addresses against reference data in the Cloud](taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-reference-data-in-cloud-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the -->
# Address verification levels in tAddressRowCloud

Last updated: 9/30/2026

The tAddressRowCloud component
outputs a VerificationLevel column. This column lists
the address verification levels defined by 
Talend
.

The providers which are supported in the component (Loqate, Melissadata
and so on) have different verification levels as these providers use different databases
and different algorithms to verify addresses. The results of address verification of the
providers are mapped to 
Talend
 verification levels.

The below table describes the verification levels that are output by the
component.

| Verification levels | Description |
| --- | --- |
| Verified | A complete match is made between the input data and a single record from the available reference data. |
| Partially Verified | A complete match is made between the input data and a single record from the available reference data. |
| Unverified | A partial match is made between the input data and a single record from the available reference data. |
| Ambiguous | More than one close reference data match is found. |
| Conflict | More than one close reference data match is found with conflicting values. |
| Reverted | The record can not be verified with a minimum acceptable level. Output fields will contain input data. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-reference-data-in-cloud-standard-component-enterprise-this -->
# Parsing addresses against reference data in the Cloud

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes a three-component Job that:

* uses the tFixedFlowInput
  component to generate the address data to be analyzed,
* uses the tAddressRowCloud
  component to parse, standardize and format the addresses in the Cloud through
  the Address Validation API,
* uses a tFileOutputExcel
  component to output the correct formatted addresses in an .xls file.

You must have internet connection to be able to use tAddressRowCloud.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise)
* [Parsing addresses against Loqate](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-loqate-standard-component-enterprise)
* [Configuring the output component and executing the Job](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise)
* [Parsing addresses against MelissaData](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-melissadata-standard-component-enterprise-you-can)
* [Parsing addresses against Google](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-google-standard-component-enterprise-you-can)
* [Parsing addresses against QAS](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-qas-standard-component-enterprise-you-can)

**Related reference**  

* [tAddressRowCloud](taddressrowcloud "Verifies and formats international addresses in the Cloud by using online services.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view in the Component tab.
2. Create the schema through the Edit Schema
   button.

   In the open dialog box, click the [+]
   button and add the columns that will hold the information in the input
   address, in this example: *Address* and
   *Country*.
3. Click OK.

   An *address* and a *country* columns
   are created in the Inline Table.
4. In the Number of rows field, set the
   number of rows as *1*.
5. In the Mode area, select the Use Inline Table option.
6. In the Content table, enter the address
   data you want to analyze, for example:

   ```
   "1 Chemin de l'Abbaye, Paris"
   "1 Rue de l'Abbaye, Paris"
   "1 Place de l'Abbaye basset, Paris"
   ```

   Set the country for the three address lines to
   *FRA*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise -->
# Configuring the output component and executing the Job

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileOutputExcel
   component to display the Basic settings
   view and define the component properties.
2. Set the destination file name as well as the sheet name and then select
   the Define all columns auto size check
   box.
3. Save your Job and press F6 to execute
   it.

   The tAddressRowCloud component uploads
   data to the cloud, retrieves the corrected data and writes the result in the
   output file.
4. Right-click the output component and select Data
   Viewer to display the formatted address data.

   tAddressRowCloud matches input address
   data against the Loqate repository.

   The *all\_info* and *Geo\_info*
   columns retrieve additional address information from the
   *Raw\_Response* and *GeoAccuracy*
   columns respectively in the Loqate repository. The
   *Raw\_Response* column provides you with all address
   information from the provider repository without any formatting. if you want
   this information to be more readable, you must parse it using json or
   xml.

   The STATUS output column returns
   the OK status for all address rows. This means that
   the verification process of all address rows could be completed successfully by the
   component. For further information about process status, see [Process status in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the).

   The VerificationLevel output column
   provides you with a verification status of the processed addresses. For
   further information, see [Verification status](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-verification-status-standard-component-enterprise-the).

   The AddressVerificationCode output column
   returns a verification code for each of the processed address rows. For
   example, the first verification code V44-I45-P3-100
   means:

   * Verification status = V (verified): a complete match was made
     between the input address and a single record from the available
     reference data.
   * Post-processed verification match level = 4 (premises): the level
     to which the input data matches the available reference data once
     all changes and additions performed during the verification process
     have been taken into account.
   * Pre-processed verification match level = 4 (premises): the level
     to which the input data matches the available reference data prior
     to any changes or additions performed during the verification
     process.
   * Parsing status = I (identified and parsed): all components of the
     input data have been able to be identified and placed into output
     fields.
   * Lexicon identification match level = 4 (premises): using pattern
     matching, a numeric value or word has been identified as a premises
     number or name.
   * Context identification match level = 5 (delivery point, PostBox or
     SubBuilding): a numeric value or word has been identified as a post
     box number or sub building name.
   * Postcode Status = P3 (added): the primary postal code for the
     country has been added.
   * Match score = 100 (complete similarity): the input data and
     closest reference data match completely.

   For further information about what values this code is made up of and the
   implications of each segment, see [Address verification codes in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-google-standard-component-enterprise-you-can -->
# Parsing addresses against Google

Last updated: 9/30/2026

## About this task

You can run the [Parsing addresses against reference data in the Cloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-reference-data-in-cloud-standard-component-enterprise-this) Job against
Google Places API by doing the followings:

## Procedure

1. In the tFixedFlowInput
   Basic settings, create the schema through
   the Edit Schema button.

   In the open dialog box, click the [+]
   button and add one column that will hold the information in the input
   address, in this example: *address*.
2. Click OK.

   An *address* column is created in the Inline Table.
3. In the Inline Table table, enter the
   address data you want to analyze, for example:

   ```
   "1211 AVENUE OF AMERICAS FL 8 10036 NEW YORK USA"
   "B69 2lt 9kings   United Kingdom ave"
   "1729号 黄兴路 China, 200433"
   "15 Rue Nelaton   Paris PARIS 92800 France"
   "1211 AVENUE OF AMERICAS FL 8 10036 NEW YORK"
   "1 Rue de l'Abbaye, Paris"
   "1 Chemin de l'Abbaye, Paris"
   "1 Place de l'Abbaye basset, Paris"
   "8000 Cummings Hall,Hanover,New Hampshire,03755,"
   ```
4. In the basic settings of tAddressRowCloud, select Google
   from the Address Provider list.
5. In the License/API key field, enter the
   API key you generate from the Google Developer Console at <https://developers.google.com/console/help/new/>.
6. In the Mapping table, click the [+]
   button to add a line and then select Address.

   The component will map the values of this field to the input column you
   set in this table.
7. If required, select the Use Additional
   Output check box and use the Output
   Mapping table to retrieve additional address information from
   the provider repository.

   For further information, see [Defining additional address fields](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-defining-additional-address-fields-standard-component-enterprise-if).
8. In the Advanced settings view, set
   Output Script to FRENCH and leave the other parameters unchanged.
9. Save your Job and press F6 to execute
   it.

   The tAddressRowCloud component uploads
   data to the cloud, retrieves the corrected data and writes the result in the
   output file.
10. Right-click the output component and select Data
    Viewer to display the formatted address data.

    tAddressRowCloud matches input address
    data against Google Places API and writes formatted addresses in the output
    file.

    The VerificationLevel output column
    provides you with a verification status of the processed addresses. For
    further information, see [Address verification levels in tAddressRowCloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-loqate-standard-component-enterprise -->
# Parsing addresses against Loqate

Last updated: 9/30/2026

### In this section

* [Setting the schema and defining address mapping](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-schema-and-defining-address-mapping-standard-component-enterprise)
* [Defining additional address fields](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-defining-additional-address-fields-standard-component-enterprise-if)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-melissadata-standard-component-enterprise-you-can -->
# Parsing addresses against MelissaData

Last updated: 9/30/2026

## About this task

You can run the [Parsing addresses against reference data in the Cloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-reference-data-in-cloud-standard-component-enterprise-this) Job against
Melissadata repository by doing the followings:

## Procedure

1. In the tFixedFlowInput
   Basic settings, create the schema through
   the Edit Schema button.

   In the open dialog box, click the [+]
   button and add one column that will hold the information in the input
   address, in this example: *address*.
2. Click OK.

   An *address* column is created in the Inline Table.
3. In the Inline Table table, enter the
   address data you want to analyze, for example:

   ```
   "1211 AVENUE OF AMERICAS FL 8 10036 NEW YORK USA"
   "B69 2lt 9kings   United Kingdom ave"
   "1729号 黄兴路 China, 200433"
   "15 Rue Nelaton   Paris PARIS 92800 France"
   "1211 AVENUE OF AMERICAS FL 8 10036 NEW YORK"
   ```
4. In the basic settings of tAddressRowCloud, select MelissaData from the Address
   Provider list.
5. In the License key/KPI key field, enter
   the license key provided by MelissaData.
6. In the Mapping table, click the [+] button to add a line and then select
   Address.

   The component will map the values of this field to the input column you
   set in this table.
7. If required, select the Use Additional
   Output check box and use the Output
   Mapping table to retrieve additional address information from
   the provider repository.

   For further information, see [Defining additional address fields](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-defining-additional-address-fields-standard-component-enterprise-if).
8. Leave the parameters in the Advanced
   settings view unchanged.
9. Save your Job and press F6 to execute
   it.

   The tAddressRowCloud component uploads
   data to the cloud, retrieves the corrected data and writes the result in the
   output file.
10. Right-click the output component and select Data
    Viewer to display the formatted address data.

    tAddressRowCloud matches input address
    data against the MelissaData data repository and writes formatted addresses
    in the output file.

    The AddressVerificationCode output column returns a
    verification code for each of the processed address rows. These codes are
    written in comma-delimited lists. Each code consists of two letters followed
    by two numbers. These codes indicate different statuses and errors. For
    example, the *AC02* code means that the state name is
    corrected based on the combination of city name and zip code.

    For a complete list of the meaning of the result codes and for further
    information about all the output columns, see the Address Object Reference
    Guide you can download from the Support Center of MelissaData at<http://www.melissadata.com/>.

    The VerificationLevel output column
    provides you with a verification status of the processed addresses. For
    further information, see [Address verification levels in tAddressRowCloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-qas-standard-component-enterprise-you-can -->
# Parsing addresses against QAS

Last updated: 9/30/2026

## About this task

You can run the [Parsing addresses against reference data in the Cloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-reference-data-in-cloud-standard-component-enterprise-this) Job using the
QAS Pro OnDemand service and verifiy the accuracy and completeness of
addresses.

## Procedure

1. In the tFixedFlowInput
   Basic settings, create the schema through
   the Edit Schema button.

   In the open dialog box, click the [+]
   button and add one column that will hold the information in the input
   address, in this example: *address*.
2. Click OK.

   An *address* column is created in the Inline Table.
3. In the Inline Table table, enter the
   address data you want to analyze, for example:

   ```
   "1 nonsense st, nowhereville, SC,11111"
   "14 elmwood,rome,ga,30161"
   "300 n quincy pl, charlestown,MA,02129"
   "reba st,pelion,SC,29123"
   "1445 montebello st,montebello,90640"
   "43400 gadsden ave,lancaster,ca,93534"
   "po box 123,san francisco,ca,94104"
   "43400 gadsden ave apt 3,lancaster,ca,93534"
   ```
4. In the basic settings of tAddressRowCloud, select QAS
   from the Address Provider list.
5. From the Country list, select the country
   corresponding to your input addresses, *United States* in
   this example.
6. In the QAS OnDemand username and
   password fields, enter respectively
   your username and password you can find in the license provided by
   QAS.
7. In the Mapping table, click the [+] button to add a line and then select
   Address.

   The component will map the values of this field to the input column you
   set in this table.
8. Leave the parameters in the Advanced
   settings view unchanged.
9. Save your Job and press F6 to execute
   it.

   The tAddressRowCloud component uploads
   data to the cloud, validates and retrieves the corrected data and writes the
   result in the output file.
10. Right-click the output component and select Data
    Viewer to display the formatted address data.

    tAddressRowCloud validates input address
    data against QAS Pro OnDemand and writes formatted addresses in the output
    file.

    The VerificationLevel output column
    provides you with a verification status of the processed addresses. For
    further information, see [Address verification levels in tAddressRowCloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tAddressRowCloud and tFileOutputExcel.
2. Connect the three components together using the Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-defining-additional-address-fields-standard-component-enterprise-if -->
# Defining additional address fields

Last updated: 9/30/2026

## Procedure

1. If required, select the Use Additional
   Output check box to retrieve additional address information
   from the provider repository.
2. Click the Edit schema button to open the
   schema dialog box and add in the output schema the columns which will hold
   the extra address information. Add all\_info
   and Geo\_info columns for this
   example.
3. In the Output Mapping table:
   * Use the [+] button to add lines
     in the table.
   * Click in the Address Field column
     and select from the predefined list the additional address fields
     you want to add to the output schema.
   * Click in the Output Column column
     and select from tAddressRowCloud
     output schema the columns that will hold the additional address
     information.

   The component maps the values of the address fields in the Loqate
   repository to the output columns you set in the table.
4. Set the parameters in the Advanced
   settings view according to your needs.

   The default parameters are not changed for this example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-schema-and-defining-address-mapping-standard-component-enterprise -->
# Setting the schema and defining address mapping

Last updated: 9/30/2026

## Procedure

1. Double-click tAddressRowCloud to display
   the Basic settings view and define the
   component properties.
2. If required, click Sync columns to
   retrieve the schema defined in the input component.
3. Click the Edit schema button to open the
   schema dialog box.

   tAddressRowCloud proposes several
   predefined read-only address columns as shown in the below capture.

   The STATUS column returns the status of
   processing input addresses. For further information about process status,
   see [Process status in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the).

   The AddressVerificationCode column
   returns the verification code for the processed address. For further
   information about what values this code is made up of and the implications
   of each segment, see [Address verification codes in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the).
4. Move any of the input columns to the output schema according to your
   needs, click OK and accept to propagate the
   changes.

   You can also add columns directly in the output schema to retrieve
   additional address information from the Loqate repository.
5. Select from the Address Provider list the
   provider of the reference data against which you want to validate and format
   input addresses, Loqate in this
   example.
6. Select the Use security mode to connect
   check box to connect to the provider repository in a secure mode. 

   This may have a slight impact on performance.
7. In the License/API key field, enter the
   license key provided by Loqate.
8. From the Processing Mode list,
   select:

   | Option | To... |
   | --- | --- |
   | Verify and Geocode (selected by default) | standardize and correct addresses and enrich them with latitude and longitude.  Information noteNote: Combining address verification and geocoding will cost extra credits. For further information, see [the Loqate pricing](https://loqate.com/en-us/pricing/). |
   | Verify only | standardize and correct addresses without enriching them with latitude and longitude. |
9. In the Mapping table:
   * Use the [+] button to add lines
     in the table.
   * Click in the Address Field column
     and select from the list predefined in the component the fields that
     hold the input address, Address and
     Country in this example.

     The component will map the values of these fields to the input
     columns you set in this table.

     tAddressRowCloud provides a list
     of individual fields because some countries have more complex
     addressing structures than others.
   * Click in the Input Column column
     and select from the list of the input schema the columns that hold
     the input address, address and
     country in this example.
