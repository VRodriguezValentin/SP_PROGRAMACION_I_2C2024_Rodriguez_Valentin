# 🔧 Proyecto: Administración de Vehículos en un Taller Mecánico 🚗🛠️

## 📝 Enunciado

Se necesita realizar un programa para la **administración de vehículos en un taller mecánico**, que permita interactuar únicamente a través de la **consola**. El mismo deberá realizarse utilizando **Python 3**, aplicando los contenidos y reglas de estilo dados en esta cátedra.

👉 Se deben diseñar e implementar las **clases necesarias** para manejar los objetos representados en los archivos `vehiculos.json` y `empleados.csv`, permitiendo su gestión en una **lista** durante el ciclo de vida del programa.

---

## ✅ Condiciones de aprobación

### 🎯 Objetivo obligatorio para aprobar

El estudiante debe demostrar **capacidad de análisis y manipulación de archivos físicos**, incluyendo:

- 🆙 Alta  
- 🗑️ Baja  
- ✏️ Modificación (ABM)  

**⚠️ Importante:** No cumplir este objetivo en la primera instancia resulta en **desaprobación directa**.

---

## 📌 Requisitos de la primera instancia

- ✅ Punto 1 y Punto 2 (ambos listados). Solo elegir un criterio de ordenamiento por punto.
- 👷‍♂️ Empleados: Puntos 3 y 6 (`alta` y `guardar empleados.csv`)
- 🚘 Vehículos: Puntos 7 y 10 (`alta` y `guardar vehiculos.json`)

---

## 📌 Requisitos de la segunda instancia

- ✅ Puntos 1 al 10 → Nota máxima: **4**
- ✅ Puntos 11 al 18 → Nota mínima: **6**

---

## 🔍 Detalle de puntos

### 1️⃣ Ver vehículos (`vehiculos.json`)
- 🔤 Ordenado por **Marca**
- 📆 Ordenado por **Año**
- 🙋 Ordenado por **Propietario**

### 2️⃣ Ver empleados (`empleados.csv`)
- 🔤 Ordenado por **Nombre**
- 💸 Ordenado por **Salario**

### 3️⃣ Empleado - ALTA  
### 4️⃣ Empleado - BAJA  
### 5️⃣ Empleado - MODIFICACIÓN  
### 6️⃣ Empleado - GUARDAR `empleados.csv`

### 7️⃣ Vehículo - ALTA  
### 8️⃣ Vehículo - BAJA  
### 9️⃣ Vehículo - MODIFICACIÓN  
### 🔟 Vehículo - GUARDAR `vehiculos.json`

---

## 🧰 Taller - Reparaciones

### 🔧 Paso 11: Reparar vehículo

- Elegir un 👨‍🔧 **empleado**
- Elegir un 🚗 **vehículo**
- Elegir una reparación de la siguiente lista:

| 🆔 ID  | 🛠️ Descripción                                 | 💰 Coste |
|-------|--------------------------------------------------|----------|
| 1000  | Mantenimiento y cambio de aceite                | $5500    |
| 1100  | Reparación de frenos                            | $1500    |
| 1200  | Alineación y balanceo de neumáticos             | $1000    |
| 1300  | Diagnóstico y reparación de fallas del motor    | $2500    |
| 1400  | Servicio de suspensión y dirección              | $1600    |

🧠 Esta tabla debe mantenerse en **memoria** como consideres conveniente.

🗃️ Guardar cada reparación en `reparaciones.txt` con el siguiente formato:

```
ID_EMPLEADO;ID_VEHICULO;ID_REPARACION;FECHA_HORA_REPARACION
```

---

### 📄 Paso 12: Ver reparaciones (`reparaciones.txt`)

Formato:

```
[REPARACION 27-06/2024 14:25]
Empleado: Nombre Apellido.
Propietario: Nombre Apellido.
Reparación: Mantenimiento y cambio de aceite.
Vehículo: [Marca], [Modelo], [Matrícula].
```

---

### 📊 Otros puntos

13️⃣ Calcular ingresos totales por tipo de reparación  
14️⃣ Buscar reparación más realizada  
15️⃣ Buscar vehículo por patente  
16️⃣ Filtrar vehículos por **color** (elección del usuario)  
17️⃣ Filtrar vehículos por **propietario** (elección del usuario)  
18️⃣ Ordenar por **fecha de reparación** (ascendente o descendente, a elección)

---

## ⚙️ Requisitos técnicos del proyecto

### 🧩 Funciones requeridas

- Implementar al menos **2 de las 3** funciones: `map`, `filter`, `reduce` ✨
- 🚫 **No se permite usar** `sort()` de Python
- ✅ Implementar un **algoritmo de ordenamiento propio**

---

### 🔐 Validación de datos

- Validar **todos los campos** ingresados por el usuario
- Usar **expresiones regulares** para validar formatos
- Controlar la **longitud máxima** de los caracteres para evitar desbordes

---

💡 **Tip final:** organizá tu código en módulos reutilizables y asegurate de probar todos los casos borde.

---

📂 Archivos utilizados:

- `vehiculos.json` 📄
- `empleados.csv` 📄
- `reparaciones.txt` 🧾

---

👨‍💻 ¡Mucho éxito programando este sistema! 🚀
