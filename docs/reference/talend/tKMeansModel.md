<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tkmeansmodel · versión 8.0 -->
# tKMeansModel

Last updated: 9/30/2026

Analyzes incoming datasets based on applying the K-Means
algorithm.

This component analyzes feature vectors usually pre-processed by tModelEncoder to generate a clustering model that is used
by tPredict to cluster given elements.

It generates a clustering model out of this analysis and
writes this model either in memory or in a given file system.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tKMeansModel properties for Apache Spark Batch

These properties are used to configure tKMeansModel running in the Spark Batch Job framework.

The Spark Batch
tKMeansModel component belongs to the Machine Learning family.

This component is available in Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Vector to process | Select the input column used to provide feature vectors. Very often, this column is the output of the feature engineering computations performed by tModelEncoder. |
| Save the model on file system | Select this check box to store the model in a given file system. Otherwise, the model is stored in memory. The button for browsing does not work with the Spark Local mode; if you are using the Spark Yarn or the Spark Standalone mode, ensure that you have properly configured the connection in a configuration component in the same Job, such as tHDFSConfiguration. |
| Number of clusters (K) | Enter the number of clusters into which you want tKMeansModel to group data.  In general, a large number of clusters can decreases errors in predictions but increases the risk of overfitting. Therefore, it is recommended to put a reasonable number based on how many potential clusters you think, by observation for example, the data to be processed might contain. |
| Set distance threshold of the convergence (Epsilon) | Select this check box and in the Epsilon field that is displayed, enter the convergence distance you want to use. The model training is considered accomplished once all of the cluster centers move less than this distance.  If you leave this check box clear, the default convergence distance *0.0001* is used. |
| Set the maximum number of runs | Select this check box and in the Maximum number of runs field that is displayed, enter the number of iterations you want the Job to perform to train the model.  If you leave this check box clear, the default value *20* is used. |
| Set the number of parallelized runs | This setting is not available from Apache Spark 3.0 onwards.  Select this check box and in the Number of parallelized runs field that is displayed, enter the number of iterations you want the Job to run in parallel.  If you leave this check box clear, the default value *1* is used. This actually means that the iterations will be run in succession.  Note that this parameter helps you optimize the use of your resources for the computations but does not impact the prediction performance of the model. |
| Initialization function | Select the mode to be used to select the points as initial cluster centers.  * Random: the points are selected   randomly. In general, this mode is used for simple datasets. * K-Means||: this mode is known   as Scalable K-Means++, a parallel algorithm that can obtain a nearly   optimal initialization result. This is also the default initialization   mode.  For further information about this mode, see [Scalable K-Means++](http://theory.stanford.edu/%7Esergei/papers/vldb12-kmpar.pdf). |
| Set the number of steps for the initialization | Select this check box and in the Steps field that is displayed, enter the number of initialization rounds to be run for the optimal initialization result.  If you leave this check box clear, the default value *5* is used. *5* rounds are almost always enough for the K-Means|| mode to obtain the optimal result. |
| Define the random seed | Select this check box and in the Seed field that is displayed, enter the seed to be used for the initialization of the cluster centers. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Display the centers after the processing | Select this check box to output the vectors of the cluster centers into the console of the Run view.  This feature is often useful when you need to understand how the cluster centers move in the process of training your K-Means model. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  You can accelerate the training process by adjusting the stopping conditions such as the maximum number of runs or the convergence distance. The training that stops too early can impact its performance. |
| Model evaluation | The parameters you need to set are free parameters and so their values may be provided by previous experiments, empirical guesses or the like. They do not have any optimal values applicable for all datasets.  Therefore, you need to train the relationship model you are generating with different sets of parameter values until you can obtain the best evaluation result. But note that you need to write the evaluation code yourself to rank your model with scores. |

**Related tasks**  

* [Modeling the accident-prone areas in a city](tmodelencoder-tkmeansmodel-ts3configuration-modeling-accident-prone-areas-in-city-spark-batch-component-in-this "In this scenario, the tKMeansModel component is used to analyze a set of sample geographical data about the destination of ambulances in a city in order to model the accident-prone areas.")
