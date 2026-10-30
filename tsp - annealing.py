import random
import math


# A function which finds a random path
def path_finder() :
  sequence = []
  while len(sequence) < 4:
    r = random.randint(0,3)
    if r not in sequence:
      sequence.append(r)
    if len(sequence) == 4:
      sequence.append(sequence[0])
  return sequence


# A function which calculates travel distance along the path
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

# Iteratively search for an optimal path.
original_path = path_finder()
best_path = original_path
print("\n")
for i in range(10) :
  a = []
  print(f"best path: {best_path} , length: {path_distance(best_path , map)}")
  successor_0 = path_finder()
  print(f"successor_0: {successor_0} , length: {path_distance(successor_0 , map)}")
  k = 0
  if path_distance(successor_0 , map) < path_distance(best_path , map) :
    best_path = successor_0
    k = 1
  elif path_distance(successor_0 , map) >= path_distance(best_path , map) and k==0:
    x = -(path_distance(successor_0 , map) - path_distance(best_path , map)) / path_distance(best_path , map)
    p = math.exp(x) * 20
    p1 = int(p)
    print(p1)
    k = 0
    for j in range(p1) :
      a.append(successor_0)
  successor_1 = path_finder()
  print(f"successor_1: {successor_1} , length: {path_distance(successor_1 , map)}")
  if path_distance(successor_1 , map) < path_distance(best_path , map) :
    best_path = successor_1
    k = 1
  elif (path_distance(successor_1 , map) >= path_distance(best_path , map)) and k==0:
    y = -(path_distance(successor_1 , map) - path_distance(best_path , map)) / path_distance(best_path , map)
    q = math.exp(y) * 20
    q1 = int(q)
    print(q1)
    k = 0
    for j in range(q1) :
      a.append(successor_1)
  if k == 0 :
    x = 0
    n = math.exp(x) * 20
    n1 = int(n)
    print(n1)
    for i in range(n1) :
      a.append(best_path)
    r = random.randint(0 , p1 + q1 + n1 - 1)
    best_path = a[r]
  print("\n")    
print(f"best path: {best_path} , length: {path_distance(best_path , map)}")


