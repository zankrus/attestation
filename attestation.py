"""Attestation 21 06 2020."""
from typing import Iterable, Dict, Optional, List, Any
from itertools import groupby


class OutOfResourceError(Exception):
    def __init__(self: Any, message: str = 'Не хватает ресурсов') -> None:
        super().__init__(message)


def grouper(data: dict) -> str:
    """Функция для сортировки по роботу"""
    return data['robot']


def calculate(data: list) -> Any:
    """основая функция.Вовзращает инструкции роботам или ошибку."""
    robots_number = dict()
    sorted_data = sorted(data, key=grouper)
    water = 0
    sugar = 0
    not_main_res = list()
    overall_instruction = list()
    for key, group in groupby(sorted_data, key=grouper):
        if not robots_number.get(key):
            robots_number[key] = dict()
            robots_number[key]["Ресурсы"] = list()
        for resource in group:
            if resource.get("resource") == "вода":
                robots_number[key]["вода"] = resource

            elif resource.get("resource") == "сахар":
                robots_number[key]["сахар"] = resource
            else:
                robots_number[key]["Ресурсы"].append(
                    resource)
    for key, item in robots_number.items():
        try:
            water = item.get("вода")
            print('Вода у робота {} '.format(key) + str(water))
            sugar = item.get('сахар')
            print('Сахар у робота {} '.format(key) + str(sugar))
            not_main_res = item.get('Ресурсы')
            print('Неосновные ресурсы у робота {} '.format(key) + str(not_main_res))
            not_main_res = sorted(not_main_res, key=lambda item: item.get('portion'))
            max_portions_water = int(water.get("limit") // water.get("portion"))
            print()
            print('Макс порций воды ' + str(max_portions_water))
            max_portions_sugar = int(sugar.get("limit") // sugar.get("portion"))
            print('Макс порций сахара ' + str(max_portions_sugar))
            max_soda_available = min(max_portions_sugar, max_portions_water)
            print('Максмимальное количество газировок : ' + str(max_soda_available))

            for not_main_res in not_main_res:

                portions_available = int(not_main_res.get("limit") // not_main_res.get("portion"))
                print('Добавка - {0}'.format(not_main_res.get('resource')))
                print('Добавок хватает на : ' + str(portions_available))

                # Пополняем инструкции для производства новыми инструкциями изготовления кексиков
                for i in range(max_soda_available):
                    if i >= portions_available:
                        overall_instruction.append(
                            {
                                sugar.get("resource"): sugar.get("portion"),
                                water.get("resource"): water.get("portion"),
                                "robot": key
                            }
                        )
                    elif i < max_portions_water:
                        overall_instruction.append(
                            {
                                sugar.get("resource"): sugar.get("portion"),
                                water.get("resource"): water.get("portion"),
                                not_main_res.get("resource"): not_main_res.get("portion"),
                                "robot": key
                            }
                        )
        except AttributeError:
            print('********************')
            print('Не хватает поставки воды или сахара  для робота {}'.format(key))
            print('********************')
            pass

    if not overall_instruction:
        raise OutOfResourceError
    return overall_instruction
