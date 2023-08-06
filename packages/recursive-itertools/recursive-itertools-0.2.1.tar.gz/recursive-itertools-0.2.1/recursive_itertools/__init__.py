from collections import Iterable

def rfilter(obj, filter_func):
  if isinstance(obj, dict):
    o = {}
    for k,v in obj.items():
      nv = rfilter(v, filter_func)
      if filter_func(nv):
        o[k] = nv
    return o
  elif isinstance(obj, Iterable):
    o = []
    for x in obj:
      nx = rfilter(x, filter_func)
      if filter_func(nx):
        o.append(nx)
    return o
  else:
    return obj


