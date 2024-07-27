# lists 
''' 
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
'''
print("list of numbers : ")
list=[10,20,30,30,48] 
print(list, "  Type  = " ,type(list))


print("\n")
print("list of name: ")
list=["harshit","chauhan","aman"]
print(list)

print("\n")
print("list containning different types of data ; ")
list= [1,2,'d']
print(list)


print("-"*50)
print(" "*15,"Operations on List"," "*20)
print("-"*50)

print('\n')
lst = [1,2,"harshit","Aman"]
print(f"list before append operation : {lst}")
lst.append(1000)
print(f"list after append operation : {lst}")

print('\n')

print(f"length of list  = {len(lst)}")

print('\n')

print("index    value")
for i in range(0,len(lst)):
    print(f"{i}       {lst[i]}")

print("inserting the value at particular index")

lst.insert(3,3000)
lst.insert(0,100)
print("index    value")
for i in range(0,len(lst)):
    print(f"{i}       {lst[i]}")

print("\n")
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

print(fruits.count('orange'))

print(f"index of apple = {fruits.index('apple')}")
print(f"index of apple  starting from index 3 = {fruits.index('apple',3)}")

print("\n")
print('fruits  = ', end = " ")
print(fruits)
print(f"Reversing the list fruits :  ",end =" ")
fruits.reverse()
print(fruits)

print("\n")
print("sorting the fruits :" )
fruits.sort()
print(fruits)


print("\n")
print("poped out from the fruits :" )
fruits.pop()
print(fruits)



