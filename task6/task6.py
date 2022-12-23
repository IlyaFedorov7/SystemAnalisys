def task(csvString):

  from io import StringIO
  import csv
  import numpy as np
  import json

  filename = StringIO(csvString)
  R = csv.reader(filename, delimiter=',')
  output = []
  for row in R:
    output.append(row)

  def get_table(out, col):
    table=np.zeros(np.array(out).shape)
    for i in range(table.shape[1]):
      for j in range(table.shape[0]):
        if (out[i][col]<out[j][col]):
          table[i,j]=1
        elif (out[i][col]==out[j][col]):
          table[i,j]=0.5
        else:
          table[i,j]=0
    return table

  tbls=[]

  for i in range(len(output)):
    tbls.append(get_table(output,i))
  X=np.zeros((len(output),len(output)))

  for i in range(len(output)):
    X+=tbls[i]
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