<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprojaiinput · versión 8.0 -->
# tMapROjaiInput

Last updated: 9/30/2026

Reads documents from a MapR-DB database to load the data in a given Job.

You must have properly installed and configured your MapR Client before using this component. A \opt\mapr\conf\mapr-clusters.conf file is automatically generated out of the Client configuration process to store the connection information to your MapR cluster and your MapR-DB database. At runtime, this OJAI component reads this connection information by itself to connect to the MapR-DB database to be used.

For further information about how to install and configure your MapR client, see [Setting up the Client](http://doc.mapr.com/display/MapR/Setting+Up+the+Client) from the MapR documentation.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMapROjaiInput Standard properties

These properties are used to configure tMapROjaiInput running in the Standard Job framework.

The Standard
tMapROjaiInput component belongs to the Databases NoSQL family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component supports the Document type. If a field is for entire documents, select Document in the Type column for this field in the schema editor.  Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Use kerberos authentication | If you are accessing a MapR-DB as-OJAI database running with Kerberos security, select this checkbox, then, enter the Kerberos principal name and password in the displayed fields.  Every time when you launch your Job, the component submits this authentication information to Kerberos for a new kinit ticket. |
| Use a keytab to authenticate | Select the Use a keytab to authenticate checkbox to log into a Kerberos-enabled system using a given keytab file. A keytab file contains pairs of Kerberos principals and encrypted keys. You need to enter the principal to be used in the Principal field and the access path to the keytab file itself in the Keytab field. This keytab file must be stored in the machine in which your Job actually runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily the one a principal designates but must have the right to read the keytab file being used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this situation, ensure that *user1* has the right to read the keytab file to be used. |
| Restrict partial sorts with Secondary Indexes | Select this check box to force the query to explicitly sort on the actual data. This way, you avoid in your query the partial sorts that could otherwise occur due to the asynchronous secondary indexes.  For further information about this partial sorts issue of MapR OJAI, see [Asynchronous Secondary Index Updates](https://maprdocs.mapr.com/home/MapR-DB/Indexes/indexes-consistency.html#indexes-consistency) from the MapR documentation.  Do not select this check box if you do not expect to encounter the lags in the asynchronous indexes or you know that the impact of the lags is trivial. By keeping this check box clear, your query benefits from the ordering advantages provided by the secondary indexes of MapR-DB JSON tables. |
| Table name | Enter the name of the table to be processed. |
| Query | Specify the where clause of the query to be performed by tMapROjaiInput.  For example, type in "{id:{$eq: 4}}" or "{id:4}}"to retrieve the record in which *id* is *4*.  As OJAI uses MongoDB query format for queries, see [Query Operators](https://docs.mongodb.com/manual/reference/operator/query/) from the MongoDB documentation for available operators. |
| Mapping | Each column of the schema defined for this component represents a field of the documents to be read. In this table, you need to specify the parent nodes of these fields, if any.  For example, in the document reading as follows  ``` {                _id: ObjectId("5099803df3f4948bd2f98391"),                person: { first: "Joe", last: "Walker" }             } ```  The *first* and the *last* fields have *person* as their parent node but the *\_id* field does not have any parent node. So once completed, this Mapping table should read as follows:  ``` Column     Parent node path _id first       "person" last        "person" ``` |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tMapROjaiInput executes queries to read data from a given MapR-DB database. It is a starting component of a Job and requires an outgoing link to send data to its following component. |
