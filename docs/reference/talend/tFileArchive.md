<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/archive-unarchive/tfilearchive · versión 8.0 -->
# tFileArchive

Last updated: 9/30/2026

Creates a new zip, gzip, or tar.gz archive file from one or more files or
folders.

The archive file can be compressed using different
compression method.

## tFileArchive Standard properties

These properties are used to configure tFileArchive running in the Standard Job framework.

The Standard
tFileArchive component belongs to the File family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Directory | Specify the directory that contains the files to be added to the archive file.  This field is available when zip or tar.gz is selected from the Archive format list.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Subdirectories | Select this check box if you want to add the files in the subdirectories to the archive file.  This field is available only when zip is selected from the Archive format list. |
| Source File | Specify the path to the file that you want to add to the archive file.  This field is available only when gzip is selected from the Archive format list. |
| Archive file | Specify the path to the archive file to be created.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Create directory if does not exist | Select this check box to create the destination folder if it does not exist. |
| Archive format | Select an archive file format from the list: zip, gzip, or tar.gz. |
| Compress level | Select the compression level you want to apply.   * Best: the compression   quality will be optimum, but the compression time will be   long. * Normal: the compression   quality and time will be average. * Fast (no compression):   the compression will be fast, but the quality will be   lower. |
| All files | Select this check box if all files in the specified directory will be added to the archive file. Clear it to specify the file(s) you want to add to the archive file in the Files table.  Filemask: type in the file name or the file mask using a special character or a regular expression.  This check box is available when zip or tar.gz is selected from the Archive format list. |
| Encoding | Select an encoding type from the list or select CUSTOM and define it manually. This field is compulsory for DB data handling.  This list is available when zip is selected from the Archive format list. |
| Overwrite Existing Archive | This check box is selected by default. This allows you to save an archive by replacing the existing one. But if you clear the check box, an error is reported, the replacement fails and the new archive cannot be saved.  Information noteNote: When the replacement fails, the Job runs. |
| Encrypt files | Select this check box if you want the archive file to be password protected.  Encrypt method: select an encrypt method from the list, Java Encrypt, Zip4j AES, or Zip4j STANDARD.  AES Key Strength: select a key strength for the Zip4j AES method, either AES 128 or AES 256.  Enter Password: enter the encryption password.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This check box is available only when zip is selected from the Archive format list. With this check box selected, the compressed archive file can be decompressed only by the tFileUnarchive component and not by a common archiver. For more information about tFileUnarchive, see [tFileUnarchive](/talend/en-US/components/8.0/archive-unarchive/tfileunarchive). |
| ZIP64 mode | This option allows for archives with the .zip64 extension to be created, with three modes available:  * ASNEEDED: archives   with the .zip64 extension will be automatically created   based on the file size. * ALWAYS: archives with   the .zip64 extension will be created, no matter what   size the file may be. * NEVER: no archives   with the .zip64 extension will be created, no matter   what size the file may be.  Note that if the file size or the total size of the archive exceeds 4GB or there are more than 65536 files inside the archive, you need to set the mode to ALWAYS. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use sync flush | Select this check box to flush the compressor before flushing the output stream. Clear this check box to flush only the output stream.  This check box is available when gzip or tar.gz is selected from the Archive format list. |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ARCHIVE\_FILEPATH: the path to the archive file. This is an After variable and it returns a string.  ARCHIVE\_FILENAME: the name of the archive file. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component must be used as a standalone component. |
| Connections | Outgoing links (from this component to another):  Row: Main; Reject; Iterate.  Trigger: On Subjob Ok; On Subjob Error; Run if; On Component Ok; On Component Error.    Incoming links (from one component to this one):  Row: Main; Reject; Iterate.  Trigger: Run if; On Subjob Ok; On Subjob Error; On component Ok; On Component Error; Synchronize; Parallelize.    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |

**Related concepts**  

* [Zipping files using a tFileArchive](tfilearchive-zipping-files-using-tfilearchive-standard-component "This scenario creates a Job with a unique component. It aims at zipping files and recording them in the selected directory.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/archive-unarchive/tfilearchive-zipping-files-using-tfilearchive-standard-component -->
# Zipping files using a tFileArchive

Last updated: 9/30/2026

This scenario creates a Job with a unique component. It aims at zipping files and
recording them in the selected directory.

### In this section

* [Procedure](/talend/en-US/components/8.0/archive-unarchive/tfilearchive-procedure-standard-component-drop)

**Related reference**  

* [tFileArchive](tfilearchive "Creates a new zip, gzip, or tar.gz archive file from one or more files or folders.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/archive-unarchive/tfilearchive-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop the tFileArchive component from the
   Palette onto the workspace.
2. Double-click it to display its Component
   view.
3. In the Directory field, click the [...] button, browse your directory and select the
   directory or the file you want to compress.
4. Select the Subdirectories check box if you
   want to include the subfolders and their files in the archive.
5. Then, set the Archive file field, by filling
   the destination path and the name of your archive file.
6. Select the Create directory if not exists
   check box if you do not have a destination directory yet and you want
   to create it.
7. In the Compress level list, select the
   compression level you want to apply to your archive. In this example, we use the
   normal level.
8. Clear the All Files check box if you only
   want to zip specific files.
9. Add a row in the table by clicking the [+]
   button and click the name which appears. Between two star symbols
   (ie. \*RG\*), type part of the name of the file that you want to compress.
10. Press F6 to execute your Job.

## Results

The tFileArchive has compressed the selected file(s)
and created the folder in the selected directory.
