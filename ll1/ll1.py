import analizador_lexico
import xlrd
import pandas as pd
import numpy as np
from graphviz import Digraph
dot = Digraph()
filas = {"Inicio"	:1	,
"E"	:2	,
"E'"	:3	,
"DeclaracionFuncion"	:4	,
"FuncionPrincipal"	:5	,
"K"	:6	,
"Parametros"	:7	,
"Y'"	:8	,
"Y"	:9	,
"TipoDato"	:10	,
"C"	:11	,
"CuerpoF"	:12	,
"J"	:13	,
"Cuerpo"	:14	,
"D'"	:15	,
"DeclaracionVariables"	:16	,
"Dc'"	:17	,
"Sentencias"	:18	,
"OPS"	:19	,
"MuchasSentenciasYoyo"	:20	,
"M'"	:21	,
"SentenciasYoyo"	:22	,
"MuchasSentencias"	:23	,
"S'"	:24	,
"DeclaracionVariable"	:25	,
"Corchetes"	:26	,
"OPI"	:27	,
"Expresion"	:28	,
"Ex"	:29	,
"Ex'"	:30	,
"Tx"	:31	,
"Literal"	:32	,
"Op"	:33	,
"ParaLLamados"	:34	,
"PL'"	:35	,
"PL"	:36	,
"Simbolo"	:37
}
columnas={"mision"	:1	,
"identificador"	:2	,
"pizquierdo"	:3	,
"pderecho"	:4	,
"lizquierdo"	:5	,
"lderecho"	:6	,
"llama"	:7	,
"coma"	:8	,
"pinocho"	:9	,
"numero"	:10	,
"decimal"	:11	,
"texto"	:12	,
"chacha"	:13	,
"cizquierdo"	:14	,
"cderecho"	:15	,
"devuelve"	:16	,
"si"	:17	,
"sino"	:18	,
"yoyo"	:19	,
"mostrar"	:20	,
"="	:21	,
"igual"	:22	,
"descansito"	:23	,
"lpinocho"	:24	,
"lnumero"	:25	,
"ltexto"	:26	,
"ldecimal"	:27	,
"lchacha"	:28	,
"verdad"	:29	,
"mentira"	:30	,
"mas"	:31	,
"menos"	:32	,
"por"	:33	,
"o"	:34	,
"y"	:35	,
"mayor_igual"	:36	,
"diferente"	:37	,
"menor_igual"	:38	,
"comparacion"	:39	,
"menor"	:40	,
"mayor"	:41	,
"modulo"	:42	,
"dividir"	:43	,
"$"	:44
}
df = pd.read_excel("tablita.xlsx", 'Hoja1',  header=None)
tablita_parse = df.values

pila = ["Inicio","$"]
entrada = analizador_lexico.tokens
entrada.append("$")

continuar=True
i=0
j=0
p=0
aux=[]
dot.node(str(j), pila[0])
padres=[0,-1]
print("Inicio:")
print(pila)
print(entrada)

while continuar:
  print("Vuelta",i)
  if pila[0]=="$" and entrada[0]=="$":
    continuar=False
    print(pila)
    print(entrada)
    print("Cadena aceptada")
  elif pila[0] == entrada[0]:
    print(pila)
    print(entrada)
    pila = pila[1:]
    entrada.pop(0)
  elif pila[0][0]==(pila[0][0]).lower() and entrada[0][0]==(entrada[0][0]).lower():
    continuar=False
    print(pila)
    print(entrada)
    print("Error: Cadena rechazada")
  else:
    if entrada[0] in columnas:
      reemplazo = tablita_parse[filas[pila[0]]][columnas[entrada[0]]]
      p=int(padres[0])
    else:
      continuar=False
      print(pila)
      print(entrada)
      print("Error: Cadena rechazada")
      break
    if reemplazo == "vacio":
      j=j+1
      h=j
      dot.node(str(h), "''")
      dot.edge(str(p),str(h))
      pila=pila[1:]
      padres=padres[1:]
      print(pila)
      print(entrada)
    else:
      array_aux=reemplazo.split()
      pila = np.concatenate((array_aux,pila[1:]),axis=0)
      hijos = len(array_aux)
      aux.clear()
      for e in range(hijos):
        j=j+1
        if array_aux[e][0]==array_aux[e][0].upper():
          aux.append(j)
        h=j
        dot.node(str(h), array_aux[e])
        dot.edge(str(p),str(h))
      padres = np.concatenate((aux,padres[1:]),axis=0)
      print(pila)
      print(entrada)
  i=i+1
print(dot.source)