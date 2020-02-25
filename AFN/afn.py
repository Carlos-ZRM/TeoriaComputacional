import networkx as nx
import matplotlib.pyplot as plt
class AFD :
  def __init__(self,q, sigma, q0,aceptacion,fi):
    """
        __init__ (): Inicializa los atributos de la clase 
        self : representa la instancia de la clase.
            - Los métodos de la clase tienen como primer parámetro
            slf. Python sabe que instancia usar
            - Los atributos se definen con self.atributo dentro del
            método init 
    """
    self.q=q
    self.sigma = sigma
    self.q0= q0
    self.aceptacion= aceptacion
    self.fi=fi

    """
    Función que permite saber si una palabra pertenece al lenguaje
    
    1 - el estado inicial sera el primer estado actual qA
    2 - Leer cada letra de la palabra
        2.1 - actualizar el estado actual con el resultado de la función
            de transición
    3 - Válidar si el último estado qA pertenece a los estados finales 
    Parameters
    ----------
    word : str 
        Palabra leída 

    Attributes
    ----------
    qA: estado actual del autómata

    Returns

    bool
        La palabra pertenece al lenguaje del autómata

    """
  def automata(self, word):
    # 1 Definimos el estado actual como el estado q0 del automata
    qA = self.q0
    # 2 recorrer cada letea de la palabra
    for w in word:
      #El estado actual cambia conforme al siguiente caracter leido
      qA = self.transicion(qA,w)

    if qA in self.aceptacion:
      print("La palabra ",word, "SI pertenece al lenguaje")
      return True
    else : 
      print("La palabra ",word, "No pertenece al lenguaje")
      return False

    """
    Función de transición del automata 
        qA = d(qA, se)
    
    Parameters
    ----------
    qA : int 
        estado actual
    se : letra leída 

    Attributes
    ----------
    qA: estado actual del autómata

    Returns

    bool
        La palabra pertenece al lenguaje del autómata

    """
  def transicion(self, qA, se):
    #Obtiene el indice del simbolo de entrada en sigma
    indice= self.sigma.index(se)
    # Se obtiene el estado , se considera que los estados están ordenados
    qR=self.fi[qA][indice]
    return qR

  def hacerGrafo(self):
    G = nx.DiGraph()
    G.add_nodes_from(self.q)
    c = 0
    for f in self.fi:
        for e in f:
            if e is not None:
                print(str(c)+" "+str(e))
                G.add_edge(c, e)
        c=c+1
    nx.draw(G, pos= nx.kamada_kawai_layout(G), with_labels=True, font_weight='bold')
    plt.show()
# Conjunto de estados
q = [0,1,2]
# Alfabeto
sigma = ['0','1']
# Estado inicial
q0=0
# Conjunto de estados posibles
aceptacion=[1]
# Funcion de transicion 
fi=[[2,0],
    [1,1],
    [2,1]
   ]
word= '1110111'

afd = AFD(q, sigma, q0,aceptacion,fi)
a = afd.automata(word)
afd.hacerGrafo()
