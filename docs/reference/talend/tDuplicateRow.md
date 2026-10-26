<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tduplicaterow · versión 8.0 -->
# tDuplicateRow

Last updated: 9/30/2026

Creates duplicates with meaningful data for data quality functional testing
purposes.

tDuplicateRow generates duplicate
data from an input flow. It groups similar duplicates together and
identifies the original record of each group by
true.

This component can be used in combination with the tRowGenerator component to generate
duplicate data.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDuplicateRow Standard properties

These properties are used to configure tDuplicateRow running
in the Standard Job framework.

The Standard
tDuplicateRow component belongs to the Data Quality family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Sync columns   to retrieve the schema from the previous component in the Job.  The output schema of this component contains one read-only   column, *ORIGINAL\_MARK*. This column identifies by   true or false if the record is an original record or a duplicate   record respectively. There is only one original record per group. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Percentage of duplicated records | Enter the percentage of the duplicate rows you want to have in the output flow. |
| Distribution of duplicates | Name: Select the probability distribution you want to use to generate duplicates: Bernoulli distribution or Poisson distribution or Geometric distribution.  Average group size: Set the average number of duplicate records you want to generate in the groups of duplicates. |
| Modifications | Define in the table what fields to change in a row and how to change them:  -Input Column: Select the column from the input flow from which you want to generate duplicates through modifying its values.  -Modification Rate: Enter a rate of the modifications you want to have in the duplicate record generated from an input column. The rate is a value between *0* and *1*. If you set the rate to *0*, no modification will be done. If you set the rate to *0.5*, modification will be done in average every two rows. But if you set the rate to *1*, modification is done at each row.  These modifications are based on the function you select in the Function column and the number of modifications you set in the Max Modification Count column.  -Function: Select the function that will decide what modification to do on a value to duplicate it. For example, you can decide to have exact or approximate duplicate values through replacing or adding letters or numbers, replacing values with synonyms from an index file or deleting values by setting the function to null or blank.  The Function list will vary according to the column type. For example, a column of a *String* type will have an *Add letters* option in the list while a column of an *Integer* type will have an *Add digits* option in the list. Also, the Function list for a *Date* column is date-specific. For further information about the functions used on *Date* columns, see [Date functions in tDuplicateRow](/talend/en-US/components/8.0/data-privacy/tduplicaterow-tduplicaterow-date-functions-in-tduplicaterow-standard-component-enterprise-the).  -Max Modification Count: Enter a maximum number of the values to be modified.  -Synonym Index Path: Set the path to the index file from which you use the synonym.  This field is available if you select the *Synonym replace* function which means that the value in the duplicate record is replaced by one of its synonym, according to the given the rate.  You must use the tSynonymOutput component to create a Lucene index and feed it with synonyms. For further information about how to create a synonym index and define the reference entries, see [tSynonymOutput](/talend/en-US/components/8.0/synonym-index/tsynonymoutput). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Seed for random generator | Set a random number if you want to generate the same sample of duplicates in each execution of the Job.  Repeating the execution with a different value for the seed will result in a different duplicate sample being generated.  Keep this field empty if you want to generate a different duplicate sample each time you execute the Job. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component helps you to generate duplicate data of an input flow according to certain criteria and use it for testing purposes. |

**Related tasks**  

* [Generating duplicate data from an input flow](generating-duplicate-data-from-input-flow "This scenario describes a basic Job that generates a sample of duplicate data from an input flow by using probability theories and specific criteria on three columns: Name, City and DOB (date of birth).")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-privacy/tduplicaterow-tduplicaterow-date-functions-in-tduplicaterow-standard-component-enterprise-the -->
# Date functions in tDuplicateRow

Last updated: 9/30/2026

The Function list for a *Date*
column is date-specific. It allows you to decide the type of modification you want to do
on date values.

There are three different ways to generate the date value for duplicated
records:

* Modify date value: randomly selects the day,
  month or year to modify and puts a random value in place.
* Switch day month value: switches the day and
  month values. If the original day value is greater than 12, then the new month
  value will be *((N-1) mod 12) +1*. For example: If the
  original day is equal to 13, then the new month is equal to 1.
* Replace by random date: generates a random
  date with day, month and year values.
