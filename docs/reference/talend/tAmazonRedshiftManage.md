<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tamazonredshiftmanage · versión 8.0 -->
# tAmazonRedshiftManage

Last updated: 9/30/2026

Manages Amazon Redshift clusters and snapshots.

tAmazonRedshiftManage manages the work of creating a new Amazon
Redshift cluster, creating a snapshot of an Amazon Redshift cluster, resizing an
existing Amazon Redshift cluster, and deleting an existing cluster or snapshot.

## tAmazonRedshiftManage Standard properties

These properties are used to configure tAmazonRedshiftManage running in the Standard Job framework.

The Standard
tAmazonRedshiftManage component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Access Key and Secret Key | Specify the access keys (the access key ID in the Access key field and the secret access key in the Secret key field) required to access the Amazon Web Services. For more information on AWS access keys, see [Access keys (access key ID and secret access key)](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Inherit credentials from AWS role | Select this checkbox to leverage the instance profile credentials. These credentials can be used on Amazon EC2 instances, and are delivered through the Amazon EC2 metadata service. To use this option, your Job must be running within Amazon EC2 or other services that can leverage IAM Roles for access to resources. For more information, see [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session. |
| Action | Select an action to be performed from the list.  * Create cluster: create a new Amazon Redshift cluster. * Delete cluster: delete a previously provisioned Amazon Redshift cluster. * Resize cluster: resize an existing Amazon Redshift cluster. * Pause cluster: pause an existing Amazon Redshift cluster. * Resume cluster: resume a paused Amazon Redshift cluster. * Restore from snapshot: create a new Amazon Redshift cluster from a snapshot. * Delete snapshot: delete the specified manual snapshot. |
| Region | Specify the AWS region by selecting a region name from the list or entering a region between double quotation marks (e.g. *"us-east-1"*) in the list. For more information about the supported AWS regions where you can provision an Amazon Redshift cluster, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region). |
| Create snapshot | Select this check box to create a final snapshot of the Amazon Redshift cluster before it is deleted.  This check box is available only when Delete cluster is selected from the Action list. |
| Snapshot id | Enter the identifier of the snapshot.  This field is available when:  * Delete cluster is selected from the Action list and the Create snapshot check box is selected. * Restore from snapshot or Delete snapshot is selected from the Action list. |
| Cluster id | Enter the ID of the cluster.  This field is available when Create cluster, Delete cluster, Resize cluster, or Restore from snapshot is selected from the Action list. |
| Database | Enter the name of the first database to be created when the cluster is created.  This field is available only when Create cluster is selected from the Action list. |
| Port | Enter the port number on which the cluster accepts connections.  This field is available when Create cluster or Restore from snapshot is selected from the Action list. |
| Master username and Master password | The user name and the password associated with the master user account for the cluster to be created.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  The two fields are available only when Create cluster is selected from the Action list. |
| Node type | Select the node type for the cluster.  This list is available when Create cluster, Resize cluster, or Restore from snapshot is selected from the Action list. |
| Node count | Enter the number of compute nodes in the cluster.  This field is available only when Create cluster or Resize cluster is selected from the Action list. |

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
| Wait for cluster ready | Select this check box to let your Job wait until the launch of the cluster is completed.  This check box is available when Create cluster, Restore from snapshot, or Resume cluster is selected from the Action list. |
| Original cluster id of snapshot | Enter the name of the cluster the source snapshot was created from.  This field is available when Restore from snapshot or Delete snapshot is selected from the Action list. |
| Parameter group name | Enter the name of the parameter group to be associated with the cluster.  This field is available when Create cluster or Restore from snapshot is selected from the Action list. |
| Subnet group name | Enter the name of the subnet group where you want the cluster to be restored.  This field is available when Create cluster or Restore from snapshot is selected from the Action list. |
| Publicly accessible | Select this check box so that the cluster can be accessed from a public network.  This check box is available when Create cluster or Restore from snapshot is selected from the Action list. |
| Set public ip address | Select this check box and in the field displayed enter the Elastic IP (EIP) address for the cluster.  This check box is available only when the Publicly accessible check box is selected. |
| Availability zone | Enter the EC2 Availability Zone in which you want Amazon Redshift to provision the cluster.  This field is available when Create cluster or Restore from snapshot is selected from the Action list. |
| VPC security group ids | Enter Virtual Private Cloud (VPC) security groups to be associated with the cluster and separate them with a comma, for example, *gname1, gname2, gname3*.  This field is available when Create cluster or Restore from snapshot is selected from the Action list. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | CLUSTER\_FINAL\_ID: the ID of the cluster. This is an After variable and it returns a string.  ENDPOINT: the endpoint address of the cluster. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tAmazonRedshiftManage is usually used as a standalone component. |
