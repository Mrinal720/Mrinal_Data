import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from lib import ConfigReader

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG4J_URI = (PROJECT_ROOT / "log4j.properties").as_uri()


def resolve_path(path):
    """Relative paths are resolved against the project root; absolute / hdfs:// paths are kept."""
    if "://" in path or os.path.isabs(path):
        return path
    return str(PROJECT_ROOT / path)


def get_spark_session(env):
    builder = SparkSession.builder.config(conf=ConfigReader.get_pyspark_config(env))
    if env == "LOCAL":
        builder = builder.config("spark.driver.extraJavaOptions", f"-Dlog4j2.configurationFile={LOG4J_URI}")
    else:
        builder = builder.enableHiveSupport()
    return builder.getOrCreate()


def get_orders_schema():
    return StructType([
        StructField("order_id", IntegerType()),
        StructField("order_date", StringType()),
        StructField("order_customer_id", IntegerType()),
        StructField("order_status", StringType()),
    ])


def get_customers_schema():
    return StructType([
        StructField("customer_id", IntegerType()),
        StructField("customer_fname", StringType()),
        StructField("customer_lname", StringType()),
        StructField("username", StringType()),
        StructField("password", StringType()),
        StructField("address", StringType()),
        StructField("city", StringType()),
        StructField("state", StringType()),
        StructField("pincode", StringType()),
    ])
