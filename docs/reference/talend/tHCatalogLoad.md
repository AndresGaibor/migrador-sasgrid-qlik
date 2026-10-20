<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/thcatalogload · versión 8.0 -->
# tHCatalogLoad (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Information noteDeprecation: This component is deprecated since the
8.0.1-R2024-08 release.

Reads data directly from HDFS and writes this data into an established HCatalog
managed table.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHCatalogLoad Standard properties

These properties are used to configure tHCatalogLoad running in the Standard Job framework.

The Standard
tHCatalogLoad component belongs to the Big Data family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository  Built-in: No property data stored centrally.  Repository: Select the repository file in which the properties are stored. The fields that follow are completed automatically using the data retrieved. |
| Distribution | Select the cluster you are using from the drop-down list. The options in the list vary depending on the component you are using. Among these options, the following ones requires specific configuration:  * If available in this Distribution drop-down list, the Microsoft HD Insight option allows you to   use a Microsoft HD Insight cluster. For this purpose, you need to configure   the connections to the HD Insight cluster and the Windows Azure Storage   service of that cluster in the areas that are displayed. For detailed   explanation about these parameters, see [Configuring the connection   manually](/talend/r/en-US/7.3/studio-user-guide/configuring-connection-manually). * If you select Amazon EMR,   find more details in [Amazon EMR - Getting Started](/talend/r/en-US/8.0/amazon-emr-getting-started). * The Custom option   allows you to connect to a cluster different from any of the distributions   given in this list, that is to say, to connect to a cluster not officially   supported by    Talend   .   1. Select Import from existing    version to import an officially supported distribution as base    and then add other required jar files which the base distribution does not    provide. 2. Select Import from zip to    import the configuration zip for the custom distribution to be used. This zip    file should contain the libraries of the different Hadoop elements and the index    file of these libraries.  Note that custom versions are not officially supported by    Talend    .     Talend     and its community provide you with the opportunity to connect to    custom versions from Talend Studio but cannot guarantee that the configuration of whichever version you choose    will be easy, due to the wide range of different Hadoop distributions and    versions that are available. As such, you should only attempt to set up such a    connection if you have sufficient Hadoop experience to handle any issues on your    own.  Information noteNote: In this dialog box, the active check box must be kept    selected so as to import the jar files pertinent to the connection to be    created between the custom distribution and this component.  For a step-by-step example about how to connect to a custom    distribution and share this connection, see [Hortonworks](/talend/r/en-US/8.0/hortonworks). |
| HCatalog version | Select the HBase version of the distribution you are using. |
| Templeton hostname | Fill this field with the URL of Templeton Webservice.  Information noteNote: Templeton is a webservice API for HCatalog. It has been renamed to WebHCat by the Apache community. This service facilitates the access to HCatalog and the related Hadoop elements such as Pig. For further information about Templeton (WebHCat), see <https://cwiki.apache.org/confluence/display/Hive/WebHCat+UsingWebHCat>. |
| Templeton port | Fill this field with the port of URL of Templeton Webservice. By default, this value is *50111*.  Information noteNote: Templeton is a webservice API for HCatalog. It has been renamed to WebHCat by the Apache community. This service facilitates the access to HCatalog and the related Hadoop elements such as Pig. For further information about Templeton (WebHCat), see <https://cwiki.apache.org/confluence/display/Hive/WebHCat+UsingWebHCat>. |
| Use kerberos authentication | If you are accessing the Hadoop cluster running with Kerberos security, select this checkbox, then, enter the Kerberos principal name for the NameNode in the field displayed. This enables you to use your username to authenticate against the credentials stored in Kerberos.  This check box is available depending on the Hadoop distribution you are connecting to. |
| Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| Database | Enter the name of the database you need to write data in. This database must already exist. |
| Table | Enter the name of the table you need to write data in. This table must already exist. |
| Partition | Fill this field to specify one or more partitions for the partition operation on the specified table. When you specify multiple partitions, use commas to separate every two partitions and use double quotation marks to quote the partition string.  If you are reading a non-partitioned table, leave this field empty.  Information noteNote: For further information about Partition, see <https://cwiki.apache.org/Hive/>. |
| Username | Fill this field with the username for the DB authentication. |
| File location | Enter the absolute path pointing to the HDFS location from which data is read. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Retrieve the HCatalog logs | Select this check box to retrieve log files generated during HCatalog operations. |
| Standard Output Folder | Fill this field with the path to which log files are stored.  Information noteNote: This field is enabled only when you selected Retrieve the HCatalog logs check box. |
| Error Output Folder | Fill this field with the path to which error log files are stored. Information noteNote: This field is enabled only when you selected Retrieve the HCatalog logs check box. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used in a single-component subJob.  HCatalog is built on top of the Hive metastore to provide read and write interface for Pig and MapReduce, so that the latter systems can use the metadata of Hive to easily read and write data in HDFS.  For further information, see Apache documentation about HCatalog: <https://cwiki.apache.org/confluence/display/Hive/HCatalog>. |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
| Limitation | When Use kerberos authentication is selected, the component cannot work with IBM JVM. |

**Related concepts**  

* [Managing HCatalog tables on Hortonworks Data Platform (deprecated)](thcatalogoperation-thcatalogload-tlogrow-managing-hcatalog-tables-on-hortonworks-data-platform-standard-component-bigdata-this)
