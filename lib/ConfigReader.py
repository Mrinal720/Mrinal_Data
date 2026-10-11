import configparser
from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent.parent / "configs"


def _read(file_name):
    parser = configparser.ConfigParser()
    parser.optionxform = str  # keep key case (e.g. spark.driver.extraJavaOptions)
    if not parser.read(CONFIG_DIR / file_name):
        raise FileNotFoundError(f"Config file not found: {CONFIG_DIR / file_name}")
    return parser


def get_app_config(env):
    """Return the [env] section of configs/application.conf as a dict (KeyError if env unknown)."""
    return dict(_read("application.conf")[env])


def get_pyspark_config(env):
    """Return a SparkConf built from the [env] section of configs/pyspark.conf."""
    from pyspark import SparkConf  # imported lazily so config tests don't need Spark

    conf = SparkConf()
    for key, value in _read("pyspark.conf")[env].items():
        conf.set(key, value)
    return conf
