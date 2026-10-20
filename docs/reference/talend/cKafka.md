<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka · versión 8.0 -->
# cKafka

Last updated: 9/30/2026

Communicates with [Apache Kafka](http://kafka.apache.org/) message broker.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cKafka Standard properties

These properties are used to configure cKafka running in the
Standard Job framework.

The Standard
cKafka component belongs to the
Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Broker List | Specify the list of Kafka message brokers in the form hostname1:port1,hostname2:port2,hostname3:port3. |
| Client Id | Specify an Id string of the client to pass to the server when making requests. |
| Topic | Type in a name for the message topic in the message broker. |
| GroupId | Enter the Id of the Kafka Connect cluster group. |
| Receive Buffer (bytes) | Specify the size of the TCP receive buffer to use when reading data. If the value is -1, the OS default will be used. |
| Use Schema Registry | Select this check box to use Confluent Schema Registry and enter the URL of the Schema Registry instance in the Schema Registry URL field in the host1:port1,host2:port2 format. For more information about Schema Registry, see the [Confluent documentation](https://docs.confluent.io/platform/current/schema-registry/index.html).  This option is available when you have installed the 8.0.1-R2023-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| The following options are available only when the cKafka is used as a Producer: |  |
| Partitioner | Enter the partitioner that determines how data is distributed across the Kafka cluster. |
| Serializer Class | Enter the class name of the serializer to be used. |
| Key Serializer Class | Enter the class name of the key serializer to be used. |
| Compression Codec | Select compression type from NONE, GZIP, SNAPPY, and LZ4. |
| The following options are available only when the cKafka is used as a Consumer: |  |
| Auto Commit Enable | Select this check box to periodically commit the offset of messages in the background. Specify the frequency in milliseconds in the Auto Commit Interval (ms) that the consumer offsets are committed to Kafka. |
| Auto Offset Reset | Choose what to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server from the following:   * EARLIEST: automatically reset the   offset to the earliest offset; * LATEST: automatically reset the   offset to the latest offset; * NONE: throw exception to the   consumer if no previous offset is found for the consumer's group. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Kafka Properties | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding value field and enter a value. See the site<http://kafka.apache.org/documentation.html> for available options. |
| SSL Key Password | Click [...] and enter the password of the private key in the key store file in double quotes. |
| SSL Keystore Location | Enter the location of the key store file. |
| SSL Keystore Password | Click [...] and enter the password for the key store file in double quotes. This is only needed if SSL Keystore Location is configured. |
| SSL Truststore Location | Enter the location of the trust store file. |
| SSL Truststore Password | Click [...] and enter the password for the trust store file in double quotes. |
| SSL Cipher Suites | Enter the list of cipher suites. This is a named combination of authentication, encryption, MAC and key exchange algorithm used to negotiate the security settings for a network connection using TLS or SSL network protocol. By default all the available cipher suites are supported. |
| SSL Endpoint Algorithm | Enter the endpoint identification algorithm to validate server hostname using server certificate. |
| Kerberos Service Name | Enter the Kerberos principal name that Kafka runs as. |
| Security Protocol | Select the protocol to use to communicate with brokers from Plaintext, SSL, SASL over Plaintext, and SASL over SSL. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cKafka is used as a start, middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Accessing Confluent Kafka using cKafka and cMap](ckafka-ctimer-cmap-clog-csetbody-accessing-confluent-kafka-using-ckafka-and-cmap)
* [Accessing Confluent Kafka using cKafka](ckafka-ctimer-cprocessor-clog-csetbody-accessing-confluent-kafka-using-ckafka)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-accessing-confluent-kafka-using-ckafka-and-cmap -->
# Accessing Confluent Kafka using cKafka and cMap

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario will show you how to use the **cKafka** and cMap
components for message exchange with Confluent Kafka message broker using schema
registry.

Before creating the Route in this scenario, check that you meet the following prerequisites.

* You have downloaded the set of Confluent Kafka Docker images from Git repository.
  For example, using the following
  command:

  ```
  git clone https://github.com/confluentinc/cp-all-in-one -b 7.1.0-post
  ```
* Docker must be up and running.
* Local Confluent Kafka environment is started using
  Docker:

  ```
  cd cp-all-in-one/cp-all-in-one
  docker-compose up
  ```

For more information about the cKafka component, see the [Apache Camel documentation](https://camel.apache.org/components/latest/kafka-component.html).

For the differences between Apache Kafka and Confluent Kafka, see [Confluent Kafka documentation](https://www.confluent.io/apache-kafka-vs-confluent/).

### In this section

* [Creating hierarchical structures and maps](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-creating-hierarchical-structures-and-maps)
* [Creating a Bean Jar](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-creating-a-bean-jar?id=370)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-dropping-and-linking-the-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-configuring-the-components)
* [Security configuration (optional)](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-security-configuration)

**Related reference**  

* [cKafka](ckafka "Communicates with Apache Kafka message broker.")

**Related information**  

* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)
* [cMap](/talend/en-US/mediation-components/8.0/mediation-map/cmap)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-accessing-confluent-kafka-using-ckafka -->
# Accessing Confluent Kafka using cKafka

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario will show you how to use the **cKafka** component for message exchange
with Confluent Kafka message broker using schema registry.

Before creating the Route in this scenario, check that you meet the following prerequisites.

* You have downloaded the set of Confluent Kafka Docker images from the Git
  repository:

  ```
  git clone https://github.com/confluentinc/cp-all-in-one -b 7.1.0-post
  ```
* Docker must be up and running.
* Local Confluent Kafka environment is started using
  Docker:

  ```
  cd cp-all-in-one/cp-all-in-one
  docker-compose up
  ```

For more information about the cKafka component, see the [Apache Camel documentation](https://camel.apache.org/components/latest/kafka-component.html).

For the differences between Apache Kafka and Confluent Kafka, see the [Confluent Kafka documentation](https://www.confluent.io/apache-kafka-vs-confluent/).

### In this section

* [Creating a Bean Jar](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-creating-a-bean-jar?id=364)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-dropping-and-linking-the-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-configuring-the-components)
* [Security configuration (optional)](/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-security-configuration)

**Related reference**  

* [cKafka](ckafka "Communicates with Apache Kafka message broker.")

**Related information**  

* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-configuring-the-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cTimer component to
   display its Basic settings view in the Component tab. Keep the default settings of the options as
   shown below.
2. Double-click the first cSetBody
   component, which is labeled `SetBodyAsJsonString`, to open its
   Basic settings view in the Component tab.
3. Select Constant from the
   Language drop-down list and type in the JSON
   string `"{\"my_field1\": 1,\"my_field2\": 72438939,\"my_field3\": \"my demo
   Test message\"}"` in the Expression
   field as the message body.
4. Click the Component tab of the first cMap component, which is labeled
   `ConvertBodyToAvro` and open its Basic settings view.
5. Click the [...] button next to the Map Path field and select the map
   “Avro/Sample\_JSON\_to\_AVRO”.
6. Select Object from the Output Type
   drop-down list.
7. Click the Component tab of the second
   cMap component, which is labeled
   `ConvertBodyToJsonString` and open its Basic
   settings.
8. Click the [...] button next to the Map
   Path field and select the map
   “Avro/Sample\_AVRO\_to\_JSON”.
9. Select Byte Array from the Output
   Type drop-down list.
10. Double-click the first cKafka
    component, which is labeled `SendMessageToKafka`, to open its
    Basic settings view in the Component tab.
11. In the Broker List field, enter
    "localhost:9092".

    In the Topic field, enter
    `"demo.AVRO"`.

    In the Serializer Class field,
    enter
    "org.example.local\_project.beansjar.kafka\_avro\_beans.KafkaAvroSerializerBean".
    Make sure you replace local\_project with the Talend
    project name.

    Keep the default settings of the other options.
12. Open Advanced settings view in the
    Component tab.
13. In the Kafka Properties field, add a parameter with the name
    "schemaRegistryURL" and the value
    "localhost:8081".
14. Double-click the second cKafka component, which is labeled
    `ReceiveMessageFromKafka`, to open its Basic
    settings view in the Component tab.
15. In the Broker List field, enter
    "localhost:9092".

    In the Topic field, enter
    `"demo.AVRO"`.

    Keep the default settings of the other options.
16. Open Advanced settings view in the
    Component tab.
17. In the Kafka Properties field, add two parameters with the
    name "schemaRegistryURL" and "valueDeserializer",
    and the value "localhost:8081" and
    "org.example.local\_project.beansjar.kafka\_avro\_beans.KafkaAvroDeserializerBean"
    respectively. Make sure you replace local\_project with the Talend
    project name.
18. Keep the default settings of the cLog components to log the message exchanges.
19. Press Ctrl+S to save your
    Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-creating-hierarchical-structures-and-maps -->
# Creating hierarchical structures and maps

Last updated: 9/30/2026

## Procedure

1. Create a text file named sample.json with the following
   content:

   ```
   {
     "doc": "Sample schema to help you get started.",
     "fields": [
       {
         "doc": "The int type is a 32-bit signed integer.",
         "name": "my_field1",
         "type": "int"
       },
       {
         "doc": "The double type is a double precision (64-bit) IEEE 754 floating-point number.",
         "name": "my_field2",
         "type": "int"
       },
       {
         "doc": "The string is a unicode character sequence.",
         "name": "my_field3",
         "type": "string"
       }
     ],
     "name": "AvroSample",
     "namespace": "talend",
     "type": "record"
   }
   ```
2. From the repository tree view, right-click Metadata > Hierarchical Mapper > Structure and select New > Folder from the contextual menu.
3. In the New Folder dialog box, enter
   `Avro` in the Folder name field and
   click Finish.
4. Right-click Metadata > Hierarchical Mapper > Structure and select New > Structure from the contextual menu.
5. In the New Structure dialog box, select Import a structure definition… > Avro Schema  > Local file. Browse to the `sample.json` file you just
   created and import the schema into the `Avro` folder.
6. Right-click Metadata > Hierarchical Mapper > Maps and select New > Folder from the contextual menu.
7. In the New Folder dialog box, enter
   `Avro` in the Name field and click
   Finish.
8. Right-click Metadata > Hierarchical Mapper > Maps and select New > Map from the contextual menu.
9. In the New Map dialog box, select Standard
   Map and create two Maps inside the `Avro` folder
   using the structure created in the previous steps.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-dropping-and-linking-the-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cTimer, a cSetBody, two cMap, two cLog, and two cKafka
   components onto the design workspace.
2. Label the components for better identification of their roles and link
   them with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cmap-clog-csetbody-security-configuration -->
# Security configuration (optional)

Last updated: 9/30/2026

## Procedure

1. Modify the Bean `KafkaAvroSerializerBean` inside
   `Kafka_Avro_Beans` with the following content:

   ```
   package org.example.local_project.beansjar.kafka_avro_beans;

   import java.util.HashMap;
   import java.util.Map;
   import io.confluent.kafka.schemaregistry.client.CachedSchemaRegistryClient;
   import io.confluent.kafka.schemaregistry.client.SchemaRegistryClientConfig;
   import io.confluent.kafka.serializers.KafkaAvroSerializer;
   import io.confluent.kafka.serializers.KafkaAvroSerializerConfig;

   public class KafkaAvroSerializerBean extends KafkaAvroSerializer {

   	@Override
   	public void configure(KafkaAvroSerializerConfig config) {

         	Map<String, String> configs = new HashMap<String, String>();
         
   configs.put(SchemaRegistryClientConfig.BASIC_AUTH_CREDENTIALS_SOURCE,
      config.getString("basic.auth.credentials.source"));
   configs.put(SchemaRegistryClientConfig.USER_INFO_CONFIG, 
      config.getPassword("basic.auth.user.info").value());       		
          this.schemaRegistry = new CachedSchemaRegistryClient(  
             config.getSchemaRegistryUrls(), 1000, configs);
          this.strategyUsesSchema(true);
          this.autoRegisterSchema = true;
   //	  this.useSchemaReflection = true;
   //	  this.normalizeSchema = true;
   //	  this.useLatestVersion = true; 
   //	  this.avroReflectionAllowNull = true;
   	}
   }
   ```
2. Modity the Bean `KafkaAvroDeserializerBean` inside
   `Kafka_Avro_Beans` with the following content:

   ```
   package org.example.local_project.beansjar.kafka_avro_beans;
    
   import java.util.HashMap;
   import java.util.Map;
   import io.confluent.kafka.schemaregistry.client.CachedSchemaRegistryClient;
   import io.confluent.kafka.schemaregistry.client.SchemaRegistryClientConfig;
   import io.confluent.kafka.serializers.KafkaAvroDeserializer;
   import io.confluent.kafka.serializers.KafkaAvroDeserializerConfig;
    
   public class KafkaAvroDeserializerBean extends KafkaAvroDeserializer {
    
   @Override
   public void configure(KafkaAvroDeserializerConfig config) {
       Map<String, String> configs = new HashMap<String, String>();
         
       configs.put(SchemaRegistryClientConfig.BASIC_AUTH_CREDENTIALS_SOURCE,
           config.getString("basic.auth.credentials.source"));
       configs.put(SchemaRegistryClientConfig.USER_INFO_CONFIG, 
           config.getPassword("basic.auth.user.info").value());       		
       this.schemaRegistry = new CachedSchemaRegistryClient(  
           config.getSchemaRegistryUrls(), 1000, configs);
       this.useSpecificAvroReader = false;
   }}
   ```
3. Create context variables for the Route, API\_KEY of String type
   and API\_SECRET of Password type with values of API KEY and API
   SECRET issued by Confluent.

   For more information on context parameters, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).

   For more information about API KEY and API SECRET, see [Confluent documentation](https://docs.confluent.io/cloud/current/access-management/authenticate/api-keys/api-keys.html#use-api-keys-to-control-access-in-ccloud).
4. Create context parameters SCHEMA\_REGISTRY\_KEY of String type and
   SCHEMA\_REGISTRY\_SECRET of Password type with values of SCHEMA
   REGISTRY KEY and SCHEMA REGISTRY SECRET issued by Confluent.
5. In the Advanced settings tab of the
   cKafka components `SendMessageToKafka`
   and `ReceiveMessageFromKafka`, add the following parameters in
   the Kafka Properties field.

   | Name | Value |
   | --- | --- |
   | "additionalProperties.basic.auth.user.info" | "RAW(" + context.SCHEMA\_REGISTRY\_KEY + ":" + context.SCHEMA\_REGISTRY\_SECRET+")" |
   | "additionalProperties.basic.auth.credentials.source" | "USER\_INFO" |
   | "additionalProperties.security.protocol" | "SASL\_SSL" |
   | "additionalProperties.sasl.jaas.config" | "org.apache.kafka.common.security.plain.PlainLoginModule required username='"+ context.API\_KEY +"' password='" + context.API\_SECRET + "';" |
   | "additionalProperties.sasl.mechanism" | "PLAIN" |

   For more information on the security configuration, see the Confluent
   Kafka security documentation <https://docs.confluent.io/platform/current/security/auth-overview.html>.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-creating-a-bean-jar -->
# Creating a Bean Jar

Last updated: 9/30/2026

## Procedure

1. From the repository tree view, right-click Code > Custom Bean Jars and select Create Bean Jar from the contextual
   menu.
2. In the New Bean Jar dialog box, enter
   `Kafka_Avro_Beans` in the Name field
   and click Finish.
3. Right-click `Kafka_Avro_Beans` under the Custom
   Bean Jars node and select Create Bean from the
   contextual menu.
4. The New Bean wizard opens. In the
   Name field, enter
   `KafkaAvroSerializerBean` and click Finish.
5. Enter the following code in the design workspace.

   ```
   package org.example.local_project.beansjar.kafka_avro_beans;

   import io.confluent.kafka.schemaregistry.client.CachedSchemaRegistryClient;
   import io.confluent.kafka.serializers.KafkaAvroSerializer;
   import io.confluent.kafka.serializers.KafkaAvroSerializerConfig;

   public class KafkaAvroSerializerBean extends KafkaAvroSerializer {

   	@Override
   	public void configure(KafkaAvroSerializerConfig config) {
   		this.schemaRegistry = new CachedSchemaRegistryClient(config.getSchemaRegistryUrls(), 1000);
   		this.strategyUsesSchema(true);
   		this.autoRegisterSchema = true;
   //		this.useSchemaReflection = true;
   //		this.normalizeSchema = true;
   //		this.useLatestVersion = true; 
   //		this.avroReflectionAllowNull = true;
   	}
   }
   ```
6. Press Ctrl+S to save your
   bean.
7. Right-click `Kafka_Avro_Beans` under the Custom
   Bean Jars node again and create a Bean with the name
   `KafkaAvroDeserializerBean` and the following content:

   ```
   package org.example.local_project.beansjar.kafka_avro_beans;

   import io.confluent.kafka.schemaregistry.client.CachedSchemaRegistryClient;
   import io.confluent.kafka.serializers.KafkaAvroDeserializer;
   import io.confluent.kafka.serializers.KafkaAvroDeserializerConfig;

   public class KafkaAvroDeserializerBean extends KafkaAvroDeserializer {

   	@Override
   	public void configure(KafkaAvroDeserializerConfig config) {
   		this.schemaRegistry = new CachedSchemaRegistryClient(config.getSchemaRegistryUrls(), 1000);
   		this.useSpecificAvroReader = false;
   	}
   }
   ```
8. Repeat this operation to create a Bean inside
   `Kafka_Avro_Beans` with the name
   `KafkaAvroConverterBean` and the following content:

   ```
   package org.example.local_project.beansjar.kafka_avro_beans;

   import java.io.ByteArrayOutputStream;
   import java.nio.charset.StandardCharsets;

   import org.apache.avro.Schema;

   import org.apache.avro.generic.GenericData.Record;
   import org.apache.avro.generic.GenericDatumReader;
   import org.apache.avro.generic.GenericDatumWriter;
   import org.apache.avro.io.DatumReader;
   import org.apache.avro.io.DatumWriter;
   import org.apache.avro.io.DecoderFactory;
   import org.apache.avro.io.EncoderFactory;
   import org.apache.avro.io.JsonEncoder;

   public class KafkaAvroConverterBean {

   	// AVRO schema
   	static Schema  schema = new Schema.Parser().parse( 
   			"{" 
   	         + "\"doc\": \"Sample schema to help you get started.\"," 
   	         + "\"fields\": [" 
   		     + "{"
   			 + "\"doc\": \"The int type is a 32-bit signed integer.\"," 
   		     + "\"name\": \"my_field1\","
   			 + "\"type\": \"int\"" 
   			 + "}," 
   			 + "{"
   			 + "\"doc\": \"The double type is a double precision (64-bit) IEEE 754 floating-point number.\","
   			 + "\"name\": \"my_field2\"," 
   			 + "\"type\": \"int\"" 
   			 + "}," 
   			 + "{"
   			 + "\"doc\": \"The string is a unicode character sequence.\"," 
   			 + "\"name\": \"my_field3\","
   			 + "\"type\": \"string\"" 
   			 + "}" 
   			 + "]," 
   			 + "\"name\": \"AvroSample\","
   			 + "\"namespace\": \"talend\"," 
   			 + "\"type\": \"record\"" 
   			 + "}");
   	
   	
   	public static String avroToJsonString(Object body) throws RuntimeException {
   		try {
   			ByteArrayOutputStream baos = new ByteArrayOutputStream();
               DatumWriter<Record> writer = new GenericDatumWriter<Record>(schema);
               JsonEncoder encoder = EncoderFactory.get().jsonEncoder(schema, baos, false);
               writer.write((Record)body, encoder);
               encoder.flush();
               baos.flush();
               return new String(baos.toByteArray(), StandardCharsets.UTF_8);
   	    } catch (Exception e) {
   		      throw new RuntimeException(
   		          String.format("Error coverting Avro to Json of schema %s", schema), e);
   	    } 
   	}
   	
   	public static Record jsonStringToAvro(Object jsonString) throws RuntimeException {
   	    try {
   	      DatumReader<Object> reader = new GenericDatumReader<Object>(schema);
   	      return (Record)reader.read(null, DecoderFactory.get().jsonDecoder(schema, (String)jsonString));
   	    } catch (Exception e) {
   		      throw new RuntimeException(
   		          String.format("Error coverting json %s to Avro of schema %s", jsonString, schema), e);
   	    }
   	}
   }
   ```
9. Right-click `Kafka_Avro_Beans` under the Custom
   Bean Jars node and select Edit Bean Jar
   Libraries from the contextual menu.
10. Add the following dependencies.
11. Create a Route for the message exchange with Confluent Kafka message broker.
12. Right-click the Route you just created and select Setup Code
    dependencies from the contextual menu.
13. In the Setup Code dependencies dialog box, select
    `Kafka_Avro_Beans` in the Custom Bean
    Jars tab and click OK.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-configuring-the-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cTimer component to
   display its Basic settings view in the Component tab. Keep the default settings of the options as
   shown below.
2. Double-click the first cSetBody
   component, which is labeled `SetBodyAsJsonString`, to open its
   Basic settings view in the Component tab.
3. Select Constant from the
   Language drop-down list and type in the JSON
   string `"{\"my_field1\": 1,\"my_field2\": 72438939,\"my_field3\": \"my demo
   Test message\"}"` in the Expression
   field as the message body.
4. Double-click the first cProcessor
   component, which is labeled `ConvertBodyToAvro`, to open its
   Basic settings view in the Component tab.
5. In the Code field, set the following Java code to convert
   the message body (JSON string) to Avro Record.

   ```
   Object body = exchange.getMessage().getBody();
   exchange.getMessage().setBody(KafkaAvroConverterBean.jsonStringToAvro(body));
   ```
6. Click the Advanced settings tab and enter the following
   statement in the Import field. Make sure you replace
   local\_project with the Talend
   project name.

   ```
   import org.example.local_project.beansjar.kafka_avro_beans.KafkaAvroConverterBean;
   ```
7. Double-click the second cProcessor component, which is
   labeled `ConvertBodyToJsonString`, to open its Basic
   settings view in the Component tab.
8. In the Code field, set the following Java code to convert
   the message body (Avro Record) to JSON string.

   ```
   Object body = exchange.getMessage().getBody();
   exchange.getMessage().setBody(KafkaAvroConverterBean.avroToJsonString(body));
   ```
9. Click the Advanced settings tab and enter the following
   statement in the Import field. Make sure you replace
   local\_project with the Talend
   project name.

   ```
   import org.example.local_project.beansjar.kafka_avro_beans.KafkaAvroConverterBean;
   ```
10. Double-click the first cKafka
    component, which is labeled `SendMessageToKafka`, to open its
    Basic settings view in the Component tab.
11. In the Broker List field, enter
    "localhost:9092".

    In the Topic field, enter
    `"demo.AVRO"`.

    In the Serializer Class field,
    enter
    "org.example.local\_project.beansjar.kafka\_avro\_beans.KafkaAvroSerializerBean".
    Make sure you replace local\_project with the Talend
    project name.

    Keep the default settings of the other options.
12. Click the Advanced settings tab. In the Kafka
    Properties field, add a parameter with the name
    "schemaRegistryURL" and the value
    "localhost:8081".
13. Double-click the second cKafka component, which is labeled
    `ReceiveMessageFromKafka`, to open its Basic
    settings view in the Component tab.
14. In the Broker List field, enter
    "localhost:9092".

    In the Topic field, enter
    `"demo.AVRO"`.

    Keep the default settings of the other options.
15. Click the Advanced settings tab. In the Kafka
    Properties field, add two parameters with the name
    "schemaRegistryURL" and "valueDeserializer", and
    the value "localhost:8081" and
    "org.example.local\_project.beansjar.kafka\_avro\_beans.KafkaAvroDeserializerBean"
    respectively. Make sure you replace local\_project with the Talend
    project name.
16. Keep the default settings of the cLog components to log the message exchanges.
17. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-dropping-and-linking-the-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cTimer, a cSetBody, two cProcessor, two
   cLog, and two cKafka components onto the design workspace.
2. Label the components for better identification of their roles and link
   them with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kafka/ckafka-ctimer-cprocessor-clog-csetbody-security-configuration -->
# Security configuration (optional)

Last updated: 9/30/2026

## Procedure

1. Modify the Bean `KafkaAvroSerializerBean` inside
   `Kafka_Avro_Beans` with the following content:

   ```
   package org.example.local_project.beansjar.kafka_avro_beans;

   import java.util.HashMap;
   import java.util.Map;
   import io.confluent.kafka.schemaregistry.client.CachedSchemaRegistryClient;
   import io.confluent.kafka.schemaregistry.client.SchemaRegistryClientConfig;
   import io.confluent.kafka.serializers.KafkaAvroSerializer;
   import io.confluent.kafka.serializers.KafkaAvroSerializerConfig;

   public class KafkaAvroSerializerBean extends KafkaAvroSerializer {

   	@Override
   	public void configure(KafkaAvroSerializerConfig config) {

         	Map<String, String> configs = new HashMap<String, String>();
         
   configs.put(SchemaRegistryClientConfig.BASIC_AUTH_CREDENTIALS_SOURCE,
      config.getString("basic.auth.credentials.source"));
   configs.put(SchemaRegistryClientConfig.USER_INFO_CONFIG, 
      config.getPassword("basic.auth.user.info").value());       		
          this.schemaRegistry = new CachedSchemaRegistryClient(  
             config.getSchemaRegistryUrls(), 1000, configs);
          this.strategyUsesSchema(true);
          this.autoRegisterSchema = true;
   //	  this.useSchemaReflection = true;
   //	  this.normalizeSchema = true;
   //	  this.useLatestVersion = true; 
   //	  this.avroReflectionAllowNull = true;
   	}
   }
   ```
2. Modity the Bean `KafkaAvroDeserializerBean` inside
   `Kafka_Avro_Beans` with the following content:

   ```
   package org.example.local_project.beansjar.kafka_avro_beans;
    
   import java.util.HashMap;
   import java.util.Map;
   import io.confluent.kafka.schemaregistry.client.CachedSchemaRegistryClient;
   import io.confluent.kafka.schemaregistry.client.SchemaRegistryClientConfig;
   import io.confluent.kafka.serializers.KafkaAvroDeserializer;
   import io.confluent.kafka.serializers.KafkaAvroDeserializerConfig;
    
   public class KafkaAvroDeserializerBean extends KafkaAvroDeserializer {
    
   @Override
   public void configure(KafkaAvroDeserializerConfig config) {
       Map<String, String> configs = new HashMap<String, String>();
         
       configs.put(SchemaRegistryClientConfig.BASIC_AUTH_CREDENTIALS_SOURCE,
           config.getString("basic.auth.credentials.source"));
       configs.put(SchemaRegistryClientConfig.USER_INFO_CONFIG, 
           config.getPassword("basic.auth.user.info").value());       		
       this.schemaRegistry = new CachedSchemaRegistryClient(  
           config.getSchemaRegistryUrls(), 1000, configs);
       this.useSpecificAvroReader = false;
   }}
   ```
3. Create context variables for the Route, API\_KEY of String type
   and API\_SECRET of Password type with values of API KEY and API
   SECRET issued by Confluent.

   For more information on context parameters, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).

   For more information about API KEY and API SECRET, see [Confluent documentation](https://docs.confluent.io/cloud/current/access-management/authenticate/api-keys/api-keys.html#use-api-keys-to-control-access-in-ccloud).
4. Create context parameters SCHEMA\_REGISTRY\_KEY of String type and
   SCHEMA\_REGISTRY\_SECRET of Password type with values of SCHEMA
   REGISTRY KEY and SCHEMA REGISTRY SECRET issued by Confluent.
5. In the Advanced settings tab of the
   cKafka components `SendMessageToKafka`
   and `ReceiveMessageFromKafka`, add the following parameters in
   the Kafka Properties field.

   | Name | Value |
   | --- | --- |
   | "additionalProperties.basic.auth.user.info" | "RAW(" + context.SCHEMA\_REGISTRY\_KEY + ":" + context.SCHEMA\_REGISTRY\_SECRET+")" |
   | "additionalProperties.basic.auth.credentials.source" | "USER\_INFO" |
   | "additionalProperties.security.protocol" | "SASL\_SSL" |
   | "additionalProperties.sasl.jaas.config" | "RAW(org.apache.kafka.common.security.plain.PlainLoginModule required username='"+ context.API\_KEY +"' password='" + context.API\_SECRET + "';)" |
   | "additionalProperties.sasl.mechanism" | "PLAIN" |

   For more information on the security configuration, see the Confluent
   Kafka security documentation <https://docs.confluent.io/platform/current/security/auth-overview.html>.
