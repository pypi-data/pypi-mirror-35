import os

import findspark
import pytest


class SparkHome(object):

    def __init__(self, pytest_config):
        self.config = pytest_config

        self._path, source_name = self._detect_path()
        if self._path:
            self._path = os.path.abspath(self._path)
            if not os.path.exists(self._path):
                raise OSError(
                    "SPARK_HOME path specified in %s does not exist: %s"
                    % (source_name, self._path))

    @property
    def path(self):
        return self._path

    @property
    def version(self):
        if self.path:
            return self._get_spark_version(self.path)

    def _get_spark_version(self, spark_home):
        release_info_filename = os.path.join(spark_home, 'RELEASE')
        if os.path.exists(release_info_filename):
            with open(release_info_filename) as release_info:
                return release_info.read()

    def _locations(self):
        yield (
            self.config.option.spark_home,
            'config (command line option "--spark_home")',
        )
        yield (self.config.getini('spark_home'), 'config (pytest.ini)')
        yield (os.environ.get('SPARK_HOME'), 'ENV')

    def _detect_path(self):
        for path, description in self._locations():
            if path:
                return path, description
        return None, None


def pytest_addoption(parser):
    parser.addini('spark_home', 'Spark install directory (SPARK_HOME).')
    parser.addoption(
        '--spark_home',
        dest='spark_home',
        help='Spark install directory (SPARK_HOME).',
    )


def pytest_configure(config):
    spark_home = SparkHome(config).path

    if spark_home:
        findspark.init(spark_home)


def pytest_report_header(config, startdir):
    spark_ver = SparkHome(config).version
    if spark_ver:
        spark_ver = spark_ver.strip().replace('\n', ' | ')
        return "spark version -- " + spark_ver


def reduce_logging(sc):
    """Reduce logging in SparkContext instance."""

    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.OFF)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.OFF)


@pytest.fixture(scope='session')
def _spark_session():
    """Internal fixture for SparkSession instance.

    Yields SparkSession instance if it is supported by the pyspark
    version, otherwise yields None.

    Required to correctly initialize `spark_context` fixture after
    `spark_session` fixture.

    ..note::
        It is not possible to create SparkSession from the existing
        SparkContext.
    """

    try:
        from pyspark.sql import SparkSession
    except ImportError:
        yield
    else:
        session = SparkSession.builder.enableHiveSupport().getOrCreate()
        yield session
        session.stop()


@pytest.fixture(scope='session')
def spark_context(_spark_session):
    """Return a SparkContext instance with reduced logging
    (session scope).
    """

    if _spark_session is None:
        from pyspark import SparkContext

        # pyspark 1.x: create SparkContext instance
        sc = SparkContext()
    else:
        # pyspark 2.x: get SparkContext from SparkSession fixture
        sc = _spark_session.sparkContext

    reduce_logging(sc)
    yield sc

    if _spark_session is None:
        sc.stop()  # pyspark 1.x: stop SparkContext instance


@pytest.fixture(scope='session')
def spark_session(_spark_session):
    """Return a Hive enabled SparkSession instance with reduced logging
    (session scope).

    Available from Spark 2.0 onwards.
    """

    if _spark_session is None:
        raise Exception(
            'The "spark_session" fixture is only available on spark 2.0 '
            'and above. Please use the spark_context fixture and instanciate '
            'a SQLContext or HiveContext from it in your tests.'
        )
    else:
        reduce_logging(_spark_session.sparkContext)
        yield _spark_session
