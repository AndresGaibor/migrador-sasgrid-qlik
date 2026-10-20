<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tmodelencoder · versión 8.0 -->
# tModelEncoder

Last updated: 9/30/2026

Performs featurization operations to transform data into the
format expected by the model training components such as tLogisticRegressionModel or tKMeansModel.

tModelEncoder receives data from its
preceding components, applies a wide range of feature processing algorithms to transform
given columns of this data and sends the result to the model training component that
follows to eventually train and create a predictive model.

In local mode, Apache Spark 3.0.x and later versions are
supported.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tModelEncoder properties for Apache Spark Batch](/talend/en-US/components/8.0/machine-learning/tmodelencoder-properties-for-apache-spark-batch)
* [tModelEncoder properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/machine-learning/tmodelencoder-properties-for-apache-spark-streaming)

**Related tasks**  

* [Creating a classification model to filter spam](classification-model)
* [Modeling the accident-prone areas in a city](tmodelencoder-tkmeansmodel-ts3configuration-modeling-accident-prone-areas-in-city-spark-batch-component-in-this "In this scenario, the tKMeansModel component is used to analyze a set of sample geographical data about the destination of ambulances in a city in order to model the accident-prone areas.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tmodelencoder-properties-for-apache-spark-batch -->
# tModelEncoder properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tModelEncoder running in the Spark Batch Job framework.

The Spark Batch
tModelEncoder component belongs to the Machine Learning family.

The component in this framework is available in all Talend Platform
products with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  An output column must be named differently from any of the input columns, because the successive transformations from the input side to the output side take place in the same DataFrame (the Spark term for a schema-based data collection) and thus the output columns are actually added to the same DataFrame alongside the input columns.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Transformation table | Complete this table using columns from the input and the output schemas and the feature-processing algorithms to be applied on these columns.  The algorithms available in the Transformation column varies depending on the type of the input schema columns to be processed.  For further information about the algorithms available for each type of input data, see [ML feature-processing algorithm in Talend](/talend/r/en-US/8.0/components/machine-learning/ml-feature-processing-algorithms-in-talend). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/machine-learning/tmodelencoder-tkmeansmodel-ts3configuration-modeling-accident-prone-areas-in-city-spark-batch-component-in-this -->
# Modeling the accident-prone areas in a city

Last updated: 9/30/2026

In this scenario, the tKMeansModel component is used to
analyze a set of sample geographical data about the destination of ambulances in a city in
order to model the accident-prone areas.

## Before you begin

* The Spark version to be used is 1.4 onwards.
* The sample data is stored in your Hadoop file system and you have proper rights
  and permissions to at least read it.
* Your Hadoop cluster is properly installed and is running.

  If you are not sure about these requirements, ask the administrator
  of your Hadoop system.
* In the Spark
  Configuration tab in the Run
  view, define the connection to a given Spark cluster for the whole Job. In
  addition, since the Job expects its dependent jar files for execution, you must
  specify the directory in the file system to which these jar files are
  transferred so that Spark can access these files:
  + Yarn mode (Yarn client or Yarn cluster):
    - When using Google Dataproc, specify a bucket in the
      Google Storage staging bucket
      field in the Spark configuration
      tab.
    - When using HDInsight, specify the blob to be used for Job
      deployment in the Windows Azure Storage
      configuration area in the Spark
      configuration tab.
    - When using Altus, specify the S3 bucket or the Azure
      Data Lake Storage for Job deployment in the Spark
      configuration tab.
    - When using on-premises distributions, use
      the configuration component corresponding to the file system
      your cluster is using. Typically, this system is HDFS and so
      use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
  + Standalone mode: use the
    configuration component corresponding to the file system your cluster is
    using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

    If you are using Databricks without any configuration component present
    in your Job, your business data is written directly in DBFS (Databricks
    Filesystem).

## About this task

* This scenario applies only to subscription-based Talend products
  with Big Data.
* A model like this can be employed to help determine the optimal locations for building hospitals.
* The sample data consists of pairs of latitudes and longitudes. It was randomly and
  automatically generated for demonstration purposes only and in any case it does not
  reflect the situation of these areas in the real world.
* The components to be used are:
  + tFileInputDelimited: it loads the
    sample data into the data flow of the Job.
  + tReplicate: it replicates the sample
    data and caches the replication.
  + tKMeansModel: it analyzes the data to
    train the model and writes the model to HDFS.
  + tModelEncoder: it pre-process the data
    to prepare proper feature vectors to be used by tKMeansModel.
  + tPredict: it applies the KMeans model
    on the replication of the sample data. In the real-world practice, this data
    should be a set of reference data to test the model accuracy.
  + tFileOutputDelimited: it writes the
    result of the prediction to HDFS.
  + tHDFSConfiguration: this component is used by Spark to connect to
    the HDFS system where the jar files dependent on the Job are transferred.

## Arranging data flow for the KMeans Job

### Procedure

1. In the Integration perspective of Talend Studio,
   create an empty Job from the Job Designs node
   in the Repository tree view.
2. In the workspace, enter the name of the component to be used and
   select it from the list that appears.
3. Connect tFileInputDelimited to tReplicate using the Row >
   Main link.
4. Do the same to connect tReplicate to tModelEncoder and then tModelEncoder to tKMeansModel.
5. Repeat the operations to connect tReplicate to tPredict and then tPredict to tFileOutputDelimited.
6. Leave tHDFSConfiguration as it is.

## Configuring the connection to the file system to be used by Spark

See the procedure in the [Getting Started Guide](/talend/en-US/studio-getting-started-guide-data-fabric/8.0/configuring-connection-to-file-system-to-be-used-by-spark).

## Reading and caching the sample data

### Procedure

1. Double-click the first tFileInputInput component to
   open its Component view.
2. Click the [...] button next to Edit schema and in the pop-up schema dialog box, define the
   schema by adding two columns *latitude* and
   *longitude* of Double type.
3. Click OK to validate these changes and accept the
   propagation prompted by the pop-up dialog box.
4. Select the Define a storage configuration
   component check box and select the tHDFSConfiguration component to be used.

   tFileInputDelimited uses this configuration
   to access the sample data to be used as training set.
5. In the Folder/File field, enter the directory
   where the training set is stored.
6. Double-click the tReplicate component to open its
   Component view.
7. Select the Cache replicated RDD check box and from
   the Storage level drop-down list, select
   Memory only. This way, this sample data is
   replicated and stored in memory for use as test set.

## Preparing features for KMeans

### Procedure

1. Double-click the tModelEncoder component to open its Component view.
2. Click the [...] button
   next to Edit schema and on the tModelEncoder side of the pop-up schema dialog box,
   define the schema by adding one column named `map` of
   Vector type.
3. Click OK to validate these changes and accept
   the propagation prompted by the pop-up dialog box.
4. In the Transformations
   table, add one row by clicking the [+]
   button and then proceed as follows: 
   1. In the Output column column, select the column
      that carry the features. In this scenario, it is
      map.
   2. In the Transformation column, select the
      algorithm to be used for the transformation. In this scenario, it is
      Vector assembler.
   3. In the Parameters column, enter the parameters
      you want to customize for use in the Vector assembler algorithm. In this
      scenario, enter
      `inputCols=latitude,longitude`.

   In this transformation, tModelEncoder combines all feature vectors into one single
   feature column.
5. Double-click tKMeansModel to open its Component view.
6. Select the Define a storage configuration
   component check box and select the tHDFSConfiguration component to be used.
7. From the Vector to
   process list, select the column that provides the feature vectors to
   be analyzed. In this scenario, it is map, which combines
   all features.
8. Select the Save the model on file system
   check box and in the HDFS folder field that
   is displayed, enter the directory you want to use to store the generated
   model.
9. In the Number of cluster
   field, enter the number of decision trees you want tKMeans to build. You need to try different numbers to run the
   current Job to create the clustering model several times; after comparing the
   evaluation results of every model created on each run, you can decide the number
   you need to use. For example, put `6`.

   You need to write the evaluation code yourself.
10. From the Initialization function, select Random. In general, this mode is used for simple datasets.
11. Leave the other parameters as they are.

## Testing the KMeans model

### Procedure

1. Double-click tPredict to open its
   Component view.
2. Select the Define a storage configuration
   component check box and select the tHDFSConfiguration component to be used.
3. From the Model type drop-down list, select
   Kmeans model.
4. Select the Model on filesystem radio button and enter the
   directory in which the KMeans model is stored.

   In this case, the tPredict component contains a
   read-only column called *label* in which the
   model provides the labels of the clusters.
5. Double-click tFileOutputDelimited to open its
   Component view.
6. Select the Define a storage configuration
   component check box and select the tHDFSConfiguration component to be used.
7. In the Folder field, browse to the location
   in HDFS in which you want to store the prediction result.
8. From the Action drop-down list, select
   Overwrite. When the target folder does
   not exist, select Create.
9. Select the Merge result to single file check
   box and then the Remove source dir check
   box.
10. In the Merge file path field, browse to the
    location in HDFS in which you want to store the merged prediction result.

## Selecting the Spark mode

See the procedure in the [Getting Started Guide](/talend/en-US/studio-getting-started-guide-data-fabric/8.0/selecting-spark-mode).

## Executing the Job

### Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   The merged prediction result is stored in HDFS and you can evaluate this
   result using your evaluation process. Then run this Job more times with
   different KMeans parameters in order to obtain the optimal model.

### Results

The following image shows an example of the predicted clusters. This visualization is
produced via a Python script. You can download this script from [here](https://talend365.sharepoint.com/:u:/g/departments/rd/EV9FXMNOcAFIrcNbw4yR9kcBVJCMG_2Cy6juKYCTAfbRlQ?e=NL9ksr) and bear in mind to adapt the path in the script to access the
prediction result in your own machine.

**Related concepts**  

* [tModelEncoder](tmodelencoder "Performs featurization operations to transform data into the format expected by the model training components such as tLogisticRegressionModel or tKMeansModel.")
* [tPredict](tpredict "Predicts the situation of an element.")

**Related reference**  

* [tKMeansModel](tkmeansmodel "Analyzes incoming datasets based on applying the K-Means algorithm.")

**Related information**  

* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tReplicate](/talend/en-US/components/8.0/orchestration/treplicate)
* [tS3Configuration](/talend/en-US/components/8.0/amazon-s3/ts3configuration)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
