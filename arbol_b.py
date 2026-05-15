import csv


# =========================
# Nodo del Árbol B
# =========================
class NodoB:
    def __init__(self, hoja=False):
        self.hoja = hoja
        self.claves = []
        self.hijos = []


# =========================
# Árbol B
# =========================
class ArbolB:
    def __init__(self, grado):
        self.raiz = NodoB(True)
        self.grado = grado

    # =====================
    # Buscar una clave
    # =====================
    def buscar(self, clave, nodo=None):

        if nodo is None:
            nodo = self.raiz

        i = 0

        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and clave == nodo.claves[i]:
            return True

        if nodo.hoja:
            return False

        return self.buscar(clave, nodo.hijos[i])

    # =====================
    # Insertar
    # =====================
    def insertar(self, clave):

        raiz = self.raiz

        # Si la raíz está llena
        if len(raiz.claves) == (2 * self.grado) - 1:

            nueva_raiz = NodoB(False)
            nueva_raiz.hijos.append(self.raiz)

            self.dividir_hijo(nueva_raiz, 0)

            self.raiz = nueva_raiz

            self.insertar_no_lleno(nueva_raiz, clave)

        else:
            self.insertar_no_lleno(raiz, clave)

    # =====================
    # Insertar en nodo no lleno
    # =====================
    def insertar_no_lleno(self, nodo, clave):

        i = len(nodo.claves) - 1

        if nodo.hoja:

            nodo.claves.append(None)

            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1

            nodo.claves[i + 1] = clave

        else:

            while i >= 0 and clave < nodo.claves[i]:
                i -= 1

            i += 1

            if len(nodo.hijos[i].claves) == (2 * self.grado) - 1:

                self.dividir_hijo(nodo, i)

                if clave > nodo.claves[i]:
                    i += 1

            self.insertar_no_lleno(nodo.hijos[i], clave)

    # =====================
    # Dividir nodo hijo
    # =====================
    def dividir_hijo(self, padre, indice):

        grado = self.grado

        nodo = padre.hijos[indice]
        nuevo_nodo = NodoB(nodo.hoja)

        padre.hijos.insert(indice + 1, nuevo_nodo)
        padre.claves.insert(indice, nodo.claves[grado - 1])

        nuevo_nodo.claves = nodo.claves[grado : (2 * grado) - 1]
        nodo.claves = nodo.claves[0 : grado - 1]

        if not nodo.hoja:
            nuevo_nodo.hijos = nodo.hijos[grado : (2 * grado)]
            nodo.hijos = nodo.hijos[0:grado]

    # =====================
    # Mostrar árbol
    # =====================
    def mostrar(self, nodo=None, nivel=0):

        if nodo is None:
            nodo = self.raiz

        print("Nivel", nivel, ":", nodo.claves)

        if not nodo.hoja:
            for hijo in nodo.hijos:
                self.mostrar(hijo, nivel + 1)

    # =====================
    # Eliminar clave
    # (Versión básica)
    # =====================
    def eliminar(self, clave, nodo=None):

        if nodo is None:
            nodo = self.raiz

        if clave in nodo.claves:
            nodo.claves.remove(clave)
            return True

        if nodo.hoja:
            return False

        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1

        return self.eliminar(clave, nodo.hijos[i])

    # =====================
    # Cargar CSV
    # =====================
    def cargar_csv(self, archivo):

        try:
            with open(archivo, newline="") as csvfile:

                lector = csv.reader(csvfile)

                for fila in lector:
                    for dato in fila:

                        try:
                            numero = int(dato)
                            self.insertar(numero)
                        except:
                            pass

            print("Datos cargados correctamente.")

        except FileNotFoundError:
            print("Archivo no encontrado.")


# =========================
# MENÚ
# =========================
def menu():

    grado = int(input("Ingrese el grado del Árbol B: "))

    arbol = ArbolB(grado)

    while True:

        print("\n===== MENÚ =====")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Mostrar árbol")
        print("5. Cargar CSV")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        # INSERTAR
        if opcion == "1":

            clave = int(input("Ingrese clave: "))
            arbol.insertar(clave)

            print("Clave insertada.")

        # BUSCAR
        elif opcion == "2":

            clave = int(input("Ingrese clave a buscar: "))

            if arbol.buscar(clave):
                print("Clave encontrada.")
            else:
                print("Clave NO encontrada.")

        # ELIMINAR
        elif opcion == "3":

            clave = int(input("Ingrese clave a eliminar: "))

            if arbol.eliminar(clave):
                print("Clave eliminada.")
            else:
                print("No existe la clave.")

        # MOSTRAR
        elif opcion == "4":

            arbol.mostrar()

        # CSV
        elif opcion == "5":

            archivo = input("Ingrese nombre del archivo CSV: ")
            arbol.cargar_csv(archivo)

        # SALIR
        elif opcion == "6":
            break

        else:
            print("Opción inválida.")


# =========================
# Ejecutar programa
# =========================
menu()
