<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-orchestration/cloop · versión 8.0 -->
# cLoop

Last updated: 9/30/2026

Processes messages repetitively and possibly in different ways.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cLoop Standard properties

These properties are used to configure cLoop running in the Standard Job framework.

The Standard
cLoop component belongs to the Orchestration family.

## Basic settings

| Properties | Description |
| --- | --- |
| Loop Type | * Select a type of loop to be carried out: Expression, Header,   or Value.  Expression: Use an expression to   determine the loop count.  Header: Use a header to determine   the loop count.  Value: Use an argument to set the   loop count. * When using Expression: In the   Language field, select the language of   the expression you want to use to determine the loop count between Constant, EL,   Groovy, Header, JoSQL, JXPath, MVEL,   None, OGNL, PHP, Property, Python, Ruby, Simple, SpEL,   SQL, XPath, XQuery. Type in the   expression in the Expression field.  For more information about how to use the languages to create an expression, see   the site <http://camel.apache.org/languages.html>.  The Add Namespaces option appears   when XPath is selected in the   Language list. Select this   check box to add namespaces for the Xpath expression. Click   [+] to add as many namespaces   as required to the table and define the prefix and URI in the   corresponding columns. * When using Header: Enter the name   of the header that you want to use to determine the loop count in   header field. * When using Value: Enter   an integer you want to set as the loop count in the value field. |
| Copy | Select this check box to use the copy mode. It is cleared by default.  If this option is disabled, the same exchange will be used for each iteration. So the result from the previous iteration will be visible for the next.  If this option is enabled, each iteration restarts with a fresh copy of the input exchange. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cLoop can be a middle component in a Route. |
| Limitation | n/a |
