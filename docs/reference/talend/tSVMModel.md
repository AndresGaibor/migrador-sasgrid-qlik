<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tsvmmodel · versión 8.0 -->
# tSVMModel

Last updated: 9/30/2026

Generates an SVM-based classifier model that can be used by
tPredict to classify given elements.

tSVMModel applies the SVM algorithm to
analyze feature vectors typically prepared and provided by tModelEncoder.

It generates a binary classification model out of this
analysis and writes this model in memory or in a file system supported by this
component, such as HDFS or S3.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSVMModel properties for Apache Spark Batch

These properties are used to configure tSVMModel running in the Spark Batch Job framework.

The Spark Batch
tSVMModel component belongs to the Machine Learning family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Label | Select the input column used to provide classification labels. The records of this column are used as the class names (Target in terms of classification) of the elements to be classified.  Since a SVM model is a binary classification model, only two classes are expected, that is to say, only two distinct values are expected from this column. |
| Vector to process | Select the input column used to provide features. Very often, this column is the output of the feature engineering computations performed by tModelEncoder. |
| Save the model on file system | Select this check box to store the model in a given file system. Otherwise, the model is stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn or the Spark Standalone mode, ensure that you have properly configured the connection in a configuration component in the same Job, such as tHDFSConfiguration. |
| Step size | Enter the size (numerical value) of the initial step of the gradient descent calculation. The default value *1.0* means that the whole data set is taken.  Selecting the best step size is often delicate in practice.  Generally speaking, when the feature points to be analyzed are very muddled, it is recommended to increase the step size in order to cover enough number of points in each iteration; however, bear in mind that too large a step size can improperly increase the time of each iteration.  On the other hand, the smaller the step size is, the more slowly the convergence occurs and a more accurate model you can expect. |
| Number of iterations | Enter the number of iterations you want the Job to perform to train the model. |
| Fraction of data to be used per iteration | Enter the fraction (expressed in decimal) of the input data to be used in each iteration to calculate the gradient.  The default value 1.0 means that the whole dataset is taken. |
| Regularization parameter | Enter the regularization number to used by the Updater function in order to avoid overfitting in learning. |
| Updater function | Select the function to calculate the form of the hyperplane that separates the two classes.  This function updates the weights of every point in each iteration so as to perform the gradient step in a given direction to form the hyperplane.  For example, in a 2-dimension space, this hyperplane can be a line or a set of lines if the points to be classified are linearly separable.  The available functions are:  * Simple: it does not use the   Regularization   parameter. * L1: it performs the L1   regularization. * Squared L2: it performs the   L2 regularization. |
| Gradient function | Select the loss function to calculate the margin between the hyperplane and the nearest point of either class.  For further information about the loss functions available on this drop-down list, see [Loss function for classification](https://en.wikipedia.org/wiki/Loss_functions_for_classification). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use feature scaling | If your training data cannot converge, select this check box to make tSVMModel reduce the condition numbers heuristically by scaling the feature data.  Reducing the condition numbers can often improve the convergence rate. |
| Intercept | Select this check box to allow the tSVMModel to automatically calculate the intercept constants and include them in the computation.  In general, intercept can guarantee that the residuals of your model have a mean of zero. |
| Validate data before training | Select this check box to check whether the vectors of the training data are well formatted before starting the training. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  You can accelerate the training process by adjusting the stopping conditions such as the maximum number of iterations or the step size but note that the training that stops too early could impact its accuracy. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the classifier model you are generating with different sets of parameter values until you can obtain the best confusion matrix. But note that you need to write the evaluation code yourself to rank your model with scores.  You need to select the scores to be used depending on the algorithm you want to use to train your classifier model. This allows you to build the most relevant confusion matrix.  For examples about how the confusion matrix is used in a  Talend  Job for classification, see [Creating a classification model to filter spam](/talend/r/en-US/8.0/components/machine-learning/classification-model).  For a general explanation about confusion matrix, see <https://en.wikipedia.org/wiki/Confusion_matrix> from Wikipedia. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
