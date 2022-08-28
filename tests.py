import friendlyBytes
import pytest

def test_1():
    assert friendlyBytes.friendly_bytes(102) == '102 B'


def test_2():
    assert friendlyBytes.friendly_bytes(1234567890) == '1.23 GB'


def test_3():
    assert friendlyBytes.friendly_bytes(1111111111) == '1.11 GB'


def test_4():
    assert friendlyBytes.friendly_bytes(1111111111, decimals=3) == '1.111 GB'


def test_5():
    assert friendlyBytes.friendly_bytes(1111111111, binary=True) == '1.03 GiB'


def test_6():
    assert friendlyBytes.friendly_bytes(1111111111, decimals=3, binary=True) == '1.035 GiB'


