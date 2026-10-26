<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/box/tboxv2input · versión 8.0 -->
# tBoxv2Input

Last updated: 9/30/2026

Reads data from files stored in a Box folder and passes the data to the
subsequent component.

For a quick introduction on using this component in your Job, see the
following video:

## tBoxv2Input Standard properties

These properties are used to configure tBoxv2Input running in
the Standard Job framework.

The Standard
tBoxv2Input component belongs to the Cloud
family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0.1-R2023-04 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository.  * Built-in: No property data is stored   centrally. * Repository: Select the repository   file where properties are stored. The fields that follow are completed   automatically using the fetched data.   This drop-down list is not available if you select the Use an existing connection option. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| Authentication type | Select the authentication type: JWT (short for JSON Web Token) or Developer token.  You need to provide the following parameters in the corresponding fields for the JWT authentication type.  * Client ID and Client secret: Enter   the client key and client secret required by Box to access the Box API. To obtain   the client key and client secret, you need to create an account at <https://developers.box.com/> and then create a Box App under the Box   account to be used. The client key and client secret can be obtained from the   account application settings. * Public key ID * Private key * Private key passphrase * Enterprise ID or User ID  For more information about JWT authentication, see [JWT Auth](https://developer.box.com/guides/authentication/jwt/).  Information noteNote: To enter the client secret, private key, or private key passphrase, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the key in the text field, and click OK. Note that you can enter the key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  If you select Developer token from the drop-down list, type in the developer token in the Developer token field. For more information about developer token, see [Developer Tokens](https://developer.box.com/guides/authentication/tokens/developer-tokens/).  The Authentication type drop-down list is available when Use an existing connection is not selected. |
| Path to Box folder | Type in the Box path of the folder where the files to read data from reside. You can also specify the Box path by clicking the [...] button next to this field and navigating to the folder.  This option is available when the Get folder by ID option in the Advanced settings view is not selected. |
| Box folder ID | Type in the Box ID of the folder where the files to read data from reside. You can also specify the Box ID by clicking the [...] button next to this field and navigating to the folder.  This option is available when the Get folder by ID option in the Advanced settings view is selected. |
| File name template | Type in the file name template to filter the files to read data from. |
| Content format | Select the format of the files from the drop-down list: CSV, Avro, Excel, or JSON. |
| Line separator type | Select the line separator: Windows type, Linux type, or Other. If you select Other, specify the line separator in the Line separator string field.  This option is available if you select CSV from the Content format drop-down list. |
| Encoding type | Select the encoding type from the drop-down list: UTF 8, ISO-8859-15 or Other. If you select Other, specify the encoding in the Custom encoding field.  This option is available if you  * select CSV from the Content   format drop-down list. * select Excel from the Content   format drop-down list and select   HTML from the Excel   format drop-down list. |
| Set header | Select this option to treat the beginning lines as the header. You can specify the number of lines that will be treated as the header in the Number of lines field. This option is available if you  * select CSV from the Content   format drop-down list. * select Excel from the Content   format drop-down list and select Excel   97 or Excel 2007 from the   Excel format drop-down list. |
| Field separator type | Select the field separator from the drop-down list. If you select Other, enter the character that will be treated as the separator in the Field separator field.  This option is available if you select CSV from the Content format drop-down list. |
| Avro configuration | Type in the Avro schema description string. This option is available if you select Avro from the Content format drop-down list. |
| Excel format | Select the Excel format of the Excel files: Excel 2007, Excel 97, or HTML. This option is available if you select Excel from the Content format drop-down list. |
| Sheet name | Type in the name of the Excel sheet of the Excel files to read data from. This option is available if you select Excel from the Content format drop-down list and select Excel 97 or Excel 2007 from the Excel format drop-down list. |
| Set footer | Select this option to treat the end lines as the footer. You can specify the number of lines that will be treated as the footer in the Number of lines field. This option is available if you select Excel from the Content format drop-down list and select Excel 97 or Excel 2007 from the Excel format drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Escape character and Quote character | * Escape character: Enter the character you want to   be used as the escape character. The escape character used by default is   `\`. * Quote character: Enter the character you want to   be used as the quote character. The quote character used by default is   `"`.  These options are available if you select CSV from the Content format list in the Basic settings view. |
| Skip empty lines | Select this option to prevent the component from generating an output record when the line of the CSV file is empty. This option is available if you select CSV from the Content format list in the Basic settings view. |
| Define a value for 'null' | By default, the CSV format can only handle empty strings, not null values. Select this option to enter a string that represent null values in the CSV file in the Value that represent ‘null’ field. When this value is found for a column or a row, this will generate a null value in the generated record.  This option is available if you select CSV from the Content format list in the Basic settings view. |
| Infer all numbers as double | Select this option to treat all numbers as Double type numbers. This option is available if you select JSON from the Content format list in the Basic settings view. |
| Get folder by ID | Select this option to specify the folder using its Box ID. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component needs a subsequent component connected through a Row > Main link to pass retrieved data to. |
