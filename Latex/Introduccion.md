
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
Algu


### Figuras y tablas
#### Figuras
Se pueden agregar las imágenes dentro de la sentencia figure .

``` 
% Agregar a la sección de preambulo
\usepackage{graphicx}

% Agrega un directorio de imagenes
\graphicspath{ {./images/} }

% Dentro de la sentencia figure o del documento
\includegraphics{imagen}
```
### Código
Podemos utilizar el paquete ``\usepackage{listings}`` .   Existen dos opciones para agregar el código: dentro del documento .tex o  desde un archivo. 

- Código agregado desde texto
 
```
\begin{lstlisting}[language=Python, caption= Ejemplo de Hola mundo en Python] 
	def HolaMundo():
		print("Hola Mundo")
\end{lstlisting}
 ```
 - Código agregado desde archivo
```
\lstinputlisting[language=Python, caption= Ejemplo de Hola mundo en Python ]{holaMundo.py}
```
 
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAwMDE0OTkyNiw0NDAxNjA1MTEsNTY0Nz
k4MTA1XX0=
-->