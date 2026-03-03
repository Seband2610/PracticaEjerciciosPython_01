precio=float(input("Ingrese el precio del producto: "))
if precio>100000:
    descuento=precio*0.10
    total=precio-descuento
    print("el total del producto con el descuento es:", total)
else:
    print("El precio del producto es:", precio)

