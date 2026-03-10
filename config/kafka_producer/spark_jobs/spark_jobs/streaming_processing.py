from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType

spark = SparkSession.builder.appName("StreamingProcessing").getOrCreate()

schema = StructType() \
    .add("patient_id", IntegerType()) \
    .add("event_type", StringType()) \
    .add("timestamp", DoubleType())

df_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "clinical_events") \
    .load()

df_parsed = df_stream.selectExpr("CAST(value AS STRING) as json").select(from_json("json", schema).alias("data")).select("data.*")

df_agg = df_parsed.groupBy("event_type").count()

query = df_agg.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()
