import sys

sys.path.insert(0, '../src')
import day_03 as d3

def test_mul():
    a = 2
    b = 5
    assert d3.mul(a, b) == 10


def test_scan_memory():
    mem = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert d3.scan_memory(mem) == 161


def test_scan_memory_conditional():
    mem = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert d3.scan_memory_conditional(mem) == 48