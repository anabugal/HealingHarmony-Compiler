# HealingHarmony-Compiler

Manual del Usuario para el Uso del Compilador Musical
Introducción
El Compilador Musical está diseñado para generar melodías MIDI específicas basadas en enfermedades y patrones matemáticos como la secuencia de Fibonacci. Este manual te guiará paso a paso sobre cómo utilizar el ejecutable del compilador.

Nota: se entiende como un desarrollo evolutivo al que se le agregarán futuras funciones.

Requisitos Previos
Sistema Operativo: Windows.
Dependencias: El ejecutable se ha creado para que no necesites instalar Python ni paquetes adicionales.
Paso a Paso para Utilizar el Ejecutable
Paso 1: Descargar el Ejecutable
Ubica el Ejecutable: Asegúrate de tener el archivo generador_musica.exe en tu computadora. Puedes descargarlo o copiarlo desde la ubicación proporcionada.
Paso 2: Configuración Inicial
Crear el Archivo de Configuración:
Crea un archivo llamado config.txt en la misma carpeta donde se encuentra el ejecutable.
Añade las configuraciones específicas para las enfermedades en el siguiente formato:
plaintext
Copiar código
# Enfermedad, Número de notas, Duración de cada nota, Velocidad, Límite de Fibonacci
Diabetes,10,0.5,100,10
Artritis,15,0.25,80,15
Estrés,12,0.4,90,12
Depresión,20,0.6,70,20
Paso 3: Ejecutar el Ejecutable
Ejecutar el Programa:
Navega a la carpeta donde se encuentra generador_musica.exe.
Haz doble clic en generador_musica.exe para ejecutarlo. Alternativamente, puedes abrir una terminal (CMD) en esa carpeta y ejecutar:
generador_musical_terapeuticoá
Paso 4: Interacción con el Compilador
Selección de Enfermedad:

Al ejecutar el compilador, se ver un menú que lista las enfermedades configuradas.
Ingresa el número correspondiente a la enfermedad para seleccionar los parámetros específicos.
Selección del Tipo de Melodía:

Se pedirá que selecciones si deseas generar la melodía utilizando la serie de Fibonacci o sin ella.
Ingresa 1 para "Con Fibonacci" o 2 para "Sin Fibonacci".
Generación y Almacenamiento de la Melodía:

El compilador generará la melodía basada en los parámetros seleccionados y guardará el archivo MIDI con un nombre específico, por ejemplo, melodia_generada_Estres_con_fibonacci.mid.
Verifica en la misma carpeta donde se encuentra el ejecutable para encontrar el archivo MIDI generado.
Paso 5: Manejo de Errores
Manejo de Excepciones:

Si ingresa un valor no válido, el compilador  mostrará un mensaje de error y  pedirá que se ingrese nuevamente la información correcta.
Errores Comunes:

Si el ejecutable se cierra de inmediato, asegúrate de ejecutar el archivo desde la terminal para ver cualquier mensaje de error.
Asegúrate de que el archivo config.txt esté en la misma carpeta que el ejecutable y tenga el formato correcto.
Paso 6: Revisión del Archivo MIDI
Reproducir el Archivo MIDI:
Usa un reproductor de MIDI o un software de edición musical como MuseScore, FL Studio, o cualquier otro que soporte archivos MIDI para reproducir la melodía generada.
Notas Adicionales
Este programa está diseñado para generar melodías de manera automática según las configuraciones predefinidas en el archivo config.txt.
Para cambiar las configuraciones, editar el archivo config.txt y volver a ejecutar el programa.
Este manual proporciona todas las instrucciones necesarias para utilizar el Compilador Musical de manera efectiva.



