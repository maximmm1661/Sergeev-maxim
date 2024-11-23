money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долго
i=1
while money_capital > spend:
    if i == 1:
        money_capital=money_capital+salary-spend
        i = i+1
    else:
        spend = spend + spend * increase
        money_capital = money_capital + salary - spend
        i = i+1
print("Количество месяцев, которое можно протянуть без долгов:", i)