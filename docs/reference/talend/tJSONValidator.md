<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/json/tjsonvalidator · versión 8.0 -->
# tJSONValidator

Last updated: 9/30/2026

Validates the data based on the given JSON schema.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tJSONValidator Standard properties

These properties are used to configure tJSONValidator running in
the Standard Job framework.

The Standard
tJSONValidator component belongs to the Data Quality family.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync   columns to retrieve the schema from the previous component connected in the   Job.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Allocate | Define the schema against which the data of each column must be validated. The schema can be a local file or a HTTP protocol. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any error and continue the Job execution process. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |
| Set JSON schema draft version when it's not defined in the schema file | Starting with the 8.0.1-R2026-08 Talend Studio monthly, the component automatically detects the draft version from the $schema declaration in the JSON schema when the declaration is available and supported. Select the checkbox to use the JSON schema draft version dropdown list when $schema is missing or empty, or when its value is unsupported. Existing Jobs without a $schema declaration continue to use the selected draft version.  For more information, see [json-schema.org](https://json-schema.org/specification). |
| JSON schema file encoding | Select the encoding from the drop-down list. |
| Custom encoding | This option is available when Other is selected as JSON schema file encoding. Enter the encoding name. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step. It requires an input and output flows. |

**Related tasks**  

* [Validating a JSON file using a JSON schema](validating-json-schema-json-file "You can validate JSON columns using the tJSONValidator component.")
* [Validating raw input JSON data using a JSON schema](validating-json-schema-raw-input-data "You can validate JSON columns using the tJSONValidator component.")
