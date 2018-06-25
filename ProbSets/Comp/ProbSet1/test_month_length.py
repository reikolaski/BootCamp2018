import month_length as ml

def test_month_length():
    assert ml.month_length("September") == 30
    assert ml.month_length("January") == 31
    assert ml.month_length("September", True) == 30
    assert ml.month_length("January", True) == 31
    assert ml.month_length("February") == 28
    assert ml.month_length("February", True) == 29
    assert ml.month_length("hello") == None