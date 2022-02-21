name = "Nikita"
print(name)

name = "Никита"
age = 18
print(name, age, "лет")

name = 5*"Никита"
print(name)

name1 = input("Ввидете ваше имя")
age1 = input("Введите ваш возраст")
print("Здравствуйте,", name1,", За пенсией!")

age = input("Введите ваш возраст")
age = int(age)
if age>45:
    print("С вас песок сыпится,дядя")
else:
    print("шуруй отсюда, малец")

name2 = 'nikita'
print(name2[1:-1])

name3 = 'nikita'
for i in reversed(name3):
    print(i)

name4 = input("Введите ваше имя")
print(name4[-3:])

name5 = input("Введите ваше имя")
print(name5[:5])

name6 = input("Введите ваше имя")
print(len(name6))

age2 = int(input("Ведите вваш возраст"))
summa = 0
proizv = 1
while age2>0:
    digit = age2%10
    summa = summa + digit
    proizv = proizv * digit
    age2 = age2//10
print('Сумма', summa)
print('Произведение', proizv)

name7 = input("Ведите имя")
print(str.upper(name7))
print(str.lower(name7))

name8 = input("Введите ваше имяяяя")
print(str.capitalize(name8))

name9 = input("Ввести имя")
name9 = name9[:1].lower() + name9[1:]
print(name9)

name10 = input("Введите ваше имя (без пробелов)")
if (" " in name10):
    print('False')
age3 = int(input("Ввведите ваш возраст"))
if (0<age3<150)==False:
    print('False')

Zadacha = int(input("Решите задачу 2*2+2"))
if Zadacha==6:
    print("True")
else:
    print("False")