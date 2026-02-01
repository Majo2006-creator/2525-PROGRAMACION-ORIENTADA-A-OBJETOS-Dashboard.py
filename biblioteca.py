# biblioteca.py
# Clase que gestiona los libros

from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        libro = Libro(titulo, autor)
        self.libros.append(libro)
        print("✅ Libro agregado.")

    def mostrar_libros(self):
        if not self.libros:
            print("⚠️ No hay libros registrados.")
        else:
            print("\n📚 Catálogo de libros:")
            for i, libro in enumerate(self.libros, 1):
                print(f"{i}. {libro.mostrar_info()}")

    def prestar_libro(self):
        self.mostrar_libros()
        indice = int(input("Ingrese el número del libro a prestar: "))
        if 1 <= indice <= len(self.libros):
            print(self.libros[indice-1].prestar())
        else:
            print("❌ Opción inválida.")

    def devolver_libro(self):
        self.mostrar_libros()
        indice = int(input("Ingrese el número del libro a devolver: "))
        if 1 <= indice <= len(self.libros):
            print(self.libros[indice-1].devolver())
        else:
            print("❌ Opción inválida.")

    def menu(self):
        while True:
            print("\n===== BIBLIOTECA ESCOLAR =====")
            print("1. Agregar libro")
            print("2. Mostrar libros")
            print("3. Prestar libro")
            print("4. Devolver libro")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.mostrar_libros()
            elif opcion == "3":
                self.prestar_libro()
            elif opcion == "4":
                self.devolver_libro()
            elif opcion == "5":
                print("👋 Gracias por usar el sistema.")
                break
            else:
                print("❌ Opción no válida.")
