
# GraphLib

**GraphLib** é uma biblioteca **Python** para manipulação e visualização de grafos, desenvolvida como parte de um projeto acadêmico. Esta biblioteca oferece uma estrutura leve para criação, manipulação e análise de grafos direcionados e não direcionados.

## 📦 Funcionalidades

A classe principal `Graph` permite:

- Criação de grafos com lista de adjacência.
- Adição de arestas direcionadas e não direcionadas.
- Cálculo de grau de entrada e saída.
- Busca em largura (BFS) e profundidade (DFS).
- Cálculo de densidade.
- Verificação de:
  - Grau mais alto de entrada e saída.
  - Se o grafo é **completo**.
  - Se o grafo é **regular**.
  - Se um grafo é subgrafo de outro.
- Geração do **grafo complementar**.

## 📂 Estrutura do Projeto

```
GraphLib/
├── graph.py    # Implementação da classe Graph
├── main.py     # Exemplo de uso da biblioteca
└── README.md   # Este arquivo
```

## ▶️ Exemplo de Uso

```python
from graph import Graph

g = Graph(5)
g.add_undirected_edge(0, 1)
g.add_undirected_edge(0, 2)
g.add_undirected_edge(1, 3)

print("Lista de adjacência:", g.adj_list)
print("BFS a partir do nó 0:", g.bfs(0))
print("DFS a partir do nó 0:", g.dfs(0))
print("Densidade:", g.density())
print("É regular?", g.regular())
```

## 📌 Observações

- A biblioteca **não depende de bibliotecas externas**.
- O arquivo `main.py` serve como exemplo de uso e teste básico.
- É possível estender a classe para incluir pesos, nomes de vértices e algoritmos mais avançados.

## 🚀 Possíveis Melhorias Futuras

- Suporte a grafos ponderados.
- Implementação de algoritmos como Dijkstra, Floyd-Warshall, e Kruskal.
- Adição de testes automatizados.
- Visualização gráfica dos grafos.

