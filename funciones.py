#Funciones generales para el código.

# Importaciones necesarias.
import emojis

# Función para la presentación del menú y la toma de decisiones.
def menu():
    print(f"""
⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
⏐⏐         \U0001F30E Base de datos: Países \U0001F30E         ⏐⏐
⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
⏐⏐           Seleccione una opción.            ⏐⏐
⏐⏐                                             ⏐⏐ 
⏐⏐          (1)\U0001F9ED Buscar un país.              ⏐⏐      
⏐⏐          (2)\U0001F50D Filtrar países.              ⏐⏐      
⏐⏐          (3)\U0001F4DA Ordenar países.              ⏐⏐
⏐⏐          (4)\U0001F4CA Mostrar estadísticas.        ⏐⏐ 
⏐⏐          (5)\U00002795 Agregar un país.             ⏐⏐ 
⏐⏐          (6)\U0001F504 Actualizar un país.          ⏐⏐ 
⏐⏐          (7)\U0000274c Salir.                       ⏐⏐
⏐⏐                                             ⏐⏐        
⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
      """)
    eleccion:int = int(input("Usted seleccionó la opción: "))
    return eleccion

# Función para convertir el archivo csv en una lista de diccionarios, para poder trabajar con la información más fácilmente.
def leer_paises():

  paises = []
  
  with open ('paises.csv', 'r', encoding='utf-8-sig') as archivo: # 'encoding='utf-8-sig' sirve para que las tildes y otros simbolos funcionen.
    titulos = archivo.readline().strip().split(',')
    
    for linea in archivo:
      datos = linea.strip().split(',')
      pais = {
        'nombre': datos[0],
        'poblacion': (datos[1]),
        'area_km2': (datos[2]),
        'continente': datos[3]
      }
      paises.append(pais)
  return paises