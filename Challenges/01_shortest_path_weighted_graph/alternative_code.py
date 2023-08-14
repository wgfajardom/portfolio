def WeightedPath(strArr):

  # Extracting main parameters
  number_of_nodes = int(strArr[0])
  
  # The array must have at least two nodes
  if number_of_nodes >= 2:
    nodes = strArr[1:1+number_of_nodes]
    first_node = nodes[0]
    last_node = nodes[-1]
    connections = [elem.split("|")[0]+"|"+elem.split("|")[1] for elem in strArr[1+number_of_nodes:]]
    weights = [int(elem.split("|")[2]) for elem in strArr[1+number_of_nodes:]]
    print(connections)
    print(weights)

    # Functions
    def connected_node(c, n):
      if c.split("|")[0] == n:
        return c.split("|")[1]
      else:
        return c.split("|")[0]

    def extract_weight(c):
      return weights[connections.index(c)]

    def check_goal(c, n):
      if connected_node(c, n) == last_node:
        return True
      else:
        return False

    def possible_connections(pc, c):
      return [elem for elem in pc if elem != c]

    def next_connections(pc, n):
      return [elem for elem in pc if n in elem]

    # # Initializing paths
    
    # data[paths[0]] = {
    #   'current_con': seed_c,
    #   'path': seed_c[0]+connected_node(seed_c,first_node),
    #   'new_node': p,
    #   'goal': check_goal(seed_c,first_node),
    #   'sum_weight': extract_weight(seed_c),
    #   'pc': possible_connections(connections,seed_c),
    #   'nc': next_connections(pc,connected_node(seed_c,first_node))
    # }


    data = dict()
    data[first_node] = {
      'current_node': first_node,
      'current_connection': '',
      'future_node': '',
      'weight': 0,
      'goal': False,
      'path': first_node,
      'possible_connections': connections,
      'next_connections': []
    }

    # Function step
    def step(data, path):
      n = data[path]['current_node']
      pc = data[path]['possible_connections']
      nc = next_connections(pc,n)
      for ii in range(len(nc)):
        c = nc[ii]
        p = connected_node(c,n)
        w = extract_weight(c)
        goal = check_goal(c,n)
        pc = possible_connections(pc,c)
        print('------------')
        print(n,c,p,w,goal,path,pc,nc)
        if goal == False:
          if len(pc)>0:
            n = p
            nc = next_connections(pc,n)
            data[path+p] = {
              'current_node': n,
              'current_connection': c,
              'future_node': p,
              'weight': data[path]['weight']+w,
              'goal': goal,
              'path': path+p,
              'possible_connections': pc,
              'next_connections': nc
            }
            path = path+p
            return step(data, path)
          else:
            data[path+p] = {
              'current_node': n,
              'current_connection': c,
              'future_node': p,
              'weight': data[path]['weight']+w,
              'goal': goal,
              'path': path+p,
              'possible_connections': pc,
              'next_connections': []
            }
        else:
            data[path+p] = {
              'current_node': n,
              'current_connection': c,
              'future_node': p,
              'weight': data[path]['weight']+w,
              'goal': goal,
              'path': path+p,
              'possible_connections': pc,
              'next_connections': []
            }
      return data  
  

    return step(data, first_node)





    # # # Initializing paths
    
    # # data[paths[0]] = {
    # #   'current_con': seed_c,
    # #   'path': seed_c[0]+connected_node(seed_c,first_node),
    # #   'new_node': p,
    # #   'goal': check_goal(seed_c,first_node),
    # #   'sum_weight': extract_weight(seed_c),
    # #   'pc': possible_connections(connections,seed_c),
    # #   'nc': next_connections(pc,connected_node(seed_c,first_node))
    # # }

  
    # paths = [first_node]
    # paths_weight = [0]
    # paths_goal = [False]

    # # Function step
    # def step(n,pc,paths,paths_weight,paths_goal):
    #   nc = next_connections(pc,n)
    #   lp = len(paths)
    #   paths = [paths[lp-1]] * len(nc)
    #   paths_weight = [paths_weight[lp-1]] * len(nc)
    #   paths_goal = [paths_goal[lp-1]] * len(nc)
    #   for ii in range(len(nc)):
    #     c = nc[ii]
    #     p = connected_node(c,n)
    #     w = extract_weight(c)
    #     goal = check_goal(c,n)
    #     paths[ii] = paths[ii]+p
    #     paths_weight[ii] = paths_weight[ii]+w
    #     paths_goal[ii] = goal
    #     pc = possible_connections(pc,c)
    #     print('------------')
    #     print(n,c,p,w,goal,paths,paths_weight,paths_goal,pc,nc)
    #     if goal == False:
    #       if len(pc)>0:
    #         n = p
    #         return step(n,pc,paths,paths_weight,paths_goal)
  

    # # return step(first_node, connections[0], possible_connections(connections,connections[0]))
    # return step(first_node,connections,paths,paths_weight,paths_goal)
    # # return data




  else:
    return "The array do not have two or more nodes"




# keep this function call here 
print WeightedPath(raw_input())




# Current node
# A 
# Connection
# A|B|2
# Paths
# [A]

  # Connected node
  # B
  # Paths
  # [AB]
  # Weights
  # [2]
  # Goals
  # [False]
  # Possible connections
  # ["C|B|11", "C|D|3", "B|D|2"]


  # Current node
  # B 
  # Connections
  # C|B|11 and B|D|2
  # Paths
  # [AB, AB]

    # Connection
    # C|B|11
    # Connected node
    # C
    # Paths
    # [ABC, AB]
    # Weights
    # [13, 2]
    # Goals
    # [False, False]
    # Possible connections
    # "C|D|3", "B|D|2"

    # Connection
    # B|D|2
    # Connected node
    # D
    # Weight
    # [13,4]
    # Possible connections
    # "C|D|3", "B|D|2"

