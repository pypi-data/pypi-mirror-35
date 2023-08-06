# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import contextlib
import re
import time
import unittest
from concurrent import futures
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import date, datetime
from decimal import Decimal
from random import randint

from past.builtins.misc import xrange

from pyathenajdbc import BINARY, BOOLEAN, DATE, DATETIME, NUMBER, STRING, connect
from pyathenajdbc.cursor import Cursor
from pyathenajdbc.error import (DatabaseError, NotSupportedError, ProgrammingError)
from tests.conftest import ENV, SCHEMA
from tests.util import with_cursor


class TestCursor(unittest.TestCase):
    """Reference test case is following:

    https://github.com/dropbox/PyHive/blob/master/pyhive/tests/dbapi_test_case.py
    https://github.com/dropbox/PyHive/blob/master/pyhive/tests/test_hive.py
    https://github.com/dropbox/PyHive/blob/master/pyhive/tests/test_presto.py
    """

    def connect(self):
        return connect(schema_name=SCHEMA)

    @with_cursor
    def test_fetchone(self, cursor):
        cursor.execute('SELECT * FROM one_row')
        self.assertEqual(cursor.rownumber, 0)
        self.assertEqual(cursor.fetchone(), (1,))
        self.assertEqual(cursor.rownumber, 1)
        self.assertEqual(cursor.fetchone(), None)
        self.assertIsNotNone(cursor.query_id)
        self.assertIsNotNone(cursor.output_location)
        self.assertIsNotNone(cursor.completion_date_time)
        self.assertIsInstance(cursor.completion_date_time, datetime)
        self.assertIsNotNone(cursor.submission_date_time)
        self.assertIsInstance(cursor.submission_date_time, datetime)
        self.assertIsNotNone(cursor.data_scanned_in_bytes)
        self.assertIsNotNone(cursor.execution_time_in_millis)

    @with_cursor
    def test_fetchall(self, cursor):
        cursor.execute('SELECT * FROM one_row')
        self.assertEqual(cursor.fetchall(), [(1,)])
        cursor.execute('SELECT a FROM many_rows ORDER BY a')
        self.assertEqual(cursor.fetchall(), [(i,) for i in xrange(10000)])

    @with_cursor
    def test_null_param(self, cursor):
        cursor.execute('SELECT %(param)s FROM one_row', {'param': None})
        self.assertEqual(cursor.fetchall(), [(None,)])

    @with_cursor
    def test_iterator(self, cursor):
        cursor.execute('SELECT * FROM one_row')
        self.assertEqual(list(cursor), [(1,)])
        self.assertRaises(StopIteration, cursor.__next__)

    @with_cursor
    def test_description_initial(self, cursor):
        self.assertEqual(cursor.description, None)

    @with_cursor
    def test_description_failed(self, cursor):
        try:
            cursor.execute('blah_blah')
        except DatabaseError:
            pass
        self.assertEqual(cursor.description, None)

    @with_cursor
    def test_bad_query(self, cursor):
        def run():
            cursor.execute('SELECT does_not_exist FROM this_really_does_not_exist')
            cursor.fetchone()
        self.assertRaises(DatabaseError, run)

    @with_cursor
    def test_fetchone_no_data(self, cursor):
        self.assertRaises(ProgrammingError, cursor.fetchone)

    @with_cursor
    def test_fetchmany(self, cursor):
        cursor.execute('SELECT * FROM many_rows LIMIT 15')
        self.assertEqual(len(cursor.fetchmany(10)), 10)
        self.assertEqual(len(cursor.fetchmany(10)), 5)

    @with_cursor
    def test_arraysize(self, cursor):
        cursor.arraysize = 5
        cursor.execute('SELECT * FROM many_rows LIMIT 20')
        self.assertEqual(len(cursor.fetchmany()), 5)

    @with_cursor
    def test_arraysize_default(self, cursor):
        self.assertEqual(cursor.arraysize, Cursor.DEFAULT_FETCH_SIZE)

    @with_cursor
    def test_invalid_arraysize(self, cursor):
        with self.assertRaises(ProgrammingError):
            cursor.arraysize = 10000
        with self.assertRaises(ProgrammingError):
            cursor.arraysize = -1

    @with_cursor
    def test_no_params(self, cursor):
        self.assertRaises(DatabaseError, lambda: cursor.execute(
            'SELECT %(param)s FROM one_row'))
        self.assertRaises(KeyError, lambda: cursor.execute(
            'SELECT %(param)s FROM one_row', {'a': 1}))

    @with_cursor
    def test_contain_special_character_query(self, cursor):
        cursor.execute("""
                       SELECT col_string FROM one_row_complex
                       WHERE col_string LIKE '%str%'
                       """)
        self.assertEqual(cursor.fetchall(), [('a string', )])
        cursor.execute("""
                       SELECT col_string FROM one_row_complex
                       WHERE col_string LIKE '%%str%%'
                       """)
        self.assertEqual(cursor.fetchall(), [('a string', )])
        cursor.execute("""
                       SELECT col_string, '%' FROM one_row_complex
                       WHERE col_string LIKE '%str%'
                       """)
        self.assertEqual(cursor.fetchall(), [('a string', '%')])
        cursor.execute("""
                       SELECT col_string, '%%' FROM one_row_complex
                       WHERE col_string LIKE '%%str%%'
                       """)
        self.assertEqual(cursor.fetchall(), [('a string', '%%')])

    @with_cursor
    def test_contain_special_character_query_with_parameter(self, cursor):
        self.assertRaises(TypeError, lambda: cursor.execute(
            """
            SELECT col_string, %(param)s FROM one_row_complex
            WHERE col_string LIKE '%str%'
            """, {'param': 'a string'}))
        cursor.execute(
            """
            SELECT col_string, %(param)s FROM one_row_complex
            WHERE col_string LIKE '%%str%%'
            """, {'param': 'a string'})
        self.assertEqual(cursor.fetchall(), [('a string', 'a string')])
        self.assertRaises(ValueError, lambda: cursor.execute(
            """
            SELECT col_string, '%' FROM one_row_complex
            WHERE col_string LIKE %(param)s
            """, {'param': '%str%'}))
        cursor.execute(
            """
            SELECT col_string, '%%' FROM one_row_complex
            WHERE col_string LIKE %(param)s
            """, {'param': '%str%'})
        self.assertEqual(cursor.fetchall(), [('a string', '%')])

    def test_escape(self):
        bad_str = """`~!@#$%^&*()_+-={}[]|\\;:'",./<>?\n\r\t """
        self.run_escape_case(bad_str)

    @with_cursor
    def run_escape_case(self, cursor, bad_str):
        cursor.execute('SELECT %(a)d, %(b)s FROM one_row', {'a': 1, 'b': bad_str})
        self.assertEqual(cursor.fetchall(), [(1, bad_str,)])

    @with_cursor
    def test_none_empty_query(self, cursor):
        self.assertRaises(ProgrammingError, lambda: cursor.execute(None))
        self.assertRaises(ProgrammingError, lambda: cursor.execute(''))

    @with_cursor
    def test_invalid_params(self, cursor):
        self.assertRaises(TypeError, lambda: cursor.execute(
            'SELECT * FROM one_row', {'foo': {'bar': 1}}))

    def test_open_close(self):
        with contextlib.closing(self.connect()):
            pass
        with contextlib.closing(self.connect()) as conn:
            with conn.cursor():
                pass

    @with_cursor
    def test_unicode(self, cursor):
        unicode_str = '王兢'
        cursor.execute('SELECT %(param)s FROM one_row', {'param': unicode_str})
        self.assertEqual(cursor.fetchall(), [(unicode_str,)])

    @with_cursor
    def test_null(self, cursor):
        cursor.execute('SELECT null FROM many_rows')
        self.assertEqual(cursor.fetchall(), [(None,)] * 10000)
        cursor.execute('SELECT IF(a % 11 = 0, null, a) FROM many_rows')
        self.assertEqual(cursor.fetchall(),
                         [(None if a % 11 == 0 else a,) for a in xrange(10000)])

    @with_cursor
    def test_description(self, cursor):
        cursor.execute('SELECT 1 AS foobar FROM one_row')
        expected = [('foobar', 'INTEGER', 11, None, 10, 0, 2)]
        self.assertEqual(cursor.description, expected)
        # description cache
        self.assertEqual(cursor.description, expected)

    @with_cursor
    def test_query_id(self, cursor):
        self.assertIsNone(cursor.query_id)
        cursor.execute('SELECT * from one_row')
        # query_id is UUID v4
        expected_pattern = \
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
        self.assertTrue(re.match(expected_pattern, cursor.query_id))

    @with_cursor
    def test_output_location(self, cursor):
        self.assertIsNone(cursor.output_location)
        cursor.execute('SELECT * from one_row')
        self.assertEqual(cursor.output_location,
                         '{0}{1}.csv'.format(ENV.s3_staging_dir, cursor.query_id))

    @with_cursor
    def test_complex(self, cursor):
        cursor.execute("""
        SELECT
          col_boolean
          ,col_tinyint
          ,col_smallint
          ,col_int
          ,col_bigint
          ,col_float
          ,col_double
          ,col_string
          ,col_timestamp
          ,col_date
          ,col_binary
          ,col_array
          ,col_map
          ,col_struct
          ,col_decimal
        FROM one_row_complex
        """)
        self.assertEqual(cursor.description, [
            ('col_boolean', 'BOOLEAN', 5, None, 0, 0, 2),
            ('col_tinyint', 'TINYINT', 4, None, 3, 0, 2),
            ('col_smallint', 'SMALLINT', 6, None, 5, 0, 2),
            ('col_int', 'INTEGER', 11, None, 10, 0, 2),
            ('col_bigint', 'BIGINT', 20, None, 19, 0, 2),
            ('col_float', 'FLOAT', 0, None, 17, 0, 2),
            ('col_double', 'DOUBLE', 24, None, 17, 0, 2),
            ('col_string', 'LONGNVARCHAR', 1073741824, None, 1073741824, 0, 2),
            ('col_timestamp', 'TIMESTAMP', 23, None, 3, 0, 2),
            ('col_date', 'DATE', 10, None, 0, 0, 2),
            ('col_binary', 'LONGVARBINARY', 1073741824, None, 1073741824, 0, 2),
            ('col_array', 'ARRAY', 0, None, 0, 0, 2),
            ('col_map', 'JAVA_OBJECT', 0, None, 0, 0, 2),
            ('col_struct', 'JAVA_OBJECT', 0, None, 0, 0, 2),
            ('col_decimal', 'DECIMAL', 0, None, 10, 1, 2),
        ])
        rows = cursor.fetchall()
        expected = [(
            True,
            127,
            32767,
            2147483647,
            9223372036854775807,
            0.5,
            0.25,
            'a string',
            datetime(2017, 1, 1, 0, 0, 0),
            date(2017, 1, 2),
            b'123',
            '[1, 2]',
            '{1=2, 3=4}',
            '{a=1, b=2}',
            Decimal('0.1'),
        )]
        self.assertEqual(rows, expected)
        # catch unicode/str
        self.assertEqual(list(map(type, rows[0])), list(map(type, expected[0])))
        # compare dbapi type object
        self.assertEqual([d[1] for d in cursor.description], [
            BOOLEAN,
            NUMBER,
            NUMBER,
            NUMBER,
            NUMBER,
            NUMBER,
            NUMBER,
            STRING,
            DATETIME,
            DATE,
            BINARY,
            STRING,
            STRING,
            STRING,
            NUMBER,
        ])

    @with_cursor
    def test_cancel(self, cursor):
        def cancel(c):
            time.sleep(randint(1, 5))
            c.cancel()

        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(cancel, cursor)

            self.assertRaises(DatabaseError, lambda: cursor.execute("""
            SELECT a.a * rand(), b.a * rand()
            FROM many_rows a
            CROSS JOIN many_rows b
            """))

    def test_multiple_connection(self):
        def execute_other_thread():
            with contextlib.closing(connect(schema_name=SCHEMA)) as conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT * FROM one_row')
                    return cursor.fetchall()

        with ThreadPoolExecutor(max_workers=2) as executor:
            fs = [executor.submit(execute_other_thread) for _ in range(2)]
            for f in futures.as_completed(fs):
                self.assertEqual(f.result(), [(1,)])

    def test_connection_is_closed(self):
        conn = self.connect()
        self.assertEqual(conn.is_closed, False)
        conn.close()
        self.assertEqual(conn.is_closed, True)
        self.assertRaises(ProgrammingError, lambda: conn.cursor())

    def test_cursor_is_closed(self):
        with contextlib.closing(self.connect()) as conn:
            cursor = conn.cursor()
            self.assertEqual(cursor.is_closed, False)
            cursor.close()
            self.assertEqual(cursor.is_closed, True)
            self.assertRaises(ProgrammingError, lambda: cursor.execute(
                'SELECT * FROM one_row'))
            self.assertRaises(ProgrammingError, lambda: cursor.fetchone())
            self.assertRaises(ProgrammingError, lambda: cursor.fetchmany())
            self.assertRaises(ProgrammingError, lambda: cursor.fetchall())
            self.assertRaises(ProgrammingError, lambda: cursor.cancel())

    def test_no_ops(self):
        conn = self.connect()
        cursor = conn.cursor()
        self.assertEqual(cursor.rowcount, -1)
        cursor.setinputsizes([])
        cursor.setoutputsize(1, 'blah')
        self.assertRaises(NotSupportedError, lambda: cursor.executemany(
            'SELECT * FROM one_row', []))
        conn.commit()
        self.assertRaises(NotSupportedError, lambda: conn.rollback())
        cursor.close()
        conn.close()

    @with_cursor
    def test_desc_query(self, cursor):
        cursor.execute('DESC one_row')
        self.assertEqual(cursor.description, [
            ('col_name', 'LONGNVARCHAR', 1073741824, None, 1073741824, 0, 2),
            ('data_type', 'LONGNVARCHAR', 1073741824, None, 1073741824, 0, 2),
            ('comment', 'LONGNVARCHAR', 1073741824, None, 1073741824, 0, 2),
        ])
        self.assertEqual(cursor.fetchall(), [
            ('number_of_rows      \tint                 \t                    ',)
        ])
