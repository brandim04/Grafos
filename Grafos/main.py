from grafo import Grafo

g = Grafo(direcionado=False)  # Agora grafo não direcionado

g.adicionar_aresta("A", "B", 3)
g.adicionar_aresta("A", "C", 5)
g.adicionar_aresta("B", "D", 2)
g.adicionar_aresta("B", "E", 4)
g.adicionar_aresta("C", "E", 1)
g.adicionar_aresta("C", "F", 7)
g.adicionar_aresta("D", "F", 6)
g.adicionar_aresta("E", "F", 2)

print("Grafo atualizado:")
g.imprimir()

# Visualizar grafo
g.visualizar()