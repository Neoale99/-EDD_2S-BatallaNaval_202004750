import os
nodos =""
d = ""
dot = ""
rC = "{rank=same;raiz;"
rF = "{rank=same;"
nC = ""
nF = ""
print("ingrese el numero de filas")
y = int(input())
print("ingrese el numero de columnas")
x = int(input())
Filas = "" 
Col  = ""
uF=""
uC=""
for i in range(y):
    Filas+= "F"+str(i+1)+"[label=\""+str(i+1)+"\",group = 1]\n"
    if (i+1==y):
        uF+=""
    else:
        uF+="F"+str(i+1)+"->F"+str(i+2)+"\n"
        uF+="F"+str(i+1)+"->F"+str(i+2)+" [dir=back]\n"

for i in range(x):
    Col+= "C"+str(i+1)+"[label=\""+str(i+1)+"\",group = "+str(i+2)+"]\n"
    if (i+1==x):
        uF+=""
        rC +="C"+str(i+1)+"}\n"
    else:
        rC +="C"+str(i+1)+";"
        uC+="C"+str(i+1)+"->C"+str(i+2)+"\n"
        uC+="C"+str(i+1)+"->C"+str(i+2)+" [dir=back]\n"
#print(Filas+"\n"+Col+"\n"+uF+"\n"+uC+"\n"+rC)

#Aquí se agregará el raiz->F1 raiz->C1 
d+= "raiz->F1 \n raiz->C1 "
#Aquí me quedé
for i in range(y):
    if (i!=0):
      rF +="{rank=same;"

    for j in range(x):
     if (j==0):  #El mimso ciclo pero con i para columnas
       nF+=("F"+str(i+1)+"->n"+str(i+1)+"_"+str(j+1)+"\n")
       nC+=("C"+str(i+1)+"->n"+str(j+1)+"_"+str(i+1)+"\n")
       nC+=("C"+str(i+1)+"->n"+str(j+1)+"_"+str(i+1)+"[dir=back]\n")
       nF+=("F"+str(i+1)+"->n"+str(i+1)+"_"+str(j+1)+"[dir=back]\n")
       nF+=("n"+str(i+1)+"_"+str(j+1)+"->n"+str(i+1)+"_"+str(j+2)+"\n")
       nF+=("n"+str(i+1)+"_"+str(j+1)+"->n"+str(i+1)+"_"+str(j+2)+"[dir=back]\n")
       nC+=("n"+str(j+1)+"_"+str(i+1)+"->n"+str(j+2)+"_"+str(i+1)+"[dir=back]\n")
       nC+=("n"+str(j+1)+"_"+str(i+1)+"->n"+str(j+2)+"_"+str(i+1)+"\n")
     else:
        if (j+1!=x):
          nF+=("n"+str(i+1)+"_"+str(j+1)+"->n"+str(i+1)+"_"+str(j+2)+"\n")
          nF+=("n"+str(i+1)+"_"+str(j+1)+"->n"+str(i+1)+"_"+str(j+2)+"[dir=back]\n")
          nC+=("n"+str(j+1)+"_"+str(i+1)+"->n"+str(j+2)+"_"+str(i+1)+"[dir=back]\n")
          nC+=("n"+str(j+1)+"_"+str(i+1)+"->n"+str(j+2)+"_"+str(i+1)+"\n")
     nodos+="n"+str(i+1)+"_"+str(j+1)+"[label=\""+str(i+1)+","+str(j+1)+"\",group = "+str(j+2)+"]\n"
     if (j+1==y):
       rF+="n"+str(i+1)+"_"+str(j+1)+";F"+str(i+1)+"}"
     else:
       rF+="n"+str(i+1)+"_"+str(j+1)+";"
    rF+="\n"

dot+=(Filas+"\n"+uF+"\n"+Col+"\n"+uC+"\n"+d+"\n"+rF+"\n"+rC+"\n"+nodos+"\n"+nF+"\n"+nC)
print (Filas)
print(uF)
print(Col)
print(uC)
print(d)
print(rF)  
print(rC)
print(nodos)  
print(nF)  
print(nC)  

file = open("datos.txt", "w")
file.write(dot)

file.close()