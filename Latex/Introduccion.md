
# Qué es Latex

## Compiladores y aplicaciones

## Estructura de un documento
LatTex funciona mediante instrucciones. Las instrucciones pertenecen a algún paquete de Latex y algunas instrucciones pueden recibir parámetros. 
Estas instrucciones inician con el símbolo ```\instrucción``` o pueden iniciar con las sentencias: 
```
\begin{instrucción}[parametros]
	...
\end{instrucción}
```

### Preambulo

#### \documentclass
#### \usepackage
- \usepackage{listings}
	Paquete que permite la inserción de código dentro del texto. Este paquete tiene formato para varios lenguajes de programación y el estilo puede personalizarse 
#### información del documento
- \title{PlantillaTeoria}
- \author{Carlos - ZRM }
- \date{Enero 2020}
### Cuerpo
Los documentos se inician y cierran entre las instrucciones 
```
\begin{document}
	...
\end{document}
```



### Figuras y tablas

### Código
Se puede utilizar el paquete ``\usepackage{listings}`` .  Se puede agregar el código dentro del documento .tex o se puede agregar desde un archivo. 

- Código agregado desde texto
 
```
\begin{lstlisting}[language=Python] 
	print("Hola Mundo")
\end{lstlisting}
 ```
 - Código agregado desde archivo
``\lstinputlisting[language=Py]{BitXorMatrix.m}``
 
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyODM5MTMxOSw1NjQ3OTgxMDVdfQ==
-->