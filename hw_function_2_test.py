import hw_function_2


def test_get_string_and_distance_3c_5mc_10kg():
    expected_result = f"Транспортний засіб вагою {10} кг рухався {3} секунд зі швидкістю {5}м/сек, і подолав відстань {15} метрів"
    result = hw_function_2.get_string_and_distance(time_seconds=3, speed=5, weight_kg=10)
    assert expected_result == result


def test_get_string_and_distance_15c_10mc_500kg():
    expected_result = f"Транспортний засіб вагою {500} кг рухався {15} секунд зі швидкістю {15}м/сек, і подолав відстань {225} метрів"
    result = hw_function_2.get_string_and_distance(time_seconds=15, speed=15, weight_kg=500)
    assert expected_result == result


def test_get_string_and_distance_150c_100mc_5000kg():
    expected_result = f"Транспортний засіб вагою {5000} кг рухався {150} секунд зі швидкістю {100}м/сек, і подолав відстань {15000} метрів"
    result = hw_function_2.get_string_and_distance(time_seconds=150, speed=100, weight_kg=5000)
    assert expected_result == result
