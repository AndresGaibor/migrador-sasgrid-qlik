<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget · versión 8.0 -->
# tHDFSGet

Last updated: 9/30/2026

Copies files from Hadoop distributed file system(HDFS), pastes them in a
user-defined directory and if needs be, renames them.

tHDFSGet connects to Hadoop distributed file system, helping to obtain
large-scale files with optimized performance.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHDFSGet Standard properties

These properties are used to configure tHDFSGet running in the Standard Job framework.

The Standard
tHDFSGet component belongs to the Big Data and the File families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| *Use an existing connection* | Select this check box and in the Component List click the HDFS connection component from which you want to reuse the connection details already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Hadoop version | Select the Hadoop version of the distribution you are using. |
| Scheme | Select the URI scheme of the file system to be used from the Scheme drop-down list. This scheme could be  * HDFS * WebHDFS. WebHDFS with SSL is not supported yet. * ADLS. Only Azure Data Lake Storage Gen1 is supported.   The schemes present on this list vary depending on the distribution you are using and only the scheme that appears on this list with a given distribution is officially supported by Talend.  Once a scheme is selected, the corresponding syntax such as webhdfs://localhost:50070/ for WebHDFS is displayed in the field for the NameNode location of your cluster.  If you have selected ADLS, the connection parameters to be defined become:  * In the Client   ID and the Client   key fields, enter, respectively, the authentication   ID and the authentication key generated upon the registration of the   application that the current Job you are developing uses to access   Azure Data Lake Storage.  Ensure that the application to be used   has appropriate permissions to access Azure Data Lake. You can check   this on the Required permissions view of this application on Azure. For   further information, see Azure documentation [Assign the Azure AD application to   the Azure Data Lake Storage account file or folder](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-service-to-service-authenticate-using-active-directory#step-3-assign-the-azure-ad-application-to-the-azure-data-lake-store-account-file-or-folder). * In the Token   endpoint field, copy-paste the OAuth 2.0 token   endpoint that you can obtain from the Endpoints list accessible on the App registrations page on your   Azure portal.  For a video demonstration, see [Configure and use Azure in a Job](https://www.youtube.com/watch?v=Ww9-sp5Kd1o). |
| Use Knox | Select this check box to enable support for Apache Knox when the Scheme is set to WebHDFS. When selected, additional Knox-specific options become available for secure gateway access.  * Knox Gateway: Enter the URL of the Knox gateway. * User: Enter the Knox username for authentication. * Password: Enter the Knox password for authentication. * Set Knox timeout (s): Option to define a custom connection   timeout. When enabled, the Knox timeout field appears.  The following options are hidden when Use Knox is selected:   * NameNode URI |
| NameNode URI | Type in the URI of the Hadoop NameNode, the master node of a Hadoop system. For example, we assume that you have chosen a machine called *masternode* as the NameNode, then the location is `hdfs://masternode:portnumber`. If you are using WebHDFS, the location should be webhdfs://masternode:portnumber; WebHDFS with SSL is not supported yet. |
| Use kerberos authentication | If you are accessing the Hadoop cluster running with Kerberos security, select this checkbox, then, enter the Kerberos principal name for the NameNode in the field displayed. This enables you to use your username to authenticate against the credentials stored in Kerberos.  This check box is available depending on the Hadoop distribution you are connecting to. |
| Use MapR Ticket authentication | Select this checkbox to authenticate using MapR Ticket, and enter the following information:  * User name: Enter your username. * Group: Enter the name of the group. * Password: Enter your password to authenticate to   MapR Ticket. * Cluster name: Enter the name of the cluster you want   to use. * Ticket duration: Enter the duration of the ticket in seconds. For example:   86400L, where L corresponds to a   long integer. |
| Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| User name | The User name field is available when you are not using Kerberos to authenticate. In the User name field, enter the login username for your distribution. If you leave it empty, the username of the machine hosting Talend Studio will be used. |
| Group | Enter the membership including the authentication user under which the HDFS instances were started. This field is available depending on the distribution you are using. |
| HDFS directory | Browse to, or enter the path pointing to the data to be used in the file system. |
| Local directory | Browse to, or enter the local directory to store the files obtained from HDFS. |
| Action on File | Select the action that you want to perform on the file:  * Create: Create a new file. * Overwrite: Overwrite the data in the existing   file. * Append: Insert the data into the file. |
| Include subdirectories | Select this check box if the selected input source type includes sub-directories. |
| Files | In the Files area, the fields to be completed are:  * File mask: type in the file name to be selected from   HDFS. Regular expression is available. * New name: give a new name to the obtained file. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Hadoop properties | *Talend Studio* uses a default configuration for its engine to perform operations in a Hadoop distribution. If you need to use a custom configuration in a specific situation, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those default ones.  * Note that if you are using the centrally stored metadata from the Repository, this table automatically inherits the   properties defined in that metadata and becomes uneditable unless you change the   Property type from Repository to Built-in.  For further information about the properties required by Hadoop and its related systems such as HDFS and Hive, see the documentation of the Hadoop distribution you are using or see [Apache's Hadoop documentation](http://hadoop.apache.org/docs) and then select the version of the documentation you want. For demonstration purposes, the links to some properties are listed below:  * Typically, the HDFS-related properties can be found in the *hdfs-default.xml* file of your distribution, such as <http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml>. * Apache also provides a page to list the [Hive-related properties](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties). |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_FILE: the number of files processed. This is an After variable and it returns an integer.  CURRENT\_STATUS: the execution result of the component. This is a Flow variable and it returns a string.  TRANSFER\_MESSAGES: file transferred information. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component combines HDFS connection and data extraction, thus used as a single-component subJob to move data from HDFS to an user-defined local directory. Different from the tHDFSInput and the tHDFSOutput components, it runs standalone and does not generate input or output flow for the other components.  It is often connected to the Job using OnSubjobOk or OnComponentOk link, depending on the context. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your HDFS connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access files in different HDFS systems or different distributions, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of *Talend Studio*.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
| Limitations | JRE 1.6+ is required. |

**Related concepts**  

* [Computing data with Hadoop distributed file system](thdfsget-thdfsput-tfileinputdelimited-tlogrow-computing-data-with-hadoop-distributed-file-system-standard-component-bigdata-the)
* [Iterating on a HDFS directory](thdfslist-thdfsget-thdfsconnection-iterating-on-hdfs-directory-standard-component-bigdata-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-computing-data-with-hadoop-distributed-file-system-standard-component-bigdata-the -->
# Computing data with Hadoop distributed file system

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

The following scenario describes a simple Job that creates a file in a defined
directory, get it into and out of HDFS, subsequently store it to another local directory, and
read it at the end of the Job.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-setting-up-job-standard-component-bigdata-drop)
* [Configuring the input component](/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-configuring-input-component-standard-component-bigdata)
* [Configuring the tFileOutputDelimited component](/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-configuring-tfileoutputdelimited-component-standard-component-bigdata)
* [Loading the data from the local file](/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-loading-data-from-local-file-standard-component-bigdata)
* [Getting the data from the HDFS](/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-getting-data-from-hdfs-standard-component-bigdata)
* [Reading data from the HDFS and saving the data locally](/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-reading-data-from-hdfs-and-saving-data-locally-standard-component-bigdata)
* [Executing the Job](/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-executing-job-standard-component-bigdata-save)

**Related reference**  

* [tHDFSGet](thdfsget "Copies files from Hadoop distributed file system(HDFS), pastes them in a user-defined directory and if needs be, renames them.")
* [tHDFSPut](thdfsput "Connects to Hadoop distributed file system to load large-scale files into it with optimized performance.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-configuring-input-component-standard-component-bigdata -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to define
   the component in its Basic settings
   view.
2. Set the Schema to Built-In and click the [...] button next to Edit
   Schema to describe the data structure you want to create from
   internal variables. In this scenario, the schema contains one column:
   *content*.
3. Click the plus button to add the parameter line.
4. Click OK to close the dialog
   box and accept to propagate the changes when prompted by Talend Studio.
5. In Basic settings, define the
   corresponding value in the Mode area using
   the Use Single Table option. In this
   scenario, the value is *"Hello world!"*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-configuring-tfileoutputdelimited-component-standard-component-bigdata -->
# Configuring the tFileOutputDelimited component

Last updated: 9/30/2026

## Procedure

1. Double-click tFileOutputDelimited to
   define the component in its Basic settings
   view.
2. Click the [...] button next to the
   File Name field and browse to the
   output file you want to write data in, *in.txt* in this
   example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-executing-job-standard-component-bigdata-save -->
# Executing the Job

Last updated: 9/30/2026

Save the Job and press F6 to execute it.

The *in.txt* file is created and loaded into the HDFS.

The file is also extracted from the HDFS by tHDFSGet and is read by tFileInputDelimited.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-getting-data-from-hdfs-standard-component-bigdata -->
# Getting the data from the HDFS

Last updated: 9/30/2026

## Procedure

1. Double-click tHDFSGet to define the
   component in its Basic settings
   view.
2. Select, for example, Apache 0.20.2 from the Hadoop
   version list.
3. In the NameNode URI, the
   Username, the Group fields, enter the connection parameters to
   the HDFS.  If you are using WebHDFS, the location should be
   webhdfs://masternode:portnumber; WebHDFS with SSL is not
   supported yet.
4. In the HDFS directory field, type in
   location storing the loaded file in HDFS. In this example, it is
   */testFile*.
5. Next to the Local directory field, click
   the [...] button to browse to the
   folder intended to store the files that are extracted out of the HDFS. In
   this scenario, the directory is:
   *C:/hadoopfiles/getFile/*.
6. Click the Overwrite file field to stretch
   the drop-down.
7. From the menu, select always.
8. In the Files area, click the plus button
   to add a row in which you define the file to be extracted.
9. In the File mask column, enter
   *\*.txt* to replace *newLine*
   between quotation marks and leave the New
   name column as it is. This allows you to extract all the
   *.txt* files from the specified directory in the HDFS
   without changing their names. In this example, the file is*in.txt*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-loading-data-from-local-file-standard-component-bigdata -->
# Loading the data from the local file

Last updated: 9/30/2026

## Procedure

1. Double-click tHDFSPut to define the
   component in its Basic settings
   view.
2. Select, for example, Apache 0.20.2 from the Hadoop
   version list.
3. In the NameNode URI, the
   Username and the Group fields, enter the connection parameters to
   the HDFS.  If you are using WebHDFS, the location should be
   webhdfs://masternode:portnumber; WebHDFS with SSL is not
   supported yet.
4. Next to the Local directory field, click
   the [...] button to browse to the
   folder with the file to be loaded into the HDFS. In this scenario, the
   directory has been specified while configuring tFileOutputDelimited:
   *C:/hadoopfiles/putFile/*.
5. In the HDFS directory field, type in the
   intended location in HDFS to store the file to be loaded. In this example,
   it is */testFile*.
6. Click the Overwrite file field to stretch
   the drop-down.
7. From the menu, select always.
8. In the Files area, click the plus button
   to add a row in which you define the file to be loaded.
9. In the File mask column, enter
   *\*.txt* to replace *newLine*
   between quotation marks and leave the New
   name column as it is. This allows you to extract all the
   *.txt* files in the specified directory without
   changing their names. In this example, the file is*in.txt*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-reading-data-from-hdfs-and-saving-data-locally-standard-component-bigdata -->
# Reading data from the HDFS and saving the data locally

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputDelimited to
   define the component in its Basic settings
   view.
2. Set property type to Built-In.
3. Next to the File Name/Stream field, click
   the [...] button to browse to the file you have obtained from the HDFS.
   In this scenario, the directory is
   *C:/hadoopfiles/getFile/in.txt*.
4. Set Schema to Built-In and click Edit
   schema to define the data to pass on to the tLogRow component.
5. Click the plus button to add a new column.
6. Click OK to close the dialog
   box and accept to propagate the changes when prompted by Talend Studio.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsget-thdfsput-tfileinputdelimited-tlogrow-setting-up-job-standard-component-bigdata-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tFileOutputDelimited, tHDFSPut, tHDFSGet,
   tFileInputDelimited and tLogRow.
2. Connect tFixedFlowInput to tFileOutputDelimited using a Row > Main
   connection.
3. Connect tFileInputDelimited to tLogRow using a Row > Main
   connection.
4. Connect tFixedFlowInput to tHDFSPut using an OnSubjobOk connection.
5. Connect tHDFSPut to tHDFSGet using an OnSubjobOk connection.
6. Connect tHDFSGet to tFileInputDelimitedusing an OnSubjobOk connection.
