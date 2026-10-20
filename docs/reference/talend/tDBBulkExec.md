<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/db-generic/tdbbulkexec · versión 8.0 -->
# tDBBulkExec

Last updated: 9/30/2026

Offers gains in performance while executing the Insert operations on a
database.

This component works with a variety of databases
depending on your selection.

The tDBOutputBulk and tDBBulkExec components are
used together in a two step process. In the first step, an output file is generated. In
the second step, this file is used in the INSERT statement used to feed a database the
selected database type. These two steps are fused together in the
tDBOutputBulkExec component, detailed in a separate section. The
advantage of using two separate steps is that the data can be transformed before it is
loaded in the database.

## tDBBulkExec Standard properties

These properties are used to configure tDBBulkExec running in the Standard Job framework.

The Standard
tDBBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

This component serves as an entry point
for the following databases. To configure this component, select a type of database from
the Database list and click Apply on its Basic
settings view. For more information about specific database properties,
see the relevant documentation. For example, for information about how to configure a
tDBCDC to work with AS400, see the tAS400CDC documentation.

* Access
* Amazon Redshift
* Exasol
* Greenplum
* IBM DB2
* Informix
* Ingres
* Microsoft SQL Server
* MySQL
* Netezza
* Oracle
* ParAccel
* PostgreSQL
* SingleStore
* Snowflake
* Sybase (ASE and IQ)
* Sybase IQ
* Vertica
