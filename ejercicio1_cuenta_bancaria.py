from datetime import date


class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo, fecha_apertura):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo
        self.__fecha_apertura = fecha_apertura

    # Getters
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_fecha_apertura(self):
        return self.__fecha_apertura

    # Setters
    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def set_titular(self, titular):
        self.__titular = titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_fecha_apertura(self, fecha_apertura):
        self.__fecha_apertura = fecha_apertura

    # Métodos
    def depositar_dinero(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"  Depósito de ${monto:,.0f} exitoso. Nuevo saldo: ${self.__saldo:,.0f}")
        else:
            print("  El monto a depositar debe ser mayor a 0.")

    def retirar_dinero(self, monto):
        if monto <= 0:
            print("  El monto a retirar debe ser mayor a 0.")
        elif monto > self.__saldo:
            print(f"  Fondos insuficientes. Saldo disponible: ${self.__saldo:,.0f}")
        else:
            self.__saldo -= monto
            print(f"  Retiro de ${monto:,.0f} exitoso. Nuevo saldo: ${self.__saldo:,.0f}")

    def __str__(self):
        return (f"Cuenta: {self.__numero_cuenta} | Titular: {self.__titular} | "
                f"Saldo: ${self.__saldo:,.0f} | Apertura: {self.__fecha_apertura}")
