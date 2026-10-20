<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-sharepoint/tsharepointconnection · versión 8.0 -->
# tSharePointConnection

Last updated: 9/30/2026

Creates an authenticated connection to SharePoint that the other SharePoint components can reuse.

## tSharePointConnection Standard properties

These properties are used to configure tSharePointConnection running in the Standard Job framework.

The Standard
tSharePointConnection component belongs to the Business and Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| URL | Enter the URL of the SharePoint account to be used. |
| Authentication mode | Select the authentication mode to access your SharePoint account:  * Bearer token if you access your SharePoint account   using a token. * OAuth2 certificate if you access your SharePoint   account using a certificate. To use this method, you need to have previously   registered an application and uploaded a certificate (public key) on   SharePoint. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | Use this component to create a connection that the other SharePoint components can reuse. |
