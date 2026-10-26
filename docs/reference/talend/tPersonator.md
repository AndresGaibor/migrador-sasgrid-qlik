<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/melissa-data-address-standardization/tpersonator · versión 8.0 -->
# tPersonator

Last updated: 9/30/2026

Ensures the quality of a US and Canadian contact database by checking,
verifying, moving and appending contact data.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tPersonator Standard properties

These properties are used to configure
tPersonator running in the Standard Job
framework.

The standard tPersonator component belongs to the Data Quality family.

## Basic Settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Click Sync columns to retrieve the schema from the previous component connected in the Job.  Select the Schema type:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:  View schema: choose this option to view the schema only.  Change to built-in property: choose this option to change the schema to Built-in for local changes.  Update repository connection: choose this option to change the schema stored in the repository and decide whether to propagate the changes to all the Jobs upon completion.  The only supported data type is String.  The output schema contains read-only columns. For more information, see the [tPersonator output schema](/talend/en-US/components/8.0/melissa-data-address-standardization/tpersonator-output-schema). |
| Input mapping | Associate the Personator field with the Input column. The supported data types are:  * Date * Long * String |
| Actions | Select the actions to perform:  * Check   action: Standardizes the data and ensures that   they are valid. This action analyses each data separately. For   example, if the zip code does not match the city, the Check action corrects it,   without impacting the other data. * Verify   action: Ensures that the different data are   associated with each other. This action analyses the data as a   whole. For example, if you perform this action on the addresses,   the Verify action   verifies whether the address is associated with the same name,   phone and email in other databases. * Move   action: Retrieves the last address. The database   must at least contain the last name or company name and an   address. * Append   action: Adds missing data.  Depending on the action, some [inputs are mandatory](tpersonator). |
| Centric hint | Available if you select Append action or Verify action. Select one reference data:  * Auto: Select to use the address as the   reference data. If not available, the phone number is used. If not   available, the email is used. If not available, the SSN (Social   Security Number) is used. * Address * Phone * Email * SSN This reference data is available if you select Verify   action. |
| Append options | Available if you select Append action. Select one action:  * Blank: Select to append data when your   database does not contain either the address, phone, email,   name or company. * Check   error: Select to append data when errors   occur to either the address, phone, email, name or company:   + An address error occurs when the     address is not found in the database, is not     partially verified, or cannot be corrected. The     component does not return the result codes: AS01,     AS02, or AS03. For more information on the result     codes, see this [description     table](http://wiki.melissadata.com/index.php?title=Result_Code_Details#Personator_Consumer) .   + A phone error occurs when the     phone number does not contain 7 or 10 digits. The     component does not return the result codes: PS01     or PS02. For more information on the result codes,     see this [description     table](http://wiki.melissadata.com/index.php?title=Result_Code_Details#Personator_Consumer).   + An email error occurs when the     email is not found in the database, or if the     email is unconfirmed. The component does not     return the result codes: ES01 or ES03. For more     information on the result codes, see this [description     table](http://wiki.melissadata.com/index.php?title=Result_Code_Details#Personator_Consumer).   + A name error occurs when the name     did not parse successfully. The component does not     return the result code: NS01. For more information     on the result codes, see this [description     table](http://wiki.melissadata.com/index.php?title=Result_Code_Details#Personator_Consumer).   + A company error occurs when the     company name is not provided. * Always: Select to append data, regardless   of whether the address, phone, email, name or company in   your database is blank or incorrect. |
| Address options | Diacritics: auto, on or off. Set to on to return the French characters. If set to auto, those characters are returned if present in your database. Advanced address correction: Select to perform an advanced correction of the address. It uses the full name or company name and can correct or append house number, street name, city, state and zip code.  Use preferred city: Select to use the city name preferred by the postal services. |
| Name options | Name hint  * Definitely   full: Select to treat the name in this order:   first name, middle name, last name, regardless of formatting or   punctuation. * Very likely   full: Select to treat the name in this order:   first name, middle name, last name, unless the order is   indicated by formatting or punctuation. * Probably   full: Select to let the statistical logic   determine the name order, with a bias toward this order: first   name, middle name, last name. * Varying: Select to let the statistical logic   determine the name order, with no bias toward either name   order. * Probably   inverse: Select to let the statistical logic   determine the name order, with a bias toward this order: last   name, middle name, first name. * Very likely   inverse: Select to treat the name in this order:   last name, middle name, first name, unless the order is   indicated by formatting or punctuation. * Definitely   inverse: Select to treat the name in this order:   last name, middle name, first name, regardless of formatting or   punctuation. * Mixed first   name: Select if the last name misses. Name field   must only contain prefixes, first name and middle name. * Mixed last   name: Select if the first and middle names miss.   Name field must only contain last names and suffixes.  Middle name logic  * Parse   logic: Select to consider the middle name as   part of the last name. This consideration is possible if the   middle name is a common last name. In this case, the last name   is hyphenated. * Hyphenated   last: Select to consider the second word as part   of the last name. * Middle   name: Select to consider the second word as a   middle name.  Salutation format: Select the salutation format. For example, John Smith:  * Formal:   Mr. Smith * Informal: John * First/Last: John Smith  Gender population: Mixed, Male, Female Select the predominant gender in your database. Genderization policy: Neutral, Conservative, Aggressive. For more information on this option, see the[Setting up the Genderization policy parameter of tPersonator](/talend/en-US/components/8.0/melissa-data-address-standardization/setting-up-genderization-policy-parameter-of-tpersonator).  To see the preceding Name options information in the output columns, select the Name details check box in Miscellaneous outputs.  Correct first name: Select to correct the spelling of the first name. Standardize company: Select to apply title cases and abbreviate the company name. For example, *melissa data corporation* is replaced by *Melissa Data Corp.*. |
| Email options | Database lookup: Select to verify the domain names using a database of valid domains. Standardize case: Select to lowercase the email characters before any action.  Correct syntax: Select to correct the syntax of the email. This option supports simple email syntax: *local part + @ + domain + ‘.’ + top-level domain*. For example, *jsmith@domain,coj* is replaced by *jsmith@domain.com*.  Update domain: Select to update the domain name if out-of-dated. |
| Address outputs | Basic (Default): Select to return the basic address. This setting is always enabled. Address details: Select to return the detailed address.  Plus4: Select to return the +4 code.  Private mailbox: Select to return the private mail box number. These mail boxes are the private mail boxes in commercial mail receiving agencies.  Suite: Select to return the apartment number.  Parsed address: Select to return the address details. |
| Geographics outputs | Census: Select to return census information. Census 2: Select to return more census information.  Geocode: Select to return the geocode. |
| Miscellaneous outputs | Demographic details: Select to return a string containing all the results of the demographics. Commas delimit the results. Name details: Select to return the name details such as the gender, salutation...  Parsed email: Select to return the email details such as the domain name, mailbox name...  Parsed phone: Select to return the phone number details such as the extension, prefix...  IP Address: Select to return details on the IP address such as the connection speed, country...  Occupation: Select to return the individual's occupation. |

Depending on the action,
some inputs are mandatory.

| Action | Mandatory inputs |
| --- | --- |
| Check | The database must at least contain one of the following:  * Address and zip code * Address and city or state * Phone number * Email * Full name * First name and last name |
| Verify | The database must at least contain two of the following:  * Address and zip code or address, city and   state * Phone number * Email * Full name or last name or first and last   names * Company name  If the database contains only names and company names, you cannot perform the verify action. The results cannot be accurate enough. |
| Move | The database must at least contain one of the following:  * Address and full name * Address and first and last names * Address and company name |
| Append | The mandatory inputs depend on the data to append. To append a name or company name, the database must at least contain one of the following:  * Address, city and state or address and zip   code * Phone number * Email  To append an address, the database must at least contain one of the following:  * Phone number * Email  To append a phone number, the database must at least contain one of the following:  * Address, city and state or address and zip   code * Email  To append an email, the database must at least contain one of the following:  * Address, city and state or address and   zip * Phone number |

## Advanced Settings

| Properties | Description |
| --- | --- |
| tStatCatcher statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| License key | To enter a key, click the […] button next to the field. If you have no license key, contact Melissa Data. |
| Number of retries | Define the number of retries before the Job fails. |
| Timeout in seconds | Define the timeout time period. |
| Cache directory | Browse the cache directory. |
| Batch request size (1-100) | Define the number of messages to be delivered in each batch. |
| Multithreading | Select to use more than one thread in the same job to handle the response from the Melissa data service. |
| Thead count (1-10) | Define the maximum number of threads. |
| Show debug console output | Select to show the debug console output. |

**Related concepts**  

* [Scenario: Verifying and enriching a database](tpersonator-tfileinputdelimited-tlogrow-tlogrow-scenario-verifying-and-enriching-database-in-this "The Job in this scenario uses the tPersonator component to ensure the quality of a customer database and enrich this database.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/melissa-data-address-standardization/tpersonator-output-schema -->
# tPersonator output schema

Last updated: 9/30/2026

The tPersonator component
generates read-only columns that are all of type String. There are two types of output
columns: dependent and default. Information is returned in the dependent output columns if
you have selected the corresponding settings. The default output columns are independent of
the settings.

The output columns contain one of the following types of
information:

* The input information.
* The information returned by the Personator™ Consumer Web Service.
* `null`: you
  have not selected the corresponding setting.
* The column is empty: there is no information to return.

## The default output columns

`md_RecordID; md_AddressExtras; md_AddressKey; md_AddressLine1; md_AddressLine2;
md_City; md_CompanyName; md_EmailAddress; md_MelissaAddressKey; md_PhoneNumber;
md_PostalCode; md_Reserved; md_Results; md_RecordExtras.`

These output columns depend on the
Basic (Default) setting that is always enabled.

## The dependent output columns

| If you select... | | Information is returned in... |
| --- | --- | --- |
| Address outputs | Address details | `md_AddressTypeCode; md_CarrierRoute; md_CityAbbreviation; md_CountryCode; md_CountryName; md_DeliveryIndicator; md_DeliveryPointCheckDigit; md_DeliveryPointCode; md_StateName; md_UTC; md_UrbanizationName` |
| Plus4 | `md_Plus4` |
| Private mailbox | `md_PrivateMailBox` |
| Suite | `md_AddressSuiteNumber; md_Suite` |
| Parsed address | `md_AddressDeliveryInstallation; md_AddressLockBox; md_AddressPostDirection; md_AddressPreDirection; md_AddressPrivateMailboxName; md_AddressPrivateMailboxRange; md_AddressRouteService; md_AddressStreetName; md_AddressStreetSuffix; md_AddressSuiteName` |
| Own/Rent | `md_OwnRent` |
| Geographics outputs | Census 2 | `md_CensusKey; md_CountySubdivisionCode; md_CountySubdivisionName; md_ElementarySchoolDistrictCode; md_ElementarySchoolDistrictName; md_SecondarySchoolDistrictCode; md_SecondarySchoolDistrictName; md_StateDistrictLower; md_StateDistrictUpper; md_UnifiedSchoolDistrictCode; md_UnifiedSchoolDistrictName` |
| Geocode | `md_Latitude; md_Longitude` |
| Census | `md_CBSACode; md_CBSADivisionCode; md_CBSADivisionLevel; md_CBSADivisionTitle; md_CBSALevel; md_CBSATitle; md_CensusBlock; md_CensusTract; md_CongressionalDistrict; md_CountyFIPS; md_CountyName; md_PlaceCode` |
| Miscellaneous outputs | Demographic details | `md_DateOfBirth; md_DateOfDeath; md_DemographicsGender; md_DemographicsResults; md_HouseholdIncome; md_LengthOfResidence; md_MaritalStatus; md_PresenceOfChildren` |
| Name details | `md_Gender; md_Gender2; md_NameFirst; md_NameFirst2; md_NameFull; md_NameLast; md_NameLast2; md_NameMiddle; md_NameMiddle2; md_NamePrefix; md_NamePrefix2; md_NameSuffix; md_NameSuffix2; md_Salutation` |
| Parsed email | `md_DomainName; md_MailboxName; md_TopLevelDomain` |
| Parsed phone | `md_AreaCode; md_NewAreaCode; md_PhoneExtension; md_PhonePrefix; md_PhoneSuffix` |
| Phone country code | `md_PhoneCountryCode` |
| Phone country name | `md_PhoneCountryName` |
| IP address | `md_IPAddress; md_IPCity; md_IPConnectionSpeed; md_IPConnectionType; md_IPContinent; md_IPCountryAbbreviation; md_IPCountryName; md_IPDomainName; md_IPISPName; md_IPLatitude; md_IPLongitude; md_IPPostalCode; md_IPProxyDescription; md_IPProxyType; md_IPRegion; md_IPUTC; md_DistanceAddressToIP` |
| Occupation | `md_Occupation` |
