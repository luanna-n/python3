for n in range(5):
    print(n)

for n in range(0,20,4):
    print(n)


burgers = ["beef", "chicken", "veg", "supreme", "double"]

for n in range(len(burgers)):
    print(n, burgers[n])

for n in range(len(burgers)-1, -1, -1):
    #inicia em double[4], termina em beef (inclusive), anda -1 até o início (inverte a ordem)
    print(n, burgers[n])