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
