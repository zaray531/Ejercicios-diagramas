from datetime import date


class Cliente:
    def __init__(self, nombre, email, telefono):
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"Cliente: {self.__nombre} | {self.__email} | {self.__telefono}"


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    # Setters
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"[{self.__codigo}] {self.__nombre} - ${self.__precio:,.0f}"


class Pedido:
    def __init__(self, cliente: Cliente, fecha: date):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__items = []
        self.__total = 0

    # Getters
    def get_cliente(self):
        return self.__cliente

    def get_fecha(self):
        return self.__fecha

    def get_items(self):
        return self.__items

    def get_total(self):
        return self.__total

    # Setters
    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def agregar_item(self, producto: Producto):
        self.__items.append(producto)
        self.__total += producto.get_precio()
        print(f"  Producto '{producto.get_nombre()}' agregado al pedido.")

    def mostrar_pedido(self):
        print(f"\n  === Pedido de {self.__cliente.get_nombre()} ({self.__fecha}) ===")
        for p in self.__items:
            print(f"  - {p}")
        print(f"  TOTAL: ${self.__total:,.0f}")

    def __str__(self):
        return (f"Pedido | Cliente: {self.__cliente.get_nombre()} | "
                f"Fecha: {self.__fecha} | Items: {len(self.__items)} | Total: ${self.__total:,.0f}")
