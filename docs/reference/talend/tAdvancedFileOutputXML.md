<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tadvancedfileoutputxml · versión 8.0 -->
# tAdvancedFileOutputXML

Last updated: 9/30/2026

Writes an XML file with separated data values according to an XML tree
structure.

tAdvancedFileOutputXML outputs data to an XML type of
file and offers an interface to deal with loop and group by elements if needed.

## tAdvancedFileOutputXML Standard properties

These properties are used to configure tAdvancedFileOutputXML running in the Standard Job framework.

The Standard
tAdvancedFileOutputXML component belongs to the File and the XML families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the Repository file   where Properties are stored. The following fields are pre-filled in using fetched   data. |
| Use Output Stream | Select this check box process the data flow of interest. Once you have selected it, the Output Stream field displays and you can type in the data flow of interest. The data flow to be processed must be added to the flow in order for this component to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  For further information about how to use a stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| File name | Name or path to the output file and/or the variable to be used. This field becomes unavailable once you have selected the Use Output Stream check box.  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |
| Configure XML tree | Opens the dedicated interface to help you set the XML mapping. For details about the interface, see [Defining the XML tree](/talend/en-US/components/8.0/xml-connectors/defining-xml-tree). |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields that will be   processed and passed on to the next component. The schema is either built-in or   remote in the Repository. Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema will be created   and stored locally for this component only. For more information about a component   schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists   and is stored in the Repository, hence can be reused in various projects and Job   designs. For more information about a component schema in its Basic   settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the Output component. |
| Append the source xml file | Select this check box to add the new lines at the end of your source XML file. |
| Generate compact file | Select this check box to generate a file that does not have any empty space or line separators. All elements then are presented in a unique line and this will reduce considerably file size. |
| Include DTD or XSL | Select this check box to to add the DOCTYPE declaration, indicating the root element, the access path and the DTD file, or to add the processing instruction, indicating the type of stylesheet used (such as XSL types), along with the access path and file name. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Split output in several files | If the XML file output is big, you can split the file every certain number of rows. |
| Trim data | This check box is activated when you are using the dom4j generation mode. Select this check box to trim the leading or trailing whitespace from the value of a XML element. |
| Create directory only if not exists | This check box is selected by default. It creates a directory to hold the output XML files if required. |
| Create empty element if needed | This box is selected by default. If no column is associated to an XML node, this option will create an open/close tag in place of the expected tag. |
| Create attribute even if its value is NULL | Select this check box to generate XML tag attribute for the associated input column whose value is null. |
| Create attribute even if it is unmapped | Select this check box to generate XML tag attribute for the associated input column that is unmapped. |
| Create associated XSD file | If one of the XML elements is defined as a Namespace element, this option will create the corresponding XSD file. This option is available only when the generation mode is set to Slow and memory-consuming (Dom4j) in the Advanced settings tab. |
| Add Document type as node | Select this check box to add column(s) of the Document type as node(s) instead of escaped string(s) in the output XML file. This option is available only when the generation mode is set to Slow and memory-consuming (Dom4j) in the Advanced settings tab. |
| Advanced separator (for number) | Select this check box to change the expected data separator. Thousands separator: define the thousands separator, between inverted commas  Decimal separator: define the decimals separator between inverted commas |
| Generation mode | Select the appropriate generation mode according to your memory availability. The available modes are:  * Slow and memory-consuming   (Dom4j) Information noteNote: This option allows you to use dom4j to process the XML   files of high complexity. * Fast with low memory   consumption   This option is not available if Append the source xml file is selected in the Basic settings view, because in this situation, the generation mode is set automatically as dom4j. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| Don't generate empty file | Select the check box to avoid the generation of an empty file. |
| Add blank line after XML declaration | This option is selected by default to add a blank line right after the XML declaration in the generated XML file. If not selected, no line is added to the file. This option is not available if Generate compact file is selected in the Basic settings view. |
| tStatCatcher Statistics | Select the check box to collect the log data at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to write an XML file with data passed on from other components using a Row link. |

**Related concepts**  

* [The Append the source XML file feature](appending-records-to-xml-file)
* [Creating an XML file using a loop](tadvancedfileoutputxml-tfileinputdelimited-creating-xml-file-using-loop-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tadvancedfileoutputxml-tfileinputdelimited-creating-xml-file-using-loop-standard-component-the -->
# Creating an XML file using a loop

Last updated: 9/30/2026

The following scenario describes the creation of an XML file from a sorted flat file
gathering a video collection.

### In this section

* [Configuring the source file](/talend/en-US/components/8.0/xml-connectors/tadvancedfileoutputxml-tfileinputdelimited-configuring-source-file-standard-component-drop)
* [Configuring the XML output and mapping](/talend/en-US/components/8.0/xml-connectors/tadvancedfileoutputxml-tfileinputdelimited-configuring-xml-output-and-mapping-standard-component-then)

**Related reference**  

* [tAdvancedFileOutputXML](tadvancedfileoutputxml "Writes an XML file with separated data values according to an XML tree structure.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tadvancedfileoutputxml-tfileinputdelimited-configuring-source-file-standard-component-drop -->
# Configuring the source file

Last updated: 9/30/2026

## Procedure

1. Drop a tFileInputDelimited and a tAdvancedFileOutputXML from the Palette onto the design workspace.
2. Alternatively, if you configured a description for the input delimited file in
   the Metadata area of the Repository, then you can directly drag & drop the metadata
   entry onto the editor, to set up automatically the input flow.
3. Right-click on the input component and drag a row main link towards the
   tAdvancedFileOutputXML component to
   implement a connection.
4. Select the tFileInputDelimited
   component and display the Component settings
   tab located in the tab system at the bottom of Talend Studio.
5. Select the Property type, according to
   whether you stored the file description in the Repository or not. If you dragged
   & dropped the component directly from the Metadata, no changes to the
   setting should be needed.

   If you didn't setup the file description in the Repository, then select Built-in and manually fill out the fields displayed on the
   Basic settings vertical tab.

   The input file contains the following type of columns separated by
   semi-colons: *id*, *name*,
   *category*, *year*,
   *language*, *director* and
   *cast*.

   In this simple use case, the Cast field
   gathers different values and the id increments when changing movie.
6. If needed, define the tFileDelimitedInput
   schema according to the file structure.
7. Once you checked that the schema of the input file meets your expectation,
   click on OK to validate.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml-connectors/tadvancedfileoutputxml-tfileinputdelimited-configuring-xml-output-and-mapping-standard-component-then -->
# Configuring the XML output and mapping

Last updated: 9/30/2026

## Procedure

1. Select the tAdvancedFileOutputXML component and click on the Component settings tab to configure the basic settings
   as well as the mapping. Note that a double-click on the component will open directly
   the mapping interface.
2. In the File Name field, browse to the file to
   be written if it exists or type in the path and file name that needs to be
   created for the output.

   By default, the schema (file description) is automatically propagated from the
   input flow. But you can edit it if you need.
3. Then click the [...] button or double-click
   on the tAdvancedFileOutputXML component on the
   design workspace to open the dedicated mapping editor. 

   To the left of the interface, are listed the columns from the
   input file description.
4. To the right of the interface, set the XML tree panel to reflect the expected
   XML structure output.

   You can create the structure node by node. For more information about the
   manual creation of an XML tree, see [Defining the XML tree](/talend/en-US/components/8.0/xml-connectors/defining-xml-tree).

   In this example, an XML template is used to populate the XML tree
   automatically.
5. Right-click on the root tag displaying by
   default and select Import XML tree at the end
   of the contextual menu options.
6. Browse to the XML file to be imported and click OK
   to validate the import operation.

   Information noteNote:

   You can import an XML tree from files in XML, XSD and DTD formats.
7. Then drag & drop each column name from the Schema
   List to the matching (or relevant) XML
   tree elements as described in [Mapping XML data](/talend/en-US/components/8.0/xml-connectors/mapping-xml-data-standard-component-click).

   The mapping is shown as blue links between the left and right panels.

   Finally, define the node status where the loop should take place. In this use
   case, the *Cast* being the changing element on which the
   iteration should operate, this element will be the loop element.

   Right-click on the Cast element on the XML tree, and select Set as loop element.
8. To group by movie, this use case needs also a group element to be
   defined.

   Right-click on the Movie parent node of the XML tree, and select Set as group element.

   The newly defined node status show on the corresponding element lines.
9. Click OK to validate the
   configuration.
10. Press F6 to execute the Job.

    The output XML file shows the structure as defined.
