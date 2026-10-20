<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor · versión 8.0 -->
# cProcessor

Last updated: 9/30/2026

Implements consumers of message exchanges or implements a Message
Translator.

cProcessor quickly whirls up some code. If the code in
the inner class is complicated, it is recommended to refactor it into a separate
class.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cProcessor Standard properties

These properties are used to configure cProcessor running in the Standard Job framework.

The Standard
cProcessor component belongs to the Custom family.

## Basic settings

| Properties | Description |
| --- | --- |
| Code | Type in the Java code you want to implement. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Import | Enter the Java code that helps to import, if necessary, external libraries used in the Code box. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cProcessor is used as a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Wiretapping a message in a Route](cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-wiretapping-message-in-route)
