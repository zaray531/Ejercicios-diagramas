class Empleado:
    def __init__(self, id, nombre, salario):
        self.__id = id
        self.__nombre = nombre
        self.__salario = salario

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_salario(self):
        return self.__salario

    def __str__(self):
        return (f"[{self.__class__.__name__}] ID: {self.__id} | Nombre: {self.__nombre} | "
                f"Salario: ${self.calcular_salario():,.0f}")


class EmpleadoFijo(Empleado):
    def __init__(self, id, nombre, salario, salario_fijo):
        super().__init__(id, nombre, salario)
        self.__salario_fijo = salario_fijo

    # Getters
    def get_salario_fijo(self):
        return self.__salario_fijo

    # Setters
    def set_salario_fijo(self, salario_fijo):
        self.__salario_fijo = salario_fijo

    def calcular_salario(self):
        return self.__salario_fijo


class Contratista(Empleado):
    def __init__(self, id, nombre, salario, tarifa_hora, horas_trabajadas):
        super().__init__(id, nombre, salario)
        self.__tarifa_hora = tarifa_hora
        self.__horas_trabajadas = horas_trabajadas

    # Getters
    def get_tarifa_hora(self):
        return self.__tarifa_hora

    def get_horas_trabajadas(self):
        return self.__horas_trabajadas

    # Setters
    def set_tarifa_hora(self, tarifa_hora):
        self.__tarifa_hora = tarifa_hora

    def set_horas_trabajadas(self, horas_trabajadas):
        self.__horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.__tarifa_hora * self.__horas_trabajadas
