<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/taggregatesortedrow · versión 8.0 -->
# tAggregateSortedRow

Last updated: 9/30/2026

Aggregates the sorted input data for output column based on a set of operations. Each
output column is configured with many rows as required, the operations to be carried out and
the input column from which the data will be taken for better data aggregation.

## tAggregateSortedRow Standard properties

These properties are used to configure tAggregateSortedRow running in the Standard Job framework.

The Standard
tAggregateSortedRow component belongs to the Processing family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Click Sync columns to retrieve   the schema from the previous component connected in the Job.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-in: The schema will be   created and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused in   various projects and Job flowcharts. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Input rows count | Specify the number of rows that are sent to the tAggregateSortedRow component.    Information noteNote: If you specified a Limit for the number of rows to be processed in the input component, you will have to use that same limit in the Input rows count field. |
| Group by | * Define the aggregation sets, the values of which will be used for   calculations. * Output Column: Select the column   label in the list offered based on the schema structure you defined.   You can add as many output columns as you wish to make more precise   aggregations.  Ex: Select Country to calculate an average of values for each   country of a list or select Country and Region if you want to   compare one country's regions with another country' regions. * Input Column: Match the input   column label with your output columns, in case the output label of   the aggregation set needs to be different. |
| Operations | * Select the type of operation along with the value to use for the   calculation and the output field. * Output Column: Select the   destination field in the list.  Function: Select the operator among:   + count: calculates the number of rows   + min: selects the minimum value   + max: selects the maximum value   + avg: calculates the average   + sum: calculates the sum   + first: returns the first value   + last: returns the last value   + list: lists values of an aggregation by multiple keys.   + list (object): lists Java values of an aggregation by multiple keys   + count (distinct): counts the number of the distinct rows   + standard deviation: calculates the     variability of a set of value.   + union (geometry): makes the union of a set of Geometry objects   + population standard deviation: calculates the     spread of a data distribution. Use this function if the data to be     calculated is considered a population on its own. This calculation     supports 39 decimal places.   + sample     standard deviation: calculates the spread of a data     distribution. Use this function if the data to be calculated is     considered a sample from a larger population. This calculation     supports 39 decimal places. * Input column: Select the input   column from which the values are taken to be aggregated. * Ignore null values: Select the   check boxes corresponding to the names of the columns for which you   want the NULL value to be ignored. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Check this box to collect the log data at component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component handles flow of data therefore it requires input and output, hence is defined as an intermediary step. |

**Related concepts**  

* [Sorting and aggregating the input data](tsortrow-taggregatesortedrow-tlogrow-tfixedflowinput-sorting-and-aggregating-input-data-standard-component-this)
