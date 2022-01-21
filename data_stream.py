import logging
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
from pyspark.sql.functions import col, from_json, window

# TODO Create a schema for incoming resources - From the messages in the JSON - Done
schema = StructType(
    [
        StructField("crime_id", StringType(), True),
        StructField("original_crime_type_name", StringType(), True),
        StructField("report_date", StringType(), True),
        StructField("call_date", StringType(), True),
        StructField("offense_date", StringType(), True),
        StructField("call_time", StringType(), True),
        StructField("call_date_time", TimestampType(), True),
        StructField("disposition", StringType(), True),
        StructField("address", StringType(), True),
        StructField("city", StringType(), True),
        StructField("state", StringType(), True),
        StructField("agency_id", StringType(), True),
        StructField("address_type", StringType(), True),
        StructField("common_location", StringType(), True),
    ]
)


def run_spark_job(spark):
    # TODO Create Spark Configuration - Done
    # Create Spark configurations with max offset of 200 per trigger - Done
    # set up correct bootstrap server and port - Done

    KAFKA_TOPIC = "crimes.calls"
    BOOTSTRAP_SERVERS = "localhost:9092"

    df = (
        spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS)
            .option("startingOffsets", "earliest")
            .option("subscribe", KAFKA_TOPIC)
            .option("maxOffsetsPerTrigger", 200)
            .load())

    # Show schema for the incoming resources for checks - Done
    df.printSchema()

    # TODO extract the correct column from the kafka input resources
    # Take only value and convert it to String - Done
    kafka_df = df.selectExpr("CAST(value AS STRING) as calls", "timestamp")
    kafka_df.printSchema()

    service_table = kafka_df \
        .select(from_json(col("calls"), schema).alias("DF"), col("timestamp")) \
        .select("DF.*", "timestamp")

    logger.info("\nService Table Schema\n")
    service_table.printSchema()

    # TODO select original_crime_type_name and disposition
    distinct_table = (service_table.select(
        col("original_crime_type_name"),
        col("disposition"),
        col("call_date_time"),
        col("timestamp")
    ).withWatermark("call_date_time", "5 minutes"))

    distinct_table.printSchema()  # check it conforms to expected schema

    # count the number of original crime type to
    agg_df = (
        distinct_table
            .groupBy("original_crime_type_name", window("call_date_time", "60 minutes"))
            .count()
            .orderBy("count", ascending=False))

    # TODO Q1. Submit a screen shot of a batch ingestion of the aggregation
    # TODO write output stream
    query = (agg_df
             .writeStream
             .outputMode("complete")
             .format("console")
             .option("truncate", "false")
             .option("numRows", 30)
             .start())

    # TODO attach a ProgressReporter
    query.awaitTermination()

    # TODO get the right radio code json path - Done
    radio_code_json_filepath = "radio_code.json"
    radio_code_df = spark.read.json(radio_code_json_filepath)

    # clean up your data so that the column names match on radio_code_df and agg_df
    # we will want to join on the disposition code

    # TODO rename disposition_code column to disposition
    radio_code_df = radio_code_df.withColumnRenamed("disposition_code", "disposition")

    radio_code_df.show(4)

    # TODO join on disposition column
    join_query = (
        agg_df.join(radio_code_df, "disposition")
            .writeStream.format("console")
            .queryName("joinWithRadio")
            .start()
    )

    join_query.awaitTermination()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    # TODO Create Spark in Standalone mode
    spark = (
        SparkSession.builder.config("spark.ui.port", 3000)
            .master("local[*]")
            .appName("KafkaSparkStructuredStreaming")
            .getOrCreate()
    )

    logger.info("Spark started")
    run_spark_job(spark)

    spark.stop()
