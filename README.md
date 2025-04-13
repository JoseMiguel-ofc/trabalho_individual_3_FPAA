# trabalho_individual_3_FPAA

# Caminho Hamiltoniano - Algoritmo em Python

Este projeto implementa um algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado. Um Caminho Hamiltoniano é um caminho que visita cada vértice de um grafo exatamente uma vez.

## Descrição do Projeto

### Algoritmo Implementado

O algoritmo implementado utiliza a técnica de backtracking para encontrar um Caminho Hamiltoniano em um grafo. O backtracking é um método algorítmico que constrói uma solução incrementalmente, removendo candidatos assim que determina que eles não podem levar a uma solução válida.

### Implementação Linha por Linha

1. **Classe Graph**: Representa um grafo usando lista de adjacências.
   - O construtor `__init__` inicializa o grafo com um número específico de vértices e define se é direcionado.
   - `add_edge` adiciona arestas entre os vértices, considerando a direcionalidade do grafo.

2. **Verificação de Segurança (`is_safe`)**: 
   - Verifica se é seguro adicionar um vértice ao caminho em construção.
   - Examina se o vértice já foi visitado (não pode aparecer duas vezes em um caminho hamiltoniano).
   - Verifica se existe uma aresta entre o último vértice adicionado e o vértice atual.

3. **Função Auxiliar Recursiva (`hamiltonian_path_util`)**:
   - Implementa a lógica de backtracking para construir o caminho.
   - Se todos os vértices foram incluídos (pos == V), retorna True.
   - Tenta diferentes vértices na próxima posição.
   - Se adicionar um vértice não leva a uma solução, desfaz a escolha (backtracking).

4. **Encontrar Caminho Hamiltoniano (`find_hamiltonian_path`)**:
   - Tenta iniciar o caminho a partir de cada vértice do grafo.
   - Para cada vértice inicial, chama a função auxiliar recursiva.
   - Retorna o caminho encontrado ou uma lista vazia se não existir solução.

5. **Função Principal (`main`)**:
   - Cria exemplos de grafos e testa o algoritmo em cada um deles.
   - Exibe os resultados obtidos.

## Como Executar o Projeto

1. Certifique-se de ter Python 3.x instalado em seu sistema.
2. Clone este repositório:
   ```
   git clone https://github.com/JoseMiguel-ofc/trabalho_individual_3_FPAA.git
   ```
3. Navegue até o diretório do projeto:
   ```
   cd caminho-hamiltoniano
   ```
4. Execute o programa:
   ```
   python main.py
   ```

## Relatório Técnico

### Classes de Complexidade (P, NP, NP-Completo, NP-Difícil)

O problema do Caminho Hamiltoniano se enquadra nas seguintes classes:

1. **NP**: O problema está em NP porque dada uma solução (um caminho), é possível verificar em tempo polinomial se esse caminho é um Caminho Hamiltoniano válido (visita cada vértice exatamente uma vez e as arestas entre vértices consecutivos existem).

2. **NP-Completo**: O problema do Caminho Hamiltoniano é NP-completo. Isso significa que é um dos problemas mais difíceis na classe NP, e qualquer problema em NP pode ser reduzido ao problema do Caminho Hamiltoniano em tempo polinomial.

3. **NP-Difícil**: Como é NP-Completo, também é NP-Difícil, pois todos os problemas NP-Completos são NP-Difíceis.

**Justificativa**: O problema do Caminho Hamiltoniano é equivalente ao problema do Caixeiro Viajante sem a restrição de retornar ao ponto inicial. O Problema do Caixeiro Viajante é conhecido por ser NP-Difícil. A redução entre esses problemas pode ser feita em tempo polinomial, confirmando que o Caminho Hamiltoniano é NP-Completo.

### Análise da Complexidade Assintótica de Tempo

A complexidade temporal do algoritmo implementado é **O(n!)** no pior caso, onde n é o número de vértices do grafo.

**Método de Determinação**:
- A complexidade foi determinada através da análise do algoritmo de backtracking:
  - No primeiro nível da recursão, temos n escolhas para o vértice inicial.
  - No segundo nível, temos (n-1) escolhas (todos os vértices exceto o primeiro).
  - No terceiro nível, temos (n-2) escolhas, e assim por diante.
- Isso resulta em um limite superior de n*(n-1)*(n-2)*...*1 = n! operações no pior caso.

### Aplicação do Teorema Mestre

O Teorema Mestre não é diretamente aplicável a este algoritmo porque:

1. O algoritmo de backtracking utilizado não segue a forma padrão T(n) = aT(n/b) + f(n) exigida pelo Teorema Mestre.
2. Não há divisão do problema em subproblemas de tamanho igual (requisito para aplicação do Teorema Mestre).
3. O algoritmo explora diferentes possibilidades em cada nível da recursão, resultando em uma árvore de recursão não balanceada.

### Análise dos Casos de Complexidade

#### Pior Caso: O(n!)
- Ocorre quando o grafo é completo (todos os vértices conectados entre si) e o algoritmo precisa explorar quase todas as permutações possíveis.
- Também ocorre quando o grafo não possui um Caminho Hamiltoniano, pois todas as possibilidades precisam ser verificadas antes de concluir que não existe solução.

#### Caso Médio: O(n!)
- A complexidade média tende a ser exponencial, mas geralmente menor que O(n!).
- Depende da estrutura do grafo e das heurísticas de poda utilizadas.

#### Melhor Caso: O(n²)
- Ocorre em situações muito específicas, como quando o grafo tem um caminho óbvio (por exemplo, um caminho onde cada vértice tem exatamente um sucessor não visitado).
- Neste caso, o algoritmo encontra a solução rapidamente, mas ainda precisa verificar as conexões.

#### Impacto no Desempenho

Estas diferenças de complexidade têm impactos significativos:
- Para grafos pequenos (até 15-20 vértices), o algoritmo funciona bem mesmo no pior caso.
- Para grafos maiores, o desempenho degrada rapidamente devido à natureza exponencial.
- Em aplicações práticas, heurísticas adicionais são frequentemente implementadas para melhorar o desempenho em casos médios, como ordenar vértices por grau ou usar técnicas de poda mais sofisticadas.
- O problema sendo NP-completo significa que não há solução eficiente (polinomial) conhecida que funcione para todos os casos, justificando a abordagem de backtracking apesar de sua complexidade exponencial.
