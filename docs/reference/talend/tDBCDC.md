<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/db-generic/tdbcdc · versión 8.0 -->
# tDBCDC

Last updated: 9/30/2026

Extracts only the changes made to the source operational data and makes them
available to the target system(s) using database CDC views.

This component works with a variety of databases
depending on your selection.

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tDBCDC Standard properties

These properties are used to configure tDBCDC running in the
Standard Job framework.

The Standard
tDBCDC component belongs to the Databases
family.

The component in this framework is available in all Talend
products.

## Basic settings

This component serves as an entry point
for the following databases. To configure this component, select a type of database from
the Database list and click Apply on its Basic
settings view. For more information about specific database properties,
see the relevant documentation. For example, for information about how to configure a
tDBCDC to work with AS400, see the tAS400CDC documentation.

* AS400
* IBM DB2
* Informix
* Ingres
* Microsoft SQL Server
* MySQL
* Oracle
* PostgreSQL
* Sybase (ASE and IQ)
* Teradata
