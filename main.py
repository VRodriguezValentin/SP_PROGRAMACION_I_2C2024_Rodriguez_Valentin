import os
import PAQUETE.procesos as ps
import PAQUETE.menu as m
import PAQUETE.map_filter_reduce_sort as mfrs
import PAQUETE.vehiculos as v
import PAQUETE.empleado as e
from datetime import datetime
from PAQUETE.archivos import escribir_txt

def main():

    opciones = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
    opciones_menu = ['Ver Vehiculos', 'Ver Empleados', 'Alta Empleado', 'Baja Empleado', 'Modificacion Empleado', 'Guardar Empleado', 'Alta Vehiculo', 'Baja Vehiculo', 'Modificacion Vehiculo', 'Guardar Vehiculo','Reparar Vehiculo', 'Ver Reparaciones', 'Filtrar Vehiculos por Color (16)']
    lista_vehiculos = v.Vehiculo.listar_vehiculos('vehiculos.json')
    lista_empleados = e.Empleado.listar_empleados('empleados.csv')
    tipos_reparacion = [{'ID': 1000,    'Descripcion': 'Mantenimiento y cambio de aceite',              'Coste': 5500},
                        {'ID': 1100,    'Descripcion': 'Reparación de frenos',                          'Coste': 1500},
                        {'ID': 1200,    'Descripcion': 'Alineación y balanceo de neumáticos',           'Coste': 1000},
                        {'ID': 1300,    'Descripcion': 'Diagnóstico y reparación de fallas del motor',  'Coste': 2500},
                        {'ID': 1400,    'Descripcion': 'Servicio de suspensión y dirección',            'Coste': 1600}]
    
    while True:

        opcion = m.menu('MAIN MENU',opciones_menu)
        opcion = ps.validacion_lista(opcion, opciones, 'opcion')
        os.system('cls')

        if opcion == '0':
            print('¡Hasta luego!')
            break
        else:
            match opcion:
                case '1':
                    while True:
                        opciones_vehiculo = ['0','1','2']
                        opciones_vehiculo_desc = ['Sin ordenar', 'Ordenados por Marca']

                        opcion_vehiculo = m.menu('Ver Vehiculos',opciones_vehiculo_desc,'Cancelar')
                        opcion_vehiculo = ps.validacion_lista(opcion_vehiculo, opciones_vehiculo, 'opcion')
                        os.system('cls')
                        if opcion_vehiculo == '0':
                            break
                        else:
                            match opcion_vehiculo:
                                case '1':
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                                    lista_vehiculos = ps.bubble_sort(lista_vehiculos, lambda x: x['ID'])
                                    for vehi in lista_vehiculos:
                                        print(f'ID: {vehi['ID']} Marca: {vehi['Marca']} Modelo: {vehi['Modelo']} Año: {vehi['Anio']} Color: {vehi['Color']} Patente: {vehi['Patente']} Propietario: {vehi['Propietario']}\n')
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                                    break
                                case '2':
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                                    lista_vehiculos = ps.bubble_sort(lista_vehiculos, lambda x: x['Marca'])
                                    for vehi in lista_vehiculos:
                                        print(f'ID: {vehi['ID']} Marca: {vehi['Marca']} Modelo: {vehi['Modelo']} Año: {vehi['Anio']} Color: {vehi['Color']} Patente: {vehi['Patente']} Propietario: {vehi['Propietario']}\n')
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                                    break
                                case _:
                                    print('¡ERROR! La opcion no es valida')
                                    break

                case '2':
                    while True:
                        opciones_empleado = ['0','1','2']
                        opciones_empleado_desc = ['Sin ordenar', 'Ordenados por Apellido y Nombre']

                        opcion_empleado = m.menu('Ver empleados',opciones_empleado_desc,'Cancelar')
                        opcion_empleado = ps.validacion_lista(opcion_empleado, opciones_empleado, 'opcion')
                        os.system('cls')
                        if opcion_empleado == '0':
                            break
                        else:
                            match opcion_empleado:
                                case '1':
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                                    lista_empleados = ps.bubble_sort(lista_empleados, lambda y: int(y[0]))
                                    for emp in lista_empleados:
                                        print(f'{emp}\n')
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                                    break
                                case '2':
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                                    lista_empleados = ps.bubble_sort(lista_empleados, lambda y: y[1])
                                    for emp in lista_empleados:
                                        print(f'{emp}\n')
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                                    break

                case '3':
                    while True:
                        os.system('cls')
                        print('╔══════════════════════════════════════════════════╗\n\t\t   Alta Empleado\n╚══════════════════════════════════════════════════╝\n')
                        nombre = ps.get_str('Ingrese el nombre del empleado: ', '¡ERROR! El nombre del empleado no es valido', 30, 3)
                        if nombre is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        nombre = nombre.capitalize()
                        os.system('cls')

                        apellido = ps.get_str('Ingrese el apellido del empleado: ', '¡ERROR! El apellido del empleado no es valido', 30, 3)
                        if apellido is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        apellido = apellido.capitalize()
                        os.system('cls')

                        apellido_nombre = apellido + ' ' + nombre

                        salario = ps.get_float('Ingrese el salario: ','¡ERROR! El valor del salario no es valido', 0, reintentos=3)
                        if salario is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        os.system('cls')

                        dni = ps.get_int('Ingrese el DNI: ','¡ERROR! El DNI no es valido', 10000000, 99999999, 3)
                        if dni is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        else:
                            dni_existente = False
                            for emp in lista_empleados:
                                if dni == int(emp[3]):
                                    dni_existente = True
                                    break
                            if dni_existente:
                                print('¡ERROR! El DNI ya se encuentra registrado\n')
                                break

                        telefono = input('Formato: [NN-NNNN-NNNN]\nIngrese un telefono: ')
                        telefono_valido = e.Empleado.validar_telefono(telefono)
                        if not telefono_valido:
                            os.system('cls')
                            print('¡ERROR! Telefono no valido\n')
                            break
                        telefono_existente = False
                        for emp in lista_empleados:
                            if telefono == emp[4]:
                                telefono_existente = True
                                break
                        if telefono_existente == True:
                            print('¡ERROR! El telefono ya se encuentra registrado\n')
                            break
                        print(e.Empleado.alta_empleado(lista_empleados, apellido_nombre, salario, dni, telefono))
                        break

                case '4':
                    while True:
                        os.system('cls')
                        print('╔══════════════════════════════════════════════════╗\n\t\t   Baja Empleado\n╚══════════════════════════════════════════════════╝\n')
                        dni_aux = ps.get_int('Ingrese un DNI: ','¡ERROR! El DNI no es valido', 10000000, 99999999, 3)
                        if dni_aux is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        else:
                            dni_existente = False
                            for emp in lista_empleados:
                                if dni_aux == int(emp[3]):
                                    dni_existente = True
                                    break
                            if dni_existente:
                                print(e.Empleado.baja_empleado(lista_empleados, dni_aux))
                                break
                            else:
                                print('¡ERROR! El empleado no se encuentra registrado\n')
                                break

                case '5':
                    print('╔══════════════════════════════════════════════════╗\n\t      Modificacion Empleado\n╚══════════════════════════════════════════════════╝\n')
                    cambiar_apellido_nombre = False
                    cambiar_salario = False
                    cambiar_telefono = False

                    dni_aux = ps.get_int('Ingrese un DNI: ','¡ERROR! El DNI no es valido', 10000000, 99999999, 3)
                    if dni_aux is None:
                        os.system('cls')
                        print('¡ERROR! Se acabaron los intentos\n')
                    else:
                        dni_existente = False
                        for emp in lista_empleados:
                            if dni_aux == int(emp[3]):
                                dni_existente = True
                                break
                        if not dni_existente:
                            print('¡ERROR! El empleado no se encuentra registrado\n')
                            break
                        else:
                            while True:
                                os.system('cls')
                                opciones_emp_modif = ['0','1','2','3','4']
                                opciones_emp_modif_desc = ['Modificar Apellido y Nombre','Modificar Salario', 'Modificar Telefono', 'Guardar Cambios']

                                opcion_emp_modif = m.menu('Modificar empleado',opciones_emp_modif_desc,'Cancelar')
                                opcion_emp_modif = ps.validacion_lista(opcion_emp_modif, opciones_emp_modif, 'opcion')
                                os.system('cls')
                                if opcion_emp_modif == '0':
                                    break
                                else:
                                    match opcion_emp_modif:
                                        case '1':
                                            nombre = ps.get_str('Ingrese el nombre del empleado: ', '¡ERROR! El nombre del empleado no es valido', 30, 3)
                                            if nombre is None:
                                                os.system('cls')
                                                print('¡ERROR! Se acabaron los intentos\n')
                                            else:
                                                nombre = nombre.capitalize()
                                                os.system('cls')

                                                apellido = ps.get_str('Ingrese el apellido del empleado: ', '¡ERROR! El apellido del empleado no es valido', 30, 3)
                                                if apellido is None:
                                                    os.system('cls')
                                                    print('¡ERROR! Se acabaron los intentos\n')
                                                else:
                                                    apellido = apellido.capitalize()
                                                    os.system('cls')

                                                    apellido_nombre = apellido + ' ' + nombre

                                                    cambiar_apellido_nombre = True
                                                    print(f'Nuevo Apellido: ({apellido}) | Nuevo Nombre: ({nombre})')

                                        case '2':
                                            salario = ps.get_float('Ingrese el salario: ','¡ERROR! El valor del salario no es valido', 0, reintentos=3)
                                            if salario is None:
                                                os.system('cls')
                                                print('¡ERROR! Se acabaron los intentos\n')
                                            else:
                                                cambiar_salario = True
                                                print(f'Nuevo salario: ${salario}')

                                        case '3':
                                            telefono = input('Formato: [NN-NNNN-NNNN]\nIngrese un telefono: ')
                                            telefono_valido = e.Empleado.validar_telefono(telefono)
                                            if not telefono_valido:
                                                os.system('cls')
                                                print('¡ERROR! Telefono no valido\n')
                                            else:
                                                telefono_existente = False
                                                for emp in lista_empleados:
                                                    if telefono == emp[4]:
                                                        telefono_existente = True
                                                        break
                                                if telefono_existente:
                                                    print('¡ERROR! El telefono ya se encuentra registrado\n')
                                                else:
                                                    cambiar_telefono = True
                                                    print(f'Nuevo telefono: {telefono}')

                                        case '4':
                                            if not cambiar_apellido_nombre:
                                                apellido_nombre = None

                                            if not cambiar_salario:
                                                salario = None

                                            if not cambiar_telefono:
                                                telefono = None

                                            print(f'{e.Empleado.modificacion_empleado(lista_empleados, dni_aux, apellido_nombre, salario, telefono)}\n')
                                            break

                                input('Presione ENTER para continuar...')
                                os.system('cls')

                case '6':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t\t   Guardar Empleado\n╚══════════════════════════════════════════════════╝\n')
                    print(f'{e.Empleado.guardar_empleado_db('empleados.csv', lista_empleados)}\n')

                case '7':
                    while True:
                        os.system('cls')
                        print('╔══════════════════════════════════════════════════╗\n\t\t   Alta Vehiculo\n╚══════════════════════════════════════════════════╝\n')
                        marca = ps.get_str('Ingrese la marca del vehiculo: ', '¡ERROR! La marca del vehiculo no es valida', 30, 3)
                        if marca is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        marca = marca.capitalize()
                        os.system('cls')

                        modelo = input('Ingrese el modelo del vehiculo: ')
                        if not modelo.isdigit():
                            modelo = modelo.capitalize()
                        os.system('cls')

                        anio = ps.get_int('Ingrese el año: ','¡ERROR! El año no es valido', 1886, 2024, 3)
                        if anio is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        os.system('cls')

                        color = ps.get_str('Ingrese el color: ','¡ERROR! El color no es valido', 10, 3)
                        if color is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        color = color.capitalize()
                        os.system('cls')

                        patente = input('Formato: [XXXNNN]\nIngrese un patente: ')
                        patente_valido = v.Vehiculo.validar_patente(patente)
                        if not patente_valido:
                            os.system('cls')
                            print('¡ERROR! Patente no valida\n')
                            break
                        patente_existente = False
                        for vehi in lista_vehiculos:
                            if patente == vehi['Patente']:
                                patente_existente = True
                                break
                        if patente_existente == True:
                            print('¡ERROR! La patente ya se encuentra registrada\n')
                            break

                        propietario_nombre = ps.get_str('Ingrese el nombre del propietario: ', '¡ERROR! El nombre del propietario no es valido', 30, 3)
                        if propietario_nombre is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        propietario_nombre = propietario_nombre.capitalize()
                        os.system('cls')

                        propietario_apellido = ps.get_str('Ingrese el apellido del empleado: ', '¡ERROR! El apellido del empleado no es valido', 30, 3)
                        if propietario_apellido is None:
                            os.system('cls')
                            print('¡ERROR! Se acabaron los intentos\n')
                            break
                        propietario_apellido = propietario_apellido.capitalize()
                        os.system('cls')

                        propietario_apellido_nombre = propietario_apellido + ' ' + propietario_nombre

                        print(v.Vehiculo.alta_vehiculo(lista_vehiculos, marca, modelo, anio, color, patente, propietario_apellido_nombre))
                        break

                case '8':
                    while True:
                        os.system('cls')
                        print('╔══════════════════════════════════════════════════╗\n\t\t   Baja Vehiculo\n╚══════════════════════════════════════════════════╝\n')
                        patente_aux = input('Formato: [XXXNNN]\nIngrese un patente: ')
                        patente_valido = v.Vehiculo.validar_patente(patente_aux)
                        if not patente_valido:
                            os.system('cls')
                            print('¡ERROR! Patente no valida\n')
                            break
                        else:
                            patente_existente = False
                            for vehi in lista_vehiculos:
                                if patente_aux == vehi['Patente']:
                                    patente_existente = True
                                    break
                            if patente_existente:
                                print(v.Vehiculo.baja_vehiculo(lista_vehiculos, patente_aux))
                                break
                            else:
                                print('¡ERROR! El vehiculo no se encuentra registrado\n')
                                break
                case '9':
                    print('╔══════════════════════════════════════════════════╗\n\t      Modificacion Vehiculo\n╚══════════════════════════════════════════════════╝\n')
                    cambiar_marca   = False
                    cambiar_modelo  = False
                    cambiar_anio    = False
                    cambiar_color   = False
                    cambiar_propietario_apellido_nombre = False

                    patente_aux = input('Formato: [XXXNNN]\nIngrese un patente: ')
                    patente_valido = v.Vehiculo.validar_patente(patente_aux)
                    if not patente_valido:
                        os.system('cls')
                        print('¡ERROR! Patente no valida\n')
                    else:
                        patente_existente = False
                        for vehi in lista_vehiculos:
                            if patente_aux == vehi['Patente']:
                                patente_existente = True
                                break
                        if not patente_existente:
                            print('¡ERROR! El vehiculo no se encuentra registrado\n')
                        else:
                            while True:
                                os.system('cls')
                                opciones_vehi_modif = ['0','1','2','3','4','5','6']
                                opciones_vehi_modif_desc = ['Modificar Marca', 'Modificar Modelo', 'Modificar Año', 'Modificar Color', 'Modificar Propietario', 'Guardar Cambios']

                                opcion_vehi_modif = m.menu('Modificar Vehiculo',opciones_vehi_modif_desc,'Cancelar')
                                opcion_vehi_modif = ps.validacion_lista(opcion_vehi_modif, opciones_vehi_modif, 'opcion')
                                os.system('cls')
                                if opcion_vehi_modif == '0':
                                    break
                                else:
                                    match opcion_vehi_modif:
                                        case '1':
                                            marca = ps.get_str('Ingrese la marca del vehiculo: ', '¡ERROR! La marca del vehiculo no es valida', 30, 3)
                                            if marca is None:
                                                os.system('cls')
                                                print('¡ERROR! Se acabaron los intentos\n')
                                            else:
                                                marca = marca.capitalize()
                                                cambiar_marca = True
                                                print(f'Nueva marca: ({marca})\n')
                                        case '2':
                                            modelo = ps.get_str('Ingrese la modelo del vehiculo: ', '¡ERROR! La modelo del vehiculo no es valida', 30, 3)
                                            if modelo is None:
                                                os.system('cls')
                                                print('¡ERROR! Se acabaron los intentos\n')
                                            else:
                                                modelo = modelo.capitalize()
                                                cambiar_modelo = True
                                                print(f'Nuevo modelo: ({modelo})\n')
                                        case '3':
                                            anio = ps.get_int('Ingrese el año: ','¡ERROR! El año no es valido', 1886, 2024, 3)
                                            if anio is None:
                                                os.system('cls')
                                                print('¡ERROR! Se acabaron los intentos\n')
                                            else:
                                                cambiar_anio = True
                                                print(f'Nuevo anio: ({anio})\n')
                                        case '4':
                                            color = ps.get_str('Ingrese la color del vehiculo: ', '¡ERROR! La color del vehiculo no es valida', 30, 3)
                                            if color is None:
                                                os.system('cls')
                                                print('¡ERROR! Se acabaron los intentos\n')
                                            else:
                                                color = color.capitalize()
                                                cambiar_color = True
                                                print(f'Nuevo color: ({color})\n')
                                        
                                        case '5':
                                            propietario_nombre = ps.get_str('Ingrese el nombre del empleado: ', '¡ERROR! El nombre del empleado no es valido', 30, 3)
                                            if propietario_nombre is None:
                                                os.system('cls')
                                                print('¡ERROR! Se acabaron los intentos\n')
                                            else:
                                                propietario_nombre = propietario_nombre.capitalize()
                                                os.system('cls')

                                                propietario_apellido = ps.get_str('Ingrese el apellido del empleado: ', '¡ERROR! El apellido del empleado no es valido', 30, 3)
                                                if propietario_apellido is None:
                                                    os.system('cls')
                                                    print('¡ERROR! Se acabaron los intentos\n')
                                                else:
                                                    propietario_apellido = propietario_apellido.capitalize()
                                                    os.system('cls')

                                                    propietario_apellido_nombre = propietario_apellido + ' ' + propietario_nombre
                                                    cambiar_propietario_apellido_nombre = True
                                                    print(f'Nuevo propietario: ({propietario_apellido_nombre})\n')

                                        case '6':
                                            if not cambiar_marca:
                                                marca = None

                                            if not cambiar_modelo:
                                                modelo = None

                                            if not cambiar_anio:
                                                anio = None

                                            if not cambiar_color:
                                                color = None

                                            if not cambiar_propietario_apellido_nombre:
                                                propietario_apellido_nombre = None

                                            print(f'{v.Vehiculo.modificacion_vehiculo(lista_vehiculos, patente_aux, marca, modelo, anio, color, propietario_apellido_nombre)}\n')
                                            break

                                    input('Presione ENTER para continuar...')
                                    os.system('cls')
                case '10':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t\t   Guardar Empleado\n╚══════════════════════════════════════════════════╝\n')
                    print(f'{v.Vehiculo.guardar_vehiculo_db('vehiculos.json', lista_vehiculos)}\n')

                case '11':
                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                    print('▬                                        Selecciona un empleado                                                ▬')
                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                    for emp in lista_empleados:
                        print(f'{emp}\n')
                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                    id_empleado = ps.get_int('Ingrese un ID: ','¡ERROR! El ID no es valido', 1, reintentos=3)
                    if id_empleado is None:
                        os.system('cls')
                        print('¡ERROR! Se acabaron los intentos\n')
                    else:
                        id_existente = False
                        for emp in lista_empleados:
                            if int(id_empleado) == int(emp[0]):
                                id_existente = True
                                break
                        if not id_existente:
                            print('¡ERROR! El empleado no se encuentra registrado\n')
                        else:
                            os.system('cls')
                            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                            print('▬                                        Selecciona un vehiculo                                                ▬')
                            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                            for vehi in lista_vehiculos:
                                print(f'ID: {vehi['ID']} Marca: {vehi['Marca']} Modelo: {vehi['Modelo']} Año: {vehi['Anio']} Color: {vehi['Color']} Patente: {vehi['Patente']} Propietario: {vehi['Propietario']}\n')
                            print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                            id_vehiculo = ps.get_int('Ingrese un ID: ','¡ERROR! El ID no es valido', 1, reintentos=3)
                            if id_vehiculo is None:
                                os.system('cls')
                                print('¡ERROR! Se acabaron los intentos\n')
                            else:
                                id_existente = False
                                for vehi in lista_vehiculos:
                                    if int(id_vehiculo) == int(vehi['ID']):
                                        id_existente = True
                                        break
                                if not id_existente:
                                    print('¡ERROR! El vehiculo no se encuentra registrado\n')
                                else:
                                    os.system('cls')
                                    opciones_repa = ['0','1','2','3','4','5']
                                    opciones_repa_desc = ['Mantenimiento y cambio de aceite','Reparación de frenos', 'Alineación y balanceo de neumáticos', 'Diagnóstico y reparación de fallas del motor', 'Servicio de suspensión y dirección']

                                    opcion_repa = m.menu('Taller de Reparacion',opciones_repa_desc,'Cancelar')
                                    opcion_repa = ps.validacion_lista(opcion_repa, opciones_repa, 'opcion')
                                    os.system('cls')
                                    if opcion_repa == '0':
                                        pass
                                    else:
                                        match opcion_repa:
                                            case '1':
                                                tipo = 'Mantenimiento y cambio de aceite'
                                                for repa in tipos_reparacion:
                                                    if tipo == repa['Descripcion']:
                                                        id_reparacion = repa['ID']
                                                        break

                                            case '2':
                                                tipo = 'Reparación de frenos'
                                                for repa in tipos_reparacion:
                                                    if tipo == repa['Descripcion']:
                                                        id_reparacion = repa['ID']
                                                        break

                                            case '3':
                                                tipo = 'Alineación y balanceo de neumáticos'
                                                for repa in tipos_reparacion:
                                                    if tipo == repa['Descripcion']:
                                                        id_reparacion = repa['ID']
                                                        break

                                            case '4':
                                                tipo = 'Diagnóstico y reparación de fallas del motor'
                                                for repa in tipos_reparacion:
                                                    if tipo == repa['Descripcion']:
                                                        id_reparacion = repa['ID']
                                                        break

                                            case '5':
                                                tipo = 'Servicio de suspensión y dirección'
                                                for repa in tipos_reparacion:
                                                    if tipo == repa['Descripcion']:
                                                        id_reparacion = repa['ID']
                                                        break
                                        
                                        fecha_hora_reparacion = datetime.now().strftime('%d-%m-%Y %H:%M')

                                        mensaje = str(id_empleado) + ';' + str(id_vehiculo) + ';' + str(id_reparacion) + ';' + str(fecha_hora_reparacion)
                                        escribir_txt('reparaciones.txt',mensaje,'a')
                                        print('Reparacion registrada con exito!\n')

                case '12': 
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t\t   Ver Reparaciones\n╚══════════════════════════════════════════════════╝\n')
                    lista_reparaciones_realizadas = v.Vehiculo.leer_reparaciones('reparaciones.txt')

                    for reparacion in lista_reparaciones_realizadas:
                        id_empleado = reparacion['ID_EMPLEADO']
                        id_vehiculo = reparacion['ID_VEHICULO']
                        id_reparacion = reparacion['ID_REPARACION']
                        fecha_hora = reparacion['FECHA_HORA_REPARACION']

                        id_existente = False
                        for emp in lista_empleados:
                            if int(id_empleado) == int(emp[0]):
                                id_existente = True
                                empleado_apellido_nombre = emp[1]
                                break

                        if not id_existente:
                            print('¡ERROR! El empleado no se encuentra registrado\n')
                        else:

                            id_existente = False
                            for vehi in lista_vehiculos:
                                if int(id_vehiculo) == int(vehi['ID']):
                                    id_existente = True
                                    propietario_apellido_nombre = vehi['Propietario']
                                    marca_vehiculo = vehi['Marca']
                                    modelo_vehiculo = vehi['Modelo']
                                    patente_vehiculo = vehi['Patente']
                                    break

                            if not id_existente:
                                print('¡ERROR! El vehiculo no se encuentra registrado\n')
                            else:

                                id_existente = False
                                for repa in tipos_reparacion:
                                    if int(id_reparacion) == int(repa['ID']):
                                        id_existente = True
                                        reparacion_desc = repa['Descripcion']
                                        break

                                if not id_existente:
                                    print('¡ERROR! El empleado no se encuentra registrado\n')
                                else:

                                    print(f'\n[REPARACION {fecha_hora}]')
                                    print(f'Empleado: {empleado_apellido_nombre}')
                                    print(f'Propietario: {propietario_apellido_nombre}')
                                    print(f'Reparación: {reparacion_desc}')
                                    print(f'Vehículo: {marca_vehiculo}, {modelo_vehiculo}, {patente_vehiculo}\n')
                case '13':
                    pass
                case '14':
                    pass
                case '15':
                    pass
                case '16':
                    opciones_filtro_color = ['0','1','2','3','4','5','6','7','8','9','10','11']
                    opciones_filtro_color_desc = ['Negro', 'Blanco', 'Gris', 'Plateado', 'Rojo', 'Naranja', 'Amarillo', 'Violeta', 'Rosa', 'Azul', 'Verde']

                    opcion_filtro_color = m.menu('Filtro por Color',opciones_filtro_color_desc,'Cancelar')
                    opcion_filtro_color = ps.validacion_lista(opcion_filtro_color, opciones_filtro_color, 'opcion')
                    os.system('cls')
                    if opcion_filtro_color == '0':
                        pass
                    else:
                        match opcion_filtro_color:
                            case '1':
                                color_buscado = 'Negro'
                            case '2':
                                color_buscado = 'Blanco'
                            case '3':
                                color_buscado = 'Gris'
                            case '4':
                                color_buscado = 'Plateado'
                            case '5':
                                color_buscado = 'Rojo'
                            case '6':
                                color_buscado = 'Naranja'
                            case '7':
                                color_buscado = 'Amarillo'
                            case '8':
                                color_buscado = 'Violeta'
                            case '9':
                                color_buscado = 'Rosa'
                            case '10':
                                color_buscado = 'Azul'
                            case '11':
                                color_buscado = 'Verde'
                            
                        lista_colores = []
                        for vehi in lista_vehiculos:
                            color_aux = vehi['Color']
                            id_aux = vehi['ID']
                            lista_colores.append((id_aux, color_aux))

                        vehiculos_filtro_color = mfrs.my_filter(lambda x: x[1] == color_buscado, lista_colores)
                        for vehi in lista_vehiculos:
                            for v_filtro in vehiculos_filtro_color:
                                if vehi['ID'] == v_filtro[0]:
                                    print(f'ID: {vehi['ID']} Marca: {vehi['Marca']} Modelo: {vehi['Modelo']} Año: {vehi['Anio']} Color: {vehi['Color']} Patente: {vehi['Patente']} Propietario: {vehi['Propietario']}\n')
                case '17':
                    pass
                case '18':
                    pass
                case _:
                    print('¡ERROR! La opcion no es valida')
        
        input('Presione ENTER para continuar...')
        os.system('cls')

main()