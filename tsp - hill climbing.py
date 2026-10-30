import random


# تابعی که یک مسیر رندوم پیدا می کند
def path_finder() :
  sequence = []
  while len(sequence) < 4:
    r = random.randint(0,3)
    if r not in sequence:
      sequence.append(r)
    if len(sequence) == 4:
      sequence.append(sequence[0])
  return sequence

# تابعی که طول مسیر را محاسبه می کند
def path_distance(path , map) :
  distance = 0
  j = 0
  while j < len(path) - 1 :
    distance += map[path[j]][path[j+1]][1]
    j += 1
  return distance


# .لیست تو در تویی که نمایانگر یک ماتریس است. لیست اولیه چهار لیست زیر مجموعه دارد. هر لیست زیر مجموعه خود چهار لیست زیر مجموعه دارد که نمایانگر چهار مسیر متفاوت است
map = [ [["tehran - tehran ", float('inf')] , ["tehran - mashhad ", 910] , ["tehran - isfahan ", 440] , ["tehran - shiraz ", 840]] ,
          [["mashhad - tehran ", 910] , ["mashhad - mashhad ", float('inf')] , ["mashhad - isfahan ", 1190] , ["mashhad - shiraz ", 1350]] ,
          [["isfahan - tehran ", 440] , ["isfahan - mashhad ", 1190] , ["isfahan - isfahan ", float('inf')] , ["isfahan - shiraz ", 400]] ,
          [["shiraz - tehran ", 840] , ["shiraz - mashhad ", 1350] , ["shiraz - isfahan ", 400] , ["shiraz - shiraz ", float('inf')]] ]
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


