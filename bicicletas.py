class Bicicletas:
    def __init__ (self):
        self.bicicletas = []

    def agregar_bicicleta(self, id_bicicleta, tipo_bicicleta, marca, color, fecha_compra, numero_marco):
        bicicleta = {
            "id_bicicleta": id_bicicleta,
            "tipo_bicicleta": tipo_bicicleta,
            "marca": marca,
            "color": color,
            "fecha_compra": fecha_compra,
            "numero_marco": numero_marco
        }
        self.bicicletas.append(bicicleta)
        return "Bicicleta agregada exitosamente"
    
    def obtener_bicicleta(self, id_bicicleta):
        for bicicleta in self.bicicletas:
            if bicicleta["id_bicicleta"] == id_bicicleta:
                return bicicleta
        return None
    
    def editar_bicicleta(self, id_bicicleta, **kwargs):
        bicicleta = self.obtener_bicicleta(id_bicicleta)
        if not bicicleta:
            return None
        for key, value in kwargs.items():
            # solo actualiza si el campo existe y el valor no es None
            if key in bicicleta and value is not None:
                bicicleta[key] = value
        return bicicleta
    
if __name__ == "__main__":
    #Pruebas

    # Aregar Bicicleta
    print("Añadir bicicleta seleccionado")
    id_bicicleta = int(input("Ingrese el ID de la bicicleta: "))
    tipo_bicicleta = input("Ingrese el tipo de bicicleta: ")
    marca = input("Ingrese la marca: ")
    color = input("Ingrese el color: ")
    fecha_compra = input("Ingrese la fecha de compra (DD/MM/AAAA): ")
    numero_marco = input("Ingrese el número de marco: ")

    bici = Bicicletas()
    resultado = bici.agregar_bicicleta(id_bicicleta, tipo_bicicleta, marca, color, fecha_compra, numero_marco)
    print(resultado)  # Output: Bicicleta agregada exitosamente

    #Editar Bicicleta
    print("Editar bicicleta seleccionado")
    id_bicicleta_editar = int(input("Ingrese el ID de la bicicleta a editar: "))
    nueva_marca = input("Ingrese la nueva marca: ")
    resultado_editar = bici.editar_bicicleta(id_bicicleta_editar, marca=nueva_marca)