from datetime import datetime

def get_days_from_today(date):
    """
    Розраховує кількість днів між поточною датою і заданою датою.

    :param date: Рядок у форматі 'РРРР-ММ-ДД'
    :return: Ціле число, що представляє різницю в днях.
             Позитивне число, якщо задана дата в минулому.
             Від'ємне число, якщо задана дата в майбутньому.
    :raises ValueError: Якщо формат дати невірний.
    """
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримання поточної дати
        today_date = datetime.today().date()
        # Обчислення різниці в днях
        difference = (today_date - input_date).days
        return difference
    except ValueError as e:
        # Виведення повідомлення, якщо формат дати невірний
        raise ValueError("Невірний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.") from e

# Приклади використання:
print(get_days_from_today("2021-10-09"))  # Очікуваний результат: -157, якщо сьогодні 5 травня 2021
print(get_days_from_today("2020-01-01"))  # Позитивне значення