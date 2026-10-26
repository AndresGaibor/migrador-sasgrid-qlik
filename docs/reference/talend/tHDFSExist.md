<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsexist · versión 8.0 -->
# tHDFSExist

Last updated: 9/30/2026

Checks whether a file exists in a specific directory in HDFS.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHDFSExist Standard properties

These properties are used to configure tHDFSExist running in the Standard Job framework.

The Standard
tHDFSExist component belongs to the Big Data and the File families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| *Use an existing connection* | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Hadoop version | Select the Hadoop version of the distribution you are using. |
| Scheme | Select the URI scheme of the file system to be used from the Scheme drop-down list. This scheme could be  * HDFS * WebHDFS. WebHDFS with SSL is not supported yet. * ADLS. Only Azure Data Lake Storage Gen1 is supported.   The schemes present on this list vary depending on the distribution you are using and only the scheme that appears on this list with a given distribution is officially supported by Talend.  Once a scheme is selected, the corresponding syntax such as webhdfs://localhost:50070/ for WebHDFS is displayed in the field for the NameNode location of your cluster.  If you have selected ADLS, the connection parameters to be defined become:  * In the Client   ID and the Client   key fields, enter, respectively, the authentication   ID and the authentication key generated upon the registration of the   application that the current Job you are developing uses to access   Azure Data Lake Storage.  Ensure that the application to be used   has appropriate permissions to access Azure Data Lake. You can check   this on the Required permissions view of this application on Azure. For   further information, see Azure documentation [Assign the Azure AD application to   the Azure Data Lake Storage account file or folder](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-service-to-service-authenticate-using-active-directory#step-3-assign-the-azure-ad-application-to-the-azure-data-lake-store-account-file-or-folder). * In the Token   endpoint field, copy-paste the OAuth 2.0 token   endpoint that you can obtain from the Endpoints list accessible on the App registrations page on your   Azure portal.  For a video demonstration, see [Configure and use Azure in a Job](https://www.youtube.com/watch?v=Ww9-sp5Kd1o). |
| Use Knox | Select this check box to enable support for Apache Knox when the Scheme is set to WebHDFS. When selected, additional Knox-specific options become available for secure gateway access.  * Knox Gateway: Enter the URL of the Knox gateway. * User: Enter the Knox username for authentication. * Password: Enter the Knox password for authentication. * Set Knox timeout (s): Option to define a custom connection   timeout. When enabled, the Knox timeout field appears.  The following options are hidden when Use Knox is selected:   * NameNode URI * Use Datanode Hostname * Use kerberos authentication * User name * Use MapR Ticket authentication |
| NameNode URI | Type in the URI of the Hadoop NameNode, the master node of a Hadoop system. For example, we assume that you have chosen a machine called *masternode* as the NameNode, then the location is `hdfs://masternode:portnumber`. If you are using WebHDFS, the location should be webhdfs://masternode:portnumber; WebHDFS with SSL is not supported yet. |
| Use kerberos authentication | If you are accessing the Hadoop cluster running with Kerberos security, select this checkbox, then, enter the Kerberos principal name for the NameNode in the field displayed. This enables you to use your username to authenticate against the credentials stored in Kerberos.  This check box is available depending on the Hadoop distribution you are connecting to. |
| Use MapR Ticket authentication | Select this checkbox to authenticate using MapR Ticket, and enter the following information:  * User name: Enter your username. * Group: Enter the name of the group. * Password: Enter your password to authenticate to   MapR Ticket. * Cluster name: Enter the name of the cluster you want   to use. * Ticket duration: Enter the duration of the ticket in seconds. For example:   86400L, where L corresponds to a   long integer. |
| Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| User name | The User name field is available when you are not using Kerberos to authenticate. In the User name field, enter the login username for your distribution. If you leave it empty, the username of the machine hosting Talend Studio will be used. |
| Group | Enter the membership including the authentication user under which the HDFS instances were started. This field is available depending on the distribution you are using. |
| HDFS directory | Browse to, or enter the path pointing to the data to be used in the file system. |
| File name or relative path | Enter the name of the file you want to check whether this file exists. Or if needs be, browse to the file or enter the path to the file, relative to the directory you entered in HDFS directory. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Hadoop properties | *Talend Studio* uses a default configuration for its engine to perform operations in a Hadoop distribution. If you need to use a custom configuration in a specific situation, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those default ones.  * Note that if you are using the centrally stored metadata from the Repository, this table automatically inherits the   properties defined in that metadata and becomes uneditable unless you change the   Property type from Repository to Built-in.  For further information about the properties required by Hadoop and its related systems such as HDFS and Hive, see the documentation of the Hadoop distribution you are using or see [Apache's Hadoop documentation](http://hadoop.apache.org/docs) and then select the version of the documentation you want. For demonstration purposes, the links to some properties are listed below:  * Typically, the HDFS-related properties can be found in the *hdfs-default.xml* file of your distribution, such as <http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml>. * Apache also provides a page to list the [Hive-related properties](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties). |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | EXISTS: the result of whether a specified file exists. This is a Flow variable and it returns a Boolean.  FILENAME: the name of the file processed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tHDFSExist is a standalone component. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your HDFS connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access files in different HDFS systems or different distributions, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of *Talend Studio*.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
| Limitations | JRE 1.6+ is required. |

**Related concepts**  

* [Checking the existence of a file in HDFS](thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-checking-existence-of-file-in-hdfs-standard-component-bigdata-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-checking-existence-of-file-in-hdfs-standard-component-bigdata-in-this -->
# Checking the existence of a file in HDFS

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

In this scenario, the two-component Job checks whether a specific file exists in HDFS
and returns a message to indicate the result of the verification.

In the real-world practice, you can take further action to process the file checked
according to the verification result, using the other HDFS components provided with the
Studio.

Launch the Hadoop distribution in which you want to check the existence of a
particular file. Then, proceed as follows:

### In this section

* [Linking the components](/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-linking-components-standard-component-bigdata-in)
* [Configuring the connection to HDFS](/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-configuring-connection-to-hdfs-standard-component-bigdata)
* [Defining the message to be returned](/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-defining-message-to-be-returned-standard-component-bigdata)
* [Defining the condition](/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-defining-condition-standard-component-bigdata-click)
* [Executing the Job](/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-executing-job-standard-component-bigdata-press-f6)

**Related reference**  

* [tHDFSExist](thdfsexist "Checks whether a file exists in a specific directory in HDFS.")
* [tHDFSConnection](thdfsconnection "Connects to a given HDFS so that the other Hadoop components can reuse the connection it creates to communicate with this HDFS.")

**Related information**  

* [tMsgBox](/talend/en-US/components/8.0/tmsgbox/tmsgbox)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-configuring-connection-to-hdfs-standard-component-bigdata -->
# Configuring the connection to HDFS

Last updated: 9/30/2026

## Procedure

1. Double-click tHDFSExist to open its
   Component view.
2. In the Version area, select the Hadoop
   distribution you are connecting to and its version.
3. In the Connection area, enter the values
   of the parameters required to connect to the HDFS.

   In the real-world practice, you may use tHDFSConnection to create a connection and reuse it from the
   current component. For further information, see [tHDFSConnection](/talend/en-US/components/8.0/hdfs/thdfsconnection).
4. In the HDFS Directory field, browse to,
   or enter the path to the folder where the file to be checked is. In this
   example, browse to */user/ychen/data/hdfs/out/dest*.
5. In the File name or relative path field,
   enter the name of the file you want to check the existence. For example,
   output.csv.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-defining-condition-standard-component-bigdata-click -->
# Defining the condition

Last updated: 9/30/2026

## Procedure

1. Click the If link to open the Basic settings view, where you are able to define
   the condition for checking the existence of this file.
2. In the Condition box, press Ctrl+Space to access the variable list and select
   the global variable EXISTS. Type an
   exclamation mark before the variable to negate the meaning of the
   variable.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-defining-message-to-be-returned-standard-component-bigdata -->
# Defining the message to be returned

Last updated: 9/30/2026

## Procedure

1. Double-click tMsgBox to open its
   Component view.
2. In the Title field, enter the title to be
   used for the pop-up message box to be created.
3. In the Buttons list, select *OK*. This defines the button to be displayed on
   the message box.
4. In the Icon list, select *Icon information*.
5. In the Message field, enter the message
   you want to displayed once the file checking is done. In this example, enter
   *"This file does not exist!"*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-executing-job-standard-component-bigdata-press-f6 -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Press F6 to execute this Job.

## Results

Once done, a message box pops up to indicate that this file called *output.csv* does not exist in the directory you defined
earlier.

In the HDFS we check the existence of the file, browse to this directory
specified, you can see that this file does not exist.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hdfs/thdfsexist-thdfsconnection-tmsgbox-thdfsconnection-tmsgbox-linking-components-standard-component-bigdata-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the 
   Integration
    perspective of
   *Talend Studio*, create an empty Job, named *hdfsexist\_file* for example, from the
   Job Designs node in the Repository tree view.

   For further information about how to create a Job, see [Creating a Job](/talend/r/en-US/8.0/studio-user-guide/creating-job).
2. Drop tHDFSExist and tMsgBox onto the workspace.
3. Connect them using the Trigger > Run if
   link.
