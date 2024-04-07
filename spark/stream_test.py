from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession \
        .builder \
        .appName("readfromcsv") \
        .master("local[*]") \
        .getOrCreate()

schema = StructType(
    [
        StructField('id', IntegerType(), True)
        ,StructField('name', StringType(), True)
        ,StructField('age', IntegerType(), True)
        ,StructField('profession', StringType(), True)
        ,StructField('city', StringType(), True)
        ,StructField('salary', DoubleType(), True)
     ]
)

customer = spark.readStream.format("csv").schema(schema) \
            .option("header", True) \
            .option("maxFilesPerTrigger", 1) \
            .load("./files")

print(f"isStreaming : {customer.isStreaming}")

print(f"schema : {customer.printSchema()}")

average_salaries = customer.groupby("profession") \
                    .agg((avg("salary").alias("average_salary")), (count("profession").alias("count"))) \
                    .sort(desc("average_salary"))

query = average_salaries.writeStream.format("console").outputMode("complete").start()

query.awaitTermination()