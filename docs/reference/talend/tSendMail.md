<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mail/tsendmail · versión 8.0 -->
# tSendMail

Last updated: 9/30/2026

Notifies recipients about a particular state of a Job or possible
errors.

tSendMail sends
emails and attachments to defined recipients.

## tSendMail Standard properties

These properties are used to configure tSendMail running in the Standard Job framework.

The Standard
tSendMail component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| To | Main recipient email address. |
| From | Sending server email address. |
| Show sender's name | Select this check box if you want the sender name to show in the messages. |
| Cc | Email addresses of secondary recipients of the email message directed to another. |
| Bcc | Email addresses of secondary recipients of the email message. Recipients listed in the Bcc field receive a copy of the message but are not shown on any other recipient's copy. |
| Subject | Heading of the mail. |
| Message | Body message of the email. Press Ctrl+Space to display the list of available variables. |
| Die if the attachment file doesn't exist | This check box is selected by default. Clear this check box if you want the message to be sent even if there are no attachments. |
| Attachments | Specify the file(s) attached and sent along with the email message. Click the [+] button to add as many rows as needed and set the value of the following columns for each row:  * File: Enter the path to the   attached file or the path to the folder if all files   directly under it will be attached. * Content Transfer Encoding:   Click the cell and select a content transfer encoding value   from the list. |
| Other Headers | Click the plus button to add as many lines as needed where you can type the Key and the corresponding Value of any header information that does not belong to the standard header. |
| SMTP Host and Port | IP address of SMTP server used to send emails. |
| SSL Support | Select this check box to authenticate the server at the client side via an SSL protocol. |
| STARTTLS Support | Select this check box to authenticate the server at the client side via a STARTTLS protocol. |
| Importance | Select in the list the priority level of your messages. |
| Authentication mode | Select one of the three authentication modes from the drop-down list.   * No Auth, which requires no authentication. * Basic, which authenticates accesses using username   and password. You need to provide the username and password to send the   mail. To enter the password, click the [...] button   next to the Password field, enter the password in   double quotes in the pop-up dialog box, and click OK   to save the settings. * OAuth2, which authenticates accesses using OAuth   2.0. You need to provide the username and OAuth access token to send the   mail. To enter the OAuth access token, click the   [...] button next to the OAuth Access   Token field, enter the OAuth access token in double quotes in   the pop-up dialog box, and click OK to save the   settings.   Information noteNote: The Authentication mode drop-down list and the Oauth2 item are available only when you have installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| MIME subtype from the 'text' MIME type | Select in the list the structural form for the text of the message. |
| Encoding type | Select the encoding from the list or select Custom and define it manually. |
| Set localhost | Select this option to specify a name for the local host. You can fill a string in the double quotes in the Localhost field as the host name.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use two line authentication for OAuth2 | Select this option to use two-line authentication for OAuth2.  This option is available when you select OAuth2 from the Authentication mode drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Custom properties | Add custom properties and set property values.  To add a custom property key-value pair, add a row in the table by clicking the plus button on the bottom of the table, fill the property name in double quotation marks in the Key column, and fill the property value in the Value column.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is typically used as one subJob but can also be used as output or end object. It can be connected to other components with either Row or Iterate links. |

**Related concepts**  

* [Sending an email on error](tsendmail-tfileinputdelimited-tfileoutputxml-tfileoutputxml-sending-email-on-error-standard-component-this)
* [Sending an email with attachment in HTML format](component-tsendmail-send-email "Through the configuration and properties of the tSendMail component, it is possible to send emails as plain text, HTML, and include attachments as required. Here is an example of using the tSendMail component to send an email with attachment in HTML format.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mail/tsendmail-tfileinputdelimited-tfileoutputxml-tfileoutputxml-sending-email-on-error-standard-component-this -->
# Sending an email on error

Last updated: 9/30/2026

This scenario creates a three-component Job which sends an email to defined recipients
when an error occurs.

* Drop the following components from your Palette to the design workspace: tFileInputDelimited, tFileOutputXML, tSendMail.
* Define tFileInputdelimited properties.
  Related topic: [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited).
* Right-click on the tFileInputDelimited
  component and select *Row > Main*. Then drag it onto the
  tFileOutputXML component and release when
  the plug symbol shows up.
* Define tFileOutputXML properties.
* Drag a Run on Error link from tFileDelimited to tSendMail component.
* Define the tSendMail component
  properties:

* Enter the recipient and sender email addresses, as well as the email
  subject.
* Enter a message containing the error code produced using the corresponding
  global variable. Access the list of variables by pressing Ctrl+Space.
* Add attachments and extra header information if any. Type in the SMTP
  information.

In this scenario, the file containing data to be transferred to XML output cannot be
found. tSendmail runs on this error and sends a
notification email to the defined recipient.

**Related reference**  

* [tSendMail](tsendmail "Notifies recipients about a particular state of a Job or possible errors.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputXML](/talend/en-US/components/8.0/xml-connectors/tfileoutputxml)
