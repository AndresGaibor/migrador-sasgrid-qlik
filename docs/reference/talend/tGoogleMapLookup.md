<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup · versión 8.0 -->
# tGoogleMapLookup

Last updated: 9/30/2026

Obtains detailed geographic information using geographic coordinates and address
information.

tGoogleMapLookup  accesses the Google
Places API over HTTP request to obtain detailed geographic information according to the
geographic coordinates you provide.

For further information about Google Places API, see [Google Places API](https://developers.google.com/places/documentation/).

Each data row needs one or several calls to the Places API. The
quota will depend on the license provided by Google. Make sure not
to run the component on a data set that exceeds your quota,
otherwise you will get error messages and addresses will not be
corrected.

For further information about the usage limits of Google Places
API, see [Usage Limits and Billing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing).

For further information about the terms of services of Google
Places API, see [Terms of Service](https://developers.google.com/maps/terms?hl=en).

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tGoogleMapLookup Standard properties

These properties are used to configure tGoogleMapLookup running in the Standard Job framework.

The Standard
tGoogleMapLookup component belongs to the Data Quality family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository. |
| Sync columns | Click this button to retrieve schema from the previous component connected in the Job. |
| Pause(in 1/10 seconds) | Time break between http requests for geographic information record. By default, the value for this field is 1. |
| Latitude Column | Select the schema column that holds the latitude information. |
| Longitude Column | Select the schema column that holds the longitude information. |
| API key | To enter a key, click the […] button next to the field.  You must generate the API key from the Google Developer Console at <https://developers.google.com/console/help/new/>.  Information noteNote: Jobs migrated from releases older than 5.6 will need a key to run. Generate a key and set it in tGoogleMapLoopup basic settings before running the Job. The component currently works with the Google Places API and not the Google Geocoding API as it was the case in releases older than 5.6. As a result, when you run the migrated Jobs in the current Talend Studio, you will have geographic information different from what you had in previous Talend Studio versions. For example, the Location\_type column outputs *ROOFTOP* in older releases, while it outputs *street\_address* now. You can find the list of location types at [Place Types](https://developers.google.com/places/supported_types). |

## Advanced settings

| Properties | Description |
| --- | --- |
| import | Customize this field to import Java class for tGoogleMapLookup. By default, you do not have to modify this part. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an in-between component. It requires an input component, an output component and row Main link. |

**Related concepts**  

* [Obtaining detailed geographic information using address and geographic coordinates](tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-obtaining-detailed-geographic-information-using-address-and-geographic-coordinates-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-obtaining-detailed-geographic-information-using-address-and-geographic-coordinates-standard-component-enterprise-this -->
# Obtaining detailed geographic information using address and geographic coordinates

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes a three-component Job which send HTTP request to Google Places
API and obtain detailed geographic information based on the geographic coordinates we
provide.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-setting-up-job-standard-component-enterprise-drop)
* [Configuring the components](/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-configuring-components-standard-component-enterprise)
* [Executing the Job](/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-executing-job-standard-component-enterprise-save)

**Related reference**  

* [tGoogleMapLookup](tgooglemaplookup "Obtains detailed geographic information using geographic coordinates and address information.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display
   its Basic settings view to define its
   properties.
2. Click Edit schema to open a dialog box
   that displays the data structure of input data and define the data you want
   to pass to tGoogleMapLookup, two columns in
   this scenario, *lat* and *lng*
   respectively to hold the geographic coordinates.
3. Set the Type of column
   *lat* and column *lng* to
   Double. Leave rest of the settings as
   they are. Then, click OK to close the
   dialog box.
4. Click Use Single Table in the Mode area, fill the Value field of the *lat* column with
   37.5300125 and that of the *lng* column
   with -122.2624254.
5. Double-click tGoogleMapLookup to display
   its Basic settings view and define its
   properties.
6. Select the latitude and longitude columns defined in the input schema,
   *lat* and *lng* respectively in this example, and leave the rest of
   settings as they are.
7. Double-click tLogRow to display its
   Basic settings view and define its
   properties.
8. Select Vertical (each row is a key/value
   list) in the Mode area and
   Print unique name in the Title printing mode area.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-executing-job-standard-component-enterprise-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Save your Job and press F6 to execute
it.

Google Places API has query limits for applications that submit requests.
For further information about the usage limits of Google Places API, see
[Usage Limits and
Billing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing).

## Results

The detailed geographic information of the given coordinates location is obtained
from the Google Map database and printed onto the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-address-standardization/tgooglemaplookup-tfixedflowinput-tlogrow-tlogrow-setting-up-job-standard-component-enterprise-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tGoogleMapLookup and tLogRow
2. Connect tFixedFlowInput to tGoogleMapLookup and tGoogleMapLookup to tLogRow
   using Main links.
