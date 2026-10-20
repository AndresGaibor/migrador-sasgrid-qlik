<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tnaivebayesmodel · versión 8.0 -->
# tNaiveBayesModel

Last updated: 9/30/2026

Generates a classifier model that is used by tPredict to classify given elements.

tNaiveBayesModel analyzes incoming datasets based on applying Bayes' law with the (naive) assumption that the analyzed features of an element are independent of each other.

It generates a classification model out of this analysis and writes this model in a given file system in the PMML (Predictive Model Markup Language) format.

In local mode, Apache Spark 3.0.x and later versions are
supported.

You must use tModelEncoder in your Job to
prepare and provide the incoming dataset.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tNaiveBayesModel properties for Apache Spark Batch

These properties are used to configure tNaiveBayesModel running in the Spark Batch Job framework.

The Spark Batch
tNaiveBayesModel component belongs to the Machine Learning family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Model location | * Save the model on file   system: Select this check box to store the model in a given file system. Otherwise, the model is   stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn   or the Spark Standalone mode, ensure that you have properly   configured the connection in a configuration component in the same Job, such as tHDFSConfiguration. * Path: This field is available when Save   the model on file system is selected. Enter the path   to the given file system. |
| Parameters | * Label   column:  Select the input column used to provide classification labels. The records of this column   are used as the class names (Target in terms of classification) of the elements to be   classified. * Feature   column:  Select the input column used to provide features. Very often, this column is the output of   the feature engineering computations performed by tModelEncoder. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the classifier model you are generating with different sets of parameter values until you can obtain the best Accuracy (ACC) score and the optimal Precision, Recall and F1-measure scores for each class:  * The Accuracy score varies from 0 to 1 to indicate how   accurate a classification is. More approximate to 1 an   Accuracy score is, more accurate the corresponding   classification is. * The Precision score, also varying from 0 to 1, indicates   how relevant the elements selected by the classification are   to a given class. * The Recall score, still varying from 0 to 1, indicates how   many relevant elements are selected. * The F1-measure score is the harmonic mean of the Precision   score and the Recall score. |
| Scores | These scores can be output to the console of the Run view when you execute the Job when you have added the following code to the Log4j view in the Project Settings dialog box.  ``` <!-- DataScience Logger --> <logger name= "org.talend.datascience.mllib" additivity= "false" > <level value= "INFO" /> <appender-ref ref= "CONSOLE" /> </logger> ```  These scores are output along with the other Log4j INFO-level information. If you want to prevent outputting the irrelevant information, you can, for example, change the Log4j level of this kind of information to WARN but note you need to keep this *DataScience Logger* code as INFO.  If you are using a subscription-based version of Talend Studio, the activity of this component can be logged using the *log4j* feature. For more information on this feature, see [Activating and configuring Log4j](/talend/r/en-US/8.0/studio-user-guide/studio-configure-log4j).  For more information on the log4j logging levels, see the Apache documentation at <http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html>. |
