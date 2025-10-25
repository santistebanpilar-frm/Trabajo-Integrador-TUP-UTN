import requests
import pandas as pd

# Campos que necesitamos de la API (la API devuelve 400 si no se especifican 'fields')
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

if __name__ == '__main__':
    crear_csv_paises()
    
print(f"""
⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
⏐⏐           Base de datos: Países             ⏐⏐
⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
⏐⏐           Seleccione una opción.            ⏐⏐
⏐⏐                                             ⏐⏐ 
⏐⏐         (1)                                 ⏐⏐      
⏐⏐         (2)                                 ⏐⏐      
⏐⏐         (3)                                 ⏐⏐
⏐⏐         (4)                                 ⏐⏐ 
⏐⏐         (5)                                 ⏐⏐ 
⏐⏐         (6)                                 ⏐⏐ 
⏐⏐         (7)                                 ⏐⏐
⏐⏐                                             ⏐⏐        
⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
      """)