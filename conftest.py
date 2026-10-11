import csv

import pytest

from lib import Utils


@pytest.fixture(scope="session")
def spark():
    """One local SparkSession shared by every test."""
    session = Utils.get_spark_session("LOCAL")
    yield session
    session.stop()


@pytest.fixture(scope="session")
def expected_state_counts():
    path = Utils.resolve_path("data/test_result/state_aggregate.csv")
    with open(path, newline="") as f:
        return {row["state"]: int(row["count"]) for row in csv.DictReader(f)}
