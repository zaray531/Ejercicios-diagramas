# Ejercicios de Programación Orientada a Objetos en Python

Este proyecto contiene la implementación en Python de 8 ejercicios de Programación Orientada a Objetos (POO), basados en diagramas de clases UML. Cada ejercicio aplica conceptos como encapsulamiento, herencia, polimorfismo, composición y agregación.

---

## Estructura del Proyecto

```
proyecto/
├── main.py                          # Archivo principal que instancia todos los ejercicios
├── ejercicio1_cuenta_bancaria.py    # Ejercicio 1: CuentaBancaria
├── ejercicio2_automovil.py          # Ejercicio 2: Automovil y Motor
├── ejercicio3_equipo.py             # Ejercicio 3: Equipo y Jugador
├── ejercicio4_formas.py             # Ejercicio 4: FormaGeometrica, Circulo, Rectangulo
├── ejercicio5_empleado.py           # Ejercicio 5: Empleado, EmpleadoFijo, Contratista
├── ejercicio6_vehiculo.py           # Ejercicio 6: Vehiculo, Terrestres, Barcos
├── ejercicio7_pedido.py             # Ejercicio 7: Cliente, Producto, Pedido
└── ejercicio8_zoologico.py          # Ejercicio 8: Animal, Mamifero, Aves, Jaula, Cuidador
```

---

## Cómo Ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Descarga todos los archivos en la **misma carpeta**.
3. Abre una terminal en esa carpeta y ejecuta:

```bash
python main.py
```

---

## Conceptos OO Aplicados

| Concepto | Descripción | Ejercicios |
|---|---|---|
| **Encapsulamiento** | Atributos privados con `__` y acceso mediante getters/setters | Todos |
| **Herencia** | Subclases que extienden una clase padre con `super().__init__()` | 4, 5, 6, 8 |
| **Polimorfismo** | Métodos sobreescritos que se comportan diferente según la subclase | 4, 5, 6, 8 |
| **Composición** | Un objeto contiene a otro y depende de él para existir | 2, 7 |
| **Agregación** | Un objeto agrupa a otros que pueden existir de forma independiente | 3, 7, 8 |

---

## Descripción de Cada Ejercicio

### Ejercicio 1 — CuentaBancaria
**Archivo:** `ejercicio1_cuenta_bancaria.py`

Clase simple que modela una cuenta bancaria con atributos privados y operaciones financieras básicas.

**Atributos:** `numeroCuenta`, `titular`, `saldo`, `fecha_apertura`

**Métodos:**
- `depositarDinero(monto)` — Suma el monto al saldo si es mayor a 0.
- `retirarDinero(monto)` — Resta el monto si hay fondos suficientes.

**Conceptos:** Encapsulamiento, getters y setters.

---

### Ejercicio 2 — Automovil y Motor
**Archivo:** `ejercicio2_automovil.py`

Modela un automóvil que **contiene** un motor como parte esencial de su estructura.

**Clases:**
- `Motor` — atributos: `cilindrada`, `tipoCombustible`, `potencia`
- `Automovil` — atributos: `marca`, `modelo`, `anio`, `color`, `motor: Motor`

**Conceptos:** Encapsulamiento, **Composición** (el Motor vive dentro del Automovil y se crea antes que él).

---

### Ejercicio 3 — Equipo y Jugador
**Archivo:** `ejercicio3_equipo.py`

Modela un equipo de fútbol que puede tener hasta 24 jugadores. Los jugadores existen de forma independiente al equipo.

**Clases:**
- `Jugador` — atributos: `nombre`, `edad`, `posicion`, `numeroCamiseta`
- `Equipo` — atributos: `nombre`, `ciudad`, `entrenador`, `jugadores`

**Métodos de Equipo:**
- `agregarJugadores(jugador)` — Agrega un jugador si no se supera el límite de 24.
- `removerJugadores(jugador)` — Elimina un jugador de la lista.
- `mostrarPlantilla()` — Imprime todos los jugadores del equipo.

**Conceptos:** Encapsulamiento, **Agregación** (los jugadores se crean antes que el equipo y pueden pertenecer a varios equipos).

---

### Ejercicio 4 — Formas Geométricas
**Archivo:** `ejercicio4_formas.py`

Jerarquía de clases para calcular áreas de figuras geométricas.

**Clases:**
- `FormaGeometrica` — clase base con atributo `color` y métodos `calcularArea()` y `mostrarInformacion()`
- `Circulo` — hereda de `FormaGeometrica`, agrega `radio` y `pi`
- `Rectangulo` — hereda de `FormaGeometrica`, agrega `base` y `altura`

**Métodos sobreescritos:**
- `calcularArea()` en `Circulo` → `π * radio²`
- `calcularArea()` en `Rectangulo` → `base * altura`

**Conceptos:** Encapsulamiento, **Herencia**, **Polimorfismo** en `calcularArea()`.

---

### Ejercicio 5 — Empleados
**Archivo:** `ejercicio5_empleado.py`

Jerarquía de empleados con dos tipos de cálculo de salario.

**Clases:**
- `Empleado` — clase base con atributos `id`, `nombre`, `salario`
- `EmpleadoFijo` — hereda de `Empleado`, agrega `salarioFijo`
- `Contratista` — hereda de `Empleado`, agrega `tarifaHora` y `horasTrabajadas`

**Métodos sobreescritos:**
- `calcularSalario()` en `EmpleadoFijo` → retorna el salario fijo
- `calcularSalario()` en `Contratista` → retorna `tarifaHora * horasTrabajadas`

**Conceptos:** Encapsulamiento, **Herencia**, **Polimorfismo** en `calcularSalario()`.

---

### Ejercicio 6 — Vehículos
**Archivo:** `ejercicio6_vehiculo.py`

Jerarquía de vehículos con comportamientos específicos según su tipo.

**Clases:**
- `Vehiculo` — clase base con atributos `marca`, `modelo`, `capacidadPasajeros` y método `mover()`
- `Terrestres` — hereda de `Vehiculo`, agrega `numeroRuedas` y método `frenar()`
- `Barcos` — hereda de `Vehiculo`, agrega `tipoPropulsion` y método `anclar()`

**Métodos sobreescritos:**
- `mover()` en `Terrestres` → describe movimiento por tierra
- `mover()` en `Barcos` → describe navegación

**Conceptos:** Encapsulamiento, **Herencia**, **Polimorfismo** en `mover()`.

---

### Ejercicio 7 — Sistema de Pedidos
**Archivo:** `ejercicio7_pedido.py`

Modela un sistema de pedidos donde un pedido pertenece a un cliente y contiene productos.

**Clases:**
- `Cliente` — atributos: `nombre`, `email`, `telefono`
- `Producto` — atributos: `codigo`, `nombre`, `precio`
- `Pedido` — atributos: `cliente: Cliente`, `fecha`, `items`, `total`

**Métodos de Pedido:**
- `agregarItem(producto)` — Agrega un producto y acumula el total.
- `mostrarPedido()` — Imprime el resumen del pedido con todos los ítems y el total.

**Orden de creación obligatorio:** primero `Cliente` y `Producto`, luego `Pedido`.

**Conceptos:** Encapsulamiento, **Composición** (Cliente dentro de Pedido), **Agregación** (Productos dentro de Pedido).

---

### Ejercicio 8 — Zoológico
**Archivo:** `ejercicio8_zoologico.py`

El ejercicio más completo. Modela un zoológico con animales, jaulas y cuidadores, combinando herencia, polimorfismo y agregación.

**Clases:**
- `Animal` — clase base con atributos `nombre`, `edad`, `especie` y métodos `hacerSonido()`, `comer()`
- `Mamifero` — hereda de `Animal`, agrega `tipoPelaje` y método `amamantan()`
- `Aves` — hereda de `Animal`, agrega `envergaduraAlas` y método `volar()`
- `Cuidador` — atributos: `nombre`, `aniosExperiencia`
- `Jaula` — atributos: `numero`, `capacidad`, `cuidador: Cuidador`, `animales`

**Métodos sobreescritos:**
- `hacerSonido()` en `Mamifero` → "ruge/gruñe"
- `hacerSonido()` en `Aves` → "canta/pía"

**Orden de creación obligatorio:** primero `Cuidador`, luego los animales (`Mamifero`, `Aves`), finalmente `Jaula`.

**Conceptos:** Encapsulamiento, **Herencia**, **Polimorfismo** en `hacerSonido()`, **Agregación** (Jaula agrupa animales y un Cuidador que existen de forma independiente).

---

## Reglas Generales Aplicadas en Todos los Ejercicios

- Todos los atributos son **privados** (declarados con `__`).
- Cada clase tiene **getters y setters** para todos sus atributos.
- En `main.py` se crean **mínimo 4 objetos por cada clase**.
- Los objetos se instancian en el **orden correcto** según la lógica de negocio: en relaciones de composición o agregación, los objetos contenidos se crean antes que el contenedor.




