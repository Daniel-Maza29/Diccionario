# Crear un diccionario vacío llamado "perro"
perro = {}

# Añadir nombre, color, raza, patas y edad al diccionario "perro"
perro['nombre'] = 'Perro'
perro['color'] = 'blanquito'
perro['raza'] = 'Labrador'
perro['patas'] = 4
perro['edad'] = 5

# Crear un diccionario de estudiante y añadir diferentes detalles
estudiante = {
    'nombre': 'Daniel',
    'apellido': 'Maza',
    'sexo': 'Masculino',
    'edad': 20,
    'estado civil': 'Soltero',
    'habilidades': ['Programación', 'Diseño gráfico'],
    'país': 'Venezuela',
    'ciudad': 'Ciudad de México',
    'dirección': 'Calle Principal 123'
}

# Obtener la longitud del diccionario "estudiante"
longitud = len(estudiante)

# Obtener el valor de las habilidades y comprobar el tipo de datos
habilidades = estudiante['habilidades']
tipo_habilidades = type(habilidades)

# Modificar los valores de las habilidades añadiendo una o dos habilidades
estudiante['habilidades'].extend(['Inglés', 'Marketing'])

# Obtener las claves del diccionario como una lista
claves = list(estudiante.keys())

# Obtener los valores del diccionario como una lista
valores = list(estudiante.values())

# Cambiar el diccionario a una lista de tuplas utilizando el método items()
lista_tuplas = list(estudiante.items())

# Eliminar uno de los elementos del diccionario
del estudiante['edad']

# Borrar uno de los diccionarios (en este caso, "perro")
del perro

# Imprimir los resultados
print("Diccionario perro eliminado")
print("Longitud del diccionario estudiante:", longitud)
print("Tipo de datos de las habilidades:", tipo_habilidades)
print("Estudiante con habilidades actualizadas:", estudiante)
print("Claves del diccionario:", claves)
print("Valores del diccionario:", valores)
print("Diccionario como lista de tuplas:", lista_tuplas)
