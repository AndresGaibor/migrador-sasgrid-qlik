<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/excel/tfileoutputexcel · versión 8.0 -->
# tFileOutputExcel

Last updated: 9/30/2026

Writes an MS Excel file with separated data values according to a defined
schema.

## tFileOutputExcel Standard properties

These properties are used to configure
tFileOutputExcel running in the Standard Job framework.

The
Standard
tFileOutputExcel component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Write excel 2007 file format (xlsx / xlsm) | Select this check box to write the processed data into the .xlsx or .xlsm format of Excel 2007. |
| Use Output Stream | Select this check box to process the data flow of interest. Once you have selected it, the Output Stream field displays and you can type in the data flow of interest. The data flow to be processed must be added to the flow in order for this component to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of writing manually, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  For further information about how to use a stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| File Name | Enter the name or path to the output file. This field becomes unavailable once you have selected the Use Output Stream check box.  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Sheet name | Enter the name of the XSL sheet. Information noteWarning: If a subJob contains multiple tFileOutputExcel components that write the same excel file (that is, the File Name options of these components point to the same file), these components overwrite the same xsl sheet and only the data of the tFileOutputExcel component that is the last one to write the excel file remains. To avoid data lost, make sure that these tFileOutputExcel components are in different subJobs. |
| Include header | Select this check box to include a header row to the output file. |
| Append existing file | Select this check box to add the new lines at the end of the file. Append existing sheet: Select this check box to add the new lines at the end of the Excel sheet. |
| Is absolute Y pos. | Select this check box to add information in specified cells: First cell X: cell position on the X-axis (X-coordinate or Abcissa).  First cell Y: cell position on the Y-axis (Y-coordinate).  Keep existing cell format: select this check box to retain the original layout and format of the cell you want to write into. |
| Font | Select in the list the font you want to use. |
| Define all columns auto size | Select this check box if you want the size of all your columns to be defined automatically. Otherwise, select the Auto size check boxes next to the column names you want their size to be defined automatically. |
| Protect file | Select this check box and enter the password in the Password field to protect the file using a password. This component encrypts files using agile encryption (which currently uses the AES 128 algorithm). For more information about agile encryption, see [Apache POI - Encryption support](https://poi.apache.org/encryption.html) and [Encryption](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-offcrypto/2d1c4f2c-7a2a-4133-998f-f3373f00d542).  This option is available when Write excel2007 file format(xlsx) is selected and Use Output Stream is not selected. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository. This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Create directory if does not exist | This check box is selected by default. This option creates the directory that will hold the output files if it does not already exist. |
| Custom the flush buffer size | Select this check box to set the maximum number of rows in the Row number field that are allowed in the buffer. Available when Write excel2007 file format (xlsx) is selected in the Basic settings view. |
| Advanced separator (for numbers) | Select this check box to modify the separators you want to use for numbers: Thousands separator: define separators for thousands.  Decimal separator: define separators for decimals. |
| Truncate characters exceeding max cell length | Select this option to truncate a string that is more than 32767 characters in length to the maximum length allowed by an cell (that is, 32767 characters) before exporting the string to a cell. This option prevents Job failures caused by exporting large amount of data to single excel cells. Also note that this option may result in data losses. This option is for Excel 2007 (and higher versions) files and is available when Write excel2007 file format (xlsx) is selected in the Basic settings view.  This option is not selected by default. |
| Encoding | Select the encoding type from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| Don't generate empty file | Select the check box to avoid the generation of an empty file. |
| Recalculate formula | Select this check box if you need to recalculate formula(s) in the specified Excel file. This check box appears only when you select all these three check boxes: Write excel2007 file format(xlsx), Append existing file, and Append existing sheet. |
| Streaming append | Select this option to write data to an existing excel2007 file in streaming mode. Select this option when you want to write large volumes of data at limited memory. This option preserves existing static formatting of data, however more advanced formatting and validation rules might be cleared when using it.  This option is available when the Write excel2007 file format (xlsx) option and the Append existing file option are selected in the Basic settings view. |
| Use shared strings table | Select this option to use a shared strings table when creating an XLSX file. This option provides a tradeoff between performance and file size. It works fine when creating XLSX files that contain many duplicated strings. It is available when Write excel2007 file format (xlsx) is selected and Append existing file is not selected in the Basic settings view.  Note that 1904 date format will be ignored if the schema contains a dynamic column and the component works in the memory-consuming mode.  Information noteNote: This option is available only when you have installed the 8.0.1-R2023-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to write an MS Excel file with data passed on from other components using a Row link. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your HDFS connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access files in different HDFS systems or different distributions, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of *Talend Studio*.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Extracting data from an Excel file using a dynamic schema](extracting-data-from-excel-file-using-dynamic-schema-c "This scenario extracts data from an Excel 2007 file. It demonstrates the use of dynamic schema.")
