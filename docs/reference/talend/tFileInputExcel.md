<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/excel/tfileinputexcel · versión 8.0 -->
# tFileInputExcel

Last updated: 9/30/2026

Reads an Excel file row by row to split them up into fields using regular
expressions and then sends the fields as defined in the schema to the next
component.

## tFileInputExcel Standard properties

These properties are used to configure tFileInputExcel running in the Standard Job
framework.

The Standard
tFileInputExcel component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository.   * Built-in: No property data stored centrally. * Repository: Select the repository file where the properties are   stored. The fields that follow are completed automatically using the data   retrieved. |
|  | Click this icon to open a connection wizard and store the Excel file connection parameters you set in the component Basic settings view.  For more information about setting up and storing file connection parameters, see [Setting connection parameters](/talend/r/en-US/8.0/studio-user-guide/setting-connection-parameters). |
| Read excel2007 file format (xlsx) | Select this check box to read the .xlsx or .xlsm file of Excel 2007. |
| File Name/Stream | File name: Name of the file and/or the variable to be processed.  Stream: Data flow to be processed. The data must be added to the flow in order to be collected by tFileInputExcel via the `INPUT_STREAM` variable in the auto-completion list (Ctrl+Space).  For further information about how to define and use a variable in a Job, see [Using variables in a Job or Route](/talend/r/en-US/7.3/studio-user-guide/using-variables-in-job-or-route).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Password | Provide the password set for the Excel file in double quotation marks by clicking the [...] button next to this frame.  This field is for Excel 2007 (and higher versions) files protected by passwords and is available when Read excel2007 file format(xlsx) is selected.  This component supports standard encryption and agile encryption. |
| All sheets | Select this check box to process all sheets of the Excel file. |
| Sheet list | Click the plus button to add as many lines as needed to the list of the excel sheets to be processed:  Sheet (name or position): enter the name or position of the excel sheet to be processed.  Use Regex: select this check box if you want to use a regular expression to filter the sheets to process. |
| Header | Enter the number of rows to be skipped in the beginning of file.  Note that when dynamic schema is used, the first row of the input data is always treated as the header row no matter whether the Header field value is set or not. For more information about dynamic schema, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema). |
| Footer | Number of records to be skipped at the end of the file. |
| Limit | Maximum number of lines to be processed. |
| Affect each sheet(header&footer) | Select this check box if you want to apply the parameters set in the Header and Footer fields to all excel sheets to be processed. Information noteNote: This option is only available when you select Memory-consuming (User mode) from the Generation mode drop-down list in the Advanced settings view. |
| Die on error | Select this check box to stop the execution of the Job when an error occurs. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can collect the rows on error using a Row > Reject link. |
| First column and Last column | Define the range of the columns to be processed through setting the first and last columns in the First column and Last column fields respectively. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.   * Built-in: The schema will be created   and stored locally for this component only. * Repository: The schema already exists   and is stored in the Repository, hence can be reused in various projects and   Job flowcharts.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Information noteNote: If you are using the dynamic schema feature, make sure date pattern is set for the dynamic column in the Date Pattern field in the schema editor. The default date pattern for the dynamic column is "dd-MM-yyyy".  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator | Select this check box to change the used data separators. |
| Trim all columns | Select this check box to remove the leading and trailing whitespaces from all columns. When this check box is cleared, the Check column to trim table is displayed, which lets you select particular columns to trim. |
| Check column to trim | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |
| Convert date column to string | Available when Read excel2007 file format (xlsx) is selected in the Basic settings view.  Select this check box to show the table Check need convert date column. Here you can parse the string columns that contain date values based on the given date pattern.  Column: all the columns available in the schema of the source .xlsx file.  Convert: select this check box to choose all the columns for conversion (only if they are all of the string type). You can also select the individual check box next to each column for conversion.  Date pattern: set the date format here. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| Read real values for numbers | Select this check box to read numbers in real values. This check box becomes unavailable when you select Read excel2007 file format (xlsx) in the Basic settings view. |
| Stop reading on encountering empty rows | Select this check box to ignore the empty line encountered and, if there are any, the lines that follow this empty line. This check box becomes unavailable when you select Read excel2007 file format (xlsx) in the Basic settings view. |
| Generation mode | Available when Read excel2007 file format (xlsx) is selected in the Basic settings view. Select the mode used to read the Excel 2007 file.   * Less memory consumed for large excel(Event   mode): used for large file. This is a memory-saving mode   to read the Excel 2007 file as a flow. This option helps prevent Job   failure with an out-of-memory error due to high memory consumption when   reading large Excel files.  With this mode selected, reference variables will be extracted with the   format symbol, for example, the percent symbol % and the currency symbol   $. Moreover, the Include phonetic runs check box   is selected by default to allow you to use phonetic strings at index. As   Event mode is a memory-saving mode (main aim), it is supposed to lose   some cell format to save memory and CPU time. * Memory-consuming (User mode): used for   small file. It needs much memory. With this mode selected, the pure data   without the format symbol will be extracted. |
| Don't validate the cells | Select this check box to in order not to validate data. This check box becomes unavailable when you select Read excel2007 file format (xlsx) in the Basic settings view. |
| Ignore the warning | Select this check box to ignore all warnings generated to indicate errors in the Excel file. This check box becomes unavailable when you select Read excel2007 file format (xlsx) in the Basic settings view. |
| Set minimum inflation rate | Select this option to set the ratio between deflated and inflated bytes to detect zipbomb. Type the new minimum inflation rate in the text box that appears. See **setMinInflateRatio**  at <https://poi.apache.org/apidocs/dev/org/apache/poi/openxml4j/util/ZipSecureFile.html> for related information.  An improper minimum inflation rate may result in Zip bomb detected exception when you try to open an Excel file. You can eliminate exceptions of this type by setting the minimum inflation rate to a smaller value.  This option is available when Read excel2007 file format (xlsx) is selected in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  CURRENT\_SHEET: the name of the sheet being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to read an Excel file and to output the data separately depending on the schemas identified in the file. You can use a Row > Reject link to filter the data which doesn't correspond to the type defined. For an example of how to use these two links, see [Procedure](/talend/en-US/components/8.0/processing/textractxmlfield-tlogrow-tfileinputdelimited-tfileoutputdelimited-procedure-standard-component-drop). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Extracting data from an Excel file using a dynamic schema](extracting-data-from-excel-file-using-dynamic-schema-c "This scenario extracts data from an Excel 2007 file. It demonstrates the use of dynamic schema.")
