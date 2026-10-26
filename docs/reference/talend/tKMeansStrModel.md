<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkmeansstrmodel · versión 8.0 -->
# tKMeansStrModel (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Analyzes incoming datasets in near real-time, based on applying
the K-Means algorithm.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

This component analyzes streaming feature vectors to continuously adapt an
existing clustering model to changing circumstances. The incoming data is usually
pre-processed by tModelEncoder and the K-Means model
is used by tPredict to cluster given elements.

It continuously updates a K-Means clustering model out of
this analysis and writes this model either in memory or in a given file system.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tKMeansStrModel properties for Apache Spark Streaming

These properties are used to configure tKMeansStrModel running in the Spark Streaming Job framework.

The Spark Streaming
tKMeansStrModel component belongs to the Machine Learning family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Save on disk | Select this check box to store the clustering model in an HDFS directory you put in the Path field.  In this case, you need to enter the time interval (in minutes) at the end of which the model is saved.  If you clear this check box, your model will be stored in memory. |
| Path | Select this check box to store the model in a given file system. Otherwise, the model is stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn or the Spark Standalone mode, ensure that you have properly configured the connection in a configuration component in the same Job, such as tHDFSConfiguration.  In the Path field, enter the HDFS directory to be used.  This field is available when you select the check boxes used to save a model to or read a model from a file system. |
| Load a precomputed model from disk | Select this check box to use an existing K-Means model stored in the directory you have specified in the Path field. This is the common case when using tKMeansStrModel. In this situation, the following behaviors can be expected:   * If you select the Reuse the model   transformation associated with the model check box,   tKMeansStrModel reuses, along   with this model to be used, the feature pre-processing   algorithms that were previously implemented during the creation   of this model. This reuse allows tKMeansStrModel to directly transform new incoming   data into K-Means compliant feature vectors and process these   vectors, without having to wait for another implementation of   the same algorithms.  However, with this option activated, you need to check the   schema of the data that was transformed by these feature   pre-processing algorithms and ensure that the new input data to   tKMeansStrModel uses the   same schema.  You can simply see this schema in the Job which initially   implemented these feature pre-processing algorithms. * If you clear the Reuse the model   transformation associated with the model check box,   you need to place one or several tModelEncoder components in front of tKMeansStrModel to transform the incoming   data to feature vectors required by K-Means. Then select the   column that provides these feature vectors from the Vector to process drop-down list that is   displayed.  For further information about tModelEncoder, see [tModelEncoder](/talend/en-US/components/8.0/machine-learning/tmodelencoder). * If the model to be loaded does not actually exist, tKMeansStrModel will automatically   initialize 2 clusters to create a K-Means model.   If you clear this Load a precomputed model from disk check box, tKMeansStrModel will create a new K-Means model from scratch. |
| Vector to process | Select the input column used to provide feature vectors. Very often, this column is the output of the feature engineering computations performed by tModelEncoder.  This list appears when you have cleared either the Load a precomputed model from disk check box or the Reuse the model transformation associated with the model check box. |
| Size of your feature vector | Enter the size of the feature vectors to be processed from the column you have selected from the Vector to process list. |
| Display the vector size | Select this check box to display the feature vectors to be used in the console of the Run view.  This feature will slow down your Job but is useful when you do not know what value to be entered in the Size of your feature vector field. |
| Number of clusters (K) | Enter the number of clusters into which you want tKMeansModel to cluster data.  In general, a large number of clusters can decreases errors in predictions but increases the risk of overfitting.  This field appears when you have cleared the Load a precomputed model from disk check box to create a K-Means model from scratch. |
| Decay factor | Enter the decay rate (ranging between 0 and 1) to be applied to discount the weight of existing points against the new incoming points in the process of evaluating new cluster centers.  Lower decay rate means more importance to be attached to the new incoming data. When decay rate is *0*, new cluster centers are determined completely by the new points; when decay rate is *1*, the existing points and new incoming points are evaluated equally. |
| Time unit | Select the unit on which the decay rate is applied: point or batch of points. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Display the centers after the processing | Select this check box to output the vectors of the cluster centers into the console of the Run view.  This feature is often useful when you need to understand how the cluster centers move in the process of training your K-Means model. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the relationship model you are generating with different sets of parameter values until you can obtain the best evaluation result. But note that you need to write the evaluation code yourself to rank your model with scores. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkmeansstrmodel -->
# tKMeansStrModel (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Analyzes incoming datasets in near real-time, based on applying
the K-Means algorithm.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

This component analyzes streaming feature vectors to continuously adapt an
existing clustering model to changing circumstances. The incoming data is usually
pre-processed by tModelEncoder and the K-Means model
is used by tPredict to cluster given elements.

It continuously updates a K-Means clustering model out of
this analysis and writes this model either in memory or in a given file system.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tKMeansStrModel properties for Apache Spark Streaming

These properties are used to configure tKMeansStrModel running in the Spark Streaming Job framework.

The Spark Streaming
tKMeansStrModel component belongs to the Machine Learning family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Save on disk | Select this check box to store the clustering model in an HDFS directory you put in the Path field.  In this case, you need to enter the time interval (in minutes) at the end of which the model is saved.  If you clear this check box, your model will be stored in memory. |
| Path | Select this check box to store the model in a given file system. Otherwise, the model is stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn or the Spark Standalone mode, ensure that you have properly configured the connection in a configuration component in the same Job, such as tHDFSConfiguration.  In the Path field, enter the HDFS directory to be used.  This field is available when you select the check boxes used to save a model to or read a model from a file system. |
| Load a precomputed model from disk | Select this check box to use an existing K-Means model stored in the directory you have specified in the Path field. This is the common case when using tKMeansStrModel. In this situation, the following behaviors can be expected:   * If you select the Reuse the model   transformation associated with the model check box,   tKMeansStrModel reuses, along   with this model to be used, the feature pre-processing   algorithms that were previously implemented during the creation   of this model. This reuse allows tKMeansStrModel to directly transform new incoming   data into K-Means compliant feature vectors and process these   vectors, without having to wait for another implementation of   the same algorithms.  However, with this option activated, you need to check the   schema of the data that was transformed by these feature   pre-processing algorithms and ensure that the new input data to   tKMeansStrModel uses the   same schema.  You can simply see this schema in the Job which initially   implemented these feature pre-processing algorithms. * If you clear the Reuse the model   transformation associated with the model check box,   you need to place one or several tModelEncoder components in front of tKMeansStrModel to transform the incoming   data to feature vectors required by K-Means. Then select the   column that provides these feature vectors from the Vector to process drop-down list that is   displayed.  For further information about tModelEncoder, see [tModelEncoder](/talend/en-US/components/8.0/machine-learning/tmodelencoder). * If the model to be loaded does not actually exist, tKMeansStrModel will automatically   initialize 2 clusters to create a K-Means model.   If you clear this Load a precomputed model from disk check box, tKMeansStrModel will create a new K-Means model from scratch. |
| Vector to process | Select the input column used to provide feature vectors. Very often, this column is the output of the feature engineering computations performed by tModelEncoder.  This list appears when you have cleared either the Load a precomputed model from disk check box or the Reuse the model transformation associated with the model check box. |
| Size of your feature vector | Enter the size of the feature vectors to be processed from the column you have selected from the Vector to process list. |
| Display the vector size | Select this check box to display the feature vectors to be used in the console of the Run view.  This feature will slow down your Job but is useful when you do not know what value to be entered in the Size of your feature vector field. |
| Number of clusters (K) | Enter the number of clusters into which you want tKMeansModel to cluster data.  In general, a large number of clusters can decreases errors in predictions but increases the risk of overfitting.  This field appears when you have cleared the Load a precomputed model from disk check box to create a K-Means model from scratch. |
| Decay factor | Enter the decay rate (ranging between 0 and 1) to be applied to discount the weight of existing points against the new incoming points in the process of evaluating new cluster centers.  Lower decay rate means more importance to be attached to the new incoming data. When decay rate is *0*, new cluster centers are determined completely by the new points; when decay rate is *1*, the existing points and new incoming points are evaluated equally. |
| Time unit | Select the unit on which the decay rate is applied: point or batch of points. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Display the centers after the processing | Select this check box to output the vectors of the cluster centers into the console of the Run view.  This feature is often useful when you need to understand how the cluster centers move in the process of training your K-Means model. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the relationship model you are generating with different sets of parameter values until you can obtain the best evaluation result. But note that you need to write the evaluation code yourself to rank your model with scores. |
