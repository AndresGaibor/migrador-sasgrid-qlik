<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldif/tfileoutputldif · versión 8.0 -->
# tFileOutputLDIF

Last updated: 9/30/2026

Writes or modifies an LDIF file with data separated in respective entries based on
the schema defined, or else deletes content from an LDIF file.

tFileOutputLDIF outputs data to an
LDIF type of file which can then be loaded into an LDAP directory.

## tFileOutputLDIF Standard properties

These properties are used to configure tFileOutputLDIF running in the Standard Job framework.

The Standard
tFileOutputLDIF component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| File Name | Specify the path to the LDIF output file.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Wrap | Specify the number of characters at which the line will be wrapped. |
| Change type | Select a changetype that defines the operation you want to perform on the entries in the output LDIF file.  * Add: the LDAP   operation for adding the entry. * Modify: the LDAP   operation for modifying the entry. * Delete: the LDAP   operation for deleting the entry. * Modrdn: the LDAP   operation for modifying an entry's RDN (Relative   Distinguished Name). * Default: the default   LDAP operation. |
| Multi-Values / Modify Detail | Specify the attributes for multi-value fields when Add or Default is selected from the Change type list or provide the detailed modification information when Modify is selected from the Change type list.   * Column: The Column cells are automatically filled with   the defined schema column names. * Operation: Select an   operation to be performed on the corresponding field. This   column is available only when Modify is selected from the Change type list. * MultiValue: Select the   check box if the corresponding field is a multi-value   field. * Separator: Specify the   value separator in the corresponding multi-value   field. * Binary: Select the check   box if the corresponding field represents binary   data. * Base64: Select the check   box if the corresponding field should be base-64 encoded.   The base-64 encoded data in the LDIF file is represented by   the :: symbol.   This table is available only when Add, Modify, or Default is selected from the Change type list. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Sync columns | Click to synchronize the output file schema with the input file schema. The Sync function only displays once the Row connection is linked with the Output component. |
| Append | Select this check box to add the new rows at the end of the file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Enforce safe base 64 conversion | Select this check box to enable the safe base-64 encoding. For more detailed information about the safe base-64 encoding, see <https://www.ietf.org/rfc/rfc2849.txt>. |
| Create directory if not exists | This check box is selected by default. It creates the directory that holds the output delimited file, if it does not already exist. |
| Custom the flush buffer size | Select this check box to specify the number of lines to write before emptying the buffer. |
| Row number | Type in the number of lines to write before emptying the buffer.  This field is available only when the Custom the flush buffer size check box is selected. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| Don't generate empty file | Select this check box if you do not want to generate empty files. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used to write an LDIF file with data passed on from an input component using a Row > Main connection. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Writing data from a database table into an LDIF file](tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-writing-data-from-database-table-into-ldif-file-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-writing-data-from-database-table-into-ldif-file-standard-component-this -->
# Writing data from a database table into an LDIF file

Last updated: 9/30/2026

This scenario describes a Job that loads data into a database table, and then
extracts the data from the table and writing the data into a new LDIF file.

### In this section

* [Adding and linking components](/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tFileOutputLDIF](tfileoutputldif "Writes or modifies an LDIF file with data separated in respective entries based on the schema defined, or else deletes content from an LDIF file.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)
* [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-adding-and-linking-components-standard-component-create -->
# Adding and linking components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in
   the design workspace or dropping them from the Palette: a tFixedFlowInput
   component, a tMysqlOutput component, a
   tMysqlInput component, and a tFileOutputLDIF component.
2. Link tFixedFlowInput to tMysqlOutput using a Row > Main
   connection.
3. Link tMysqlInput to tFileOutputLDIF using a Row
   > Main connection.
4. Link tFixedFlowInput to tMysqlInput using a Trigger > On Subjob Ok
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Loading data into a database table](/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-loading-data-into-database-table-standard-component)
* [Extracting data from the database table and writing it into an LDIF file](/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-extracting-data-from-database-table-and-writing-it-into-ldif-file-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The LDIF file created contains the data from the database table and the
   change type for the entries is set to add.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-extracting-data-from-database-table-and-writing-it-into-ldif-file-standard-component -->
# Extracting data from the database table and writing it into an LDIF file

Last updated: 9/30/2026

## Procedure

1. Double-click tMysqlInput to open its
   Basic settings view.
2. Fill in the Host, Port, Database, Username, and Password fields with your MySQL database connection
   details.
3. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding four columns: *dn*,
   *id\_owners*, *registration*, and *make*,
   all of String type.
4. In the Table Name field, enter the name
   of the table from which the data will be read. In this example, it is
   *ldifdata*.
5. Click the Guess Query button to fill in
   the Query field with the auto-generated
   query.
6. Double-click tFileOutputLDIF to open its
   Basic settings view.
7. In the File Name field, browse to or
   enter the path to the LDIF file to be generated. In this example, it is
   *E:/out.ldif*.
8. Select the operation Add from the
   Change type list.
9. Click the Sync columns button to retrieve
   the schema from the preceding component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldif/tfileoutputldif-tfixedflowinput-tmysqlinput-tmysqloutput-loading-data-into-database-table-standard-component -->
# Loading data into a database table

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding four columns: *dn*,
   *id\_owners*, *registration*, and *make*,
   all of String type.
3. Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
4. In the Mode area, select Use Inline Content(delimited file), and then in
   the Content field displayed, enter the
   following input
   data:24;24;5382 KC 94;Volkswagen
   32;32;9591 0E 79;Honda
   35;35;3129 VH 61;Volkswagen
5. Double-click tMysqlOutput to open its
   Basic settings view.
6. Fill in the Host, Port, Database, Username, and Password fields with your MySQL database connection
   details.
7. In the Table field, enter the name of the
   table into which the data will be written. In this example, it is *ldifdata*.
8. Select Drop table if exists and create
   from the Action on table drop-down
   list.
