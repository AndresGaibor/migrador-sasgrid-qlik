<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tsqoopexport · versión 8.0 -->
# tSqoopExport (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Information noteDeprecation: This component is deprecated since the
7.3.1-R2021-06 release.

Defines the arguments required by Sqoop for transferring data to a
RDBMS.

tSqoopExport calls sqoop to transfer data from the Hadoop Distributed
File System (HDFS) to a relational database management system (RDBMS).

Please be aware that some features provided by this component are only
supported by the latest Sqoop version. For further information about the availability of
each feature, see Apache's documentation about Sqoop.

Information noteNote:

Sqoop is typically installed in every Hadoop distribution. But if the Hadoop
distribution you need to use have no Sqoop installed, you have to install one on your
own and ensure to add the Sqoop command line to the PATH variable of that distribution.
For further information about how to install Sqoop, see the documentation of Sqoop.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSqoopExport Standard properties

These properties are used to configure tSqoopExport running in the Standard Job framework.

The Standard
tSqoopExport component belongs to the Big Data and the File families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Mode | Select the mode in which Sqoop is called in a Job execution.  Use Commandline: the Sqoop shell is used to call Sqoop. You can read data from either HDFS or HCatalog. In this mode, you have to deploy and run the Job in the host where Sqoop is installed. Therefore, if you are a subscription-based user, we recommend installing and using a Talend JobServer provided by Talend in that host to run the Job; if you are using one of the Talend solutions with Big Data, you have to ensure that Talend Studio and the Sqoop to be used are in the same machine.  Use Java API: the Java API is used to call Sqoop. In this mode, the Job can be run locally in Talend Studio but you need to configure the connection to the Hadoop distribution to be used. Note that JDK is required to execute the Job in the Java API mode and the versions of the JDK kits installed in both machines must be compatible with each other; for example, the versions are the same or the JDK version of the Hadoop machine is more recent. |
| Hadoop properties | Either Built-in or Repository:  * Built-in: you enter the configuration   information of the Hadoop distribution to be used locally for this component   only. * Repository: you have already created the   Hadoop connection and stored it in the Repository; therefore, you reuse it directly for the component   configuration and the Job design. For further information about how to create a   centralized Hadoop connection, see [Centralizing Hadoop connection   metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-hadoop-connection). |
| Distribution | Select the cluster you are using from the drop-down list. The options in the list vary depending on the component you are using. Among these options, the following ones requires specific configuration:  * If available in this Distribution drop-down list, the Microsoft HD Insight option allows you to   use a Microsoft HD Insight cluster. For this purpose, you need to configure   the connections to the HD Insight cluster and the Windows Azure Storage   service of that cluster in the areas that are displayed. For detailed   explanation about these parameters, see [Configuring the connection   manually](/talend/r/en-US/7.3/studio-user-guide/configuring-connection-manually). * If you select Amazon EMR,   find more details in [Amazon EMR - Getting Started](/talend/r/en-US/8.0/amazon-emr-getting-started). * The Custom option   allows you to connect to a cluster different from any of the distributions   given in this list, that is to say, to connect to a cluster not officially   supported by    Talend   .   1. Select Import from existing    version to import an officially supported distribution as base    and then add other required jar files which the base distribution does not    provide. 2. Select Import from zip to    import the configuration zip for the custom distribution to be used. This zip    file should contain the libraries of the different Hadoop elements and the index    file of these libraries.  Note that custom versions are not officially supported by    Talend    .     Talend     and its community provide you with the opportunity to connect to    custom versions from Talend Studio but cannot guarantee that the configuration of whichever version you choose    will be easy, due to the wide range of different Hadoop distributions and    versions that are available. As such, you should only attempt to set up such a    connection if you have sufficient Hadoop experience to handle any issues on your    own.  Information noteNote: In this dialog box, the active check box must be kept    selected so as to import the jar files pertinent to the connection to be    created between the custom distribution and this component.  For a step-by-step example about how to connect to a custom    distribution and share this connection, see [Hortonworks](/talend/r/en-US/8.0/hortonworks). |
| Hadoop Version | Select the HBase version of the distribution you are using. |
| NameNode URI | Type in the URI of the Hadoop NameNode, the master node of a Hadoop system. For example, we assume that you have chosen a machine called *masternode* as the NameNode, then the location is `hdfs://masternode:portnumber`. If you are using WebHDFS, the location should be webhdfs://masternode:portnumber; WebHDFS with SSL is not supported yet. |
| JobTracker Host | Select this check box and in the displayed field, enter the location of the ResourceManager of your distribution. For example, `tal-qa114.talend.lan:8050`.  This property is required when the query you want to use is executed in Windows and it is a Select query. For example, SELECT your\_column\_name FROM your\_table\_name  Then you can continue to set the following parameters depending on the configuration of the Hadoop cluster to be used (if you leave the check box of a parameter clear, then at runtime, the configuration about this parameter in the Hadoop cluster to be used will be ignored ):  1. Select the Set resourcemanager    scheduler address check box and enter the Scheduler address in    the field that appears. 2. Select the Set jobhistory    address check box and enter the location of the JobHistory    server of the Hadoop cluster to be used. This allows the metrics information of    the current Job to be stored in that JobHistory server. 3. Select the Set staging    directory check box and enter this directory defined in your    Hadoop cluster for temporary files created by running programs. Typically, this    directory can be found under the *yarn.app.mapreduce.am.staging-dir* property in the configuration files    such as *yarn-site.xml* or *mapred-site.xml* of your distribution. 4. Allocate proper memory volumes to the Map and the Reduce    computations and the ApplicationMaster    of YARN by selecting the Set memory    check box in the Advanced settings    view. 5. Select the Set Hadoop    user check box and enter the user name under which you    want to execute the Job. Since a file or a directory in Hadoop has its    specific owner with appropriate read or write rights, this field allows    you to execute the Job directly under the user name that has the    appropriate rights to access the file or directory to be processed. 6. Select the Use datanode hostname check box to allow the    Job to access datanodes via their hostnames. This actually sets the *dfs.client.use.datanode.hostname*    property to *true*. When connecting to a    S3N filesystem, you must select this check box.  For further information about these parameters, see the documentation or contact the administrator of the Hadoop cluster to be used.  For further information about the Hadoop Map/Reduce framework, see the Map/Reduce tutorial in [Apache's Hadoop documentation](http://hadoop.apache.org). |
| Use kerberos authentication | If you are accessing the Hadoop cluster running with Kerberos security, select this checkbox, then, enter the Kerberos principal name for the NameNode in the field displayed. This enables you to use your username to authenticate against the credentials stored in Kerberos.  In addition, since this component performs Map/Reduce computations, you also need to authenticate the related services such as the Job history server and the Resource manager or JobTracker depending on your distribution in the corresponding field. These principals can be found in the configuration files of your distribution. For example, in a CDH4 distribution, the Resource manager principal is set in the *yarn-site.xml* file and the Job history principal in the *mapred-site.xml* file.  This check box is available depending on the Hadoop distribution you are connecting to. |
| Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| Hadoop user name | Enter the user name under which you want to execute the Job. Since a file or a directory in Hadoop has its specific owner with appropriate read or write rights, this field allows you to execute the Job directly under the user name that has the appropriate rights to access the file or directory to be processed. Note that this field is available depending on the distribution you are using. |
| JDBC property | Either Built-in or Repository:  * Built-in: you enter the connection   information of the database to be used locally for this component only. * Repository: you have already created the   database connection and stored it in the Repository; therefore, you reuse it directly for the component   configuration and the Job design.  Note that only the General   JDBC connection stored in the Repository is supported. |
| Connection | Type in the JDBC URL used to connect to the target database. |
| User name and Password | Type in the authentication information to the target database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  If your password is stored in a file, select the The password is stored in a file check box and enter the path to that file in the File path field that is displayed.  * This file can be stored either in the machine   where the Job is to be executed or in the HDFS system of the Hadoop cluster to be   used. * The password stored in this file must not   contain \n (the newline escape) at the end, that is to say, you must not insert a   new line at the end of the password even though this line is empty.  Note that this feature is available for the Sqoop version 1.4.4 or later. |
| Driver JAR | In either the Use Commandline mode or the Java API mode, you must add the driver file of the database to be used to the *lib* folder of the Hadoop distribution you are using. For that purpose, use this Driver JAR table to add that driver file for the current Job you are designing. |
| Driver class name | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| Table Name | Type in the name of the target table to which data is transferred from HDFS or HCatalog. This table must already exist in the target database. The input files are read and parsed into a set of records according to the user-specified delimiters. |
| Input source | Select the type of the source system from which data is read. This system could be:  * HDFS: the source system is HDFS. In the   Export dir field that is displayed, enter the path   to the source data to be transferred in HDFS. * HCatalog: the source system is HCatalog. In the   HCatalog database and the HCatalog   table fields that are displayed, enter the database name and   the table name to be used, respectively, |
| Direct | Select this check box to use the export fast path. |
| Specify Number of Mappers | Select this check box to indicate the number of map tasks (parallel processes) used to perform the data transfer.  If you do not want Sqoop to work in parallel, enter *1* in the displayed field. |
| Call a stored procedure | Select this check box to enable the component to call a specific store procedure to write data into the target database.  You need to enter the name of the stored procedure to be used in the field that is displayed.  Syntax and capabilities of stored procedures vary among different databases; for this reason, you are recommended to consult the documentation of the database you want to use for details about how a given stored procedure could be called. |
| Use batch mode | Select this check box to execute the statements in batch mode instead of running a multi-row INSERT statement to write multiple records in the target database. |
| Clear staging table | If you are using a specific staging table for the desired data transfer, select this check box to ensure that the staging table is empty when the data transfer runs. |
| Define a staging table | Select this check box to create a staging table for the data to be transferred. The transferred data is staged within this table before being written into the target table so as to avoid only a part of the data being committed to the target table when the transfer fails.  For further information about whether a staging table is supported for a given data transfer, see Apache's documentation for Sqoop. |
| Specify how updates are performed when new rows are found with non-match keys in database | Select this check box to determine the action to be taken when a given update key does not have any matching records in the target table. You can then select either of the following options:  * Update only: this updates only   the records that already exist in the target table. * Allow insert: this works like   the SQL UPSERT statement. It writes new records in the table if they   do not exist there. |
| Use column for update | Select this check box and in the table that is displayed, add the columns to be used as the update key. |
| Print Log | Select this check box to activate the Verbose check box. |
| Verbose | Select this check box to print more information while working, for example, the debugging information. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use MySQL default delimiters | Select this check box to use MySQL's default delimiter set. This check box is available only to the Talend CommandLine mode. |
| Define Java mapping | Sqoop provides default configuration that maps most SQL types to appropriate Java types. If you need to use your custom map to overwrite the default ones at runtime, select this check box and define the map(s) you want to use in the table that appears. |
| Additional arguments | Complete this table to use additional arguments if needs be.  By adding additional arguments, you are able to perform multiple operations in one single transaction. For example, you can use --hive-import and --hive-table in the Talend CommandLine mode or hive.import and hive.table.name in the Java API mode to create Hive table and write data in at the runtime of the transaction writing data in HDFS. For further information about the available Sqoop arguments in the Talend CommandLine mode and the Java API mode, respectively, see [Additional arguments](/talend/en-US/components/8.0/sqoop/tsqoopexport-tsqoopexport-additional-arguments-standard-component-bigdata).  With the Talend CommandLine mode, you can use generic arguments by completing this table in a proper format (for example, -D org.apache.sqoop.splitter.allow\_text\_splitter). Information noteNote: You should not use tool specific arguments with one hyphen in the beginning (for example, -m or -e), use full name argument instead (for example, --num-mappers or --query).  With the Java API mode, you can use generic arguments by using Hadoop Properties and entering values in a proper format (for example, org.apache.sqoop.splitter.allow\_text\_splitter). Information noteNote: Note that some arguments might not be supported in Java API mode due to API limitations.  For more information about generic and specific arguments, see [Using Generic and Specific Arguments](https://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html#_using_generic_and_specific_arguments) in the official Sqoop documentation. |
| Use speed parallel data transfers | Select this check box to enable quick parallel data transfers between the Teradata database and the Hortonworks Hadoop distribution. Then the Specific params table and the Use additional params check box appear to allow you to specify the Teradata parameters required by parallel transfers.  * In the Specific params   table, two columns are available:   + Argument: select the     parameters as needed from the drop-down list. They are the most common     parameters for the parallel transfer.   + Value: type in the value     of the parameters. * By selecting the Additional   params check box, you make the Specific additional params field displayed. In this field, you can   enter the Teradata parameters that you need to use but are not provided in the   Specific params table. The syntax for   a parameter is -Dparameter=value and when you   put more than one parameter in this field, separate them using whitespace.  You must ensure that the Hortonworks Connector for Teradata has been installed in your Hortonworks cluster. The latest connector can be downloaded from the website of Hortonworks and installed by following the explanations from <http://hortonworks.com/wp-content/uploads/2014/02/bk_HortonworksConnectorForTeradata.pdf>. In the same document, you can as well find the detailed explanations about each parameter that is available for the parallel transfer purpose.  Available in the Use Commandline mode only. |
| Hadoop properties | *Talend Studio* uses a default configuration for its engine to perform operations in a Hadoop distribution. If you need to use a custom configuration in a specific situation, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those default ones.  * Note that if you are using the centrally stored metadata from the Repository, this table automatically inherits the   properties defined in that metadata and becomes uneditable unless you change the   Property type from Repository to Built-in.  For further information about the properties required by Hadoop and its related systems such as HDFS and Hive, see the documentation of the Hadoop distribution you are using or see [Apache's Hadoop documentation](http://hadoop.apache.org/docs) and then select the version of the documentation you want. For demonstration purposes, the links to some properties are listed below:  * Typically, the HDFS-related properties can be found in the *hdfs-default.xml* file of your distribution, such as <http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml>. * Apache also provides a page to list the [Hive-related properties](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties). |
| Mapred job map memory mb and Mapred job reduce memory mb | You can tune the map and reduce computations by selecting the Set memory check box to set proper memory allocations for the computations to be performed by the Hadoop system.  In that situation, you need to enter the values you need in the Mapred job map memory mb and the Mapred job reduce memory mb fields, respectively. By default, the values are both *1024* which are normally appropriate for running the computations.  The memory parameters to be set are Map (in Mb), Reduce (in Mb) and ApplicationMaster (in Mb). These fields allow you to dynamically allocate memory to the map and the reduce computations and the ApplicationMaster of YARN. |
| Path separator in server | Leave the default value of the Path separator in server as it is, unless you have changed the separator used by your Hadoop distribution's host machine for its PATH variable or in other words, that separator is not a colon (:). In that situation, you must change this value to the one you are using in that host. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  EXIT\_CODE: the exit code of the remote command. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used standalone. It respects the Sqoop prerequisites. You need necessary knowledge about Sqoop to use it.  Talend recommends you to use the Sqoop of version 1.4+ in order to benefit the full functions of these components.  For further information about Sqoop, see the Sqoop manual on: <http://sqoop.apache.org/docs/> |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
| Limitation | If you have selected the Use Commandline mode, you need to use the host where Sqoop is installed to run the Job using this component. |
| Connections | Outgoing links (from this component to another):  Trigger: Run if; On Subjob Ok; On Subjob Error.    Incoming links (from one component to this one):  Row: Iterate;  Trigger: Run if; On Subjob Ok; On Subjob Error; On Component Ok; On Component Error    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sqoop/tsqoopexport-tsqoopexport-additional-arguments-standard-component-bigdata -->
# Additional Sqoop arguments (deprecated)

Last updated: 9/30/2026

Information noteDeprecation: The Sqoop components are deprecated since the
7.3.1-R2021-06 release.

| mode | Java API mode |
| --- | --- |
| --driver | jdbc.driver.class |
| --direct-split-size | import.direct.split.size |
| --inline-lob-limit | import.max.inline.lob.size |
| --split-by | db.split.column |
| --warehouse-dir | hdfs.warehouse.dir |
| --enclosed-by | codegen.output.delimiters.enclose |
| --escaped-by | codegen.output.delimiters.escape |
| --fields-terminated-by | codegen.output.delimiters.field |
| --lines-terminated-by | codegen.output.delimiters.record |
| --optionally-enclosed-by | codegen.output.delimiters.required |
| --input-enclosed-by | codegen.input.delimiters.enclose |
| --input-escaped-by | codegen.input.delimiters.escape |
| --input-fields-terminated-by | codegen.input.delimiters.field |
| --input-lines-terminated-by | codegen.input.delimiters.record |
| --input-optionally-enclosed-by | codegen.input.delimiters.required |
| --hive-home | hive.home |
| --hive-import | hive.import |
| --hive-overwrite | hive.overwrite.table |
| --hive-table | hive.table.name |
| --class-name | codegen.java.classname |
| --jar-file | codegen.jar.file |
| --outdir | codegen.output.dir |
| --package-name | codegen.java.packagename |

For further information about the arguments available in the Sqoop Talend CommandLine mode, see
the documentation of Sqoop.

The arguments listed earlier for the Java API mode are subject to updates and changes
by Java. For further information about these arguments, see <http://svn.apache.org/repos/asf/sqoop/trunk/src/java/org/apache/sqoop/SqoopOptions.java>
