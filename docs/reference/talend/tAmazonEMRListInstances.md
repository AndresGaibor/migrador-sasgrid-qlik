<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrlistinstances · versión 8.0 -->
# tAmazonEMRListInstances

Last updated: 9/30/2026

Lists the details about the instance groups in a cluster on Amazon EMR (Elastic
MapReduce).

## tAmazonEMRListInstances Standard properties

These properties are used to configure
tAmazonEMRListInstances running in the
Standard Job framework.

The
Standard
tAmazonEMRListInstances component belongs to the
Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Access key and Secret key | Specify the access keys (the access key ID in the Access key field and the secret access key in the Secret key field) required to access the Amazon Web Services. For more information on AWS access keys, see [Access keys (access key ID and secret access key)](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Inherit credentials from AWS role | Select this checkbox to leverage the instance profile credentials. These credentials can be used on Amazon EC2 instances, and are delivered through the Amazon EC2 metadata service. To use this option, your Job must be running within Amazon EC2 or other services that can leverage IAM Roles for access to resources. For more information, see [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session. |
| Region | Specify the AWS region by selecting a region name from the list or entering a region between double quotation marks (for example *"us-east-1"*). For more information about how to specify the AWS region, see [Choose an AWS Region](http://docs.aws.amazon.com/ElasticMapReduce/latest/ManagementGuide/emr-plan-region.html). |
| Filter master and core instances | Select this check box to ignore the master and core instance groups and list only the task instance groups. |
| Cluster id | Enter the ID of the cluster for which you want to list the instance groups. |

## Advanced settings

| Properties | Description |
| --- | --- |
| STS Endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This checkbox is available only when the Assume role checkbox is selected. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | CURRENT\_GROUP\_ID: the ID of the current instance group. This is an After variable and it returns a string.  CURRENT\_GROUP\_NAME: the name of the current instance group. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tAmazonEMRListInstances is usually used as a start component of a Job or subJob. |

**Related concepts**  

* [Managing an Amazon EMR cluster](tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-managing-amazon-emr-cluster-standard-component "Here's an example of using Talend components to manage an Amazon EMR cluster.")
