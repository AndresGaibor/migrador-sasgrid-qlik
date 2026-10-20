<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tas400cdc · versión 8.0 -->
# tAS400CDC

Last updated: 9/30/2026

Addresses data extraction and transportation needs.

tAS400CDC only extracts the changes carried out on the source
operational data and makes them available to the target system(s) using database CDC
views.

By default, this component automatically calls the AS/400-dedicated program RUNCDC to
write the latest update information into a change table (a CDC table) and runs queries
in the same table to read changes.

The RUNCDC program is automatically installed by Talend Studio using a
savf script stored in the following directory:
<Studio\_install>\plugins\org.talend.designer.cdc\_<version>\resource\fitcdc.savf.

For further information about this fitcdc.savf script
and the command used to install the RUNCDC program, see [CDC Redo/Archive log mode](/talend/r/en-US/8.0/studio-user-guide/cdc-redo-archive-log-mode).

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tAS400CDC Standard properties

These properties are used to configure tAS400CDC running in the Standard Job framework.

The Standard
tAS400CDC component belongs to the Databases family.

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
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Property type | Either Built-in or Repository.  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved.  Information noteWarning: Reset the DB type by clicking the relevant button to select the CDC connection. |
| DB Version | Select the AS/400 database version you are using. |
| Host name | Database server IP address. |
| Database | Name of the CDC database.  Information noteNote: The CDC database in which are stored the modified data must be different from the one containing the source data. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Information noteWarning: Reset the DB type by clicking the relevant button to select the schema of the CDC connection. Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Table Name | Short name of the source table where changes made to data should be captured. The target CDC table uses automatically this short name to name itself. |
| Source Library | The AS/400 database's source library.  Information noteNote: The library name must not contain more than 10 characters. The database name is generally used. |
| Subscriber | Enter the name of the application that will use the change table. |
| Events to catch | * Insert: Select this check box to   catch the data inserted in the change table since the last   extraction. * Update: Select this check box to catch   the data updated in the change table since the last extraction. * Delete: Select this check box catch the   data deleted in the change table since the last extraction. |
| Member | Enter the name of the member that holds the desired records. A member is part of a physical file in the library and contains a group of entries. For details, search *format of an AS/400 file* at <http://www.ibm.com>. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Process all input data and empty CDC table | Select this option to process all the input data and empty CDC tables. |
| Keep data in CDC Table | Select this check box to retain changes in the CDC table, allowing one or more target systems to consult the data even after ingestion. When enabled, this option prevents deletion of the consulted CDC data; instead, it updates the value of the field CDC\_STATE to 'x'. This mechanism lets users recheck previously ingested data by filtering records where CDC\_STATE = 'x' (for example, using a tMysqlInput component), and manage deletion themselves if needed. This option is especially useful for users who need to audit or revisit ingested data without having to re-run Jobs or reverse-engineer the process to understand how the checkbox affects CDC\_STATE. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. Information noteNote: Deselect Trim all the String/Char columns to enable Trim columns in this field. |
| Disable command | Select this check box to be able to manually call the *RUNCDC* program by yourself to write changes to the CDC table. |
| Customize command | Select this check box to specify the parameters of the commands to be executed by tAS400CDC. The following gives the syntax of the command executed by tAS400CDC.  ``` library/RUNCDC OPTION(*RUN)                FILE(DATA_LIB/FILE)                JOURNAL(*FILE) LIBOUT(*DEFAULT) MBROPT(*ADD) MODE(*CURRENT) DTCHJRN(*YES) ```  where,   * OPTION, specifies the operation to perform.  You can specify \*RUN (the default),   \*ENDRUN, \*HELP,   \*LOG, \*PARM, and   \*TAB. * FILE, lists the files to be extracted with the library   where the files reside.  The RUNCDC command can extract data from multiple   files given that the files are in the same library. To do so, provide   this parameter in this form: FILE(DATA\_LIB/FILE1 DATA\_LIB/FILE2   DATA\_LIB/FILE3...). You can specify up to 300 files. * JOURNAL, specifies the name and the library of the   journal to be processed.  By default, the journal that is attached to the files is specified. * LIBOUT, specifies the output library for the generated   files. * MBROPT, specifies the output option for the generated   files, which can be \*ADD (the default) and   \*REPLACE. * MODE, specifies the log reading mode, which can be   \*DETACHED (the default), \*CURRENT,   and \*REEL. * DTCHJRN, specifies whether the journal receiver should   be detached at the start of processing.  This parameter can be \*YES (the default) and   \*NO. This parameter is used only when the value of   the MODE parameter is DETACHED.   By default, the component execute the following command.  ``` <CDC_library_name>/RUNCDC FILE(<Source_library_name>/<Source_table_name>)                            LIBOUT(<CDC_library_name>) MODE(*DETACHED) MBROPT(*ADD) DTCHJRN(*YES) ```  For more information about the RUNCDC command, refer to *CDC\_Documentation\_1.09\_EN.pdf*. You can find this document at <Studio\_install>\plugins\org.talend.designer.cdc\_<version>\resource\. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component. It requires an output component and row Main link. Note that the journal and the receiver required by CDC are typically controlled by the administrator of the AS/400 system. For this reason, since version 5.4.2 (included) of Talend Studio, tAS400CDC runs the *RUNCDC* program only and does not automatically create, activate, deactivate, modify, or delete any journal or receiver of that AS/400 system any more. You need to contact the AS/400 administrator before performing any of these operations. Depending on the policy in your company, the administrator will either perform the operation or provide you with the authorization to do it yourself.  Because of this behavior updates, since 5.4.2, the tAS400CDC component does not execute the following command as it did in the 5.4.1 or earlier versions:  ``` CHGJRN JRN(<Source_library_name>/<Source_table_name>) JRNRCV(*GEN) ```  This command is used to ensure that an older receiver is detached from a journal and a newer one is attached to the journal to retrieve the last change. You are then recommended to execute this command in your AS/400 system before running this component. Alternatively, enter the example command given above for the Customize command check box is selected, in order to automate the detachment and attachment process.  For further information about how the CDC for AS/400 is handled by Talend Studio, see [CDC architecture](/talend/r/en-US/8.0/studio-user-guide/cdc-architectural-overview) and [CDC Redo/Archive log mode](/talend/r/en-US/8.0/studio-user-guide/cdc-redo-archive-log-mode). |
