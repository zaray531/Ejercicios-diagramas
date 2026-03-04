import math


class FormaGeometrica:
    def __init__(self, color):
        self.__color = color

    # Getters
    def get_color(self):
        return self.__color

    # Setters
    def set_color(self, color):
        self.__color = color

    def calcular_area(self):
        raise NotImplementedError("Subclases deben implementar calcular_area()")

    def mostrar_informacion(self):
        print(f"  Forma: {self.__class__.__name__} | Color: {self.__color} | "
              f"Área: {self.calcular_area():.2f}")

    def __str__(self):
        return f"{self.__class__.__name__}(color={self.__color})"


class Circulo(FormaGeometrica):
    PI = math.pi

    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    # Getters
    def get_pi(self):
        return self.PI

    def get_radio(self):
        return self.__radio

    # Setters
    def set_radio(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return self.PI * self.__radio ** 2

    def __str__(self):
        return f"Círculo(color={self.get_color()}, radio={self.__radio})"


class Rectangulo(FormaGeometrica):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.__base = base
        self.__altura = altura

    # Getters
    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    # Setters
    def set_base(self, base):
        self.__base = base

    def set_altura(self, altura):
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura

    def __str__(self):
        return (f"Rectángulo(color={self.get_color()}, "
                f"base={self.__base}, altura={self.__altura})")
