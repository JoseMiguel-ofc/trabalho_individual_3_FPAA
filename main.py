# main.py
class Graph:
    def __init__(self, vertices, directed=False):
        """
        Inicializa um grafo com o número especificado de vértices.
        
        Args:
            vertices (int): Número de vértices no grafo
            directed (bool): Define se o grafo é direcionado (True) ou não direcionado (False)
        """
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.directed = directed
    
    def add_edge(self, u, v):
        """
        Adiciona uma aresta ao grafo entre os vértices u e v.
        
        Args:
            u (int): Vértice de origem
            v (int): Vértice de destino
        """
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)  # Para grafos não direcionados, adiciona a aresta bidirecional
    
    def is_safe(self, v, pos, path):
        """
        Verifica se o vértice v pode ser adicionado na posição 'pos' do caminho hamiltoniano.
        
        Args:
            v (int): Vértice a ser verificado
            pos (int): Posição atual no caminho
            path (list): Caminho parcial construído até agora
            
        Returns:
            bool: True se for seguro adicionar o vértice, False caso contrário
        """
        # Verifica se o vértice já está no caminho
        if v in path:
            return False
            
        # Verifica se existe uma aresta entre o vértice anterior e o vértice atual
        if pos > 0 and v not in self.graph[path[pos-1]]:
            return False
            
        return True
        
    def hamiltonian_path_util(self, path, pos):
        """
        Função auxiliar recursiva que utiliza backtracking para encontrar um caminho hamiltoniano.
        
        Args:
            path (list): Caminho parcial construído até agora
            pos (int): Posição atual no caminho
            
        Returns:
            bool: True se um caminho hamiltoniano for encontrado, False caso contrário
        """
        # Se todos os vértices estiverem incluídos no caminho
        if pos == self.V:
            return True
            
        # Tenta diferentes vértices na próxima posição
        for v in range(self.V):
            # Verifica se é possível adicionar o vértice v no caminho
            if self.is_safe(v, pos, path):
                path[pos] = v
                
                # Recursivamente constrói o resto do caminho
                if self.hamiltonian_path_util(path, pos + 1):
                    return True
                    
                # Se adicionar o vértice v não levar a uma solução, remove-o (backtracking)
                path[pos] = -1
                
        return False
        
    def find_hamiltonian_path(self):
        """
        Encontra um caminho hamiltoniano no grafo, se existir.
        
        Returns:
            list: Um caminho hamiltoniano se existir, lista vazia caso contrário
        """
        # Inicializa o caminho com -1 para todas as posições
        path = [-1] * self.V
        
        # Tenta o caminho a partir de cada vértice
        for start in range(self.V):
            # Reinicializa o caminho
            path = [-1] * self.V
            path[0] = start
            
            if self.hamiltonian_path_util(path, 1):
                return path
                
        return []
        
def main():
    """
    Função principal para testar o algoritmo de caminho hamiltoniano
    """
    # Exemplo 1: Grafo com caminho hamiltoniano
    print("Exemplo 1: Grafo com caminho hamiltoniano")
    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(0, 3)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(2, 4)
    g1.add_edge(3, 4)
    
    path = g1.find_hamiltonian_path()
    if path:
        print(f"Caminho hamiltoniano encontrado: {path}")
    else:
        print("Não existe caminho hamiltoniano neste grafo.")
    
    # Exemplo 2: Grafo sem caminho hamiltoniano
    print("\nExemplo 2: Grafo sem caminho hamiltoniano")
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    # Este grafo não possui uma aresta conectando o vértice 2 ao vértice 3
    
    path = g2.find_hamiltonian_path()
    if path:
        print(f"Caminho hamiltoniano encontrado: {path}")
    else:
        print("Não existe caminho hamiltoniano neste grafo.")
        
    # Exemplo 3: Grafo direcionado com caminho hamiltoniano
    print("\nExemplo 3: Grafo direcionado com caminho hamiltoniano")
    g3 = Graph(5, directed=True)
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 3)
    g3.add_edge(3, 4)
    
    path = g3.find_hamiltonian_path()
    if path:
        print(f"Caminho hamiltoniano encontrado: {path}")
    else:
        print("Não existe caminho hamiltoniano neste grafo.")

if __name__ == "__main__":
    main()
