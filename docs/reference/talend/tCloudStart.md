<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/cloud/tcloudstart · versión 8.0 -->
# tCloudStart

Last updated: 9/30/2026

Starts instances on Amazon EC2 (Amazon Elastic Compute Cloud).

This component accesses the cloud provider to be used (Amazon EC2)
and launches instances, which are virtual servers in that cloud. If
an instance to be launched does not exist, tCloudStart creates it.

## tCloudStart Standard properties

These properties are used to configure tCloudStart running in the Standard Job framework.

The Standard
tCloudStart component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Access key and Secret key | Enter or paste the access key and the secret key required by Amazon to authenticate your requests to its web services. These access credentials are generated from the Security Credential tab of your Amazon account page.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Cloud provider | Select the cloud provider to be used. |
| Image | Enter the name of the Amazon Machine Image (AMI) to be used to launch an instance. This AMI defines the basic configuration of that instance. |
| Region and Zone | Enter the region and the zone to be used as the geographic location where you want to launch an instance.  The syntax used to express a location is predefined by Amazon, for example, *us-east-1* representing the *US East (Northern Virginia)* region and *us-east-1a* representing one of the Availability Zones within that region. For further information about available regions for Amazon, see Amazon's documentation about regions and endpoints and as well Amazon's FAQ about region and Availability Zone. |
| Instance name | Enter the name of the instance to be launched. For example, you can enter *Talend*.  Note that the upper letter will be converted to lower letter. |
| Instance count | Enter the number of instances to be launched. At runtime, the name specified in the Instance name field, for example *Talend*, will be used as the initial part of each instance name, and letters and numbers will be randomly added to complete each name. |
| Instance type | Select the type of the instance(s) to be launched. Each type is predefined by Amazon and defines the performance of every instance you want to launch.  This drop-down list presents the API name of each instance type. For further information, see Amazon's documentation about instance types. |
| Proceed with a Key pair | Select this check box to use Amazon Key Pair for your login to Amazon EC2. Once selecting it, a drop-down list appears to allow you to select :  * Use an existing Key Pair to   enter the name of that Key Pair in the field next to the drop-down   list. If required, Amazon will prompt you at runtime to find and use   that Key Pair. * Create a Key Pair to enter the   name of the new Key Pair in the field next to the drop-down list and   define the location where you want to store this Key Pair in the   Advanced settings tab   view. |
| Security group | Add rows to this table and enter the names of the security groups to which you need to assign the instance(s) to be launched. The security groups set in this table must exist on your Amazon EC2.  A security group applies specific rules on inbound traffic to instances assigned to the group, such as the ports to be used. For further information about security groups, see Amazon's documentation about security groups.  Note that an instance can be assigned to a group by setting its security group name or key pair name to `jclouds#<$group_name>`, where `<$group_name>` identifies the group to which the instance belongs. In this way, you can change the status of all instances or running instances in one group at the same time using the tCloudStop component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Key Pair folder | Browse to, or enter the path to the folder you use to store the created Key Pair file.  This field appears when you select Creating a Key Pair in the Basic settings tab view. |
| Volumes | Add rows and define the volume(s) to be created for the instances to be launched in addition to the volumes predefined and allocated by the given Amazon EC2.  The parameters to be set in this table are the same parameters used by Amazon for describing a volume.  If you need to remove automatically an additional volume after terminating its related instance, select the check box in the Delete on termination column. |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NODE\_GROUP: the name of the instance. This is an After variable and it returns a string.  NODES: the instances launched. This is an After variable and it returns an object.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component works standalone to launch an instance on Amazon EC2. You can use this component to start the instance you need to deploy Jobs on. |
