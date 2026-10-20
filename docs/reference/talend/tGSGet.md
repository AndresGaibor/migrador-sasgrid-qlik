<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgsget · versión 8.0 -->
# tGSGet

Last updated: 9/30/2026

Retrieves objects which match the specified criteria from Google Cloud Storage and
outputs them to a local directory.

## tGSGet Standard properties

These properties are used to configure tGSGet running in the Standard Job framework.

The Standard
tGSGet component belongs to the Big Data and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List click the relevant connection component to reuse the connection details you already defined. |
| Credential type | Select the mode to be used to authenticate to your project.  * Service account: authenticate using a Google account   that is associated with your Google Cloud Platform project. When selecting this   mode, the access key must be provided in the Service account   key field. * Workload Identity Federation: authenticate using an   external identity provider, such as AWS, Azure, or OIDC, without needing a   service account key. When selecting this mode, the identity federation   configuration must be provided in the Client library configuration   file field. * Application Default Credentials: authenticate using the   Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based on   the application environment. * OAuth Access Token: authenticate using an OAuth access   token. When selecting this mode, the token must be provided in the   OAuth Access Token field.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Service account key | Click the [...] button next to the service account key field to browse for the JSON file that contains your service account key.  This property is only available when you authenticate using Service account. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit. This property is only available when you authenticate using OAuth Access Token. |
| Key prefix | Specify the prefix to download only objects which keys begin with the specified prefix. |
| Delimiter | Specify the delimiter in order to download only those objects with key names up to the delimiter. |
| Specify project ID | When the credential type is set to OAuth Access Token, select this check box and in the Project ID field enter the project ID from which you want to obtain objects. |
| Use keys | Select this check box and complete the Keys table to define the criteria for objects to be downloaded from Google Cloud Storage.   * Bucket name: type in the name   of the bucket from which you want to download objects. * Key: type in the key of the   object to be downloaded. * New name: type in a new name   for the object to be downloaded.   If you select the Use keys check box, the Key prefix and Delimiter fields as well as the Specify project ID check box and the Get files from bucket list check box will not be available. |
| Get files from bucket list | Select this check box and complete the Bucket table to define the criteria for objects to be downloaded from Google Cloud Storage.   * Bucket name: type in the name of   the bucket from which you want to download objects. * Key prefix: type in the prefix   to download objects whose keys start with the specified prefix   from the specified bucket. * Delimiter: specify the delimiter   to download those objects with key names up to the delimiter   from the specified bucket.   If you select the Get files from bucket list check box, the Key prefix and Delimiter fields as well as the Specify project ID check box and the Use keys check box will not be available. |
| Output directory | Specify the directory where you want to store the downloaded objects. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use a custom endpoint | Select this check box to use a private endpoint rather than the default one. When selected, enter the URL in the Google Storage Private API URL property, by respecting the following format: "https://storage.goggleapis.com".  For more information, see [Access Google APIs through endpoints](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis) from Google documentation.  This property is only available when you authenticate using Service account and Application Default Credentials. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used together with other Google Cloud Storage components, particularly tGSPut. |
