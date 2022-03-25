age = int(input("Сколько лет: "))

if age < 18:
    print("Иди в школу")
elif age >= 18 and age <= 30:
    print("Иди в институт")
elif age >30 and age <=40:
    print('Не рано начинать учиться')
else:
    print("Ты уже не в школе")
    why = input("Почему ты не хочешь в школу? ")
    print(why)
print('end')
