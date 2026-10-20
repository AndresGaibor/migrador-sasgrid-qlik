<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow · versión 8.0 -->
# tLoqateAddressRow

Last updated: 9/30/2026

Parses, verifies, cleanses, standardizes, transliterates, and formats international
addresses.

tLoqateAddressRow enables you to parse structured or unstructured text
into labeled address, it automatically puts address components into the correct address
field. You can compare address data against reference data to ensure that it is accurate
and complete. You can correct spellings, add missing address data such as city, city area,
region, or postcode, and enrich address with other elements such as latitude longitude and
other relevant data.

This address management component is the result of Talend collaboration with Loqate, one of the world leaders for high quality,
accurate location information. For more information about the enterprise and its software
tools, see the [Loqate website](http://www.loqate.com/).

This component uses the Loqate Global Knowledge Repository containing definitive
address and geographic reference data for over 240 countries in multiple languages
and character sets.

tLoqateAddressRow uses the Q1.1.2020 release.

This component is not compatible with Java 17.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tLoqateAddressRow Standard properties

These properties are used to configure tLoqateAddressRow running in the Standard Job framework.

The Standard
tLoqateAddressRow component belongs to the Data Quality family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description, it defines the number of fields to be processed   and passed on to the next component. The schema is either Built-in or stored remotely in the Repository. * Built-in: You create the schema and store it   locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already created the schema   and stored it in the Repository. You can reuse it in various projects and job   designs. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Edit Schema | Click the [...] button and define the input and output schema of the address data.  Make sure to define in the output schema all columns necessary to output the formatted data you want to get from tLoqateAddressRow. |
| Input Address | Address field: add lines to the table and select from the component predefined list the fields that will hold the input address.  tLoqateAddressRow provides a long list of individual fields because some countries have more complex addressing structures than others. For further information about the input fields, see [Address fields in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-fields-in-tloqateaddressrow-standard-component-enterprise-some).  Input Column: add lines to the table and select from the list the columns that hold the input address. The input schema can have one or multiple columns and can have columns that do not represent address data. |
| Output Address | Address field: add lines to the table and select from the component predefined list the fields that will hold the output address. The component will map the values of these fields to the output columns you set in the table.  tLoqateAddressRow provides a long list of individual fields because some countries have more complex addressing structures than others. For further information about the output fields, see [Address fields in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-fields-in-tloqateaddressrow-standard-component-enterprise-some).  Output Column: add lines to the table and select from the list the columns that will hold the output address.  If you select to have an output column in the Output Address table that has the exact name of an input column, the input column value will be overwritten by the value given by tLoqateAddressRow.  In the output schema, there are two output standard columns that are read-only:  -STATUS: returns the status of processing input addresses. For further information about process status, see [Process status in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the).  -ACCURACYCODE: returns the verification code for the processed address. For further information about what values this code is made up of and the implications of each segment, see [Address verification codes in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the). |
| Loqate Data Path | Set the path to the Loqate Global Knowledge Repository provided by Loqate and installed locally.  You must order and download the Loqate Local API and the Global Knowledge Repository from [http:// www.loqate.com/](http://www.loqate.com/). tLoqateAddressRow uses the Q1.1.2020 release. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Server options | Set the server options as the following:  -Address Line Separator: define the string which will separate the output address components within the output address fields. The default separator is the line break string (<BR>).  -Default Country: select the country name for which the ISO 3166-1 alpha-3 code should be used when parsing data and if no identifiable country is found in an input record.  -Forced Country: select the country name for which the ISO 3166-1 alpha-3 code should be used for all input records when parsing data.  -Output Script: use this option to transliterate the output address.  Select Latin to encode the parsing results in Latin, or western characters.  Select Native to encode the parsing results using the country script.  Below is a list of the character sets (scripts) and languages tLoqateAddressRow can transliterate:  Latn - Latin (Western characters),  Cyrl - Cyrillic (Russia),  Grek - Greek (Greece)  Hebr - Hebrew (Israel),  Hani - Kanji (Japan),  Hans - simplified Chinese (China),  Arab - Arabic (United Arab Emirates),  Thai - Thai (Thailand),  Hang - Hangul (South Korea),  Native - output in the native script wherever possible.  -Minimum match score: specify the minimum match score a record must reach in order not to be reverted. The default value is zero, and valid values are between zero and 100.  This option is very helpful when you want to get, in the output fields, the input data if a specific level of verification (minimum match score) was not reached. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an intermediary step. It requires an input and output flows. |

**Related concepts**  

* [Parsing addresses against Loqate data](tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-loqate-data-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-loqate-data-standard-component-enterprise-this -->
# Parsing addresses against Loqate data

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes a three-component Job that:

* uses the tFixedFlowInput component
  to generate the address data to be analyzed,
* uses the tLoqateAddressRow
  component to parse, standardize and format the US addresses generated by the
  tFixedFlowInput component,
* uses a tFileOutputExcel component
  to output the correct formatted addresses in an .xsl file.

Before being able to use the tLoqateAddressRow component, you must order and download the Loqate Local
API and the Global Knowledge Repository from [http://
www.loqate.com/](http://www.loqate.com/). tLoqateAddressRow uses the
Q1.1.2020 release.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise)
* [Configuring the tLoqateAddressRow component](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-tloqateaddressrow-component-standard-component-enterprise)
* [Setting a JVM argument and finalizing the Job](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-jvm-argument-and-finalizing-job-standard-component-enterprise)

**Related reference**  

* [tLoqateAddressRow](tloqateaddressrow "Parses, verifies, cleanses, standardizes, transliterates, and formats international addresses.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-fields-in-tloqateaddressrow-standard-component-enterprise-some -->
# Address fields in tLoqateAddressRow

Last updated: 9/30/2026

Some countries have more complex addressing structures than others. As such, the use of
individual fields in this component will vary based on the input country and the available
reference data.

The table below lists all input and output fields in tLoqateAddressRow. The field that can be used on input is designated as [in] ,
[out] designates a field that may be present on output, and [in,out] designates that a field
can be used for both input and output.

| Field name | Description |
| --- | --- |
| Address [in,out] | specifies the full mailing address in the relevant country. |
| Address1, Address2, ... Address12 [in,out] | specifies input data for the address line in the relevant country, split into individual address lines. |
| DeliveryAddress [out] | specifies the full address including line breaks without the Organization, Locality, AdministrativeArea and PostalCode fields. |
| DeliveryAddress1, DeliveryAddress2...DeliveryAddress12 [out] | specifies the individual lines contained within the DeliveryAddress field. |
| Country [in] | provides the country name or code. |
| CountryName [out] | provides the ISO 3166 official country name. |
| ISO3166-2 [out] | provides the ISO 3166 2-character country code. |
| ISO3166-3 [out] | provides the ISO 3166 3-character country code. |
| ISO3166-N [out] | provides the ISO 3166 3-digit numeric country code. |
| SuperAdministrativeArea [in,out] | provides the largest geographic data element within a country. |
| AdministrativeArea [in,out] | provides the most common geographic data element within a country. For example, USA State, and Canadian Province. |
| SubAdministrativeArea [in,out] | provides the smallest geographic data element within a country. For example, USA County. |
| Locality [in,out] | provides the most common population center data element within a country. For example, USA City, Canadian Municipality. |
| DependentLocality [in,out] | provides a smaller population center data element, dependent on the contents of the Locality field. For example, Turkish Neighborhood. |
| DoubleDependentLocality [in,out] | provides the smallest population center data element, dependent on both the contents of the Locality and DependentLocality fields. For example, UK Village |
| Thoroughfare [in,out] | provides the most common street or block data element within a country. For example, USA Street. |
| DependentThoroughfare [in,out] | provides the dependent street or block data element within a country. For example, UK Dependent Street. |
| Building [in,out] | provides the descriptive name identifying an individual location, if such a name exists. |
| Premise [in,out] | provides the alphanumeric code identifying an individual location, if such a code exists. |
| SubBuilding [in,out] | provides the secondary identifiers for a particular delivery point. For example, "FLAT 1" or "SUITE 212". |
| PostalCode [in,out] | provides the complete postal code for a particular delivery point, if such detail can be determined. |
| PostalCodePrimary [out] | provides the primary postal code used for a particular country. For example, USA Zip, Canadian Postcode, Indian PINcode. |
| PostalCodeSecondary [out] | provides secondary postal code information, if used in a particular country and if such detail can be determined and reference data is available. For example, USA Zip Plus 4. |
| Organization [in,out] | provides the business name associated with a particular delivery point, if such a name exists. |
| PostBox [out] | provides the post box for a particular delivery point, if it exists. |
| Unmatched [out] | lists any words that could not be matched to a particular address component. |
| Latitude [out] | provides the WGS 84 latitude in decimal degrees format. |
| Longitude [out] | provides the WGS 84 longitude in decimal degrees format. |
| GeoAccuracy [out] | provides the GeoAccuracy code. For further information, see [GeoAccuracy Code](/talend/en-US/components/8.0/loqate-address-standardization/geoaccuracy). |
| GeoDistance [out] | provides the radius of accuracy in meters, giving an indication of the likely maximum distance between the given geocode and the physical location. |
| AddressFormat [out] | provides the elements of the address. For example, if Address contains 805 Veterans Blvd Redwood City CA 94063-1734, AddressFormat contains Premise Thoroughfare Locality AdministrativeArea PostalCode. |
| DeliveryAddressFormat [out] | provides the elements of the delivery address. For example, if Address contains 805 Veterans Blvd Redwood City CA 94063-1734, DeliveryAddressFormat contains Premise Thoroughfare Locality AdministrativeArea PostalCode. |
| MatchRuleLabel [out] | provides the label of the match rule used to match the input with the reference data. For further information, see the [match rule syntax](https://support.loqate.com/documentation/options-original/match-rules-syntax/). |
| Contact [in,out] | provides the contact name. |
| Function [in,out] | provides the function or job title. |
| Department [in,out] | provides the organizational department. |
| LocalityExtra [out] | provides information that could be as part of the Locality field. This information is not mandatory but is necessary to obtain a complete delivery address. For example in a French address: 12 rue de la Gare, 75019 PARIS CEDEX, France. CEDEX will be considered as Locality Extra. |
| DependentLocalityName [in,out] | provides the name indicator within the DependentLocality field. For example, if DependentLocality contains Dong Cheng Qu, DependentLocalityName contains Dong Cheng if a sufficient level of parsing detail exists for the particular country. |
| DependentLocalityType [in,out] | provides the type indicator within the DependentLocality field. For example, if DependentLocality contains Dong Cheng Qu, DependentLocalityType contains Qu if a sufficient level of parsing detail exists for the particular country. |
| DoubleDependentLocalityName [in,out] | provides the name indicator within the DoubleDependentLocality field. For example, if DoubleDependentLocality contains Xin Zhuang Zhen, DoubleDependentLocalityName contains Xin Zhuang if a sufficient level of parsing detail exists for the particular country. |
| DoubleDependentLocalityType [in,out] | provides the type indicator within the DoubleDependentLocality field. For example, if DoubleDependentLocality contains Xin Zhuang Zhen, DoubleDependentLocalityType contains Zhen if a sufficient level of parsing detail exists for the particular country. |
| ThoroughfarePreDirection [in,out] | provides the prefix directional contained within the Thoroughfare field. For example, if Thoroughfare contains N MAIN ST, ThoroughfarePreDirection contains N if a sufficient level of parsing detail exists for the particular country. |
| ThoroughfareLeadingType [in,out] | provides the leading thoroughfare type indicator within the Thoroughfare field. For example, if Thoroughfare contains RUE DE LA GARE, ThoroughfareLeadingType contains RUE if a sufficient level of parsing detail exists for the particular country. |
| ThoroughfareName [in,out] | provides the name indicator within the Thoroughfare field. For example, if Thoroughfare contains N MAIN ST, ThoroughfareName contains MAIN if a sufficient level of parsing detail exists for the particular country. |
| ThoroughfareTrailingType [in,out] | provides the trailing thoroughfare type indicator within the Thoroughfare field. For example, if Thoroughfare contains N MAIN ST, ThoroughfareTrailingType contains ST if a sufficient level of parsing detail exists for the particular country. |
| ThoroughfarePostDirection [in,out] | provides the postfix directional contained within the Thoroughfare field. For example, if Thoroughfare contains MAIN ST N, ThoroughfarePostDirection contains N if a sufficient level of parsing detail exists for the particular country. |
| DependentThoroughfarePreDirection [in,out] | provides the prefix directional contained within the DependentThoroughfare field. For example, if DependentThoroughfare contains N MAIN ST, DependentThoroughfarePreDirection contains N if a sufficient level of parsing detail exists for the particular country. |
| DependentThoroughfareLeadingType [in,out] | provides the leading thoroughfare type indicator within the DependentThoroughfare field. For example, if DependentThoroughfare contains RUE DE LA GARE, DependentThoroughfareLeadingType contains RUE if a sufficient level of parsing detail exists for the particular country. |
| DependentThoroughfareName [in,out] | provides the name indicator within the DependentThoroughfare field. For example, if DependentThoroughfare contains N MAIN ST, DependentThoroughfareName contains MAIN if a sufficient level of parsing detail exists for the particular country. |
| DependentThoroughfareTrailingType [in,out] | provides the trailing thoroughfare type indicator within the DependentThoroughfare field. For example, if DependentThoroughfare contains N MAIN ST, DependentThoroughfareTrailingType contains ST if a sufficient level of parsing detail exists for the particular country. |
| DependentThoroughfarePostDirection [in,out] | provides the prefix directional contained within the DependentThoroughfare field. For example, if DependentThoroughfare contains MAIN ST N, DependentThoroughfarePostDirection contains N if a sufficient level of parsing detail exists for the particular country. |
| BuildingLeadingType [in,out] | provides the leading building type indicator within the Building field. For example, if Building contains BLOC C, BuildingLeadingType contains BLOC if a sufficient level of parsing detail exists for the particular country. |
| BuildingName [in,out] | provides the name indicator within the Building field. For example, if Building contains WESTMINSTER HOUSE, BuildingName contains WESTMINSTER if a sufficient level of parsing detail exists for the particular country. |
| BuildingTrailingType [in,out] | provides the name indicator within the Building field. For example, if Building contains WESTMINSTER HOUSE, BuildingTrailingType contains HOUSE if a sufficient level of parsing detail exists for the particular country. |
| PremiseType [in,out] | provides the leading premise type indicator within the Premise field. For example, if Premise contains Plot 7/7A, PremiseType contains Plot if a sufficient level of parsing detail exists within a particular country. |
| PremiseNumber [in,out] | provides the leading premise type indicator within the Premise field. For example, if Premise contains Plot 7/7A, PremiseNumber contains 7/7A if a sufficient level of parsing detail exists within a particular country. |
| PremiseExtra [out] | provides information that could be as part of the Premise field. This information is not mandatory but is necessary to obtain a complete delivery address. For example in a French address: 12 bis rue de la Gare, 75019 PARIS, France. Bis will be considered as Locality Extra. |
| SubBuildingType [in,out] | provides the leading sub-building type indicator within the SubBuilding field. For example, if SubBuilding contains FLAT 1, SubBuildingType contains FLAT if a sufficient level of parsing detail exists within a particular country. |
| SubBuildingLeadingType [in,out] | provides the leading sub-building type indicator within the SubBuilding field. For example, if SubBuilding contains FLAT 1, SubBuildingLeadingType contains FLAT if a sufficient level of parsing detail exists within a particular country. |
| SubBuildingNumber [in,out] | provides the leading sub-building type indicator within the SubBuilding field. For example, if SubBuilding contains FLAT 1, SubBuildingNumber contains 1 if a sufficient level of parsing detail exists within a particular country. |
| SubBuildingName [in,out] | provides the descriptive name within the SubBuilding field. For example:  * If the address contains BASEMENT, SubBuilding and SubBuildingName contain BASEMENT. * If the address contains Ste 11, SubBuildingName is blank. SubBuilding will contain Ste 11 and   SubBuildingNumber will contain   11. |
| OrganizationName [in,out] | provides the trailing type indicator contained within the Organization field. For example, if Organization contains Loqate Inc, OrganizationName contains Loqate if a sufficient level of parsing detail exists for the particular country. |
| OrganizationType [in,out] | provides the trailing type indicator contained within the Organization field. For example, if Organization contains Loqate Inc, OrganizationType contains Inc if a sufficient level of parsing detail exists for the particular country. |
| PostBoxType [in,out] | provides the type indicator contained within the PostBox field. For example, if PostBox contains PO BOX 1234, PostBoxType contains PO BOX if a sufficient level of parsing detail exists for the particular country. |
| PostBoxNumber [in,out] | provides the alphanumeric indicator contained within the PostBox field. For example, if PostBox contains PO BOX 1234, PostBoxNumber contains 1234 if a sufficient level of parsing detail exists for the particular country. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the -->
# Address verification codes in tLoqateAddressRow

Last updated: 9/30/2026

The tLoqateAddressRow component
outputs an ACCURACYCODE column. This column holds the
verification codes for processed addresses.

The verification code is made up of the following values:

| Verification code values | Description |
| --- | --- |
| The verification status | used to specify the full mailing address in the relevant country. |
| The post-processed verification match level. | used to specify input data for the address line in the relevant country, split into individual address lines. |
| The pre-processed verification match level | used to specify the full address including line breaks without the Organization, Locality, AdministrativeArea and PostalCode fields. |
| The parsing status | used to specify the individual lines contained within the DeliveryAddress field. |
| The lexicon identification match level | used to supply the country name or code. |
| The context identification match level | used to supply the ISO 3166 official country name. |
| The postcode status | used to supply the ISO 3166 2-character country code. |
| The matchscore | used to supply the ISO 3166 3-character country code. |

For example, the V44-I44-P3-100
verification code implies:

* Verification status = V (verified): a complete match was made
  between the input address and a single record from the available reference
  data.
* Post-processed verification match level = 4 (premises): the
  level to which the input data matches the available reference data once all
  changes and additions performed during the verification process have been taken
  into account.
* Pre-processed verification match level = 4 (premises): the level
  to which the input data matches the available reference data prior to any
  changes or additions performed during the verification process.
* Parsing status = I (identified and parsed): all components of
  the input data have been able to be identified and placed into output
  fields.
* Lexicon identification match level = 4 (premises): using pattern
  matching, a numeric value or word has been identified as a premise number or
  name.
* Context identification match level = 4 (premises): using a least
  accurate form of matching, a numeric value or word has been identified as a
  premises number or name.
* Postcode Status = P3 (added): the primary postal code for the
  country has been added.
* Match score = 100 (complete similarity): the input data and
  closest reference data match completely.

The following sections explain in more details all segments of the
verification code.

### In this section

* [Verification status](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-verification-status-standard-component-enterprise-the)
* [Post-processed verification match level](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-post-processed-verification-match-level-standard-component-enterprise-the)
* [Pre-processed verification match level](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-pre-processed-verification-match-level-standard-component-enterprise-the)
* [Parsing status](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-parsing-status-standard-component-enterprise-the)
* [Lexicon identification match level](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-lexicon-identification-match-level-standard-component-enterprise-the)
* [Context identification match level](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-context-identification-match-level-standard-component-enterprise-the)
* [Postcode status](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-postcode-status-standard-component-enterprise-the)
* [Match score](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-match-score-standard-component-enterprise-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the -->
# Process status in tLoqateAddressRow

Last updated: 9/30/2026

The tLoqateAddressRow component outputs a
STATUS column. This column holds the status of processing input addresses as
the following:

| Status | Description |
| --- | --- |
| psOK | the process completed normally. The score must be examined to determine result accuracy. |
| psException | an exception occurred during processing input records, normally as a result of malformed input data. |
| psServerUninitialized | the process could not be completed because the server has not been initialized. |
| psInvalidInputRecord | the input record contains invalid data, often due to the supply of non-UTF8/Unicode data. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view in the Component tab.
2. Create the schema through the Edit Schema
   button.

   In the open dialog box, click the plus button and add the columns that will
   hold the information in the input address, in this example:
   *address\_input*, *COUNTRY* and
   *data\_description*.
3. Click OK.
4. In the Number of rows field, set the number
   of rows as *1*.
5. In the Mode area, select the Use Inline Content (delimited file) option, and set
   the row and field separators in the corresponding fields.
6. In the Content table, enter the address data
   you want to analyze, for example:

   ```
   Boise Town Square  421 N Cole Rd   83704,,wrong data
   Boise Capitol 280 S Capitol Blvd  83702,us,both address coutry correct
   Federal Way  3563 South Federal Way    83705,US, both correct
   Salmon Creek In-Store (ALB) 14300 NE 20th Ave Ste.B-101  Vancouver WA 98686,US,both correct
   Battle Ground   2500 West Main Street,,no country;address miss(Battle Ground WA 98604 )
   Battle Ground   2500 West abcd Street,,no country address changed
   south southjkjkjkjkjkj,,wrong data
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-tloqateaddressrow-component-standard-component-enterprise -->
# Configuring the tLoqateAddressRow component

Last updated: 9/30/2026

## Procedure

1. Double-click tLoqateAddressRow to display the
   Basic settings view and define the
   component properties.
2. Click the Edit schema button and define in
   the output schema all the columns necessary to hold the formatted address you
   want to get from tLoqateAddressRow.

   Two output columns are read-only: *STATUS* and
   ACCURACYCODE. The first column returns the status of processing
   input addresses. For further information about process status, see [Process status in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the). The second
   column returns the verification code for the processed address. For further
   information about what values this code is made up of and the implications of
   each segment, see [Address verification codes in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the).

   In this example, using the same address-input
   column in the output schema will output the input address. This could be helpful
   to compare how the address elements were parsed and standardized.
3. Click OK and accept to propagate the
   changes.
4. In the Input Address table:
   * add lines in the table,
   * in the Address Field column, click a
     line and select from the list, predefined in the component, the fields
     that hold the input address, Address
     and Country in this example.
   * in the Input Column column, click a
     line and select from the list of the input schema the columns that hold
     the input address, address-input and
     COUNTRY in this example.
5. In the Output Address table:
   * add lines in the table,
   * in the Address Field column, click a
     line and select from the list, predefined in the component, the fields
     that will hold the output address.

     The component will map the values of these fields to the output
     columns you set in this table.

     tLoqateAddressRow provides a long
     list of individual fields because some countries have more complex
     addressing structures than others. For further information about the
     output fields, see [Address fields in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-fields-in-tloqateaddressrow-standard-component-enterprise-some).
   * in the Output Column column, click a
     line and select from the list the columns that will hold the
     standardized output address.
6. In the Loqate Data Path field, set the path
   to the Loqate data folder provided by Loqate and installed locally.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-jvm-argument-and-finalizing-job-standard-component-enterprise -->
# Setting a JVM argument and finalizing the Job

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileOutputExcel component
   to display the Basic settings view and define
   the component properties.
2. Set the destination file name as well as the sheet name and then select the
   Include header and Define all columns auto size check boxes.
3. Click the Run tab and then in the open view
   click Advanced settings.
4. Select the Use specific JVM arguments check
   box and then click New....
5. In the pop-up window, set the following JVM argument: -Djava.library.path=<path/to/lqtjava.dll/folder/>.

   In this argument, you must indicate the folder where the
   loqate library, called liblqtjava.so on Linux or
   lqtjava.dll on Windows, is installed.

   Without the correct JVM argument setting, the following error
   is to be expected: java.lang.Error:
   java.lang.UnsatisfiedLinkError.
6. Save your Job and press F6 to execute
   it.

   tLoqateAddressRow reads the input address
   data. It parses, verifies, cleanses, standardizes addresses and gives the result
   in the output rows you defined in the output schema.

   tLoqateAddressRow matches input address
   data against the Loqate data file you downloaded locally.

   The STATUS standard output column returns the psOKstatus for all address rows. This means that
   the verification process of all address rows could be completed successfully by
   the component. For further information about process status, see [Process status in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the).

   The ACCURACYCODE standard output column returns a verification
   code for each of the processed address rows. For example, the first verification
   code V44-I45-P7-100 means:
   * Verification status = V (verified): a complete match was made between
     the input address and a single record from the available reference
     data.
   * Post-processed verification match level = 4 (premises): the level to
     which the input data matches the available reference data once all
     changes and additions performed during the verification process have
     been taken into account.
   * Pre-processed verification match level = 4 (premises): the level to
     which the input data matches the available reference data prior to any
     changes or additions performed during the verification process.
   * Parsing status = I (identified and parsed): all components of the input
     data have been able to be identified and placed into output fields.
   * Lexicon identification match level = 4 (premises): using pattern
     matching, a numeric value or word has been identified as a premises
     number or name.
   * Context identification match level = 5 (delivery point, PostBox or
     SubBuilding): a numeric value or word has been identified as a post box
     number or sub building name.
   * Postcode Status = P7 (added): the primary postal code for the country
     has been verified and a secondary postal code has been added.
   * Match score = 100 (complete similarity): the input data and closest
     reference data match completely.

   For further information about what values this code is made up
   of and the implications of each segment, see [Address verification codes in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tLoqateAddressRow and tFileOutputExcel.
2. Connect the three components together using the Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-context-identification-match-level-standard-component-enterprise-the -->
# Context identification match level

Last updated: 9/30/2026

The context identification match level gives the level to which the input data can be
recognized based on the context in which it appears.

This is the least accurate form of matching and is based on identifying a word as, for
instance, a Thoroughfare based on it being preceded by something that could be
a Premise, and followed by something that could be a Locality, the
latter items being identified through a match against the reference data or the
lexicon.

| Match level | Description |
| --- | --- |
| 5 | delivery point (PostBox or SubBuilding). |
| 4 | premises (Premise or Building). |
| 3 | thoroughfare. |
| 2 | locality. |
| 1 | administrative area. |
| 0 | none. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-lexicon-identification-match-level-standard-component-enterprise-the -->
# Lexicon identification match level

Last updated: 9/30/2026

The lexicon identification match level gives the level to which the input
data has some recognized form, through the use of:

* pattern matching, for example a numeric value could be a
  premises number, and
* lexicon matching, for example *rd*
  could be a Thoroughfare type (*road*) and *London* could be a
  Locality.

| Match level | Description |
| --- | --- |
| 5 | delivery point (PostBox or SubBuilding). |
| 4 | premises (Premises or Building). |
| 3 | thoroughfare. |
| 2 | locality. |
| 1 | administrative area. |
| 0 | none. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-match-score-standard-component-enterprise-the -->
# Match score

Last updated: 9/30/2026

The match score gives the similarity between the input data and closest reference data
match as a percentage between 0 and 100. 100% means complete similarity.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-parsing-status-standard-component-enterprise-the -->
# Parsing status

Last updated: 9/30/2026

The parsing status can be one of the followings:

* I (identified and parsed): all input data was identified and placed
  into different address fields.
* U (unable to parse): not all input data was identified and
  parsed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-post-processed-verification-match-level-standard-component-enterprise-the -->
# Post-processed verification match level

Last updated: 9/30/2026

The post-processed verification match level gives the level to which the
input data matches the available reference data once all changes and additions performed
during the verification process have been taken into account.

| Match level | Description |
| --- | --- |
| 5 | delivery point (PostBox or SubBuilding). |
| 4 | premises (Premises or Building). |
| 3 | thoroughfare. |
| 2 | locality. |
| 1 | administrative area. |
| 0 | none. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-postcode-status-standard-component-enterprise-the -->
# Postcode status

Last updated: 9/30/2026

The postal code status can be of the following values:

| Status | Description |
| --- | --- |
| P8 | PostalCodePrimary and PostalCodeSecondary are verified. |
| P7 | PostalCodePrimary is verified and PostalCodeSecondary is added or changed. |
| P6 | PostalCodePrimary is verified. |
| P5 | PostalCodePrimary is verified with small change. |
| P4 | PostalCodePrimary is verified with large change. |
| P3 | PostalCodePrimary is added. |
| P2 | PostalCodePrimary is identified by lexicon. |
| P1 | PostalCodePrimary is identified by context. |
| P0 | PostalCodePrimary is empty. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-pre-processed-verification-match-level-standard-component-enterprise-the -->
# Pre-processed verification match level

Last updated: 9/30/2026

The pre-processed verification match level gives the level to which the
input data matches the available reference data prior to any changes or additions
performed during the verification process.

| Match level | Description |
| --- | --- |
| 5 | delivery point (PostBox or SubBuilding). |
| 4 | premises (Premises or Building). |
| 3 | thoroughfare. |
| 2 | locality. |
| 1 | administrative area. |
| 0 | none. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-verification-status-standard-component-enterprise-the -->
# Verification status

Last updated: 9/30/2026

The verification status can be one of the followings:

| Status | Description |
| --- | --- |
| V (Verified) | the address was parsed and an exact match in the reference data was found for all the address components. |
| P (Partially Verified) | the reference data has more detail than the input data for the address. The address was parsed and most of the components of the address were matched against the reference data. |
| U (Unverified) | the input data could not be parsed. The output fields will contain the input data. |
| A (Ambiguous) | more than one item in the reference data match the input data. |
| C (Conflict) | individual address components are valid, but the address is not valid when combining the components together. |
| R (Reverted) | the address was parsed and verified but a minimum acceptable level of verification was not reached. The output fields will contain the input data. |
