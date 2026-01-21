import pytest
from core.sql.validator import validate_sql


def test_valid_select_simple():
    sql = "SELECT * FROM tabla"
    assert validate_sql(sql) == sql


def test_valid_select_with_where():
    sql = "SELECT * FROM tabla WHERE id = 1"
    assert validate_sql(sql) == sql


def test_empty_sql_raises_error():
    with pytest.raises(ValueError):
        validate_sql("   ")


def test_non_select_raises_error():
    with pytest.raises(ValueError):
        validate_sql("DELETE FROM tabla")


def test_multiple_statements_raises_error():
    with pytest.raises(ValueError):
        validate_sql("SELECT * FROM tabla; DELETE FROM tabla")


def test_comment_raises_error():
    with pytest.raises(ValueError):
        validate_sql("SELECT * FROM tabla -- comentario")
