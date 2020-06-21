"""Main file for execute app"""
from test_data import data1, data3, data2, data4
from attestation import calculate, OutOfResourceError

"""Позитивные сценарии"""
if __name__ == '__main__':

    while True:
        number_of_scenario = int(input('Выберите номер сценария (1-2 позитивные ,3-4 негативные : '))
        if number_of_scenario == 1:
            print('Начинаем прогон тестовый данных #1')
            print(calculate(data1))
        elif number_of_scenario == 2:
            print('Начинаем прогон тестовый данных #2')
            print(calculate(data2))
        elif number_of_scenario == 3:
            print('Начинаем прогон тестовый данных #3')
            print(calculate(data3))
        elif number_of_scenario == 4:
            print('Начинаем прогон тестовый данных #4')
            print(calculate(data4))
        else:
            print('Вы выбрали неверный вариант.Попробуйте еще раз')



