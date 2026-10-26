<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/ctransaction · versión 8.0 -->
# cTransaction

Last updated: 9/30/2026

Handles transaction for multiple cSQLConnection components within the same Camel
context.

Information noteNote: This component is available only if you have installed the R2025-01 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cTransaction Standard properties

These properties are used to configure cTransaction running in
the Standard Route framework.

The Standard
cTransaction component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Datasource | Select a cTransaction component from the list that has enabled transaction. |
| Propagation Type | Select the propagation type from:  * PROPAGATION\_MANDATORY: Throw an exception if no transaction exists. * PROPAGATION\_REQUIRED: Reuse an existing transaction or create a new one   if none exists. * PROPAGATION\_REQUIRES\_NEW: Create a new transaction, suspending the   current transaction if one exists. * PROPAGATION\_NESTED: Execute within a nested transaction if a current   transaction exists or create a new one if none exists. * PROPAGATION\_SUPPORTS: Use a transaction if available. Execute   non-transactionally if none exists. * PROPAGATION\_NOT\_SUPPORTED: Always execute non-transactionally. * PROPAGATION\_NEVER: Throw an exception if a transaction exists. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cTransaction can be a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Writing and reading data in an H2 database with an SQL statement](csql-writing-and-reading-data-in-an-h2-database-with-an-sql-statement)
