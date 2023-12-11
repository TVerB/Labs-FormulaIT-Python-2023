import doctest
from typing import Union


class SteelBeam:
    def __init__(self, beam_length: Union[int, float], tensile_strength: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Стальная балка"

        :param beam_length: Длина балки
        :param tensile_strength: Предел прочности

        Примеры:
        >>> beam = SteelBeam(1500, 350) # инициализация экземпляра класса
        """
        if not isinstance(beam_length, (int, float)):
            raise TypeError("Длина балки должна быть типа int или float")
        if beam_length <= 0:
            raise ValueError("Длина балки должна быть положительным числом")
        self.beam_length = beam_length

        if not isinstance(tensile_strength, (int, float)):
            raise TypeError("Предел прочности должен быть типа int или float")
        if tensile_strength <= 0:
            raise ValueError("Предел прочности должен быть положительным числом")
        self.tensile_strength = tensile_strength

    def changing_beam_length(self, length: Union[int, float]) -> None:
        """
        Изменение длины балки

        :param length: Добавочная длина балки
        :raise ValueError: Если уменьшаемая длина первышает изначальную длину балки, то возвращается ошибка

        Примеры:
        >>> beam = SteelBeam(1500, 350)
        >>> beam.changing_beam_length(300)
        >>> beam.changing_beam_length(-300)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Добавляемая длина должна быть типа int или float")
        ...

    def thermal_treatment(self, required_tensile_strength: Union[int, float]) -> bool:
        """
        Функция, которая проверяет необходимость применения термической обработки

        :param required_tensile_strength: Требуемый предел прочности

        :return: Нужна ли термическая обработка

        Примеры:
        >>> beam = SteelBeam(1500, 350)
        >>> beam.thermal_treatment(400)
        """
        if not isinstance(required_tensile_strength, (int, float)):
            raise TypeError("Предел прочности должен быть типа int или float")
        if required_tensile_strength <= 0:
            raise ValueError("Предел прочности должен быть положительным числом")
        ...


class RollingLawn:
    def __init__(self, roll_width: Union[int, float], roll_length: Union[int, float], cost: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Рулонный газон"

        :param roll_width: Ширина рулона
        :param roll_length: Длина рулона
        :param cost: Стоимость квадратного метра газона

        Примеры:
        >>> lawn = RollingLawn(1000, 600, 250) # инициализация экземпляра класса
        """
        if not isinstance(roll_width, (int, float)):
            raise TypeError("Ширина рулона должна быть типа int или float")
        if roll_width <= 0:
            raise ValueError("Ширина рулона должна быть положительным числом")
        self.roll_width = roll_width

        if not isinstance(roll_length, (int, float)):
            raise TypeError("Длина рулона должна быть типа int или float")
        if roll_length <= 0:
            raise ValueError("Длина рулона должна быть положительным числом")
        self.roll_length = roll_length

        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость должна быть типа int или float")
        if cost <= 0:
            raise ValueError("Стоимость должна быть положительным числом")
        self.cost = cost

    def lawn_area(self, rolls_quantity: int) -> (int, float):
        """
        Вычисление площади газона

        :param rolls_quantity: Количество рулонов газона

        :return: Площадь газона

        Примеры:
        >>> lawn = RollingLawn(1000, 600, 250)
        >>> lawn.lawn_area(30)
        """
        if not isinstance(rolls_quantity, int):
            raise TypeError("Количество рулонов должно быть типа int")
        if rolls_quantity < 0:
            raise ValueError("Количество рулонов не может быть отрицательным числом")
        ...

    def lawn_cost(self, area: Union[int, float]) -> (int, float):
        """
        Вычисление стоимости газона для покрытия заданной территории

        :param area: Площадь территории

        :return: Стоимость газона

        Примеры:
        >>> lawn = RollingLawn(1000, 600, 250)
        >>> lawn.lawn_cost(35)
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь территории должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь территории должна быть положительным числом")
        ...


class FuelTank:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float], cost: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Топливный бак"

        :param capacity_volume: Объём бака
        :param occupied_volume: Объём топлива в баке
        :param cost: Стоимость топлива за литр

        Примеры:
        >>> tank = FuelTank(85, 30, 62) # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объём бака должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объём бака должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество топлива должно быть типа int или float")
        if occupied_volume <= 0:
            raise ValueError("Количество топлива должно быть положительным числом")
        self.occupied_volume = occupied_volume

        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость должна быть типа int или float")
        if cost <= 0:
            raise ValueError("Стоимость должна быть положительным числом")
        self.cost = cost

    def possible_mileage(self, fuel_consumption: Union[int, float]) -> (int, float):
        """
        Вычисление расстояния, которое сможет преодолеть транспортное стредство

        :param fuel_consumption: Расход топлива на 100 километров

        :return: Максимальное расстояние

        Примеры:
        >>> tank = FuelTank(85, 30, 62)
        >>> tank.possible_mileage(8)
        """
        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть типа int или float")
        if fuel_consumption < 0:
            raise ValueError("Расход топлива не может быть отрицательным числом")
        ...

    def fuel_cost(self) -> (int, float):
        """
        Вычисление стоимости топлива для заполнения бака

        :return: Стоимость топлива

        Примеры:
        >>> tank = FuelTank(85, 30, 62)
        >>> tank.fuel_cost()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
