def super_calc():
    q = float(input('Введите количество отработанных часов в месяц : '))
    w = float(input('Введите суммы оплаты труда за 1 час : '))
    e = float(input('Укажите размер премии в месяц- '))
    pay = q * w
    return pay + e


print(f'Размер заработной платы составил за месяц: {super_calc()} ')
