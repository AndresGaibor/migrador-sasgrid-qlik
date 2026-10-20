<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tableau/ttableauinput · versión 8.0 -->
# tTableauInput

Last updated: 9/30/2026

Retrieves data from a site on a Tableau server and sends them to the component that
follows for transformation. Note that this component only retrieves data from HYPER (hyper)
extraction files. It requires Tableau Server 2020.3 (and later versions) and requires that
Tableau REST API be enabled on the Tableau server. See [REST
API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_requ.htm) for related information.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tTableauInput Standard properties

These properties are used to configure tTableauInput running
in the Standard Job framework.

The Standard
tTableauInput component belongs to the Business Intelligence family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0 R2022-02 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| URL | Enter the Tableau server URL. |
| Site | Enter the site URL. On a Tableau server, users, groups, and contents are grouped in sites. See [What is a site](https://help.tableau.com/current/server/en-us/sites_intro.htm) for related information. |
| Authentication | Specify the authentication method for logging into the Tableau server: Basic or Token. |
| Username and Password | Enter the authentication information required to access the server.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only.  These two fields are available when you select Basic from the Authentication drop-down list. |
| Token name and Token secret | Enter your personal access token name and token secret required to access the server. See [Create and revoke personal access tokens](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens) and [Personal Access Tokens](https://help.tableau.com/current/server/en-us/security_personal_access_tokens.htm) for related information.  To enter the token secret, click the [...] button next to the Token secret field to bring out the Enter a new password dialog box, enter the token secret in the text field, and click OK. Note that you can enter the token secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter token secrets in the Java mode   only.  These two fields are available when you select Token from the Authentication drop-down list. |
| Project name | Enter the project name. On a Tableau server, a project holds related contents. See [Use Projects to Manage Content Access](https://help.tableau.com/current/server/en-us/projects.htm) for related information. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the table schema. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link. |
| **Limitations** | If you are using Apple Silicon with arm64 CPU, this component might not be compatible with your architecture by default. Read the [Tableau documentation](https://tableau.github.io/hyper-db/docs/releases/) for more information. |
