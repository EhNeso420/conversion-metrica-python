# 1. Solicitar al usuario las medidas de los muebles en cms

medidas_cms = float(input("Por favor, ingresar las medidas de los muebles en cms: "))

# 2. Convertir las medidas de cms a pulgadas

medidas_pulgadas = medidas_cms / 2.54
medida_redondeada = round(medidas_pulgadas, 2)

# 3. Mostrar el resultado al usuario en pulgadas

print("Las medidas en pulgadas de la pieza ingresada son:", medida_redondeada)