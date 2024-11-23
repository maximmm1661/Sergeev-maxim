salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_needed = 0
current_spend = spend

for month in range(months):
    deficit = current_spend - salary
    if deficit > 0:
        total_needed += deficit
    current_spend *= (1 + increase)
pillow = total_needed

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(total_needed))
