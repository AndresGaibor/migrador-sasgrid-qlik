<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-oracle/teltoraclemap · versión 8.0 -->
# tELTOracleMap

Last updated: 9/30/2026

Builds the SQL SELECT statement using the table schema(s) provided by one or more
tELTOracleInput components.

The three ELT Oracle components are closely related, in
terms of their operating conditions. These components should be used to handle Oracle
database table schemas to generate SQL statements, including clauses, which are to be
executed in the database output table defined.

## tELTOracleMap Standard properties

These properties are used to configure tELTOracleMap running in the Standard Job framework.

The Standard
tELTOracleMap component belongs to the ELT family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Make sure that the connection selected is not of the WALLET type to prevent possible errors.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| ELT Oracle Map Editor | The ELT Map editor allows you to define the output schema and make a graphical build of the SQL statement to be executed. The column names of schema can be different from the column names in the database.  On the upper left corner of the ELT Map editor, you can click the Setup the configurations of elt map button to open a dialog box Property Settings which contains two options:   * Add quotes in columns when generating query: With   this check box selected, double quotes will be added for all output column   names to support delimited identifiers. By default, this check box is   cleared. This check box is displayed as Delimited   identifiers if you have not installed the 8.0 R2022-11   Talend Studio monthly update or a later one provided by Talend. * Automatic   alias: With this check box selected, if a schema   column has a different name than its database column, an alias will   be automatically created in the SQL query for that column. By   default, this check box is selected.   You can filter schema columns in an input or output table by clicking the Enable/disable column name filter button in the corresponding table and entering the search keyword in the field displayed. |
| Style link | Auto: By default, the links between the input and output schemas and the Web service parameters are in the form of curves.  Bezier curve: Links between the schema and the Web service parameters are in the form of curve.  Line: Links between the schema and the Web service parameters are in the form of straight lines.  This option slightly optimizes performance. |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored centrally. * Repository: Select the Repository file where Properties are stored. The following fields are pre-filled in using fetched data. |
| Connection type | Drop-down list of the available drivers. |
| DB Version | Select the Oracle version you are using. |
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Mapping | Automatically set mapping parameter. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Dry run | Select this option to populate the QUERY variable of the ELTOutput component connected to the component while not connecting to the database or executing queries.  Information noteNote: This option is available only when you have installed the R2022-01 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Additional JDBC Parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Use Hint Options | Select this check box to activate the hint configuration area to help you optimize a query's execution. In this area, parameters are:  - HINT: specify the hint you need, using the syntax /\*+ \*/. - POSITION: specify where you put the hint in a SQL statement.  - SQL STMT: select the SQL statement you need to use. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tELTOracleMap is used along with a tELTOracleInput and tELTOracleOutput. Note that the Output link to be used with these components must correspond strictly to the syntax of the table name.  Information noteNote: Note that the ELT components do not handle actual data flow but only schema information. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Updating Oracle database entries](teltoracleoutput-teltoraclemap-teltoracleinput-updating-oracle-database-entries-standard-component-this)
* [Managing data using the Oracle MERGE function](teltoraclemap-teltoracleinput-teltoracleoutput-managing-data-using-oracle-merge-function-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-oracle/teltoraclemap-teltoracleinput-teltoracleoutput-managing-data-using-oracle-merge-function-standard-component-the -->
# Managing data using the Oracle MERGE function

Last updated: 9/30/2026

The sample Job described in this scenario allows you to add
new customer information and update existing customer information in a database table using
the Oracle MERGE command.

### In this section

* [Linking the components](/talend/en-US/components/8.0/elt-oracle/teltoraclemap-teltoracleinput-teltoracleoutput-linking-components-standard-component-add)
* [Configuring the components](/talend/en-US/components/8.0/elt-oracle/teltoraclemap-teltoracleinput-teltoracleoutput-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/elt-oracle/teltoraclemap-teltoracleinput-teltoracleoutput-executing-job-standard-component-save)

**Related reference**  

* [tELTOracleOutput](teltoracleoutput "Performs the action (insert, update, delete, or merge) on data in the specified Oracle table through the SQL statement generated by the tELTOracleMap component.")
* [tELTOracleMap](teltoraclemap "Builds the SQL SELECT statement using the table schema(s) provided by one or more tELTOracleInput components.")
* [tELTOracleInput](teltoracleinput "Provides the Oracle table schema that will be used by the tELTOracleMap component to generate the SQL SELECT statement.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-oracle/teltoraclemap-teltoracleinput-teltoracleoutput-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tELTOracleInput component to display its Basic settings view.
2. Select Repository from the Schema list and click the [...] button preceding Edit schema.
3. Select your database connection and the desired schema from the
   Repository Content dialog
   box. 

   The selected schema name appears in the
   Default Table Name field
   automatically.

   * In this use case, the database connection is 
     Talend\_Oracle and the schema is
     `new_customers`.
   * In this use case, the input schema is stored in the Metadata node of the Repository tree view for easy retrieval. For further
     information concerning metadata, see [Managing metadata](/talend/r/dOXsfaOC6ylu%7Ejg52cCKWQ/VHVZkeKaOyORqUVvp3W1gg).
   * You can also select the input component by dropping the
     relevant schema from the Metadata area onto the design workspace and double-clicking
     tELTOracleInput from
     the Components dialog box.
     Doing so allows you to skip the steps of labeling the input component and
     defining its schema manually.
4. Click the tELTOracleMap component to display its Basic settings view.
5. Select Repository from the Property Type list, and select the same database connection that you
   use for the input components. 

   Information noteRemember: All the database details are automatically
   retrieved. Leave the other settings as they are.
6. Double-click the tELTOracleMap component to launch the ELT Map editor
   for setting up the data transformation flow. 

   Add the input table by clicking the
   [+] button on the upper left corner of the ELT Map editor
   and selecting the relevant table name in the pop-up dialog box.

   In this use case, the only input table is
   new\_customers.
7. Select all the columns in the input table and drop
   them to the output table.
8. Click the Generated SQL Select query tab to display the query
   statement to be executed.

   Click OK to validate the ELT Map settings and close the ELT Map
   editor.
9. Double-click the tELTOracleOutput component to display its Basic settings view.
   1. From the Action on
      data list, select MERGE.
   2. Click the Sync
      columns button to retrieve the schema from the preceding
      component.
   3. Select the Use
      Merge Update check box to update the data using Oracle's MERGE
      function.
10. In the table that appears, select the check boxes
    for the columns you want to update. 

    In this use case, youupdate all the data
    according to the customer ID. Therefore, select all the check boxes except the one
    for the ID column.

    Information noteWarning: The columns defined as the
    primary key cannot and must not be made subject to updates.
11. Select the Use Merge Insert check box to insert new data while
    updating the existing data by leveraging the OracleMERGE function.
12. In the table that appears, select the check boxes for the columns
    into which you want to insert new data.

    In this use case, insert all the new customer
    data. Therefore, select all the check boxes by clicking the Check All check box.
13. Fill the Default Table Name field with the name of the target
    table already existing in your database. In this example, fill in `customers_merge`.
14. Leave the other parameters as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-oracle/teltoraclemap-teltoracleinput-teltoracleoutput-executing-job-standard-component-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Save
   the Job.
2. Click
   Run to
   execute
   the Job.

   The data is updated and inserted in the database. The query used
   is displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elt-oracle/teltoraclemap-teltoracleinput-teltoracleoutput-linking-components-standard-component-add -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Add the following components from the Palette to the design workspace:
   tELTOracleInput, tELTOracleMap, and tELTOracleOutput.
2. Label tELTOracleInput as `new_customer`, tELTOracleMap as `ELT Mapper`,
   and tELTOracleOutput as
   `merge_data`.
3. Link tELTOracleInput to tELTOracleMap using a Row > New Output (table) connection.
4. When prompted, enter `NEW_CUSTOMER` as the table name, which should be the actual database
   table name.
5. Link tELTOracleMap to tELTOracleOutput using a Row >  New Output (table) connection.
6. When prompted, enter `customers_merge` as the name of the database table, which holds the
   merge results.
