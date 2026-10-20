<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/singlestore/tsinglestoreoutputbulkexec · versión 8.0 -->
# tSingleStoreOutputBulkExec

Last updated: 9/30/2026

Provides performance gain when loading data from a file into a table
of a database connected through JDBC API.

Normally, the tSingleStoreOutputBulk and
tSingleStoreBulkExec components work together in a
two-step process:

1. The tSingleStoreOutputBulk component uploads incoming data to a
   storage.
2. The tSingleStoreBulkExec component loads the data from a storage into
   a database table.

You can transform the data before it is loaded into the database table in this
two-step process. These two steps are fused together in the tSingleStoreOutputBulkExec component.

## tSingleStoreOutputBulkExec Standard properties

These properties are used to configure tSingleStoreOutputBulkExec running in the Standard Job framework.

The Standard
tSingleStoreOutputBulkExec component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for   all related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component. You need to   click the [...] button   next to it and in the pop-up Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is available when Use this Component is selected from the Connection Component dropdown list. |
| Component list | Select the component that opens the database connection to be reused by this component. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`. |
| Drivers | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Driver Class | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| User Id and Password | The database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Table | Enter the name of the table into which data will be written. |
| Bulk file | Name of the bulk file to be loaded. |
| Append | Select this option if you want to append the incoming data to an existing bulk file.  This option prevents the data in an exisitng file from being overwritten. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Row Separator | The separator used to identify the end of a row. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Set text enclosure | Select this option to set the text enclosure. You can enter the enclosure character (only one character) between double quotation marks in the text field to the right. For example, to use double quotation mark (") as the enclosure character, enter `"""` in this field.  It is recommended to use standard escape character, that is `"\"`. Otherwise, you should set the same character for Escape char and Text enclosure. If the escape character is set to `"\"`, the text enclosure can be set to any other character; if the escape character is set to a character other rather than `"\"`, it will be changed to the same character as the text enclosure. For example, with the escape character set to `"#"` and the text enclosure set to `"@"`, the escape character will be changed to `"@"`. |
| Set null value | Select this option to set the null value. You can set the null value in the field to the right. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded into the database. |
