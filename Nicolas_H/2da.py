# motor = int(input("Ingrese el estado del motor "))
# if motor >= 80:
#     print("El motor está encendido")
# else:
#     print("El motor está apagado")

# numero = int(input("Ingresa un número: "))
# print(f"Tabla de multiplicar del {numero}:")
# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

# cont = 'S'
# while cont.upper() == 'S':  
#     n1 = int(input("Ingrese el número para ver su tabla de multiplicar: "))
#     print(f'TABLA DEL {n1}:')
#     n2 = 1
#     while n2 < 11:
#         r = n1 * n2
#         print(f'{n1} * {n2} = {r}')
#         n2 += 1
#     print('¿Desea continuar? S/N')
#     cont = input()  

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

suma_listas = []

for a, b in zip(lista1, lista2):
    suma_listas.append(a + b)

print(suma_listas)

