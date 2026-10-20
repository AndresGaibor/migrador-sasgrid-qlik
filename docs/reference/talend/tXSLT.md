<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml/txslt · versión 8.0 -->
# tXSLT

Last updated: 9/30/2026

Helps to transform data structure to another structure.

This component refers to an XSL stylesheet, to transform an XML source file
into a defined output file.

## tXSLT Standard properties

These properties are used to configure tXSLT running in the Standard Job framework.

The Standard
tXSLT component belongs to the XML family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| XML file/stream | File path to the XML file or data flow to be validated. Note that in the case of stream, the data must be added to the flow for the component to fetch the data through the corresponding variable.  The data flow to be processed must be added to the flow in order for this component to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  For further information about how to use a stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this).  Information noteNote: This field is not available if you select the Use column instead of file/stream for XML option. |
| XSL file/stream | File path to the reference XSL transformation file or transformation data flow. Note that in the case of stream, the data must be added to the flow for the component to fetch the data through the corresponding variable.  The data flow to be processed must be added to the flow in order for this component to fetch these data via the corresponding representative variable.  This variable can be already pre-defined in Talend Studio or provided by the context or the components you are using along with this component; otherwise, you can define it manually and use it according to the design of your Job, for example, using tJava or tJavaFlex.  In order to avoid the inconvenience of hand writing, you could select the variable of interest from the auto-completion list (Ctrl+Space) to fill the current field on condition that this variable has been properly defined.  For further information about how to use a stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this).  Information noteNote: This field is not available if you select the Use column instead of file/stream for XSL option. |
| Output file | File path to the output file. If the file does not exist, it will be created. The output file can be any structured or unstructured file such as html, xml, txt or even pdf or edifact depending on your xsl.  Information noteNote: This field is not available if you select the Use column instead of File for Result option. |
| Parameters | Click the plus button to add new lines in the Parameters list and define the transformation parameters of the XSLT file. Click in each line and enter the key in the *name* list and its associated value in the *value* list. |
| Use column instead of file/stream for XML | Select this option to use the data of a specified column as the input. You need to specify the column to which the input data is passed to in the Input column for XML drop-down list. |
| Use column instead of file/stream for XSL | Select this option to use the data of a specified column as the XSL. You need to specify the column to which the XSL data is passed to in the Input column for XSL drop-down list. |
| Use column instead of File for Result | Select this option to output the transformed data to a specified column. You need to specify the column to which the transformed data is passed to in the Input column for result drop-down list. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.   * Built-in: The schema will be created and stored locally for   this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists and is stored in the   Repository, hence can be reused in various projects and Job flowcharts. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the Output component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  OUTPUT\_FILEPATH: the output file path. This is a Flow variable and it returns a string.  OUTPUT\_FILENAME: the output file name. This is a Flow variable and it returns a string.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as standalone component. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Transforming stream into HTML using an XSL stylesheet](transforming-stream-to-html-using-xsl-stylesheet-standard-component "The tXSLT component provides support for streams. It can receive XML files or XSL files passed to it in the form of stream and, in addition to sending the output to files, it can send the output to the subsequent component through a Row > Main connection. The tXSLT component in this scenario receives the XML file from a tFileInputRaw component in the form of stream and sends its output to a tLogRow component through a predefined column.")
* [Transforming XML into HTML using an XSL stylesheet](txslt-tmsgbox-transforming-xml-to-html-using-xsl-stylesheet-standard-component "This scenario describes a two-component Job that converts XML data into an HTML document using an XSL stylesheet. It also defines a transformation parameter of the XSL stylesheet to change the background color of the header of the HTML document created.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml/txslt-tmsgbox-transforming-xml-to-html-using-xsl-stylesheet-standard-component -->
# Transforming XML into HTML using an XSL stylesheet

Last updated: 9/30/2026

This scenario describes a two-component Job that converts XML data into an HTML
document using an XSL stylesheet. It also defines a transformation parameter of the XSL
stylesheet to change the background color of the header of the HTML document created.

This scenario uses two input files: customers.xml and
customers.xsl.

The content of the customers.xml file is as
follows.

```
<?xml version="1.0" encoding="UTF-8"?>
<Customers>
    <Customer RegisterTime="2001-01-17 06:26:40.000">
        <Name>
            <id>1</id>
            <CustomerName>Griffith Paving and Sealcoatin</CustomerName>
        </Name>
        <Address>
            <CustomerAddress>talend@apres91</CustomerAddress>
            <idState>2</idState>
        </Address>
        <Revenue>
            <Sum1>67852</Sum1>
        </Revenue>
    </Customer>
    <Customer RegisterTime="2002-06-07 09:40:00.000">
        <Name>
            <id>2</id>
            <CustomerName>Bill's Dive Shop</CustomerName>
        </Name>
        <Address>
            <CustomerAddress>511 Maple Ave. Apt. 1B</CustomerAddress>
            <idState>3</idState>
        </Address>
        <Revenue>
            <Sum1>88792</Sum1>
        </Revenue>
    </Customer>
    <Customer RegisterTime="1987-02-23 17:33:20.000">
        <Name>
            <id>3</id>
            <CustomerName>Glenn Oaks Office Supplies</CustomerName>
        </Name>
        <Address>
            <CustomerAddress>1859 Green Bay Rd.</CustomerAddress>
            <idState>2</idState>
        </Address>
        <Revenue>
            <Sum1>1225.</Sum1>
        </Revenue>
    </Customer>
    <Customer RegisterTime="1992-04-28 23:26:40.000">
        <Name>
            <id>4</id>
            <CustomerName>DBN Bank</CustomerName>
        </Name>
        <Address>
            <CustomerAddress>456 Grossman Ln.</CustomerAddress>
            <idState>3</idState>
        </Address>
        <Revenue>
            <Sum1>64493</Sum1>
        </Revenue>
    </Customer>
    <Customer RegisterTime="1999-04-26 23:26:44.000">
        <Name>
            <id>5</id>
            <CustomerName>Facelift Kitchen and Bath</CustomerName>
        </Name>
        <Address>
            <CustomerAddress>220 Vine Ave.</CustomerAddress>
            <idState>10</idState>
        </Address>
        <Revenue>
            <Sum1>888888</Sum1>
        </Revenue>
    </Customer>
</Customers>
```

The content of the customer.xsl file is as
follows.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:param name="bgcolor"/>
    <xsl:template match="/">
        <html>
            <body>
                <h2>Customers</h2>
                <table border="1">
                    <tr bgcolor="{$bgcolor}">
                        <th>ID</th>
                        <th>Name</th>
                        <th>Address</th>
                    </tr>
                    <xsl:for-each select="Customers/Customer">
                        <tr>
                            <td><xsl:value-of select="Name/id"/></td>
                            <td><xsl:value-of select="Name/CustomerName"/></td>
                            <td><xsl:value-of select="Address/CustomerAddress"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
```

### In this section

* [Procedure](/talend/en-US/components/8.0/xml/txslt-tmsgbox-procedure-standard-component-drop)

**Related reference**  

* [tXSLT](txslt "Helps to transform data structure to another structure.")

**Related information**  

* [tMsgBox](/talend/en-US/components/8.0/tmsgbox/tmsgbox)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/xml/txslt-tmsgbox-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop the tXSLT and tMsBox components from the Palette to the design workspace.
2. Double-click tXSLT to open its Basic settings view where you can define the
   component properties.
3. In the XML file field, set the
   path or browse to the customers.xml file. The XML file holds a
   list of customers and related information including customer name, customer address
   etc.
4. In the XSL file field in the
   Basic settings view, set the path or browse
   to the customers.xsl file.
5. In the Output file field, set
   the path or browse to the output HTML file (customers.html in
   this scenario).

   In this example, we want to convert the XML data into an HTML file
   containing a table heading followed by a table listing customer IDs, customer names,
   and customer addresses.
6. In the Parameters area of
   the Basic settings view, click the plus button
   to add a line where you can define the name and value of the transformation parameter
   of the XSL file. In this example, enter `"bgcolor"` as the
   transformation parameter name and `"green"` as the parameter
   value to set the background color of the table head in the HTML file.
7. Double-click the tMsgBox to display its
   Basic settings view and define its display
   properties as needed.
8. Save the Job and press F6 to execute it. The
   message box displays confirming that the output html file is created and stored
   in the defined path.
9. Click OK to close the message box.

## Results

You can now open the output html file to check the transformation of the
XML data and that of the background color of the table heading.
