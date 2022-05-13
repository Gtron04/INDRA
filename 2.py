def perm(list,newPer):
    if not list:
        print(newPer)    #  Al final del árbol, envíe el resultado
    else:               # Cuando no haya alcanzado el nodo hoja del árbol, use la recursividad para continuar mirando hacia abajo.
        for i in range(len(list)):
            newPer.append(list[i])
            del list[i]
            perm(list,newPer)
            list.insert(i,newPer.pop())

list=["a","b","c"]
newPer=[]
perm(list,newPer)