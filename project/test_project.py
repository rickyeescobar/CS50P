import project
import pytest

def test_get_stock_data_contents():
    assert 'symbol','price' in project.get_stock_data('tsla')


def test_get_stock_data():
    with pytest.raises(OSError):
        project.get_stock_data('')


def test_exit():
    with pytest.raises(SystemExit):
        project.get_stock_data('exit')

