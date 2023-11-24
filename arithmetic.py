print('~' * 40)

name_user = input()
age_user = int(input())
average_salary = float(input())

quantity_ages = 65 - age_user
all_money = (quantity_ages * average_salary * 12) / 37.3
cars_quantity = all_money // 31500

print(f"я, {name_user.strip().title()}, зможу заробити лише {all_money} доларів, що вистачить лише на {cars_quantity} тойот, мене це не влаштовує, тому я буду змінювати своє життя і буду завзято вивчати програмування! ")
