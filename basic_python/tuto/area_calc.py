# A área de um círculo

radius = int(input("Entre com o raio do seu circulo (m): "))
area = 3.142 * radius ** 2
print("A area do seu círculo é de: ", area)

#FORMAT METHOD
print("A area do seu círculo é de: {:.2f}".format(area))

#USING F-STRINGS
print(f'A area do seu círculo é de: {area:.3f}')