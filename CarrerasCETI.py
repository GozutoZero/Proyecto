import json

def cargar_datos_desde_json(archivo):
    try:
        with open(archivo, 'r') as file:
            datos = json.load(file)
        return datos
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al cargar {archivo}: {e}")
        return []

def guardar_datos_en_json(archivo, datos):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=2)

def cargar_preguntas():
    return cargar_datos_desde_json('preguntas.json')

def cargar_respuestas_carreras():
    return cargar_datos_desde_json('respuestas_carreras.json')

def guardar_respuestas_carrera(respuestas_carreras):
    guardar_datos_en_json('respuestas_carreras.json', respuestas_carreras)

def mostrar_lista_carreras(datos_carreras):
    if not datos_carreras:
        print("No hay información de carreras disponible.")
        return

    print("Lista de Carreras:")
    for carrera in datos_carreras:
        nombre = carrera.get('nombre', 'Nombre no disponible')
        requisitos = carrera.get('requisitos', 'Requisitos no disponibles')
        print(f"{nombre} - Requisitos: {requisitos}")

def realizar_entrevista(preguntas):
    respuestas_usuario = {}

    print("¡Bienvenido a la entrevista!")
    for i, pregunta in enumerate(preguntas, start=1):
        respuesta = input(f"{pregunta['pregunta']}: (si,no)").lower()
        respuestas_usuario[f"P{i}"] = respuesta

    return respuestas_usuario

def encontrar_carreras_coincidentes(respuestas_usuario, datos_carreras):
    carreras_coincidentes = []

    for carrera in datos_carreras:
        print("Respuestas del usuario:", respuestas_usuario)
        print("Respuestas almacenadas en el archivo JSON:", carrera["respuestas"])

        coincidencias = all(
            respuestas_usuario.get(pregunta, '').lower() == carrera["respuestas"].get(pregunta, '').lower()
            for pregunta in respuestas_usuario
        )
        if coincidencias:
            carreras_coincidentes.append(carrera["nombre"])

    return carreras_coincidentes

# Cargar datos desde archivos JSON
preguntas = cargar_preguntas()
datos_carreras = cargar_respuestas_carreras()

# Interfaz inicial
while True:
    print("\n=== Asesor de Elección de Carrera ===")
    print("1. Ver carreras")
    print("2. Descubre tu carrera")
    print("3. Salir")

    opcion = input("Selecciona una opción (1, 2 o 3): ")

    if opcion == '1':
        mostrar_lista_carreras(datos_carreras)
    elif opcion == '2':
        respuestas_usuario = realizar_entrevista(preguntas)
        carreras_coincidentes = encontrar_carreras_coincidentes(respuestas_usuario, datos_carreras)

        if carreras_coincidentes:
            print("Carreras coincidentes:")
            for carrera in carreras_coincidentes:
                print(carrera)
        else:
            print("No se encontraron coincidencias.")
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")

# Guardar datos actualizados
guardar_respuestas_carrera(datos_carreras)
