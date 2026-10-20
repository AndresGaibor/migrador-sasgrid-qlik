<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tlinearregressionmodel · versión 8.0 -->
# tLinearRegressionModel

Last updated: 9/30/2026

Builds a linear regression model using a training
dataset.

This component analyzes feature vectors usually prepared and provided by
tModelEncoder to generate a linear regression
model that expresses how an outcome is dependent on a given set of features. Then
tPredict uses this model to predict the outcome
ofthe same type of features it receives.

This model can be used directly in the same Job or written
to a file system for later use.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tLinearRegressionModel properties for Apache Spark Batch

These properties are used to configure tLinearRegressionModel running in the Spark Batch Job framework.

The Spark Batch
tLinearRegressionModel component belongs to the Machine Learning family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Label column | Select the input column used to provide Double-type labels (values of the dependent variable in terms of linear regression). The records of this column are used as the potential situations (the variation of the dependent variable in terms of linear regression) a given element could fall into. |
| Feature column | Select the input column used to provide Vector-type features (values of the independent or explanatory variable in terms of linear regression). Very often, this column is the output of the feature engineering computations performed by tModelEncoder. |
| Save the model on file system | Select this check box to store the model in a given file system. Otherwise, the model is stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn or the Spark Standalone mode, ensure that you have properly configured the connection in a configuration component in the same Job, such as tHDFSConfiguration. |
| ElasticNet mixing parameter | Enter the ElasticNet coefficient (numerical value) used for the regularization calculation in order to control the bias/variance trade-off in feature selection. ElasticNet is the combination of L1 regularization and L2 regularization.  The value to be put varies between 0.0 and 1.0, indicating the weights of the L1 regularization and the L2 regularization in the ElasticNet combination. When the value is 0.0, the regularization is actually equivalent to the L2 regularization; when the value is 1.0, it is equivalent to the L1 regularization.  For further information about how ElasticNet is implemented in Spark, see [ML linear methods](http://spark.apache.org/docs/latest/ml-classification-regression.html), in which the related formula shows how the value you put (*α* in that formula) is used to calculate the ElasticNet regularization.  For further information about ElasticNet, see [Regularization and variable selection via the elastic net](http://web.stanford.edu/~hastie/Papers/B67.2%20%282005%29%20301-320%20Zou%20&%20Hastie.pdf). |
| Fit an intercept term | Select this check box to let tLinearRegressionModel automatically calculate the intercept constants and include them in the regression computation.  In general, intercept should be present to guarantee that the residuals of your model have a mean of zero. |
| Standardize features before fitting model | Select this check box to scale the features to make them normally distributed. |
| Maximum number of iterations | Enter the number of iterations you want the Job to perform to train the model. |
| Regularization | Enter the regularization coefficient (numerical value) to be used along with ElasticNet for the regularization calculation.  For further information about how this parameter is implemented in Spark, see [ML linear methods](http://spark.apache.org/docs/latest/ml-classification-regression.html), in which the related formula shows how the value you put (*λ* in that formula) is used to calculate the eventual regularization. |
| Convergence tolerance | Enter the convergence score which the iterations are expected to obtain.  In general, smaller value will result in higher accuracy in the prediction at the cost of more iterations.  In some cases, your model may not be able to reach the convergence you put despite of whatever number of iterations you want the Job to perform. This failure to converge might indicate that the convergence score you use is not realistic to the features you are processing and therefore, you need to process these features to a greater degree. |
| Solver algorithm | Select the algorithm used for optimization.   * Normal: this algorithm uses   normal equations. * L-BFGS: this algorithm   approximates the BFGS algorithm using a limited amount of   computer memory. * Auto: the component select   either of the above-mentioned algorithms. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  You can accelerate the training process by adjusting the stopping conditions such as the maximum number of iterations or the convergence tolerance but note that the training that stops too early could impact its performance. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the relationship model you are generating with different sets of parameter values until you can obtain the best evaluation result. But note that you need to write the evaluation code yourself to rank your model with scores.  For general information about validating a regression-based relationship model, see <https://en.wikipedia.org/wiki/Regression_validation>. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
