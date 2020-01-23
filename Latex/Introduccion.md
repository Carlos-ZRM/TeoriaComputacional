
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
- Papeeria
- Datazar

## Estructura de un documento
LatTex funciona mediante instrucciones. Las instrucciones pertenecen a un paquete de Latex y algunas instrucciones pueden recibir parámetros. 
Estas instrucciones inician con el símbolo ```\instrucción``` o pueden iniciar con las sentencias: 
```
\begin{instrucción}[parametros]
	...
\end{instrucción}
```

### Preambulo
La primera instrucción indica la clase del documento que el motor creará 

```\documentclass{aticle}```
#### Diferentes tipos de clases

| Clase | Resumen |
--------| --------|
|**article** | Para artículos académicos y otros documentos cortos que no es necesario dividir en capítulos, sino que bastan las secciones y subsecciones y sus párrafos y subpárrafos.
| **book** | Para libros y otros documentos más largos que deben incluir capítulos, prólogo, apéndices o incluso partes. |
| **report** | Para informes técnicos. Es similar a la clase  `book`. |
| **beamer** | Otra clase para presentaciones mediante diapositivas. |

En el preambulo se suelen indicar los paquetes que se usaran dentro del documento. Así como instrucciones que nos permiten darle formato al documento.  
```
\documentclass{aticle}

% Este paquete proporciona una interfaz para modificar las dimensiones de la página.
\usepackage{geometry}

% Se especifica el tamaño de la pagina y los margenes
\geometry{legalpaper, margin=2in}

```

También es posible escribir los paquetes en un archivo terminacion **.sty** e importarlo en el documento principal
 ```
\documentclass{aticle}
% Agregamos el archivo packages.sty al directorio raiz
\usepackage{packages}
```

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

``\input{filename.tex}``
 
#### Texto
- Saltos de linea ``\\``

El texto puede tener varias decoraciones. entre ellas

- Palabras en itálicas ``\textit{Palabras en italicas}``
- Palabras resaltadas ``\textbf{Palabras resaltadas}``
- Palabras subrayadas ``\underline{underlined words}``
- Se puede encapsular los decoradores por ejemplo
 ``\underline{\textit{\textbf{Negrita, italica y subrayada}}}``

- Tamaño
En cuanto al tamano de la letra este puede definrse al inicio del documento, mediante una sentencia o en un bloque. 

	 - Desde la instruccion de la clase del documento 
	``\documentclass[12 pt]{article}`` 		
	- Desde la instruccion
		- \tiny 
		- \scriptsize 
		- \footnotesize 
		- \small 
		- \normalsize 
		- \large 
		- \Large 
		- \LARGE 
		- \huge 
		- \Huge
	- Al modificar el tamanio de letra en la clase del documento se modifica \normalsize por lo que todas las demas sentencias tambien lo hacen
	- El tamanio de la letra por default varia dependiendo del tipo de documento
	- Al utilizar un comando modifica el tamanio del resto del documento hasta que termine o hasta que otra sentencia lo modifique
	- Para solo modificar algunas lineas del documento pueden encerrarse entre corchetes `` {\LargeTexto Largo}``


### Figuras y tablas
#### Listas
Podemos indicar el elemento grafico para crear listas, pero normalmente utilizamos **itemize** y **enumerate** . Estas pueden anidarse.

```
\begin{enumerate}
    \item Uno 
        \begin{itemize}
            \item Elemento
            \item Elemento  
        \end{itemize}
        
    \item Dos
\end{enumerate}
```
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
 
# Paquetes comunes

- \package{geometry}
 ![Layout-dimensions.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/f/fc/Layout-dimensions.png)

- \usepackage[spanish]{babel}
	El paquete Babel permite utilizar caracteres especiales y también traduce algunos elementos dentro del documento. También activa automáticamente las reglas de separación de sílabas apropiadas para el idioma que elija.
	
 - \usepackage[utf8]{inputenc}
  Con esta instrucción se le indica a látex que codificación debe utilizar. Se agrega utf8 para añadir acentos.
  
- \usepackage{listings}
	Paquete que permite la inserción de código dentro del texto. Este paquete tiene formato para varios lenguajes de programación y el estilo puede personalizarse 
	

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMyMjgwMjMxNiwxNTI4MzcwMjMwLC0xMj
MwMDg3OTU1LDEzNDYxNzIwNzIsMTg0MjkzMjY5MiwtMjAxMzcz
NTUxMywtMTEyNDEzMjg5MCwxNzg2MTc3MDgzLDIwNzk3NjA5MT
ksMTY4NDY2MzA0NSwtMzk3MzYwMzQzLDEwMDM0NjI5NjMsMTI3
NzA0NjU2NSwxMzk4ODU4NDA5LC0xNzA5NTc4MzQsLTgyNjYxNj
MxMSwtMTk1ODg0MzI2NCwtMTI1MTY2OTYwMCw5MTMyNDc4LDQ0
MDE2MDUxMV19
-->