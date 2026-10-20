<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/tapioperation · versión 8.0 -->
# tAPIOperation

Last updated: 9/30/2026

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Defines and configures API operations from a contract-first Data Services implementation.

Use tAPIOperation to implement request handling for API operations defined in the contract.

## tAPIOperation Standard properties

These properties are used to configure tAPIOperation running in the Standard Job framework.

The Standard tAPIOperation component belongs to the ESB family.

*This component is relevant only when used with one of the 
Talend
 solutions with ESB, as it should be used with the Service Repository node and the Data Service creation related wizard(s).*

## Basic settings

| Properties | Description |
| --- | --- |
| API -> Schema | Use this control to synchronize the component schema from the selected API operation contract. |
| Edit schema | Opens the schema editor to review or adjust the generated schema. |
| Settings table | * Settings table tab: Defines operation-specific   settings using the columns Name and   Value. * Operation Contract tab: Contains the text field used   to display or edit the selected operation contract identifier. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect runtime metrics for this component. |

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

## Security

Select the Security tab on tAPIOperation to inspect the effective requirement for the current operation.

This tab is informational. It does not configure authorization rules independently from the OpenAPI contract.

Security requirements can be operation-level, inherited globally, explicitly public, or absent. The effective security comes from the loaded contract and any operation-level override.

When exactly one scheme applies to the operation, selecting Configure Security Profiles... opens the contract mapping dialog with that scheme preselected.

| Field | Description |
| --- | --- |
| Security source | Shows whether the requirement is operation-level, inherited, or explicitly public. |
| Contract security | Shows the effective contract mechanism for the operation. |
| Scheme | Shows the scheme name from the loaded contract. |
| Required scopes | Shows the scopes required by the current operation when the contract defines them. |
| Runtime profile | Shows the profile currently bound to the scheme. |

For the complete mapping workflow and update behavior, see [API First security](esb-rest-api-first-security "Review contract security and map supported OpenAPI security schemes to runtime profiles for an API-first service.").

## Usage

Use tAPIOperation to handle operation-level request processing in API-first Data Services jobs after tAPIContract defines and maps the contract security.

After contract import, review the Security tab to confirm the expected effective requirement for the operation and reopen the profile mapping when you need to change the runtime profile.
