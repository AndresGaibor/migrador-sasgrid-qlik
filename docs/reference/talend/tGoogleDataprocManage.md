<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-dataproc/tgoogledataprocmanage · versión 8.0 -->
# tGoogleDataprocManage

Last updated: 9/30/2026

Creates or deletes a Dataproc cluster in the Global region on Google Cloud
Platform.

## tGoogleDataprocManage Standard properties

These properties are used to configure tGoogleDataprocManage running in the Standard Job framework.

The Standard
tGoogleDataprocManage component belongs to the Cloud family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Project ID | Enter the ID of your Google Cloud Platform project.  If you are not certain about your project ID, confirm it in the Manage Resources page of your Google Cloud Platform services. |
| Cluster ID | Enter the ID of your Dataproc cluster to be used. |
| Provide Google Credentials in file | Leave this check box clear, when you launch your Job from a given machine in which Google Cloud SDK has been installed and authorized to use your user account credentials to access Google Cloud Platform. In this situation, this machine is often your local machine.  When you launch your Job from a remote machine, such as a Talend JobServer, select this check box and in the Path to Google Credentials file field that is displayed, enter the directory in which this JSON file is stored in the Talend JobServer machine. You can also click the [...] button, and then in the pop-up dialog box, browse for the JSON file.  For further information about this Google Credentials file, see the administrator of your Google Cloud Platform or visit [Google Cloud Platform Auth Guide](https://cloud.google.com/docs/authentication). |
| Action | Select the action you want tGoogleDataprocManage to perform on the your cluster:  * `Start` to create a cluster * `Stop` to destroy a cluster |
| Version | Select the version of the image to be used to create a Dataproc cluster. |
| Region | From this drop-down list, select the Google Cloud region to be used. |
| Zone | Select the geographic zone in which the computing resources are used and your data is stored and processed. The available zones vary depending on the region you have selected from the Regional drop-down list.  A zone in terms of Google Cloud is an isolated location within a region, another geographical term employed by Google Cloud. |
| Instance configuration | Enter the parameters to determine how many masters and workers to be used by the Dataproc cluster to be created and the performance of these masters and workers. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Wait for cluster ready | Select this check box to keep this component running until the cluster is completely set up.  When you clear this check box, this component stops running immediately after sending the command to create. |
| Master disk size | Enter a number without quotation marks to determine the size of the disk of each master instance. |
| Master local SSD | Enter a number without quotation marks to determine the number of local solid-state drive (SSD) storage devices to be added to each master instance.  According to Google, these local SSDs are suitable only for temporary storage such as caches, processing space or low value data. It is recommended to store important data to durable storage options of Google. For further information about the Google storage options, see [Durable storage options](https://cloud.google.com/compute/docs/disks/). |
| Worker disk size | Enter a number without quotation marks to determine the size of the disk of each worker instance. |
| Worker local SSD | Enter a number without quotation marks to determine the number of local solid-state drive (SSD) storage devices to be added to each worker instance.  According to Google, these local SSDs are suitable only for temporary storage such as caches, processing space or low value data. It is recommended to store important data to durable storage options of Google. For further information about the Google storage options, see [Durable storage options](https://cloud.google.com/compute/docs/disks/). |
| Network or Subnetwork | Select either check box to use a Google Compute Engine network or subnetwork for the cluster to be created to enable intra-cluster communications.  As Google does not allow network and subnetwork to be used concurrently, selecting one check box hides the other check box.  For further information about Google Dataproc cluster network configuration, see [Dataproc Network](https://cloud.google.com/dataproc/docs/concepts/network). |
| Internal IP only | Select the check box to configure all instances in the cluster to have only internal IP addresses.  The subnetwork of the cluster must have Private Google Access enabled to allow cluster nodes to access Google APIs and services from internal IPs.  For more information, see [Dataproc Cluster Network Configuration](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/network#create_a_cloud_dataproc_cluster_with_internal_ip_address_only). |
| Initialization action | In this table, select the initialization actions that are available in the shared bucket on Google Cloud Storage to run on all the nodes in your Dataproc cluster immediately after this cluster is set up.  If you need to use custom initialization scripts, upload them to this shared Google bucket so that tGoogleDataprocManage can read them.   * In the Executable file column, enter the   Google Cloud Storage URI to these scripts to be used, for example   gs://dataproc-initialization-actions/MyScript * In the Executable timeout column, enter the   amount of time in double quotation marks to determine the duration   of the execution. If the executable is not completed at the end of   this timeout, an explanatory error message is returned. The value is   a string with up to nine fractional digits, for example,   "3.5s" for 3.5 seconds.   For further information about this shared bucket and the initialization actions, see [Initialization actions](https://cloud.google.com/dataproc/docs/concepts/init-actions). |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used standalone in a subJob. |
