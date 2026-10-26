<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsinput · versión 8.0 -->
# tHDFSInput

Last updated: 9/30/2026

Extracts the data in a HDFS file for other components to process it.

tHDFSInput reads a file located on a given Hadoop distributed file
system (HDFS) and puts the data of interest from this file into a Talend schema.
Then it passes the data to the component that follows.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHDFSInput Standard properties

These properties are used to configure tHDFSInput running in the Standard Job framework.

The Standard
tHDFSInput component belongs to the Big Data and the File families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| *Use an existing connection* | Select this check box and in the Component List click the HDFS connection component from which you want to reuse the connection details already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Hadoop version | Select the Hadoop version of the distribution you are using. |
| Scheme | Select the URI scheme of the file system to be used from the Scheme drop-down list. This scheme could be  * HDFS * WebHDFS. WebHDFS with SSL is not supported yet. * ADLS. Only Azure Data Lake Storage Gen1 is supported.   The schemes present on this list vary depending on the distribution you are using and only the scheme that appears on this list with a given distribution is officially supported by Talend.  Once a scheme is selected, the corresponding syntax such as webhdfs://localhost:50070/ for WebHDFS is displayed in the field for the NameNode location of your cluster.  If you have selected ADLS, the connection parameters to be defined become:  * In the Client   ID and the Client   key fields, enter, respectively, the authentication   ID and the authentication key generated upon the registration of the   application that the current Job you are developing uses to access   Azure Data Lake Storage.  Ensure that the application to be used   has appropriate permissions to access Azure Data Lake. You can check   this on the Required permissions view of this application on Azure. For   further information, see Azure documentation [Assign the Azure AD application to   the Azure Data Lake Storage account file or folder](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-service-to-service-authenticate-using-active-directory#step-3-assign-the-azure-ad-application-to-the-azure-data-lake-store-account-file-or-folder). * In the Token   endpoint field, copy-paste the OAuth 2.0 token   endpoint that you can obtain from the Endpoints list accessible on the App registrations page on your   Azure portal.  For a video demonstration, see [Configure and use Azure in a Job](https://www.youtube.com/watch?v=Ww9-sp5Kd1o). |
| NameNode URI | Type in the URI of the Hadoop NameNode, the master node of a Hadoop system. For example, we assume that you have chosen a machine called *masternode* as the NameNode, then the location is `hdfs://masternode:portnumber`. If you are using WebHDFS, the location should be webhdfs://masternode:portnumber; WebHDFS with SSL is not supported yet. |
| Use kerberos authentication | If you are accessing the Hadoop cluster running with Kerberos security, select this checkbox, then, enter the Kerberos principal name for the NameNode in the field displayed. This enables you to use your username to authenticate against the credentials stored in Kerberos.  This check box is available depending on the Hadoop distribution you are connecting to. |
| Use MapR Ticket authentication | Select this checkbox to authenticate using MapR Ticket, and enter the following information:  * User name: Enter your username. * Group: Enter the name of the group. * Password: Enter your password to authenticate to   MapR Ticket. * Cluster name: Enter the name of the cluster you want   to use. * Ticket duration: Enter the duration of the ticket in seconds. For example:   86400L, where L corresponds to a   long integer. |
| Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| User name | The User name field is available when you are not using Kerberos to authenticate. In the User name field, enter the login username for your distribution. If you leave it empty, the username of the machine hosting Talend Studio will be used. |
| Group | Enter the membership including the authentication user under which the HDFS instances were started. This field is available depending on the distribution you are using. |
| File Name | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will read all of the files stored in that folder. Furthermore, if sub-folders exist in that folder and you need to read files in the sub-folders, select the Include sub-directories if path is directory check box in the Advanced settings view. |
| Type | Select the type of the file to be processed. The type of the file may be:  * Text file. * Sequence file: a Hadoop sequence file   consists of binary key/value pairs and is suitable for the Map/Reduce framework.   For further information, see <http://wiki.apache.org/hadoop/SequenceFile>.  Once you select the Sequence file format, the   Key column list and the Value column list appear to allow you to select the   keys and the values of that Sequence file to be processed. |
| Row separator | The separator used to identify the end of a row.  This field is not available for a Sequence file. |
| Field separator | Enter a character, a string, or a regular expression to separate fields for the transferred data.  This field is not available for a Sequence file. |
| Header | Set values to ignore the header of the transferred data. For example, enter *0* to ignore no rows for the data without header and set *1* for the data with header at the first row. This field is not available for a Sequence file. |
| Custom encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>.  This option is not available for a Sequence file. |
| Compression | Select the Uncompress the data check box to uncompress the input data.  Hadoop provides different compression formats that help reduce the space needed for storing files and speed up data transfer. When reading a compressed file, Talend Studio needs to uncompress it before being able to feed it to the input flow.  This option is not available for a Sequence file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Include sub-directories if path is directory | Select this check box to read not only the folder you have specified in the File name field but also the sub-folders in that folder. |
| Hadoop properties | *Talend Studio* uses a default configuration for its engine to perform operations in a Hadoop distribution. If you need to use a custom configuration in a specific situation, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those default ones.  * Note that if you are using the centrally stored metadata from the Repository, this table automatically inherits the   properties defined in that metadata and becomes uneditable unless you change the   Property type from Repository to Built-in.  For further information about the properties required by Hadoop and its related systems such as HDFS and Hive, see the documentation of the Hadoop distribution you are using or see [Apache's Hadoop documentation](http://hadoop.apache.org/docs) and then select the version of the documentation you want. For demonstration purposes, the links to some properties are listed below:  * Typically, the HDFS-related properties can be found in the *hdfs-default.xml* file of your distribution, such as <http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml>. * Apache also provides a page to list the [Hive-related properties](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties). |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. Note that this check box is not available in the Map/Reduce version of the component. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component needs an output link. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your HDFS connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access files in different HDFS systems or different distributions, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of *Talend Studio*.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
| Limitations | JRE 1.6+ is required. |

**Related concepts**  

* [Using HDFS components to work with Azure Data Lake Storage (ADLS)](thdfsinput-thdfsoutput-tlogrow-tfixedflowinput-using-hdfs-components-to-work-with-azure-data-lake-storage-adls "This scenario describes how to use the HDFS components to read data from and write data to Azure Data Lake Storage.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsinput-thdfsoutput-tlogrow-tfixedflowinput-using-hdfs-components-to-work-with-azure-data-lake-storage-adls -->
# Using HDFS components to work with Azure Data Lake Storage (ADLS)

Last updated: 9/30/2026

This scenario describes how to use the HDFS components to read data from and write data to Azure Data Lake Storage.

This scenario applies only to Talend products
with Big Data.

* tFixedFlowInput: it provides sample data to the Job.
* tHDFSOutput: it writes sample data to Azure Data Lake
  Store.
* tHDFSInput: it reads sample data from Azure Data Lake
  Store.
* tLogRow: it displays the output of the Job on the console of
  the Run view of the Job.

### In this section

* [Grant your application the access to your ADLS Gen2](/talend/en-US/components/8.0/hdfs/tazurefsconfiguration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-grant-your-application-access-to-your-adls-gen2-an-azure?id=2566)
* [Creating an HDFS Job in Talend Studio](/talend/en-US/components/8.0/hdfs/thdfsinput-thdfsoutput-tlogrow-tfixedflowinput-creating-hdfs-job-in-studio-on)
* [Configuring the HDFS components to work with Azure Data Lake Storage](/talend/en-US/components/8.0/hdfs/thdfsinput-thdfsoutput-tlogrow-tfixedflowinput-configuring-hdfs-components-to-work-with-azure-data-lake-storage)

**Related reference**  

* [tHDFSInput](thdfsinput "Extracts the data in a HDFS file for other components to process it.")
* [tHDFSOutput](thdfsoutput "Writes data flows it receives into a given Hadoop distributed file system (HDFS).")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsinput-thdfsoutput-tlogrow-tfixedflowinput-configuring-hdfs-components-to-work-with-azure-data-lake-storage -->
# Configuring the HDFS components to work with Azure Data Lake Storage

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Component view to provide sample data to the
   Job.

   The sample data to be used contains only one row with two column:
   `id` and `name`.
2. Click the [...] button next to Edit
   schema to open the schema editor.
3. Click the [+] button to add the two columns and rename
   them to `id` and `name`.
4. Click OK to close the schema editor and validate the
   schema.
5. In the Mode area, select Use single
   table.

   The `id` and the `name` columns
   automatically appear in the Value table and you can
   enter the values you want within double quotation marks in the
   Value column for the two schema values.
6. Double-click tHDFSOutput to open its
   Component view.

   ### Example
7. In the Version area, select
   Hortonworks or Cloudera
   depending on the distribution you are using. In the Standard
   framework, only these two distributions with ADLS are supported by the HDFS
   components.
8. From the Scheme drop-down list, select
   ADLS. The ADLS related parameters appear in the
   Component view.
9. In the URI field, enter the NameNode service of your
   application. The location of this service is actually the address of your Data
   Lake Store.

   For example, if your Data Lake Storage name is
   `data_lake_store_name`, the NameNode URI to be used
   is
   `adl://data_lake_store_name.azuredatalakestore.net`.
10. In the Client
    ID and the Client
    key fields, enter, respectively, the authentication
    ID and the authentication key generated upon the registration of the
    application that the current Job you are developing uses to access
    Azure Data Lake Storage.

    Ensure that the application to be used
    has appropriate permissions to access Azure Data Lake. You can check
    this on the Required permissions view of this application on Azure. For
    further information, see Azure documentation [Assign the Azure AD application to
    the Azure Data Lake Storage account file or folder](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-service-to-service-authenticate-using-active-directory#step-3-assign-the-azure-ad-application-to-the-azure-data-lake-store-account-file-or-folder).

    This application must
    be the one to which you assigned permissions to access your Azure Data
    Lake Storage in the previous step.
11. In the Token
    endpoint field, copy-paste the OAuth 2.0 token
    endpoint that you can obtain from the Endpoints list accessible on the App registrations page on your
    Azure portal.
12. In the File name field, enter the directory to be used
    to store the sample data on Azure Data Lake Storage.
13. From the Action drop-down list, select
    Create if the directory to be used does not exist yet
    on Azure Data Lake Storage; if this folder already exists, select
    Overwrite.
14. Do the same configuration for tHDFSInput.
15. Press F6 to run your Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsinput-thdfsoutput-tlogrow-tfixedflowinput-creating-hdfs-job-in-studio-on -->
# Creating an HDFS Job in Talend Studio

Last updated: 9/30/2026

## Procedure

1. On the Integration
   perspective, drop the following components from the
   Palette onto the design workspace:
   tFixedFlowInput, tHDFSOutput,
   tHDFSInput and tLogRow.
2. Connect tFixedFlowInput to
   tHDFSOutput using a Row > Main link.
3. Do the same to connect tHDFSInput to
   tLogRow.
4. Connect tFixedFlowInput to tHDFSInput using a Trigger > OnSubjobOk link.

## Results
