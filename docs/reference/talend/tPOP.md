<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/pop/tpop · versión 8.0 -->
# tPOP

Last updated: 9/30/2026

Fetches one or more email messages from a server using the POP3 or IMAP
protocol.

tPOP uses the POP or IMAP protocol to
connect to a specific email server. Then it fetches one or more email messages and
writes the recovered information in specified files. Parameters in the Advanced
settings view allows you to use filters on your selection.

## tPOP Standard properties

These properties are used to configure tPOP running in the Standard Job framework.

The Standard
tPOP component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Host | IP address of the email server you want to connect to. |
| Port | Port number of the email server. |
| Authentication mode | Select one of the two authentication modes from the drop-down list.   * Basic, which authenticates accesses using   username and password. You need to provide the username and password   to retrieve the mail messages. To enter the password, click the   [...] button next to the   Password field, enter the password in   double quotes in the pop-up dialog box, and click   OK to save the settings. * OAuth2, which authenticates accesses using OAuth   2.0. You need to provide the username and OAuth access token to   retrieve the mail messages. To enter the OAuth access token, click   the [...] button next to the OAuth   Access Token field, enter the OAuth access token in   double quotes in the pop-up dialog box, and click   OK to save the settings.  * Microsoft Exchange, which authenticates   accesses using Microsoft Exchange. You need to provide the username,   tenant ID, application (client) ID, and secret value of a Microsoft   Azure application in the Username,   Directory (tenant) ID,   Application (client) ID, and   Secret Value fields. Note that the   Microsoft Azure application needs to have the POP or IMAP API   permission and the service principal of the application needs to be   registered in Microsoft Exchange. See [Configuring a Microsoft Azure application for POP and IMAP](/talend/en-US/components/8.0/pop/configuring-an-oauth2-application-for-pop-and-imap) and [Registering the service principal of an application in Microsoft Exchange](/talend/en-US/components/8.0/pop/registering-service-principal-in-exchange) for   related information.   Information noteNote:  * The Authentication mode drop-down list and the   Oauth2 item are available only when you have   installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by   Talend. For more information, check with your administrator. * The Microsoft Exchange item is available only   when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update   or a later one delivered by Talend. For more information, check with your administrator. |
| Username and Password | User authentication data for the email server.   * Username: enter the username you use to   access your email box. * Password: enter the password you use to   access your email box.   These two fields are available when you select Basic from the Authentication mode drop-down list. |
| Output directory | Enter the path to the file in which you want to store the email messages you retrieve from the email server, or click the [...] button next to the field to browse to the file. |
| Filename pattern | Define the syntax of the names of the files that will hold each of the email messages retrieved from the email server, or press Ctrl+Space to display the list of predefined patterns. |
| Retrieve all emails? | Select this check box to retrieve all email messages present on the specified server. |
| Number of emails to retrieve | Enter the number of email messages you want to retrieve.  This field is available only when the Retrieve all emails? check box is cleared. |
| Newer email first | Select this check box to retrieve the most recent email messages according to the number specified in the Number of emails to retrieve field, and the email messages will be returned in chronological order.  This check box is available only when the Retrieve all emails? check box, which is selected by default, is cleared. |
| Delete emails from server | Select this check box if you do not want to keep the retrieved email messages on the server.  Information noteNote: For Gmail servers, this option does not work for the pop3 protocol. Select the imap protocol and ensure that the Gmail account is configured to use imap. |
| Choose the protocol | From the list, select the protocol to be used to retrieve the email messages from the server. This protocol is the one used by the email server. If you choose the imap protocol, you will be able to select the folder from which you want to retrieve your emails. |
| Use SSL | Select this check box if your email server uses this protocol for authentication and communication confidentiality.  Information noteNote: This option is obligatory for users of Gmail. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a job level as well as at each component level. |
| Filter | Click the plus button to add as many lines as needed to filter email messages, select one or multiple of the following filter items in the Filter item columns of the lines, and set values for the filter items in the Pattern columns.   * From: email messages are filtered   according to the sender email address. * To: email messages are filtered   according to the recipient email address. * Subject: email messages are filtered   according to the message subject matter. * Before date: email messages are   filtered by the sending or receiving date. All messages before the set   date are retrieved. * After date: email messages are filtered   by the sending or receiving date. All messages after the set date are   retrieved.   To set a value for the filter item, you can enter the value in the Pattern column directly or press Ctrl + Space and select the expression from the list. |
| Use two line authentication for OAuth2 | Select this option to use two-line authentication for OAuth2.  This option is available when you select OAuth2 from the Authentication mode drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Custom properties | Add custom properties and set property values.  To add a custom property key-value pair, add a row in the table by clicking the plus button on the bottom of the table, fill the property name in double quotation marks in the Key column, and fill the property value in the Value column.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Filter condition relation | Select the type of logical relation you want to use to combine the specified filters:  and: the conditions set by the filters are combined together, the research is more restrictive.  or: the conditions set by the filters are independent, the research is large. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_EMAIL: the number of emails received. This is an After variable and it returns an integer.  CURRENT\_FILE: the current file name. This is a Flow variable and it returns a string.  CURRENT\_FILEPATH: the current file path. This is a Flow variable and it returns a string.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component does not handle data flow, it can be used alone. |
| Limitation | When the Use SSL check box or the imap protocol is selected, tPOP cannot work with IBM Java 6. |

**Related concepts**  

* [Retrieving a selection of email messages from an email server](tpop-retrieving-selection-of-email-messages-from-email-server-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/pop/tpop-retrieving-selection-of-email-messages-from-email-server-standard-component-this -->
# Retrieving a selection of email messages from an email server

Last updated: 9/30/2026

This scenario is a one-component Job that retrieves a predefined number of email
messages from an email server.

* Drop the tPOP component from the Palette to the design workspace.
* Double-click tPOP to display the Basic settings view and define the component
  properties.
* Enter the email server IP address and port number in the corresponding
  fields.
* Enter the username and password for your email account in the corresponding
  fields. In this example, the email server is called *Free*.

* In the Output directory field, enter the
  path to the output directory manually, or click the [...] button next to the
  field and browse to the output directory where the email messages retrieved from
  the email server are to be stored.
* In the Filename pattern field, define the
  syntax you want to use to name the output files that will hold the messages
  retrieved from the email server, or press Ctrl+Space to display a list of predefined patterns. The syntax
  used in this example is the following:
  TalendDate.getDate("yyyyMMdd-hhmmss") + "\_" + (counter\_tPOP\_1 + 1) +
  ".txt".

  The output files will be stored as .txt files and are defined by date, time
  and arrival chronological order.
* Clear the Retrieve all emails? field and in
  the Number of emails to retrieve field, enter
  the number of email messages you want to retrieve, 10 in this example.
* Select the Delete emails from server check
  box to delete the email messages from the email server once they are retrieved
  and stored locally.
* In the Choose the protocol field, select the
  protocol type you want to use. This depends on the protocol used by the email
  server. Certain email suppliers, like *Gmail*, use both
  protocols. In this example, the protocol used is *pop3*.
* Save your Job and press F6 to execute
  it.

The tPOP component retrieves the 10 recent messages
from the specified email server.

In the *tPOP* directory stored locally, a .txt file is created for
each retrieved message. Each file holds the metadata of the email message headings
(sender's address, recipient's address, subject matter) in addition to the message
content.

**Related reference**  

* [tPOP](tpop "Fetches one or more email messages from a server using the POP3 or IMAP protocol.")
