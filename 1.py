list=[1,0,0,0,0,1,0,1]
print(list)
print("cantidad de dias")
dias=int(input())
def validar_dias(dias, list):
  if dias or len(list):
    competencia_diaria(dias,list)
  else:
    print(" error de datos de entrada")
  return ()

def competencia_diaria(dias, list):
  
  for x in range(1,dias): # loop para dias  
    valor_anterior=0
    valor_siguiente=0
    
    for k in list: #loop para casas
      valor_siguiente=list[k+1]
      if valor_anterior == valor_siguiente:
          valor_anterior=k
          list[k]==0
      else: 
          valor_anterior=k
          list[k]==1
          
    print(list)            
    return list


print(validar_dias(2, list))









