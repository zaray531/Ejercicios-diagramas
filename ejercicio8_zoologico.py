class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

    
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_especie(self):
        return self.__especie

   
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_especie(self, especie):
        self.__especie = especie

    def hacer_sonido(self):
        print(f"  {self.__nombre} hace un sonido genérico.")

    def comer(self):
        print(f"  {self.__nombre} está comiendo.")

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__nombre} ({self.__especie}, {self.__edad} años)"


class Mamifero(Animal):
    def __init__(self, nombre, edad, especie, tipo_pelaje):
        super().__init__(nombre, edad, especie)
        self.__tipo_pelaje = tipo_pelaje

 
    def get_tipo_pelaje(self):
        return self.__tipo_pelaje

   
    def set_tipo_pelaje(self, tipo_pelaje):
        self.__tipo_pelaje = tipo_pelaje

    def amamantan(self):
        print(f"  {self.get_nombre()} amamanta a sus crías.")

    def hacer_sonido(self):
        print(f"  {self.get_nombre()} ruge/gruñe.")

    def __str__(self):
        return super().__str__() + f" | Pelaje: {self.__tipo_pelaje}"


class Aves(Animal):
    def __init__(self, nombre, edad, especie, envergadura_alas):
        super().__init__(nombre, edad, especie)
        self.__envergadura_alas = envergadura_alas


    def get_envergadura_alas(self):
        return self.__envergadura_alas

   
    def set_envergadura_alas(self, envergadura_alas):
        self.__envergadura_alas = envergadura_alas

    def volar(self):
        print(f"  {self.get_nombre()} vuela con una envergadura de {self.__envergadura_alas}cm.")

    def hacer_sonido(self):
        print(f"  {self.get_nombre()} canta/pía.")

    def __str__(self):
        return super().__str__() + f" | Envergadura: {self.__envergadura_alas}cm"


class Cuidador:
    def __init__(self, nombre, anios_experiencia):
        self.__nombre = nombre
        self.__anios_experiencia = anios_experiencia

   
    def get_nombre(self):
        return self.__nombre

    def get_anios_experiencia(self):
        return self.__anios_experiencia

  
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_anios_experiencia(self, anios_experiencia):
        self.__anios_experiencia = anios_experiencia

    def __str__(self):
        return f"Cuidador: {self.__nombre} ({self.__anios_experiencia} años exp.)"


class Jaula:
    def __init__(self, numero, capacidad, cuidador: Cuidador):
        self.__numero = numero
        self.__capacidad = capacidad
        self.__cuidador = cuidador
        self.__animales = []

    
    def get_numero(self):
        return self.__numero

    def get_capacidad(self):
        return self.__capacidad

    def get_cuidador(self):
        return self.__cuidador

    def get_animales(self):
        return self.__animales

    
    def set_numero(self, numero):
        self.__numero = numero

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad

    def set_cuidador(self, cuidador):
        self.__cuidador = cuidador

    def agregar_animal(self, animal: Animal):
        if len(self.__animales) < self.__capacidad:
            self.__animales.append(animal)
            print(f"  {animal.get_nombre()} asignado a jaula #{self.__numero}.")
        else:
            print(f"  Jaula #{self.__numero} está llena (capacidad: {self.__capacidad}).")

    def mostrar_info(self):
        print(f"\n  === Jaula #{self.__numero} | {self.__cuidador} ===")
        if not self.__animales:
            print("  Sin animales asignados.")
        for a in self.__animales:
            print(f"  {a}")

    def __str__(self):
        return (f"Jaula #{self.__numero} | Capacidad: {self.__capacidad} | "
                f"Animales: {len(self.__animales)} | {self.__cuidador}")
