class Фигура:
    """
    Базовый класс для геометрических фигур.

    Атрибуты:
        _название (str): Название фигуры.
        _периметр (float): Периметр фигуры.
        _площадь (float): Площадь фигуры.

    Методы:
        __init__(название: str) -> None: Инициализирует фигуру.
        __str__(self) -> str: Возвращает строковое представление фигуры.
        __repr__(self) -> str: Возвращает каноническое представление фигуры.
        get_название(self) -> str: Возвращает название фигуры.
        get_периметр(self) -> float: Возвращает периметр фигуры.
        get_площадь(self) -> float: Возвращает площадь фигуры.
    """

    def __init__(self, название: str) -> None:
        """
        Инициализирует фигуру.

        Args:
            название (str): Название фигуры.
        """
        self._название = название
        self._периметр = None
        self._площадь = None

    def __str__(self) -> str:
        """
        Возвращает строковое представление фигуры.

        Returns:
            str: Строковое представление фигуры.
        """
        return f"{self._название}({self._периметр}, {self._площадь})"

    def __repr__(self) -> str:
        """
        Возвращает каноническое представление фигуры.

        Returns:
            str: Каноническое представление фигуры.
        """
        return f"{type(self).__name__}('{self._название}')"

    def get_название(self) -> str:
        """
        Возвращает название фигуры.

        Returns:
            str: Название фигуры.
        """
        return self._название

    def get_периметр(self) -> float:
        """
        Возвращает периметр фигуры.

        Returns:
            float: Периметр фигуры.
        """
        if self._периметр is None:
            self._периметр = self._calculate_perimeter()
        return self._периметр

    def get_площадь(self) -> float:
        """
        Возвращает площадь фигуры.

        Returns:
            float: Площадь фигуры.
        """
        if self._площадь is None:
            self._площадь = self._calculate_area()
        return self._площадь

    def _calculate_perimeter(self) -> float:
        """
        Вычисляет периметр фигуры.

        Returns:
            float: Периметр фигуры.
        """
        raise NotImplementedError

    def _calculate_area(self) -> float:
        """
        Вычисляет площадь фигуры.

        Returns:
            float: Площадь фигуры.
        """
        raise NotImplementedError


class Прямоугольник(Фигура):
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
        _длина (float): Длина стороны прямоугольника.
        _ширина (float): Ширина стороны прямоугольника.

    Методы:
        __init__(self, название: str, длина: float, ширина: float) -> None: Инициализирует прямоугольник.
        get_периметр(self) -> float: Возвращает периметр прямоугольника.
        get_площадь(self) -> float: Возвращает площадь прямоугольника.
    """

    def __init__(self, название: str, длина: float, ширина: float) -> None:
        """
        Инициализирует прямоугольник.

        Args:
            название (str): Название прямоугольника.
            длина (float): Длина стороны прямоугольника.
            ширина (float): Ширина стороны прямоугольника.
        """
        super().__init__(название)
        self._длина = длина
        self._ширина = ширина

    def get_периметр(self) -> float:
        """
        Возвращает периметр прямоугольника.

        Returns:
            float: Периметр прямоугольника.
        """

