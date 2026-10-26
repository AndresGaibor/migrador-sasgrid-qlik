<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/talsmodel · versión 8.0 -->
# tALSModel

Last updated: 9/30/2026

Generates an user-ranking-product associated matrix, based on given user-product
interactive data.

This matrix is used by tRecommend to estimate these users'
preferences.

tALSModel leverages Spark to process a
large amount of information about users' preferences over given products.

It receives this kind of information from its preceding Spark
component and performs ALS (Alternating Least Squares) computations over
these sets of information in order to generate and write a fine-tuned
product recommender model in a given file system in the Parquet
format.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tALSModel properties for Apache Spark Batch

These properties are used to configure tALSModel running in the Spark Batch Job framework.

The Spark Batch
tALSModel component belongs to the Machine Learning family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Feature table | Complete this table to map the input columns with the three factors required to compute the recommender model.  * Input column: select   the input column to be used from the drop-down list.  These selected columns must contain the user   IDs, the product IDs and the ratings and the data must be   numerical values. * Feature type: select   the factor that each selected input column needs to be   mapped with. The three factors are User\_ID, Product\_ID and Rating.  This map allows tALSModel to read the right type of data for each required factor. |
| Training percentage | Enter the percentage (expressed in the decimal form) of the input data to be used to train the recommender model. The rest of the data is used to test the model. |
| Number of latent factors | Enter the number of the latent factors, with which each user or product feature is measured. |
| Number of iterations | Enter the number of iterations you want the Job to perform to train the model.  This number should be smaller than 30 in order to avoid stack overflow issues and in practices, the convergent score (RMSE score) can often be obtained before you have to use a number beyond 30.  However, if you need to perform more than 30 iterations, you must increase the stack size used to run the Job; to do this, you can add the -Xss argument, for example *-Xss2048k*, to the JVM Settings table in the Advanced settings tab of the Run view. For further information about the JVM Settings table, see [Specifying the limits of VM memory for a Job or Route](/talend/r/en-US/8.0/studio-user-guide/specifying-limits-of-vm-memory-for-job-or-route). |
| Regularization factor | Enter the regularization number you want to use to avoid overfitting. |
| Build model for implicit feedback data set | Select this check box to let tALSModel handle the implicit datasets.  Contrary to the explicit data sets such as the ranking of a product, an implicit dataset only implies users' preferences, for example, a record showing how frequently a user is buying a certain item.  If you leave this check box clear, tALSModel handles the explicit data sets only.  For related details about how the ALS model handles the implicit data sets, see the documentation of Spark in the following link:<https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html>. |
| Confidence coefficient for implicit training | Enter the number to indicate the level of confidence you have in the observed user preferences. |
| Parquet model path | Enter the directory in which you need to store the generated recommender model in the file system to be used.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Parquet model name | Enter the name you need to use for the recommender model. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set Checkpoint Interval | Set the frequency of checkpoints. It is recommended to leave the default value (`10`).  Before setting a value for this parameter, activate checkpointing and set the checkpoint directory in the Spark Configuration tab of the Run view.  For further information about checkpointing, see [Logging and checkpointing the activities of your Apache Spark Job](/talend/en-US/components/8.0/spark-batch/logging-and-checkpointing-activities-of-your-apache-spark-job-spark-batch-component-if-you). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  Note that the parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets. Therefore, you need to train the model you are generating with different sets of parameter values until you can obtain the minimum RMSE score. This score is outputted in the console of the Run view each time a Job execution is done. |
| MLlib installation | In Apache Spark V1.3 or earlier versions of Spark, the Spark machine learning library, MLlib, uses the *gfortran runtime* library. You need to ensure that this library is already present in every node of the Spark cluster to be used.  For further information about MLlib and this library, see the related documentation from Spark. |
| RMSE score | These scores can be output to the console of the Run view when you execute the Job when you have added the following code to the Log4j view in the Project Settings dialog box.  ``` <!-- DataScience Logger --> <logger name= "org.talend.datascience.mllib" additivity= "false" > <level value= "INFO" /> <appender-ref ref= "CONSOLE" /> </logger> ```  These scores are output along with the other Log4j INFO-level information. If you want to prevent outputting the irrelevant information, you can, for example, change the Log4j level of this kind of information to WARN but note you need to keep this *DataScience Logger* code as INFO.  If you are using a subscription-based version of Talend Studio, the activity of this component can be logged using the *log4j* feature. For more information on this feature, see [Activating and configuring Log4j](/talend/r/en-US/8.0/studio-user-guide/studio-configure-log4j).  For more information on the log4j logging levels, see the Apache documentation at <http://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html>. |
