<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage · versión 8.0 -->
# tAmazonEMRManage

Last updated: 9/30/2026

Launches or terminates a cluster on Amazon EMR (Elastic MapReduce).

## tAmazonEMRManage Standard properties

These properties are used to configure
tAmazonEMRManage running in the Standard Job framework.

The
Standard
tAmazonEMRManage component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Access key and Secret key | Specify the access keys (the access key ID in the Access key field and the secret access key in the Secret key field) required to access the Amazon Web Services. For more information on AWS access keys, see [Access keys (access key ID and secret access key)](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Inherit credentials from AWS role | Select this checkbox to leverage the instance profile credentials. The credentials can be used on Amazon EC2 instances or AWS ECS, and are delivered through the Amazon EC2 metadata service. To use this option, your Job must be running within Amazon EC2 or other services that can leverage IAM Roles for access to resources. For more information, see [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session. |
| Action | Select an action to be performed from the list, either Start or Stop.  * Start: launch an Amazon EMR   cluster. * Stop: terminate an Amazon   EMR cluster. |
| Region | Specify the AWS region by selecting a region name from the list or entering a region between double quotation marks (for example *"us-east-1"*). For more information about how to specify the AWS region, see [Choose an AWS Region](http://docs.aws.amazon.com/ElasticMapReduce/latest/ManagementGuide/emr-plan-region.html). |
| Cluster name | Enter the name of the cluster. |
| Cluster version | Select the version of the cluster.  You can also select the Customize Version and Application check box on the Advanced settings view to customize the cluster version information.  This property is not available when the Customize Version and Application check box is selected. |
| Application | Select the applications to be installed on the cluster.  You can also select the Customize Version and Application check box on the Advanced settings view to customize the applications information.  This property is available when an EMR version is selected from the Cluster version list and the Customize Version and Application check box is cleared. |
| Service role | Enter the IAM (Identity and Access Management) role for the Amazon EMR service. The default role is *EMR\_DefaultRole*. To use this default role, you must have already created it. |
| Job flow role | Enter the IAM role for the EC2 instances that Amazon EMR manages. The default role is *EMR\_EC2\_DefaultRole*. To use this default role, you must have already created it. |
| Enable log | Select this check box to enable logging and in the field displayed specify the path to a folder in an S3 bucket where you want Amazon EMR to write the log data. |
| Use EC2 key pair | Select this check box to associate an Amazon EC2 (Elastic Compute Cloud) key pair with the cluster and in the field displayed enter the name of your EC2 key pair. |
| Predicate | Specify the cluster(s) that you want to stop:  * All running clusters: all   running clusters will be stopped. * All running clusters with predefined   name: the running cluster with a given name   will be stopped. In the Cluster name field   displayed, you need to specify the name of the cluster to be   stopped. * Running cluster with predefined   id: the running cluster with a given ID will   be stopped. In the Cluster id field displayed,   you need to specify the ID of the cluster to be stopped.  This list is available only when Stop is selected from the Action list. |
| Instance count | Enter the number of Amazon EC2 instances to initialize.  This field is available only if you select Start from the Action drop-down list in the Basic settings view and if the Use multiple master nodes check box is cleared. |
| Slave instance count | Enter the number of Amazon EC2 slave instances to initialize.  This field is available only if you select Start from the Action drop-down list in the Basic settings view and if you select the Use multiple master nodes check box in the Advanced settings view. |
| Master instance type | Select the type of the master instance to initialize. |
| Slave instance type | Select the type of the slave instance to initialize. |

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
| Wait for cluster ready | Select this check box to let your Job wait until the launch of the cluster is completed. |
| Visible to all users | Select this check box to make the cluster visible to all IAM users. |
| Termination Protect | Select this check box to enable termination protection to prevent instances in the cluster from shutting down due to errors or issues during processing. |
| Enable debug | Select this check box to enable the debug mode. |
| Customize Version and Application | Select this check box to customize the version of the cluster and the applications to be installed on the cluster.   * Cluster   version: enter the version of the cluster. * Applications: click the [+] button below the table to   add as many rows as needed, each row for an application, and   specify the application by clicking the right side of the cell   and selecting the application from the drop-down list displayed,   or just entering the application name in the cell if it is not   in the list. |
| Use multiple master nodes | Select this check box to enable high availability and launch a cluster with multiple master nodes with the Amazon EMR distribution in version 5.23 or later. Information noteImportant: If you select this check box, you must specify the identifier of the Amazon VPC subnet in the Subnet id field. |
| Subnet id | Specify the identifier of the Amazon VPC (Virtual Private Cloud) subnet where you want the Job flow to launch. |
| Availability Zone | Specify the availability zone for your cluster's EC2 instances. |
| Master security group | Specify the security group for the master instance. |
| Additional master security groups | Specify additional security groups for the master instance and separate them with a comma, for example, *gname1, gname2, gname3*. |
| Slave security group | Specify the security group for the slave instances. |
| Additional slave security groups | Specify additional security groups for the slave instances and separate them with a comma, for example, *gname1, gname2, gname3*. |
| Service Access Security Group | Specify the identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnet.  For how to create a private subnet to enable service access security group on Amazon EMR, see [Scenario 2: VPC with Public and Private Subnets (NAT)](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario2.html). |
| Actions | Specify the bootstrap actions associated with the cluster, by clicking the [+] button below the table to add as many rows as needed, each row for a bootstrap action, and setting the following parameters for each action:   * Name: enter the name of the   bootstrap action. * Script location: specify the   location of the script run by the bootstrap action, for example,   *s3://ap-northeast-1.elasticmapreduce/bootstrap-actions/run-if*. * Arguments: enter the list of   command line arguments (separated by commas) passed to the   bootstrap action script, for example, *"arg0","arg1","arg2"*.   For more information about the bootstrap actions, see [BootstrapActionConfig](http://docs.aws.amazon.com/ElasticMapReduce/latest/API/API_BootstrapActionConfig.html). |
| Steps | Specify the Job flow step(s) to be invoked on the cluster after its launch, by clicking the [+] button below the table to add as many rows as needed, each row for a step, and setting the following parameters for each step:   * Name: enter the name of the job   flow step. * Action on Failure: click the   cell and from the drop-down list select the action to take if   the Job flow step fails. * Main Class: enter the name of   the main class in the specified Java file. If not specified, the   JAR file should specify a Main-Class in its manifest file. * Jar: enter the path to the JAR   file run during the step, for example, *"s3://inputjar/test.jar"*. * Args: enter the list of command   line arguments (separated by commas) passed to the JAR file's   main function when executed, for example, *"arg0","arg1","arg2"*.   For more information about the Job flow steps, see [StepConfig](http://docs.aws.amazon.com/ElasticMapReduce/latest/API/API_StepConfig.html). |
| Keep alive after steps complete | Select this check box to keep the job flow alive after completing all steps. |
| Wait for steps to complete | Select this check box to let your Job wait until the Job flow steps are completed.  This check box is available only when the Wait for cluster ready check box is selected. |
| Properties | Specify the classification and property information supplied to the configuration object of the EMR cluster to be created, by clicking the [+] button below the table to add as many rows as needed, each row for a property, and setting the following parameters:   * Classification: specify the   classification of the configuration. * Key: enter the key of the   property. * Value: enter the value of the   property.   This field is available only if you select Start from the Action drop-down list in the Basic settings view and if the Use multiple master nodes check box is cleared. |
| Properties in JSON | Enter, in JSON format, the classification and property information supplied to the configuration object of the EMR clusters to be created.  This field is available only if you select Start from the Action drop-down list in the Basic settings view and if you select the Use multiple master nodes check box in the Advanced settings view. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| CLUSTER\_FINAL\_ID | The ID of the cluster. This is an After variable and it returns a string. |
| CLUSTER\_FINAL\_NAME | The name of the cluster. This is an After variable and it returns a string. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | tAmazonEMRManage is usually used as a standalone component. |

**Related concepts**  

* [Managing an Amazon EMR cluster](tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-managing-amazon-emr-cluster-standard-component "Here's an example of using Talend components to manage an Amazon EMR cluster.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-managing-amazon-emr-cluster-standard-component -->
# Managing an Amazon EMR cluster

Last updated: 9/30/2026

Here's an example of using Talend components
to manage an Amazon EMR cluster.

### In this section

* [Creating an Amazon EMR cluster management Job](/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-creating-amazon-emr-cluster-management-job-standard-component-create)
* [Starting a new Amazon EMR cluster](/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-starting-new-amazon-emr-cluster-standard-component)
* [Resizing the Amazon EMR cluster by adding a new task instance group](/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-resizing-amazon-emr-cluster-by-adding-new-task-instance-group-standard-component)
* [Listing the instance groups in the Amazon EMR cluster](/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-listing-instance-groups-in-amazon-emr-cluster-standard-component)
* [Executing the Job to manage the Amazon EMR cluster](/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-executing-job-to-manage-amazon-emr-cluster-standard-component-press)

**Related reference**  

* [tAmazonEMRManage](tamazonemrmanage "Launches or terminates a cluster on Amazon EMR (Elastic MapReduce).")
* [tAmazonEMRResize](tamazonemrresize "Adds or resizes a task instance group in a cluster on Amazon EMR (Elastic MapReduce).")
* [tAmazonEMRListInstances](tamazonemrlistinstances "Lists the details about the instance groups in a cluster on Amazon EMR (Elastic MapReduce).")

**Related information**  

* [tJava](/talend/en-US/components/8.0/java-custom-code/tjava)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-creating-amazon-emr-cluster-management-job-standard-component-create -->
# Creating an Amazon EMR cluster management Job

Last updated: 9/30/2026

Create a Job to start a new Amazon EMR cluster, then resize the
cluster, and finally list the ID and name information of the instance groups in the
cluster.

## Procedure

1. Create a new Job and add a tAmazonEMRManage component, a tAmazonEMRResize component, a tAmazonEMRListInstances component, and a tJava component by typing their names in the design workspace or
   dropping them from the Palette.
2. Link the tAmazonEMRManage component to
   the tAmazonEMRResize component using a Trigger > OnSubjobOk
   connection.
3. Link the tAmazonEMRResize component to
   the tAmazonEMRListInstances component using a
   Trigger > OnSubjobOk connection.
4. Link the tAmazonEMRListInstances
   component to the tJava component using a Row > Iterate
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-executing-job-to-manage-amazon-emr-cluster-standard-component-press -->
# Executing the Job to manage the Amazon EMR cluster

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the
Job for managing Amazon EMR cluster, you can then execute the Job and verify the Job
execution result.

## Procedure

1. Press Ctrl + S to save the Job and
   then F6 to execute the Job.

   As shown above, the Job starts and resizes the Amazon EMR
   cluster, and then lists all instance groups in the cluster.
2. View the cluster details on the Amazon EMR Cluster List page to
   validate the Job execution result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-listing-instance-groups-in-amazon-emr-cluster-standard-component -->
# Listing the instance groups in the Amazon EMR cluster

Last updated: 9/30/2026

Configure the tAmazonEMRListInstances component and the tJava component to retrieve and display the ID and name information of all
instance groups in a running cluster.

## Procedure

1. Double-click the tAmazonEMRListInstances component to open its Basic settings view.
2. In the Access Key and Secret Key fields, enter the authentication credentials
   required to access Amazon S3.
3. Select the AWS region from the Region
   drop-down list. In this example, it is *Asia Pacific
   (Tokyo)*.
4. Clear the Filter master and core
   instances check box to list all instance groups, including the
   Master, Core, and Task type instance groups.
5. In the Cluster id field, enter the ID
   of the cluster for which to list the instance groups. In this example, the returned
   value of the global variable *CLUSTER\_FINAL\_ID* of the previous
   tAmazonEMRManage component is used.
6. Double-click the tJava component to
   open its Basic settings view.
7. In the Code field, enter the following
   code to print the ID and Name information of each instance group in the
   cluster.

   ```
   System.out.println("\r\n===== Instance Group =====");
   System.out.println("Instance Group ID:    " + (String)globalMap.get("tAmazonEMRListInstances_1_CURRENT_GROUP_ID"));
   System.out.println("Instance Group Name:  " + (String)globalMap.get("tAmazonEMRListInstances_1_CURRENT_GROUP_NAME"));
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-resizing-amazon-emr-cluster-by-adding-new-task-instance-group-standard-component -->
# Resizing the Amazon EMR cluster by adding a new task instance group

Last updated: 9/30/2026

Configure the tAmazonEMRResize
component to resize a running Amazon EMR cluster by adding a new task instance
group.

## Procedure

1. Double-click the tAmazonEMRResize
   component to open its Basic settings view.
2. In the Access Key and Secret Key fields, enter the authentication credentials
   required to access Amazon S3.
3. From the Action drop-down list, select
   Add task instance group to resize the cluster
   by adding a new task instance group.
4. In the Cluster id field, enter the ID
   of the cluster to be resized. In this example, the returned value of the global
   variable *CLUSTER\_FINAL\_ID* of the previous tAmazonEMRManage component is used.

   Note that you can retrieve the global variable by pressing Ctrl + Space and selecting the relevant global variable
   from the list.
5. In the Group name field, enter the
   name of the task instance group to be added in the cluster. In this example, it is
   *talend-doc-instance-group*.
6. In the Instance count field, specify
   the number of the instances to be created.
7. From the Task instance type drop-down
   list, select the type of the instances to be created.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-emr/tamazonemrmanage-tamazonemrresize-tamazonemrlistinstances-tjava-starting-new-amazon-emr-cluster-standard-component -->
# Starting a new Amazon EMR cluster

Last updated: 9/30/2026

Configure the tAmazonEMRManage
component to start a new Amazon EMR cluster.

## Procedure

1. Double-click the tAmazonEMRManage
   component to open its Basic settings view.
2. In the Access Key and Secret Key fields, enter the authentication credentials
   required to access Amazon S3.
3. From the Action list, select Start to start a cluster.
4. Select the AWS region from the Region
   drop-down list. In this example, it is *Asia Pacific
   (Tokyo)*.
5. In the Cluster name field, enter the
   name of the cluster to be started. In this example, it is
   *talend-doc-emr-cluster*.
6. From the Cluster version and Application drop-down list, select the version of the
   cluster and the application to be installed on the cluster.
7. Select the Enable log check box and in
   the field displayed, specify the path to a folder in an S3 bucket where you want
   Amazon EMR to write the log data. In this example, it is
   *s3://talend-doc-emr-bucket*.
