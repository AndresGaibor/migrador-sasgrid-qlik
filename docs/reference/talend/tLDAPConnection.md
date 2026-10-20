<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ldap/tldapconnection · versión 8.0 -->
# tLDAPConnection

Last updated: 9/30/2026

Creates a connection to an LDAP Directory server.

tLDAPConnection can be invoked by other components that need to access
the LDAP Directory server, e.g., tLDAPInput,
tLDAPOutput, etc.

## tLDAPConnection Standard properties

These properties are used to configure tLDAPConnection running in the Standard Job framework.

The Standard
tLDAPConnection component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Host | LDAP Directory server IP address. |
| Port | Listening port number of server. |
| Protocol | Select the protocol type on the list.  LDAP: no encryption is used  LDAPS: secured LDAP. When this option is chosen, the Advanced CA check box appears. Once selected, the advanced mode allows you to specify the directory and the keystore password of the certificate file for storing a specific CA. However, you can still deactivate this certificate validation by selecting the Trust all certs check box.  TLS: certificate is used. When this option is chosen, the Advanced CA check box appears and is used the same way as that of the LDAPS type. |
| Base DN | Path to user's authorized tree leaf. |
| User and Password | Fill in the User and Password as required by the directory  Note that the login must match the LDAP syntax requirement to be valid. e.g.: "cn=Directory Manager".  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Alias dereferencing | Select the option on the list. Never improves search performance if you are sure that no aliases is to be dereferenced. By default, Always is to be used:  Always: Always dereference aliases  Never: Never dereferences aliases.  Searching:Dereferences aliases only after name resolution.  Finding: Dereferences aliases only during name resolution |
| Referral handling | Select the option on the list:  Ignore: does not handle request redirections  Follow:does handle request redirections |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is to be used with other LDAP components, especially with tLDAPInput and tLDAPOutput. |
