from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession \
        .builder \
        .appName("readfromkafka") \
        .master("local[*]") \
        .getOrCreate()

kafka_bootstrap_servers = "172.31.9.181:9092"
topic_name = "worldmoney.filebeat.spark"

print("=================================Start Read Kafka Topic=================================")
df = spark \
  .readStream\
  .format("kafka") \
  .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
  .option("subscribe", topic_name) \
  .load()
print("=================================End Read Kafka Topic=================================")

print(df.printSchema())


## complete 모드 사용시에는 aggregation 필요 
query = df.writeStream \
        .format("console") \
        .outputMode("complete") \
        .start()

query.awaitTermination()

# query = df.writeStream \
# .outputMode("append") \
# .queryName("writing_to_es") \
# .format("org.elasticsearch.spark.sql") \
# .option("checkpointLocation", "/tmp/") \
# .option("es.resource", "index/type") \
# .option("es.nodes", "localhost") \
# .start()
