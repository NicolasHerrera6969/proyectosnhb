# puertos = {22:’SSH’, 23:’Telnet’, 80:’HTTP’, 3306:’MySQL’}
# print (puertos)

# dict_ports1 = {22:"SSH", 80:"Http"}
# dict_ports2 = {53:"DNS", 443:"https"}
# print(dict_ports1)
# dict_ports1.update(dict_ports2)
# print(dict_ports1)

# puertos = {22:"SSH", 23:"Telnet", 80:"HTTP", 3306:"MySQL"}
# print(puertos)
# del puertos[23]
# print(puertos)


# puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
# if 80 in puertos:
# print("yes")
# if 110 not in puertos:
# print("no")
# else:
# print("yes")

# dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
# for key in dict_ports:
#     print(key)}

# dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
# for k, v in dict_ports.items():
#     print(k, "->", v)
    
    
    
# puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
# print(len(puertos))

dict1 = {"a":1, "b":2, "c":3}
print(dict1.get("a"))
print(dict1.get("d", "clave no encontrada."))

