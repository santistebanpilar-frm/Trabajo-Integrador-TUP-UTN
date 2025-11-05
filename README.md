### Tecnicatura Universitaria de Programación - UTN FRM  
### Integrador Final: Manejo de Base de Datos de Países  
### Asignatura: Programación I - Profesor Ariel Enferrel 
### Integrantes: Quirós, Pablo - Santisteban, Pilar (1prog2)  

# 📄 Descripción del programa 
Este proyecto se hizo con la idea de poder incorporar los conocimientos aprendidos en la materia de Programación I.  
La base de datos se realizó gracias a la API de https://restcountries.com/.  
El programa cuenta con un menú principal donde el usuario tendrá distintas operaciones para ejecutar.  
  •Uno podrá buscar un país, el cual si existiese se le devolverá una breve información.  
  •Permite filtrar la información de la base de datos de acuerdo al continente, un determinado rango de población o un rango de superficie.  
  •Mostrará a los países ordenados por su nombre alfabéticamente, por la cantidad de habitantes y por su superfice.   
  •Ofrece estadísticas de cual es el país con mayor cantidad de población como también cuáles son los que tienen la menor cantidad.   
  •Además brinda con el promedio de población y superficie. Incluso muestra cuantos países se encuentran por continente.  
  
# 🚧 Estructura  
El proyecto consiste de dos documentos principales.  
Primero se encuentra el archivo *main.py* el cual contiene funciones básicas del proyecto, la creación del archivo csv si no existiese, y el menú interactivo donde el usuario podrá elegir entre las distintas operaciones a realizar.  
Y segundo, el archivo *funciones.py* que almacena principalmente las funciones que son llamadas desde el menú del *main*. Dentro además se encuentran funciones de validación y auxiliares.  

# 💻 Instrucciones de uso 
Antes de ejecutar el programa es importate tener instaladas e importadas las siguientes librerías las cuales son necesarias para el funcionamiento del código.
Ya que cada una tiene un papel fundamental para que el proyecto funcione de manera correcta.  
Librerias nátivas de Python:   
•csv: permite leer y escribir archivos CSV.  
•os: módulo que provee de manera versátil de usar funcionalidades dependientes del sistema operativo.  
Librerías no-nativas (se deben instalar):  
•requests: realiza peticiones HTTP, en el caso del proyecto fue para obtener la API. 
``pip install requests``    

## 🐳 Uso con Docker
Si **Docker** está instalado, se puede construir la imagen y ejecutar el programa en un contenedor, evitando la necesidad de instalar las librerías directamente en tu sistema.

Primero, hay que abrir Docker Desktop.  
Segundo, hay que abrir una terminal desde dónde esté el Dockerfile de este repositorio.
Tercero, ejecutar las siguientes líneas en dicha terminal.  
Para **construir la imagen** de la aplicación:
``docker build -t paises-app .``

Y finalmente para **ejecutar el contenedor** de la aplicación:
``docker run -it --rm --name paises-container paises-app``

# ✏️ Ejemplos de entradas y salidas
##**Ejemplo 1**  

*<ins> "Entrada"	 </ins>*  
entrada_pais = input("Ingrese el nombre del país a buscar: ").strip()  
El usuario si escribe: arg  
<*ins> "Salida" </ins>*  
País(es) encontrado(s):  

  Nombre: Argelia  
  Población: 47400000  
  Área: 2381741.0 km²  
  Continente: África  

  Nombre: Argentina  
  Población: 46735004  
  Área: 2780400.0 km²  
  Continente: América  

##**Ejemplo 2**  

*<ins> "Entrada"	 </ins>*  
minimo:int = int(input("Ingrese el mínimo del rango de población: "))  
Usuario ingresa: 0  
maximo:int = int(input("Ingrese el máximo del rango de población: "))  
Usuario ingresa: 50  
<*ins> "Salida" </ins>*  
País(es) con una población entre 0 y 50:  

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

##**Ejemplo 3**  

*<ins> "Entrada"	 </ins>*   
Solicitar al usuario que como ordenar a los países.  
  opcion : str = str(input("Usted seleccionó la opción: "))  
Usuario ingresa: 2  
<*ins> "Salida" </ins>*   
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
   
##**Ejemplo 4**  

*<ins> "Entrada"	 </ins>*  
Solicitar al usuario que estadística desea ver.  
opcion : str = str(input("Usted seleccionó la opción: "))   
Usuario ingresa: 4  
*<ins> "Salida" </ins>*  
Usted seleccionó la opción: 4  
Cantidad de Países por Continente:  
África: 58  
América: 55  
Asia: 50  
Europa: 55  
Oceanía: 27  
Antártida: 5 

# 🪪 Participación de los integrantes
Este trabajo se puedo realizar gracias a la comunicación y feedback de los alumnos. 
Lo principal fue poder dialogar cómo se podían llevar las distintas tareas a realizar para que el código funcione de manera correcta.  
Así mismo se llegó a un acuerdo de que hacía cada uno.  
De esta manera poder ir realizando distintas partes del proyecto sin que haya problemas a la hora de subir al repositorio.  
