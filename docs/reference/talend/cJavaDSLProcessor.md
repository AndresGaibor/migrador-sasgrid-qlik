<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-custom-code/cjavadslprocessor · versión 8.0 -->
# cJavaDSLProcessor

Last updated: 9/30/2026

Implements producers and consumers of message exchanges or implements a message
translator using the Java Domain Specific Language (DSL).

cJavaDSLProcessor can quickly whirls up some code
using Java DSL. If the code in the inner class gets a bit more complicated it is of
course advised to refactor it into a separate class.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cJavaDSLProcessor Standard properties

These properties are used to configure cJavaDSLProcessor running in the Standard Job framework.

The Standard
cJavaDSLProcessor component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| Code | Type in the code you want to implement using Java DSL. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cJavaDSLProcessor is used as a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Wiretapping a message in a Route](cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-wiretapping-message-in-route)
