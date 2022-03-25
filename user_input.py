# Пользовательский ввод

name = input("input your name: ")

print("Hello", name)

age = input("input your age: ")
print(type(age))
# Приведение типов
age = int(age)
print(type(age))
print("age", age)

after20years = age + 20
print("Будет через 20 лет:", after20years)