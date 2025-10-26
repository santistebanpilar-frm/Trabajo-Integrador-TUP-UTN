# Archivo principal del programa.

# Importaciones necesarias para el funcionamiento del código.
import requests
import pandas as pd
import funciones
import emojis

# Campos que necesitamos de la API (la API devuelve 400 si no se especifican 'fields').
FIELDS = "name,translations,population,area,continents"
CONT_MAP = {
    'Africa': 'África', 'Americas': 'América', 'South America': 'América',
    'North America': 'América', 'Northern America': 'América', 'Central America': 'América',
    'Caribbean': 'América', 'Asia': 'Asia', 'Europe': 'Europa', 'Oceania': 'Oceanía',
    'Antarctic': 'Antártida', 'Antarctica': 'Antártida'
}

def obtener_datos_paises():
    r = requests.get("https://restcountries.com/v3.1/all", params={'fields': FIELDS}, timeout=10)
    r.raise_for_status()
    return r.json()

def crear_csv_paises():
    datos = obtener_datos_paises()
    rows = []
    for p in datos:
        nombre = (p.get('translations') or {}).get('spa', {}).get('common') or p.get('name', {}).get('common', '')
        cont = (p.get('continents') or [p.get('region', 'N/A')])[0]
        rows.append({
            'nombre': nombre,
            'poblacion': p.get('population', 0),
            'area_km2': p.get('area', 0),
            'continente': CONT_MAP.get(cont, cont),
        })
    df = pd.DataFrame(rows)
    df.to_csv('paises.csv', index=False, encoding='utf-8-sig')
    print("Archivo 'paises.csv' creado exitosamente. Columnas:", ", ".join(df.columns))

# Función principal del programa, donde se maneja el menú y las opciones seleccionadas.
def main():
    crear_csv_paises()
    eleccion:int = int()
    while eleccion != 7:
        try:
            eleccion:int = funciones.menu()
            if eleccion == 1:
                print("Opción 1 seleccionada.")
                buscar_pais()
            elif eleccion == 2:
                print("Opción 2 seleccionada.")
                filtrar_paises()
            elif eleccion == 3:
                print("Opción 3 seleccionada.")
                ordenar_paises()
            elif eleccion == 4:
                print("Opción 4 seleccionada.")
                estadisticas()
            elif eleccion == 5:
                print("Opción 5 seleccionada.")
                agregar_pais()
            elif eleccion == 6:
                print("Opción 6 seleccionada.")
                actualizar_pais()
            elif eleccion == 7:
                print("Saliendo del programa.")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")                                            
        except KeyboardInterrupt:
            print(f"Programa terminado por el usuario.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")     

#Funcnion para validar inputs del usuario
def validar_entrada(texto):
    if texto == "":
       raise ValueError("No se permite dejar el campo vacío")
    if texto.isspace():
       raise ValueError("No se permite ingresar solo espacios en blanco")
    if texto == ".":
       raise ValueError("No se permite ingresar solo un punto")
    return texto.title()

#Funcion pra leer y verificar csv
def leer_csv(path: str = 'paises.csv'):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{path}'.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo '{path}' está vacío.")
        return None

#Funcion para buscar pais
def buscar_pais():
    # Leer el archivo CSV de forma segura
    df = leer_csv()
    if df is None:
        return
    busqueda_valida : bool = False
    while not busqueda_valida:
        try:
        # Solicitar el nombre del país al usuario
            entrada = input("Ingrese el nombre del país a buscar: ").strip()
        # Validar la entrada (lanzará ValueError si no es válida)
            pais_buscar = validar_entrada(entrada)    
        # Buscar el país en el DataFrame
            resultado = df[df['nombre'].str.contains(pais_buscar, case=False, na=False)]
            busqueda_valida = True
        except ValueError as e:
            print(f"Error: {e}.Intente de nuevo.")
        except KeyboardInterrupt:
            print("Búsqueda cancelada por el usuario.")
            return
    #Mostrara todos los paises que se encuentren en la base de datos respecto a lo que ingreso el usuario
    if len(resultado) > 0:
        print("Pais encontrado: ")
        for _,pais in resultado.iterrows():
            print(f"Nombre: {pais['nombre']}") 
            print(f"Poblacion: {pais['poblacion':,]}") 
            print(f"Área: {pais['area_km2']:,.1f} km²") 
            print(f"Contiente: {pais['continente']}") 
    else:
        print("El país ingresado no se encontra en la base de datos!")


#Funcion para filtrar paises
def filtrar_paises():    
    print(f"""
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
    ⏐⏐                Filtrar paises               ⏐⏐
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
    ⏐⏐           Seleccione una opción.            ⏐⏐
    ⏐⏐                                             ⏐⏐ 
    ⏐⏐          (1) Por Continentes.               ⏐⏐      
    ⏐⏐          (2) Por Rango de Supercifie.       ⏐⏐      
    ⏐⏐          (3) Por Rango de Población.        ⏐⏐
    ⏐⏐          (4) Salir.                         ⏐⏐
    ⏐⏐                                             ⏐⏐        
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
        """)
    #Solicitar al usuario que filtro desea realizar
    opcion : str = str(input("Ingrese una opcion: "))
    while opcion != "4":
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            print("Saliendo...")
        else:
            print("Opcion invalida, intente nuevamnte!")
        

#Funcion para ordenar paises
def ordenar_paises():
    print(f"""
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
    ⏐⏐                Ordenar paises               ⏐⏐
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
    ⏐⏐           Seleccione una opción.            ⏐⏐
    ⏐⏐                                             ⏐⏐ 
    ⏐⏐          (1) Por Nombre.                    ⏐⏐      
    ⏐⏐          (2) Por Poblacion.                 ⏐⏐      
    ⏐⏐          (3) Por Superfice Ascendente.      ⏐⏐
    ⏐⏐          (4) Por Superfice Desencente.      ⏐⏐
    ⏐⏐          (5) Salir.                         ⏐⏐
    ⏐⏐                                             ⏐⏐        
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
        """)
    #Solicitar al usuario que como ordenar a los paises
    opcion : str = str(input("Ingrese una opcion: "))
    while opcion != "4":
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Saliendo...")
        else:
            print("Opcion invalida, intente nuevamnte!")

def estadisticas():
    print(f"""
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
    ⏐⏐                 Estadisticas                ⏐⏐
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
    ⏐⏐           Seleccione una opción.            ⏐⏐
    ⏐⏐                                             ⏐⏐ 
    ⏐⏐    (1) Pais con Mayor y Menor Población.    ⏐⏐      
    ⏐⏐    (2) Promedio de Población.               ⏐⏐      
    ⏐⏐    (3) Promedio de Superficie.              ⏐⏐
    ⏐⏐    (4) Cantidad de Paises por Continente.   ⏐⏐
    ⏐⏐    (5) Salir.                               ⏐⏐
    ⏐⏐                                             ⏐⏐        
    ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
        """)
    #Solicitar al usuario que estadistica desea ver
    opcion : str = str(input("Ingrese una opcion: "))
    while opcion != "4":
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Saliendo...")
        else:
            print("Opcion invalida, intente nuevamnte!")

#Funcion para agregar pais
def agregar_pais():
    # Leer el archivo CSV y verificar que exista
    df = leer_csv()
    if df is None:
        return
    
#Funcion para actualizar pais
def actualizar_pais():
    # Leer el archivo CSV y verificar que exista
    df = leer_csv()
    if df is None:
        return

# Llamada a la función principal.
if __name__ == '__main__':
    main()