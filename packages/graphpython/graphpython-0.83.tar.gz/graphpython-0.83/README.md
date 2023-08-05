# graphpy

This is a package for the manipulation of graphs
made for a class of graphs in the Brazilian university 'Universidade Tecnologica Federal do Paraná'

## Installation

```
pip install graphpython
```

## Complete Documentation

### Graph

to use this class, the main element is `Graph class`. With this class, you will be able to fill the graph with vertex and edges and do all the necessary operations

- `Graph([directed])`: create a graph
    - `directed`: Defaults to False.
                tells if the graph is directed or not

#### Code example

``` python
# Create a new graph
from graphpy.graph import Graph

gp = Graph()
# add a new vertex
gp.add_vertex('vertex1')

# to get the create vertex, you can use the [] operator
vertex1 = gp['vertex1']
```

### Vertex operations

The base of all graph is the vertex, to create a new vertex you got to use the follow functions

- `gp.add_vertex(name, [value])`: create a new vertex and insert to the graph
    - `name`: Unique identification to the vertex inside the graph
    - `value`: optional value to the vertex

- `gp.get_vertex(name)` or `gp[name]`: return the vertex from the graph
    - `name`: Unique identification to the vertex inside the graph

- `gp.get_all_vertex()`: get a list with all vertex from the graph

- `gp.adjacents_vertex(vtx)`: get all adjacent vertex from one vertex
    - `vtx`: vertex you want to know the adjacent

- `gp.remove_vertex(vertex_to_remove)`: Remove a vertex and all the connections he have
    - `vertex_to_remove`: vertex you want to remove

#### Code example

```python
from graphpy.graph import Graph

gp = Graph()
gp.add_vertex('01')
gp.remove_vertex(gp['01'])
```

## Search in the graph

The main class has a search method and to use, you need to pass a by params an strategy to make the search.

#### Implement a new search strategy

In the class has two class strategies already implemented:

- BFSstrategy
- DFSstrategy

```python
from graphpy.graph import Graph
from graphpy.BFSstrategy import BFSstrategy

graph = Graph()
graph.search(BFSstrategy(INITIAL_VERTEX))
```

To extend all the search types you can create a new strategy extending the SearchStrategy class from search_strategy.

```python
from graphpy.search_strategy import SearchStrategy


class DFSstrategy(SearchStrategy):
    def __init__(self):

        self.__predecessors = {}
        self.__firstSee = {}
        self.__close = {}
        self.__time = 0

    def __dfs_visit(self, vertex):
        self.__time = self.__time + 1
        self.__firstSee[vertex] = self.__time
        vertex.set_color(1)

        for adjacent in self.get_adjacent_list()[vertex]:
            if adjacent.get_color() == 0:
                self.__predecessors[adjacent] = vertex
                self.__dfs_visit(adjacent)
        vertex.set_color(2)
        self.__time += 1
        self.__close[vertex] = self.__time

    def search(self):
        # colors:
        #   white: not visited
        #   grey: in the queue
        #   black: nothing more to do
        for key in self.get_adjacent_list():
            # set color for all vertices to white
            key.set_color(0)
            self.__predecessors[key] = None
        self.__time = 0
        for key in self.get_adjacent_list():
            if key.get_color() == 0:
                self.__dfs_visit(key)

        return self.__firstSee, self.__close, self.__predecessors
```