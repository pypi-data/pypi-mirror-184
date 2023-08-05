from functools import lru_cache

from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

sc = spark.sparkContext
sql = spark.sql

# We'll later overwrite the secrets.get() method of dbutils
dbutils, __dbutils = DBUtils(spark), DBUtils(spark)

__secrets_cache = {}


@lru_cache(maxsize=10)
def __get_cached_secret(scope: str, key: str) -> str:
    if cached_secret := __secrets_cache.get((scope, key), None) is not None:
        return cached_secret

    __secrets_cache[(scope, key)] = __dbutils.secrets.get(scope, key)
    return __secrets_cache[(scope, key)]


dbutils.secrets.get = __get_cached_secret


def redact_string(s: str) -> str:
    if not s:
        return s

    s = str(s)
    for _, v in __secrets_cache.items():
        s.replace(v, "*****")

    return s


from .pipeline import *

__all__ = ["Pipeline", "configuration", "sources"]
