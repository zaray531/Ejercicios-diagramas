class Motor:
    def __init__(self, cilindrada, tipo_combustible, potencia):
        self.__cilindrada = cilindrada
        self.__tipo_combustible = tipo_combustible
        self.__potencia = potencia

    # Getters
    def get_cilindrada(self):
        return self.__cilindrada

    def get_tipo_combustible(self):
        return self.__tipo_combustible

    def get_potencia(self):
        return self.__potencia

    # Setters
    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def set_tipo_combustible(self, tipo_combustible):
        self.__tipo_combustible = tipo_combustible

    def set_potencia(self, potencia):
        self.__potencia = potencia

    def __str__(self):
        return (f"Motor({self.__cilindrada}cc, {self.__tipo_combustible}, "
                f"{self.__potencia}HP)")


class Automovil:
    def __init__(self, marca, modelo, anio, color, motor: Motor):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__color = color
        self.__motor = motor

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__anio

    def get_color(self):
        return self.__color

    def get_motor(self):
        return self.__motor

    # Setters
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_anio(self, anio):
        self.__anio = anio

    def set_color(self, color):
        self.__color = color

    def set_motor(self, motor):
        self.__motor = motor

    def __str__(self):
        return (f"{self.__anio} {self.__marca} {self.__modelo} ({self.__color}) | "
                f"{self.__motor}")
