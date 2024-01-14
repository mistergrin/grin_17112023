def get_string_and_distance(*, time_seconds, speed, weight_kg) -> str:
    if time_seconds == 0 or speed == 0 or weight_kg == 0:
        raise ValueError("Час, швидкість та вага повинні бути встановлені і не можуть дорівнювати нулю.")
    distance = time_seconds * speed
    result = f"Транспортний засіб вагою {weight_kg} кг рухався {time_seconds} секунд зі швидкістю {speed}м/сек, і подолав відстань {distance} метрів"
    return result


