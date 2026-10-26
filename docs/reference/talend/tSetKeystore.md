<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/keystore/tsetkeystore · versión 8.0 -->
# tSetKeystore

Last updated: 9/30/2026

Sets the authentication data type between PKCS
12 and JKS.

tSetKeystore submits authentication data of a truststore with or without
keystore to validation for the SSL connection.

### In this section

* [tSetKeystore Standard properties](/talend/en-US/components/8.0/keystore/tsetkeystore-standard-properties)
* [tSetKeystore properties for Apache Spark Batch](/talend/en-US/components/8.0/keystore/tsetkeystore-properties-for-apache-spark-batch)
* [tSetKeystore properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/keystore/tsetkeystore-properties-for-apache-spark-streaming)

**Related concepts**  

* [Extracting customer information from a private WSDL file](tsetkeystore-twebservice-tlogrow-tlogrow-extracting-customer-information-from-private-wsdl-file-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/keystore/tsetkeystore-properties-for-apache-spark-batch -->
# tSetKeystore properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tSetKeystore running in the Spark Batch Job framework.

The Spark Batch
tSetKeystore component belongs to the Authentication family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| TrustStore type | Select the type of the TrustStore to be used. It may be PKCS 12 or JKS. |
| TrustStore file | Type in the path, or browse to the certificate TrustStore file (including filename) that contains the list of certificates that the client trusts. |
| TrustStore password | Type in the password used to check the integrity of the TrustStore data. |
| Need Client authentication | Select this check box to validate the keystore data. Once doing so, you need complete three fields:  - KeyStore type: select the type of the keystore to be used. It may be PKCS 12 or JKS.  - KeyStore file: type in the path, or browse to the file (including filename) containing the keystore data.  - KeyStore password: type in the password for this keystore. |
| Check server identity | Select this checkbox to make the Job verify the match between the hostname of the URL and the hostname of the server. If they mismatch, the verification mechanism asks whether this connection should be allowed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/keystore/tsetkeystore-standard-properties -->
# tSetKeystore Standard properties

Last updated: 9/30/2026

These properties are used to configure tSetKeystore running in the Standard Job framework.

The Standard
tSetKeystore component belongs to the Internet family.

Information noteNote: This component is designed for Data Integration Jobs. It is not supported in ESB use
cases.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Set TrustStore | Select this option to set the truststore. Information noteNote: This option is available only when you have installed the 8.0.1-R2023-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Set KeyStore | Select this option to set the keystore. Information noteNote: This option is available only when you have installed the 8.0.1-R2023-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Both | Select this option to set both the truststore and keystore. Information noteNote: This option is available only when you have installed the 8.0.1-R2023-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| TrustStore type | Select the type of the truststore to be used: PKCS 12 or JKS.  This option is available when you select the Set TrustStore option or the Both option. |
| TrustStore file | Type in the path, or browse to the certificate truststore file (including filename) that contains the list of certificates that the client trusts.  This option is available when you select the Set TrustStore option or the Both option. |
| TrustStore password | Type in the password used to check the integrity of the truststore data.  This option is available when you select the Set TrustStore option or the Both option. |
| KeyStore type | Select the type of the keystore to be used: PKCS 12 or JKS. This option is available when you select the Set KeyStore option or Both option. |
| KeyStore file | Select the type of the keystore to be used: PKCS 12 or JKS. This option is available when you select the Set KeyStore option or Both option. |
| KeyStore password | Type in the password for this keystore. This option is available when you select the Set KeyStore option or Both option. |
| Check server identity | Select this checkbox to make the Job verify the match between the hostname of the URL and the hostname of the server. If they mismatch, the verification mechanism asks whether this connection should be allowed. |
| Use SSLContext | Select this option to have the component constructing the SSLContext and setting the default SSLContext for the current JVM. With this option selected, the component operates in the following way to construct the SSLContext.  1. Loading the default JRE truststore by loading the    {java-home}/lib/security/jssecacerts file. If the    file does not exist, the file    {java-home}/lib/security/cacerts will be    loaded. 2. Loading the operating system truststore. 3. Loading the truststore/keystore specified in the component.  The SSLContext constructed will be used by the subsequent components or third-party libraries that support SSLContext. The following lists the third-party libraries that support the default Java SSLContext.  * javax.net.ssl.HttpsURLConnection * apache httpclient 4 * apache httpclient 5 * cxf httpclient * jetty httpclient  In Talend Studio, the components that support SSLContext include (but not limited to) tHTTPClient, tHttpRequest. Information noteNote: This option is available only when you have installed the 8.0.1-R2023-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used standalone. |
| Connections | Outgoing links (from this component to another):  Trigger: Run if; On Subjob Ok, On Subjob Error, On Component Ok; On Component Error.    Incoming links (from one component to this one):  Trigger: Run if, On Subjob Ok, On Component Ok, On Component Error.    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Limitation | n/a. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/keystore/tsetkeystore-twebservice-tlogrow-tlogrow-extracting-customer-information-from-private-wsdl-file-standard-component-this -->
# Extracting customer information from a private WSDL file

Last updated: 9/30/2026

This scenario describes a three-component Job that connects to a private WSDL file in
order to extract customer information.

The WSDL file used in this Job accesses the corresponding web service under the SSL
protocol. For this purpose, the most relative code in this file reads as follows
:

```
<wsdl:port name="CustomerServiceHttpSoap11Endpoint"
binding="ns:CustomerServiceSoap11Binding">
            <soap:address location="https://192.168.0.22:8443/axis2/services/CustomerService.CustomerServiceHttpSoap11Endpoint/"/>
        </wsdl:port>
```

Accordingly, we enter the following code in the *server.xml* file
of Tomcat:

```
<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"
               maxThreads="150" scheme="https" secure="true"
               clientAuth="true" sslProtocol="TLS" 
     keystoreFile="D:/server.keystore" keystorePass="password"
     keystoreType="JKS"
     truststoreFile="D:/server.p12" truststorePass="password"
     truststoreType="PKCS12"
    />
```

So we need keystore files to connect to this WSDL file. To replicate this Job, proceed
as follows:

* Drop the following components from the Palette onto the design workspace: tSetKeystore, tWebService, and
  tLogRow.

* Right-click tSetKeystore to open its
  contextual menu.
* In this menu, select Trigger > On Subjob Ok to connect this component to tWebService.
* Right-click tWebService to open its
  contextual menu.
* In this menu, select Row > Main to connect this component to tLogRow.
* Double-click tSetKeystore to open its
  Basic settings view and define the
  component properties.

* In the TrustStore type field, select
  PKCS12 from the drop-down list.
* In the TrustStore file field, browse to the
  corresponding truststore file. Here, it is
  *server.p12*.
* In the TrustStore password field, type in the
  password for this truststore file. In this example, it is
  *password*.
* Select the Need Client authentication check
  box to activate the keystore configuration fields.
* In the KeyStore type field, select JKS from the drop-down list.
* In the KeyStore file field, browse to the
  corresponding keystore file. Here, it is
  *server.keystore.*
* Double-click tWebService to open the
  component editor, or select the component in the design workspace and in the
  Basic settings view, click the [...]
  button next to Service configuration.

* In the WSDL field, browse to the private WSDL
  file to be used. In this example, it is
  *CustomerService.wsdl*.
* Click the refresh button next to the WSDL
  field to retrieve the WSDL description and display it in the fields that
  follow.
* In the Port Name list, select the port you
  want to use, *CustomerServiceHttpSoap11Endpoint* in this
  example.
* In the Operation list, select the service you
  want to use. In this example the selected service is
  *getCustomer(parameters):Customer*.
* Click Next to open a new view in the
  editor.

In the panel to the right of the Input mapping view,
the input parameter of the service displays automatically. However, you can add other
parameters if you select [+] parameters and then click
the plus button on top to display the Parameter Tree
dialog box where you can select any of the listed parameters.

The Web service in this example has only one input parameter, ID.

* In the Expression column of the
  *parameters.ID* row, type in the customer ID of your
  interest between quotation marks. In this example, it is
  *A00001*.
* Click Next to open a new view in the
  editor.

In the Element list to the left of the view, the
output parameter of the web service displays automatically. However, you can add other
parameters if you select [+] parameters and then click
the plus button on top to display the Parameter Tree
dialog box where you can select any of the parameters listed.

The Web service in this example has four output parameter:
*return.address*, *return.email*,
*return.name* and *return.phone*.

You now need to create a connection between the output parameter of the defined Web
service and the schema of the output component. To do so:

* In the panel to the right of the view, click the [...] button next to
  Edit Schema to open a dialog box in which
  you can define the output schema.

* In the schema editing dialog box, click the plus button to add four columns to
  the output schema.
* Click in each column and type in the new names, *Name*,
  *Phone*, *Email* and
  *Address* in this example. This will retrieve the
  customer information of your interest.
* Click OK to validate your changes and to
  close the schema editing dialog box.
* In the Element list to the right of the
  editor, drag each parameter to the field that corresponds to the column you have
  defined in the schema editing dialog box.

Information noteNote:

If available, use the Auto map! button, located
at the bottom left of the interface, to carry out the mapping operation
automatically.

* Click OK to validate your changes and to
  close the editor.
* In the design workspace, double-click tLogRow
  to open its Basic settings view and define its
  properties.
* Click Sync columns to retrieve the schema
  from the preceding component.
* Save your Job and press F6 to execute
  it.

The information of the customer with ID *A00001* is returned and
displayed in the console of *Talend Studio*.

**Related concepts**  

* [tSetKeystore](tsetkeystore "Sets the authentication data type between PKCS 12 and JKS.")

**Related information**  

* [tWebService](/talend/en-US/components/8.0/webservice/twebservice)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
