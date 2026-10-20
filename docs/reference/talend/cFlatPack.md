<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack · versión 8.0 -->
# cFlatPack

Last updated: 9/30/2026

Processes fixed width or delimited files or messages using the [FlatPack
library](http://flatpack.sourceforge.net)

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cFlatPack Standard properties

These properties are used to configure cFlatPack running in the Standard Job framework.

The Standard
cFlatPack component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| When using as a start component in a route: |  |
| PZMAP FileType | The PZMAP file is the Flatpack configuration file that is used to configure the structure of the input file. For more information about the PZMAP file configuration, see the website <http://flatpack.sourceforge.net/documentation/index.html>.  Select the PZMAP file type from Filename and Repository Resource.  Filename: The PZMAP file is stored in the local file system.  Repository Resource: The PZMAP file is stored in the Resources node of the Repository. |
| PZMAP Filename | This option appears when Filename is selected in the PZMAP FileType list. Enter or browse to the path to the PZMAP file. |
| PZMAP Repository Resource | This option appears when Repository Resource is selected in the PZMAP FileType list. Click [...] and select the PZMAP file under the Resources node in the dialog box. |
| Fixed Positional file | Select this option if the file is a fixed format file. |
| Delimited file | Select this option if the file is delimited.  Text Qualifier: Specify the text qualifier for delimited files. The default value is ".  Text Delimiter: Specify the character delimiter for delimited files. The default value is ,. |
| Split Rows | Select this check box to process each row one by one. |
| Ignore First Record | Select this check box to ignore the first line for delimited files (for the column headers). This option is only available if the Delimited file option is selected. |
| Allow Short Lines | Select this check box to allow lines shorter than expected by the PZMAP file. |
| Ignore Extra Columns | Select this check box to allow lines longer than expected by the PZMAP file and ignore the extra characters. |
| When using as a middle or end component in a Route: |  |
| Use Exist cFlatPack | Click [...] and select the cFlatPack component to be used as the file parser in the dialog box. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cFlatPack can be a start, middle, or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Parsing delimited file using the cFlatPack component](cflatpack-cfile-cbean-clog-parsing-delimited-file-using-cflatpack-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-parsing-delimited-file-using-cflatpack-component -->
# Parsing delimited file using the cFlatPack component

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cFile component reads a delimited file
from the local file system, which contains the customers information including id, first
name, surname, and order id, as shown below:

```
1,"Harry",Carter,21
2,Padre,Boulevard,22
3,Andrew,Polk,23
4,Herbert,Reagan,"24"
5,Chester,Eisenhower,25
```

The file is parsed by the cFlatPack component, using
a predefined PZMAP XML file:

```
<?xml version="1.0"?>
<!-- DTD can be pulled from the Jar or over the web-->
<!DOCTYPE PZMAP SYSTEM	"flatpack.dtd" >
<!--<!DOCTYPE PZMAP SYSTEM	"http://flatpack.sourceforge.net/flatpack.dtd" >-->
<PZMAP>
	<COLUMN name="id" length="5" />
	<COLUMN name="name" length="20" />
	<COLUMN name="surname" length="20" />
	<COLUMN name="orderid" length="5" />
</PZMAP>
```

The customer information is then printed in the execution console by a cBean component.

For more information about the PZMAP file configuration, see the website <http://flatpack.sourceforge.net/documentation/index.html>.

### In this section

* [Creating a Bean](/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-creating-bean)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-viewing-code-and-executing-route)

**Related reference**  

* [cFlatPack](cflatpack "Processes fixed width or delimited files or messages using the FlatPack library")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cBean](/talend/en-US/mediation-components/8.0/mediation-bean/cbean)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click Delimited\_file in the design workspace to
   display its Basic settings view in the
   Component tab.
2. In the Path field, browse to or enter the file path
   where the flatpack file is located. 

   In the FileName field, enter the name of
   the file to be processed.
3. Double-click Flat\_file\_parser to display its Basic settings view in the Component tab.
4. Click [...] and in the Select a
   Node: wizard, select *FlatPack\_config* to configure the structure of the input
   file.
5. Double-click *FlatPack\_config* to display its Basic settings view in the Component tab.
6. In the PZMAP FileType list, select Filename to use the PZMAP XML file from the local file
   system to configure the structure of the input file. Then in the PZMAP Filename field, browse to path
   where the PZMAP XML file is located.

   Select the Allow Short Lines check box to
   allow lines shorter than expected by the PZMAP file.

   Keep the default settings of the other options.
7. Double-click ReadOrder to display its Basic settings view in the Component tab.
8. Select the New Instance option to invoke a Java bean
   that is stored in the Code node of the
   Repository. 

   In the Bean class field, enter the name of the bean
   class, *beans.ReadOrder.class* which is just
   created.
9. Keep the default settings of the cLog
   component to log the message exchanges.
10. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-creating-bean -->
# Creating a Bean

Last updated: 9/30/2026

## About this task

In this section, a JavaBean is created to print the id, first name, and
surname from the customer information with the corresponding column names into the
execution console.

## Procedure

1. From the repository tree view, expand the Code node and right click the Beans node. In the contextual menu, select Create Bean.

   The New Bean wizard opens. In the Name field, type in a name for the bean, for
   example, *ReadOrder*. Click Finish to close the wizard. The bean is opened automatically
   in the design workspace.
2. Enter the following code in the design workspace.

   ```
   package beans;

   import org.apache.camel.Exchange;

   public class ReadOrder {
   	

   	public static void getCustomer(Exchange exch) { 
   		if(exch.getIn().getBody() !=null)
   		{ 
   			java.util.Map data = exch.getIn().getBody(java.util.Map.class); 
   			if(data != null){ 
   				String id= (String)(data.get("id")); 
   				System.out.println("id :"+id);
   				String name= (String)(data.get("name")); 
   				System.out.println("name :"+name);
   				String surname= (String)(data.get("surname")); 
   				System.out.println("surname :"+surname);
   				exch.getIn().setBody("<customer><id>" + id + "</id><name>" + name + "</name><surname>" + surname + "</surname></customer>", String.class);
   			} 
   		}
   	}
   	
   	
   }
   ```
3. Press Ctrl+S to save your bean.

## Results

For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cFile, two cFlatPack, a cBean, and a
   cLog component onto the design
   workspace.
2. Link the components using the Row >
   Route connection as shown above.
3. Label the components to better identify their roles in the Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-flatpack/cflatpack-cfile-cbean-clog-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom
   of the design workspace to look at the generated code.

   As shown in the code, one Route is built from "Delimited\_file\_cFile\_1", to "cFlatPack\_1". The other is built from cFlatPack\_2, processed by "cBean\_1" and
   "cLog\_1" sequentially.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: The delimited file is parsed. The id, first name, and surname of the customer
   information with the corresponding column names is shown in the execution
   console.
