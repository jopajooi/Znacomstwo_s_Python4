# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random, numpy as np
a = int(input("Введите количество элементов первого набора:  "))
lower_face= 0
upper_face=1000

first_list =np.random.randint(lower_face,upper_face, a)

a1 = int(input("Введите количество элементов второго набора:  "))

second_list =np.random.randint(lower_face,upper_face, a1)
print()
print(first_list)
print()
print(second_list)
print()
third_list = np.intersect1d([first_list],[second_list])
print(third_list)
