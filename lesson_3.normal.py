__author__ = 'Ivanov Andrei'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print('задание №1')
n = int(input('Введите начало ряда: '))
m = int(input('Введите конец ряда: '))
def fibonacci(n, m):
    '''
    Функция, возвращающая ряд Фибоначчи с n-элемента до m-элемента.
    '''
    a, b = 1, 1
    f_list = [1, ]

    for i in range(m):
        a, b = b, a + b
        f_list.append(a)

    return f_list[n - 1:m]


print('Получим следующий ряд Фибоначчи: ', fibonacci(n, m))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print('задание №2')




def sort_to_max(origin_list):
    '''
        Функция, сортирующая принимаемый список по возрастанию(пузырьковый метод).
    '''
    for bypass in range(1,len(origin_list)):
        for k in range(0, len(origin_list)- bypass):
            if origin_list[k] > origin_list[k + 1]:
                origin_list[k], origin_list[k + 1] = origin_list[k + 1], origin_list[k]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print('задание №3')


def filter_func(function, iterable):
    '''
        Реализация стандартной функции filter.
    '''
    return (item for item in iterable if function(item))


print(list(filter_func(lambda x: True if x % 2 == 0 else False, [0, 23, 586, 44, 22, 11, 156])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print('задание №4')
print("ВНИМАНИЕ КООРДИНАТЫ ТОЧЕК ВВОДЯТСЯ БЕЗ РАЗДЕЛИТЬЛЬНЫХ ЗНАКОВ!!!")
a = list(str(input('Введите координаты первой точки: ')))
b = list(str(input('Введите координаты второй точки: ')))
c = list(str(input('Введите координаты третьей точки: ')))
d = list(str(input('Введите координаты четвертой точки: ')))
def is_a_parallelogram(a,b,c,d):
    '''
           Это программа определяет являются ли точки вершинами паралеллограммма.
    '''

    if abs(int(a[1])) == abs(int(d[1])) and abs(int(b[1])) == abs(int(c[1])) \
            and abs(int(a[0]) - int(b[0])) == abs(int(c[0]) - int(d[0])):

        return True
    return False

print(is_a_parallelogram(a,b,c,d))
