import logging
import sys

from lib import DataManipulation, DataReader, Utils

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("retail")


def main(env):
    spark = Utils.get_spark_session(env)
    logger.info("Created Spark session for env=%s", env)

    orders_df = DataReader.read_orders(spark, env)
    closed_orders = DataManipulation.filter_closed_orders(orders_df)
    customers_df = DataReader.read_customers(spark, env)
    joined_df = DataManipulation.join_orders_customers(closed_orders, customers_df)
    aggregated = DataManipulation.count_orders_state(joined_df)

    aggregated.orderBy("count", ascending=False).show(50)
    logger.info("Job finished")
    spark.stop()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify the environment, e.g.: python application_main.py LOCAL")
        sys.exit(-1)
    main(sys.argv[1].upper())
