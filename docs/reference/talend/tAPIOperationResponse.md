<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/tapioperationresponse · versión 8.0 -->
# tAPIOperationResponse

Last updated: 9/30/2026

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Builds operation responses according to the status codes and payload models defined in the API contract.

tAPIOperationResponse helps return successful or error responses that match contract response definitions.

## tAPIOperationResponse Standard properties

These properties are used to configure tAPIOperationResponse running in the Standard Job framework.

The Standard tAPIOperationResponse component belongs to the ESB family.

*This component is relevant only when used with one of the 
Talend
 solutions with ESB, as it should be used with the Service Repository node and the Data Service creation related wizard(s).*

## Basic settings

| Properties | Description |
| --- | --- |
| Select API Contract, Operation and Response | Opens the Select API Operation Response window, where you select values in the API Contract list, Operation list, and Response list. |
| Map Response Body | Maps Job output data to the response payload structure defined in the selected response contract. Information noteRestriction: Arrays and nested objects within arrays cannot be mapped at the individual field level. Map them as complete JSON strings matching the API contract structure. A warning displayed when saving the Job indicates that validation is performed only at runtime.  Flat nested objects that are not array elements support field-by-field mapping when source and target fields have a one-to-one relationship. |
| Schema and Edit schema | Displays the response schema and opens the schema editor for manual adjustments when needed. |
| Settings table | * Settings table tab: Defines operation-specific   settings using the columns Name and   Value. * Operation Contract tab: Contains the text field used   to display or edit the selected operation contract identifier. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect runtime metrics for this component. |

## Usage

Use tAPIOperationResponse after operation processing to ensure responses remain consistent with the API contract.
