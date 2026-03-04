ancho=float(input("ingresa el ancho del cuarto en metros:"))
largo=float(input("ingresa el largo del cuarto en metros:"))
area=ancho * largo 
if area<12:
    print("es pequeño")
elif area>=12 and area<=20:
    print("es mediano")
else:
    print("es grande")