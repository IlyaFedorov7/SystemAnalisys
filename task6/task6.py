def task(csvString):
  from io import StringIO
  import csv
  import numpy as np
  import json

  file = StringIO(csvString)
  r = csv.reader(file, delimiter=',')
  output = []
  for row in r:
    output.append(row)
  output=np.array(output).T
  def get_table(output, col):
    table=np.zeros(np.array(output).shape)
    for i in range(table.shape[1]):
      for j in range(table.shape[0]):
        if (output[i][col]<output[j][col]):
          table[i,j]=1
        elif (output[i][col]==output[j][col]):
          table[i,j]=0.5
        else:
          table[i,j]=0
    return table
  tables=[]
  for i in range(len(output)):
    tables.append(get_table(output,i))
  X=np.zeros((len(output),len(output)))
  for i in range(len(output)):
    X+=tables[i]
  X=X/len(output)
  k0=np.array([1/len(output)]*len(output))
  eps=0.001
  Y=X.dot(k0)
  lya1=(np.ones(len(output))).dot(Y)
  k1=1/lya1*Y
  while (abs(max(k1-k0))>=eps):
    k0=k1
    Y=X.dot(k0)
    lya1=(np.ones(len(output))).dot(Y)
    k1=1/lya1*Y
  for i in range(len(k1)):
    k1[i]=round(k1[i],3)
  return(json.dumps(k1.tolist()))