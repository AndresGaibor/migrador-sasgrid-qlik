<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/trandomforestmodel · versión 8.0 -->
# tRandomForestModel

Last updated: 9/30/2026

Analyzes feature vectors.

These vectors are usually pre-processed by tModelEncoder to generate a classifier model that is used by tPredict to classify given elements.

tRandomForestModel analyzes incoming datasets based on applying the Random Forest algorithm.

It generates a classification model out of this analysis and writes this model either in memory or in a given file system.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tRandomForestModel properties for Apache Spark Batch

These properties are used to configure tRandomForestModel running in the Spark Batch Job framework.

The Spark Batch
tRandomForestModel component belongs to the Machine Learning family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Label column | Select the input column used to provide classification labels. The records of this column are used as the class names (Target in terms of classification) of the elements to be classified. |
| Feature column | Select the input column used to provide features. Very often, this column is the output of the feature engineering computations performed by tModelEncoder. |
| Save the model on file system | Select this check box to store the model in a given file system. Otherwise, the model is stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn or the Spark Standalone mode, ensure that you have properly configured the connection in a configuration component in the same Job, such as tHDFSConfiguration. |
| Number of trees in the forest | Enter the number of decision trees you want tRandomForestModel to build.  Each decision tree is trained independently using a random sample of features.  Increasing this number can improve the accuracy by decreasing the variance in predictions, but will increase the training time. |
| Maximum depth of each tree in the forest | Enter the decision tree depth at which the training should stop adding new nodes. New nodes represent further tests on features on internal nodes and possible class labels held by leaf nodes.  For a tree of *n* depth, the number of internal nodes is *2n - 1*. For example, depth *1* means *1* internal node plus *2* leaf nodes.  Generally speaking, a deeper decision tree is more expressive and thus potentially more accurate in predictions, but it is also more resource consuming and prone to overfitting. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Subsampling rate | Enter the numeric value to indicate the fraction of the input dataset used for training each tree in the forest. The default value *1.0* is recommended, meaning to take the whole dataset for test. |
| Subset strategy | Select the strategy about how many features should be considered on each internal node in order to appropriately split this internal node (actually the training set or subset of a feature on this node) into smaller subsets. These subsets are used to build child nodes.  Each strategy takes a different number of features into account to find the optimal point among these features for split. This point could be, for example, the age *35* of the categorical feature *age*.  * auto: this strategy   is based on the number of trees you have set in the   Number of trees in the   forest field in the Basic settings view. This is   the default strategy to be used.  If the number of trees is *1*, the strategy is actually all; if this number is   greater than *1*, the strategy is   sqrt. * all: the total number   of features is considered for split. * sqrt: the number of   features to be considered is the square root of the total   number of features. * log2: the number of   features to be considered is the result of *log2(M)*,   in which *M* is the total number of   features. |
| Set Checkpoint Interval | Set the frequency of checkpoints. It is recommended to leave the default value (`10`).  Before setting a value for this parameter, activate checkpointing and set the checkpoint directory in the Spark Configuration tab of the Run view.  For further information about checkpointing, see [Logging and checkpointing the activities of your Apache Spark Job](/talend/en-US/components/8.0/spark-batch/logging-and-checkpointing-activities-of-your-apache-spark-job-spark-batch-component-if-you). |
| Max bins | Enter the numeric value to indicate the maximum number of bins used for splitting features.  The continuous features are automatically transformed to ordered discrete features. |
| Min info gain | Enter the minimum number of information gain to be expected from a parent node to its child nodes. When the number of information gain is less than this minimum number, node split is stopped.  The default value of the minimum number of information gain is *0.0*, meaning that no further information is obtained by splitting a given node. As a result, the splitting could be stopped.  For further information about how the information gain is calculated, see [Impurity and Information gain](http://spark.apache.org/docs/latest/mllib-decision-tree.html#node-impurity-and-information-gain) from the Spark documentation. |
| Min instances per node | Enter the minimum number of training instances a node should have to make it valid for further splitting.  The default value is *1*, which means when a node has only *1* row of training data, it stops splitting. |
| Impurity | Select the measure used to select the best split from each set of splits.   * gini: it is about how often an element could be   incorrectly labeled in a split. * entropy: it is about how unpredictable the information in   each split is.   For further information about how each of the measures is calculated, see [Impurity measures](http://spark.apache.org/docs/latest/mllib-decision-tree.html#node-impurity-and-information-gain) from the Spark documentation. |
| Set a random seed | Enter the random seed number to be used for bootstrapping and choosing feature subsets |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  You can accelerate the training process by adjusting the stopping conditions such as the maximum depth of each decision tree, the maximum number of bins of splitting or the minimum number of information gain, but note that the training that stops too early could impact its performance. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the classifier model you are generating with different sets of parameter values until you can obtain the best confusion matrix. But note that you need to write the evaluation code yourself to rank your model with scores.  You need to select the scores to be used depending on the algorithm you want to use to train your classifier model. This allows you to build the most relevant confusion matrix.  For examples about how the confusion matrix is used in a  Talend  Job for classification, see [Creating a classification model to filter spam](/talend/r/en-US/8.0/components/machine-learning/classification-model).  For a general explanation about confusion matrix, see <https://en.wikipedia.org/wiki/Confusion_matrix> from Wikipedia. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |

**Related tasks**  

* [Creating a classification model to filter spam](classification-model)
