
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

El archivo packages.sty debe lucir así 
```
\ProvidesPackage{packages}

\usepackage[utf8]{inputenc}
\usepackage[spanish, activeacute]{babel}

% configuracion 
\marginsize{3cm}{2cm}{2cm}{2cm}

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

El documento se puede dividir por secciones de tal manera que se muestren de forma jerárquica en el indice. 
 
 - Parte: \part ( body y report) -1
 - Parte: \part ( Article ) 0
 -  Capítulo: \chapter 0
 - Apéndice: \appendix, \chapter 0
 -  Sección: \section 1
 - Subsección: \subsection 2 
 - Subsubsección: \subsubsection 3 
 - Párrafo: \paragraph 4 
 - Subpárrafo: \subparagraph 5

- Para construir el indice se utiliza ``\tableofcontents``
- Para indicar las secciones que aparecerán en el indice se utiliza el comando 
	``\setcounter{tocdepth}{nivel}``
- Podemos utilizar un nombre alternativo que aparecerá en la cabecera y en el indice. Es útil para nombres muy largos
	``\section[nombre corto]{nombre muy largo}``
- También se pueden crear secciones no numeradas y que no aparecerán en el indice ``\section*{No numerada}``
#### inport
Se pueden importar diferentes documentos como .tex .pdf . estos se agregaran dentro del documento

``\input{filename.tex}``
 
#### Texto
- Saltos de linea ``\\``
- Notas al pie ``\footnote{Texto de la nota al pie}``
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
Podemos agregar las imágenes de forma simple 
```  
% Agregar a la sección de preambulo
\usepackage{graphicx}

% Agrega un directorio de imagenes
\graphicspath{ {./images/} }

% Dentro de la sentencia figure o del documento
\includegraphics{imagen}
```

Ademas podemos modificar el tamaño de la imagen por ejemplo :
```
% Escala la imagen un porcentaje y mantiene su aspecto, ademas la rota
\includegraphics[scale=.15, angle=90]{img/rule90.png}


% Para agregar dimensiones maximas se utiliza el paquete
% \usepackage[export]{adjustbox}

% Escala la imagen a dimensiones maximas, si la imagen no las sobrepasa no tiene transformaciones 
\includegraphics[max width=200mm ,max height=200 mm , keepaspectratio]{img/rule90.png}
```
También podemos agregar las imágenes dentro de la sentencia **figure** este objeto nos permite agregar imágenes, posicionarlos dentro del documento, agregar títulos y referencias .

```
\begin{figure}[h]
    % Alineacion 
    \centering
    % Se agrega el contenido 
    \includegraphics{universe}
    % Pie de imagen
    \caption{Texto dentro de la imagen}
    % Label para hacer referencias dentro del texto
    \label{fig:label}
\end{figure}
```
#### Tablas

Tablas en linea
[ ]: https://www.tablesgenerator.com


Al igual que las figuras las tablas pueden tener titulo, alineación, referencias. Se utilizara el comando tabular para  crear las filas y columnas.  

- Dentro de los corchetes de tabular se define el número de columnas mediante letras. cada letra es una columna y representa la justificación del texto dentro de la tabla **l,c,r**.  Con | se agregan lineas para separar columnas.

- Para separar las columnas se utiliza el símbolo & y para  agregar filas se utilizan ``\\`` al final de las columnas
- Para agregar una linea horizontal se utiliza ``\hline``  

```
\begin{table}[h]
    \centering
    \begin{tabular}{l|c}
        \hline
        Columna 1 & Columna 2  \\ \hline
        Texto & Texto  \\hline 
    \end{tabular}
    \caption{titulo}
    \label{tab:my_label}
\end{table}
```

Como hemos visto **table** y **figure** son muy parecidos
Podemos controlar la forma en que se posicionara en el texto 

| identificador | Descripción |
|----------------|------------|
|h |Coloque el flotador aquí, es decir, aproximadamente en el mismo punto en que aparece en el texto fuente (sin embargo, no exactamente en el lugar) |
|t | Posición en la parte superior de la página. |
|b | Posición al final de la página. |
| H | Coloca el objeto exactamente en la ubicación del código LaTeX. Requiere el paquete flotante, ``\usepackage{float}``

Ademas podemos utilizar tabular para para ordenar las imágenes dentro de la figura a modo de tablas

```
        \begin{figure}[H]
            \centering
            \label{caoticos}
            \begin{tabular}{ll}
                \hline
                \includegraphics{img/r30.png}
                &
                \includegraphics{img/r45.png}
				\\ 
				\hline
            
            \caption{Caption}
        \end{figure}
```
##### Citar dentro del texto
Latex nos permite hacer referencias dentro del texto. No solo podemos reverenciar tablas o figuras, sino cualquier lugar del texto donde podamos insertar el comando 
``\label{etiqueta}``
Y podemos referenciar el elemento con ``\ref{etiqueta}`` o ``\pageref{etiqueta}`` 

##### Listas de contenido 
  
  Latex nos permite crear listas de figuras y contenido. 
  ```
  \listoffigures
  \clearpage
  
  \listoftables
  \clearpage
  ```
### Ecuaciones

- Herramienta para buscar símbolos 
[]:http://detexify.kirelabs.org/classify.html

- Herramienta para crear ecuaciones 
[]: https://www.codecogs.com/latex/eqneditor.php?lang=es-es
Latex posee instrucciones dedidacas a crear texto matemático. 
- Pueden escribirse formulas dentro del texto ``$ ax+by+c=0 $``
- Pueden escribirse adjuntando un salto de linea ``$$ \frac{a}{b}=\frac{c}{d} $$``
- O pueden escribirse como ecuaciones. Estas son numeradas.
```
begin{equation*}
	ax+by+c=0
\end{equation*}

```
 

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

### Referencias
Existen varias formas de referencia dentro de un documento. Podemos usar el paquete ``\usepackage{natbib}
``
Usualmente la información de la bibliografía se almacena en un archivo tipo BibText. Este es parecido a un JSON y también divide los documentos en clases : Libros, revistas, tesis, reportes, patentes... 
También es importante indicarle a Latext el tipo de bibliografía o forma de citar que utilizara. 
```    
% estilo IEEE
\bibliographystyle{IEEEtranN}
& Archivo BibText
\bibliography{cite.bib}
```
 Ejemplos de documentos en BoibText
 ```
 %%% Articulo
 @article
{   adamanstky2013-OnCreativity,
    Title = {On Creativity of Elementary Cellular Automata},
    Journal = {Complex Systems},
    Author = {A. Adamatzky and A. Wuensche},
    Volume = {22},
    Number = {4},
    Year = {2013}    
}

%%% Libro
@book
{
McIntosh2009-OneDimensionalCA,
Author ={H. McIntosh },
Title={One Dimensional Cellular Automata},
Publisher = {Luniver Press },
Year = {2009}
}

%%% Tesis de doctorado
@phdthesis
{
    Seck2002-Phd-AnalisisTopo,
	Author = {J. Seck Tuoh},
	Title = {Análisis dinámico y topológico de los autómatas celulares unidimensionales reversibles},
	school ={Centro de Investigación y de Estudios Avanzados del IPN}, 
  year =         {2002}
	}	
	
	
%%% URL
@misc{
    Feldman-scallingFractales,
	Author = {D. Feldman},
	Title = {Exploring the Sierpi{\'n}ski triangle},
	note = {Last accessed 4 May 2019},
	url = {https://www.youtube.com/watch?v=4I-mvjYtl2k}
	}
 ```

La forma que tenemos para citar dentro del texto es mediante el comando cite
```\cite{Seck2002-Phd-AnalisisTopo}```
 
# Paquetes comunes
- \usepackage{amssymb,amsmath,amsthm}
- \usepackage{anysize}
\usepackage{appendix}
- \usepackage{array,longtable}
- \usepackage[spanish]{babel}
	El paquete Babel permite utilizar caracteres especiales y también traduce algunos elementos dentro del documento. También activa automáticamente las reglas de separación de sílabas apropiadas para el idioma que elija.
- \usepackage{colortbl}
- \usepackage{enumerate}
- \usepackage{float}

- \package{geometry}
 ![Layout-dimensions.png](https://sharelatex-wiki-cdn-671420.c.cdn77.org/learn-scripts/images/f/fc/Layout-dimensions.png)
```
\usepackage{geometry}
\geometry{
 letterpaper,
 landscape,
 twoside,
 left=10mm,
 right =10mm,
 top=15mm
 }
```
- \usepackage{hyperref}
- \usepackage{import}
	
 - \usepackage[utf8]{inputenc}
  Con esta instrucción se le indica a látex que codificación debe utilizar. Se agrega utf8 para añadir acentos.
  
- \usepackage{listings}
	Paquete que permite la inserción de código dentro del texto. Este paquete tiene formato para varios lenguajes de programación y el estilo puede personalizarse 

- \usepackage{mathtools}
- \usepackage{multirow, array} 

- \usepackage{setspace}
- \usepackage{subfig}
- \usepackage{svg}

 
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEzMjg2OTI5OCwtNzM3MzU5NDg5LDQxNT
Y3Njg5OCwtMjEyNzQ0MjEyOCwtNjc2MDc5NjksMTkxNzg5MjYz
NCwtNjgyODU0MjQsLTE1MzYzNzQ1MDQsLTEzNzE3MjUwMDEsLT
E4NzQ3NDc1MDUsLTE5OTQ0NTc4OTIsLTIwMDU2NTA1MzMsMjg3
NzIxNzI0LC0yMDI5NDg2MTgwLDMyNDkxNTcwMCwtMTA1MjUyNz
E4MiwtNzY4NTgwOTYxLDEzMjI4MDIzMTYsMTUyODM3MDIzMCwt
MTIzMDA4Nzk1NV19
-->