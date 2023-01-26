from graph import Graph

g1 = Graph(4, adj_list=[])
g1.add_undirected_edge(0, 1)
g1.add_undirected_edge(0, 2)
g1.add_undirected_edge(0, 3)
g1.add_undirected_edge(1, 2)

print("GRAPH 1:", g1.adj_list)
print("DENSITY:", g1.density())
print("DEGREE_OUT(0):", g1.degree_out(0))
print("DEGREE_OUT(1):", g1.degree_out(1))
print("HIGHEST_DEGREE_OUT:", g1.highest_degree_out())
print("DEGREE_IN(0):", g1.degree_in(0))
print("DEGREE_IN(1):", g1.degree_in(1))
print("COMPLEMENT:", g1.complement().adj_list)
