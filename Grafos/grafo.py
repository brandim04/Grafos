import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self, direcionado=True):
        self.adj = {}
        self.direcionado = direcionado

    def adicionar_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def adicionar_aresta(self, u, v, peso=1):
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self.adj[u].append((v, peso))
        if not self.direcionado:
            self.adj[v].append((u, peso))

    def remover_aresta(self, u, v):
        if u in self.adj:
            self.adj[u] = [(x, p) for (x, p) in self.adj[u] if x != v]
        if not self.direcionado and v in self.adj:
            self.adj[v] = [(x, p) for (x, p) in self.adj[v] if x != u]

    def remover_vertice(self, v):
        if v in self.adj:
            del self.adj[v]
        for u in self.adj:
            self.adj[u] = [(x, p) for (x, p) in self.adj[u] if x != v]

    def vizinhos(self, v):
        return self.adj.get(v, [])

    def imprimir(self):
        for v in self.adj:
            print(f"{v} -> {self.adj[v]}")

    def visualizar(self):
        """Desenha o grafo usando NetworkX e Matplotlib"""
        if self.direcionado:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        for u in self.adj:
            for v, peso in self.adj[u]:
                G.add_edge(u, v, weight=peso)

        pos = nx.spring_layout(G)  # layout automático
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', font_size=12, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()