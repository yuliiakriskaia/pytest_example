from unittest import mock
import unittest
import pytest

from hello_world_app.hello_world_app import hello_world_write, hello_world_read


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        """ Setup initial data if we need to reuse it in several test cases """
        self.sentence = "test sentence"

    @mock.patch("hello_world_app.postgres_operations.sqlalchemy")
    def test_write(self, db_mock):
        engine = db_mock.create_engine.return_value
        connection_mock = mock.Mock(**{"execute.return_value": []})
        # MagicMock has magic methods mocked
        # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock
        engine.connect.return_value = mock.MagicMock(
            **{"__enter__.return_value": connection_mock}
        )

        hello_world_write(self.sentence)
        # One of the 2 next asserts can be used to check if mocked func has been called once
        self.assertEqual(engine.connect.call_count, 1)
        connection_mock.execute.assert_called_once()

    @mock.patch("hello_world_app.postgres_operations.sqlalchemy")
    def test_read(self, db_mock):
        test_data = [{"a": 1}, {"b": 2}]
        engine = db_mock.create_engine.return_value
        connection_mock = mock.Mock(**{"execute.return_value": test_data})
        engine.connect.return_value = mock.MagicMock(
            **{"__enter__.return_value": connection_mock}
        )

        res = hello_world_read()
        # One of the 2 next asserts can be used to check if mocked func has been called once
        self.assertEqual(engine.connect.call_count, 1)
        connection_mock.execute.assert_called_once()
        self.assertEqual(res, len(test_data))
