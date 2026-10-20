<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/tgeminiclient · versión 8.0 -->
# tGeminiClient

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Accesses the Gemini API. With this component, you can use Gemini AI models and
their different capabilities.

## tGeminiClient Standard properties

These properties are used to configure tGeminiClient running in the
Standard Job framework.

The Standard
tGeminiClient component belongs to the AI
family.

Information noteNote: This component is available only when you have installed the 8.0.1-R2025-11 Talend Studio
monthly update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its   Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| API Key | Enter the Gemini API key in this field.  To enter the raw key, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the key in the text field, and click OK. You can also use a context variable in that field.  For more information on Gemini API Key, read [Using Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key). |
| Model | To select one of the available Gemini models, click the [...] button next to the field. In the dialog box displayed, select the model that will be used or select the Use custom value check box and specify the model name in the Custom value field. |
| Prompt | Enter your instructions in this field. For more information on prompt writing best practices, read [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies). Example: `Given the following addresses, guess the corresponding country names`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |
| Base URL | Type in the base URL address of the Gemini API server you want to access, by default it is `https://xxx.googleapis.com`. |
| API version | Enter the version of the Gemini API server you want to access. |
| Endpoint | Enter the second part of the URL in order to complete the base URL filled in the Base URL field. Base URL and Endpoint values are joined with the character / when needed. |
| Use raw JSON | Select this option to manually enter the raw JSON body. |
| Response body format | Select the response body format from the drop-down list. The right format allows the connector to parse and apply operations to the response. Currently, text, and JSON formats are supported.  * Text: Select this format to return a plain text   message. In that case the response payload is not parsed and it will not be   possible to extract a sub-part from it. * JSON: Select this format if the response received has   a JSON format. In that case the payload is translated into correctly parsed   JSON records. |
| Extract a sub-part of the response | Enter the path of a node to select a sub-element of the response. If the element is an array, each element of the array will be looped over. For more information about the syntax for entering the node name, see [Data Shaping Selector Language syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language). This field is optional and must remain empty to retrieve the entire JSON response.  This field is only available if you select JSON from the Response body format drop-down list.  Information noteNote: This field impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Update configuration button after setting this field. |
| Customize output with DSSL | Select this option to customize the output by entering key/value pairs. Add a row in the table by clicking the plus button under the table, enter the name of the node in the Name field, and enter the value in the Value field. For more information about the value syntax, see [Data Shaping Selector Language syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language).  This field is only available if you select JSON from the Response body format drop-down list.  Information noteNote: This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Update configuration button after setting the key/value pairs in the table under this option. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer. |

**Related tasks**  

* [Comparing the content of two online pages with Gemini](tgeminiclient-tlogrow-comparing-content-of-online-pages-with-gemini-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/tgeminiclient-tlogrow-comparing-content-of-online-pages-with-gemini-standard-component -->
# Comparing the content of two online pages with Gemini

Last updated: 9/30/2026

The following Job aims at accessing a Gemini API, using a Gemini model to extract the information from online pages about Qlik products, compare the information, and displaying the result in the run console.

## Before you begin

This scenario uses Gemini model capabilities. For more information, read the
corresponding [Gemini documentation](https://ai.google.dev/gemini-api/docs).

## Linking the components

### Procedure

1. Drag and drop the following components from the Palette:
   tGeminiClient, and tLogRow.
2. Connect the components using a Row >
   FLOW connection.

## Configuring the components

### Procedure

1. Double-click the tGeminiClient component to display its
   Component view.
2. In the Basic settings view, enter your Gemini API key and
   select the desired Gemini model.

   In this scenario, the `gemini-3-pro-preview` is used. For
   more information on the Gemini models that support PDF files, read the
   corresponding [Gemini documentation](https://ai.google.dev/gemini-api/docs/models).

   You can leave the Prompt field empty as it will be
   provided in the Advanced settings as a JSON code.
3. In the Advanced settings view, enter the API version of
   your choice, and configure the JSON request that will reference your PDF and
   provide the prompt.

   To do so, select Use raw JSON, and enter the following
   JSON in the Request body field:

   ```
   {
         "contents": [
             {
                 "parts": [
                     {"text": "Compare the capabilities and features from the Qlik Analytics and the Data Integration products described at https://www.qlik.com/us/products/qlik-cloud-analytics and https://www.qlik.com/us/products/qlik-talend-data-integration-and-quality"}
                 ]
             }
         ],
         "tools": [
             {
                 "url_context": {}
             }
         ]
     }
   ```

   In this scenario, two web pages on the Qlik website about the Qlik Analytics
   and Data Integration products are processed and compared.
4. Double-click the tLogRow component to display its
   Component view.

   Click Sync columns to retrieve the schema structure from
   the previous component if needed.

   In the Mode area, select Basic,
   and click Print content with log4j to display the Job
   result in the console.

## Executing the Job

### Procedure

1. Press Ctrl + S to save your Job.
2. Press F6 to execute it.

### Results

The Run console displays the result of the comparison of the
two Qlik products and their capabilities.

**Related reference**  

* [tGeminiClient](tgeminiclient "Accesses the Gemini API. With this component, you can use Gemini AI models and their different capabilities.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
