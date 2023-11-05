import Lab2.bmi as bmi

def test_bmi_underweight():
    result = None
    input_height = 1.75
    input_weight = 55
    test = -1

    result = bmi.calculate_bmi(input_height, input_weight)

    assert (result == test)


def test_bmi_normal_weight():
    result = None
    input_height = 1.8
    input_weight = 75
    test = 0

    result = bmi.calculate_bmi(input_height, input_weight)

    assert (result == test)


def test_bmi_overweight():
    result = None
    input_height = 1.65
    input_weight = 80
    test = 1

    result = bmi.calculate_bmi(input_height, input_weight)

    assert (result == test)