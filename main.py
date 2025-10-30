# Proyecto en Python para gestion de bicicletas
from bicicletas import Bicicletas
import time

#Instancia unica para todo el programa
bici_gestor = Bicicletas()

while True:
    print("Bienvenido al sistema de gestión de bicicletas")
    print("1. Añadir bicicleta")
    print("2. Editar bicicletas")
    print("3. Eliminar bicicletas")
    print("4. Ver todas las bicicletas")
    print("5. Agregar recorridos")
    print("6. Editar recorridos")
    print("7. Ver recorridos")
    print("8. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 8:
            print("Error: Opción inválida. Por favor, seleccione una opción del 1 al 8.")
            continue
    
        match opcion:
            case 1:
                print()
                print("Añadir bicicleta seleccionado")
                print()

                # Lógica para añadir bicicleta
                id_bicicleta = int(input("Ingrese el ID de la bicicleta (Numerico): "))
                tipo_bicicleta = input("Ingrese el tipo de bicicleta (MTB/Ruta/Electrica): ")
                marca = input("Ingrese la marca: ")
                color = input("Ingrese el color: ")
                fecha_compra = input("Ingrese la fecha de compra (DD/MM/AAAA): ")
                numero_marco = input("Ingrese el número de marco: ")
                print()
                resultado = bici_gestor.agregar_bicicleta(id_bicicleta, tipo_bicicleta, marca, color, fecha_compra, numero_marco)
                print(resultado)

                print()
                time.sleep(2)
            case 2:
                print()
                print("Editar bicicletas seleccionado")
                print()
                
                # Lógica para editar bicicletas
                # Pedir ID y validar
                try:
                    id_editar = int(input("Ingrese el ID de la bicicleta a editar: "))
                    print()
                except ValueError:
                    print()
                    print("ID inválido. Debe ser un número.")
                    print()
                    time.sleep(2)
                    continue

                bicicleta = bici_gestor.obtener_bicicleta(id_editar)
                if not bicicleta:
                    print("Bicicleta no encontrada.")
                    print()
                    time.sleep(2)
                    continue

                print("Bicicleta encontrada:")
                print()
                for k, v in bicicleta.items():
                    print(f"{k}: {v}")

                print("\nDeje en blanco para mantener el valor actual.")
                print()
                tipo_n = input(f"Tipo [{bicicleta['tipo_bicicleta']}]: ")
                marca_n = input(f"Marca [{bicicleta['marca']}]: ")
                color_n = input(f"Color [{bicicleta['color']}]: ")
                fecha_n = input(f"Fecha compra [{bicicleta['fecha_compra']}]: ")
                nro_marco_n = input(f"Número marco [{bicicleta['numero_marco']}]: ")
                print()

                cambios = {}
                if tipo_n != "": cambios["tipo_bicicleta"] = tipo_n
                if marca_n != "": cambios["marca"] = marca_n
                if color_n != "": cambios["color"] = color_n
                if fecha_n != "": cambios["fecha_compra"] = fecha_n
                if nro_marco_n != "": cambios["numero_marco"] = nro_marco_n

                actualizado = bici_gestor.editar_bicicleta(id_editar, **cambios)
                if actualizado:
                    print("Bicicleta actualizada:")
                    print()
                    for k, v in actualizado.items():
                        print(f"{k}: {v}")
                else:
                    print("No se pudo actualizar la bicicleta.")

                print()
                time.sleep(2)
            case 3:
                print()
                print("Eliminar bicicletas seleccionado")
                # Lógica para eliminar bicicletas
                print()
                time.sleep(2)
            case 4:
                print()
                print("Ver todas las bicicletas seleccionado")
                # Lógica para ver todas las bicicletas
                print()
                time.sleep(2)
            case 5:
                print()
                print("Agregar recorridos seleccionado")
                # Lógica para agregar recorridos
                print()
                time.sleep(2)
            case 6:
                print()
                print("Editar recorridos seleccionado")
                # Lógica para editar recorridos
                print()
                time.sleep(2)
            case 7:
                print()
                print("Ver recorridos seleccionado")
                # Lógica para ver recorridos
                print()
                time.sleep(2)
            case 8:
                print()
                print("Saliendo del sistema...")
                break
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un número del 1 al 8.")
        continue