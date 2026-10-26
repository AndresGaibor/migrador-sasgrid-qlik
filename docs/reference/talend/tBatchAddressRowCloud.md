<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud · versión 8.0 -->
# tBatchAddressRowCloud

Last updated: 9/30/2026

Uses batch processing to parse address data and get formatted addresses quickly,
accurately and without installing any software.

Address data is corrected against the latest online reference data from providers that
support a batch services including Loqate and MelissaData.
tBatchAddressRowCloud proposes alternatives for missing address data
such as country or postal code, and addresses are enriched with other elements such as
latitude longitude. The advantages of this component over
tAddressRowCloud is that you gain in performance when dealing with
large amounts of data.

tBatchAddressRowCloud splits addresses
from input streams into several files (batches) and verifies and formats addresses in each
file by using online batch services.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tBatchAddressRowCloud Standard properties

These properties are used to configure tBatchAddressRowCloud running in the Standard Job framework.

The Standard
tBatchAddressRowCloud component belongs to the Data Quality family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Edit Schema | Click the [...] button and define the input and output schema of the address data.  The output schema of tBatchAddressRowCloud proposes several read-only address columns including a VerificationLevel column which provides you with a verification status of the processed address. The verification levels in this column are defined by  Talend . For further information, see [Address verification levels in tAddressRowCloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the).  Also some of the output columns could be empty depending on what address provider you select in the component basic settings when executing the Job. |
| Address Provider | Select from the list the provider of the reference data against which you want to validate and format addresses.  The list of address providers includes Loqate and MelissaData. |
| Default Country | Select the country name for which the ISO 3166-1 alpha-3 code should be used when parsing data and if no identifiable country is found in an input record. |
| License/API key | Enter the license or the API key provided by the address provider you select from the list.  To enter a key, click the […] button next to the field.  You must visit the provider website, register and get the license/API key. |
| Batch job name | Enter, between quotation marks, a name of your choice to give to the batch files that will be generated and saved on the Loqate server. These files hold the results of batch processing.  This option only appears if Loqate is the selected address provider. |
| Number of rows in each batch file | Enter the number of address records you want to group in each batch file.  This option only appears if Loqate is the selected address provider.  Information noteNote: If MelissaData is the selected address provider, 100 rows are sent in each batch file. |
| Loqate website login | Enter your login provided by Loqate.  This option only appears if Loqate is the selected address provider. |
| Loqate website password | Enter the password provided by Loqate.  This option only appears if Loqate is the selected address provider. |
| Processing Mode | This option is applied only to the Loqate provider.  Select from the list the mode of address validation you want to have:  Verify and Geocode (selected by default): with this mode, the component standardizes and corrects addresses and enriches them with latitude and longitude information. Information noteNote: Combining address verification and geocoding will use extra credits. For more information, see [the Loqate pricing](https://loqate.com/en-us/pricing/)  -Verify only: with this mode, the component standardizes and corrects addresses without enriching them with latitude and longitude information.  This option only appears if Loqate is the selected address provider. |
| Input Mapping | Address field: add lines to the table and select from the predefined address list the fields that will hold input addresses.  tBatchAddressRowCloud provides a long list of address fields because some countries have more complex address structures than others. For further information about the input fields, see [Address fields in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-fields-in-tloqateaddressrow-standard-component-enterprise-some).  Input Column: add lines to the table and select from the list the columns that hold the input addresses. The input schema can have one or multiple columns and can have columns that do not represent address data. |
| Use Additional Output | Select this check box and use the Output Mapping table to add more address columns to the output schema:  Address field: add lines to the table and select from a predefined address list the fields of the extra information you want to output.  These predefined address fields vary according to the provider you select from the Address Provider list. For further information about the additional address fields, check the provider website.  Output Column: select from the list the columns that will hold the additional addresses information. You must first add these additional columns to the tBatchAddressRowCloud output schema through the Edit Schema button.  tBatchAddressRowCloud maps the values of the address fields to the output columns in the Output Column.  If you select to have an output column in the Output Address table that has the exact name of an input column, the input column value will be overwritten by the value given by the component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use mockup mode (no credit consumption) | Before being able to use this option, you must run your Job at least once to create batch files on the Loqate server.  This option is only for testing or for development needs. You will not be charged for batch processing if you select to run the Job with this option.  Select this check box to simulate execution and responses from the Loqate server by using as output a batch file that has been previously processed and saved on the server.  Batch ID: set the identifier of the batch file you want to use as input in your Job.  You can get the file identifier if you log in at [Loqate](https://account.loqate.com/Login/) and access the Loqate server. |
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

* [Parsing addresses against reference data in the Cloud using batch processing](tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-reference-data-in-cloud-using-batch-processing-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-reference-data-in-cloud-using-batch-processing-standard-component-enterprise-this -->
# Parsing addresses against reference data in the Cloud using batch processing

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes a Job which uses:

* the tFixedFlowInput
  component to generate the address data to be analyzed,
* the tBatchAddressRowCloud
  component to parse, standardize and format the addresses in the Cloud through
  the Address Validation API,
* the tFileOutputExcel
  component to output the correct formatted addresses in an .xls file.

You must have internet connection to be able to use tBatchAddressRowCloud.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise)
* [Parsing addresses against Loqate](/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-loqate-standard-component-enterprise)
* [Configuring the output component and executing the Job](/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise)

**Related reference**  

* [tBatchAddressRowCloud](tbatchaddressrowcloud "Uses batch processing to parse address data and get formatted addresses quickly, accurately and without installing any software.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-input-component-standard-component-enterprise -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view in the Component tab.
2. Create the schema through the Edit Schema
   button.

   In the open dialog box, click the [+]
   button and add the columns that will hold the information in the input
   address. For this example, add *ID*,
   *Organization*, *Address1* x 8,
   *Locality*, *AdministrativeArea*,
   *PostalCode* and *Country*.
3. Click OK.
4. In the Number of rows field, enter
   *1*.
5. In the Mode area, select the Use Inline Content option.
6. In the Content table, enter the address
   data you want to analyze, for example:

   ```
   1000		23 girdwood road								london		sw18	GBR
   1001		1111 bayhill drive ste 290	san bruno								ca		USA
   1002		23 girdwood road								london		sw18	GBR
   1003		1111 bayhill drive ste 290	san bruno								ca		USA
   1004		23 girdwood road								london		sw18	GBR
   1005		1111 bayhill drive ste 290	san bruno								ca		USA
   1006		23 girdwood road								london		sw18	GBR
   1007		1111 bayhill drive ste 290	san bruno								ca		USA
   1008		23 girdwood road								london		sw18	GBR
   1009		1111 bayhill drive ste 290	san bruno								ca		USA
   1010		23 girdwood road								london		sw18	GBR
   ...
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-configuring-output-component-and-executing-job-standard-component-enterprise -->
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

   The tBatchAddressRowCloud component
   parses addresses using batch processing. It corrects addresses using the
   online batch service of Loqate and writes the result in batch files on the
   Loqate server.
4. Right-click the output component and select Data
   Viewer to display the formatted address data.

   tBatchAddressRowCloud matches input
   address data against the Loqate repository.

   The STATUS output column returns the OK status
   for all address rows. This means that the verification process of all
   address rows could be completed successfully by the component. For further
   information about process status, see [Process status in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the).

   The VerificationLevel output column
   provides you with a verification levels defined by 
   Talend
   . For further information, see [Address verification levels in tAddressRowCloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the).

   The AddressVerificationCode output column returns a
   verification code for each of the processed address rows.

   For further information about what values this code is made up of and the
   implications of each segment, see [Address verification codes in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-parsing-addresses-against-loqate-standard-component-enterprise -->
# Parsing addresses against Loqate

Last updated: 9/30/2026

### In this section

* [Setting the schema and selecting an address provider](/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-schema-and-selecting-address-provider-standard-component-enterprise)
* [Defining address mapping and setting advanced parameters](/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-defining-address-mapping-and-setting-advanced-parameters-standard-component-enterprise-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tBatchAddressRowCloud and tFileOutputExcel.
2. Connect the three components together using the Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-defining-address-mapping-and-setting-advanced-parameters-standard-component-enterprise-in -->
# Defining address mapping and setting advanced parameters

Last updated: 9/30/2026

## Procedure

1. In the Input Mapping table:
   * Use the [+] button to add lines
     in the table.
   * Click in the Address Field column
     and select from the predefined list the fields that hold the input
     address, Address in this
     example.

     The component will map the values of these fields to the input
     columns you set in this table.

     tBatchAddressRowCloud provides a
     list of individual fields because some countries have more complex
     addressing structures than others.
   * Click in the Input Column column
     and select from the list of the input schema the columns that hold
     the input address you want to parse, Address1 in this example.
2. If required, select the Use Additional
   Output check box and define in the table what extra address
   fields you want to retrieve from the provider repository and add to the
   parsing results. For an example on how to use this table, check [Defining additional address fields](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-defining-additional-address-fields-standard-component-enterprise-if).

   The Address field column holds predefined
   address fields which vary according to the provider you select. The
   Output Column column holds the fields
   you want to use to output the extra information. You must first add these
   additional columns to the component schema through the Edit Schema button.
3. Click the Advanced settings tab and set the
   parameters in this view according to your needs.

   In this example:

   * Select the Use mockup mode (no credit
     consumption) check box.

     This check box enables you to simulate execution and
     responses from the Loqate server by using as input a batch file that has
     been already processed by the Job and saved on the server.
   * Log in to [Loqate](https://account.loqate.com/Login/) and access the Loqate server to fetch
     the identifier of the batch file you want to use as output in your
     Job.
   * Set the identifier in the Batch ID
     field.

     This option is used only for testing or for development needs.
   * Leave all other default parameters as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/address-standardization/tbatchaddressrowcloud-tfixedflowinput-tfileoutputexcel-tfileoutputexcel-setting-schema-and-selecting-address-provider-standard-component-enterprise -->
# Setting the schema and selecting an address provider

Last updated: 9/30/2026

## Procedure

1. Double-click tBatchAddressRowCloud to
   display the Basic settings view and define
   the component properties.
2. If required, click Sync columns to
   retrieve the schema defined in the input component.
3. Click the Edit schema button to open the
   schema dialog box.

   tBatchAddressRowCloud proposes several
   predefined read-only address columns as shown in the below capture.

   The *STATUS* column returns the status of
   processing input addresses. For further information about process status,
   see [Process status in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-process-status-in-tloqateaddressrow-standard-component-enterprise-the).

   The AddressVerificationCode column returns the verification
   code for the processed address. For further information about what values
   this code is made up of and the implications of each segment, see [Address verification codes in tLoqateAddressRow](/talend/en-US/components/8.0/loqate-address-standardization/tloqateaddressrow-tloqateaddressrow-address-verification-codes-in-tloqateaddressrow-standard-component-enterprise-the).

   The VerificationLevel output column
   provides you with a verification status of the processed addresses. For
   further information, see [Address verification levels in tAddressRowCloud](/talend/en-US/components/8.0/address-standardization/taddressrowcloud-taddressrowcloud-address-verification-levels-in-taddressrowcloud-standard-component-enterprise-the).
4. Move any of the input columns to the output schema if you want to show
   them in the verification results, click OK
   and accept to propagate the changes.

   You can also add columns directly in the output schema to retrieve
   additional address information from the provider repository.
5. Select from the Address Provider list the
   provider of the reference data against which you want to validate and format
   input addresses, Loqate in this
   example.

   You can also validate addresses against MelissaData online service.
6. In the License/API key field, enter the
   license key provided by Loqate.
7. In the Batch job name field, enter
   between quotation marks a name of your choice to give to the batch files
   that will be generated and saved on the Loqate server. 

   Set the number of address records you want to group in each batch file in
   the Number of rows in each batch file
   field.
8. Enter the login and password provided by Loqate in the Loqate website login and Loqate website password respectively.
9. From the Processing Mode list,
   select:

   | Option | To... |
   | --- | --- |
   | Verify and Geocode (selected by default) | standardize and correct addresses and enrich them with latitude and longitude.  Combining address verification and geocoding will cost extra credits. For further information, see [the Loqate pricing](https://loqate.com/en-us/pricing/). |
   | Verify only | standardize and correct addresses without enriching them with latitude and longitude. |
