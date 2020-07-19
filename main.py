from ABB import*
from lista import*
from funcAux import*
from nodoABB import*
from nodoLista import*




archivoPalabras = open("palabras_paginas_lote_de_prueba.csv")

arbolBuscadorTest = ABB()

palabrasPaginas = {}
palabrasCargadas = set()
for lineaArchivo in archivoPalabras:
  lineaArchivo = lineaArchivo[:-1].split(",")
  direccionWeb = lineaArchivo[-1]
  palabrasCargadas = palabrasCargadas.union(set(lineaArchivo[:-1]))
  if direccionWeb not in palabrasPaginas:
    palabrasPaginas[direccionWeb] = set(lineaArchivo[:-1])
  else:
    palabrasPaginas[direccionWeb] = palabrasPaginas[direccionWeb].union(
        set(lineaArchivo[:-1]))
  palabras = Lista()
  for palabra in lineaArchivo[:-1]:
    # CAMBIAR SEGUN EL NOMBRE DE SU FUNCION APPEND DEL TIPO LISTA
    palabras.append(palabra)
  arbolBuscadorTest.insertarPagina(palabras, direccionWeb)
archivoPalabras.close()

################################################################################
################################################################################

#arbolBuscadorTest.treePlot("arbolCompleto")

################################################################################
###################LISTA DE PAGINAS CARGADAS####################################

paginas = list(palabrasPaginas.keys())
print("Las direcciones web de las paginas cargadas son:")
for pagina in paginas:
  print(pagina)

################################################################################
################################################################################

################################################################################
###################PRUEBA DE OPERACION buscarPalabras###########################

print("\nBusqueda de palabras que no existen en el arbol:")
palabrasNoEstan = ["generador", "palabras", "aleatorias", "propio"]
for palabra in palabrasNoEstan:
  listaPalabras = Lista()
  # CAMBIAR SEGUN EL NOMBRE DE SU FUNCION APPEND DEL TIPO LISTA
  listaPalabras.append(palabra)
  print(arbolBuscadorTest.buscarPalabras(listaPalabras))

print("\nBusqueda de palabras que estan en el arbol pero no todas en una pagina:")
palabrasEnDistintas = ["priori", "dinámica", "recursividad", "mismos"]
listaPalabras = Lista()
print("\nBuscadas de a una:")
for palabra in palabrasEnDistintas:
  listaActual = Lista()
  # CAMBIAR SEGUN EL NOMBRE DE SU FUNCION APPEND DEL TIPO LISTA
  listaActual.append(palabra)
  print("La palabra:", palabra, "esta en las Paginas:",
        arbolBuscadorTest.buscarPalabras(listaActual))
  # CAMBIAR SEGUN EL NOMBRE DE SU FUNCION APPEND DEL TIPO LISTA
  listaPalabras.append(palabra)
print("\nTodas juntas:", listaPalabras, "estan en las Paginas:",
      arbolBuscadorTest.buscarPalabras(listaPalabras))

print("\nBusqueda de palabras que estan en dos paginas a la vez:")
for i in range(len(paginas)-1):
  palabras = palabrasPaginas[paginas[i]].intersection(
      palabrasPaginas[paginas[i+1]])
  listaPalabras = Lista()
  for palabra in palabras:
    # CAMBIAR SEGUN EL NOMBRE DE SU FUNCION APPEND DEL TIPO LISTA
    listaPalabras.append(palabra)
  print("Palabras buscadas:", listaPalabras)
  print("Paginas:", arbolBuscadorTest.buscarPalabras(listaPalabras))

################################################################################
################################################################################

################################################################################
###################PRUEBA DE OPERACION palabrasDePagina#########################

print("\nContador de palabras de cada una de las paginas guardadas:")
for pagina in paginas:
  palabrasDePagina = list(palabrasPaginas[pagina])
  palabrasDePaginaArbol = arbolBuscadorTest.palabrasDePagina(pagina)
  print("La pagina", pagina, "tiene", len(palabrasDePagina),
        "palabras distintas ingresadas segun datos de entrada.")
  # CAMBIAR SEGUN OPERACION QUE CALCULA LONGITUD DE SU TIPO LISTA
  print("La pagina", pagina, "tiene", palabrasDePaginaArbol.len(),
        "palabras distintas segun el arbol.")

print("\nContador de palabras de paginas que no estan en el arbol:")
print("La pagina google.com tiene", arbolBuscadorTest.palabrasDePagina("google.com").len(
), "palabras")  # CAMBIAR SEGUN OPERACION QUE CALCULA LONGITUD DE SU TIPO LISTA
print("La pagina yahoo.com tiene", arbolBuscadorTest.palabrasDePagina("yahoo.com").len(
), "palabras")  # CAMBIAR SEGUN OPERACION QUE CALCULA LONGITUD DE SU TIPO LISTA

################################################################################
################################################################################

################################################################################
###############PRUEBA DE OPERACION cantidadTotalPalabras########################

print("\nCantidades de palabras de mas de 1, 5 y 9 letras:")
for nLetras in [1, 5, 9]:
  print("Cantidad de palabras con", nLetras, "letras o mas ingresadas:",
        len(list(filter(lambda x: len(x) >= nLetras, palabrasCargadas))))
  print("Cantidad de palabras con", nLetras, "letras o mas segun el arbol:",
        arbolBuscadorTest.cantidadTotalPalabras(nLetras))

################################################################################
################################################################################

################################################################################
###############PRUEBA DE OPERACION estaBalanceado###############################

print("\nBalanceo del arbol:", arbolBuscadorTest.estaBalanceado())

################################################################################
################################################################################

################################################################################
###############PRUEBA DE OPERACION paginasEnNivel###############################

print("\nDirecciones web de las paginas en cada nivel del arbol:")
for nivel in range(17):
  print(arbolBuscadorTest.paginasEnNivel(nivel))

################################################################################
################################################################################

################################################################################
###############PRUEBA DE OPERACION cantidadPalabrasMasUsadas####################

print("\nCantidades de palabras mas usadas:")
for cantidadPaginas in range(1, 10):
  print("Hay", arbolBuscadorTest.cantidadDePalabrasMasUsadas(
      cantidadPaginas), "palabras usadas en", cantidadPaginas, "paginas o mas")

################################################################################
################################################################################

################################################################################
###############PRUEBA DE OPERACION internasMayusculaAlfabetico##################

print("\nPalabras internas en orden alfabetico:")
mayusculasOrdenadas = list(filter(lambda x: x[0].isupper(), palabrasCargadas))
mayusculasOrdenadas.sort()
print("Todas las palabras con mayuscula ingresadas:", mayusculasOrdenadas)
print("Palabras en mayuscula de nodos internos",
      arbolBuscadorTest.internasMayusculaAlfabetico())

################################################################################
################################################################################

################################################################################
###############PRUEBA DE OPERACION eliminarPalabra##############################

print("\nEliminamos todas las palabras de la pagina listas.edu.ar una por una con la operacion eliminarPalabra:")
for palabra in palabrasPaginas["listas.edu.ar"]:
  arbolBuscadorTest.eliminarPalabra(palabra)
arbolBuscadorTest.treePlot("arbolSinListasEduAr")

print("\nContamos de nuevo las palabras de cada una de las paginas guardadas:")
for pagina in paginas:
  palabrasDePagina = list(palabrasPaginas[pagina])
  palabrasDePaginaArbol = arbolBuscadorTest.palabrasDePagina(pagina)
  print("La pagina", pagina, "tiene", len(palabrasDePagina),
        "palabras distintas ingresadas segun datos de entrada.")
  # CAMBIAR SEGUN OPERACION QUE CALCULA LONGITUD DE SU TIPO LISTA
  print("La pagina", pagina, "tiene", palabrasDePaginaArbol.len(),
        "palabras distintas segun el arbol.")

################################################################################
################################################################################

################################################################################
###############PRUEBA DE OPERACION eliminarPagina###############################

print("\nEliminamos la pagina python.org.ar con la operacion eliminarPagina:")
arbolBuscadorTest.eliminarPagina("python.org.ar")
arbolBuscadorTest.treePlot("arbolListasNiPython")

print("\nContamos de nuevo las palabras de cada una de las paginas guardadas:")
for pagina in paginas:
  palabrasDePagina = list(palabrasPaginas[pagina])
  palabrasDePaginaArbol = arbolBuscadorTest.palabrasDePagina(pagina)
  print("La pagina", pagina, "tiene", len(palabrasDePagina),
        "palabras distintas ingresadas segun datos de entrada.")
  # CAMBIAR SEGUN OPERACION QUE CALCULA LONGITUD DE SU TIPO LISTA
  print("La pagina", pagina, "tiene", palabrasDePaginaArbol.len(),
        "palabras distintas segun el arbol.")

################################################################################
################################################################################
