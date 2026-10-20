<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-validation/cxmlvalidator · versión 8.0 -->
# cXmlValidator

Last updated: 9/30/2026

Validates the data based on the given XML schema.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

Information noteNote: This component is available only if you have installed the R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cXmlValidator Standard properties

These properties are used to configure cXmlValidator running in
the Standard Route framework.

The Standard
cXmlValidator component belongs to the Data Quality family.

## Basic settings

| Properties | Description |
| --- | --- |
| Type | Select the way the XML schema will be set.  * Repository Resource: The XML schema will be selected   from an existing repository resource file. * File Path: The XML schema will be selected from the   local file system or a remote resource. |
| Resource / Version | This field appears when Repository Resource is selected from the Type list. Click [...] and select the resource file containing the XML schema from the dialog box. Select the version of the resource if more than one version of the resource is available. |
| Schema URI | This field appears when File Path is selected from the Type list. Enter the URL to a local resource on the classpath or a full URL to a remote resource or a resource on the file system which contains the XML schema to validate against. |
| Cache Resource | Select this check box to cache the resource instead of reloading it for each message. |

## Advanced settings

| Properties | Description |
| --- | --- |
| URI Options | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <https://camel.apache.org/components/3.11.x/validator-component.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cXmlValidator can be a middle or end component in a Route. |
| Limitation | n/a |
