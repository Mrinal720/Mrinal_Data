from pyspark.sql.functions import col


def filter_orders_generic(orders_df, status):
    return orders_df.filter(col("order_status") == status)


def filter_closed_orders(orders_df):
    return filter_orders_generic(orders_df, "CLOSED")


def join_orders_customers(orders_df, customers_df):
    return orders_df.join(customers_df, orders_df.order_customer_id == customers_df.customer_id, "inner")


def count_orders_state(joined_df):
    return joined_df.groupBy("state").count()
