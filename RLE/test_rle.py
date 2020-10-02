#Run length encoding
# 'kkkkkaaaa' => '5k4a'
from hypothesis import given,settings
from hypothesis.strategies import text
from rle import rle,decode
import pytest

def test_simple():
    assert rle('kkkaaa') == '3k3a'
    assert rle('') == ''


def test_decode_simple():
    assert decode('2k3a') == 'kkaaa'

def test_decode_simple():
    assert decode('') == ''

def test_decode_simple():
    assert decode('41') == '1111'

@pytest.mark.skip()
def test_decode_simple():
    assert decode('123') == '333333333333'

def test_enkod_dekod():
    x = 'assssassssassssaaaaaaasssassasfegrhjyuki'
    assert decode(rle(x)) == x

def test_enkod_dekod_empty():
    x = ''
    assert decode(rle(x)) == x

@given(text())
@settings(max_examples=1000)
def test_enkod_dekod_hypo(x):
    assert decode(rle(x)) == x

#@pytest.mark.skip("Fejler")
def test_enkod_dekod_tal_2cifre():
    x = '11111111111111'
    assert decode(rle(x)) == x

def test_enkod_dekod_tal():
    x = '1111'
    assert decode(rle(x)) == x
