<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/topenaiclient · versión 8.0 -->
# tOpenAIClient

Last updated: 9/30/2026

Available in...

* Cloud Data Fabric
* Data Fabric
* Qlik Talend Cloud Enterprise Edition
* Real-Time Big Data Platform

Accesses the OpenAI API. With this component, you can use OpenAI models and
their different capabilities.

For a quick introduction on using this component in your Job, see the
following video:

## tOpenAIClient Standard properties

These properties are used to configure tOpenAIClient running
in the Standard Job framework.

The Standard
tOpenAIClient component belongs to the AI family.

Information noteNote: This component is available only when you have installed the 8.0.1-R2024-05 Talend Studio monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its   Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Token | To enter the raw access token, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the token in the text field, and click OK. Note that you can enter either a JSON string in the pure password mode or a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. |
| Model | To select one of the available OpenAI models, click the [...] button next to the field. In the dialog box displayed, select the model that will be used or select the Use custom value check box and specify the model name in the Custom value field. |
| Prompt | Enter your instructions in this field. For more information on prompt writing best practices, read [Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering). Example: `Given the following addresses, guess the corresponding country names`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |
| Base URL | Type in the base URL address of the OpenAI API server you want to access, by default it is `https://api.openai.com`. |
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

* [Identifying countries from input addresses using OpenAI](topenaiclient-tfixedflowinput-tlogrow-identifying-countries-from-addresses "This Job uses fixed input data containing addresses provided by sales team in different formats without country names, sends them to OpenAI to identify the countries, and displays the results in the console.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/topenaiclient-tfixedflowinput-tlogrow-identifying-countries-from-addresses -->
# Identifying countries from input addresses using OpenAI

Last updated: 9/30/2026

This Job uses fixed input data containing addresses provided by sales team in
different formats without country names, sends them to OpenAI to identify the countries,
and displays the results in the console.

## Before you begin

Before running this Job, ensure you have:

* An active OpenAI API account with a valid API token.
* Sufficient API credits to process translation requests.

## Linking the components

### Procedure

1. Create a new Standard Job and add the following components by typing their names
   in the design workspace or dragging them from the Palette:
   tFixedFlowInput, tOpenAIClient,
   tLogRow.
2. Connect tFixedFlowInput to
   tOpenAIClient using a Row >
   Main connection.
3. Connect tOpenAIClient to tLogRow
   using a Row > FLOW
   connection.

## Configuring the components

### Procedure

1. Double-click the tFixedFlowInput component to open its
   Component view.
2. In the Basic settings tab, click Edit
   schema and define the column:

   * `content` (String)
3. Click OK to close the schema editor.
4. In the Mode area, select Use Inline
   Table.
5. In the Content field, add a line for each address:

   ```
   "23 Shevchenka St., Kyiv, 01001"
   "17 Rue de la République, Lyon, 69002"
   "東京都新宿区西新宿３丁目７−１"
   "Avenida Paulista, São Paulo"
   ```
6. Click OK to close the component view.
7. Double-click the tOpenAIClient component to open its
   Component view.
8. In the Basic settings tab, configure the following parameters:

   * Click Sync columns to retrieve the schema from tFixedFlowInput.
   * In the Token field, click the [...] button and enter your OpenAI API token in the password dialog box, then click OK.
   * In the Model field, click the [...] button and select `gpt-3.5-turbo` from the list.
   * In the Prompt field, enter the following
     instruction:

     ```
     Given the following addresses, guess the country names.
     ```
9. Click OK to close the schema editor and OK to close the component view.
10. Double-click the tLogRow component to open its
    Component view.
11. In the Basic settings tab, keep the default Mode as Table (print values in cells of a table).
12. Click OK to close the component view.

## Executing the Job

### Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to execute the Job.

### Results

The Job reads the addresses from the fixed input data, sends each address to the
OpenAI API to identify the country, and displays the identified country names
corresponding to the addresses in the console. The OpenAI model analyzed the address
format, postal codes, city names, and street patterns to determine the country. Each
address is processed individually.

**Related reference**  

* [tOpenAIClient](topenaiclient "Accesses the OpenAI API. With this component, you can use OpenAI models and their different capabilities.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
