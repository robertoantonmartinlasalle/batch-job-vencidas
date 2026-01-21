from unittest.mock import MagicMock
import pytest

from core.sql.executor import execute_select


def test_execute_select_without_params():
    # Mock de cursor
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [("row1",), ("row2",)]

    # Mock de conexión
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    sql = "SELECT * FROM tabla"

    rows = execute_select(mock_connection, sql)

    # Comprobaciones
    mock_connection.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once_with(sql)
    mock_cursor.fetchall.assert_called_once()
    mock_cursor.close.assert_called_once()

    assert rows == [("row1",), ("row2",)]


def test_execute_select_with_params():
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [("row1",)]

    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    sql = "SELECT * FROM tabla WHERE id = ?"
    params = (1,)

    rows = execute_select(mock_connection, sql, params)

    mock_cursor.execute.assert_called_once_with(sql, params)
    mock_cursor.close.assert_called_once()
    assert rows == [("row1",)]
