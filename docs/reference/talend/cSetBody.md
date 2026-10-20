<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody · versión 8.0 -->
# cSetBody

Last updated: 9/30/2026

Sets the message body in the Route.

cSetBody replaces the payload of each message sent to
it.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cSetBody Standard properties

These properties are used to configure cSetBody running in the Standard Job framework.

The Standard
cSetBody component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| Language | Select the language of the expression you use to set the content for matched messages, from None, Bean, CONSTANT, CorrelationID, EL, GROOVY, HEADER, JoSQL, JSonPath, JXPATH, MVEL, OGNL, PHP, PROPERTY, PYTHON, RUBY, SIMPLE, SpEL, SQL, XPATH, and XQUERY.  For more information about how to use the languages to create an expression, see the site <http://camel.apache.org/languages.html>. |
| Expression | Type in the expression to set the message content. |
| Correlation expression/Add Namespaces | This option appears when XPath is selected in the Language list.  Select this check box to add namespaces for the Xpath expression. Click [+] to add as many namespaces as required to the table and define the prefix and URI in the corresponding columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSetBody is used as a middle component in a Route. |
| Limitation | n/a |
