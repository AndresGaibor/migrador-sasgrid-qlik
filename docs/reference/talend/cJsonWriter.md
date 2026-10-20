<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-json-processing/cjsonwriter · versión 8.0 -->
# cJsonWriter

Last updated: 9/30/2026

Transforms the incoming data into JSON format.

Information noteNote: This component is available only if you have installed the R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cJsonWriter Standard properties

These properties are used to configure cJsonWriter running in
the Standard Route framework.

The Standard
cJsonWriter component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| JSON Library | Select the JSON library from Gson, Jackson, Fastjson, and Custom to transform the incoming data. |
| Bean Reference ID | This option appears when Custom is selected in the JSON Library list. Select the ID of the Bean where your custom JSON structure is defined. |
| Pretty Print | Select this check box to have the output in several rows. If you clear this check box, you will have the output in one row. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cJsonWriter can be a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Extracting a JSON string into a map and converting the map back to JSON](cjsonparser-cjsonwriter-extracting-a-json-string-into-a-map-and-converting-the-map-back-to-json)
