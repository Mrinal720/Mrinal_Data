import pytest

from lib import ConfigReader, DataManipulation, DataReader


@pytest.mark.config
def test_app_config_local():
    conf = ConfigReader.get_app_config("LOCAL")
    assert conf["orders.file.path"] == "data/orders.csv"
    assert conf["customers.file.path"] == "data/customers.csv"


@pytest.mark.config
def test_unknown_env_raises_key_error():
    with pytest.raises(KeyError):
        ConfigReader.get_app_config("DOES_NOT_EXIST")


@pytest.mark.read
def test_read_customers_df(spark):
    assert DataReader.read_customers(spark, "LOCAL").count() == 2000


@pytest.mark.read
def test_read_orders_df(spark):
    assert DataReader.read_orders(spark, "LOCAL").count() == 8000


@pytest.mark.transformation
def test_filter_closed_orders(spark):
    orders_df = DataReader.read_orders(spark, "LOCAL")
    assert DataManipulation.filter_closed_orders(orders_df).count() == 788


@pytest.mark.transformation
@pytest.mark.parametrize("status, expected_count", [('CANCELED', 422), ('CLOSED', 788), ('COMPLETE', 2357), ('ON_HOLD', 558), ('PAYMENT_REVIEW', 167), ('PENDING', 709), ('PENDING_PAYMENT', 1562), ('PROCESSING', 1203), ('SUSPECTED_FRAUD', 234)])
def test_filter_orders_generic(spark, status, expected_count):
    orders_df = DataReader.read_orders(spark, "LOCAL")
    assert DataManipulation.filter_orders_generic(orders_df, status).count() == expected_count


@pytest.mark.transformation
def test_join_closed_orders_with_customers(spark):
    orders_df = DataManipulation.filter_closed_orders(DataReader.read_orders(spark, "LOCAL"))
    customers_df = DataReader.read_customers(spark, "LOCAL")
    assert DataManipulation.join_orders_customers(orders_df, customers_df).count() == 739


@pytest.mark.transformation
def test_count_orders_state(spark, expected_state_counts):
    orders_df = DataManipulation.filter_closed_orders(DataReader.read_orders(spark, "LOCAL"))
    customers_df = DataReader.read_customers(spark, "LOCAL")
    joined_df = DataManipulation.join_orders_customers(orders_df, customers_df)
    actual = {row["state"]: row["count"] for row in DataManipulation.count_orders_state(joined_df).collect()}
    assert actual == expected_state_counts
