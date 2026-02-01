# Dashboard.py
# Gestión sencilla de tareas para Programación Orientada a Objetos
# Autor: MARIA JOSE TORRES JUNGAL
# Fecha: [01/02/2026]

class Dashboard:
    def __init__(self):
        self.tareas = []

    def mostrar_menu(self):
        print("\n===== DASHBOARD POO =====")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

    def agregar_tarea(self):
        tarea = input("📌 Ingrese la descripción de la tarea: ")
        self.tareas.append(tarea)
        print("✅ Tarea agregada.")

    def ver_tareas(self):
        if not self.tareas:
            print("⚠️ No hay tareas registradas.")
        else:
            print("\n📋 Tareas actuales:")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self):
        self.ver_tareas()
        if self.tareas:
            indice = int(input("Ingrese número de tarea a eliminar: "))
            if 1 <= indice <= len(self.tareas):
                eliminado = self.tareas.pop(indice-1)
                print(f"🗑️ Tarea eliminada: {eliminado}")
            else:
                print("❌ Número inválido.")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.ver_tareas()
            elif opcion == "3":
                self.eliminar_tarea()
            elif opcion == "4":
                print("👋 ¡Hasta pronto!")
                break
            else:
                print("❌ Opción no válida.")

# Ejecutar el Dashboard
if __name__ == "__main__":
# libro.py
# Clase que representa un libro en la biblioteca

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return "📕 Libro prestado correctamente."
        else:
            return "❌ El libro no está disponible."

    def devolver(self):
        self.disponible = True
        return "📗 Libro devuelto correctamente."

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"
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
# main.py
# Archivo principal

from biblioteca import Biblioteca

if __name__ == "__main__":
    sistema = Biblioteca()
    sistema.menu()

    dash = Dashboard()
    dash.ejecutar()
