import PAQUETE.archivos as arch
import re
import PAQUETE.map_filter_reduce_sort as mfrs

class Empleado:
    id_empleado = 1
    def __init__(self, apellido_nombre, salario, dni, telefono) -> None:
        self.id = Empleado.id_empleado
        Empleado.id_empleado += 1
        self.apellido_nombre = apellido_nombre
        self.salario = salario
        self.dni = dni
        self.telefono = telefono


    def id_mas_alto(lista_empleados):
        lista_ids = []
        for emp in lista_empleados:
            lista_ids.append(emp[0])
        id_max = mfrs.my_reduce(lambda a, b: a if int(a) > int(b) else b ,lista_ids)
        Empleado.id_empleado = int(id_max) + 1

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
        Empleado.id_mas_alto(lista)
        nuevo_empleado = Empleado(apellido_nombre, salario, dni, telefono)
        lista.append([nuevo_empleado.id, nuevo_empleado.apellido_nombre, nuevo_empleado.salario, nuevo_empleado.dni, nuevo_empleado.telefono])
        return 'Alta de empleado exitosa!'
    
    def guardar_empleado_db(path, data) -> str:
        arch.escribir_csv_mas(path, data)
        return 'Archivo guardado con exito!'
    
    def baja_empleado(lista, dni) -> str:
        for e in lista:
            if dni == int(e[3]):
                lista.remove(e)
                return f'Empleado {e[1]} dado de baja con exito!'
        return '¡ERROR! No se pudo dar de baja el empleado'
    
    def modificacion_empleado(lista, dni, apellido_nombre = None, salario = None, telefono = None ):
        contador_cambios = 0

        if apellido_nombre != None:
            for emp in lista:
                if int(dni) == int(emp[3]):
                    emp[1] = apellido_nombre
                    contador_cambios += 1
                    break
        
        if salario != None:
            for emp in lista:
                if int(dni) == int(emp[3]):
                    emp[2] = salario
                    contador_cambios += 1
                    break

        if telefono != None:
            for emp in lista:
                if int(dni) == int(emp[3]):
                    emp[4] = telefono
                    contador_cambios += 1
                    break
        
        if contador_cambios > 0:
            return 'Empleado modificado con exito!'
        else:
            return 'No se realizaron modificaciones.'

