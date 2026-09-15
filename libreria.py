"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""
print(" ================== Ejercicio 1 ================== ")
# Escribe tu código aquí

def agregar_libro(titulo, autor):
    libro = {
        "titulo": titulo,
        "autor": autor
    }
    return libro

# Prueba la función con algunos valores

libro1 = agregar_libro("El arte del joseo", "Jose")
print(libro1)

"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""
print(" ================== Ejercicio 2 ================== ")
# Escribe tu código aquí

def listar_libros(libros):
    titulos = []
    for libro in libros:
        titulos.append(libro["titulo"])
    return titulos

# Prueba la función con algunos valores
libro2 = agregar_libro("Amar o ser amado", "Maria")
libro3 = agregar_libro("Ni un paso más", "Juli")
libro4 = agregar_libro("Páginas amarillas", "Bertran")
libro5 = agregar_libro("Condenados al mismo destino", "Celia")

libros = [libro1, libro2, libro3, libro4, libro5]
titulos = listar_libros(libros)
print(titulos)

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""
print(" ================== Ejercicio 3 ================== ")
# Escribe tu código aquí

def buscar_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            return libro
    return None

# Prueba la función con algunos valores

print(buscar_libro(libros, "El arte del joseo"))
print(buscar_libro(libros, "El arte del amor"))

"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""
print(" ================== Ejercicio 4 ================== ")
# Escribe tu código aquí

def quitar_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            libros.remove(libro)
            return libros
    return f"No hay un libro con titulo: {titulo}"

# Prueba la función con algunos valores

print("Libros sin modificar:", libros)
print(quitar_libro(libros, "Amar o ser olvidado"))
print("Libros modificados:", quitar_libro(libros, "Amar o ser amado"))


"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""
print(" ================== Ejercicio 5 ================== ")
# Escribe tu código aquí

def crear_inventario(libros):
    inventario = {}
    for libro in libros:
        autor = libro["autor"]
        if autor in inventario:
            inventario[autor] += 1
        else:
            inventario[autor] = 1
    return inventario

# Prueba la función con algunos valores
print(crear_inventario(libros))


"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""
print(" ================== Ejercicio 6 ================== ")
# Escribe tu código aquí

def libros_por_autor(libros, autor):
    titulos = []
    for libro in libros:
        if libro["autor"] == autor:
            titulos.append(libro["titulo"])
    return titulos

# Prueba la función con algunos valores
print("Libros de Jose:", libros_por_autor(libros, "Jose"))
print("Libros de Juli:", libros_por_autor(libros, "Juli"))

"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""
print(" ================== Ejercicio 7 ================== ")
# Escribe tu código aquí

def existe_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            return True
    return False

# Prueba la función con algunos valores
print("¿Existe 'El arte del joseo'?:", existe_libro(libros, "El arte del joseo"))
print("¿Existe 'Cien años de soledad'?:", existe_libro(libros, "Cien años de soledad"))
