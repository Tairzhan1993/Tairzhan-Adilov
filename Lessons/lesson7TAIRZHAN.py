'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Пример использования функции
number = int(input("Введите число для вычисления факториала: "))
result = factorial(number)
print(f"Факториал числа {number} равен {result}")'''

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# def main():
#     print("Выберите действие:")
#     print("1. Конвертация из Цельсия в Фаренгейт")
#     print("2. Конвертация из Фаренгейта в Цельсия")

#     choice = int(input("Введите номер действия (1 или 2): "))

#     if choice == 1:
#         celsius_temp = float(input("Введите температуру в градусах Цельсия: "))
#         fahrenheit_result = celsius_to_fahrenheit(celsius_temp)
#         print(f"{celsius_temp} градусов Цельсия равны {fahrenheit_result:.2f} градусам Фаренгейта")
#     elif choice == 2:
#         fahrenheit_temp = float(input("Введите температуру в градусах Фаренгейта: "))
#         celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
#         print(f"{fahrenheit_temp} градусов Фаренгейта равны {celsius_result:.2f} градусам Цельсия")
#     else:
#         print("Некорректный выбор. Введите 1 или 2.")

# if __name__ == "__main__":
#     main()


# Простой калькулятор для расчета ежемесячных выплат по кредиту

# Функция для расчета ежемесячного платежа
def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = years * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                      ((1 + monthly_interest_rate) ** total_payments - 1)
    return monthly_payment

# Основная часть программы
print("Добро пожаловать в калькулятор ежемесячных выплат по кредиту!")

# Получаем ввод от пользователя
principal = float(input("Введите сумму кредита: "))
annual_interest_rate = float(input("Введите годовую процентную ставку: "))
years = int(input("Введите срок кредита в годах: "))

# Рассчитываем и выводим ежемесячный платеж
monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
print(f"Ваш ежемесячный платеж составит примерно: {monthly_payment:.2f}")