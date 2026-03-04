nota1=float(input("Ingresa tu primera nota:"))
nota2=float(input("ingresa tu segunda nota"))
nota3=float(input("ingrsa tu tercera nota"))
promedio=(nota1+nota2+nota3)/3
if promedio>59:
    print("aprobo")
elif promedio >=55 and promedio <=59:
    print("habilito")
else:
    print("reprobo")

