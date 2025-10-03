el=[]
for x in range(5):
    e = int(input("Ingrese un número: "))
    el=el+[e]
b=int(input("Ingrese un número para saber si esta en lista y ver cuantas veces se repite: "))
if b in(el):
    print("El número", b, "si está en la lista")
    c=el.count(b)
    print("El número", b, "se repite", c, "veces" )
else:
    print("El valor ingresado no existe")