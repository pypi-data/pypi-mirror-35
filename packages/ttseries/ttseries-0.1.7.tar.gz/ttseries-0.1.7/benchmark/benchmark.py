# encoding:utf-8

import datetime

import numpy
import pandas
import pytest
import pytz
import redis

import ttseries
from ttseries.serializers import DumpySerializer


class InitData(object):
    def __init__(self):

        self.now = datetime.datetime.now()
        self.timestamp = self.now.timestamp()

    def prepare_data(self, length=1000):
        results = []
        for i in range(length):
            results.append((self.timestamp + i, i))
        return results

    def prepare_data_with_dict(self, length=1000):

        results = []
        for i in range(length):
            results.append((self.timestamp + i, {"value": i}))
        return results

    def prepare_data_with_list(self, length):
        results = []
        for i in range(length):
            results.append((self.timestamp + i, [i + 1, "A"]))
        return results

    def prepare_numpy_array(self, length):
        results = []
        for i in range(length):
            results.append((self.timestamp + i, i))
        array = numpy.array(results)
        return array

    def prepare_numpy_array_dtype(self, length):
        results = []
        for i in range(length):
            results.append((self.timestamp + i, i))
        array = numpy.array(results, dtype=[("timestamp", "float64"), ("value", "i")])
        return array

    def prepare_pd_dataframe(self, length):

        date_range = pandas.date_range(self.now, periods=length,
                                       freq="1min", tz=pytz.UTC)

        return pandas.DataFrame([i + 1 for i in range(len(date_range))],
                                index=date_range, columns=["values"])


init_data = InitData()
key = "APPL:SECOND:10"


@pytest.fixture()
def simple_timeseries_dumpy():
    redis_client = redis.StrictRedis()
    series = ttseries.RedisSampleTimeSeries(redis_client, serializer_cls=DumpySerializer)
    yield series
    series.flush()


@pytest.fixture()
def simple_time_series():
    redis_client = redis.StrictRedis()
    series = ttseries.RedisSampleTimeSeries(redis_client)
    yield series
    series.flush()


@pytest.fixture()
def numpy_timeseries():
    redis_client = redis.StrictRedis()
    series = ttseries.RedisNumpyTimeSeries(redis_client)
    yield series
    series.flush()


@pytest.fixture()
def numpy_timeseries_dtype():
    redis_client = redis.StrictRedis()
    series = ttseries.RedisNumpyTimeSeries(redis_client, dtype=[("timestamp", "float64"), ("value", "i")],
                                           timestamp_column_name="timestamp")
    yield series
    series.flush()


@pytest.fixture()
def hash_timeseries():
    redis_client = redis.StrictRedis()
    series = ttseries.RedisHashTimeSeries(redis_client, serializer_cls=DumpySerializer)
    yield series
    series.flush()


@pytest.fixture()
def pandas_timeseries():
    redis_client = redis.StrictRedis()
    dtypes = {"value": "int64"}
    series = ttseries.RedisPandasTimeSeries(redis_client, timezone=pytz.UTC,
                                            columns=["value"],
                                            dtypes=dtypes)
    yield series
    series.flush()


@pytest.mark.usefixtures("simple_timeseries_dumpy")
@pytest.mark.benchmark(group="simple_dumpy", disable_gc=True)
@pytest.mark.parametrize('data', [init_data.prepare_data(1000),
                                  init_data.prepare_data(10000),
                                  init_data.prepare_data(100000)])
@pytest.mark.parametrize("chunks", [2000, 5000, 6000, 10000])
def test_add_simple_timeseries_without_serializer(simple_timeseries_dumpy,
                                                  benchmark,
                                                  data,
                                                  chunks):
    @benchmark
    def bench():
        simple_timeseries_dumpy.add_many(name=key, array=data,
                                         chunks_size=chunks)

        simple_timeseries_dumpy.flush()


@pytest.mark.usefixtures("simple_timeseries_dumpy")
@pytest.mark.benchmark(group="simple_dumpy", disable_gc=True)
@pytest.mark.parametrize("length", [1000, 10000, 100000])
def test_get_simple_timeseries_dumpy_serializer(simple_timeseries_dumpy,
                                                benchmark,
                                                length):
    simple_timeseries_dumpy.add_many(key,
                                     init_data.prepare_data(length))

    @benchmark
    def bench():
        simple_timeseries_dumpy.get_slice(key)


@pytest.mark.usefixtures("simple_timeseries_dumpy")
@pytest.mark.benchmark(group="simple_dumpy", disable_gc=True)
@pytest.mark.parametrize("length", [1000, 10000, 100000])
def test_iter_simple_timeseries_dumpy_serializer(simple_timeseries_dumpy,
                                                 benchmark,
                                                 length):
    simple_timeseries_dumpy.add_many(key, init_data.prepare_data(length))

    @benchmark
    def bench():
        for item in simple_timeseries_dumpy.iter(key):
            pass


@pytest.mark.usefixtures("simple_time_series")
@pytest.mark.benchmark(group="simple", disable_gc=True)
@pytest.mark.parametrize('data', [init_data.prepare_data_with_dict(1000),
                                  init_data.prepare_data_with_dict(10000),
                                  init_data.prepare_data_with_dict(100000)])
def test_simple_timeseries_serializer(simple_time_series, benchmark, data):
    @benchmark
    def bench():
        simple_time_series.add_many(name=key, array=data)

        simple_time_series.flush()


@pytest.mark.usefixtures("simple_time_series")
@pytest.mark.benchmark(group="simple", disable_gc=True)
@pytest.mark.parametrize("length", [1000, 10000, 100000])
def test_get_simple_timeseries_serializer(simple_time_series,
                                          benchmark,
                                          length):
    simple_time_series.add_many(key,
                                init_data.prepare_data_with_dict(length))

    @benchmark
    def bench():
        simple_time_series.get_slice(key)


@pytest.mark.usefixtures("numpy_timeseries")
@pytest.mark.benchmark(group="numpy", disable_gc=True)
@pytest.mark.parametrize("length", [1000, 10000, 100000])
def test_get_numpy_timeseries_serializer(numpy_timeseries,
                                         benchmark,
                                         length):
    numpy_timeseries.add_many(key,
                              init_data.prepare_numpy_array(length))

    @benchmark
    def bench():
        numpy_timeseries.get_slice(key)


@pytest.mark.usefixtures("numpy_timeseries")
@pytest.mark.benchmark(group="numpy", disable_gc=True)
@pytest.mark.parametrize('data', [init_data.prepare_numpy_array(1000),
                                  init_data.prepare_numpy_array(10000),
                                  init_data.prepare_numpy_array(100000)])
@pytest.mark.parametrize("chunks", [2000, 5000, 8000, 10000])
def test_add_numpy_timeseries_serializer(numpy_timeseries,
                                         benchmark,
                                         data, chunks):
    @benchmark
    def bench():
        numpy_timeseries.add_many(name=key, array=data,
                                  chunks_size=chunks)

        numpy_timeseries.flush()


@pytest.mark.usefixtures("hash_timeseries")
@pytest.mark.benchmark(group="hash", disable_gc=True)
@pytest.mark.parametrize("length", [1000, 10000, 100000])
def test_get_hash_timeseries_without_serializer(hash_timeseries,
                                                benchmark,
                                                length):
    hash_timeseries.add_many(key,
                             init_data.prepare_data(length))

    @benchmark
    def bench():
        hash_timeseries.get_slice(key)


@pytest.mark.usefixtures("hash_timeseries")
@pytest.mark.benchmark(group="hash", disable_gc=True)
@pytest.mark.parametrize('data', [init_data.prepare_data(1000),
                                  init_data.prepare_data(10000),
                                  init_data.prepare_data(100000)])
def test_add_hash_timeseries_without_serializer(hash_timeseries,
                                                benchmark,
                                                data):
    @benchmark
    def bench():
        hash_timeseries.add_many(name=key, array=data)

        hash_timeseries.flush()


@pytest.mark.usefixtures("numpy_timeseries_dtype")
@pytest.mark.benchmark(group="numpy_dtype", disable_gc=True)
@pytest.mark.parametrize("length", [1000, 10000, 100000])
def test_get_numpy_dtype_timeseries_serializer(numpy_timeseries_dtype,
                                               benchmark,
                                               length):
    numpy_timeseries_dtype.add_many(key,
                                    init_data.prepare_numpy_array_dtype(length))

    @benchmark
    def bench():
        numpy_timeseries_dtype.get_slice(key)


@pytest.mark.usefixtures("numpy_timeseries_dtype")
@pytest.mark.benchmark(group="numpy_dtype", disable_gc=True)
@pytest.mark.parametrize('data', [init_data.prepare_numpy_array_dtype(1000),
                                  init_data.prepare_numpy_array_dtype(10000),
                                  init_data.prepare_numpy_array_dtype(100000)])
def test_add_numpy_dtype_timeseries_serializer(numpy_timeseries_dtype,
                                               benchmark,
                                               data):
    @benchmark
    def bench():
        numpy_timeseries_dtype.add_many(name=key, array=data)

        numpy_timeseries_dtype.flush()


@pytest.mark.usefixtures("pandas_timeseries")
@pytest.mark.benchmark(group="pandas", disable_gc=True)
@pytest.mark.parametrize("data_frame", [init_data.prepare_pd_dataframe(1000),
                                        init_data.prepare_pd_dataframe(10000),
                                        init_data.prepare_pd_dataframe(100000)])
def test_add_pandas_timeseries_serializer(pandas_timeseries,
                                          benchmark,
                                          data_frame):
    @benchmark
    def bench():
        pandas_timeseries.add_many(name=key, data_frame=data_frame)
        pandas_timeseries.flush()


@pytest.mark.usefixtures("pandas_timeseries")
@pytest.mark.benchmark(group="pandas", disable_gc=True)
@pytest.mark.parametrize("length", [1000, 10000, 100000])
def test_get_pandas_timeseries_serializer(pandas_timeseries,
                                          benchmark,
                                          length):
    pandas_timeseries.add_many(key, init_data.prepare_pd_dataframe(length))

    @benchmark
    def bench():
        pandas_timeseries.get_slice(key)
