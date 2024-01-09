from decimal import Decimal

FROM_INCHES_TO_CENTIMETERS = 2.54


def convert_centimeters_to_inches(centimetres: int | float) -> Decimal:
    inches = centimetres / FROM_INCHES_TO_CENTIMETERS
    result = Decimal(str(inches)).quantize(Decimal('0.01'))
    return result


def get_list_of_paired_numbers(list_numbers: list[int]) -> list[int]:
    for numbers in list_numbers:
        if numbers % 2 != 0:
            list_numbers.remove(numbers)
    return list_numbers


YEARS = 25


def is_bank_issue_loan(sum_payments: float | int, monthly_income: int | float) -> bool:
    monthly_payment = sum_payments / (YEARS * 12)
    percent_income = monthly_income * 0.35
    if percent_income > monthly_payment:
        answer = True
    else:
        answer = False
    return answer
