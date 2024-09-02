from example import functions as fun

def test_frequency_zero():
    lamda = 0

    assert fun.frequency_calculation(lamda) == 0

def test_frequency_int():
    lamda = 2

    assert fun.frequency_calculation(lamda) == 0.22507907903927654

