# it contain distinct items
# unordered
# no indexing
# union intersection set difference are fast
# uses hashing internally

# it contains only distinct values
s={2,2,2,4,7,8,}
print(s)

set1={1,2,3,4,5}
print(type(set1))
print(set1)

set2=set([10,20,3,0])
print(type(set2))
print(set2)

set3={}    #creates empty dictionary

set3=set()  #this will create empty set.
print(set3)

set3={1,5,7,8}
print(set3)


# set methods  
set3={10,20,}
set3.add(456)
print(set3)


set3.update({12,13},[100,569])
print(set3)
set3.discard(10)
print(set3)
# set3.remove(10)
set3.remove(20)
print(set3)
set3.clear()
print(set3)
del set3
# print(set3)

s1 = {2, 4, 6, 8}

s2 = {3, 6, 9}

print('union ', s1 | s2)
print(s1.union(s2))

print('intersecton', s1 & s2)
print(s1.intersection(s2))

print('present in s1, but not present in s2', s1 - s2)
print(s1.difference(s2))

print('symmetric differences, not present in both', s1 ^ s2)
s1 = {2, 4, 6, 8}
s2 = {4, 8}

print('disjoint sets:', s1.isdisjoint(s2))

print('isSubset:', s1 <= s2)
print(s1.issubset(s2))

print('proper set:', s1 < s2)

print('s1 is superset of s2:', s1 >= s2)
print(s1.issuperset(s2))

print('s1 is proper superset of s2:', s1 > s2)
