import doctest
from abc import ABC, abstractmethod


class LibraryBook(ABC):
    def __init__(self, title: str, pages: int, is_checked_out: bool):
        """
        Создание и подготовка к работе объекта "Книга библиотеки"

        :param title: Название книги
        :param pages: Количество страниц
        :param is_checked_out: Признак, выдана ли книга

        Примеры:
        >>> book = ConcreteLibraryBook("Python", 300, False)  # инициализация экземпляра
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not title.strip():
            raise ValueError("Название не может быть пустым")
        self.title = title

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

        if not isinstance(is_checked_out, bool):
            raise TypeError("Признак выдачи должен быть bool")
        self.is_checked_out = is_checked_out

    @abstractmethod
    def check_out(self, reader_id: int) -> None:
        """
        Выдача книги читателю.

        :param reader_id: Идентификатор читателя

        Примеры:
        >>> book = ConcreteLibraryBook("Python", 300, False)
        >>> book.check_out(1)
        """
        if not isinstance(reader_id, int):
            raise TypeError("Идентификатор читателя должен быть int")
        if reader_id <= 0:
            raise ValueError("Идентификатор читателя должен быть положительным")
        ...

    @abstractmethod
    def return_book(self) -> None:
        """
        Возврат книги в библиотеку.

        :return: None

        Примеры:
        >>> book = ConcreteLibraryBook("Python", 300, True)
        >>> book.return_book()
        """
        ...

    @abstractmethod
    def estimate_reading_time(self, pages_per_hour: int) -> float:
        """
        Оценка времени чтения.

        :param pages_per_hour: Скорость чтения
        :return: Время чтения в часах

        Примеры:
        >>> book = ConcreteLibraryBook("Python", 300, False)
        >>> book.estimate_reading_time(50)
        """
        if not isinstance(pages_per_hour, int):
            raise TypeError("Скорость чтения должна быть int")
        if pages_per_hour <= 0:
            raise ValueError("Скорость чтения должна быть положительной")
        ...


class SmartDevice(ABC):
    def __init__(self, brand: str, power_watts: int, is_on: bool):
        """
        Создание и подготовка к работе объекта "Умное устройство"

        :param brand: Бренд устройства
        :param power_watts: Потребляемая мощность
        :param is_on: Состояние включения

        Примеры:
        >>> device = ConcreteSmartDevice("Acme", 60, False)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not brand.strip():
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(power_watts, int):
            raise TypeError("Мощность должна быть int")
        if power_watts <= 0:
            raise ValueError("Мощность должна быть положительной")
        self.power_watts = power_watts

        if not isinstance(is_on, bool):
            raise TypeError("Состояние включения должно быть bool")
        self.is_on = is_on

    @abstractmethod
    def turn_on(self) -> None:
        """
        Включить устройство.

        :return: None

        Примеры:
        >>> device = ConcreteSmartDevice("Acme", 60, False)
        >>> device.turn_on()
        """
        ...

    @abstractmethod
    def turn_off(self) -> None:
        """
        Выключить устройство.

        :return: None

        Примеры:
        >>> device = ConcreteSmartDevice("Acme", 60, True)
        >>> device.turn_off()
        """
        ...

    @abstractmethod
    def set_power_mode(self, mode: str) -> None:
        """
        Установить режим мощности.

        :param mode: Режим мощности (например, "eco", "normal", "turbo")

        Примеры:
        >>> device = ConcreteSmartDevice("Acme", 60, False)
        >>> device.set_power_mode("eco")
        """
        if not isinstance(mode, str):
            raise TypeError("Режим должен быть строкой")
        if not mode.strip():
            raise ValueError("Режим не может быть пустым")
        ...


class OnlineCourse(ABC):
    def __init__(self, name: str, duration_hours: float, rating: float):
        """
        Создание и подготовка к работе объекта "Онлайн-курс"

        :param name: Название курса
        :param duration_hours: Длительность в часах
        :param rating: Рейтинг курса (0.0 - 5.0)

        Примеры:
        >>> course = ConcreteOnlineCourse("Python базовый", 20.5, 4.8)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not name.strip():
            raise ValueError("Название не может быть пустым")
        self.name = name

        if not isinstance(duration_hours, (int, float)):
            raise TypeError("Длительность должна быть int или float")
        if duration_hours <= 0:
            raise ValueError("Длительность должна быть положительной")
        self.duration_hours = float(duration_hours)

        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен быть int или float")
        if not (0.0 <= rating <= 5.0):
            raise ValueError("Рейтинг должен быть в диапазоне 0.0-5.0")
        self.rating = float(rating)

    @abstractmethod
    def enroll(self, student_id: int) -> None:
        """
        Записать студента на курс.

        :param student_id: Идентификатор студента

        Примеры:
        >>> course = ConcreteOnlineCourse("Python базовый", 20.5, 4.8)
        >>> course.enroll(10)
        """
        if not isinstance(student_id, int):
            raise TypeError("Идентификатор студента должен быть int")
        if student_id <= 0:
            raise ValueError("Идентификатор студента должен быть положительным")
        ...

    @abstractmethod
    def start_lesson(self, lesson_number: int) -> None:
        """
        Начать урок.

        :param lesson_number: Номер урока

        Примеры:
        >>> course = ConcreteOnlineCourse("Python базовый", 20.5, 4.8)
        >>> course.start_lesson(1)
        """
        if not isinstance(lesson_number, int):
            raise TypeError("Номер урока должен быть int")
        if lesson_number <= 0:
            raise ValueError("Номер урока должен быть положительным")
        ...

    @abstractmethod
    def get_certificate(self, student_id: int) -> str:
        """
        Получить сертификат по окончании курса.

        :param student_id: Идентификатор студента
        :return: Строка с названием сертификата

        Примеры:
        >>> course = ConcreteOnlineCourse("Python базовый", 20.5, 4.8)
        >>> course.get_certificate(10)
        """
        if not isinstance(student_id, int):
            raise TypeError("Идентификатор студента должен быть int")
        if student_id <= 0:
            raise ValueError("Идентификатор студента должен быть положительным")
        ...


class ConcreteLibraryBook(LibraryBook):
    def check_out(self, reader_id: int) -> None:
        super().check_out(reader_id)

    def return_book(self) -> None:
        ...

    def estimate_reading_time(self, pages_per_hour: int) -> float:
        super().estimate_reading_time(pages_per_hour)
        ...


class ConcreteSmartDevice(SmartDevice):
    def turn_on(self) -> None:
        ...

    def turn_off(self) -> None:
        ...

    def set_power_mode(self, mode: str) -> None:
        super().set_power_mode(mode)


class ConcreteOnlineCourse(OnlineCourse):
    def enroll(self, student_id: int) -> None:
        super().enroll(student_id)

    def start_lesson(self, lesson_number: int) -> None:
        super().start_lesson(lesson_number)

    def get_certificate(self, student_id: int) -> str:
        super().get_certificate(student_id)
        ...


if __name__ == "__main__":
    doctest.testmod()