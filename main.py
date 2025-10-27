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
                try:
                    paises = funciones.leer_paises()
                    if paises:                      
                        print(f"Se encontraron {len(paises)} países en total.")
                        print("Mostrando los países como prueba:")
                        for pais in paises:
                            print(f"\nPaís: {pais['nombre']}")
                            print(f"Población: {pais['poblacion']}")
                            print(f"Área: {pais['area_km2']} km²")
                            print(f"Continente: {pais['continente']}")
                            print("-" * 50)
                    else:
                        print("No se encontraron países en el archivo.")        
                except Exception as e:
                    print(f"Error al leer los países: {str(e)}")
            elif eleccion == 2:
                print("Opción 2 seleccionada.")
            elif eleccion == 3:
                print("Opción 3 seleccionada.")
            elif eleccion == 4:
                print("Opción 4 seleccionada.")
            elif eleccion == 5:
                print("Opción 5 seleccionada.")
            elif eleccion == 6:
                print("Opción 6 seleccionada.")
            elif eleccion == 7:
                print("Saliendo del programa.")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")                                            
        except KeyboardInterrupt:
            print(f"Programa terminado por el usuario.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")     

# Llamada a la función principal.
if __name__ == '__main__':
    main()