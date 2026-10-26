<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-validation/cjsonvalidator · versión 8.0 -->
# cJsonValidator

Last updated: 9/30/2026

Validates the data based on the given JSON schema.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

Information noteNote: This component is available only if you have installed the R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cJsonValidator Standard properties

These properties are used to configure cJsonValidator running in
the Standard Route framework.

The Standard
cJsonValidator component belongs to the Data Quality family.

## Basic settings

| Properties | Description |
| --- | --- |
| Type | Select the way the JSON schema will be set.  * Repository Resource: The JSON schema will be   selected from an existing repository resource file. * File Path: The JSON schema will be selected from the   local file system or a remote resource. |
| Resource / Version | This field appears when Repository Resource is selected from the Type list. Click [...] and select the resource file containing the JSON schema from the dialog box. Select the version of the resource if more than one version of the resource is available. |
| Schema URI | This field appears when File Path is selected from the Type list. Enter the URL to a local resource on the classpath or a full URL to a remote resource or a resource on the file system which contains the JSON schema to validate against. |
| Cache Resource | Select this check box to cache the resource instead of reloading it for each message. |

## Advanced settings

| Properties | Description |
| --- | --- |
| URI Options | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <https://camel.apache.org/components/3.11.x/json-validator-component.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cJsonValidator can be a middle or end component in a Route. |
| Limitation | n/a |
