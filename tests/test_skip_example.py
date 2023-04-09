import pytest
import time


@pytest.fixture()
def browser():
    """chrome or firefox"""
    time.sleep(1)


@pytest.mark.fast
def test_first(browser):
    time.sleep(1)

@pytest.mark.slow
@pytest.mark.skip(reason="ТАСК-123: Ждем пока реализуют фичу")
def test_second(browser):
    time.sleep(5)

def test_third():
    user_status = 'disabled'
    try:
        assert user_status == 'active'
    except AssertionError:
        pytest.xfail(reason="ТАСК-123: Ждем пока реализуют фичу")
    assert False