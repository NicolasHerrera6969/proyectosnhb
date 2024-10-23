frutas = {
    'manzana': 'apple',
    'platano': 'banana',
    'naranja': 'orange',
    'fresa': 'strawberry',
    'uva': 'grape',
}

def traducir_fruta(frutas):
    while True:
        fruta = input("Ingrese el nombre de una fruta en español (o 'salir' para terminar): ").lower()
        
        if fruta == 'salir':
            print("Gracias por usar el traductor de frutas!")
            break

        if fruta in frutas:
            print(f"La traducción de '{fruta}' es '{frutas[fruta]}'")
        else:
            opcion = input(f"La fruta '{fruta}' no está en el diccionario. Desea agregarla? (si/no): ").lower()
            if opcion == 'si':
                traduccion = input(f"Ingrese la traducción en inglés para '{fruta}': ").lower()
                frutas[fruta] = traduccion
                print(f"'{fruta}' ha sido agregada al diccionario con la traducción '{traduccion}'")
            else:
                print("No se agregó la fruta.")
                break

traducir_fruta(frutas)
