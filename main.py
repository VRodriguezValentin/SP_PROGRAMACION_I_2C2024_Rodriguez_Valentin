import os
import PAQUETE.procesos as ps
import PAQUETE.menu as m
import PAQUETE.map_filter_reduce_sort as mfrs
import PAQUETE.vehiculos as v
import PAQUETE.empleado as e

def main():

    opciones = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
    opciones_menu = ['Ver Vehiculos', 'Ver Empleados', 'Alta Empleado', 'Baja Empleado', 'Modificacion Empleado', 'Guardar Empleado', 'Alta Vehiculo', 'Baja Vehiculo', 'Modificacion Vehiculo', 'Guardar Vehiculo']
    lista_vehiculos = v.Vehiculo.listar_vehiculos('vehiculos.json')
    lista_vehiculos_ordenada = []
    lista_empleados = e.Empleado.listar_empleados('empleados.csv')
    lista_empleados_ordenada = []

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
                                    for vehi in lista_vehiculos:
                                        print(f'ID: {vehi.id} Marca: {vehi.marca} Modelo: {vehi.modelo} Año: {vehi.anio} Color: {vehi.color} Patente: {vehi.patente} Propietario: {vehi.propietario}\n')
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                                    break
                                case '2':
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                                    lista_vehiculos_ordenada = ps.bubble_sort(lista_vehiculos, lambda x: x.marca)
                                    for vehi in lista_vehiculos_ordenada:
                                                print(f'ID: {vehi.id} Marca: {vehi.marca} Modelo: {vehi.modelo} Año: {vehi.anio} Color: {vehi.color} Patente: {vehi.patente} Propietario: {vehi.propietario}\n')
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
                                    for emp in lista_empleados:
                                        print(f'{emp}\n')
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                                    break
                                case '2':
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                                    lista_empleados_ordenada = ps.bubble_sort(lista_empleados, lambda y: y[1])
                                    for emp_ord in lista_empleados_ordenada:
                                        print(f'{emp_ord}\n')
                                    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n')
                                    break

                case '3':
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
                    os.system('cls')

                    telefono = input('Formato: [NN-NNNN-NNNN]\nIngrese un telefono: ')
                    telefono_valido = e.Empleado.validar_telefono(telefono)
                    if not telefono_valido:
                        os.system('cls')
                        print('¡ERROR! Telefono no valido\n')
                        break
                    
                    print(e.Empleado.alta_empleado(lista_empleados, apellido_nombre, salario, dni, telefono))

                case '4':
                    pass
                case '5':
                    pass
                case '6':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t\t   Guardar Empleado\n╚══════════════════════════════════════════════════╝\n')
                    if len(lista_empleados_ordenada) > 0:
                        print(e.Empleado.guardar_empleado_db('empleados.csv', lista_empleados_ordenada))
                    else:
                        print(e.Empleado.guardar_empleado_db('empleados.csv', lista_empleados))

                case '7':
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
                    if modelo != str or modelo != int or modelo != float:
                        print('¡ERROR! El modelo del vehiculo no es valido')
                        break
                    else:
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
                    os.system('cls')

                    patente = input('Formato: [XXXNNN]\nIngrese un patente: ')
                    patente_valido = e.Empleado.validar_patente(patente)
                    if not patente_valido:
                        os.system('cls')
                        print('¡ERROR! Patente no valida\n')
                        break

                    propietario_nombre = ps.get_str('Ingrese el nombre del empleado: ', '¡ERROR! El nombre del empleado no es valido', 30, 3)
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
                    
                    print(e.Empleado.alta_empleado(lista_vehiculos, marca, modelo, anio, color, patente, propietario_apellido_nombre))
                case '8':
                    pass
                case '9':
                    pass
                case '10':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t\t   Guardar Empleado\n╚══════════════════════════════════════════════════╝\n')
                    if len(lista_empleados_ordenada) > 0:
                        print(v.Vehiculo.guardar_vehiculo_db('vehiculos.json', lista_vehiculos_ordenada))
                    else:
                        print(v.Vehiculo.guardar_vehiculo_db('vehiculos.json', lista_vehiculos))
                case '11':
                    pass
                case '12':
                    pass
                case '13':
                    pass
                case '14':
                    pass
                case '15':
                    pass
                case '16':
                    pass
                case '17':
                    pass
                case '18':
                    pass
                case _:
                    print('¡ERROR! La opcion no es valida')
        
        input('Presione ENTER para continuar...')
        os.system('cls')

main()