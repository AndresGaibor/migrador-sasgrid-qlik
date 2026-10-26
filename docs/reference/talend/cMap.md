<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-map/cmap · versión 8.0 -->
# cMap

Last updated: 9/30/2026

Information noteNote: This component is not shipped with your
Talend Studio by
default. To use it, you need to install the Data Mapper > Talend Data Mapper feature using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

Executes transformations (called maps) between different sources and destinations
by harnessing the capabilities of *Talend Data Mapper*, available in the 
Mapping
 perspective.

cMap transforms data from a wide range of sources to a
wide range of destinations. If you want to use multiple inputs and/or outputs, you must use
*Talend Data Mapper* I/O functions. For more information, see [Input/Output expressions](/talend/r/en-US/8.0/data-mapper-user-guide/input-output-expressions).

## cMap Standard properties

These properties are used to configure cMap running in the Standard Job framework.

The Standard
cMap component belongs to the Transformation family.

The component in this framework is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Open Map Editor | Click the [...] button to open the Structure Generate/Select wizard.  You can first select the type of map to create:  * Standard Map: Map that perform mappings using   functions based on xQuery * DSQL Map: Map that performs mappings using   Data Shaping Query Language.  You can select the Don't ask me again check box to save this preference. For more information about these map types, see [Working with maps](/talend/r/en-US/8.0/data-mapper-user-guide/working-with-maps). Information noteNote: This option is available only if you have installed the R2023-10 Studio monthly update or a later one delivered by Talend. For more information, check with your administrator.  Then you can either have the hierarchical mapper structure generated automatically based on the schema, or select an existing hierarchical mapper structure. You must do this for both the input and output sides of your Map. The following lists the options for the output structure:  * Generate hierarchical mapper structure based on the   schema option: When you connect multiple output   connections to the tHMap, the page displays a confirmation message   that informs you that the mapper structures are generated based on   the output connections. * Select an existing hierarchical mapper   structure option: You can connect multiple outputs   that are payload-based connections to the tHMap. If there is a   single payload-type connection, you can select the Allow   support for multiple output connections check box.   The generated output map inherits from the existing payload   structure.  If Talend Studio detects multiple output connections available, the window displays both output structure options without the support for multiple output connections check boxes.  If neither input nor output connection exists, the Structure Selection page is displayed. |
| Map Path | Specifies the map to be executed.  Click the [...] button next to the Map Path field to open a dialog box in which you can select the map you want to use, then click the [...] button next to Open Map Editor to work with the map selected. Note that this map must have previously been created in the  Mapping  perspective. |
| Output Type | From the drop-down list, select how you want the output to be written.   * Default: The default   output is the same as the input, or Java if the map outputs   Java. * String: Use this option   if the data in the output column is to be a   String. * Byte Array: Use this   option if the data in the output column is to be a   Byte array. * InputStream: Use this option if you   are working with Talend Data Mapper metadata and the input is a stream. * Object: Use this option to produce a collection of   Avro GenericRecord objects. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use old Eclipse runtime (deprecated) | Select this check box to include the old Eclipse runtime in your Route. Information noteNote: This option is available only if you have installed the R2024-03 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Exception Threshold | *Talend Data Mapper* returns an execution status with an severity value which can be OK, Info, Warning, Error or Fatal. By setting the exception threshold, you can specify the severity level at which an exception is thrown, thus enabling downstream components to detect the error in cases other than the default value of Fatal.  From the drop-down list, select the severity level at which an exception may be thrown during the execution of a map.   * Fatal (default): An   exception is thrown when a fatal error occurs. * Error: An exception is   thrown when an error (or higher) occurs. * Warning: An exception is   thrown when a warning (or higher) occurs. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cMap is used for Routes that require data mapping. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules).  This limitation applies to maps that reference databases. |

Information noteNote:

* For further information about performing transformations using *Talend Data Mapper*, see [Talend Data Mapper User Guide](/talend/r/en-US/8.0/data-mapper-user-guide).
* When using representations other than Map, CSV, Avro, XML, and Cobol,
  running this component with the old Eclipse-based Runtime may create temporary
  folders, which are not automatically removed after stopping the Runtime. If you
  frequently run Talend Data Mapper,
  these files may pile up and eventually lead to a disk full error. When the error
  occurs, the runtime fails. To avoid this, ensure that you perform periodical
  cleaning. For more information, see [Cleaning up temporary folders and
  files](/talend/r/en-US/8.0/data-mapper-user-guide/cleaning-up-temporary-folders-and-files).

**Related concepts**  

* [Mapping data with cMap](cmap-cfile-mapping-data-with-cmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-mapping-data-with-cmap -->
# Mapping data with cMap

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

The following scenario creates a three-component Route, in which a cFile component visits a local file directory to copy its
contents, performs a transformation using a cMap
component, and then sends the files in the input directory to an output cFile component that writes the files in another
directory.

### In this section

* [Copying an editable version of the example files](/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-copying-editable-version-of-example-files)
* [Adding and linking the components](/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-adding-and-linking-components)
* [Defining the properties of cFile\_1](/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-defining-properties-of-cfile-1)
* [Defining the properties of cMap](/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-defining-properties-of-cmap)
* [Defining the properties of cFile\_2](/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-defining-properties-of-cfile-2)
* [Saving and executing the Route](/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-saving-and-executing-route)

**Related reference**  

* [cMap](cmap "Executes transformations (called maps) between different sources and destinations by harnessing the capabilities of Talend Data Mapper , available in the Mapping perspective.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-adding-and-linking-components -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Click the point in the design workspace where you want to add the first
   component, start typing cFile, and then click
   the name of the component when it appears in the list proposed in order to
   select it.
2. Do the same to add a cMap component and a
   second cFile component as well.
3. Connect the cFile\_1 component to the
   cMap component using a Row > Route link, then connect the cMap component to the cFile\_2 component using a second Row >
   Route link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-defining-properties-of-cfile-1 -->
# Defining the properties of cFile\_1

Last updated: 9/30/2026

## Procedure

1. Select the cFile\_1 component to define its
   properties.
2. In the Path field, browse to or enter the
   path to where the input file is located.
3. In the fileName field, enter the name of the
   input file: *PayPalPO.csv* in this
   example.
4. Leave the other parameters unchanged.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-defining-properties-of-cfile-2 -->
# Defining the properties of cFile\_2

Last updated: 9/30/2026

## Procedure

1. Select the cFile\_2 component to define its
   properties.
2. In the Path field, browse to or enter the
   path to where the output file is to be located.
3. In the fileName field, enter a name for the
   output file with the extension *.xml*.
4. Leave the other parameters unchanged.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-defining-properties-of-cmap -->
# Defining the properties of cMap

Last updated: 9/30/2026

## Procedure

1. Select the cMap component to define its
   properties.
2. Click the [...] button next to the Map Path field to open the picker and select the map
   to use, *Maps/CSV/POPayPalCsv\_PO2*, then click
   OK. This map transforms a CSV file into an
   XML file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-map/cmap-cfile-saving-and-executing-route -->
# Saving and executing the Route

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Route.
2. In the Run tab, click Run to execute the Route.
3. Browse to the output directory on your file system to check that the input
   files have been transformed and written in the output directory.
