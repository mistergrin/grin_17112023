from decimal import Decimal

FROM_INCHES_TO_CENTIMETERS = 2.54
centimetres = 12.7


def convert_centimeters_to_inches() -> Decimal:
    inches = centimetres / FROM_INCHES_TO_CENTIMETERS
    result = Decimal(str(inches)).quantize(Decimal('0.01'))
    return result


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_list_of_paired_numbers():
    for numbers in list:
        if numbers % 2 != 0:
            list.remove(numbers)
    return list


YEARS = 25
sum_payments = 120000000
monthly_income = 55000


def is_bank_issue_loan(sum_payments: float | int, monthly_income: int | float) -> bool:
    monthly_payment = sum_payments / (YEARS * 12)
    percent_income = monthly_income * 0.35
    if percent_income > monthly_payment:
        answer = True
    else:
        answer = False
    return answer
