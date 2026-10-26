<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-bean/cbean · versión 8.0 -->
# cBean

Last updated: 9/30/2026

Invokes a Java bean that is stored in the Code node of the
Repository or registered by a
cBeanRegister.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cBean Standard properties

These properties are used to configure cBean running in the Standard Job framework.

The Standard
cBean component belongs to the Custom family.

## Basic settings

| Properties | Description |
| --- | --- |
| Reference | Select this option to reference a JavaBean registered by a cBeanRegister.  In the Id field that appears, enter the Id of the JavaBean. |
| New Instance | Select this option to invoke a JavaBean that is stored in the Code node of the Repository.  In the Bean class field that appears, enter the name of the bean class.  For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans). |
| Specify the method | Select this check box to enter the name of a method to be included in the bean. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cBean can be a start, middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Converting the body of an XML file into an org.w3c.dom.Document.class](cconvertbodyto-cbean-cfile-cbeanregister-converting-body-of-xml-file-into-org.w3c.dom.document.class)
