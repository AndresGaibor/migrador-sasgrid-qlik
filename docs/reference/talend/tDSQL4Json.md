<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-mapping/tdsql4json · versión 8.0 -->
# tDSQL4JSON

Last updated: 9/30/2026

Information noteNote: This component is not shipped with your Talend Studio by
default. To use it, you need to install the Data Integration > DSQL4JSON feature using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

Transforms JSON input data to JSON output data using DSQL.

## tDSQL4JSON Standard properties

These properties are used to configure tDSQL4JSON running in the
Standard Job framework.

The Standard
tDSQL4JSON component belongs to the Processing family.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

This component is available when you have installed the 8.0.1-R2025-09 Studio Monthly
or a later one provided by Talend.
For more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component. Select the type of schema from the dropdown list:  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.  Click Guess schema to retrieve the table schema from the source component. |
| Input name | Enter a name to be used as a reference of the entire JSON in the script. The name must be unique and not present in the selected input JSON data. By default, the input name is `in`. For example, if you write `SELECT in` in the script, `in` refers to all the input JSON data.  Starting with the 8.0.1-R2026-04 Studio Monthly, this parameter is only available if you have Talend Data Mapper installed in Talend Studio. If not, you can use the @inputInfo annotation at the beginning of your DSQL query to specify the input name. The annotation format is: /\* INPUT INFO ANNOTATIONS BEGIN \*/ @inputInfo( name = 'inputName', sample = 'filepath' ) /\* INPUT INFO ANNOTATIONS END \*/. This annotation is automatically added when migrating from an earlier component version. |
| Sample | Browse to a sample JSON file to enable the test run and autocomplete suggestions in the DSQL editor. |
| Script | Enter a DSQL script to transform your input JSON data. For more information about DSQL, see [Talend Data Shaping Language Reference Guide](https://help.qlik.com/talend/en-US/data-shaping-language-reference-guide/8.0/introduction-data-shaping-language).  For example, the following DSQL script returns a list of items that are shipped to London: FROM order WHERE shipto.city = 'London' UNNEST item SELECT { orderid, itemno, total\_price = quantity \* price }.  Note that single comment lines `//` are not supported in the script, but multi-line comment lines `/**/` are supported. The additional operation `+` is also not supported.  Byte array input and Stream input are not supported.  Starting with the 8.0.1-R2026-04 Studio Monthly, the component provides an enhanced DSQL editor with autocomplete suggestions, syntax highlighting, and contextual help based on the sample data structure. |
|  | Click to create a parameterized expression to be used in the DSQL script. For more information about parameterized expression, see [Using Data Shaping Parameterized Expression](https://help.qlik.com/talend/en-US/data-mapper-user-guide/8.0-R2026-03/using-data-shaping-parameterized-expression). If your script contains a parameterized expression that is not implemented in the parameterized editor, you can right-click the script and select Migrate Parameterized Expression(s) to add it. |
| Copy Full Script To Clipboard | Click to copy the full DSQL script to the clipboard. The copied script includes parameterized expressions defined in WITH clauses but excludes context variable annotations and debug comments. Use this feature to share DSQL scripts with team members, document data transformations, or test scripts in external DSQL interpreters. This button is available starting with the 8.0.1-R2026-06 Studio Monthly. |
| Test Run Environment | Select the environment defined in the Context view of your Job from which you want to execute a test run. Otherwise, the default environment is used. |
|  | Click to preview and validate the results of your DSQL script against the sample data. Starting with the 8.0.1-R2026-04 Studio Monthly, you can define context variables in the Context view of your Job, and reference them in your query using the getContextVariable('name', 'type') function, where name is the variable name and type is the data type. For test runs, select a context environment from the Test Run Environment dropdown list to apply those values during execution.  For example: FROM customer WHERE rating > getContextVariable('min\_rating', 'integer') SELECT name. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect the log data at both a Job and component levels. |
| Input JSON column | Select a column name that contains the input JSON data in the source component schema from the dropdown list. If the schema contains only one column, this column is used by default. |
| Set output column(s) | Select this checkbox to specify how the JSON result is emitted to the output schema. When enabled, configure the Output column mode property. If you leave this checkbox cleared, the JSON result is set to a column with the same name as the input JSON column. If there is no column with the same name, an error appears. |
| Output column mode | Select the mode to emit the JSON result:  * Result into one column: Emits the entire JSON   result into a single output column. This is the default   behavior. * Map result to schema columns: Maps each field   of the JSON result to corresponding columns in the output schema.   This mode is only compatible with JSON record outputs or arrays of   records (when combined with Emit multiple   rows).   Information noteNote: When using Map result to schema columns mode, ensure your DSQL script produces a JSON record output, and the output schema contains columns matching the field names in the JSON result. Field values are emitted as strings.  This property is only available when you select Set output column(s). |
| Output JSON column | This property is available when Set output column(s) is selected and Output column mode is set to Result into one column. Select the column name from the dropdown list where the JSON result will be stored. In case of a single column in the output schema, that column is used by default. |
| Emit multiple rows | Select this checkbox to split array outputs into separate rows during Job run. When combined with Output column mode set to Map result to schema columns, each record in an array is emitted as a separate row with fields mapped to the corresponding schema columns. |
| Enable Java functions calls | Select this checkbox to enable a Java function call in the DSQL script. For example, you can call a:  * Java static method:   `java:call(java:call('java.lang.String' , 'valueOf',   100), 'concat', '$')` * Java non-static method:   `java:call(java:call(java:new('java.text.SimpleDateFormat',   'yyyy-MM-dd'), 'parse', '2018-10-15'),   'getDate')`  For more information about Java functions calls, see [Calling Java function in expressions](https://help.qlik.com/talend/en-US/data-shaping-language-reference-guide/8.0/calling-java-functions). |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component only supports a single input and single output. |
