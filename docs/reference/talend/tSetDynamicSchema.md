<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema · versión 8.0 -->
# tSetDynamicSchema

Last updated: 9/30/2026

Sets a dynamic schema that can be reused by components in the subsequent subJob or
subJobs to retrieve data from unknown columns.

tSetDynamicSchema creates a dynamic schema to allow components that are unable
to guess the structure of the data being handled based on field separators, such as tFileInputPositional and tFileOutputPositional, to retrieve data from unknown columns.

## tSetDynamicSchema Standard properties

These properties are used to configure tSetDynamicSchema running in the Standard Job framework.

The Standard
tSetDynamicSchema component belongs to the Custom Code family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This option is not available if you select the Guess schema from file option or the Read schema from file option. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function is available only when the component is linked with an input component using a Row connection. |
| Guess schema from file | Select this option to generate the schema from a csv file. You need to enter the path to the csv file in the Filename field manually or by clicking the [...] button and navigating to the csv file.  This option is not available if the component is linked with an input component using a Row connection or if you select the Read schema from file option. |
| Read schema from file | Select this option to generate the schema from a schema definition file. You need to enter the path to the schema definition file in the Filename field manually or by clicking the [...] button and navigating to the file.  Information noteNote:  * A schema definition file needs to be a csv file. * A schema definition file contains a header line and multiple column   definitions, with each column definition occupies one line in the file.   It can contain column definitions of multiple tables. * The header line contains multiple fields. The value of a field can only   be an option of the Property drop-down list in the   Parameters table (case sensitive). * When the schema of this component is used by a tSAPTableInput component,   the value of a ExtendedConfiguration field needs   to be in the format of   `{"TableName":"{your_table_name}"}.` * This option is available only when you have installed the 8.0.1-R2022-04   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  This option is not available if the component is linked with an input component using a Row connection or if you select the Guess schema from file option. |
| Parameters | This table contains two columns.   * Property: Property of the schema   entry: `ColumnName`, `DBName`,   `Type`, `DBType`,   `Length`, `Precision`,   `Nullable`, `Key`, or   `ExtendedConfiguration`. * Value: Value assigned to this   property.   This option is not available if you select the Guess schema from file option or the Read schema from file option.  Information noteNote:  * The `ExtendedConfiguration` property is available   only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. * The use of the `ExtendedConfiguration` property   varies with the component that uses the schema of this component. When   used with a tSAPTableInput component, this property holds table names and   the value needs to be in the format of   `{"TableName":"{your_table_name}"}`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Row limit | Specify the number of rows in the csv file to guess schema from.  This field is available if you select the Guess schema from file option in the Basic settings view. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | DYNAMIC: the last row of the data retrieved using the defined dynamic schema. This is an After variable and it returns a dynamic.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as the end component or be used independently in a subJob. |
| Limitation | To work with tSetDynamicSchema, components should have the option of Use existing dynamic, which allows you to select the tSetDynamicSchema component from the list. |

**Related concepts**  

* [Handling a positional file based on a dynamic schema](tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-handling-positional-file-based-on-dynamic-schema-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-handling-positional-file-based-on-dynamic-schema-standard-component-enterprise-this -->
# Handling a positional file based on a dynamic schema

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

This scenario describes a four-component Job that reads data from a positional
file, writes the data to another positional file, and replaces the padding characters with
space. The schema column details are not defined in the positional file components; instead,
they leverages a reusable dynamic schema. The input file used in this scenario is as
follows:

```
id----name--------city--------
1-----Andrews-----Paris-------
2-----Mark--------London------
3-----Marie-------Paris-------
4-----Michael-----Washington--
```

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-dropping-and-linking-components-standard-component-enterprise-drop?id=1720)
* [Configuring the first subJob: creating a dynamic schema](/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-configuring-first-subjob-creating-dynamic-schema-standard-component-enterprise?id=1721)
* [Configuring the second subJob: reading and writing positional data](/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-configuring-second-subjob-reading-and-writing-positional-data-standard-component-enterprise?id=1722)
* [Saving and executing the Job](/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-saving-and-executing-job-standard-component-enterprise-press?id=1723)

**Related concepts**  

* [tFileInputPositional](tfileinputpositional "Reads a positional file row by row to split them up into fields based on a given pattern and then sends the fields as defined in the schema to the next component.")
* [tFileOutputPositional](tfileoutputpositional "Writes a file row by row according to the length and the format of the fields or columns in a row.")

**Related information**  

* [tSetDynamicSchema](/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-configuring-first-subjob-creating-dynamic-schema-standard-component-enterprise -->
# Configuring the first subJob: creating a dynamic schema

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowInput component to show its Basic settings view and define its
   properties.
2. Click the [...] button
   next to Edit schema to open the Schema dialog box.
3. Click the [+] button to
   add three columns: *ColumnName*, *ColumnType*, and *ColumnLength*, and set their
   types to String, String, and Integer respectively to define the minimum properties required
   for a positional file schema. Then, click OK to close the dialog box.
4. Select the Use Inline
   Table option, click the [+] button three times to add three lines, give them a name in
   the ColumnName field, according to the
   actual columns of the input file to read: *ID*, *Name*, and *City*, set their types
   in the corresponding ColumnType field: *id\_Interger* for column *ID*, and *id\_String* for columns *Name* and *City*, and set the length values of the columns in the
   corresponding ColumnLength field. Note
   that the column names you give in this table will compose the header of the
   output file.
5. Double-click the tSetDynamicSchema component to open its Basic settings view.
6. Click Sync columns to
   ensure that the schema structure is properly retrieved from the preceding
   component.
7. Under the Parameters
   table, click the [+] button to add three
   lines in the table.
8. Click in the Property
   field for each line, and select ColumnName, Type, and
   Length respectively.
9. Click in the Value field
   for each line, and select ColumnName,
   ColumnType, and ColumnLength respectively. 

   Now, with the values set in the inline table of the tFixedFlowInput component retrieved, the
   following data structure is defined in the dynamic schema:

   | Column Name | Type | Length |
   | --- | --- | --- |
   | ID | Integer | 6 |
   | Name | String | 12 |
   | City | String | 12 |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-configuring-second-subjob-reading-and-writing-positional-data-standard-component-enterprise -->
# Configuring the second subJob: reading and writing positional data

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputPositional
   component to open its Basic settings
   view.

   Information noteWarning:

   *The dynamic schema feature is only supported in Built-In mode and requires the input file
   to have a header row.*
2. Select the Use existing dynamic check
   box, and in from the Component List that
   appears, select the tSetDynamicSchema
   component you use to create the dynamic schema. In this use case, only one
   tSetDynamicSchema component is used, so
   it is automatically selected.
3. In the File name/Stream field, enter the
   path to the input positional file, or browse to the file path by clicking
   the [...] button.
4. Fill in the Header, Footer and Limit fields
   according to your input file structure and your need. In this scenario, we
   only need to skip the first row when reading the input file. To do this,
   fill the Header field with *1* and leave the other fields as they are.
5. Click the [...] button next to Edit schema to open the Schema dialog box, define only one column, *dyn* in this example, and select Dynamic from the Type list. Then, click OK
   to close the Schema dialog box and
   propagate the changes.
6. Select the Customize check box, enter
   '-' in the Padding char
   field, and keep the other settings as they are.
7. Double-click the tFileOutputPositional
   component to open its Basic settings
   view.
8. Select the Use existing dynamic check
   box, specify the output file path, and select the Include header check box.
9. In the Padding char field, enter '
   ' so that the padding characters will be replaced with space in
   the output file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-dropping-and-linking-components-standard-component-enterprise-drop -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tSetDynamicSchema, tFileInputPositional, and tFileOutputPositional.
2. Connect the tFixedFlowInput component to
   the tSetDynamicSchema using a Row > Main
   connection to form a subJob. This subJob will define a reusable dynamic
   schema.
3. Connect the tFileInputPositional
   component to the tFileOutputPositional
   component using a Row > Main connection to form another subJob. This
   subJob will read data from the input positional file and write the data to
   another positional file based on the dynamic schema set in the previous
   subJob.
4. Connect the tFixedFlowInput component to
   the tFileInputPositional component using a
   Trigger > On
   Subjob Ok connection to link the two subJobs together.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/dynamic-schema/tsetdynamicschema-tfileinputpositional-tfileoutputpositional-tfixedflowinput-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job to ensure
   that all the configured parameters take effect.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The data is read from the input positional file and written into the
   output positional file, with the padding characters replaced by
   space.
