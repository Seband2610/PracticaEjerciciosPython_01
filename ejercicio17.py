kilometros=float(input("Ingresa el numero de kilometros reccoridos por el taxi "))
tiempo=int(input("ingresa el tiempo que demoro el taxi, escribelo en minutos"))
if tiempo<10:
    cobro=5000

else:
    cobro=800*kilometros 
