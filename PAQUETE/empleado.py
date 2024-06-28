import PAQUETE.archivos as arch
import re

class Empleado:
    id_empleado = 11
    def __init__(self, apellido_nombre, salario, dni, telefono) -> None:
        self.id = Empleado.id_empleado
        Empleado.id_empleado += 1
        self.apellido_nombre = apellido_nombre
        self.salario = salario
        self.dni = dni
        self.telefono = telefono

    
    def listar_empleados(path) -> list:
        lista_empleados = []
        leer = arch.leer_csv(path)
        for linea in leer:
            lista_empleados.append(linea)
        return lista_empleados
    
    def validar_telefono(telefono) -> bool:
        patron = r'^\d{2}-\d{4}-\d{4}$'
        if re.match(patron, telefono):
            return True
        else:
            return False

    def alta_empleado(lista, apellido_nombre, salario, dni, telefono) -> str:
        nuevo_empleado = Empleado(apellido_nombre, salario, dni, telefono)
        lista.append([nuevo_empleado.id, nuevo_empleado.apellido_nombre, nuevo_empleado.salario, nuevo_empleado.dni, nuevo_empleado.telefono])
        return f'Alta de empleado exitosa!'
    
    def guardar_empleado_db(path, data) -> str:
        arch.escribir_csv_mas(path, data)
        return 'Archivo guardado con exito!'
