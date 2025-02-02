
def convert_base(num, to_base=10, from_base=10):
    # Перевод в десятичную систему
    if isinstance(num, str):  # Если число - строка, то ...
        n = int(num, from_base)  # ... переводим его в нужную систему счисления
    else:  # Если же ввели число, то ...
        n = int(num)  # ... просто воспринять его как число
    # Перевод десятичной в 'to_base' систему
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Берём алфавит
    if n < to_base:  # Если число меньшеq системы счисления в которую переводить...
        return alphabet[n]  # ... вернуть значения номера в алфавите (остаток от деления)
    else:  # Иначе...
        return convert_base(n // to_base, to_base) + alphabet[
            n % to_base]  # ... рекурсивно обратиться к функии нахождения остатка


#ТИП?
a = '9' * 1000
while '999' in a or '888' in a:
    if '888' in a:
        a = a.replace('888', '9', 1)
    else:
        a = a.replace('999', '8', 1)
print(a)


# ТИП? 7761
a = 4 ** 2020 + 2 ** 2017 - 15
k = 0
while a > 0:
    if a % 2 == 1:
        k += 1
        a = a // 2

print(k)

# ТИП
with open("17.txt", "r") as f: #Открыли файл 17.txt для чтения
    text = f.read() #В переменную text запихнули строку целиком
a = text.split("\n") #Разбили строку энтерами (\n - знак перехода на новую строку)

k = 0 #Стандартно обнуляем количество
m = -20001 #Так как у нас сумма 2-ух чисел и минимальное равно -10000, то минимум по условию равен -20000, поэтому...

for i in range(len(a)): #Обходим все элементы массива
	if (int(a[i - 1]) % 3 == 0) or (int(a[i]) % 3 == 0): #Условное условие
		k += 1 #Счётчик
		if int(a[i - 1]) + int(a[i]) > m: #Нахождение минимума
			m = int(a[i - 1]) + int(a[i])

print(k, m) #Вывод




# t4 тип?
def f(x, y, p): #Рекурсивная функция
	if x + y >= 69 or p > 3: #Условия завершения игры
		return p == 3
	return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or\
		   f(x * 2, y, p + 1) or f(x, y * 3, p + 1) #Варианты действий

for s in range (1, 58 + 1): #Перебор S
	if f(10, s, 1): #Начали с 10 камней
		print(s)
		break
# t5 тип?
def f(x, y):
	if x > y: #Перегнали цель
		return 0
	if x == y:  #Догнали цель
		return 1
	if x < y: #Догоняем цель тремя методами
		return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)

print(f(3, 10) * f(10, 12)) #Прошло через 10, значит догнали 10 и от де догоняем 12
# t6
# t7
# t8
# t9
# t10


# ТИП?
print("ЖЖЖЖЖ11111")
print('y', 'x', 'z', 'F')  # Напечатаем заголовки таблицы
for y in range(2):  # Берём все переменные и меняем их в циклах '0' и '1'
    for x in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not x or y) == (not z or w)) or (x and w)  # Записываем функцию
                print(x, y, z, F)  # Выводим результат

#ТИП?
def f(x, y, p): #Рекурсивная функция
	if x + y >= 69 or p > 3: #Условия завершения игры
		return p == 3
	return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or\
		   f(x * 2, y, p + 1) or f(x, y * 3, p + 1) #Варианты действий

for s in range (1, 58 + 1): #Перебор S
	if f(10, s, 1): #Начали с 10 камней
		print(s)
		break

#ТИП
def f(x, y, p): #Рекурсивная функция
	if x + y >= 69 or p > 4: #Условия завершения игры
		return p == 4
	if p % 2 != 0:
		return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or\
			   f(x * 2, y, p + 1) or f(x, y * 3, p + 1) #Варианты действий
	else:
		return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and\
			   f(x * 2, y, p + 1) and f(x, y * 3, p + 1) #Варианты действий


for s in range (1, 58 + 1): #Перебор S
	if f(10, s, 1): #Начали с 10 камней
		print(s)