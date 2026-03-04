sueldo=float(input("Ingrese su sueldo mensual:"))
if sueldo<1500000:
    impuesto=0

elif sueldo>=1500000 and sueldo<=3000000:
    impuesto=sueldo*0.05
else:
    impuesto=sueldo*0.10
sueldo_neto= sueldo-impuesto

print("el sueldo neto es de",sueldo_neto)
print("El impuesto a pgar es", impuesto)
