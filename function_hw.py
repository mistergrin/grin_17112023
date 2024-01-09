def from_centimeters_to_inches():
    centimetres = float(input("type your value(centimeters)"))
    inches = centimetres / 2.54
    return inches


def get_list_of_paired_numbers():
    list_paired_numbers = []
    lists = input("enter list of numbers").split()
    for numbers in lists:
        if int(numbers) % 2 == 0:
            list_paired_numbers.append(int(numbers))
    return list_paired_numbers


def is_bank_issue_loan():
    sum_payments = float(input("enter your payments for 25 years"))
    monthly_income = float(input("enter your income per month"))
    monthly_payment = sum_payments / 300
    percent_income = monthly_income * 0.35
    if percent_income > monthly_payment:
        answer = "Yes, you can"
    else:
        answer = "No, tou can't"
    return answer
