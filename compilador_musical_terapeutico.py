import re
import random
from mido import Message, MidiFile, MidiTrack

# Función para leer configuración desde el archivo
def leer_configuracion(filename='config.txt'):
    configuraciones = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                enfermedad, num_notas, duracion, velocidad, fib_limit = line.split(',')
                configuraciones[enfermedad] = {
                    'NOTAS': int(num_notas),
                    'DURACION': float(duracion),
                    'VELOCIDAD': int(velocidad),
                    'FIB_LIMIT': int(fib_limit)
                }
    return configuraciones

# Función para generar música basada en parámetros
def generar_musica(params, enfermedad, usar_fibonacci=False):
    num_notas = params['NOTAS']
    duracion = params['DURACION']
    velocidad = params['VELOCIDAD']
    fib_limit = params['FIB_LIMIT']

    # Crear un archivo MIDI
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Generar la melodía basada en Fibonacci si se selecciona
    if usar_fibonacci:
        fibonacci = [0, 1]
        for _ in range(2, fib_limit):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

        notas_musicales = [60, 62, 64, 65, 67, 69, 71, 72]  # C4 to C5

        for value in fibonacci[:num_notas]:
            nota = notas_musicales[value % len(notas_musicales)]
            track.append(Message('note_on', note=nota, velocity=velocidad, time=int(480 * duracion)))
            track.append(Message('note_off', note=nota, velocity=velocidad, time=int(480 * duracion)))
    else:
        # Generar notas aleatorias si no se selecciona Fibonacci
        notas_musicales = [60, 62, 64, 65, 67, 69, 71, 72]  # C4 to C5
        for _ in range(num_notas):
            nota = random.choice(notas_musicales)
            track.append(Message('note_on', note=nota, velocity=velocidad, time=int(480 * duracion)))
            track.append(Message('note_off', note=nota, velocity=velocidad, time=int(480 * duracion)))

    # Guardar el archivo MIDI con el nombre específico
    suffix = "con_fibonacci" if usar_fibonacci else "sin_fibonacci"
    filename = f'melodia_generada_{enfermedad}_{suffix}.mid'
    midi.save(filename)
    print(f"Archivo guardado como '{filename}'")

# Ejecutar el programa principal con manejo de excepciones
if __name__ == "__main__":
    try:
        # Leer configuraciones desde el archivo
        configuraciones = leer_configuracion()

        # Menú interactivo con manejo de excepciones
        while True:
            try:
                print("Seleccione una enfermedad:")
                for idx, enfermedad in enumerate(configuraciones.keys()):
                    print(f"{idx + 1}. {enfermedad}")

                seleccion = int(input("Ingrese el número de la enfermedad: ")) - 1
                if seleccion < 0 or seleccion >= len(configuraciones):
                    raise ValueError("Selección inválida. Por favor, ingrese un número válido.")
                enfermedad_seleccionada = list(configuraciones.keys())[seleccion]
                break
            except ValueError as e:
                print(f"Error: {e}. Inténtelo de nuevo.")

        # Menú para seleccionar el tipo de melodía
        while True:
            try:
                print("Seleccione el tipo de melodía:")
                print("1. Con Fibonacci")
                print("2. Sin Fibonacci")
                tipo_melodia = int(input("Ingrese el número de la opción: "))
                if tipo_melodia not in [1, 2]:
                    raise ValueError("Selección inválida. Por favor, ingrese 1 o 2.")
                usar_fibonacci = tipo_melodia == 1
                break
            except ValueError as e:
                print(f"Error: {e}. Inténtelo de nuevo.")

        # Generar la música basada en la selección
        generar_musica(configuraciones[enfermedad_seleccionada], enfermedad_seleccionada, usar_fibonacci)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        input("Presione Enter para salir...")
