<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tlogisticregressionmodel · versión 8.0 -->
# tLogisticRegressionModel

Last updated: 9/30/2026

Analyzes feature vectors usually pre-processed by tModelEncoder to generate a classifier model that is used
by tPredict to classify given elements.

tLogisticRegressionModel analyzes
incoming datasets based on applying the Logistic Regression algorithm.

It generates a classification model out of this analysis
and writes this model either in memory or in a given file system.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tLogisticRegressionModel properties for Apache Spark Batch

These properties are used to configure tLogisticRegressionModel running in the Spark Batch Job framework.

The Spark Batch
tLogisticRegressionModel component belongs to the Machine Learning family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Label column | Select the input column used to provide classification labels. The records of this column are used as the class names (Target in terms of classification) of the elements to be classified. |
| Feature column | Select the input column used to provide features. Very often, this column is the output of the feature engineering computations performed by tModelEncoder. |
| Save the model on file system | Select this check box to store the model in a given file system. Otherwise, the model is stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn or the Spark Standalone mode, ensure that you have properly configured the connection in a configuration component in the same Job, such as tHDFSConfiguration. |
| ElasticNet mixing parameter | Enter the ElasticNet coefficient (numerical value) used for the regularization calculation in order to control the bias/variance trade-off in feature selection. ElasticNet is the combination of L1 regularization and L2 regularization.  The value to be put varies between 0.0 and 1.0, indicating the weights of the L1 regularization and the L2 regularization in the ElasticNet combination. When the value is 0.0, the regularization is actually equivalent to the L2 regularization; when the value is 1.0, it is equivalent to the L1 regularization.  For further information about how ElasticNet is implemented in Spark, see [ML linear methods](http://spark.apache.org/docs/latest/ml-linear-methods.html), in which the related formula shows how the value you put (*α* in that formula) is used to calculate the ElasticNet regularization.  For further information about ElasticNet, see [Regularization and variable selection via the elastic net](http://web.stanford.edu/~hastie/Papers/B67.2%20%282005%29%20301-320%20Zou%20&%20Hastie.pdf). |
| Fit an intercept term | Select this check box to allow the tLogisticRegressionModel to automatically calculate the intercept constants and include them in the regression computation.  In general, intercept should present to guarantee that the residuals of your model have a mean of zero. |
| Maximum number of iterations | Enter the number of iterations you want the Job to perform to train the model. |
| Regularization | Enter the regularization coefficient (numerical value) to be used along with ElasticNet for the regularization calculation.  For further information about how this parameter is implemented in Spark, see [ML linear methods](http://spark.apache.org/docs/latest/ml-linear-methods.html), in which the related formula shows how the value you put (*λ* in that formula) is used to calculate the eventual regularization. |
| Threshold | Enter the threshold (numerical value and ranging between 0.0 and 1.0) used to separate the positive predictions from the negative predictions. An element about which the prediction score (the odds of being a case) is greater or equal to this threshold will be identified as positive, and negative otherwise.  The default threshold is *0.5*. |
| Convergence tolerance | Enter the convergence score which the iterations are expected to obtain.  In general, smaller value will result in higher accuracy in the prediction at the cost of more iterations.  But note that in some cases, your model may not be able to reach the convergence you put despite of whatever number of iterations you want the Job to perform. This failure to converge might indicate that the convergence score you use is not realistic to the features you are processing and therefore, you need to process these features to a greater degree. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  You can accelerate the training process by adjusting the stopping conditions such as the maximum number of iterations, the threshold or the convergence tolerance but note that the training that stops too early could impact its performance. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the classifier model you are generating with different sets of parameter values until you can obtain the best confusion matrix. But note that you need to write the evaluation code yourself to rank your model with scores.  You need to select the scores to be used depending on the algorithm you want to use to train your classifier model. This allows you to build the most relevant confusion matrix.  For examples about how the confusion matrix is used in a  Talend  Job for classification, see [Creating a classification model to filter spam](/talend/r/en-US/8.0/components/machine-learning/classification-model).  For a general explanation about confusion matrix, see <https://en.wikipedia.org/wiki/Confusion_matrix> from Wikipedia. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
