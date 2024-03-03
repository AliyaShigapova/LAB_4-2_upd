class Shape:
    """
    Базовый класс для геометрических фигур.

    Атрибуты:
        _name (str): Название фигуры.
        _perimeter (float): Периметр фигуры.
        _area (float): Площадь фигуры.

    Методы:
        __init__(name: str) -> None: Инициализирует фигуру.
        __str__(self) -> str: Возвращает строковое представление фигуры.
        __repr__(self) -> str: Возвращает каноническое представление фигуры.
        get_name(self) -> str: Возвращает название фигуры.
        get_perimeter(self) -> float: Возвращает периметр фигуры.
        get_area(self) -> float: Возвращает площадь фигуры.
    """

    def __init__(self, name: str) -> None:
        """
        Инициализирует фигуру.

        Args:
            name (str): Название фигуры.
        """
        self._name = name
        self._perimeter = None
        self._area = None

    def __str__(self) -> str:
        """
        Возвращает строковое представление фигуры.

        Returns:
            str: Строковое представление фигуры.
        """
        return f"{self._name}({self._perimeter}, {self._area})"

    def __repr__(self) -> str:
        """
        Возвращает каноническое представление фигуры.

        Returns:
            str: Каноническое представление фигуры.
        """
        return f"{type(self).__name__}('{self._name}')"

    def get_name(self) -> str:
        """
        Возвращает название фигуры.

        Returns:
            str: Название фигуры.
        """
        return self._name

    def get_perimeter(self) -> float:
        """
        Возвращает периметр фигуры.

        Returns:
            float: Периметр фигуры.
        """
        if self._perimeter is None:
            self._perimeter = self._calculate_perimeter()
        return self._perimeter

    def get_area(self) -> float:
        """
        Возвращает площадь фигуры.

        Returns:
            float: Площадь фигуры.
        """
        if self._area is None:
            self._area = self._calculate_area()
        return self._area

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


class Rect(Shape):
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
        _length (float): Длина стороны прямоугольника.
        _width (float): Ширина стороны прямоугольника.

    Методы:
        __init__(self, название: str, длина: float, ширина: float) -> None: Инициализирует прямоугольник.
        get_perimeter(self) -> float: Возвращает периметр прямоугольника.
        get_area(self) -> float: Возвращает площадь прямоугольника.
    """

    def __init__(self, name: str, length: float, width: float) -> None:
        """
        Инициализирует прямоугольник.

        Args:
            name (str): Название прямоугольника.
            length (float): Длина стороны прямоугольника.
            width (float): Ширина стороны прямоугольника.
        """
        super().__init__(name)
        self._length = length
        self._width = width

    def get_perimeter(self) -> float:
        """
        Возвращает периметр прямоугольника.
        Returns:
            float: Периметр прямоугольника.
        """
