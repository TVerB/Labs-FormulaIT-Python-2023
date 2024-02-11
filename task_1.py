import doctest
from typing import Union


class Car:
    """Базовый класс, представляющий автомобиль."""

    def __init__(self, brand: str, model: str, body: str, seats: int, price: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param body: Кузов автомобиля.
        :param seats: Количество мест в автомобиле.
        :param price: Цена автомобиля.

        Примеры:
        >>> car = Car("Porsche", "Macan", "SUV", 4, 129000) # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть типа str")
        self.model = model

        if not isinstance(body, str):
            raise TypeError("Кузов автомобиля должен быть типа str")
        self.body = body

        if not isinstance(seats, int):
            raise TypeError("Количество мест в автомобиле должно быть типа int")
        if seats <= 0:
            raise ValueError("Количество мест в автомобиле должно быть положительным числом")
        self.seats = seats

        if not isinstance(price, int):
            raise TypeError("Цена автомобиля должна быть типа int")
        if price <= 0:
            raise ValueError("Цена автомобиля должна быть положительным числом")
        self.price = price

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car для печати.

        :return: Строковое представление автомобиля для печати.

        Примеры:
        >>> car = Car("Porsche", "Macan", "SUV", 4, 129000)
        >>> print(car)
        Автомобиль Porsche Macan в кузове SUV, количество мест: 4. Стоимость: $129000
        """
        return f"Автомобиль {self.brand} {self.model} в кузове {self.body}, количество мест: {self.seats}. " \
               f"Стоимость: ${self.price}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Car для отладки.

        :return: Строковое представление автомобиля.

        Примеры:
        >>> car = Car("Porsche", "Macan", "SUV", 4, 129000)
        >>> car.__repr__()
        "Car(brand='Porsche', model='Macan', body='SUV', seats=4, price=129000)"
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, body={self.body!r}, " \
               f"seats={self.seats}, price={self.price})"

    def check_passenger_capacity(self, passengers: int) -> bool:
        """
        Проверяет, возможно ли перевезти заданное количество пассажиров за один раз.

        :param passengers: Желаемое количество пассажиров в автомобиле.
        :return: True или False

        Примеры:
        >>> car = Car("Porsche", "Macan", "SUV", 4, 129000)
        >>> car.check_passenger_capacity(4)
        False
        """
        if not isinstance(passengers, int):
            raise TypeError("Количество пассажиров должно быть типа int")
        if passengers < 0:
            raise ValueError("Количество пассажиров не может быть отрицательным числом")
        if (self.seats - 1) >= passengers:
            return True
        else:
            return False

    def fuel_cost(self, cost_per_unit: Union[int, float]) -> (int, float):
        """
        Вычисление стоимости топлива для заполнения бака.

        :param cost_per_unit: Стоимость топлива за единицу.
        :return: Стоимость топлива.

        Примеры:
        >>> car = Car("Porsche", "Macan", "SUV", 4, 129000)
        >>> car.fuel_cost(62.3)
        """
        if not isinstance(cost_per_unit, (int, float)):
            raise TypeError("Стоимость топлива за единицу должна быть типа int или float")
        if cost_per_unit <= 0:
            raise ValueError("Стоимость топлива за единицу должна быть положительным числом")
        ...


class ElectricCar(Car):
    """Класс, представляющий электрический автомобиль, наследующий от Car"""

    def __init__(self, brand: str, model: str, body: str, seats: int, price: int, battery_capacity: Union[int, float],
                 motor_power: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Электрический автомобиль"

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param body: Кузов автомобиля.
        :param seats: Количество мест в автомобиле.
        :param price: Цена автомобиля.
        :param battery_capacity: Емкость батареи автомобиля.
        :param motor_power: Мощность силовой установки автомобиля.

        Примеры:
        >>> electric_car = ElectricCar("Porsche", "Taycan", "Sport Saloon", 4, 129000, 93.4, 350) # инициализация экземпляра класса
        """
        super().__init__(brand, model, body, seats, price)

        if not isinstance(battery_capacity, (int, float)):
            raise TypeError("Емкость батареи должна быть типа int или float")
        if battery_capacity <= 0:
            raise ValueError("Емкость батареи должна быть положительным числом")
        self.battery_capacity = battery_capacity

        if not isinstance(motor_power, (int, float)):
            raise TypeError("Мощность силовой установки должна быть типа int или float")
        if motor_power <= 0:
            raise ValueError("Мощность силовой установки должна быть положительным числом")
        self.motor_power = motor_power

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта ElectricCar для отладки.

        :return: Строковое представление электрического автомобиля.

        Примеры:
        >>> electric_car = ElectricCar("Porsche", "Taycan", "Sport Saloon", 4, 129000, 93.4, 350)
        >>> electric_car.__repr__()
        "ElectricCar(brand='Porsche', model='Taycan', body='Sport Saloon', seats=4, price=129000, battery_capacity=93.4, motor_power=350)"
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, body={self.body!r}, " \
               f"seats={self.seats}, price={self.price}, battery_capacity={self.battery_capacity}, " \
               f"motor_power={self.motor_power})"

    def fuel_cost(self, charging_method: str, cost_per_unit=None) -> (int, float):
        """
        Вычисление стоимости полной зарядки электрического автомобиля.
        Перегрузить метод необходимо из-за вариативности способов зарядки электрического транспорта.

        :param charging_method: Способ зарядки электрического автомобиля.
        :param cost_per_unit: Стоимость энергии за единицу.
        :return: Стоимость зарядки.

        Примеры:
        >>> electric_car = ElectricCar("Porsche", "Taycan", "Sport Saloon", 4, 129000, 93.4, 350)
        >>> electric_car.fuel_cost('fast charge', 2.5)
        """
        if not isinstance(charging_method, str):
            raise TypeError("Способ зарядки должен быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
