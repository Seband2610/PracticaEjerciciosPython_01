edad=int(input("ingresa tu edad:"))
estrato=int(input("Ingresa tu estrato:"))
if edad >=18 and edad <=25 and (estrato==1 or estrato==2 or estrato==3):
    print("Aplica para el subsidio")
else:
    print("no aplica")
