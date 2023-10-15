### Challenge 01
### Shortest Path in a Weighted Graph

from collections import namedtuple, deque
from pprint import pprint as pp
 
inf = float('inf')

def WeightedPath(strArr):

  ### Extract information from input
  number_of_nodes = int(strArr[0])
  nodes = strArr[1:1+number_of_nodes]
  source = nodes[0]
  dest = nodes[-1]
  connections = [(elem.split("|")[0], elem.split("|")[1], int(elem.split("|")[2])) for elem in strArr[1+number_of_nodes:]]

  def dijkstra(source, dest, nodes, connections):

      ### Definition of auxiliary variables
      
      # Dictionary for distances 
      # key: value -> node: accumulated distance from starting node
      dist = {node: inf for node in nodes}
      # Distance at the starting node is zero
      dist[source] = 0

      # Dictionary for saving previous node
      # key: value -> node: previous node
      previous = {node: None for node in nodes}
      
      # Auxiliary list of nodes
      q = nodes.copy()

      # Dictionary for neighbours
      # key: value -> node: (neighbour, distance to neighbor)
      neighbours = {node: set() for node in nodes}
      for start, end, disttn in connections:
          neighbours[start].add((end, disttn))
          neighbours[end].add((start, disttn))


      ### First while cycle
      ### Steps to the closest neighbour, taking into account distance to neighbor. 
      ### Saves the previous neighbor in dictionary previous.
      ### Stops when the current node is the ending node or when ... ADD CASE

      while q:

          # List of available nodes
          pp(q)

          # Current node (node having the smallest distance within the available nodes)
          u = min(q, key=lambda node: dist[node])

          # Remove current node from list of available nodes
          q.remove(u)

          # Condition to exit the while cycle -> arrive to destination node
          if dist[u] == inf or u == dest:
              break

          # Step forward
          for v, disttn in neighbours[u]:
              new_dist = dist[u] + disttn
              if new_dist < dist[v]:                                  # Relax (u,v,a)                  
                  # Updates of dictionaries dist and previous
                  dist[v] = new_dist
                  previous[v] = u


      ### Reconstruct shortest path
      ### The dictionary previous is used for this task

      # Dictionary previous having the correct path
      pp(previous)

      # Define the variable path
      path, u = deque(), dest

      # Second while cycle
      # Path reconstruction
      while previous[u]:
          path.appendleft(u)
          u = previous[u]
      path.appendleft(u)
      ls_path = list(path)

      if len(ls_path)>1:
        result = ls_path
      else:
        result = -1

      ### Retrieve result
      return result

  return dijkstra(source, dest, nodes, connections)


print('--- Result 1 ---')
input_1 = ["4","A","B","C","D", "A|B|2", "C|B|11", "C|D|3", "B|D|2"]
print(input_1)
print(WeightedPath(input_1))
print('--- Result 2 ---')
input_2 = ["4","A","B","C","D","A|B|1","B|D|9","B|C|3","C|D|4"]
print(input_2)
print(WeightedPath(input_2))
print('--- Result 3 ---')
input_3 = ["7","A","B","C","D","E","F","G","A|B|1","A|E|9","B|C|2","C|D|1","D|F|2","E|D|6","F|G|2"]
print(input_3)
print(WeightedPath(input_3))
print('--- Result 4 ---')
input_4 = ["4","x","y","z","w","x|y|2","y|z|14", "z|y|31"]
print(input_4)
print(WeightedPath(input_4))

