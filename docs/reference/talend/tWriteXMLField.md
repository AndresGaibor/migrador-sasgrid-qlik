<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml/twritexmlfield · versión 8.0 -->
# tWriteXMLField

Last updated: 9/30/2026

Reads an input XML file and extracts the structure to insert it in defined fields
of the output XML file.

## tWriteXMLField Standard properties

These properties are used to configure tWriteXMLField running in the Standard Job framework.

The Standard
tWriteXMLField component belongs to the XML family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Output Column | Select the destination field in the output component where you want to write the XML structure. |
| Configure XML Tree | Opens the interface that supports the creation of the XML structure you want to write in a field. For more information about the interface, see [Defining the XML tree](/talend/en-US/components/8.0/xml-connectors/defining-xml-tree). |
| Schema and Edit Schema | * A schema is a row description, it defines   the number of fields that will be processed and passed on to the next   component. The schema is either built-in or remote in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: You create the schema and   store it locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You already created the   schema and stored it in the Repository, hence can be reused in various   projects and Job flowcharts. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the input component. |
| Group by | Define the aggregation set, the columns you want to use to regroup the data. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Remove the XML declaration | Select this check box if you do not want to include the XML header. |
| Create empty element if needed | This check box is selected by default. If the Related Column in the XML tree editor has null values, or if no column is associated with the XML node, this option creates an open/close tag in the expected place. |
| Ignore service attributes for empty elements | Select this option to prevent the component from generating an XML node if the input node is null but has service attributes (such as @type, @class, and @array).  This option is available when the Create empty element if needed option is not selected. |
| Expand Empty Element if needed(for dom4j) | Select this option to allow a null element to appear in the form of tag pair, e.g. <element></element>. Otherwise, such an element appears as a solo tag, e.g. <element/>. For more information about XML tags, see <http://www.tizag.com/xmlTutorial/xmltag.php>.  Information noteNote: To use this option, you must select the Dom4J generation mode. Available when Create empty element if needed is selected. |
| Create associated XSD file | If one of the XML elements is defined as a Namespace element, this option will create the corresponding XSD file.  Information noteNote: To use this option, you must select the Dom4J generation mode. |
| Advanced separator (for number) | Select this check box if you want to modify the separators used by default for numbers.  Thousands separator: enter between brackets the separators to use for thousands.  Decimal separator: enter between brackets the separators to use for decimals. |
| Generation mode | Select the appropriate generation mode according to your memory availability. The available modes are:   * Slow and memory-consuming   (Dom4j) Information noteNote: This   option allows you to use dom4j to process the XML files of high   complexity. * Fast with low memory   consumption |
| Encoding | Select the encoding type in the list or select Custom and define it manually. This field is compulsory when working with databases. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as intermediate step in a data flow. |

**Related concepts**  

* [Extracting the structure of an XML file and inserting it into the fields of a database table](twritexmlfield-tfileinputxml-tmysqloutput-tmysqloutput-extracting-structure-of-xml-file-and-inserting-it-into-fields-of-database-table-standard-component "This three-component scenario allows to read an XML file, extract the XML structure, and finally outputs the structure to the fields of a database table.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml/twritexmlfield-tfileinputxml-tmysqloutput-tmysqloutput-extracting-structure-of-xml-file-and-inserting-it-into-fields-of-database-table-standard-component -->
# Extracting the structure of an XML file and inserting it into the fields of a database table

Last updated: 9/30/2026

This three-component scenario allows to read an XML file, extract the XML structure,
and finally outputs the structure to the fields of a database table.

### In this section

* [Procedure](/talend/en-US/components/8.0/xml/twritexmlfield-tfileinputxml-tmysqloutput-tmysqloutput-procedure-standard-component-drop)

**Related reference**  

* [tWriteXMLField](twritexmlfield "Reads an input XML file and extracts the structure to insert it in defined fields of the output XML file.")

**Related information**  

* [tFileInputXML](/talend/en-US/components/8.0/xml-connectors/tfileinputxml)
* [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml/twritexmlfield-tfileinputxml-tmysqloutput-tmysqloutput-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFileInputXml, tWriteXMLField,
   and tMysqlOutput.

   Connect the three components using Main
   links.
2. Double-click tFileInputXml to open its
   Basic settings view and define its
   properties.
3. If you have already stored the input schema in the Repository tree view, select Repository first from the Property
   Type list and then from the Schema list to display the Repository
   Content dialog box where you can select the relevant metadata. 

   For more information about storing schema metadata in the
   Repository tree view, [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).
4. If you have not stored the input schema locally, select Built-in in the Property Type
   and Schema fields and fill in the fields that
   follow manually. For more information about tFileInputXML properties, see [tFileInputXML](/talend/en-US/components/8.0/xml-connectors/tfileinputxml).

   If you have selected Built-in, click the
   [...] button next to the Edit schema field
   to open a dialog box where you can manually define the structure of your
   file.
5. In the Look Xpath query field, enter the node
   of the structure where the loop is based. In this example, the loop is based on
   the *customer* node. Column
   in the Mapping table will be automatically
   populated with the defined file content.

   In the Xpath query column, enter between
   inverted commas the node of the XML file that holds the data corresponding to
   each of the Column fields.
6. In the design workspace, click tWriteXMLField
   and then in the Component view,
   click Basic settings to open the relevant view
   where you can define the component properties.
7. Click the [...] button next to the Edit
   schema field to open a dialog box where you can add a line by
   clicking the plus button.
8. Click in the line and enter the name of the output column where you want to
   write the XML content, *CustomerDetails* in this example. 

   Define the type and length in the corresponding fields,
   *String* and *255*in this example.

   Click Ok to validate your output schema and
   close the dialog box.

   In the Basic settings view and from the
   Output Column list, select the column you
   already defined where you want to write the XML content.
9. Click the [...] button next to Configure Xml
   Tree to open the interface that helps to create the XML
   structure.
10. In the Link Target area, click
    *rootTag* and rename it as
    *CustomerDetails*.

    In the Linker source area, drop
    *CustomerName* and *CustomerAddress*
    to *CustomerDetails*. A dialog box displays asking what type
    of operation you want to do.

    Select Create as sub-element of target node
    to create a sub-element of the *CustomerDetails node*.

    Right-click *CustomerName* and select from the contextual
    menu Set As Loop Element.

    Click OK to validate the XML structure you
    defined.
11. Double-click tMysqlOutput to open its
    Basic settings view and define its
    properties.
12. If you have already stored the schema in the DB
    Connection node in the Repository tree view, select Repository from the Schema list
    to display the Repository Content dialog box
    where you can select the relevant metadata. 

    For more information about storing schema metadata in the
    Repository tree view, [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).

    If you have not stored the schema locally, select Built-in in the Property Type
    and Schema fields and enter the database
    connection and data structure information manually. For more information about
    tMysqlOutput properties, see [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput).

    In the Table field, enter the name of the
    database table to be created, where you want to write the extracted XML
    data.

    From the Action on table list, select
    Create table to create the defined
    table.

    From the Action on data list, select Insert
    to write the data.

    Click Sync columns to retrieve the schema
    from the preceding component. You can click the [...] button next to
    Edit schema to view the schema.
13. Save your Job and click F6 to execute it.

## Results

tWriteXMLField fills every field of the
*CustomerDetails* column with the XML structure of the input
file: the XML processing instruction <?xml version=""1.0""
encoding=""ISO-8859-15""?>, the first node that separates each client
<CustomerDetails> and finally customer information
<CustomerAddress> and <CustomerName>.
