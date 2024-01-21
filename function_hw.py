from decimal import Decimal

FROM_INCHES_TO_CENTIMETERS = 2.54
YEARS = 25
PERCENTS = 0.35
MONTH_IN_YEAR = 12


def convert_centimeters_to_inches(centimetres: int | float) -> Decimal:
    inches = centimetres / FROM_INCHES_TO_CENTIMETERS
    result = Decimal(str(inches)).quantize(Decimal('0.01'))
    return result


def get_list_of_paired_numbers(list_numbers: list[int]) -> list[int]:
    for numbers in list_numbers:
        if numbers % 2 != 0:
            list_numbers.pop(numbers)
    return list_numbers


def is_bank_issue_loan(sum_payments: float | int, monthly_income: float | int) -> bool:
    monthly_payment = sum_payments / (YEARS * MONTH_IN_YEAR)
    percent_income = monthly_income * PERCENTS
    if percent_income > monthly_payment:
        answer = True
    else:
        answer = False
    return answer
