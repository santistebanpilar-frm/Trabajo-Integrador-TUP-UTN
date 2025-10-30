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
  return texto.title()

def normalizar_input(texto):
  texto = texto.lower() 
  tabla = str.maketrans( "áéíóúüñ", "aeiouun" ) 
  return texto.translate(tabla)

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
    return continente_elegido

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
                print("Búsqueda cancelada por el usuario.")
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
            ⏐⏐           Seleccione una opción.            ⏐⏐
            ⏐⏐                                             ⏐⏐ 
            ⏐⏐          (1) Por Continentes.               ⏐⏐      
            ⏐⏐          (2) Por Rango de Supercifie.       ⏐⏐      
            ⏐⏐          (3) Por Rango de Población.        ⏐⏐
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
                            ------------------------------------            
                                """)
                            continente_a_buscar = int(input("Usted seleccionó la opción: "))
                            if 1 <= continente_a_buscar <= 5:
                                entrada_valida = True
                            else:
                                print("Opción inválida. Por favor, intente de nuevo.")       
                        except ValueError as e:
                            print(f"Error de valor ingresado. Por favor, ingrese un número válido.") 
                            print(" ")
                        except KeyboardInterrupt:
                            print("Búsqueda cancelada por el usuario.")
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
                           minimo:float = float(input("Ingrese el minimo del rango de superficie:"))
                           if minimo <= 0:
                               print("Error. No se pueden ingresar numeros negativos o cero.")
                               print(" ")    
                           else:
                               maximo:float = float(input("Ingrese el máximo del rango de superficie:"))
                               if maximo <= 0 or maximo <= minimo:
                                   print("Error. No se pueden ingresar numeros negativos, cero, o que el maximo sea menor que el minimo.")
                                   print(" ")
                               else:                                      
                                   entrada_valida = True  
                        except ValueError as e:
                            print(f"Error de valor ingresado. Por favor, ingrese un número válido.") 
                            print(" ")
                        except KeyboardInterrupt:
                            print("Búsqueda cancelada por el usuario.")
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
                except Exception as e:
                    print(f"Error inesperado: {str(e)}")
            # Filtrado por rango de población.
            elif opcion == "3":
                pass
            # Salir.
            elif opcion == "4":
                print("Volviendo al menú principal...")
            else:
                print("Opción inválida. Port favor, intente de nuevo.")
        except KeyboardInterrupt:
            print(f"Programa terminado por el usuario.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")  
            
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
            ⏐⏐           Seleccione una opción.            ⏐⏐
            ⏐⏐                                             ⏐⏐ 
            ⏐⏐          (1) Por Nombre.                    ⏐⏐      
            ⏐⏐          (2) Por Poblacion.                 ⏐⏐      
            ⏐⏐          (3) Por Superfice Ascendente.      ⏐⏐
            ⏐⏐          (4) Por Superfice Desencente.      ⏐⏐
            ⏐⏐          (5) Volver al menú principal.      ⏐⏐
            ⏐⏐                                             ⏐⏐        
            ⏐⏐≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡⏐⏐         
                """)
            # Solicitar al usuario que como ordenar a los paises.
            opcion : str = str(input("Ingrese una opcion: "))
            if opcion == "1":
                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                print("Volviendo al menú principal...")
            else:
                print("Opcion invalida, intente nuevamnte!")
        except KeyboardInterrupt:
            print(f"Programa terminado por el usuario.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")  

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
            ⏐⏐           Seleccione una opción.            ⏐⏐
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
            opcion : str = str(input("Ingrese una opcion: "))  
            if opcion == "1":
                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                print("Volviendo al menú principal...")
            else:
                print("Opcion invalida, intente nuevamnte!")
        except KeyboardInterrupt:
            print(f"Programa terminado por el usuario.")
        except ValueError as e:
            print(f"Error de valor ingresado. Por favor, ingrese un número válido.")  