class Vehiculo:
    def __init__(self, marca, modelo, capacidad_pasajeros):
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad_pasajeros = capacidad_pasajeros

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_capacidad_pasajeros(self):
        return self.__capacidad_pasajeros

    # Setters
    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self.__capacidad_pasajeros = capacidad_pasajeros

    def mover(self):
        print(f"  {self.__class__.__name__} {self.__marca} {self.__modelo} está en movimiento.")

    def __str__(self):
        return (f"[{self.__class__.__name__}] {self.__marca} {self.__modelo} | "
                f"Pasajeros: {self.__capacidad_pasajeros}")


class Terrestres(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros, numero_ruedas):
        super().__init__(marca, modelo, capacidad_pasajeros)
        self.__numero_ruedas = numero_ruedas

    # Getters
    def get_numero_ruedas(self):
        return self.__numero_ruedas

    # Setters
    def set_numero_ruedas(self, numero_ruedas):
        self.__numero_ruedas = numero_ruedas

    def frenar(self):
        print(f"  {self.get_marca()} {self.get_modelo()} frenando con {self.__numero_ruedas} ruedas.")

    def mover(self):
        print(f"  {self.get_marca()} {self.get_modelo()} avanza por tierra con {self.__numero_ruedas} ruedas.")

    def __str__(self):
        return super().__str__() + f" | Ruedas: {self.__numero_ruedas}"


class Barcos(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros, tipo_propulsion):
        super().__init__(marca, modelo, capacidad_pasajeros)
        self.__tipo_propulsion = tipo_propulsion

    # Getters
    def get_tipo_propulsion(self):
        return self.__tipo_propulsion

    # Setters
    def set_tipo_propulsion(self, tipo_propulsion):
        self.__tipo_propulsion = tipo_propulsion

    def anclar(self):
        print(f"  {self.get_marca()} {self.get_modelo()} está anclado.")

    def mover(self):
        print(f"  {self.get_marca()} {self.get_modelo()} navega con propulsión {self.__tipo_propulsion}.")

    def __str__(self):
        return super().__str__() + f" | Propulsión: {self.__tipo_propulsion}"
