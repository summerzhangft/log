from collections import namedtuple
import time
Request = namedtuple('Request',['method','url','version'])
MapItem = namedtuple('MapItem',['name','convert'])
mapping = [
    MapItem('',None),
    MapItem('local',lambda x: x),
    MapItem('',None),
    MapItem('',None),
    MapItem('time',lambda x : datetime.datetime.strptime(x, '%d/%b/%Y:%H:%M:%S %z')),
    MapItem('request',lambda x : Request(*x.split())),
    MapItem('status',int),
    MapItem('length',int),
    MapItem('html', lambda x : x),
    MapItem('ua',lambda x:x),
]
def ext(line):
    tmp = []
    ret = []
    splite = True
    for c in line:
        if c == '[':
            splite = False
            continue
        if c == ']':
            splite = True
            continue
        if c == '"':
            splite = not splite
            continue
        if c == ' ' and splite:
            ret.append(''.join(tmp))
            tmp.clear()
        else:
            tmp.append(c)
    ret.append(''.join(tmp))
    result = dict()
    for i, item in enumerate(mapping):
        if item.name:
            result[item.name] = item.convert(ret[i])
    return result
