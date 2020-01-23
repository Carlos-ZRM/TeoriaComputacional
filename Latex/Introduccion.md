
# Qué es Latex
TeX es un lenguaje creado por Donald Knuth para escribir documentos de forma atractiva y consistente. Knuth comenzó a escribir el motor de composición tipográfica TeX en 1977,
Si bien TeX es un lenguaje de marcado para describir cómo debe verse su documento. El control fino que ofrece TeX sobre la estructura y el formato del documento lo convierte en una herramienta poderosa y formidable para producir textos académicos, científicos, matemáticos y de ingeniería.

Un **lenguaje de marcado**  es una forma de codificar un documento que, junto con el texto, incorpora Etiqueta o marcas que contienen información adicional acerca de la estructura del texto o su presentación.

## Motores y aplicaciones

Cada motor contiene algunas librerías e implementaciones diferentes. por lo que el resultado de un archivo .tex puede variar

- xetex,  xelatex 
- lualatex
- pdflatex
- tex,  latex

Latex esta disponible en varios sistemas operativos. Por lo que pueden instalar los diversos motores y un IDE de edición. 

- MacTeX
- MiKTeX
- TeX Live

Tambiien existen servicios web que permiten la edición colaborativa, versionamiento, previsualizar y compilar.

- Overleaf

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
#### inport
Se pueden importar diferentes documentos como .tex .pdf . estos se agregaran dentro del documento
\input{filename}


La division de los documentos se realiza a partir de la clase a la que pertenecen, Por ejemplo la division mas grande de las clases book y reportes
 
#### Texto
El texto puede tener varias decoraciones. entre ellas

\textit{Palabras en italicas}
\textbf{Palabras resaltadas}
\underline{underlined words}

- Se puede encapsular los decoradores por ejemplo

\underline{\textit{\textbf{Negrita, italica y subrayada}}}


En cuanto al tamano de la letra este puede definrse al inicio del documento, mediante una sentencia o en un bloque. 
Desde la instruccion de la clase del documento 

\documentclass[12 pt]{article} 

Las sentencias que provee latex son las siguientes

- Al modificar el tamanio de letra en la clase del documento se modifica \normalsize por lo que todas las demas sentencias tambien lo hacen
- El tamanio de la letra por default varia dependiendo del tipo de documento
- Al utilizar un comando modifica el tamanio del resto del documento hasta que termine o hasta que otra sentencia lo modifique
- Para solo modificar lineas del documento pueden encerrarse entre corchetes {\LargeTexto Largo}


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
eyJoaXN0b3J5IjpbLTgyNjYxNjMxMSwtMTk1ODg0MzI2NCwtMT
I1MTY2OTYwMCw5MTMyNDc4LDQ0MDE2MDUxMSw1NjQ3OTgxMDVd
fQ==
-->