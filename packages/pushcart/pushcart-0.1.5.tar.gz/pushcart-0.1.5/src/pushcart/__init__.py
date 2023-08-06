from functools import lru_cache

try:
    from pyspark.dbutils import DBUtils
except ImportError:
    # TODO: Create DBUtils wrapper using Databricks CLI and keyring
    pass

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

sc = spark.sparkContext
sql = spark.sql

# We'll later overwrite the secrets.get() method of dbutils
dbutils, __dbutils = DBUtils(spark), DBUtils(spark)

__secrets_cache = {}


# TODO: Use keyring to pull secrets from the local keyring when remote
@lru_cache(maxsize=50)
def __get_cached_secret(scope: str, key: str) -> str:
    return __dbutils.secrets.get(scope, key)


dbutils.secrets.get = __get_cached_secret

from .pipeline import *

__all__ = ["Pipeline", "Release", "configuration", "sources"]
