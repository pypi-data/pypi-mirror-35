# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import datetime

from pyathenajdbc.error import *  

__version__ = '1.3.4'
# __athena_driver_version__ = '1.1.0'

# Globals https://www.python.org/dev/peps/pep-0249/#globals
apilevel = '2.0'
threadsafety = 3
paramstyle = 'pyformat'
name = 'pyathenajdbc_qubole'

# ATHENA_JAR = 'AthenaJDBC41-{0}.jar'.format(__athena_driver_version__)
# ATHENA_DRIVER_DOWNLOAD_URL = 'https://s3.amazonaws.com/athena-downloads/drivers/{0}'.format(
#     ATHENA_JAR)
# ATHENA_DRIVER_CLASS_NAME = 'com.amazonaws.athena.jdbc.AthenaDriver'
# ATHENA_CONNECTION_STRING = 'jdbc:awsathena://athena.{region}.amazonaws.com:443/hive/{schema}/'

ATHENA_JAR = 'QuboleJDBC41.jar'
ATHENA_DRIVER_DOWNLOAD_URL = 'https://s3.amazonaws.com/athena-downloads/drivers/{0}'.format(ATHENA_JAR) # how does this work?
# ATHENA_DRIVER_DOWNLOAD_URL = 'https://s3.amazonaws.com/paid-qubole/jdbc/{0}'.format(ATHENA_JAR) # how does this work?
ATHENA_DRIVER_CLASS_NAME = 'com.qubole.jdbc.jdbc41.core.QDriver'
# ATHENA_CONNECTION_STRING = 'jdbc:qubole://sqlcommand/{schema}/'
ATHENA_CONNECTION_STRING = 'jdbc:qubole://presto/presto/{schema}/'


class DBAPITypeObject:
    """Type Objects and Constructors

    https://www.python.org/dev/peps/pep-0249/#type-objects-and-constructors
    """
    def __init__(self, *values):
        self.values = values

    def __cmp__(self, other):
        if other in self.values:
            return 0
        if other < self.values:
            return 1
        else:
            return -1

    def __eq__(self, other):
        return other in self.values


STRING = DBAPITypeObject('CHAR', 'NCHAR', 'VARCHAR', 'NVARCHAR', 'LONGVARCHAR', 'LONGNVARCHAR',
                         'ARRAY', 'JAVA_OBJECT')
BINARY = DBAPITypeObject('BINARY', 'VARBINARY', 'LONGVARBINARY')
BOOLEAN = DBAPITypeObject('BOOLEAN')
NUMBER = DBAPITypeObject('TINYINT', 'SMALLINT', 'BIGINT', 'INTEGER',
                         'REAL', 'DOUBLE', 'FLOAT', 'DECIMAL', 'NUMERIC')
DATE = DBAPITypeObject('DATE')
DATETIME = DBAPITypeObject('TIMESTAMP')


Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime


def connect(user=None, api_token=None, schema_name='default',
            jvm_path=None, jvm_options=None, converter=None, formatter=None,
            driver_path=None, **kwargs):
    from pyathenajdbc.connection import Connection
    return Connection(user, api_token, schema_name,
                      jvm_path, jvm_options, converter, formatter,
                      driver_path, **kwargs)
