from lib import ConfigReader, Utils


def read_customers(spark, env):
    path = Utils.resolve_path(ConfigReader.get_app_config(env)["customers.file.path"])
    return spark.read.csv(path, header=False, schema=Utils.get_customers_schema())


def read_orders(spark, env):
    path = Utils.resolve_path(ConfigReader.get_app_config(env)["orders.file.path"])
    return spark.read.csv(path, header=False, schema=Utils.get_orders_schema())
