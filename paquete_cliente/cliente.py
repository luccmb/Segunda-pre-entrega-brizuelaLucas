class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.historial_compras = []

    def agregar_compra(self, compra):
        self.historial_compras.append(compra)
        
    def mostrar_historial(self):
        return f"Historial de compras de {self.nombre}: {self.historial_compras}"
    
    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Telefono: {self.telefono}"
    