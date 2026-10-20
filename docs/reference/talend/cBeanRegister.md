<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-bean/cbeanregister · versión 8.0 -->
# cBeanRegister

Last updated: 9/30/2026

Registers a Java bean in the registry to be used in message exchanges.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cBeanRegister Standard properties

These properties are used to configure cBeanRegister running in the Standard Job framework.

The Standard
cBeanRegister component belongs to the Custom family.

## Basic settings

| Properties | Description |
| --- | --- |
| Id | Enter any string which is used to look up the bean in the registry. |
| Simple | Select this option to call a bean class that is stored in the Code node of the Repository. |
| Customized | Select this option to define the JavaBean by entering the code in the Code box. |
| Class Name | This field appears when the Simple option is selected.  Enter the name of the bean class that is stored in the Code node of the Repository.  For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans). |
| Specify Arguments | This check box appears when the Simple option is selected. Select this check box to set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. |
| Code | This box appears when the Customized option is selected.  Enter the code of the bean in the box. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Imports | This box appears when the Customized option is selected in the Basic settings view.  Enter the Java code that helps to import, if necessary, external libraries used in the Code box. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cBeanRegister cannot be added directly in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Converting the body of an XML file into an org.w3c.dom.Document.class](cconvertbodyto-cbean-cfile-cbeanregister-converting-body-of-xml-file-into-org.w3c.dom.document.class)
