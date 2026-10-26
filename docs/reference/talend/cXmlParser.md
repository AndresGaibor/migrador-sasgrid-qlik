<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-xml-processing/cxmlparser · versión 8.0 -->
# cXmlParser

Last updated: 9/30/2026

Extracts the desired data from XML format.

Information noteNote: This component is available only if you have installed the R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cXmlParser Standard properties

These properties are used to configure cXmlParser running in the
Standard Route framework.

The Standard
cXmlParser component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| XML Library | Select the XML library from Jackson XML, XStream, and Custom to extract the incoming data. |
| Mapping Class | This option appears when Jackson XML or XStream is selected in the XML Library list. Enter the mapping class to be used for parsing the data into a map. |
| Bean Reference | This option appears when Custom is selected in the XML Library list. Select the ID of the Bean where your custom XML structure is defined. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cXmlParser can be a middle or end component in a Route. |
| Limitation | n/a |
