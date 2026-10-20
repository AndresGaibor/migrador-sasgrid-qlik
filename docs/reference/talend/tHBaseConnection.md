<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconnection · versión 8.0 -->
# tHBaseConnection

Last updated: 9/30/2026

Establishes an HBase connection to be reused by other HBase components in your
Job.

tHBaseConnection opens a
connection to an HBase database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tHBaseConnection Standard properties

These properties are used to configure tHBaseConnection running in the Standard Job framework.

The Standard
tHBaseConnection component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository  - Built-in: no property data stored centrally.  - Repository: select the repository file in which the properties are stored. The fields that follow are completed automatically using the data retrieved. |
| HBase version | Select the HBase version of the distribution you are using. |
| Hadoop version | Select the Hadoop version of the distribution you are using. |
| Zookeeper quorum | Type in the name or the URL of the ZooKeeper service you use to coordinate the transaction between your Talend Studio and your database. Note that when you configure the ZooKeeper, you might need to explicitly set the *zookeeper.znode.parent* property to define the path to the root Znode that contains all the Znodes created and used by your database; then select the Set Zookeeper znode parent check box to define this property. |
| Zookeeper client port | Type in the number of the client listening port of the ZooKeeper service you are using. |
| Inspect the classpath for configurations | Select this check box to allow the component to check the configuration files in the directory you have set with the *$HADOOP\_CONF\_DIR* variable and directly read parameters from these files in this directory. This feature allows you to easily change the Hadoop configuration for the component to switch between different environments, for example, from a test environment to a production environment.  In this situation, the fields or options used to configure Hadoop connection and/or Kerberos security are hidden.  If you want to use certain parameters such as the Kerberos parameters but these parameters are not included in these Hadoop configuration files, you need to create a file called *talend-site.xml* and put this file into the same directory defined with *$HADOOP\_CONF\_DIR*. This *talend-site.xml* file should read as follows:  ``` <!-- Put site-specific property overrides in this file. -->  <configuration>      <property>          <name>talend.kerberos.authentication </name>          <value>kinit </value>          <description> Set the Kerberos authentication method to use. Valid values are: kinit or keytab.  </description>      </property>      <property>          <name>talend.kerberos.keytab.principal </name>         <value>user@BIGDATA.COM </value>         <description> Set the keytab's principal name.  </description>     </property>      <property>            <name>talend.kerberos.keytab.path </name>          <value>/kdc/user.keytab </value>          <description> Set the keytab's path.  </description>      </property>      <property>          <name>talend.encryption </name>          <value>none </value>          <description> Set the encryption method to use. Valid values are: none or ssl.  </description>      </property>      <property>          <name>talend.ssl.trustStore.path </name>          <value>ssl </value>          <description> Set SSL trust store path.  </description>      </property>      <property>          <name>talend.ssl.trustStore.password </name>          <value>ssl </value>          <description> Set SSL trust store password.  </description>      </property>  </configuration> ```  The parameters read from these configuration files override the default ones used by Talend Studio. When a parameter does not exist in these configuration files, the default one is used. |
| Use kerberos authentication | If the database to be used is running with Kerberos security, select this checkbox, then, enter the principal names in the HBase Master principal and HBase Region Server principal fields. You should be able to find the information in the *hbase-site.xml* file of the cluster to be used.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Properties | If you need to use custom configuration for your HBase, complete this table with the property or properties to be customized. Then at runtime, the customized property or properties will override those corresponding ones defined earlier for your HBase.  For example, you need to define the value of the *dfs.replication* property as *1* for the HBase configuration. Then you need to add one row to this table using the plus button and type in the name and the value of this property in this row. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other HBase components, particularly tHBaseClose. |
| Prerequisites | Before starting, ensure that you have met the Loopback IP prerequisites expected by your database.  For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |

**Related concepts**  

* [Exchanging customer data with HBase](thbaseconnection-thbaseinput-tfileinputdelimited-exchanging-customer-data-with-hbase-standard-component-bigdata-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-exchanging-customer-data-with-hbase-standard-component-bigdata-in-this -->
# Exchanging customer data with HBase

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

In this scenario, a six-component Job is used to exchange customer data with a given
HBase.

The six components are:

* tHBaseConnection: creates a connection to
  your HBase database.
* tFixedFlowInput: creates the data to be
  written into your HBase. In the real use case, this component could be
  replaced by the other input components like tFileInputDelimited.
* tHBaseOutput: writes the data it receives
  from the preceding component into your HBase.
* tHBaseInput: extracts the columns of
  interest from your HBase.
* tLogRow: presents the execution
  result.
* tHBaseClose: closes the
  transaction.

To replicate this scenario, proceed as the following sections illustrate.

Information noteNote:

Before starting the replication, your Hbase and Zookeeper service should
have been correctly installed and well configured. This scenario explains only how to
use Talend
solution to make data transaction with a given HBase.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-dropping-and-linking-components-standard-component-bigdata-to-do)
* [Configuring the connection](/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-configuring-connection-standard-component-bigdata-to)
* [Configuring the process of writing data into the HBase](/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-configuring-process-of-writing-data-into-hbase-standard-component-bigdata-to-do)
* [Configuring the process of extracting data from the HBase](/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-configuring-process-of-extracting-data-from-hbase-standard-component-bigdata-to-do)
* [Executing the Job](/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-executing-job-standard-component-bigdata-to)

**Related concepts**  

* [tHBaseInput](thbaseinput "Reads data from a given HBase database and extracts columns of selection.")
* [tHBaseOutput](thbaseoutput "Writes columns of data into a given HBase database.")

**Related reference**  

* [tHBaseConnection](thbaseconnection "Establishes an HBase connection to be reused by other HBase components in your Job.")
* [tHBaseClose](thbaseclose "Closes an HBase connection you have established in your Job.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-configuring-connection-standard-component-bigdata-to -->
# Configuring the connection

Last updated: 9/30/2026

## About this task

To configure the connection to your Zookeeper service and thus to the HBase of
interest, proceed as follows:

## Procedure

1. On the Talend Studio
   workspace, double-click the tHBaseConnection
   component to open its Component view.
2. Select Hortonworks Data Platform 1.0 from
   the HBase version list.
3. In the Zookeeper quorum field, type in
   the name or the URL of the Zookeeper service you are using. In this example,
   the name of the service in use is *hbase*.
4. In the Zookeeper client port field, type
   in the number of client listening port. In this example, it is *2181*.
5. If the Zookeeper znode parent location has been defined in the Hadoop
   cluster you are connecting to, you need to select the Set zookeeper znode parent check box and enter the value of
   this property in the field that is displayed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-configuring-process-of-extracting-data-from-hbase-standard-component-bigdata-to-do -->
# Configuring the process of extracting data from the HBase

Last updated: 9/30/2026

## About this task

To do this, perform the following operations:

## Procedure

1. Double-click tHBaseInput to open its
   Component view.
2. Select the Use an existing connection
   check box and then select the connection you have configured earlier. In
   this example, it is *tHBaseConnection\_1*.
3. Click the [...] button next to Edit
   schema to open the schema editor.
4. Click the plus button three times to add three rows and rename them as
   *id*, *name* and *age* respectively
   in the Column column. This means that you
   extract these three columns from the HBase.
5. Select the types for each of the three columns. In this example, Integer for *id*
   and *age*, String for *name*.
6. Click OK to validate these changes and
   accept the propagation prompted by the pop-up dialog box.
7. In the Table name field, type in the
   table from which you extract the columns of interest. In this scenario, the
   table is *customer*.
8. In the Mapping table, the Column column has been already filled
   automatically since the schema was defined, so simply enter the name of
   every family in the Column family column,
   each corresponding to the column it contains.
9. Double-click tHBaseClose to open its
   Component view.
10. In the Component List field, select the
    connection you need to close. In this example, this connection is *tHBaseConnection\_1*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-configuring-process-of-writing-data-into-hbase-standard-component-bigdata-to-do -->
# Configuring the process of writing data into the HBase

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. On the Design workspace, double-click the tFixedFlowInput component to open its Component view.
2. In this view, click the [...] button next to Edit schema to open the schema editor.
3. Click the plus button three times to add three rows and in the Column column, rename the three rows respectively
   as: *id*,*name* and *age*.
4. In the Type column, click each of these
   rows and from the drop-down list, select the data type of every row. In this
   scenario, they are Integer for *id* and *age*,
   String for *name*.
5. Click OK to validate these changes and
   accept the propagation prompted by the pop-up dialog box.
6. In the Mode area, select the Use Inline Content (delimited file) to display
   the fields for editing.
7. In the Content field, type in the
   delimited data to be written into the HBase, separated with the semicolon
   ";". In this example, they are:

   ```
                     1;Albert;23
   2;Alexandre;24
   3;Alfred-Hubert;22
   4;Andre;40
   5;Didier;28
   6;Anthony;35
   7;Artus;32
   8;Catherine;34
   9;Charles;21
   10;Christophe;36
   11;Christian;67
   12;Danniel;54
   13;Elisabeth;58
   14;Emile;32
   15;Gregory;30 
   ```
8. Double-click tHBaseOutput to open its
   Component view.

   Information noteNote: If this component does not have the same schema of the preceding
   component, a warning icon appears. In this case, click the Sync columns button to retrieve the schema
   from the preceding one and once done, the warning icon disappears.
9. Select the Use an existing connection
   check box and then select the connection you have configured earlier. In
   this example, it is *tHBaseConnection\_1*.
10. In the Table name field, type in the name
    of the table to be created in the HBase. In this example, it is *customer*.
11. In the Action on table field, select the
    action of interest from the drop-down list. In this scenario, select
    Drop table if exists and create. This
    way, if a table named customer exists already in the HBase, it will be
    disabled and deleted before creating this current table.
12. Click the Advanced settings tab to open
    the corresponding view.
13. In the Family parameters table, add two
    rows by clicking the plus button, rename them as *family1* and *family2*
    respectively and then leave the other columns empty. These two column
    families will be created in the HBase using the default family performance
    options.

    Information noteNote: The Family parameters table is
    available only when the action you have selected in the Action on table field is to create a table in
    HBase. For further information about this Family
    parameters table, see [tHBaseOutput](/talend/en-US/components/8.0/hbase/thbaseoutput).
14. In the Families table of the Basic settings view, enter the family names in
    the Family name column, each corresponding
    to the column this family contains. In this example, the *id* and the *age* columns belong to *family1* and the *name*
    column to *family2*.

    Information noteNote: These column families should already exist in the HBase to be
    connected to; if not, you need to define them in the Family parameters table of the Advanced settings view for creating them at
    runtime.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-dropping-and-linking-components-standard-component-bigdata-to-do -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. Drop tHBaseConnection, tFixedFlowInput, tHBaseOutput, tHBaseInput, tLogRow and
   tHBaseClose from Palette onto the
   Design workspace.
2. Right-click tHBaseConnection to open its
   contextual menu and select the Trigger >
   On Subjob Ok link from this menu to
   connect this component to tFixedFlowInput.
3. Do the same to create the OnSubjobOk link
   from tFixedFlowInput to tHBaseInput and then to tHBaseClose.
4. Right-click tFixedFlowInput and select
   the Row > Main link to connect this component to tHBaseOutput.
5. Do the same to create the Main link from
   tHBaseInput to tLogRow.

## Results

The components to be used in this scenario are all placed and linked. Then you
need continue to configure them sucessively.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hbase/thbaseconnection-thbaseinput-tfileinputdelimited-executing-job-standard-component-bigdata-to -->
# Executing the Job

Last updated: 9/30/2026

To execute this Job, press F6.

Once done, the Run view is opened automatically,
where you can check the execution result.

These columns of interest are extracted and you can process them according to
your needs.

Login to your HBase database, you can check the *customer* table this Job has created.
