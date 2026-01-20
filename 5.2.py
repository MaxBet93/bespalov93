while True:
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: введіть коректне число!")
        continue
    result = None

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Помилка: ділення на нуль!")
        else:
            result = num1 / num2
    else:
        print("Невідома операція.")
    if result is not None:
        print(f"Результат: {result}")
    answer = input("Бажаєте виконати ще одне обчислення? (y/yes): ")
    if answer.lower() not in ['y', 'yes']:
        print("Роботу завершено.")
        break