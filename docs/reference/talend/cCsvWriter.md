<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-csv-processing/ccsvwriter · versión 8.0 -->
# cCsvWriter

Last updated: 9/30/2026

Transforms the incoming data into CSV format.

Information noteNote: This component is available only if you have installed the R2024-10 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cCsvWriter Standard properties

These properties are used to configure cCsvWriter running in the
Standard Route framework.

The Standard
cCsvWriter component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| CSV Format | Select the format of the CSV file for parsing from Default, Custom, RFC-4180, Excel, MySQL, Oracle, PostgreSQL CSV, PostgreSQL TEXT, Informix UNLOAD, Informix UNLOAD CSV, TDF, Bean. |
| Custom | * Delimiter: Enter the separator   you want to use as the value delimiter. * Record Separator: Enter the record separator to delimit   output records. * Escape Character: Enter the character to be used as   escape character. * Null String: Enter the String to indicate that the value   is null. * Comment Marker: Enter the character to be written at the   start of each comment line. * Quote Mode: Select the quote policy to use for output   from None, Minimal,   All non-numeric values, All except null   values, and All values. Enter the mapping   class to be used for parsing the data into a map. In the   Quote field, enter the character to be used to   encapsulate values containing special characters. * Trim values: Select this check box to trim leading and   trailing blanks. * Handle CSV Headers: Select the way the headers will be handled.   + No header line: There is no header line.   + Custom defined headers: Define custom headers in     the CSV Columns table. Click [+] as many times as required to add columns     to the table. Then click the corresponding value field and enter a     value. |
| Bean | Bean Reference: Select the Bean where your custom CSV format is defined. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cCsvWriter can be a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Extracting and transforming data in CSV format](extracting-and-transforming-data-in-csv-format)
