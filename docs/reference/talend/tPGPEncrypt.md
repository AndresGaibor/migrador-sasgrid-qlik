<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gpg/tpgpencrypt · versión 8.0 -->
# tPGPEncrypt

Last updated: 9/30/2026

Encrypts or signs a file using OpenPGP and stores the encrypted or signed file in a
specified directory. The key algorithms supported includes RSA, EIGamal, DSA, ECDH, ECDSA,
and EdDSA.

## tPGPEncrypt Standard properties

These properties are used to configure tPGPEncrypt running in
the Standard Job framework.

The Standard
tPGPEncrypt component belongs to the File
family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is available only when you have installed the 8.0.1-R2023-07 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use public key file | Select this option to encrypt/sign the file using a public key file. You need to enter the path to the public key file in the Public key file path field.  This option is available when Encrypt or Encrypt and sign is selected from the Action drop-down list. |
| Public key | Enter the public key to encrypt/sign the file.  To enter the public key, click the [...] button next to the Public key field to bring out the Enter a new password dialog box, enter the public key in the text field, and click OK. Note that you can enter the public key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  This option is available when Encrypt or Encrypt and sign is selected from the Action drop-down list and the Use public key file option is not selected. |
| Use private key file | Select this option to encrypt/sign the file using a private key file. You need to enter the path to the private key file in the Private key file path field.  This option is available when Sign or Encrypt and sign is selected from the Action drop-down list. |
| Private key | Enter the private key to encrypt/sign the file.  To enter the private key, click the [...] button next to the Private key field to bring out the Enter a new password dialog box, enter the private key in the text field, and click OK. Note that you can enter the private key either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  This option is available when Encrypt or Encrypt and sign is selected from the Action drop-down list and the Use public key file option is not selected. |
| Private key passphrase | Enter the passphrase of the private key.  To enter the private key passphrase, click the [...] button next to the Private key passphrase field to bring out the Enter a new password dialog box, enter the private key passphrase in the text field, and click OK. Note that you can enter the private key passphrase either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field.  This option is available when Sign or Encrypt and sign is selected from the Action drop-down list and the Use private key file option is not selected. |
| Action | Select the action to be performed on the file: Encrypt, Encrypt and sign, or Sign. |
| Source file | Enter the path to the file to be encrypted or signed. |
| Target file | Enter the path to the target file. |
| Message passphrase | Enter a message passphrase for encrypting the specified input file. This field is optional.  To enter the message passphrase, click the [...] button next to the Message passphrase field to bring out the Enter a new password dialog box, enter the message passphrase in the text field, and click OK. Note that you can enter the message passphrase either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |
| Signature type | Set the signature type: Binary document or Canonical text document. |
| Convert output to ASCII-armored format | Select this option to convert the output file to ASCII-armored format. |
| Output comment | Enter a comment for the ASCII-armored conversion. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a standalone component. |
