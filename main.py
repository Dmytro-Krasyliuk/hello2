# # Наследование
# class A(object): #
#     def method(self):
#         print("Hello World")
#
# class B(A):  # наследует все аттрибуты и методы класса A
#     def method2(self):
#         print('Method 2')
# A().method()
# B().method()
# B().method2()

# Наследование
# class A(object): #
#     def method(self, string: str):
#         print(string)
#     def method(self, string: int):
#         print(f'{string} hello')
# A().method(12)
# A().method('12')

# Наследование видов
class Animal:
    def move(self):
        pass


class Snake(Animal):
    def move(self):
        color = 'ffffff'
        print('Извивается')


class Human(Animal):
    def move(self):
        print('Передвигает ногами')


h = Human()
s = Snake()
h.move()
s.move()

# 1. Запиши в словарь (JSON), следующие данные:

# Разыскивается человек: Мужчина 32 лет, уроженец Казахстана.
# Рост: около 180 см, Худощавое телосложение.
# Особые приметы: Татуировка на лице: Maks.
