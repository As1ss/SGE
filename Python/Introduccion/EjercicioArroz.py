#ArrozDificil
j=1

for i in range(1,65):
    print(f"Dia {i} Granos: {j}")
    j=j*2
 
#ArrozFacil
def arrozFacil(num:int):
    return 2**(num-1)

#ArrozConCosas



def arrozAcumulado(num:int):
    j=1
    suma=0
    for i in range(1,num+1):
        suma+=j
        j=j*2
       
        
    return suma
print(str(arrozAcumulado(4)))

    
