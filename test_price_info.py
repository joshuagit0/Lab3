import price_info as exercise4


def test_total_cost_shopping():
    result = []

    input_price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90,
                        'papaya': 2.95,
                        'pomegranate': 4.95}

    input_quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1,
                           'pomegranate': 2}

    test_arr = 46.75

    result = exercise4.total_cost_shopping()

    assert (result == test_arr)


def test_cost_of_fruits():
    result = []

    input_fruit = "pear"
    input_quantity = 12
    test_arr = 10.8

    result = exercise4.cost_of_fruits(input_fruit, input_quantity)

    assert (result == test_arr)

