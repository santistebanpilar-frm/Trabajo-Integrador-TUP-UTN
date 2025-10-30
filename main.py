# -----------------------------------------------------------
#        Integrador Final - Manejo de Datos de Países
#                   Programación I
# -----------------------------------------------------------
# Alumnos: Pablo Quirós y Pilar Santiesteban
# Turno: 1Prog2
# Año: 2025
# -----------------------------------------------------------

# -----------------------------------------------------------
# Importaciones necesarias para el funcionamiento del código.
# -----------------------------------------------------------
import funciones
import emojis
import requests
import csv
import os

# --------------------------------------------------------------------------
# Creación del archivo CSV con datos de países, desde la API REST Countries.
# --------------------------------------------------------------------------
FIELDS = "name,translations,population,area,continents" # Campos que necesitamos de la API (la API devuelve 400 si no se especifican 'fields').
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
    if not os.path.exists('paises.csv'):
        print("Creando archivo 'paises.csv' (Alternativa sin pandas)...")
        try:
            datos = obtener_datos_paises()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la API: {e}")
            return
            
        columnas = ['nombre', 'poblacion', 'area_km2', 'continente']
        with open('paises.csv', 'w', newline='', encoding='utf-8-sig') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)
            escritor.writeheader()
            
            for p in datos:
                nombre = (p.get('translations') or {}).get('spa', {}).get('common') or p.get('name', {}).get('common', '')
                cont = (p.get('continents') or [p.get('region', 'N/A')])[0]
                
                fila = {
                    'nombre': nombre,
                    'poblacion': p.get('population', 0),
                    'area_km2': p.get('area', 0),
                    'continente': CONT_MAP.get(cont, cont),
                }
                escritor.writerow(fila)
        print("Archivo 'paises.csv' creado exitosamente.")
    else:
        print("El archivo 'paises.csv' ya existe. No se ha recreado.")
        
# -------------------------------------------------------------------------------------        
# Función principal del programa, donde se maneja el menú y las opciones seleccionadas.
# -------------------------------------------------------------------------------------
def main():
    crear_csv_paises()
    eleccion:int = int()
    while eleccion != 5:
        try:
            eleccion:int = funciones.menu()
            if eleccion == 1:
                funciones.buscar_pais()
            elif eleccion == 2:
                funciones.filtrar_paises()
            elif eleccion == 3:
                funciones.ordenar_paises()
            elif eleccion == 4:
                funciones.estadisticas()
            elif eleccion == 5:
                print("Saliendo del programa...")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")                                            
        except KeyboardInterrupt:
            print(f"Programa terminado por el usuario.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")     
            
# -------------------------------
# Llamada a la función principal.
# -------------------------------
if __name__ == '__main__':
    main()