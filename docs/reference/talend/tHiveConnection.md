<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection · versión 8.0 -->
# tHiveConnection

Last updated: 9/30/2026

Establishes a Hive connection to be reused by other Hive components in your
Job.

tHiveConnection opens a
connection to a Hive database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHiveConnection Standard properties

These properties are used to configure tHiveConnection running in the Standard Job framework.

The Standard
tHiveConnection component belongs to the Big Data, the Databases and the ELT families.

The component in this framework is available in all Talend
products.

## Basic settings

Connection configuration:

* When you use this component with Google Dataproc:

  | Project ID | Enter the ID of your Google Cloud Platform project.  If you are not certain about your project ID, confirm it in the Manage Resources page of your Google Cloud Platform services. |
  | Cluster ID | Enter the ID of your Dataproc cluster to be used. |
  | Region | From this drop-down list, select the Google Cloud region to be used. |
  | Google Storage staging bucket | As a Talend Job expects its dependent jar files for execution, specify the Google Storage directory to which these jar files are transferred so that your Job can access these files at execution.  The directory to be entered must end with a slash (/). If not existing, the directory is created on the fly but the bucket to be used must already exist. |
  | Database | Fill this field with the name of the database. |
  | Provide Google Credentials in file | Leave this check box clear, when you launch your Job from a given machine in which Google Cloud SDK has been installed and authorized to use your user account credentials to access Google Cloud Platform. In this situation, this machine is often your local machine.  When you launch your Job from a remote machine, such as a Talend JobServer, select this check box and in the Path to Google Credentials file field that is displayed, enter the directory in which this JSON file is stored in the Talend JobServer machine. You can also click the [...] button, and then in the pop-up dialog box, browse for the JSON file.  For further information about this Google Credentials file, see the administrator of your Google Cloud Platform or visit [Google Cloud Platform Auth Guide](https://cloud.google.com/docs/authentication). |
* When you use this component with Microsoft HDInsight distribution:

  | Livy configuration | Enter the address and the authentication information of the Microsoft HD Insight cluster to be used. For example, the address could be `https://your_hdinsight_cluster_name.azurehdinsight.net` and the authentication information is your Azure account name: `yourname`. Talend Studio uses this service to submit the Job to the HD Insight cluster.  In the Job result folder field, enter the location in which you want to store the execution result of a Job in the Azure Storage to be used. |
  | Job status polling configuration | In the Poll interval when retrieving Job status (in ms) field, enter the time interval (in milliseconds) at the end of which you want Talend Studio to ask Spark for the status of your Job. For example, this status could be Pending or Running.  In the Maximum number of consecutive statuses missing field, enter the maximum number of times Talend Studio should retry to get a status when there is no status response. |
  | HDInsight configuration | + The Username is the   one defined when creating your cluster. You can find it in the   SSH + Cluster login blade of your   cluster. + The Password is   defined when creating your HDInsight cluster for authentication to this   cluster. |
  | Windows Azure Storage configuration | Enter the address and the authentication information of the Azure Storage or ADLS Gen2 account to be used. In this configuration, you do not define where to read or write your business data but define where to deploy your Job only.  In the Container field, enter the name of the container to be used. You can find the available containers in the Blob blade of the Azure Storage account to be used.  In the Deployment Blob field, enter the location in which you want to store the current Job and its dependent libraries in this Azure Storage account.  In the Hostname field, enter the Primary Blob Service Endpoint of your Azure Storage account without the https:// part. You can find this endpoint in the Properties blade of this storage account.  In the Username field, enter the name of the Azure Storage account to be used.  In the Password field, enter the access key of the Azure Storage account to be used. This key can be found in the Access keys blade of this storage account. |
  | Database | Fill this field with the name of the database. |
* When you use the other distributions:

  | Connection mode | Select a connection mode from the list. The options vary depending on the distribution you are using. |
  | Hive version | Select the Hive version you are using. |
  | Host | Enter the database server IP address. |
  | Port | Enter the listening port number of DB server. |
  | Database | Fill this field with the name of the database. |
  | Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
  | Use kerberos authentication | If you are accessing a Hive metastore running with Kerberos security, select this checkbox and then enter the relevant parameters in the fields that appear.  The values of the following parameters can be found in the *hive-site.xml* file of the Hive system to be used. 1. Hive principal uses the value    of *hive.metastore.kerberos.principal*. This is    the service principal of the Hive metastore. 2. HiveServer2 local user    principal uses the value of *hive.server2.authentication.kerberos.principal*. 3. HiveServer2 local user keytab    uses the value of *hive.server2.authentication.kerberos.keytab* 4. Metastore URL uses the value of    *javax.jdo.option.ConnectionURL*. This is the    JDBC connection string to the Hive metastore. 5. Driver class uses the value of    *javax.jdo.option.ConnectionDriverName*. This    is the name of the driver for the JDBC connection. 6. Username uses the value of *javax.jdo.option.ConnectionUserName*. This, as    well as the Password parameter, is the user credential for connecting to    the Hive Metastore. 7. Password uses the value of *javax.jdo.option.ConnectionPassword*.For the other parameters that are displayed, consult the Hadoop configuration files they belong to. For example, the Namenode principal can be found in the *hdfs-site.xml* file or the *hdfs-default.xml* file of the distribution you are using.  This check box is available depending on the Hadoop distribution you are connecting to. |
  | Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
  | Use SSL encryption | Select this checkbox to enable the SSL or TLS encrypted connection.  Then in the fields that are displayed, provide the authentication information: + In the Trust store   path field, enter the path, or browse to the TrustStore   file to be used. By default, the supported TrustStore types are *JKS* and *PKCS 12*. + To enter the password, click the [...] button   next to the password field, enter the password in double quotes in the pop-up dialog box,   and click OK to save the settings.  This feature is available only to the HiveServer2 in the Standalone mode of the following distributions: + Hortonworks Data Platform 2.0 + + Cloudera CDH4 + + Pivotal HD 2.0 + + Amazon EMR 4.0.0 + |
  | Set Resource Manager | Select this check box and in the displayed field, enter the location of the ResourceManager of your distribution. For example, `tal-qa114.talend.lan:8050`.  Then you can continue to set the following parameters depending on the configuration of the Hadoop cluster to be used (if you leave the check box of a parameter clear, then at runtime, the configuration about this parameter in the Hadoop cluster to be used will be ignored ): 1. Select the Set resourcemanager    scheduler address check box and enter the Scheduler address in    the field that appears. 2. Select the Set jobhistory    address check box and enter the location of the JobHistory    server of the Hadoop cluster to be used. This allows the metrics information of    the current Job to be stored in that JobHistory server. 3. Select the Set staging    directory check box and enter this directory defined in your    Hadoop cluster for temporary files created by running programs. Typically, this    directory can be found under the *yarn.app.mapreduce.am.staging-dir* property in the configuration files    such as *yarn-site.xml* or *mapred-site.xml* of your distribution. 4. Allocate proper memory volumes to the Map and the Reduce    computations and the ApplicationMaster    of YARN by selecting the Set memory    check box in the Advanced settings    view. 5. Select the Set Hadoop    user check box and enter the user name under which you    want to execute the Job. Since a file or a directory in Hadoop has its    specific owner with appropriate read or write rights, this field allows    you to execute the Job directly under the user name that has the    appropriate rights to access the file or directory to be processed. 6. Select the Use datanode hostname check box to allow the    Job to access datanodes via their hostnames. This actually sets the *dfs.client.use.datanode.hostname*    property to *true*. When connecting to a    S3N filesystem, you must select this check box.For further information about these parameters, see the documentation or contact the administrator of the Hadoop cluster to be used.  For further information about the Hadoop Map/Reduce framework, see the Map/Reduce tutorial in [Apache's Hadoop documentation](http://hadoop.apache.org). |
  | Set NameNode URI | Select this check box and in the displayed field, enter the URI of the Hadoop NameNode, the master node of a Hadoop system. For example, assuming that you have chosen a machine called `masternode` as the NameNode, then the location is `hdfs://masternode:portnumber`.  If you are using WebHDFS, the location should be webhdfs://masternode:portnumber; WebHDFS with SSL is not supported yet.  For further information about the Hadoop Map/Reduce framework, see the Map/Reduce tutorial in [Apache's Hadoop documentation](http://hadoop.apache.org). |
  | Spark catalog | Select the Spark implementation to use. + In-memory: select this value   if you set the Hive thrift   metastore to a Hive metastore that is   not an external metastore. + Hive: select this value if   you set the Hive thrift   metastore to an external Hive   metastore that exists outside of your cluster. |

The other properties:

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Distribution | Select the cluster you are using from the drop-down list. The options in the list vary depending on the component you are using. Among these options, the following ones requires specific configuration:  * If available in this Distribution drop-down list, the Microsoft HD Insight option allows you to   use a Microsoft HD Insight cluster. For this purpose, you need to configure   the connections to the HD Insight cluster and the Windows Azure Storage   service of that cluster in the areas that are displayed. For detailed   explanation about these parameters, see [Configuring the connection   manually](/talend/r/en-US/7.3/studio-user-guide/configuring-connection-manually). * If you select Amazon EMR,   find more details in [Amazon EMR - Getting Started](/talend/r/en-US/8.0/amazon-emr-getting-started). * The Custom option   allows you to connect to a cluster different from any of the distributions   given in this list, that is to say, to connect to a cluster not officially   supported by    Talend   .   1. Select Import from existing    version to import an officially supported distribution as base    and then add other required jar files which the base distribution does not    provide. 2. Select Import from zip to    import the configuration zip for the custom distribution to be used. This zip    file should contain the libraries of the different Hadoop elements and the index    file of these libraries.  Note that custom versions are not officially supported by    Talend    .     Talend     and its community provide you with the opportunity to connect to    custom versions from Talend Studio but cannot guarantee that the configuration of whichever version you choose    will be easy, due to the wide range of different Hadoop distributions and    versions that are available. As such, you should only attempt to set up such a    connection if you have sufficient Hadoop experience to handle any issues on your    own.  Information noteNote: In this dialog box, the active check box must be kept    selected so as to import the jar files pertinent to the connection to be    created between the custom distribution and this component.  For a step-by-step example about how to connect to a custom    distribution and share this connection, see [Hortonworks](/talend/r/en-US/8.0/hortonworks).   Information noteNote: From Talend Studio 8.0 R2024-04 onwards, the Distribution parameter has been removed. |
| Hive version | Select the HBase version of the distribution you are using.  Information noteNote: From Talend Studio 8.0 R2024-04 onwards, the Hive version parameter has been removed. |
| Hiver Server | Select the Hive version you are using. |
| Hadoop version | Select the Hadoop version you are using. |
| Inspect the classpath for configurations | Select this check box to allow the component to check the configuration files in the directory you have set with the *$HADOOP\_CONF\_DIR* variable and directly read parameters from these files in this directory. This feature allows you to easily change the Hadoop configuration for the component to switch between different environments, for example, from a test environment to a production environment.  In this situation, the fields or options used to configure Hadoop connection and/or Kerberos security are hidden.  If you want to use certain parameters such as the Kerberos parameters but these parameters are not included in these Hadoop configuration files, you need to create a file called *talend-site.xml* and put this file into the same directory defined with *$HADOOP\_CONF\_DIR*. This *talend-site.xml* file should read as follows:  ``` <!-- Put site-specific property overrides in this file. -->  <configuration>      <property>          <name>talend.kerberos.authentication </name>          <value>kinit </value>          <description> Set the Kerberos authentication method to use. Valid values are: kinit or keytab.  </description>      </property>      <property>          <name>talend.kerberos.keytab.principal </name>         <value>user@BIGDATA.COM </value>         <description> Set the keytab's principal name.  </description>     </property>      <property>            <name>talend.kerberos.keytab.path </name>          <value>/kdc/user.keytab </value>          <description> Set the keytab's path.  </description>      </property>      <property>          <name>talend.encryption </name>          <value>none </value>          <description> Set the encryption method to use. Valid values are: none or ssl.  </description>      </property>      <property>          <name>talend.ssl.trustStore.path </name>          <value>ssl </value>          <description> Set SSL trust store path.  </description>      </property>      <property>          <name>talend.ssl.trustStore.password </name>          <value>ssl </value>          <description> Set SSL trust store password.  </description>      </property>  </configuration> ```  The parameters read from these configuration files override the default ones used by Talend Studio. When a parameter does not exist in these configuration files, the default one is used.  Note that this option is available only in Hive Standalone mode with Hive 2. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail. |
| Execution engine | Select this check box and from the drop-down list, select the framework you need to use for big data processing. The available frameworks are MapReduce and Tez.  This property is available with the following connection modes:  * Dataproc * HDInsight * Standalone  Before using Tez or MapReduce, ensure that the Hadoop cluster you are using supports Tez by checking the hive.execution.engine parameter in the hive-site.xml file. You will need to configure the access to the relevant Tez libraries via the Advanced settings view of this component.  For further information about Hive on Tez, see [Apache's related documentation](https://cwiki.apache.org/confluence/display/Hive/Hive+on+Tez). Some examples are presented there to show how Tez can be used to gain performance over MapReduce. |
| Store by HBase | Select this check box to display the parameters to be set to allow the Hive components to access HBase tables:  * Once this access is configured, you will be able to use, in tHiveRow and tHiveInput, the Hive QL statements to read and write data in   HBase. * If you are using the Kerberos authentication, you need to define the HBase   related principals in the corresponding fields that are displayed.  For further information about this access involving Hive and HBase, see Apache's Hive documentation about Hive/HBase integration. |
| Define the jars to register for HBase | Select this check box to display the Register jar for HBase table, in which you can register any missing jar file required by HBase, for example, the Hive Storage Handler, by default, registered along with your Hive installation. |
| Register jar for HBase | Click the [+] button to add rows to this table, then, in the Jar name column, select the JAR file to be registered and in the Jar path column, enter the path pointing to that JAR file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Tez lib | Select how the Tez libraries are accessed:  * Auto install: at runtime, the Job uploads   and deploys the Tez libraries provided by Talend Studio   into the directory you specified in the Install   folder in HDFS field, for example, */tmp/usr/tez*.  If you have set the *tez.lib.uris* property in the properties   table, this directory overrides the value of that property at runtime. But the other   properties set in the properties table are still effective. * Use exist: the Job accesses the Tez libraries already   deployed in the Hadoop cluster to be used. You need to enter the path pointing to   those libraries in the Lib path (folder or file)   field. * Lib jar: this table appears when you have selected Auto install from the Tez   lib list and the distribution you are using is Custom. In this table, you need to add the Tez libraries to be   uploaded. |
| Hadoop properties | *Talend Studio* uses a default configuration for its engine to perform operations in a Hadoop distribution. If you need to use a custom configuration in a specific situation, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those default ones.  * Note that if you are using the centrally stored metadata from the Repository, this table automatically inherits the   properties defined in that metadata and becomes uneditable unless you change the   Property type from Repository to Built-in.  For further information about the properties required by Hadoop and its related systems such as HDFS and Hive, see the documentation of the Hadoop distribution you are using or see [Apache's Hadoop documentation](http://hadoop.apache.org/docs) and then select the version of the documentation you want. For demonstration purposes, the links to some properties are listed below:  * Typically, the HDFS-related properties can be found in the *hdfs-default.xml* file of your distribution, such as <http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml>. * Apache also provides a page to list the [Hive-related properties](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties). |
| Hive properties | *Talend Studio* uses a default configuration for its engine to perform operations in a Hive database. If you need to use a custom configuration in a specific situation, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those default ones. For further information, see [Hive dedicated properties](https://cwiki.apache.org/confluence/display/Hive/AdminManual+Configuration).  * If you need to use Tez to run your Hive Job, add   hive.execution.engine to the   Properties column and Tez to the   Value column, enclosing both of these strings in   double quotation marks. * Note that if you are using the centrally stored metadata   from the Repository, this   table automatically inherits the properties defined in that metadata and   becomes uneditable unless you change the Property type from Repository to Built-in. |
| Path separator in server | Leave the default value of the Path separator in server as it is, unless you have changed the separator used by your Hadoop distribution's host machine for its PATH variable or in other words, that separator is not a colon (:). In that situation, you must change this value to the one you are using in that host. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other Hive components, particularly tHiveClose.  If Talend Studio used to connect to a Hive database is operated on Windows, you must manually create a folder called *tmp* in the root of the disk where Talend Studio is installed. |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |

**Related concepts**  

* [Creating a JDBC Connection to Azure HDInsight Hive](thiveconnection-thiveload-thivecreatetable-thdfsoutput-creating-jdbc-connection-to-azure-hdinsight-hive-standard-component-this)
* [Creating a partitioned Hive table](thiveconnection-thiveload-thivecreatetable-thdfsoutput-creating-partitioned-hive-table-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-creating-jdbc-connection-to-azure-hdinsight-hive-standard-component-this -->
# Creating a JDBC Connection to Azure HDInsight Hive

Last updated: 9/30/2026

This scenario illustrates how to use tHiveConnection, tHiveInput and
tHiveClose to create a JDBC Connection to
HDInsight Hive.

## Prerequisites

Before starting to replicate this scenario, ensure that you have appropriate rights and permissions to access the Hive database to be used.

### In this section

* [Configuring a DataBase Connection to Hive](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-database-connection-to-hive-this)
* [Building the Job](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-building-job-from)

**Related reference**  

* [tHiveConnection](thiveconnection "Establishes a Hive connection to be reused by other Hive components in your Job.")
* [tHiveLoad](thiveload "Writes data of different formats into a given Hive table or to export data from a Hive table to a directory.")
* [tHiveCreateTable](thivecreatetable "Creates Hive tables that fit a wide range of Hive data formats.")

**Related information**  

* [tHDFSOutput](/talend/en-US/components/8.0/hdfs/thdfsoutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-creating-partitioned-hive-table-standard-component-this -->
# Creating a partitioned Hive table

Last updated: 9/30/2026

This scenario illustrates how to use tHiveConnection,
tHiveCreateTable and tHiveLoad to create a partitioned Hive table and write data in
it.

Note that tHiveCreateTable and tHiveLoad are available only when you are using one of the 
Talend
solutions with Big Data.

The sample data to be used in this scenario is employee information of a company,
reading as follows:

```
1;Lyndon;Fillmore;21-05-2008;US
2;Ronald;McKinley;15-08-2008
3;Ulysses;Roosevelt;05-10-2008
4;Harry;Harrison;23-11-2007
5;Lyndon;Garfield;19-07-2007
6;James;Quincy;15-07-2008
7;Chester;Jackson;26-02-2008
8;Dwight;McKinley;16-07-2008
9;Jimmy;Johnson;23-12-2007
10;Herbert;Fillmore;03-04-2008
				
```

The information contains some employees' names and the dates when they are registered
in a HR system. Since these employees work for the US subsidiary of the company, you
will create a US partition for this sample data.

Before starting to replicate this scenario, ensure that you have appropriate rights
and permissions to access the Hive database to be used.

Note that if you are using the Windows operating system, you have to create a
*tmp* folder at the root of the disk where Talend Studio is
installed.

Then proceed as follows:

### In this section

* [Linking the components](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-linking-components-standard-component-in)
* [Configuring the connection to Hive](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-connection-to-hive-standard-component)
* [Creating the Hive table](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-creating-hive-table-standard-component)
* [Writing data to the table](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-writing-data-to-table-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-executing-job-standard-component-then-you)

**Related reference**  

* [tHiveConnection](thiveconnection "Establishes a Hive connection to be reused by other Hive components in your Job.")
* [tHiveLoad](thiveload "Writes data of different formats into a given Hive table or to export data from a Hive table to a directory.")
* [tHiveCreateTable](thivecreatetable "Creates Hive tables that fit a wide range of Hive data formats.")

**Related information**  

* [tHDFSOutput](/talend/en-US/components/8.0/hdfs/thdfsoutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-building-job-from -->
# Building the Job

Last updated: 9/30/2026

## Procedure

1. From the Repository view of the Talend Studio, right-click Job Designs, and then click Create Standard Job.
2. Give a name to your Job.
3. Click Finish.
4. Add a tPreJob component
   to your workspace.
5. Add a tHiveConnection
   component to your workspace.
6. Double-click the tHiveConnection component and choose Repository as the Property Type and the Database Connection created above.
7. Right-click the tPreJob
   component.
8. Select Trigger > On Component Ok and connect the tPreJob to the tHiveConnection.
9. Add a tHiveInput
   component to your workspace.
10. Select it and check the box Use an
    existing connection, then select the tHiveConnection component in the Component List drop-down menu.
11. In the Query field,
    input `show tables` to run a query
    displaying the available tables in the database.
12. Add a tLogRow component
    to your workspace.
13. Right-click the tHiveInput component and select Row > Main.
14. Click the tLogRow
    component to connect both components. They will display the information from the
    query above.
15. From the Component tab of the tLogRow, select Table (print values in celles of a table).
16. Add a tPostJob component
    to your workspace.
17. Add a tHiveClose
    component to your workspace.
18. Connect the tPostJob
    component to the tHiveClose component
    using an On Component Ok connection to
    close the connection opened.
19. From the Run tab,
    click Run to run the Job and ensure of a
    successful connection to Hive on HDInsight and of the readability of the table
    data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-database-connection-to-hive-this -->
# Configuring a DataBase Connection to Hive

Last updated: 9/30/2026

## About this task

This example uses version 3.6 of Azure
HDInsight.

## Procedure

1. In the Repository view,
   extend the Metadata drop-down menu.
2. Click Db Connections, and then right-click Create Connection
   .
3. Give a name to your connection.
4. Click Next.
5. Set up the connection configuration similarly to the following table:

   | DB Type | Select Hive. |
   | Hadoop Cluster | Select None. |
   | Distribution | Select Horton Works.  HDInsight is leveraging Horton Works distribution on the backend. This will allow you to use Horton Works libraries to connect to HDInsighs. |
   | DB Type | Select Hive. |
   | Version | Select Hortonworks Data Platform V2.6.0.3-8 [Built in]. |
   | Hive Model | Select Standalone. |
   | Login  Password  Server | Fill in the fields as required. |
   | Port | Input `443`.  You will be able to communicate through the proxy port since the HDInsight cluster sits behind a proxy by default. |
   | DataBase | Leave default. |
   | Additional JDBC Setting | Input `transportMode=http;ssl=true;httpPath=/hive2`, where: * `transportMode=http` sets the transport mode to HTTP instead of the default Hive JDBC transport mode. * `SSL=true` enables SSL. * `httpPath=/hive2` sets the HTTP endpoint. |
6. Click Test Connection to
   ensure the Talend Studio connects
   successfully to the cluster.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-connection-to-hive-standard-component -->
# Configuring the connection to Hive

Last updated: 9/30/2026

## About this task

Configuring tHiveConnection

## Procedure

1. Double-click tHiveConnection to open its
   Component view.
2. From the Property type list,
   select Built-in. If you have created the
   connection to be used in Repository, then
   select Repository, click the 
   button to open the Repository content dialog box
   and select that connection. This way, Talend Studio
   will reuse that set of connection information for this Job.

   For further information about how to create a Hadoop connection in
   Repository, see [Centralizing Hadoop connections](/talend/r/en-US/8.0/studio-user-guide/centralizing-hadoop-connection).
3. In the Version area, select
   the Hadoop distribution to be used and its version. If you cannot find from the list
   the distribution corresponding to yours, select Custom so as to connect to a Hadoop distribution not officially
   supported in Talend Studio.

   For a step-by-step example about how to use this Custom option, see [Connecting to a custom Hadoop distribution](/talend/en-US/components/8.0/cloudera/connecting-to-custom-hadoop-distribution-standard-component).
4. In the Connection area, enter the
   connection parameters to the Hive database to be used.
5. In the Name node field,
   enter the location of the master node, the NameNode, of the distribution to be
   used. For example, `talend-hdp-all:50300`. If you are using WebHDFS, the location should be
   webhdfs://masternode:portnumber; WebHDFS with SSL is not
   supported yet.
6. In the Job tracker field, enter the
   location of the JobTracker of your distribution. For example, *hdfs://talend-hdp-all:8020*.

   Note that the notion Job in this term JobTracker designates the MR or the
   MapReduce jobs described in Apache's documentation on <http://hadoop.apache.org/>.

### In this section

* [Configuring tHiveConnection](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-thiveconnection-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-creating-hive-table-standard-component -->
# Creating the Hive table

Last updated: 9/30/2026

### In this section

* [Defining the schema](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-defining-schema-standard-component)
* [Defining the table settings](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-defining-table-settings-standard-component-i)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-executing-job-standard-component-then-you -->
# Executing the Job

Last updated: 9/30/2026

Then you can press F6 to run this Job.

Once done, the Run view is opened automatically,
where you can check the execution process.

You can as well verify the results in the web console of the Hadoop distribution
used.

If you need to obtain more details about the Job, it is recommended to use the web
console of the Jobtracker provided by the Hadoop distribution you are using.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-linking-components-standard-component-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective of Talend Studio,
   create an empty Job from the Job Designs node in
   the Repository tree view.

   For further information about how to create a Job, see [Creating a Job](/talend/r/en-US/8.0/studio-user-guide/creating-job).
2. Drop tHiveConnection, tHiveCreateTable and tHiveLoad onto the workspace.
3. Connect them using the Trigger > On Subjob
   OK link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-writing-data-to-table-standard-component -->
# Writing data to the table

Last updated: 9/30/2026

## About this task

Configuring tHiveLoad

## Procedure

1. Double-click tHiveLoad to open its
   Component view.
2. Select the Use an existing connection
   check box and from Component list, select
   the connection configured in the tHiveConnection component you are using for this Job.
3. From the Load action field, select
   LOAD to write data from the file
   holding the sample data that is presented at the beginning of this
   scenario.
4. In the File path field, enter the
   directory where the sample data is stored. In this example, the data is
   stored in the HDFS system to be used.

   In the real-world practice, you can
   use tHDFSOutput to write data into the HDFS
   system and you need to ensure that the Hive application has the appropriate
   rights and permissions to read or even move the data.

   For further information about tHDFSOutput, see [tHDFSOutput](/talend/en-US/components/8.0/hdfs/thdfsoutput).

   for further
   information about the related rights and permissions, see the documentation
   or contact the administrator of the Hadoop cluster to be used.

   Note if you need to read data from a local file system other than the HDFS
   system, ensure that the data to be read is stored in the local file system
   of the machine in which the Job is run and then select the Local check box in this Basic settings view. For example, when the connection mode
   to Hive is Standalone, the Job is run in
   the machine where the Hive application is installed and thus the data should
   be stored in that machine.
5. In the Table name field, enter the name
   of the target table you need to load data in. In this scenario, it is
   *employees*.
6. From the Action on file list, select
   APPEND.
7. Select the Set partitions check box and
   in the field that appears, enter the partition you need to add data to. In
   this scenario, this partition is *country='US'*.

### In this section

* [Configuring tHiveLoad](/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-thiveload-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-thiveconnection-standard-component -->
# Configuring tHiveConnection

Last updated: 9/30/2026

## Procedure

1. Double-click tHiveConnection to open its
   Component view.
2. From the Property type list,
   select Built-in. If you have created the
   connection to be used in Repository, then
   select Repository, click the 
   button to open the Repository content dialog box
   and select that connection. This way, Talend Studio
   will reuse that set of connection information for this Job.

   For further information about how to create a Hadoop connection in
   Repository, see [Centralizing Hadoop connections](/talend/r/en-US/8.0/studio-user-guide/centralizing-hadoop-connection).
3. In the Version area, select
   the Hadoop distribution to be used and its version. If you cannot find from the list
   the distribution corresponding to yours, select Custom so as to connect to a Hadoop distribution not officially
   supported in Talend Studio.

   For a step-by-step example about how to use this Custom option, see [Connecting to a custom Hadoop distribution](/talend/en-US/components/8.0/cloudera/connecting-to-custom-hadoop-distribution-standard-component).
4. In the Connection area, enter the
   connection parameters to the Hive database to be used.
5. In the Name node field, enter
   the location of the master node, the NameNode, of the distribution to be used. For
   example, *talend-hdp-all:50300*.  If you are using WebHDFS, the location should be
   webhdfs://masternode:portnumber; WebHDFS with SSL is not
   supported yet.
6. In the Job tracker field, enter the
   location of the JobTracker of your distribution. For example, *hdfs://talend-hdp-all:8020*.

   Note that the notion Job in this term JobTracker designates the MR or the
   MapReduce jobs described in Apache's documentation on <http://hadoop.apache.org/>.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-defining-schema-standard-component -->
# Defining the schema

Last updated: 9/30/2026

## Procedure

1. Double-click tHiveCreateTable to open its
   Component view.
2. Select the Use an existing connection
   check box and from Component list, select
   the connection configured in the tHiveConnection component you are using for this Job.
3. Click the
   button next to Edit
   schema to open the schema editor.
4. Click the
   button four times to add four rows and in the Column column, rename them to *Id*, *FirstName*, *LastName* and
   *Reg\_date*, respectively.

   Note that you cannot use the Hive reserved keywords to name the columns,
   such as *location* or *date*.
5. In the Type column, select the type of
   the data in each column. In this scenario, *Id* is of the Integer type,
   *Reg\_date* is of the Date type and the others are of the String type.
6. In the DB type column, select the Hive
   type of each column corresponding to their data types you have defined. For
   example, *Id* is of INT and *Reg\_date* is of
   TIMESTAMP.
7. In the Data pattern column, define the
   pattern corresponding to that of the raw data. In this example, use the
   default one.
8. Click OK to validate these
   changes.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-defining-table-settings-standard-component-i -->
# Defining the table settings

Last updated: 9/30/2026

## Procedure

1. In Table name field, enter the name of
   the Hive table to be created. In this scenario, it is *employees*.
2. From the Action on table list, select
   Create table if not exists.
3. From the Format list, select the data
   format that this Hive table in question is created for. In this scenario, it
   is TEXTFILE.
4. Select the Set partitions check box to
   add the *US* partition as explained at the
   beginning of this scenario. To define this partition, click the
   button next to Edit
   schema that appears.
5. Leave the Set file location check box
   clear to use the default path for Hive table.
6. Select the Set Delimited row format check
   box to display the available options of row format.
7. Select the Field check box and enter a
   semicolon (*;*) as field separator in the
   field that appears.
8. Select the Line check box and leave the
   default value as line separator.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveconnection-thiveload-thivecreatetable-thdfsoutput-configuring-thiveload-standard-component -->
# Configuring tHiveLoad

Last updated: 9/30/2026

## Procedure

1. Double-click tHiveLoad to open its
   Component view.
2. Select the Use an existing connection
   check box and from Component list, select
   the connection configured in the tHiveConnection component you are using for this Job.
3. From the Load action field, select
   LOAD to write data from the file
   holding the sample data that is presented at the beginning of this
   scenario.
4. In the File path field, enter
   the directory where the sample data is stored. In this example, the data is
   stored in the HDFS system to be used.  In the real-world
   practice, you can use tHDFSOutput to write
   data into the HDFS system and you need to ensure that the Hive application has
   the appropriate rights and permissions to read or even move the data.

   For further information about the related rights and permissions,
   see the documentation or contact the administrator of the Hadoop cluster to be
   used.

   Note if you need to read data from a local file system other than the HDFS
   system, ensure that the data to be read is stored in the local file system
   of the machine in which the Job is run and then select the Local check box in this Basic settings view. For example, when the connection mode
   to Hive is Standalone, the Job is run in
   the machine where the Hive application is installed and thus the data should
   be stored in that machine.
5. In the Table name field, enter the name
   of the target table you need to load data in. In this scenario, it is
   *employees*.
6. From the Action on file list, select
   APPEND.
7. Select the Set partitions check box and
   in the field that appears, enter the partition you need to add data to. In
   this scenario, this partition is *country='US'*.
