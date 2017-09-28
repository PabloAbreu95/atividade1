def triangularizar(matriz,aux1,aux2,aux3):
    if matriz[0][0] != 0:
        for i in range(0,len(matriz[0])):
            aux1.append((matriz[0][i]*matriz[1][0]) - (matriz[1][i]*matriz[0][0]))
            aux2.append((matriz[0][i]*matriz[2][0]) - (matriz[2][i]*matriz[0][0]))
        matriz[1] = aux1
        matriz[2] = aux2
    if matriz[1][1] != 0:
        for i in range (0,len(matriz[0])):
            aux3.append((matriz[1][i]*matriz[2][1] - (matriz[2][i]*matriz[1][1])))
        matriz[2] = aux3

    z = matriz[2][3]/matriz[2][2]
    y = (matriz[1][3] - matriz[1][2])/matriz[1][1]
    x = (matriz[0][3] - (matriz[0][1] * y) - (matriz[0][2]*z))/matriz[0][0]

    print('\nMatriz triângularizada\n')
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print("\nx = %d\ny = %d\nz = %d"%(x,y,z))

