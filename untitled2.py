i = 1
a = 0
b = 0
c = 1
d = 1
e = i
max = -500
min = 500
nechet = 0
chet = 0
while i > 0:
    i = int(input('Enter your the number: '))
    if i == 0:
        break
    a = a + 1
    b = b + i
    c = c * a
    d = b / a
    if (i > max):
        max = i
    if (i < min):
        min = i
    if (i % 2 == 1):
        nechet += 1
    if (i % 2 == 0):
        chet += 1
print(a)
print("1. Найти сумму введенных чисел.")
print("2. Найти произведение введенных чисел.")
print("3. Найти среднее значение введенных чисел.")
print("4. Найти максимальное из введенных чисел.")
print("5. Найти минимальное из введенных чисел.")
print("6. Найти четные и нечетные числа")

j = int(input("Выберите номер операции над рядом: "))
if j == 1:
    print("Результат: ", b)
elif j == 2:
    print("Результат: ", c)
elif j == 3:
    print("Результат: ", min)
elif j == 4:
    print("Результат: ", max)
elif j == 5:
    print("Результат: ", )
elif j ==6 :
    print("nechetnyh = ", nechet, "\nchetnyh = ", chet)
