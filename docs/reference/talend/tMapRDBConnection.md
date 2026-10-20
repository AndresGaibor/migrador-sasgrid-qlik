<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprdbconnection · versión 8.0 -->
# tMapRDBConnection

Last updated: 9/30/2026

Establishes a MapRDB connection to be reused by other MapRDB components in a same
Job.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMapRDBConnection Standard properties

These properties are used to configure tMapRDBConnection running in the Standard Job framework.

The Standard
tMapRDBConnection component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored.  The properties are stored centrally under the Hadoop Cluster node of the Repository tree. |
| Hadoop version of the distribution | This list is displayed only when you have selected Custom from the distribution list to connect to a cluster not yet officially supported by Talend Studio. In this situation, you need to select the Hadoop version of this custom cluster, that is to say, Hadoop 1 or Hadoop 2. |
| Zookeeper quorum | Type in the name or the URL of the ZooKeeper service you use to coordinate the transaction between your Talend Studio and your database. Note that when you configure the ZooKeeper, you might need to explicitly set the *zookeeper.znode.parent* property to define the path to the root Znode that contains all the Znodes created and used by your database; then select the Set Zookeeper znode parent check box to define this property. |
| Zookeeper client port | Type in the number of the client listening port of the ZooKeeper service you are using. |
| Inspect the classpath for configurations | Select this check box to allow the component to check the configuration files in the directory you have set with the *$HADOOP\_CONF\_DIR* variable and directly read parameters from these files in this directory. This feature allows you to easily change the Hadoop configuration for the component to switch between different environments, for example, from a test environment to a production environment.  In this situation, the fields or options used to configure Hadoop connection and/or Kerberos security are hidden.  If you want to use certain parameters such as the Kerberos parameters but these parameters are not included in these Hadoop configuration files, you need to create a file called *talend-site.xml* and put this file into the same directory defined with *$HADOOP\_CONF\_DIR*. This *talend-site.xml* file should read as follows:  ``` <!-- Put site-specific property overrides in this file. -->  <configuration>      <property>          <name>talend.kerberos.authentication </name>          <value>kinit </value>          <description> Set the Kerberos authentication method to use. Valid values are: kinit or keytab.  </description>      </property>      <property>          <name>talend.kerberos.keytab.principal </name>         <value>user@BIGDATA.COM </value>         <description> Set the keytab's principal name.  </description>     </property>      <property>            <name>talend.kerberos.keytab.path </name>          <value>/kdc/user.keytab </value>          <description> Set the keytab's path.  </description>      </property>      <property>          <name>talend.encryption </name>          <value>none </value>          <description> Set the encryption method to use. Valid values are: none or ssl.  </description>      </property>      <property>          <name>talend.ssl.trustStore.path </name>          <value>ssl </value>          <description> Set SSL trust store path.  </description>      </property>      <property>          <name>talend.ssl.trustStore.password </name>          <value>ssl </value>          <description> Set SSL trust store password.  </description>      </property>  </configuration> ```  The parameters read from these configuration files override the default ones used by Talend Studio. When a parameter does not exist in these configuration files, the default one is used. |
| Use kerberos authentication | If the database to be used is running with Kerberos security, select this checkbox, then, enter the principal names in the HBase Master principal and HBase Region Server principal fields. You should be able to find the information in the *hbase-site.xml* file of the cluster to be used.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used.  For further information about how Kerberos can be configured for your database in a MapR cluster, see [Configuring Kerberos Authentication](http://doc.mapr.com/display/MapR/Configure+Kerberos+Authentication+for+the+HBase+REST+Gateway). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Properties | If you need to use custom configuration for your database, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those corresponding ones defined earlier for your database.  For example, you need to define the value of the *dfs.replication* property as *1* for the database configuration. Then you need to add one row to this table using the plus button and type in the name and the value of this property in this row. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other MapRDB components, particularly tMapRDBClose. |
| Prerequisites | Before starting, ensure that you have met the Loopback IP prerequisites expected by your database.  The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
