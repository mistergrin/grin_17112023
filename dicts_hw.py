students = {
    "Іван Петров": {
        "Пошта": "Ivan@gmail.com",
        "Вік": 14,
        "Номер телефону": "+380987771221",
        "Середній бал": 95.8,
    },
    "Женя Курич": {
        "Пошта": "Geka@gmail.com",
        "Вік": 16,
        "Номер телефону": None,
        "Середній бал": 64.5,
    },
    "Маша Кера": {
        "Пошта": "Masha@gmail.com",
        "Вік": 18,
        "Номер телефону": "+380986671221",
        "Середній бал": 80,
    },
}

students["Ivan Alekseev"] = {
    "Пошта": "IvanAleks@gmail.com",
    "Вік": 23,
    "Номер телефону": "+380986654821",
    "Середній бал": 72.5,
}

students["Іван Петров"].update({'bank_account_number': None})
get_account = students.get('bank_account_number', 0.0)
quantity_students = len(students)

grades = 0
for student in students.values():
    grades += student["Середній бал"]

average_grade = grades / quantity_students

print(f"Середній бал студентів = {average_grade}, \nДані Івана Петрова про акаунт - {get_account}")
