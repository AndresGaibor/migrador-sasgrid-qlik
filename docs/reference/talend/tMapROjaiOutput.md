<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprojaioutput · versión 8.0 -->
# tMapROjaiOutput

Last updated: 9/30/2026

Inserts, replaces or deletes documents in a MapR-DB database to be used as document
database, based on the incoming flow from the preceding component in the Job.

You must have properly installed and configured your MapR Client before using this component. A \opt\mapr\conf\mapr-clusters.conf file is automatically generated out of the Client configuration process to store the connection information to your MapR cluster and your MapR-DB database. At runtime, this OJAI component reads this connection information by itself to connect to the MapR-DB database to be used.

For further information about how to install and configure your MapR client, see [Setting up the Client](http://doc.mapr.com/display/MapR/Setting+Up+the+Client) from the MapR documentation.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMapROjaiOutput Standard properties

These properties are used to configure tMapROjaiOutput running in the Standard Job framework.

The Standard
tMapROjaiOutput component belongs to the Databases NoSQL family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component supports the Document type. If a field is for entire documents, select Document in the Type column for this field in the schema editor.  Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Use kerberos authentication | If you are accessing a MapR-DB as-OJAI database running with Kerberos security, select this checkbox, then, enter the Kerberos principal name and password in the displayed fields.  Every time when you launch your Job, the component submits this authentication information to Kerberos for a new kinit ticket. |
| Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| Table | Enter the name of the table to be processed. |
| Action on table | Select an operation to be performed on the table defined.   * None: No operation is carried out. * Drop and create table: The table is removed   and created again. * Create table: The table does not exist and   gets created. * Create table if does not exist: The table is   created if it does not exist. * Drop table if exist and create: The table is   removed if it already exists and created again. * Truncate: The table content   is deleted. |
| Action on data | Select an action to be performed on data of the table defined.   * Insert: Add   new entries to the table. If duplicates are found, the Job stops. * Replace:   if the table already contains data, delete all the existing data and insert the new   data. If the table is empty, insert the new data. * Insert or   Replace: it looks at the document IDs, replaces the documents whose IDs   exist in both the database and the data to be written, and inserts the documents whose   IDs do not exist in the database. * Delete:   Remove entries corresponding to the input flow. |
| Bulk write | Select this check box to insert, update or remove data in bulk.  In the Bulk write size field, enter the size of each query group to be processed by MapR-DB. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tMapROjaiOutput executes the action defined on the documents in a given MapR-DB database based on the flow incoming from the preceding component in your Job. |

**Related concepts**  

* [Writing candidate data in a MapR-DB OJAI database](tmaprojaioutput-tfixedflowinput-writing-candidate-data-in-mapr-db-ojai-database-standard-component-bigdata "This scenario uses tMapROjaiOutput to write data about some candidates in a MapR-DB OJAI database.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprojaioutput-tfixedflowinput-writing-candidate-data-in-mapr-db-ojai-database-standard-component-bigdata -->
# Writing candidate data in a MapR-DB OJAI database

Last updated: 9/30/2026

This scenario uses tMapROjaiOutput to write data about some candidates in a MapR-DB OJAI database.

This scenario applies only to Talend products
with Big Data.

* tFixedFlowInput: it provides the sample data to be written in the database.
* tMapROjaiOutput: it writes the sample data to the database.

### In this section

* [Reading the sample candidate data](/talend/en-US/components/8.0/maprdb/tmaprojaioutput-tfixedflowinput-reading-sample-candidate-data-standard-component-bigdata-ensure)
* [Writing the sample data to the MapR OJAI database](/talend/en-US/components/8.0/maprdb/tmaprojaioutput-tfixedflowinput-writing-sample-data-to-mapr-ojai-database-standard-component-bigdata)

**Related reference**  

* [tMapROjaiOutput](tmaprojaioutput "Inserts, replaces or deletes documents in a MapR-DB database to be used as document database, based on the incoming flow from the preceding component in the Job.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprojaioutput-tfixedflowinput-reading-sample-candidate-data-standard-component-bigdata-ensure -->
# Reading the sample candidate data

Last updated: 9/30/2026

## Procedure

1. Ensure that the MapR client has been properly installed and configured in the machine in which the current Job runs.
2. Drop tFixedFlowInput and tMapROjaiOutput onto the workspace.
3. Connect tFixedFlowInput to tMapROjaiOutput using a Row > Main link and accept the propagation of the schema from tMapROjaiOutput.
4. Double-click tFixedFlowInput to open its Component view.
5. Click the [...] button to open the schema editor.

   * The `_id` column exists already because this
     column was retrieved from tMapROjaiOutput in
     the previous steps to provide the technical IDs of the documents to
     be stored in a MapR Ojai database. This column is required by
     tMapROjaiOutput.
   * Click the [+] button to add the other columns
     and rename them to `firstname`,
     `lastname`, `sex`,
     `married`, `age` and
     `salary`, respectively. The type of the
     `married` column should be
     Boolean, the type of the
     `age` column Integer and
     the `salary` column
     Float.
6. Click OK to close the schema editor and accept the
   propagation of the schema.
7. In the Mode area, select the Use Inline
   table radio button to display the table in which you add the sample
   data.
8. Click the `[+]` button to add four rows and enter the
   sample data as is displayed in the image above.

   This sample data is used for demonstration purposes only.

   The data of the String type should be put in double
   quotation marks and the data of the three other types should be put without any
   quotation marks.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprojaioutput-tfixedflowinput-writing-sample-data-to-mapr-ojai-database-standard-component-bigdata -->
# Writing the sample data to the MapR OJAI database

Last updated: 9/30/2026

## Procedure

1. Double-click tMapROjaiOutput to open
   its Component view.
2. In the Table field, enter the name of the table to be used in your MapR OJAI database.
3. From the DB Version list, select the
   MapR OJAI database version you are using.

   At runtime, tMapROjaiOutput automatically reads the connection information to the database from the \opt\mapr\conf\mapr-clusters.conf file of your MapR client.

   In this example, the content of this file reads as follows:

   ```
   mapr521   mapr521:7222
   ```
4. From the Action on table drop-down list, select Drop table if exists and create and then from the Action on data drop-down list, select Insert.
5. In the Mapping table, the columns from the schema has
   automatically appears in the Column column. In the
   Parent field path column, enter
   `Name` within double quotation marks in the
   `firstname` row and the `lastname` row
   and enter `Status` within double quotation marks in the
   `sex` row, the `married` row and the
   `age` row.

   This configuration groups the candidates' first names and last names in the `Name` field and their sexes, marriage status and ages in the `Status` field in the outputted data flow.
6. Press F6 to run the Job.
