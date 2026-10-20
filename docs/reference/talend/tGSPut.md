<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgsput · versión 8.0 -->
# tGSPut

Last updated: 9/30/2026

Uploads files from a local directory to Google Cloud Storage so that you can manage
them with Google Cloud Storage.

## tGSPut Standard properties

These properties are used to configure tGSPut running in the Standard Job framework.

The Standard
tGSPut component belongs to the Big Data and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List click the relevant connection component to reuse the connection details you already defined. |
| Credential type | Select the mode to be used to authenticate to your project.  * Service account: authenticate using a Google account   that is associated with your Google Cloud Platform project. When selecting this   mode, the access key must be provided in the Service account   key field. * Workload Identity Federation: authenticate using an   external identity provider, such as AWS, Azure, or OIDC, without needing a   service account key. When selecting this mode, the identity federation   configuration must be provided in the Client library configuration   file field. * Application Default Credentials: authenticate using the   Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based on   the application environment. * OAuth Access Token: authenticate using an OAuth access   token. When selecting this mode, the token must be provided in the   OAuth Access Token field.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Service account key | Click the [...] button next to the service account key field to browse for the JSON file that contains your service account key.  This property is only available when you authenticate using Service account. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit. This property is only available when you authenticate using OAuth Access Token. |
| Bucket name | Type in the name of the bucket into which you want to upload files. |
| Project ID | When the credential type is set to OAuth Access Token, specify the project ID into which you want to upload files. |
| Local directory or file | Type in the full path of or browse to the local file or directory where the files to be uploaded are located.  If you select the Use files list check box, you can only specify a directory in this field.  If you unselect the Use files list check box, you can specify a file or directory in this field. |
| Google Storage directory | Type in the Google Storage directory to which you want to upload files. |
| Use files list | Select this check box and complete the Files table with the files to be uploaded.   * Filemask: enter the   pattern used to match the file or files you want to upload.  If you enter part of a file name, you can use the "\*" character to   replace any number of characters in the file name.  For example, sales\_\*.csv would look for both   sales\_112023.csv and   sales\_122023.csv * New name: enter a   new name for the file to be uploaded. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use a custom endpoint | Select this check box to use a private endpoint rather than the default one. When selected, enter the URL in the Google Storage Private API URL property, by respecting the following format: "https://storage.goggleapis.com".  For more information, see [Access Google APIs through endpoints](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis) from Google documentation.  This property is only available when you authenticate using Service account and Application Default Credentials. |
| Part size(Mb) | Specify the part size (in MB) when uploading an object in parts. The property work as follows:  * If the value is 0, the object is uploaded without being divided into   parts. * If the value is bigger than 0, the object that is bigger than the part   size is uploaded in parts. * If the value is bigger than 0, the object that is smaller is uploaded   without being divided into parts.  The file should not be larger than 2147483647 bytes when the value is 0.  This option is available with all credential types. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used together with other components, particularly the tGSGet component. |

**Related concepts**  

* [Managing files with Google Cloud Storage](tgscopy-tgslist-tlogrow-managing-files-with-google-cloud-storage-standard-component-the)
