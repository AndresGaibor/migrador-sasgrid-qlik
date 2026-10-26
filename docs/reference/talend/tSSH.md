<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/system/tssh · versión 8.0 -->
# tSSH

Last updated: 9/30/2026

Establishes a communication with distant server and returns securely sensible
information.

Returns data from a remote computer, based on the secure shell
command defined.

## tSSH Standard properties

These properties are used to configure tSSH running in the Standard Job
framework.

The Standard
tSSH component belongs to the System family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-in: You create and store the   schema locally for this component only. For more information about a   component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already created   the schema and stored it in the Repository. You can reuse it in various   projects and Job flowcharts. For more information about a component schema   in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Host | Enter the IP address of the SSH server. |
| Port | Enter the listening port number of the SSH server. |
| User | Enter the username used to authenticate to the SSH server. |
| Authentication method | Select the authentication method to be used: Public key, Password, or Keyboard Interactive.   * Public key: Enter the path to the private   key and the passphrase for the key in the Private   key and Key Passphrase   fields correspondingly. To enter the passphrase, click the   [...] button next to the   Key Passphrase field, enter the   passphrase between double quotes in the pop-up dialog box, and   click OK to save the settings. * Password: Enter the password required. To   enter the password, click the [...] button next to the   Password field, enter the password in   double quotes in the pop-up dialog box, and click OK to save the settings. * Keyboard Interactive: Enter the required   password in the Password field. To enter the   password, click the [...] button next to the   Password field, enter the password in   double quotes in the pop-up dialog box, and click   OK to save the settings. |
| Pseudo terminal | Select this check box to call the interactive shell that performs the terminal operations. |
| Command separator | Type in the command separator required. Once the Pseudo terminal check box is selected, this field becomes unavailable. |
| Commands | Type in the command for the relevant information to be returned from the remote computer. When you select the Pseudo terminal check box, this table becomes a terminal emulator and each row in this table is a single command. |
| Use timeout/timeout in seconds | Define the timeout time period. A timeout message will be generated if the actual response time exceeds this expected processing time. |
| Standard Output | Select the destination to which the standard output is returned. The output may be returned to:  - to console: the output is displayed in the console of the Run view.  - to global variable: the output is indicated by the corresponding global variable.  - both to console and global variable: the output is indicated both of the two means.  - normal: the output is a standard ssh output. |
| Error Output | Select the destination to which the error output is returned. The output may be returned to:  - to console: the output is displayed in the console of the Run view.  - to global variable: the output is indicated by the corresponding global variable.  - both to console and global variable: the output is indicated both of the two means.  - normal: the output is a standard ssh output. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use session heartbeat | Enable this option to send a heartbeat message (specifically, 'SSH\_MSG\_IGNORE') at regular intervals during the SSH session. This helps keep the session active by preventing timeouts. Specify the interval (in seconds) in the **Heartbeat interval** field. The default value is **1800 seconds** (30 minutes). |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  STDOUT: the standard execution output of the remote command. This is an After variable and it returns a string.  STDERR: the error execution output of the remote command. This is an After variable and it returns a string.  EXIT\_CODE: the exit code of the remote command. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as standalone component.  Note that for some sensitive information such as password and username, you can define the context variables in the Context view and press Ctrl + Space to access them.  Information noteNote: The data returned by this component may be large in size. Allocate more memory space if the Job takes extra long time to complete. You can set memory space for a Job in the Advanced settings view of the Run tab. |
| Connections | Outgoing links (from this component to another):  Row: Main  Trigger: Run if; On Component Ok; On Component Error; On Subjob Ok; On Subjob Error.    Incoming links (from one component to this one):  Row: Main; Iterate  Trigger: Run if; On Component Ok; On Component Error; On Subjob Ok; On Subjob Error.    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Limitation | The component use is optimized for Unix-like systems. |

**Related concepts**  

* [Displaying remote system information via SSH](tssh-displaying-remote-system-information-via-ssh-standard-component "The following use case describes a basic Job that uses SSH command to display the hostname of the distant server being connected to, and the current date on this remote system.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/system/tssh-displaying-remote-system-information-via-ssh-standard-component -->
# Displaying remote system information via SSH

Last updated: 9/30/2026

The following use case describes a basic Job that uses SSH command to display the
hostname of the distant server being connected to, and the current date on this remote
system.

The tSSH component is sufficient for this Job. Drop
it from the Palette to the design workspace.

Double-click on the tSSH component and select the
Basic settings view tab.

### In this section

* [Procedure](/talend/en-US/components/8.0/system/tssh-procedure-standard-component-type-in)

**Related reference**  

* [tSSH](tssh "Establishes a communication with distant server and returns securely sensible information.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/system/tssh-procedure-standard-component-type-in -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Type in the name of the Host to be accessed
   through SSH as well as the Port number.
2. Fill in the User identification name on the
   remote machine.
3. Select the Authentication method on the list.
   For this use case, the authentication method used is the public key.
4. Thus fill in the corresponding Private
   key.
5. On the Command field, type in the following
   command. For this use case, type in hostname; date between double
   quotes.
6. Select the Use timeout check box and set the
   time before falling in error to 5 seconds.

## Results

The remote machine returns the host name and the current date and time as defined on
its system.
