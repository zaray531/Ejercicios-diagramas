from datetime import date
from ejercicio1_cuenta_bancaria import CuentaBancaria
from ejercicio2_automovil import Motor, Automovil
from ejercicio3_equipo import Jugador, Equipo
from ejercicio4_formas import Circulo, Rectangulo
from ejercicio5_empleado import EmpleadoFijo, Contratista
from ejercicio6_vehiculo import Terrestres, Barcos
from ejercicio7_pedido import Cliente, Producto, Pedido
from ejercicio8_zoologico import Mamifero, Aves, Cuidador, Jaula


def separador(titulo):
    print(f"\n{'='*60}")
    print(f"  {titulo}")
    print('='*60)



separador("EJERCICIO 1: CUENTA BANCARIA")

c1 = CuentaBancaria("001-123", "Ana Gómez",    5_000_000, date(2020, 3, 15))
c2 = CuentaBancaria("001-456", "Luis Pérez",   2_500_000, date(2021, 7,  1))
c3 = CuentaBancaria("001-789", "María Torres", 8_000_000, date(2019, 11, 20))
c4 = CuentaBancaria("001-321", "Carlos Ruiz",  1_200_000, date(2023, 1,  5))

for c in [c1, c2, c3, c4]:
    print(f"\n{c}")

print("\n--- Operaciones ---")
c1.depositar_dinero(500_000)
c1.retirar_dinero(200_000)
c1.retirar_dinero(10_000_000)
c2.depositar_dinero(1_000_000)
c2.retirar_dinero(800_000)
c3.depositar_dinero(300_000)
c4.retirar_dinero(500_000)



separador("EJERCICIO 2: AUTOMOVIL (Composición)")

m1 = Motor(2000, "Gasolina",  150)
m2 = Motor(1600, "Diesel",    110)
m3 = Motor(3000, "Gasolina",  250)
m4 = Motor(1000, "Eléctrico",  90)

a1 = Automovil("Toyota",    "Corolla", 2022, "Blanco", m1)
a2 = Automovil("Renault",   "Duster",  2021, "Gris",   m2)
a3 = Automovil("BMW",       "Serie 3", 2023, "Negro",  m3)
a4 = Automovil("Chevrolet", "Spark",   2020, "Rojo",   m4)

for a in [a1, a2, a3, a4]:
    print(f"{a}")



separador("EJERCICIO 3: EQUIPO DE FÚTBOL (Agregación)")

j1  = Jugador("James Rodríguez",  32, "Mediocampista", 10)
j2  = Jugador("Falcao García",    37, "Delantero",      9)
j3  = Jugador("Davinson Sánchez", 27, "Defensa",        6)
j4  = Jugador("David Ospina",     35, "Portero",        1)
j5  = Jugador("Luis Díaz",        27, "Extremo",        7)
j6  = Jugador("Juan Cuadrado",    35, "Lateral",        2)
j7  = Jugador("Miguel Borja",     31, "Delantero",     11)
j8  = Jugador("Juan Quintero",    31, "Mediocampista",  8)
j9  = Jugador("Stefan Medina",    30, "Lateral",        2)
j10 = Jugador("Jhon Lucumí",      26, "Defensa",        4)
j11 = Jugador("Camilo Vargas",    32, "Portero",       12)
j12 = Jugador("Jefferson Lerma",  29, "Mediocampista",  6)

eq1 = Equipo("Selección Colombia", "Bogotá",    "Néstor Lorenzo")
eq2 = Equipo("Atlético Nacional",  "Medellín",  "Jhon Bodmer")
eq3 = Equipo("Millonarios FC",     "Bogotá",    "Alberto Gamero")
eq4 = Equipo("América de Cali",    "Cali",      "Jorge Da Silva")

print("\n--- Equipos creados ---")
for eq in [eq1, eq2, eq3, eq4]:
    print(f"  {eq}")

print("\n--- Agregando jugadores ---")
for j in [j1, j2, j3, j4, j5]:
    eq1.agregar_jugadores(j)
for j in [j6, j7, j8, j9]:
    eq2.agregar_jugadores(j)
for j in [j10, j11, j12]:
    eq3.agregar_jugadores(j)
for j in [j1, j4, j6, j7]:
    eq4.agregar_jugadores(j)

eq1.mostrar_plantilla()
eq2.mostrar_plantilla()
eq3.mostrar_plantilla()
eq4.mostrar_plantilla()

print("\n--- Removiendo un jugador ---")
eq1.remover_jugadores(j2)
eq1.mostrar_plantilla()



separador("EJERCICIO 4: FORMAS GEOMÉTRICAS (Herencia + Polimorfismo)")

circulos = [
    Circulo("Rojo",    5.0),
    Circulo("Azul",    3.5),
    Circulo("Verde",   7.2),
    Circulo("Naranja", 1.8),
]

rectangulos = [
    Rectangulo("Amarillo", 8,  4),
    Rectangulo("Morado",   12, 6),
    Rectangulo("Gris",     5,  5),
    Rectangulo("Café",     10, 3),
]

print("\n--- Círculos ---")
for c in circulos:
    c.mostrar_informacion()

print("\n--- Rectángulos ---")
for r in rectangulos:
    r.mostrar_informacion()

print("\n--- Polimorfismo: todas las formas juntas ---")
for forma in circulos + rectangulos:
    print(f"  {forma} → Área: {forma.calcular_area():.2f}")



separador("EJERCICIO 5: EMPLEADOS (Herencia + Polimorfismo)")

fijos = [
    EmpleadoFijo("E001", "Sofía Mendoza",  0, 4_500_000),
    EmpleadoFijo("E002", "Pedro Castillo", 0, 3_800_000),
    EmpleadoFijo("E003", "Camila Herrera", 0, 5_200_000),
    EmpleadoFijo("E004", "Nicolás Pardo",  0, 2_900_000),
]

contratistas = [
    Contratista("C001", "Laura Vargas",  0, 85_000, 120),
    Contratista("C002", "Andrés Mora",   0, 70_000, 160),
    Contratista("C003", "Diana Salinas", 0, 95_000,  80),
    Contratista("C004", "Felipe Castro", 0, 60_000, 200),
]

print("\n--- Empleados Fijos ---")
for e in fijos:
    print(f"  {e}")

print("\n--- Contratistas ---")
for c in contratistas:
    print(f"  {c}")

print("\n--- Polimorfismo: nómina completa ---")
for emp in fijos + contratistas:
    print(f"  {emp.get_nombre()} → Salario: ${emp.calcular_salario():,.0f}")



separador("EJERCICIO 6: VEHÍCULOS (Herencia + Polimorfismo)")

terrestres = [
    Terrestres("Mazda",     "CX-5",   5,  4),
    Terrestres("Volvo",     "FH16",   2, 18),
    Terrestres("Honda",     "CB500",  2,  2),
    Terrestres("Chevrolet", "Tahoe",  8,  4),
]

barcos = [
    Barcos("Carnival",        "Vista",      3000, "Motor Diésel"),
    Barcos("Royal Caribbean", "Symphony",   6000, "Turbina a Gas"),
    Barcos("MSC",             "Meraviglia", 5700, "Motor Diésel"),
    Barcos("Norwegian",       "Bliss",      4000, "Propulsión Azipod"),
]

print("\n--- Polimorfismo en mover() ---")
for v in terrestres + barcos:
    print(f"\n  {v}")
    v.mover()

print("\n--- Métodos específicos ---")
for t in terrestres:
    t.frenar()
for b in barcos:
    b.anclar()



separador("EJERCICIO 7: SISTEMA DE PEDIDOS (Composición/Agregación)")

cl1 = Cliente("Isabel Ramírez", "isabel@email.com",  "310-111-2222")
cl2 = Cliente("Roberto Silva",  "roberto@email.com", "320-333-4444")
cl3 = Cliente("Valentina Cruz", "vale@email.com",    "315-555-6666")
cl4 = Cliente("Sergio Lozano",  "sergio@email.com",  "311-777-8888")

p1 = Producto("P001", "Laptop Dell",       3_200_000)
p2 = Producto("P002", "Mouse Inalámbrico",    80_000)
p3 = Producto("P003", "Teclado Mecánico",    350_000)
p4 = Producto("P004", 'Monitor 27"',       1_500_000)
p5 = Producto("P005", "Audífonos Sony",      420_000)
p6 = Producto("P006", "Webcam HD",           180_000)
p7 = Producto("P007", "Disco SSD 1TB",       450_000)

print("\n--- Clientes ---")
for cl in [cl1, cl2, cl3, cl4]:
    print(f"  {cl}")

print("\n--- Productos ---")
for p in [p1, p2, p3, p4, p5, p6, p7]:
    print(f"  {p}")

# Pedidos (4) — clientes y productos deben existir antes
ped1 = Pedido(cl1, date(2026, 3, 1))
ped1.agregar_item(p1)
ped1.agregar_item(p2)
ped1.agregar_item(p3)
ped1.mostrar_pedido()

ped2 = Pedido(cl2, date(2026, 3, 2))
ped2.agregar_item(p4)
ped2.agregar_item(p5)
ped2.mostrar_pedido()

ped3 = Pedido(cl3, date(2026, 3, 3))
ped3.agregar_item(p6)
ped3.agregar_item(p7)
ped3.mostrar_pedido()

ped4 = Pedido(cl4, date(2026, 3, 3))
ped4.agregar_item(p1)
ped4.agregar_item(p4)
ped4.agregar_item(p7)
ped4.mostrar_pedido()


separador("EJERCICIO 8: ZOOLÓGICO (Herencia + Polimorfismo + Agregación)")

# Cuidadores (4) — primero porque Jaula los necesita
cu1 = Cuidador("Jorge Infante",  8)
cu2 = Cuidador("Diana Salcedo",  5)
cu3 = Cuidador("Camilo Reyes",  12)
cu4 = Cuidador("Paola Nieto",    3)

# Mamíferos (4)
ma1 = Mamifero("León",              6,  "Panthera leo",    "Corto y denso")
ma2 = Mamifero("Oso Pardo",        10,  "Ursus arctos",    "Largo y grueso")
ma3 = Mamifero("Tigre de Bengala",  7,  "Panthera tigris", "Corto rayado")
ma4 = Mamifero("Lobo Gris",         4,  "Canis lupus",     "Denso y gris")

# Aves (4)
av1 = Aves("Águila Real", 4, "Aquila chrysaetos", 220)
av2 = Aves("Tucán",       3, "Ramphastos toco",    55)
av3 = Aves("Flamenco",    6, "Phoenicopterus",      95)
av4 = Aves("Guacamaya",   5, "Ara macao",           80)

# Jaulas (4) — después de cuidadores y animales
ja1 = Jaula(1, 3, cu1)
ja2 = Jaula(2, 2, cu2)
ja3 = Jaula(3, 2, cu3)
ja4 = Jaula(4, 4, cu4)

print("\n--- Asignando animales a jaulas ---")
ja1.agregar_animal(ma1)
ja1.agregar_animal(ma2)
ja1.agregar_animal(ma3)

ja2.agregar_animal(av1)
ja2.agregar_animal(av2)

ja3.agregar_animal(ma4)
ja3.agregar_animal(av3)

ja4.agregar_animal(av4)
ja4.agregar_animal(ma1)

ja1.mostrar_info()
ja2.mostrar_info()
ja3.mostrar_info()
ja4.mostrar_info()

print("\n--- Polimorfismo en hacerSonido() ---")
for a in [ma1, ma2, ma3, ma4, av1, av2, av3, av4]:
    a.hacer_sonido()

print("\n--- Métodos específicos ---")
for m in [ma1, ma2, ma3, ma4]:
    m.amamantan()
for av in [av1, av2, av3, av4]:
    av.volar()

print("\n" + "="*60)
print("  Todos los ejercicios ejecutados correctamente.")
print("="*60)