### Tecnicatura Universitaria de Progrmación - UTN FRM 

### Integrador Final: Manejo de Base de Datos de Países

### Integrantes: Quirós, Pablo - Santisteban, Pilar (1prog2)

# Descripción del programa
Este proyecto se hizo con la idea de poder incorporar los conocimientos aprendidos en la materia de Programación I.

La base de datos se realizó gracias a la API de https://restcountries.com/.

El programa cuenta con un menú principal donde el usuario tendrá distintas operaciones para ejecutar.

  •Uno podrá buscar un país, el cual si existise se le devolvera una breve informacion.
  
  •Permite filtrar la información de la base de datos de acuerdo al continente, un determinado rango de poblacion o un rango de superficie.
  
  •Mostrará a los países ordenados por su nombre alfabeticamente, por la cantidad de habitantes y por su superfice. 
  
  •Ofrece estadisticas de cual es el pais con mayor cantidad de poblacion como tambien cuales son los que tienen la menor cantidad. 
  
  •Ademas brinda con el promedio de población y superficie. Incluso muestra cuantos paises se encuntran por continente.
  

# Instrucciones de uso
Antes de ejecutar el programa es importate tener las siguente librerias importadas las cuales son necesarias para el funcionamiento del código:

•requests

•csv

•os

•emojis

Cada una de estas tienen un papel fundamental para que el proyecto corra de manera correcta.

# Ejemplos de entradas y salidas
Ejemplo 1
"Entrada"
entrada_pais = input("Ingrese el nombre del país a buscar: ").strip()
El usuario si escribe: arg
"Salida"
País(es) encontrado(s):

  Nombre: Argelia
  Población: 47400000
  Área: 2381741.0 km²
  Continente: África

  Nombre: Argentina
  Población: 46735004
  Área: 2780400.0 km²
  Continente: América

Ejemplo 2
"Entrada"
minimo:int = int(input("Ingrese el minimo del rango de población: "))
Usuario ingresa: 0
maximo:int = int(input("Ingrese el maximo del rango de población: "))
Usuario ingresa: 50
"Salida"País(es) con una poblacion entre 0 y 50:

Nombre: Territorio Británico del Océano Índico
Población: 0
Área: 60.0 km²
Continente: Asia

Nombre: Islas Georgias del Sur y Sandwich del Sur
Población: 0
Área: 3903.0 km²
Continente: Antártida

Nombre: Islas Pitcairn
Población: 35
Área: 47.0 km²
Continente: Oceanía

(.....)

Ejemplo 3
"Entrada"
Solicitar al usuario que como ordenar a los paises.
  opcion : str = str(input("Usted seleccionó la opción: "))
Usuario ingresa: 2
"salida"
Usted seleccionó la opción: 2
Países ordenados por población:
 - Territorio Británico del Océano Índico: 0
 - Islas Georgias del Sur y Sandwich del Sur: 0
 - Isla Bouvet: 0
 - Islas Ultramarinas Menores de Estados Unidos: 0
 - Islas Heard y McDonald: 0
 - Islas Pitcairn: 35
 - Tierras Australes y Antárticas Francesas: 400
 -...
   
Ejemplo 4
"Entrada"
Solicitar al usuario que estadistica desea ver.
opcion : str = str(input("Usted seleccionó la opción: ")) 
Usuario ingresa: 4
"Salida"
Usted seleccionó la opción: 4
Cantidad de Países por Continente:
África: 58
América: 55
Asia: 50
Europa: 55
Oceanía: 27
Antártida: 5

# Participación de los integrantes 

Este trabajo se puedo realizar gracias a la comunicación y feedback de los alumnos.
Lo principal fue poder dialogar como se podian llevar las distintas tareas a realizar para que el codigo funcione de manera correcta.
Asi mismo se llego a un acuerdo de que hacia cada uno.
De esta manera poder ir realizando distintas partes del proyecto sin que hayan problemas a la hora de subir al repositorio.
-----------------------------------------------------------
