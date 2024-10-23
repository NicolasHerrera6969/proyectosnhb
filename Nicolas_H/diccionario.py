'''X = {} : Le asigna el diccionario vacio a la variable x.
puertos = {22:' SSH', 23:'Telnet', 80: 'HTTP', 3306: 'MySQL'}'''

'''dict_ports1={22:'SSH', 80:'Http'}
dict_ports2={53:'DNS', 443:'Https'}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1)
#pasamos la imformacion de ports2 a ports 1 es como agregar update seria concatenar
a = {123:'Rojas', 87:'Rosas'} == {87:'Rosas', 123:'Rojas'}#TIENEN LOS MISMOS DATOS
print(a)
print({'Rosas':123} != {'rosas':123})#IGUAL VERDADERO PORQUE SON DIFERENTES != 
b = {123:'Rosas', 87:'rojas'} == {'Rosas':123 , 87:'rojas'}#AQUI ES FALSO porque tienen lo mismos datos pero diferente orden
print(b)'''

'''puertos = {22:'SHH', 23: 'Telnet', 80: 'HTTP', 3306: 'MySQL'}#22: es una clave, 23 otra clave 
protocolo = puertos [22]
print(protocolo)
puertos [22]#Con la clave puede acceder al valor (dato) si ingresa 22 podra ingresar a la clave o llave
'''
'''aGREGA
puertos={80:'HTTP', 23:'SMTP', 443:'HTTPS'}
print (puertos)
puertos[23]='Telnet' #esto permite cambiar la clave smtp a telnet
print(puertos)
puertos[110]= 'POP' #este caso agrega una nueva clave en este caso 110 POP
print(puertos)'''

'''ELIMINAr
puertos ={22:'SHH', 23:'Telnet', 80:'HTTP',3306:'MySQL'}
print(puertos)
del puertos[23] #con la funcion del eliminamos la clave 23
print(puertos)'''

'''diccionarios y'''

'''puertos={80:'HHTP',23:'SMTP',443:'HTTPS'}
if 80 in puertos:
    print ('yes')
if 110 not in puertos:
    print('no')
else:
    print('yes')
 #con esta fornula podemos sacar datos del diccionario'''

'''iterar con for

dict_ports = {22:'SHH', 23:'telnet', 80:'Https'}
for key in dict_ports:
    print (key)

#Aqui solamente tiene datos y los pone en orden numerico'''

''' iteRAr diccionARIO

dict_ports = {22:'SHH', 23:'telnet', 80:'HTPP'}
for k,v in dict_ports.items(): #es un ciclo for y items es un metodo para aplicar a ese objeto 
    print (k, '->', v)#escribe la clave y seguido de su contenido sale la flecha y nos da la propiedad de items
#keys es la llave para llamar solo las claves
    #k es key y la v son variables '''

'''longitud nos dice 
puertos ={80:'HTTP', 23:'SMTP', 443:'HTTPS'}
print(len(puertos))'''#len nos dice la cantidad de items que tiene el diccionario 

'''sacar un valor get trAER DATOS metodo

dict1={'a':1, 'b':2, 'c':3}
print(dict1.get('a'))
print(dict1.get('d', 'clave no encontrada.'))'''
#la funcion get llama los datos existentes y si no estan dice que no la encontro

'''max y min obtiene la maxima y minima clave los items en el diccionario'''

'''puertos={80:'HTTP',23:'SMTP', 443:'HTTPS'}
print(max(puertos))
print(min(puertos))'''
#toma las llaves

'''metodo keys valores'''

dict1 = {'a':1, 'b':2, 'c':3}
print(list(dict1.keys()))
print(list(dict1.values()))
