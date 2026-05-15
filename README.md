README - Árbol B en Python

Este proyecto implementa un Árbol B en Python de forma interactiva mediante consola.
El programa permite:

Insertar claves
Buscar claves
Eliminar claves
Mostrar la estructura del árbol
Cargar datos desde archivos CSV

El grado del árbol es configurable al iniciar el programa.

¿Qué es un Árbol B?

Un Árbol B es una estructura de datos utilizada para almacenar grandes cantidades de información de manera eficiente.

Se utiliza comúnmente en:

Bases de datos
Sistemas de archivos
Índices
Motores de búsqueda

Sus principales ventajas son:

Búsquedas rápidas
Inserciones eficientes
Eliminaciones eficientes
Mantener datos ordenados automáticamente

Requisitos

Tener instalado:

Python 3.x

Ejecución del programa
1. Descargar el archivo

Archivo principal:

arbol_b.py
2. Abrir terminal o CMD

Ubicarse en la carpeta del proyecto:

cd ruta/del/proyecto

Ejemplo:

cd "D:\Proyectos\ArbolB"
3. Ejecutar el programa
python arbol_b.py
Funcionamiento del programa

Al iniciar, el sistema solicitará el grado del Árbol B:

Ingrese el grado del Árbol B:

Ejemplo:

Ingrese el grado del Árbol B: 3
Menú principal
===== MENÚ =====
1. Insertar
2. Buscar
3. Eliminar
4. Mostrar árbol
5. Cargar CSV
6. Salir
Opciones del sistema
1. Insertar

Permite agregar una clave al árbol.

Ejemplo:

Ingrese clave: 25
2. Buscar

Permite verificar si una clave existe.

Ejemplo:

Ingrese clave a buscar: 25
Clave encontrada.
3. Eliminar

Elimina una clave del árbol.

Ejemplo:

Ingrese clave a eliminar: 25
Clave eliminada.
4. Mostrar árbol

Muestra la estructura del Árbol B por niveles.

Ejemplo:

Nivel 0 : [20]
Nivel 1 : [5, 10]
Nivel 1 : [25, 30]
Cargar archivos CSV

La opción 5 permite cargar datos automáticamente desde un archivo CSV.

Formato del archivo CSV

El archivo debe contener números enteros.

Ejemplo:

10,20,30,40
50,60,70
80

También funciona:

1
2
3
4
5
Cómo cargar un CSV
1. Colocar el archivo CSV

El archivo debe estar:

En la misma carpeta del programa
O indicar la ruta completa

Ejemplo:

datos.csv

o

D:\Archivos\datos.csv
2. Seleccionar opción 5
5. Cargar CSV
3. Ingresar nombre del archivo

Ejemplo:

Ingrese nombre del archivo CSV: datos.csv
4. Resultado esperado
Datos cargados correctamente.
Ejemplo completo de uso
Ingrese el grado del Árbol B: 3

===== MENÚ =====
1. Insertar
2. Buscar
3. Eliminar
4. Mostrar árbol
5. Cargar CSV
6. Salir

Seleccione una opción: 1
Ingrese clave: 50

Seleccione una opción: 1
Ingrese clave: 20

Seleccione una opción: 4

Nivel 0 : [20, 50]
Estructura del proyecto
Proyecto/
│
├── arbol_b.py
├── datos.csv
└── README.md
Posibles errores
Archivo no encontrado
Archivo no encontrado.

Solución:

Verificar nombre del archivo
Verificar extensión .csv
Verificar ubicación del archivo
