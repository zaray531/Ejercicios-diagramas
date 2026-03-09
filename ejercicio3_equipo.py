class Jugador:
    def __init__(self, nombre, edad, posicion, numero_camiseta):
        self.__nombre = nombre
        self.__edad = edad
        self.__posicion = posicion
        self.__numero_camiseta = numero_camiseta

    
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_posicion(self):
        return self.__posicion

    def get_numero_camiseta(self):
        return self.__numero_camiseta

    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_posicion(self, posicion):
        self.__posicion = posicion

    def set_numero_camiseta(self, numero_camiseta):
        self.__numero_camiseta = numero_camiseta

    def __str__(self):
        return (f"#{self.__numero_camiseta} {self.__nombre} "
                f"({self.__posicion}, {self.__edad} años)")


class Equipo:
    def __init__(self, nombre, ciudad, entrenador):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__entrenador = entrenador
        self.__jugadores = []

    
    def get_nombre(self):
        return self.__nombre

    def get_ciudad(self):
        return self.__ciudad

    def get_entrenador(self):
        return self.__entrenador

    def get_jugadores(self):
        return self.__jugadores


    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def set_entrenador(self, entrenador):
        self.__entrenador = entrenador

    
    def agregar_jugadores(self, jugador: Jugador):
        if len(self.__jugadores) < 24:
            self.__jugadores.append(jugador)
            print(f"  {jugador.get_nombre()} agregado al equipo {self.__nombre}.")
        else:
            print("  El equipo ya tiene el máximo de 24 jugadores.")

    def remover_jugadores(self, jugador: Jugador):
        if jugador in self.__jugadores:
            self.__jugadores.remove(jugador)
            print(f"  {jugador.get_nombre()} removido del equipo {self.__nombre}.")
        else:
            print(f"  {jugador.get_nombre()} no pertenece a este equipo.")

    def mostrar_plantilla(self):
        print(f"\n  === Plantilla: {self.__nombre} ({self.__ciudad}) ===")
        print(f"  Entrenador: {self.__entrenador}")
        if not self.__jugadores:
            print("  No hay jugadores registrados.")
        for j in self.__jugadores:
            print(f"  {j}")

    def __str__(self):
        return (f"Equipo: {self.__nombre} | Ciudad: {self.__ciudad} | "
                f"Entrenador: {self.__entrenador} | Jugadores: {len(self.__jugadores)}")
