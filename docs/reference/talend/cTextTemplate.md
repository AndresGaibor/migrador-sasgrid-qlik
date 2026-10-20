<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-text-processing/ctexttemplate · versión 8.0 -->
# cTextTemplate

Last updated: 9/30/2026

Supports multiple template engines to replace placeholders in text templates with
actual values. It can be used as the cSetBody component with support for multiline text
input and advanced placeholder handling.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

Information noteNote: This component is available only if you have installed the R2025-08
Talend Studio
Monthly update or a later one delivered by Talend. For
more information, check with your administrator.

## cTextTemplate Standard properties

These properties are used to configure cTextTemplate running in the
Standard Route framework.

The Standard
cTextTemplate component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| Template Engine | Select which engine to use.  * Mustache: Using   {{headers.placeholder}} syntax. * Velocity: Using   $headers.placeholder syntax. * FreeMarker: Using   ${headers.placeholder} syntax. * String Template: Using   <headers.placeholder> syntax. |
| Type | Select the template source type.  * Built-In: The template will be entered directly within the   component. * Repository: The template will be selected from an existing   repository resource file. * File Path: The template will be selected from the local file   system. |
| Resource | This field appears when Repository is selected from the Type list. Select the resource template file from the project resources. Select the version of the template in the Version field if more than one version of the template is available. |
| Resource File | This field appears when File Path is selected from the Type list. Enter the path to the template file in your local file system. |
| Template | This option appears when Built-In is selected from the Type list. Enter the template to be applied on incoming messages. |

## Advanced settings

| Properties | Description |
| --- | --- |
| URI Options | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding value field and enter a value. Available URI options depend on the selected template engine. See the site <https://camel.apache.org/components/latest/> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cTextTemplate can be a middle or end component in a Route. |
| Limitation | n/a |

**Related tasks**  

* [Formulating message body using template](formulating-message-body-using-template)
