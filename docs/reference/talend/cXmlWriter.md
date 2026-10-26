<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-xml-processing/cxmlwriter · versión 8.0 -->
# cXmlWriter

Last updated: 9/30/2026

Transforms the incoming data into XML format.

Information noteNote: This component is available only if you have installed the R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cXmlWriter Standard properties

These properties are used to configure cXmlWriter running in the
Standard Route framework.

The Standard
cXmlWriter component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| XML Library | Select the XML library from Jackson XML, JAXB, XStream, and Custom to transform the incoming data. |
| Bean Reference ID | This option appears when Custom is selected in the XML Library list. Select the ID of the Bean where your custom XML structure is defined. |
| Pretty Print | Select this check box to have the output in several rows. If you clear this check box, you will have the output in one row. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cXmlWriter can be a middle or end component in a Route. |
| Limitation | n/a |
