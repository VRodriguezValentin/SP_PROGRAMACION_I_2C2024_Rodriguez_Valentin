import PAQUETE.archivos as arch
import re

class Vehiculo:
    id_vehiculo = 1
    def __init__(self, marca, modelo, anio, color, patente, propietario) -> None:
        self.id = Vehiculo.id_vehiculo
        Vehiculo.id_vehiculo += 1
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.patente = patente
        self.propietario = propietario

    
    def listar_vehiculos(path: str) -> list:
        vehiculos_data = arch.leer_json(path)
        vehiculos = []
        for v in vehiculos_data:
            vehiculo_aux = Vehiculo(v['Marca'],v['Modelo'],v['Anio'],v['Color'],v['Patente'],v['Propietario'])
            vehiculo_aux.id = v['ID']
            vehiculos.append({'ID': vehiculo_aux.id, 'Marca': vehiculo_aux.marca, 'Modelo': vehiculo_aux.modelo, 'Anio': vehiculo_aux.anio, 'Color': vehiculo_aux.color, 'Patente': vehiculo_aux.patente, 'Propietario': vehiculo_aux.propietario})
        return vehiculos

    def validar_patente(patente) -> bool:
        patron = r'^[A-Z]{3}\d{3}$'
        if re.match(patron, patente):
            return True
        else:
            return False

    def alta_vehiculo(lista, marca, modelo, anio, color, patente, propietario_apellido_nombre) -> str:
        nuevo_vehiculo = Vehiculo(marca, modelo, anio, color, patente, propietario_apellido_nombre)
        lista.append({'ID': nuevo_vehiculo.id, 'Marca': nuevo_vehiculo.marca, 'Modelo': nuevo_vehiculo.modelo, 'Anio': nuevo_vehiculo.anio, 'Color': nuevo_vehiculo.color, 'Patente': nuevo_vehiculo.patente, 'Propietario': nuevo_vehiculo.propietario})
        return f'Alta de vehiculo exitosa!'
    
    def guardar_vehiculo_db(path, data) -> str:
        arch.escribir_json(path, data)
        return 'Archivo guardado con exito!'