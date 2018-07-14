

# 利用lambda排序


lambda實際上就是匿名函式

一般形式：
```python
lambda arguments: expression
```

寫成函式形式就是
```python
def <lambda>(arguments):
    return expression
```
    
## 利用lambda做各種排序  

1. 簡單排序
```python
lis = ['a', 'b', 'c']    
print(sorted(lis))  
['a', 'b', 'c']    
print(sorted(lis, reverse=True))  
['c', 'b', 'a']
```

2. 對dictionary的key做排序  
```python
dic = {'c': 1, 'b': 2, 'a': 3}
print(sorted(dic))
['a', 'b', 'c']
print(sorted(dic, reverse=True))
['c', 'b', 'a'] 
```

3.dict的value排序
```python
dic = {'c': 1, 'b': 2, 'a': 3}
print(sorted(dic, key=lambda k: dic[k]))
# ['c', 'b', 'a']
print(sorted(dic, key=lambda k: dic[k], reverse=True))
# ['a', 'b', 'c']
```

4. list內的list排序
```python
lis = [[4, 2, 9], [1, 5, 6], [7, 8, 3]]
print(sorted(lis, key=lambda k: k[0]))
# [[1, 5, 6], [4, 2, 9], [7, 8, 3]]
print(sorted(lis, key=lambda k: k[1]))
# [[4, 2, 9], [1, 5, 6], [7, 8, 3]]
print(sorted(lis, key=lambda k: k[2]))
# [[7, 8, 3], [1, 5, 6], [4, 2, 9]]
print(sorted(lis, key=lambda k: k[0], reverse=True))
# [[7, 8, 3], [4, 2, 9], [1, 5, 6]]
```
    
5.dict内的dict排序
```python
dic = {
    'a': {'x': 3, 'y': 2, 'z': 1},
    'b': {'x': 2, 'y': 1, 'z': 3},
    'c': {'x': 1, 'y': 3, 'z': 2},
}
print(sorted(dic, key=lambda k: dic[k]['x']))
# ['c', 'b', 'a']
print(sorted(dic, key=lambda k: dic[k]['y']))
# ['b', 'a', 'c']
print(sorted(dic, key=lambda k: dic[k]['z']))
# ['a', 'c', 'b']
print(sorted(dic, key=lambda k: dic[k]['x'], reverse=True))
# ['a', 'b', 'c']
```

6.list內的dict排序
```python
lis = [
    {'x': 3, 'y': 2, 'z': 1},
    {'x': 2, 'y': 1, 'z': 3},
    {'x': 1, 'y': 3, 'z': 2},
]
print(sorted(lis, key=lambda k: k['x']))
# [{'z': 2, 'x': 1, 'y': 3}, {'z': 3, 'x': 2, 'y': 1}, {'z': 1, 'x': 3, 'y': 2}]
print(sorted(lis, key=lambda k: k['y']))
# [{'z': 3, 'x': 2, 'y': 1}, {'z': 1, 'x': 3, 'y': 2}, {'z': 2, 'x': 1, 'y': 3}]
print(sorted(lis, key=lambda k: k['z']))
# [{'z': 1, 'x': 3, 'y': 2}, {'z': 2, 'x': 1, 'y': 3}, {'z': 3, 'x': 2, 'y': 1}]
print(sorted(lis, key=lambda k: k['x'], reverse=True))
# [{'z': 1, 'x': 3, 'y': 2}, {'z': 3, 'x': 2, 'y': 1}, {'z': 2, 'x': 1, 'y': 3}]
```

7.dict內的list排序
```python
dic = {
    'a': [1, 2, 3],
    'b': [2, 1, 3],
    'c': [3, 1, 2],
}
print(sorted(dic, key=lambda k: dic[k][0]))
# ['a', 'b', 'c']
print(sorted(dic, key=lambda k: dic[k][1]))
# ['b', 'c', 'a']
print(sorted(dic, key=lambda k: dic[k][2]))
# ['c', 'b', 'a']
print(sorted(dic, key=lambda k: dic[k][0], reverse=True))
# ['c', 'b', 'a']
```