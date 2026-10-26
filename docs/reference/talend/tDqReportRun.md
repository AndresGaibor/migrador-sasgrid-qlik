<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun · versión 8.0 -->
# tDqReportRun

Last updated: 9/30/2026

Launches the analyses listed in a report and save the results in the data quality
data mart.

You can schedule the Job that uses this component in *Talend Administration Center* and simply launch it to generate the report file without having to deploy Talend Studio on the
same host server as the Job server. Using this component, you can also generate all types
of reports (PDF, XML, or HTML) in folders of your choice and save the analysis results in
the report database.

tDqReportRun launches the profiling analyses defined in a report created
in the 
Profiling
 perspective and generates a report file without having to open Talend Studio.

This component executes report as does the Generate report file menu item in the 
Profiling
 perspective.

For more information about how to generate a report file from report items
in the DQ Repository tree view, see [Reports](/talend/en-US/studio-user-guide/8.0-R2024-08/reports).

Information noteNote: When using a referenced project,
the main and referenced projects must be in the same Git repository. Otherwise, the Job
cannot run.

Information noteNote: From Talend Studio 8.0
R2025-05 and if the analysis is on Snowflake using the key-pair authentication, add the
tSetKeystore component before tDqReportRun and
select Set KeyStore. For more information, see [tSetKeystore documentation](https://help.qlik.com/talend/en-US/components/8.0/keystore/tsetkeystore).

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDqReportRun Standard properties

These properties are used to configure tDqReportRun running in the Standard Job framework.

The Standard
tDqReportRun component belongs to the Data Quality family.

Information noteRestriction: From Talend Studio 8.0
R2023-04 to 8.0 R2025-02, tDqReportRun can run on Java 8, except
with the HSQL data mart. From Talend Studio 8.0
R2025-02, tDqReportRun can run on Java 17 only.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  The schema of this component is read-only. It gives some information about the report such as report identification, report name, execution time and so on. * Built-in: You create and store the schema locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already created and stored the schema in the Repository. You can reuse it in other projects and Job designs. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Refresh Dependency | Click this button to update the jars needed by the report data mart before executing the report Job.  This operation is mandatory when:  * You modify the indicators used on the analysis in the analysis editor in   the Profiling perspective. * You change the database type of the report data mart in the report   editor in the Profiling perspective.  For further information about configuring databases to store report results, see [Managing the report database](/talend/r/en-US/8.0/studio-user-guide/managing-report-database). |
| Browse Reports | Click this button to open a dialog box where you can select one or more reports to be generated.  The reports you select overwrite the current Job contexts.  If the reports you select store analysis results in different data marts, generating the report will store these results in the different databases accordingly. However, one report file will be generated in the path defined in the component basic settings.  All reports created in the  Profiling  perspective are listed in this dialog box. |
| Report filenames | This field holds the technical path of the reports to be generated. You can fill it:  * Automatically by selecting the reports from the report   list through the Browse reports   button, * Manually, by typing in or pasting the report technical path. You can   copy the technical path of the report from the Detail view panel below DQ   Repository in the Profiling perspective of Talend Studio. The technical path is displayed in the panel when you select the   report in the repository.  You can set several report paths separated by commas.  To set one report path by combining contexts and strings, use plus signs. To set several report paths, use commas:  * Path examples for one file:   + context.filename1+"/localpath/report.rep"   + context.filename1+context.filename2   + context.filename1+context.filename2+"/report.rep" * Path examples for two or more files:   + context.filename1,"/report.rep"   + context.filename1,context.filename2,context.filename3   + "/localpath/report1.rep","/localpath/report2.rep" You can use both the comma `,` and the plus sign   `+`. In this case, two files will be generated.   The comma and plus sign must be outside of the quotation marks.   Example: ```   context.filename1+"/report.rep","/localpath/report2.rep"   ``` |
| Output folder | Set the path to the folder where to store the generated report file.  The path is set by default to the home directory of Talend Studio. This path overwrites the path information set in each report item. Information noteNote: If the shared mode is enabled, the path has changed to C:/Users/user-account/studio-path/.... For more information, see [Shared mode for Talend Studio](/talend/r/en-US/8.0/installation-guide-windows/enabling-the-shared-mode-for-talend-studio) in the Talend Installation Guide. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Driver JAR | Jars are listed by default in this table if you generate the Job via the Generate report file menu item in the  Profiling  perspective.  You can still add Jar files by adding lines to the table. Then on each line, click the [...] button to open a wizard from which you can select a driver Jar relevant to the connection used by the analyses listed in the report. In the wizard, you can select Jars from either internal or external modules. |
| Parallel execution | Select this check box when you use tParallelize to run tDqReportRun components in parallel. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This is a start component of a Job. It needs an output component to which it sends information about report execution.  Information noteNote: You are recommended to generate a launch-report Job using this component from the DQ Repository tree view in the Profiling perspective of Talend Studio. For further information about how to generate this ready-to-use Job, see [Generating a Job to launch a report](/talend/r/en-US/8.0/studio-user-guide/generating-job-to-launch-report). |

**Related concepts**  

* [Launching a profiling report from Talend Management Console](tdqreportrun-tlogrow-launching-profiling-report-from-talend-cloud-management-console-standard-component-enterprise-this)
* [Launching a profiling report from Talend Administration Center Web application](tdqreportrun-tlogrow-launching-profiling-report-from-talend-administration-center-web-application-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-launching-profiling-report-from-talend-administration-center-web-application-standard-component-enterprise-this -->
# Launching a profiling report from Talend Administration Center Web application

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes how you can remotely execute a data quality launch-report Job
from a given *Talend Administration Center* Web application.

To do this, you must first commit all of the required metadata to the remote SVN or Git
repository used by the *Talend Administration Center* Web application.

### In this section

* [Prerequisites](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-prerequisites-standard-component-enterprise-proceed)
* [Creating the analysis and generating the report](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-analysis-and-generating-report-standard-component-enterprise-in)
* [Launching the report remotely](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-launching-report-remotely-standard-component-enterprise-from)

**Related reference**  

* [tDqReportRun](tdqreportrun "Launches the analyses listed in a report and save the results in the data quality data mart.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-launching-profiling-report-from-talend-cloud-management-console-standard-component-enterprise-this -->
# Launching a profiling report from Talend Management Console

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This scenario describes how you can remotely execute a data
quality launch-report Job from *Talend Management Console*.

In this scenario, Microsoft Azure is used to store the database to which you want to
connect.

### In this section

* [Creating and configuring the database in Microsoft Azure](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-and-configuring-database-in-microsoft-azure-standard-component-enterprise-click)
* [Creating the connection and publishing the Job to Talend Cloud](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-connection-and-publishing-job-to-talend-cloud-standard-component-enterprise-you)
* [Launching the report remotely](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-launching-report-remotely-standard-component-enterprise-you)

**Related reference**  

* [tDqReportRun](tdqreportrun "Launches the analyses listed in a report and save the results in the data quality data mart.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-analysis-and-generating-report-standard-component-enterprise-in -->
# Creating the analysis and generating the report

Last updated: 9/30/2026

## Procedure

1. In the Profiling perspective of Talend Studio,
   create an analysis.
2. Right-click the analysis and select New
   Report to open the report editor and generate a report file
   on this analysis.
3. In the Output\_Folder field, set the path
   to a local directory where to save the report file. Also, in the File Type field, select the format of the report
   output file.
4. In the Database Connection Settings tab,
   set the parameters to the report database where to save the analysis results
   and click Check to validate your
   connection. 

   If the database structure to which you want to connect does not already
   exist in the database, it will be created and you will be asked to confirm
   its creation.

   For further information about how to generate a report file and
   how to set a report database, see [Managing the report database](/talend/r/en-US/8.0/studio-user-guide/managing-report-database).

   The required metadata such as the analysis and report parameters and the database
   connection have been committed to the remote SVN or Git repository used by
   the *Talend Administration Center* Web application.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-launching-report-remotely-standard-component-enterprise-from -->
# Launching the report remotely

Last updated: 9/30/2026

## Procedure

1. From the 
   Profiling
    perspective, right-click the *ColumnAnalysis\_WithThresholds* report under the Report node and select Generate Jobs > Launch a report from the contextual menu.

   This generates a launch-report Job and opens it in the 
   Integration
    perspective.

   The Report filenames field
   points to the technical path of the report. You can modify the path.

   To set one report path by combining contexts and
   strings, use plus signs. To set several report paths, use commas:
   * Path examples for one file:
     + context.filename1+"/localpath/report.rep"
     + context.filename1+context.filename2
     + context.filename1+context.filename2+"/report.rep"
   * Path examples for two or more files:
     + context.filename1,"/report.rep"
     + context.filename1,context.filename2,context.filename3
     + "/localpath/report1.rep","/localpath/report2.rep"

     You can use both the comma `,` and the plus sign
     `+`. In this case, two files will be generated.
     The comma and plus sign must be outside of the quotation marks.
     Example:

     ```
     context.filename1+"/report.rep","/localpath/report2.rep"
     ```

   The Output Folder field points to the folder where to save the report file.
2. From Talend Studio 8.0
   R2025-05 and if the analysis is on Snowflake using the key-pair authentication, add the
   tSetKeystore component before tDqReportRun and
   select Set KeyStore. For more information, see [tSetKeystore documentation](https://help.qlik.com/talend/en-US/components/8.0/keystore/tsetkeystore).
3. Press F6 to execute the Job
   from Talend Studio for
   testing purposes. 

   If any modifications are done in the analysis after you generate
   the Job from the analysis report, you must click the Refresh Dependency tab in the basic settings of tDqReportRun before you execute the Job.
4. Connect to the *Talend Administration Center* Web application.
5. In the menu tree view of the Web application, expand Conductor and click Job Conductor to display the execution task list.

   The Job Conductor page gathers the script generation, Job deployment and Job execution phases.
6. From the toolbar on the Job Conductor page, click Add>Normal Task to clear the Execution task configuration panel. 

   On this configuration panel, set the parameters required for executing the launch-report Job as the following:

   * In the Label field, type in the task name.
   * In the Project field, select the project in which the launch-report Job was created.
   * In the Branch field, select  *trunk* as the branch of this project.
   * From the Name list, select the launch-report Job to be used.
   * In the Version list, select the Job version you want to launch; and in the Context field, select the context in which to run the Job.
   * From the Execution server list, select the server which you want to use to execute this task you are configuring.
7. Click Save to validate the configuration of this execution task. 

   The new task is displayed in the Job Conductor page under the corresponding project.
8. From the task list, select the newly added task.
9. On the toolbar of the Job Conductor page, click Generate.
10. Once the status of this task reads *Ready to send* on the task list, select the task again and click Deploy on the toolbar.
11. Once the status of this task reads *Ready to run* on the task list, select the task again and click Run on the toolbar.

    When you run the launch-report Job from *Talend Administration Center* Web Application, the analysis listed in the report is executed. The analysis results are saved in the report database and the report file is saved in the output folder defined in the tDqReportRun basic settings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-prerequisites-standard-component-enterprise-proceed -->
# Prerequisites

Last updated: 9/30/2026

## About this task

Proceed as follows to set up the scenario prerequisites:

## Procedure

1. Create a data quality project from the Talend Administration Center Web application.

   You will launch the report from this project, *dq\_proj* in this scenario.

   For further information about how to create a project in the *Talend Administration Center* Web application, see [Adding a project](/talend/r/en-US/8.0/administration-center-user-guide/adding-project).

   If you have not the required rights to create or manage a project,
   see the administrator of your Web application.
2. Establish a connection from Talend Studio to
   the remote Git repository storing the above-mentioned project. 

   For further information about how to create the connection of this
   kind, see [Enabling the standard Git storage
   mode](/talend/r/en-US/8.0/studio-user-guide/enabling-the-standard-git-storage-mode).
3. Launch Talend Studio
   using this new connection and the new project created.

   For further information about how to launch Talend Studio in
   this way, see [Accessing remote projects from Talend
   Studio](/talend/r/en-US/8.0/studio-user-guide/tmc-access-projects).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-and-configuring-database-in-microsoft-azure-standard-component-enterprise-click -->
# Creating and configuring the database in Microsoft Azure

Last updated: 9/30/2026

## Procedure

1. Click Home > Azure Database for MySQL > Add.
2. Fill in the mandatory fields.

   For more information about how to create and configure a database in Microsoft
   Azure, see the [video procedure](https://azure.microsoft.com/en-en/resources/videos/create-sql-database-on-azure/) on their website.
3. Click Review + create.

   The database is available in Azure Database for MySQL
   servers.
4. Click your database and click 
   Connection security.
5. Your IP must be in the Firewall
   rules table. If it is not, enter it and click Save.

   You must declare your IP in the Firewall
   rules table to authorize the connection to your database. Otherwise,
   the report cannot be launched from Talend Management Console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-connection-and-publishing-job-to-talend-cloud-standard-component-enterprise-you -->
# Creating the connection and publishing the Job to Talend Cloud

Last updated: 9/30/2026

## Before you begin

You have:

* created and configured a [Creating and configuring the database in Microsoft
  Azure](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-and-configuring-database-in-microsoft-azure-standard-component-enterprise-click).
* created an analysis to analyze this database. For more information, see [Creating a database content analysis](/talend/r/en-US/8.0/studio-user-guide/creating-database-content-analysis).
* created a report on this analysis. For more information, see [Creating a report on specific analyses](/talend/r/en-US/8.0/studio-user-guide/creating-report-on-specific-analyses).

## Procedure

1. Create the database connection.
   1. Enter the same Login, Password
      and Server as defined in your
      MySQL database.

      For more information, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata).
2. To test the connection with Talend Management Console,
   click Windows > Preferences > 
   Talend
    > 
   Talend Cloud
    > Test Connection.

   Service available is displayed. If the service is not
   available, verify the parameters.
3. Before publishing the Job to Talend Cloud, you must generate it from the report. In the
   DQ Repository tree view, right-click the report  > Generate jobs > Launch a report.

   A Job using the tDqReportRun component is created.
4. To publish the Job to Talend Cloud, in the
   Repository tree view, right-click the Job > Publish to Cloud.

   The Publish to Cloud wizard is
   displayed.
5. Verify the parameters and click Finish.

   For more information about this dialog, see [Publishing artifacts from Talend Studio](/talend/r/en-US/Cloud/management-console-user-guide/publish-jobs).

   The publishing may take few minutes.

## Results

The Job is published in Talend Management Console as a
task.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-launching-report-remotely-standard-component-enterprise-you -->
# Launching the report remotely

Last updated: 9/30/2026

## Before you begin

You have:

* created and configured a [Creating and configuring the database in Microsoft
  Azure](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-and-configuring-database-in-microsoft-azure-standard-component-enterprise-click).
* connected the database and published [Creating the connection and publishing the Job to](/talend/en-US/components/8.0/reporting/tdqreportrun-tlogrow-creating-connection-and-publishing-job-to-talend-cloud-standard-component-enterprise-you).

## Procedure

1. In Talend Management Console, go to Tasks and
   plans.

   The Job published from Talend Studio is
   available.
2. To execute the Job (task), click it and click Run now.

## Results

The task executed successfully.
