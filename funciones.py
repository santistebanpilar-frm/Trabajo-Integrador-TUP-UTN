# -----------------------------------------------------------
# Importaciones necesarias para el funcionamiento del código.
# -----------------------------------------------------------
import emojis
import csv
import os

# -----------------------------------
# Funciones generales para el código.
# -----------------------------------

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
⏐⏐          (5)\U0000274c Salir.                       ⏐⏐
⏐⏐                                             ⏐⏐        
⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
      """)
    eleccion:int = int(input("Usted seleccionó la opción: "))
    return eleccion

# Función para convertir el archivo csv en una lista de diccionarios, para poder trabajar con la información más fácilmente.
def leer_paises():
    paises = []
    try:
        with open('paises.csv', 'r', encoding='utf-8-sig') as archivo: # 'encoding='utf-8-sig' sirve para que las tildes y otros simbolos funcionen.
            titulos = archivo.readline().strip().split(',')
            
            for linea in archivo:
                datos = linea.strip().split(',')
                if len(datos) >= 4:  # Se verifica que tengamos todos los campos necesarios.
                    pais = {
                        'nombre': datos[0].strip(),
                        'poblacion': datos[1].strip(),
                        'area_km2': datos[2].strip(),
                        'continente': datos[3].strip()
                    }
                    paises.append(pais)
            return paises      
    except FileNotFoundError:
        print("Error: no se encontró el archivo 'paises.csv'")
    except Exception as e:
        print(f"Error al leer los países: {str(e)}")
    return []  # Retornar lista vacía en caso de error.

# Funciones de validaciones.
def validar_input(texto):
  if texto == "":
    raise ValueError("No se permite dejar el campo vacio.")
  elif texto.isspace():
    raise ValueError("No se puede ingresar espacios vacios.")
  elif texto==".":
    raise ValueError("No se puede ingresar un punto.")
  elif texto.isnumeric():
    raise ValueError("No se permiten números.")
  return texto

def normalizar_input(texto):
  texto = texto.lower() 
  tabla = str.maketrans( "áéíóúüñ", "aeiouun" ) 
  return texto.translate(tabla)

# Funciones auxiliares.
def elegir_continente(continente_a_buscar:int):
    if continente_a_buscar == 1:
        continente_elegido = 'África'
    elif continente_a_buscar == 2:
        continente_elegido = 'América'
    elif continente_a_buscar == 3:
        continente_elegido = 'Asia'
    elif continente_a_buscar == 4:
        continente_elegido = 'Europa'
    elif continente_a_buscar == 5:
        continente_elegido = 'Oceanía' 
    elif continente_a_buscar == 6:
        continente_elegido = 'Antártida'    
    return continente_elegido

def obtener_clave(criterio):
    def clave(pais):
        if criterio == "nombre":
            return pais["nombre"].lower()
        elif criterio == "poblacion":
            return int(pais["poblacion"])
        elif criterio == "superficie":
            return float(pais["area_km2"])
        else:
            return pais["nombre"].lower()
    return clave


# -------------------------------
# Funciones principales del menú.
# -------------------------------

# Elección 1: Buscar país.
def buscar_pais():
    paises:list = leer_paises()
    if not paises:
        print("No se pudieron cargar los países.")
        return
    
    try:
        entrada_valida:bool = False
        pais_a_buscar:str = ""
        
        while not entrada_valida:
            try:
                entrada_pais = input("Ingrese el nombre del país a buscar: ").strip()
                pais_a_buscar = validar_input(entrada_pais)
                entrada_valida = True
            except ValueError as e:
                print(f"Error: {e} Intente de nuevo.")
                print(" ")
            except KeyboardInterrupt:
                print("Error: Interrupción por teclado.")
                return

        pais_normalizado = normalizar_input(pais_a_buscar)
        encontrados = [
            pais for pais in paises
            if pais_normalizado in normalizar_input(pais["nombre"])
        ]

        if len(encontrados) > 0:
            print("País(es) encontrado(s):")
            print(" ")
            for pais in encontrados:
                print(f"Nombre: {pais['nombre']}")
                print(f"Población: {pais['poblacion']}")
                print(f"Área: {pais['area_km2']} km²")
                print(f"Continente: {pais['continente']}")
                print("-" * 40)
        else:
            print(f"No se encontró al pais '{pais_a_buscar}' en nuestra base de datos.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
    os.system('pause')
    os.system('cls' if os.name == 'nt' else 'clear')    

# Elección 2: Filtrar países.
def filtrar_paises():
    paises:list = leer_paises()
    if not paises:
        print("No se pudieron cargar los países.")
        return
    opcion = ()
    while opcion != "4":
        try:
            print(f"""
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
            ⏐⏐                Filtrar paises               ⏐⏐
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
            ⏐⏐            Seleccione una opción.           ⏐⏐
            ⏐⏐                                             ⏐⏐ 
            ⏐⏐          (1) Por continentes.               ⏐⏐      
            ⏐⏐          (2) Por rango de supercifie.       ⏐⏐      
            ⏐⏐          (3) Por rango de población.        ⏐⏐
            ⏐⏐          (4) Volver al menú principal.      ⏐⏐
            ⏐⏐                                             ⏐⏐        
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
                """)
            # Solicitar al usuario que filtro desea realizar.
            opcion:str = str(input("Usted seleccionó la opción: "))
            
            # Filtrado por continentes.  
            if opcion == "1":
                try:
                    entrada_valida:bool = False
                    continente_a_buscar = ()
            
                    while not entrada_valida:
                        try:
                            print(f"""
                            ------------------------------------      
                                        Continentes
                            ------------------------------------
                                    Elija un continente.
                                    
                                        (1) África.
                                        (2) América.
                                        (3) Asia.
                                        (4) Europa.
                                        (5) Oceanía.
                                        (6) Antártida.
                            ------------------------------------            
                                """)
                            continente_a_buscar = int(input("Usted seleccionó la opción: "))
                            if 1 <= continente_a_buscar <= 6:
                                entrada_valida = True
                            else:
                                print("Opción inválida. Por favor, intente de nuevo.")       
                        except ValueError as e:
                            print(f"Error de valor ingresado. Por favor, ingrese un número válido.") 
                            print(" ")
                        except KeyboardInterrupt:
                            print("Error: Interrupción por teclado.")
                            return
                        
                    continente_elegido = elegir_continente(continente_a_buscar)
                    encontrados = [
                        continente for continente in paises
                        if continente["continente"] == continente_elegido
                    ]
                    
                    if len(encontrados) > 0:
                        print(f"País(es) encontrado(s) en {continente_elegido}:")
                        print(" ")
                        for continente in encontrados:
                            print(f"Nombre: {continente['nombre']}")
                            print(f"Población: {continente['poblacion']}")
                            print(f"Área: {continente['area_km2']} km²")
                            print(f"Continente: {continente['continente']}")
                            print("-" * 40)            
                except Exception as e:
                    print(f"Error inesperado: {str(e)}")
            # Filtrado por rango de superficie.          
            elif opcion == "2":
                try:
                    entrada_valida:bool = False
                    minimo:float = ()
                    maximo:float = ()
                    while not entrada_valida:
                        try:
                           minimo:float = float(input("Ingrese el minimo del rango de superficie: "))
                           if minimo <= 0:
                               print("Error. No se pueden ingresar numeros negativos o cero.")
                               print(" ")    
                           else:
                               maximo:float = float(input("Ingrese el máximo del rango de superficie: "))
                               if maximo <= 0 or maximo <= minimo:
                                   print("Error. No se pueden ingresar numeros negativos, cero, o que el maximo sea menor que el minimo.")
                                   print(" ")
                               else:                                      
                                   entrada_valida = True  
                        except ValueError as e:
                            print(f"Error de valor ingresado. Por favor, ingrese un número válido.") 
                            print(" ")
                        except KeyboardInterrupt:
                            print("Error: Interrupción por teclado.")
                            return
                        
                    encontrados = [
                        area for area in paises
                        if float(area["area_km2"]) >= minimo and float(area["area_km2"]) <= maximo
                    ]
                    
                    if len(encontrados) > 0:
                        print(f"País(es) con un área entre {minimo} y {maximo}:")
                        print(" ")
                        for area in encontrados:
                            print(f"Nombre: {area['nombre']}")
                            print(f"Población: {area['poblacion']}")
                            print(f"Área: {area['area_km2']} km²")
                            print(f"Continente: {area['continente']}")
                            print("-" * 40)
                    else:
                        print("No se encontraron países en ese rango de superficie.")                    
                except Exception as e:
                    print(f"Error inesperado: {str(e)}")
            # Filtrado por rango de población.
            elif opcion == "3":
                try:
                    entrada_valida:bool = False
                    minimo:int = ()
                    maximo:int = ()
                    while not entrada_valida:
                        try:
                           minimo:int = int(input("Ingrese el minimo del rango de población: "))
                           if minimo < 0:
                               print("Error. No se pueden ingresar numeros negativos.")
                               print(" ")    
                           else:
                               maximo:int = int(input("Ingrese el máximo del rango de población: "))
                               if maximo <= 0 or maximo <= minimo:
                                   print("Error. No se pueden ingresar numeros negativos, cero, o que el maximo sea menor que el minimo.")
                                   print(" ")
                               else:                                      
                                   entrada_valida = True  
                        except ValueError as e:
                            print(f"Error de valor ingresado. Por favor, ingrese un número válido.") 
                            print(" ")
                        except KeyboardInterrupt:
                            print("Error: Interrupción por teclado.")
                            return
                        
                    encontrados = [
                        poblacion for poblacion in paises
                        if int(poblacion["poblacion"]) >= minimo and int(poblacion["poblacion"]) <= maximo
                    ]
                    
                    if len(encontrados) > 0:
                        print(f"País(es) con una poblacion entre {minimo} y {maximo}:")
                        print(" ")
                        for poblacion in encontrados:
                            print(f"Nombre: {poblacion['nombre']}")
                            print(f"Población: {poblacion['poblacion']}")
                            print(f"Área: {poblacion['area_km2']} km²")
                            print(f"Continente: {poblacion['continente']}")
                            print("-" * 40)    
                    else:
                        print("No se encontraron países en ese rango de población.")                
                except Exception as e:
                    print(f"Error inesperado: {str(e)}")
            # Salir.
            elif opcion == "4":
                print("Volviendo al menú principal...")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        except KeyboardInterrupt:
            print(f"Error: Interrupción por teclado.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")  
    os.system('cls' if os.name == 'nt' else 'clear')  
          
# Elección 3: Ordenar países.
def ordenar_paises():
    paises = leer_paises()
    if not paises:
        print("No se pudieron cargar los países.")
        return
    opcion = ()
    while opcion != "5":
        try:
            print(f"""
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
            ⏐⏐                Ordenar paises               ⏐⏐
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
            ⏐⏐            Seleccione una opción.           ⏐⏐
            ⏐⏐                                             ⏐⏐ 
            ⏐⏐          (1) Por nombre.                    ⏐⏐      
            ⏐⏐          (2) Por poblacion.                 ⏐⏐      
            ⏐⏐          (3) Por superfice ascendente.      ⏐⏐
            ⏐⏐          (4) Por superfice desencente.      ⏐⏐
            ⏐⏐          (5) Volver al menú principal.      ⏐⏐
            ⏐⏐                                             ⏐⏐        
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
                """)
            # Solicitar al usuario que como ordenar a los paises.
            opcion : str = str(input("Usted seleccionó la opción: "))
            
            # Ordenar por nombre.
            if opcion == "1":
                ordenados_nombre = sorted(paises, key=obtener_clave("nombre"))
                print("Países ordenados por Nombre:")
                for pais in ordenados_nombre:
                    print(f" - {pais['nombre']}")
            # Ordenar por población.
            elif opcion == "2":
                ordenados_poblacion = sorted(paises, key=obtener_clave("poblacion"))
                print("Países ordenados por población:")
                for pais in ordenados_poblacion:
                    print(f" - {pais['nombre']}: {pais['poblacion']}")
            # Ordenar por superficie ascendente.
            elif opcion == "3":
                ordenados_superficie= sorted(paises, key=obtener_clave("superficie"))
                print("Países ordenados por superficie(Ascendente):")
                for pais in ordenados_superficie:
                    print(f"- {pais['nombre']}: {pais['area_km2']} km²")
            # Ordenar por superficie descendente.    
            elif opcion == "4":
                ordenados_superficie = sorted(paises, key=obtener_clave("superficie"), reverse=True)
                print("Países ordenados por superficie(Descendente):")
                for pais in ordenados_superficie:
                    print(f"- {pais['nombre']}: {pais['area_km2']} km²")
            # Salir.
            elif opcion == "5":
                print("Volviendo al menú principal...")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        except KeyboardInterrupt:
            print(f"Error: Interrupción por teclado.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")  
    os.system('cls' if os.name == 'nt' else 'clear') 
    
# Elección 4: Estadísticas.
def estadisticas():
    paises = leer_paises()
    if not paises:
        print("No se pudieron cargar los países.")
        return
    opcion = ()
    while opcion != "5":
        try:
            print(f"""
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐
            ⏐⏐                 Estadisticas                ⏐⏐
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐     
            ⏐⏐            Seleccione una opción.           ⏐⏐
            ⏐⏐                                             ⏐⏐ 
            ⏐⏐    (1) Pais con Mayor y Menor Población.    ⏐⏐      
            ⏐⏐    (2) Promedio de Población.               ⏐⏐      
            ⏐⏐    (3) Promedio de Superficie.              ⏐⏐
            ⏐⏐    (4) Cantidad de Paises por Continente.   ⏐⏐
            ⏐⏐    (5) Volver al menú principal.            ⏐⏐
            ⏐⏐                                             ⏐⏐        
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
                """)
            # Solicitar al usuario que estadistica desea ver.
            opcion : str = str(input("Usted seleccionó la opción: ")) 
            
            # Estadistica 1: País con mayor y menor población.  
            if opcion == "1":
                # Convertimos las poblaciones a número enteros para mejor facilidad al comparar dentro de una lista de tuplas.
                poblaciones = [(int(p['poblacion']),p['nombre']) for p in paises]
                mayor_poblacion = max(poblaciones)
                menor_poblacion = min(poblaciones)
                print(f"País con Mayor Número de Población: {mayor_poblacion[1]} ({mayor_poblacion[0]:,} habitantes)")
                print("-" * 40)
                encontrados_menor = [
                        pais for pais in paises
                        if int(pais["poblacion"]) == 0
                    ]
                if len(encontrados_menor) > 0:
                    print("Pais(es) con Menor Número de Población: ")
                    for pais in encontrados_menor:
                        print(f"Nombre: {pais['nombre']}")
                        print(f"Población: {pais['poblacion']} habitantes")
                        print("-" * 40)
                else:
                    print(f"País con Menor Número de Población: {menor_poblacion[1]} ({menor_poblacion[0]:,} habitantes)")
            # Estadistica 2: Promedio de población.
            elif opcion == "2":
                total_poblacion = sum(int(p['poblacion']) for p in paises)
                promedio_poblacion = total_poblacion / len(paises)
                print(f"Promedio de Población: {promedio_poblacion:.2f} habitantes")
            # Estadistica 3: Promedio de superficie.
            elif opcion == "3":
                total_superficie = sum(float(p['area_km2']) for p in paises)
                promedio_superficie = total_superficie / len(paises)
                print(f"Promedio de Superficie: {promedio_superficie:.2f} km²")
            # Estadistica 4: Cantidad de países por continente.    
            elif opcion == "4":
                cantidad_continentes = []
                for pais in paises:
                    continente = pais['continente']
                    cantidad_continentes.append(continente)
                conteo = {}
                for continente in cantidad_continentes:
                    if continente in conteo:
                        conteo[continente] += 1
                    else:
                        conteo[continente] = 1
                print("Cantidad de Países por Continente:")
                for continente, cantidad in conteo.items():
                    print(f"{continente}: {cantidad}")
            # Salir.
            elif opcion == "5":
                print("Volviendo al menú principal...")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        except KeyboardInterrupt:
            print("Error: Interrupción por teclado.")
        except ValueError as e:
            print(f"{e} Error de valor ingresado. Por favor, ingrese un número válido.") 
    os.system('cls' if os.name == 'nt' else 'clear')