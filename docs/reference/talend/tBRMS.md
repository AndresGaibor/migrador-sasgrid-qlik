<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms · versión 8.0 -->
# tBRMS

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

Applies Drools business rules to an incoming flow and writes the output data to an
XML file.

tBRMS retrieves business rules from a Drools repository and applies them
to a Job.

Drools is a Business Rules Management System, BRMS solution, that enables business experts
to create business rules and customize them on the run.

For more information about Drools, see <http://drools.org/>.

You can install and use Red Hat BRMS or JBoss BRMS to manage business rules. For more
information, see [Red Hat JBoss BRMS documentation](https://access.redhat.com/documentation/en/red-hat-jboss-brms/) and [JBoss documentation](https://docs.jboss.org/drools/release/6.2.0.Final/drools-docs/html/pt05.html).

## tBRMS Standard properties

These properties are used to configure tBRMS running in the
Standard Job framework.

The Standard
tBRMS component belongs to the Processing
family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository file   where properties are stored. The fields that follow are completed automatically   using the fetched data. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields   that will be processed and passed on to the next component. The schema is   either Built-in or stored remotely in   the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: You create and store the   schema locally for only the current component. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists   and is stored in the Repository, hence can be reused in various projects and   Job flowcharts. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| XML Field | Select the XML field for the data to be written to the output file. |
| Choose rule module | Select from the list:  - Use latest deployment from Drools workbench: Always choose this option when you run the Job for the first time. The Job uses the latest deployment of the rule on the Drools repository. If the rule has been changed meanwhile, the Job results will be different.  - Use local rules: with this option, you execute the Job with the local rule you imported previously from the repository to the root folder of Talend Studio, in /studio\_path/Drools/<project\_name>, that is the latest package you browse from the Drools workbench. This means, even if you have modified the rule and deployed it on the repository, the Job results will not be different.  Do not use this option when you run your Job for the first time.  Information noteNote: If the shared mode is enabled, the path to the Drools folder has changed to C:/Users/user-account/studio-path/Drools/<project\_name>. For more information, see [Shared mode for Talend Studio](/talend/r/en-US/8.0/installation-guide-windows/enabling-the-shared-mode-for-talend-studio) in the Talend Installation Guide.  The fields that follow will vary according to your choice. |
| Drools Workbench Connection | Select the Drools distribution from the Choose distribution list:  * Redhat BRMS 6.2 * JBoss BRMS 6.2 * Redhat Decision Manager 7.3 |
| Drools Workbench URL | Enter the address of the business rule repository. |
| Username and Password | Enter the authentication information used to connect to the Drools Workbench of interest.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Module list | Click the [...] button next to the field to open a list of the Jars on the Drools Workbench.  You can select Jar files from all branches, main and other branches. In Deploy Package, click the [...] button and select the Master artifacts or Custom artifact tab. To select a Jar file that is not from the latest version or the main branch, select the Custom artifact tab and enter the artifact ID, the group ID and the version. You can find these parameters in the Drools workbench.  Snapshot versions are not supported. |
| Maven Deployment Path | After you select the Jar file from the Drools Workbench, this field is automatically populated. |
| Class Name | After you select the Jar file, this field is automatically populated with the name of the class in which the business rule is stored in a Jar file. |
| Drools flow ID (optional) | A Drools flow describes the order in which a series of business rules are executed. Its flow ID is defined manually when you are creating the Drools flow.  When you need to call a specific Drools flow via tBRMS to use the execution order it defines, enter the corresponding flow ID in this field.  For more information about Drools flow, see the relevant Drools manuals. |

## Advanced Settings

| Properties | Description |
| --- | --- |
| Configure XML Tree | Click [...] to map the source schema to the XML output schema. |
| Group by | Use the tool bar to modify the column order. |
| Advanced separator | Select this check box to modify the separators used for numbers. |
| Encoding | Select the encoding type from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles data flows. Therefore it requires input and output components. |
| **Limitation** | When using the tBRMS component in subJobs with the same value in the Class name field, select the Use an independent process to run subJob check box in the tRunJob component settings to be able to run the Job correctly.  For further information about the tRunJob component, see [tRunJob](/talend/en-US/components/8.0/orchestration/trunjob). |

**Related concepts**  

* [Applying business rules to an Excel file to filter data](tbrms-tmap-textractxmlfield-tlogrow-applying-business-rules-to-excel-file-to-filter-data-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-applying-business-rules-to-excel-file-to-filter-data-standard-component-enterprise-this -->
# Applying business rules to an Excel file to filter data

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

This scenario applies only to subscription-based Talend
products.

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

This scenario describes a Job in which tBRMS applies Drools business rules to an Excel
file, in order that relevant data can be retrieved in the output. In this case, rules are
applied to input data about candidates applying for a loan. The output will show whether
the candidates are qualified or not.

Before you begin, the business rules to use in the Job have
been already created and deployed on the Drools repository.

You can also clone repositories in Drools to have access to
business rules stored in them.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-dropping-and-linking-components-standard-component-enterprise-drop)
* [Configuring the input component](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-input-component-standard-component-enterprise)
* [Configuring the tMap component](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-tmap-component-standard-component-enterprise)
* [Configuring the tBRMS component](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-tbrms-component-standard-component-enterprise)
* [Configuring the output flow](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-output-flow-standard-component-enterprise-to)
* [Saving and executing the Job](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-saving-and-executing-job-standard-component-enterprise-press)

**Related reference**  

* [tBRMS](tbrms "Applies Drools business rules to an incoming flow and writes the output data to an XML file.")

**Related information**  

* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tExtractXMLField](/talend/en-US/components/8.0/processing/textractxmlfield)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-input-component-standard-component-enterprise -->
# Configuring the input component

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

## About this task

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

## Procedure

1. Double-click tFileInputExcel to open its Basic
   settings view and define the component properties:
2. In the Property
   type list, select Built-in and fill in the fields that follow.
3. Click the [...] button next to the File Name/Stream field and browse to the source file
   to set its path and name.

   The source file used in this example is called *brmsInput*
   and it holds candidate data.

   Information noteRestriction: The tBRMS component supports the
   `XLSX` format from version 8.0 R2022-09. If you are
   using a previous version, do not select Read excel2007 file
   format(xlsx).
4. If needed, right-click tFileInputExcel and select Data
   viewer to have a preview of the input data.
5. Select the All
   sheets check box to retrieve the data from all sheets of the
   excel file.
6. From the Schema list, select Built-in and click Edit
   schema to define the structure of the source data. In this
   example, five columns are defined for the input information of candidates.
7. Click OK to validate your changes and
   close the dialog box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-output-flow-standard-component-enterprise-to -->
# Configuring the output flow

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

## About this task

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

To extract the data of interest, you need to configure the output flow. The
operations to be performed are as follows:

## Procedure

1. Double-click tExtractXMLField to open its
   Basic settings view.
2. Click Edit schema to open the schema
   editor.
3. In the Output schema to the right of the editor, add and define the
   columns which correspond to those columns in the tBRMS input schema. The sequence and names of columns may
   vary according to your need.
4. Click OK to close the editor.
5. In the Loop XPath query field, enter the
   name of the XML Tree root tag, as it
   appears in the Configure XML Tree editor of
   the tBRMS component, preceded by the
   forward slash symbol and between double quotation marks, for example:
   *"/loanSimulator"*.
6. In the XPath query fields, next to the
   corresponding columns, enter the fields exactly as they appear in the
   XML Tree fields of the tBRMS component, in the Link Target area of the Configure XML
   tree editor, between double quotation marks.
7. Double-click tLogRow to open its
   Basic settings view:
8. In the Mode area, select the Table (print values in cells of a table)
   option.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-tbrms-component-standard-component-enterprise -->
# Configuring the tBRMS component

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

### In this section

* [Configuring the basic settings of the tBRMS component](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-basic-settings-of-tbrms-component-standard-component-enterprise-click)
* [Configuring the XML mapping](/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-xml-mapping-standard-component-enterprise-click)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-tmap-component-standard-component-enterprise -->
# Configuring the tMap component

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

## About this task

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

## Procedure

1. Double-click tMap to
   open its Map Editor.
2. In the lower right part of the map editor, click the plus button to add
   eight columns: *age*, *annualRevenue*, *loanDeposit*, *loanAmount*,
   *numberOfYears*, *loanInterest*, *monthlyPayment*, *rejected*. 

   These columns will appear in the synonyms table on the right side of the
   map editor. In this example, the table is *row1*.
3. In the upper left part of the map editor (input flow), select the
   age and annualRevenue columns and drop them respectively to the
   age and annualRevenue columns in the upper right part of the map
   editor (output flow).

   Alternatively, click Auto map! to map the
   columns with the same name automatically.
4. In the *row1* table, click the Expression column in the *loanDeposit* row to locate the cursor, and then click the [...] button to open the
   Expression Builder dialog box.

   Enter the following expression to calculate the loan deposit:

   ```
   Math.round(((loanAsk.downPayment  / loanAsk.totalAmount)*100))
   ```

   Click OK to close the Expression Builder dialog box.

   Now the *downPayment* and *totalAmount* fields from the incoming data flow
   are concatenated to the output column: *loanDeposit*.
5. Click the Expression column in the
   *loanAmount* row to locate the
   cursor.

   Enter the following expression to calculate the amount of
   loan:

   ```
   loanAsk.totalAmount - loanAsk.downPayment
   ```
6. Click the Expression column in the
   *numberOfYears* row to locate the
   cursor.

   Enter *loanAsk.duration* to concatenate
   the *duration* row of the input flow to the
   *numberOfYears* row in the output
   column.
7. Enter *0.0* in the Expression column of the *loanInterest* and *monthlyPayment* rows respectively.
8. Enter *false* in the Expression column of the *rejected* row.
9. Click OK to close the map editor.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-dropping-and-linking-components-standard-component-enterprise-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

## About this task

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFileInputExcel, tMap,
   tBRMS, tExtractXMLField, tLogRow.
2. Link tFileInputExcel to
   tMap using a Row > Main connection. Rename the link as *loanAsk* to better identify its function.
3. Link tMap to tBRMS using a Row > \*New Output\*
   (Main) connection.
4. Link tBRMS to tExtractXMLField using a Row > Main connection
   and then use another Row > Main
   connection to connect tExtractXMLField to
   tLogRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-saving-and-executing-job-standard-component-enterprise-press -->
# Saving and executing the Job

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

## About this task

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run console to
   launch the Job.

   The business rule has been applied to the input data and the table of
   results indicates which candidates have been rejected. The Reason column indicates the reason for which the
   candidate has been rejected.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-basic-settings-of-tbrms-component-standard-component-enterprise-click -->
# Configuring the basic settings of the tBRMS component

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

## About this task

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

## Procedure

1. Click tBRMS to open its
   Basic settings view.
2. Click [...] next to
   Edit schema to open the schema
   editor.

   The input schema to the left is automatically retrieved from
   tMap.
3. In the output area, click [+] to add a new column which will serve to write the output data to
   an XML file.
   1. Enter a name for the column.
   2. Define the Type as
      String.

   Click OK to validate your
   changes and close the dialog box.
4. From the XML Field list,
   select the name of the XML column you entered in the output schema.
5. From the Choose rule module
   list, select Use latest deployment from Drools
   workbench to download the Jar file from the Drools repository.
6. From the Choose distribution list, select Redhat
   Decision Manager 7.3.
7. In the Drools Workbench Url,
   enter the address of the Drools Workbench .
8. Type in the user name and the password used to connect to the
   Drools Workbench.
9. Next to Module List, click
   [...] to open the Deploy Package dialog box. 

   In this dialog box, the URL, Username and Password fields are already filled with the
   corresponding information you entered in the earlier steps.
10. Click [...] to browse the
    Jar files in the Select Package dialog box and
    select the jar package `org.talend.bank` for this example.
11. From the list next to the selected jar package, select the class
    `org.talend.bank.LoanSimulator` and then click OK to close the dialog box. 

    A Talend program transforms the business rule library into a form which
    can be used in the Job and creates an XSD file at the root of Talend Studio, at
    /studio\_path/Drools/<project\_name>. The XSD file
    records the mapping between the incoming data flow and the objects to be handled by
    the Drools engine.

    Information noteNote: If the shared mode is enabled, the path to the Drools
    folder has changed to
    C:/Users/user-account/studio-path/Drools/<project\_name>.
    For more information, see [Shared mode for Talend Studio](/talend/r/en-US/8.0/installation-guide-windows/enabling-the-shared-mode-for-talend-studio) in the
    Talend Installation Guide.
12. In the Drools Flow ID
    (optional) field, enter, between quotation marks, the ID of Drools
    flow to be used when executing the rules of interest. 

    In this example, it is `loanflow`. For more
    information about Drools flow, see the relevant Drools manuals.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/business-rules/tbrms-tmap-textractxmlfield-tlogrow-configuring-xml-mapping-standard-component-enterprise-click -->
# Configuring the XML mapping

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

## About this task

Information noteImportant: The tBRMS component is deprecated since
Talend Studio 8.0
R2026-05. You can use the [tDQRules](https://help.qlik.com/talend/en-US/components/8.0/validation/tdqrules) component instead.

## Procedure

1. Click the Advanced Settings tab to set
   the additional parameters.
2. In the XML Mapping area, click [...] to configure the XML tree.

   Right-click the first row in the Link
   target table and select Import XML
   Tree.
3. Browse to and select the XSD file from the root of Talend Studio.
   The XML Tree schema is completed
   automatically.
4. Drop all of the relevant columns from the Schema
   List onto the corresponding related column fields in the
   Link target schema.

   From the dialog box which appears, select the Add
   linker to target node option.

   Alternatively, you can click Auto map! to
   concatenate automatically the columns between the Linker source and Link
   target.
5. Right-click the reason field and select
   Set As Loop Element from the
   list.
6. Click OK to close the dialog box.
