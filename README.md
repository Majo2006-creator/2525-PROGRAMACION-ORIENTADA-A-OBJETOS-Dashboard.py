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
    dash = Dashboard()
    dash.ejecutar()
