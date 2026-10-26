<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-setproperty/csetproperty · versión 8.0 -->
# cSetProperty

Last updated: 9/30/2026

Sets properties for each message sent to it for subsequent message
processing.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cSetProperty Standard properties

These properties are used to configure cSetProperty running in the Standard Job framework.

The Standard
cSetProperty component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| Properties | * Click [+] to add as many properties as required to the   table: * Name: define the name of the   property. * Language: select the language of the   expression you use to set the value for property, from None, Bean, Constant, ESBCorrelationID, EL,   Groovy, Header, JoSQL, JSonPath, JXPath, MVEL, OGNL, PHP,   Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  For more information about how to use the languages to create an expression, see   the site <http://camel.apache.org/languages.html>. * Value: enter the value of the property. |
| Add Namespaces | This option appears when XPath is selected in the Language list.  Select this check box to add namespaces for the properties. Click [+] to add as many namespaces as required to the table and define the prefix and URI in the corresponding columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSetProperty is used as a middle component in a Route. |
| Limitation | n/a |
