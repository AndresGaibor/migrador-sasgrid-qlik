<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto · versión 8.0 -->
# cConvertBodyTo

Last updated: 9/30/2026

Converts the message body to the given class type.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cConvertBodyTo Standard properties

These properties are used to configure cConvertBodyTo running in the Standard Job framework.

The Standard
cConvertBodyTo component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| Target Class Name | Enter the name of the class type that you want to convert the message body to. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cConvertBodyTo is used as a middle component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Converting the body of an XML file into an org.w3c.dom.Document.class](cconvertbodyto-cbean-cfile-cbeanregister-converting-body-of-xml-file-into-org.w3c.dom.document.class)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-converting-body-of-xml-file-into-org.w3c.dom.document.class -->
# Converting the body of an XML file into an org.w3c.dom.Document.class

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cConvertBodyTo component is used
to convert the body of an XML file into an org.w3c.dom.Document.class. Then a cBean component imports the org.w3c.dom.Document class,
checks its content and prints out the root element name and the content of each
category element.

The XML file is as follows:

```
<bookstore>
    <bookshelf>
        <category>Cooking</category>
        <quantity>100</quantity>
    </bookshelf>
    <bookshelf>
        <category>Languages</category>
        <quantity>200</quantity>
    </bookshelf>
    <bookshelf>
        <category>Arts</category>
        <quantity>300</quantity>
    </bookshelf>
    <bookshelf>
        <category>Science</category>
        <quantity>400</quantity>
    </bookshelf>
</bookstore>
```

### In this section

* [Creating a Bean](/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-creating-bean?id=184)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-dropping-and-linking-components?id=185)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-configuring-components?id=186)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-viewing-code-and-executing-route?id=187)

**Related reference**  

* [cConvertBodyTo](cconvertbodyto "Converts the message body to the given class type.")

**Related information**  

* [cBean](/talend/en-US/mediation-components/8.0/mediation-bean/cbean)
* [cBeanRegister](/talend/en-US/mediation-components/8.0/mediation-bean/cbeanregister)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component to open
   its Basic settings view in the Component tab.
2. In the Path field, enter or browse to the
   path to the source XML file. 

   If the source file folder contains more than one file, enter the name of
   the XML file of interest in the FileName
   field, and leave the other parameters as they are.
3. Double-click the cConvertBodyTo component
   to open its Basic settings view in the
   Component tab.
4. In the Target Class Name field,
   enter your target class name, `org.w3c.dom.Document.class` in
   this scenario.
5. Double-click the cBeanRegister component to open its Basic
   settings view in the Component
   tab.
6. In the Id field, enter
   `"bean"`.

   Select the Simple option and in
   the Class Name field, enter the name of the bean
   to be invoked, `beans.PrintConvertToBean` in this
   scenario.
7. Double-click the cBean component to open
   its Basic settings view in the Component tab.
8. Select Reference and in the
   Id field, enter `"bean"`
   to call the bean that is registered by the cBeanRegister.
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-creating-bean -->
# Creating a Bean

Last updated: 9/30/2026

## Procedure

1. From the repository tree view, expand the Code node and right-click the Beans node. In the contextual menu, select Create Bean.
2. The New Bean wizard opens. In the
   Name field, type in a name for the bean, for
   example, `PrintConvertToBean`. Click Finish to close the wizard.
3. Enter the following code in the design workspace.

   ```
   package beans;

   import org.w3c.dom.Document;
   import org.w3c.dom.Element;
   import org.w3c.dom.NodeList;
   public class PrintConvertToBean {

   	/**
   	 * print input message
   	 * @param message
   	 */
   	public static void helloExample(Document message) {
   		if (message == null) {
   			System.out.println("There's no message here!");
   			return;
   		}
   		Element rootElement = message.getDocumentElement();
   		if (rootElement == null) {
   			System.out.println("There's no root element here!");
   			return;
   		}
   		System.out.println("The root element name is:"
   				+ rootElement.getNodeName());
   		System.out.println("The book categories are:");
   		NodeList types = rootElement.getElementsByTagName("category");
   		for(int i = 0;i<types.getLength();i++){
   			Element child = (Element) types.item(i);
   			System.out.println(child.getFirstChild().getNodeValue());
   		}
   	}
   }
   ```
4. Press Ctrl+S to save your bean.

## Results

For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drag and drop a cFile, a cConvertBodyTo, a cBean and a cBeanRegister
   from the Palette onto the workspace.
2. Link the cFile, cConvertBodyTo and cBean
   using the Row > Route connection as shown above.
3. Label the components to better identify their functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-convertbody/cconvertbodyto-cbean-cfile-cbeanregister-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message from the endpoint
   Read\_message\_cFile\_1 has its body converted to
   org.w3c.dom.Document.class by
   cConvertBodyTo\_1, and then processed by bean
   invoked by cBean\_1.
2. Press F6 to execute the Route.

   RESULT: The root element name and the contents of the category elements are displayed.
