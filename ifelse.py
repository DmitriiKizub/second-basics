age = int(input("Сколько лет: "))

if age < 18:
    print("Иди в школу")
else:
    print("Ты уже не в школе")
    print("Иди в институт")
    why = input("Почему ты не хочешь в школу? ")
    print(why)
print('end')