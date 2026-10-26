<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mail/cmail · versión 8.0 -->
# cMail

Last updated: 9/30/2026

Sends or receives mails in a Route.

cMail provides access to Email
via Spring's Mail support and the underlying Java Mail
system.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cMail Standard properties

These properties are used to configure cMail running in the Standard Job framework.

The Standard
cMail component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Protocols | List of protocols for sending or receiving mails. |
| Host | Host name of the mail server. |
| Port | Port number of the mail server. |
| UserName and Password | Login authentication data. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Content Type | The mail content type. |
| The following options are available for sending mails only: |  |
| Subject | Subject of the mail being sent. |
| From | The mail sender. |
| To | The mail receivers. |
| CC | The CC recipients of the mail. Separate multiple email addresses with a comma. |
| BCC | The BCC recipients of the mail. Separate multiple email addresses with a comma. |
| The following options are available for receiving mails only: | Information noteNote: These options are available only if you have installed the R2025-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Subject Filter | The subject text you want to use to filter mails. |
| From Filter | The sender you want to use to filter mails. |
| To Filter | The receiver you want to use to filter mails. |
| Check Interval | The time interval (in milliseconds) to check for new mails. |
| Fetch Size | The number of messages per poll. |
| Unseen only | Select this check box to fetch unread mails only. |
| Delete after processed | Select this check box to delete mails after consumption. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Arguments | Click the [+] button to add lines as needed in the Arguments table. Then, enter the name and value of an argument. See the site <https://camel.apache.org/components/latest/mail-component.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | When used as a start component, cMail is intended to receive mails. Otherwise, it is intended to send mails. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Using cMail to send and receive mails](cmail-cprocessor-cfile-cfile-using-cmail-to-send-and-receive-mails)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mail/cmail-cprocessor-cfile-cfile-using-cmail-to-send-and-receive-mails -->
# Using cMail to send and receive mails

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario includes two routes. The first one sends a mail while the second
receives it.

Now we build a route to send a mail.

As shown above, the mail has been sent out successfully.

Now we build a route to receive the mail.

### In this section

* [Mail sending](/talend/en-US/mediation-components/8.0/mediation-mail/cmail-cprocessor-cfile-cfile-mail-sending)
* [Mail receiving](/talend/en-US/mediation-components/8.0/mediation-mail/cmail-cprocessor-cfile-cfile-mail-receiving)

**Related reference**  

* [cMail](cmail "Sends or receives mails in a Route.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mail/cmail-cprocessor-cfile-cfile-mail-receiving -->
# Mail receiving

Last updated: 9/30/2026

## Procedure

1. Drop the components from the Palette onto the
   workspace: cMail and cProcessor, respectively labeled as Receive\_Mail and Mail\_Body.
2. Link the components using a Row > Route connection.
3. Double-click cMail to open its Basic settings view in the Component tab.
4. In the Protocols list, select *imaps*.
5. In the Host field, type in the host name of
   the imap server, *imap.gmail.com* in this use
   case.
6. In the Port field, type in the port number,
   *993* in this use case.
7. In the UserName and Password fields, enter the login authentication
   credentials, which are in the form of context variables in this example. For more
   information about context variable setup, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).
8. Keep the default setting of the ContentType
   field, *text/plain*.
9. Double-click cProcessor to open its Basic settings view in the Component tab.
10. In the Code box, enter the code below to
    print the mail body.

    ```
    System.out.println(exchange.getIn().getBody(String.class));
    ```
11. Save the route and press F6 to run.

    As shown above, the mail has been received and its content is *test mail body*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mail/cmail-cprocessor-cfile-cfile-mail-sending -->
# Mail sending

Last updated: 9/30/2026

## Procedure

1. Drop the components from the Palette onto the
   workspace: cFile, cMail and cProcessor,
   respectively labeled as Mail\_to\_send,
   Send\_Mail and Mail\_Sent.
2. Link the components using a Row > Route connection.
3. Double-click cFile to open its Basic settings view in the Component tab.
4. Click the [...] button next to the Path field to select the folder that has the file to
   send.
5. In the FileName field, enter the
   name of the file to send, `test mail.txt` in this use case. Keep
   the default setup of other items.

   The content of this file is test mail body.
6. Double-click cMail to open its Basic settings view in the Component tab.
7. In the Protocols list, select *smtps*.

   In the Host field, type in the host name of
   the smtp server, *smtp.gmail.com* in this use
   case.

   In the UserName and Password fields, enter the login authentication
   credentials, which are in the form of context variables in this example. For more
   information about context variable setup, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).

   Keep the default setting of the ContentType
   field, *text/plain*.

   In the To field, enter the receiver of the
   mail, which is also in the form of context variable in this example.
8. Double-click cProcessor to open its Basic settings view in the Component tab.
9. In the Code box, enter the code below to give
   a prompt after the mail is sent.

   ```
   System.out.println("Mail sent");
   ```
10. Save the Route and press F6 to
    run.
