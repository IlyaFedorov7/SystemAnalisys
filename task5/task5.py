def task(dataA,dataB):
  import numpy as np
  def bah4a(numbers):
    max=0
    for elem in numbers:
      try:
        if elem>max:
          max=elem
      except:
        for i in elem:
          if i>max:
            max=i
    table = np.zeros((max,max))
    mas=np.zeros(max)
    for item in numbers:
      try:
        mas[item-1]=1
        for j in range(max):
          if mas[j]==0:
            table[j,item-1]=0
          else:
            table[j,item-1]=1
      except:
        for elem in item:
          mas[elem-1]=1
        for elem in item:
          for j in range(max):
            if mas[j]==0:
              table[j,elem-1]=0
            else:
              table[j,elem-1]=1
    return table
  def masiv4ikvkusnenkii(A):
    numbers=[]
    for item in A:
      try:
        numbers.append(int(item))
      except:
        mas=[]
        for i in range(len(item)):
          mas.append(int(item[i]))
        numbers.append(mas)
    return numbers
  def back_string(arg):
    estimated=[]
    for item in arg:
      try:
        estimated.append(str(item+1))
      except:
        mas=[]
        for elem in item:
          mas.append(str(elem+1))
        estimated.append(mas)
    return estimated
  dataA=masiv4ikvkusnenkii(dataA)
  dataB=masiv4ikvkusnenkii(dataB)
  tableA=bah4a(dataA)
  tableB=bah4a(dataB)
  mergedTable=tableA*tableB+tableA.T*tableB.T
  answer=[]
  for j in range(mergedTable.shape[1]):
    for i in range(j):
      if mergedTable[i,j]==0:
        answer.append([i,j])
  return back_string(answer)