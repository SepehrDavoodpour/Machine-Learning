import random

# A function that finds a random path
def path_finder() :
  sequence = []
  while len(sequence) < 4:
    r = random.randint(0,3)
    if r not in sequence:
      sequence.append(r)
    if len(sequence) == 4:
      sequence.append(sequence[0])
  return sequence

# A function that calculates travel distance along the path
def path_distance(path , map) :
  distance = 0
  j = 0
  while j < len(path) - 1 :
    distance += map[path[j]][path[j+1]][1]
    j += 1
  return distance


# A nested list representing a distance matrix
map = [ [["tehran - tehran ", float('inf')] , ["tehran - mashhad ", 910] , ["tehran - isfahan ", 440] , ["tehran - shiraz ", 840]] ,
          [["mashhad - tehran ", 910] , ["mashhad - mashhad ", float('inf')] , ["mashhad - isfahan ", 1190] , ["mashhad - shiraz ", 1350]] ,
          [["isfahan - tehran ", 440] , ["isfahan - mashhad ", 1190] , ["isfahan - isfahan ", float('inf')] , ["isfahan - shiraz ", 400]] ,
          [["shiraz - tehran ", 840] , ["shiraz - mashhad ", 1350] , ["shiraz - isfahan ", 400] , ["shiraz - shiraz ", float('inf')]] ]

# Continuously evaluate successors and move only to strictly better paths; terminate when a local minimum is reached (no improvement found).
original_path = path_finder()
new_path = original_path
print("\n")
i = 1
while i!=0 :
  print(f"best path: {new_path} , length: {path_distance(new_path , map)}")
  i = 0
  successor_0 = path_finder()
  print(f"successor_0: {successor_0} , length: {path_distance(successor_0 , map)}")
  successor_1 = path_finder()
  print(f"successor_1: {successor_1} , length: {path_distance(successor_1 , map)}")
  if path_distance(successor_0 , map) < path_distance(new_path , map) :
    new_path = successor_0
    i = 1
  if path_distance(successor_1 , map) < path_distance(new_path , map) :
    new_path = successor_1
    i = 1
print("\n")    
print(f"best path: {new_path} , length: {path_distance(new_path , map)}")


