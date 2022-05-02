ask1 = input('Введите путь до файла: ')
ask2 = input('Какие столбцы вам нужны? (укажите их индекс, счет начинается с 0) ')
ask3 = input('Нужно ли вам объединять столбцы? ')
if ask3 == 'да':
  ask31 = int(input('По какому столбцу? '))
ask4 = input('Какой тип графика вам нужен? ')

ask2_1 = []
ask3_1 = []
ask31_1 = []
ask4_1 = []

ask2_1.append(ask2)
ask3_1.append(ask3)
ask31_1.append(ask31)
ask4_1.append(ask4)

print(ask2_1, ask3_1, ask31_1, ask4_1)