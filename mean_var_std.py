import numpy as np

def calculate(list):
  calculations = {} 
  try:
    nparray = np.array(list).reshape(3,3)
    calculations = {
      'mean': [nparray.mean(axis=0).tolist(), nparray.mean(axis=1).tolist(), nparray.mean()],
      'variance': [nparray.var(axis=0).tolist(), nparray.var(axis=1).tolist(), nparray.var()],
      'standard deviation': [nparray.std(axis=0).tolist(), nparray.std(axis=1).tolist(), nparray.std()],
      'max': [nparray.max(axis=0).tolist(), nparray.max(axis=1).tolist(), nparray.max()],
      'min': [nparray.min(axis=0).tolist(), nparray.min(axis=1).tolist(), nparray.min()],
      'sum': [nparray.sum(axis=0).tolist(), nparray.sum(axis=1).tolist(), nparray.sum()]
    }
    return calculations
  except ValueError:
    print('List must contain nine numbers.')
