"""
Задача 1: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

# n = int(input('число цифр первого массива '))
# m = int(input('число цифр второго массива '))
# n_sp = []
# m_sp = []
#
# print("Первый массив")
# for i in range(n):
#     n_sp.append(int(input("Число ")))
# print("Второй массив")
#
# for i in range(m):
#     m_sp.append(int(input("Число ")))
#
# n_sp = set(n_sp)
# m_sp = set(m_sp)
# spmn = []
#
# for el in n_sp:
#     if el in m_sp:
#         spmn.append(el)
#
# spmn.sort()
# print(spmn)


"""
Задача 2: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

"""

n = int(input())
a = []
for i in range(n):
    a.append(i+1)

print(a)
s = a[n-1] + a[n-2] + a[n-3]
print(s)