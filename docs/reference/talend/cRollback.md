<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/crollback · versión 8.0 -->
# cRollback

Last updated: 9/30/2026

Triggers rollback when error occurs in Route.

Information noteNote: This component is available only if you have installed the R2025-01 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cRollback Standard properties

These properties are used to configure cRollback running in the
Standard Route framework.

The Standard
cRollback component belongs to the Connectivity family.

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cRollback can be a middle or end component in a Route. It is used to trigger rollback when unhandled exception occurs. When the cOnException component is used to handle exceptions in the Route, cRollback can be used to trigger rollback explicitly. For more information, see [cOnException](https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/conexception). |
| Limitation | n/a |

**Related concepts**  

* [Writing and reading data in an H2 database with an SQL statement](csql-writing-and-reading-data-in-an-h2-database-with-an-sql-statement)
