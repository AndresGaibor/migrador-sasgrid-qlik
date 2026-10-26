<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-file/cfile · versión 8.0 -->
# cFile

Last updated: 9/30/2026

Provides access to file systems, allowing files to be processed by any other
components or messages from other components to be saved to the disk.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cFile Standard properties

These properties are used to configure cFile running in the Standard Job framework.

The Standard
cFile component belongs to the Connectivity family.

Information noteNote: The properties of cFile is updated in R2026-01. To have all the properties in the
following tables, you need to install the R2026-01 Talend Studio
Monthly update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Path | Path to the file or files to be accessed or saved. |
| The following options are available when the cFile is used as a consumer: |  |
| Parameters/noop | When enabled, the file will not be moved or deleted in any way. |
| Parameters/recursive | When enabled, files in all the sub-directories will be consumed as well. |
| Parameters/readlock | When enabled, the file will be consumed only if it has exclusive read-lock on it. Select the strategy from:  * none: No read lock is in use. * markerFile: A marker file will be created and a   lock is hold on the file. * fileLock: For using java.nio.channels.FileLock.   This approach should be avoided when accessing a remote file system via a   mount/share unless that file system supports distributed file locks. * rename: Try to rename the file as a test to see   if an exclusive read lock can be obtained. * idempotent: For using an idempotentRepository as   the read-lock. This allows to use read-locks if the idempotent repository   implementation supports clustering. * idempotent-changed: For using an   idempotentRepository and changed as the combined read-lock. This allows   to use read-locks if the idempotent repository implementation supports   clustering. * idempotent-rename: For using an   idempotentRepository and rename as the combined read-lock. This allows to   use read-locks if the idempotent repository implementation supports   clustering. |
| Parameters/doneFileName | The name of a marker file (done file) to signal when a file is done and ready to be consumed. If provided, the file will only be consumed if a done file exists. The done file is always expected in the same folder as the original file. |
| Filter | Select a filter for the files to be consumed from:  * fileName: Filters the files based on the file name.   Specify the name of the file in the fileName   field. * Ant: Filters the files based on the Ant style.   Specify the inclusion and exclusion criteria respectively. Select the   case sensitive checkbox to enable case sensitive   matching. Multiple inclusions and exclusions can be separated by comma. If   both inclusion and exclusion are used, exclusion takes precedence over   inclusion. * Regex: Filters the files based on the regex pattern.   Specify the inclusion and exclusion criteria respectively. The matching is   case insensitive. * Extension: Filters the files based on the file   extension. Specify the inclusion and exclusion criteria respectively. The   matching is case insensitive. Multiple extensions can be separated by   comma. |
| move/success | This option allows you to move files that are consumed successfully to another location. Enter the success folder of your choice. For example, to move files into a .done sub-directory, enter ".done". |
| move/failed | This option allows you to move files that can not be consumed successfully to another location. Enter the error folder of your choice. |
| move/delete file | Select this checkbox to delete the file after it is consumed successfully. |

The following options are available when the cFile is used as a
producer:

| Properties | Description |
| --- | --- |
| FileName | The name of the file to write. |
| Parameters/fileExist | Select the operation if a file with the name specified in the FileName field already exists from:  * Override: Replace the existing file. * Append: Add content to the existing file. * Fail: Throw a GenericFileOperationException,   indicating that there is already an existing file. * Ignore: Silently ignore the problem and do not   override the existing file. * Move: Move any existing files to a target folder   before writing the file. Specify the target folder of your choice in the   move/exisiting field. * TryRename: Try renaming the file without doing   any exists check. |
| Parameters/doneFileName | The name of a marker file (done file) to signal when the original file has been written. If provided, a done file will be written. The done file will be empty and always written in the same folder as the original file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Parameters/AutoCreate | Select this checkbox to create the directory specified in the Path field automatically if it does not exist. |
| Parameters/Encoding | Specify the encoding of the file, ISO-8859-15, UTF-8, or CUSTOM. |
| Advanced | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. In the Name field, you can either select the URI option from the drop-down list, or enter an option name that is not available in the list. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/file2.html> for available URI options. |

The following options are available only when the cFile is used
as a producer:

| Properties | Description |
| --- | --- |
| Parameters/Flatten | Select this checkbox to flatten the file name path to strip any leading paths. This allows you to produce recursively into sub-directories, but when you, for example, write the files to another directory, they will be written in a single directory. |
| Parameters/BufferSize(kb) | Write buffer sized in bytes. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cFile can be a start, middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Reading and writing files in the local file system](cfile-reading-and-writing-files-in-the-local-file-system)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-file/cfile-reading-and-writing-files-in-the-local-file-system -->
# Reading and writing files in the local file system

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, two cFile components will
be used to read and write files in the local file system.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-file/cfile-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-file/cfile-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-file/cfile-viewing-code-and-executing-route)

**Related reference**  

* [cFile](cfile "Provides access to file systems, allowing files to be processed by any other components or messages from other components to be saved to the disk.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-file/cfile-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the first cFile
   component to display its Basic settings view in
   the Component tab.
2. Configure the properties as follows:
   1. In the Path field, browse to or enter
      the path `"C:/Talend/demo"` where two TXT files
      `input.txt` and `output.txt`
      exist.
   2. In the fileName field, enter the name of the file to
      be consumed, `"input.txt"` in this example.
   3. Keep the default settings of the other options.
3. Double-click the second cFile
   component to display its Basic settings view in
   the Component tab.
4. Configure the properties as follows:
   1. In the Path field, browse to or enter
      the file path `"C:/Talend/demo"`.
   2. In the fileName field, enter the name of the file to
      be written, `"ouput.txt"` in this example.
   3. In the fileExist list, select
      Move and enter `move` in the
      move/existing field to move the original
      `"output.txt"` file to the `move`
      sub-directory.
5. Press Ctrl+S to save your
   Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-file/cfile-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, expand the Connectivity/File folder and select the cFile component. Drop one as the input component
   and another as the output component onto the design workspace.
2. Right-click the input cFile component,
   select Row > Route in the contextual menu and click the output cFile component.
3. Label the components to better identify their respective
   functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-file/cfile-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to have a look at the generated code.

   As shown in the code, a message Route is built from
   "cFile\_cFile\_1\_consumer" to
   "cFile\_cFile\_2\_producer".
2. Click the Run view to display it
   and click the Run button to launch the execution
   of your Route. You can also press F6 to execute
   it. 

   RESULT:

   A new `output.txt` file is written
   in the `C:/Talend/demo` directory with the content of the
   `input.txt` file.

   The
   `input.txt` file is consumed and moved to the
   `.done` sub-directory.

   The original `output.txt` file is moved to the
   `move` sub-directory.
