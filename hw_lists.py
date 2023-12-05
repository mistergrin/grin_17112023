string = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"

list_cities = string.strip("45678.:$?").title().split()

for cities in list_cities:
    print(f"Я \U00002764 {cities}")
