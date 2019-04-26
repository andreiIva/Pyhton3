__author__ = 'Ivanov Andrei'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print('задание №1')

def my_round(number, ndigits):

    '''
    Функция, округляющая полученное произвольное десятичное число
         до указанного количества знаков
    '''
    number = round(number, ndigits)
    return number
    #number = number * (10 ** ndigits)
    #if float(number) - int(number) >= 0.5:
    #    number = number // 1 + 1
    #else:
    #    number = number // 1
    #return number / (10 ** ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print('задание №2')


def lucky_ticket(ticket_number):
    '''
    Функция, определяющая по 6-тизначному номеру билета, является ли билет счасливым!
    '''
    ticket_number = list(str(ticket_number))
    for s in ticket_number:
        if len(ticket_number) < 6:
            return "Должен быть указан 6-тизначный номер"
        else:
            sum_1 = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
            sum_2 = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
            #print(sum_1)
            if sum_1 == sum_2:
                return 'Ура у Вас счастливый билет!' + ' ' + '-' + ' ' + ''.join([str(i) for i in ticket_number])
            else:
                return "Повезет в любви .("

    #pass

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))

