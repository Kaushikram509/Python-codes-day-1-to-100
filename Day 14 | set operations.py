#set operations
#set is unordered collection
s = {1,2,3,10,'hi',4.5}
print(s)



#set allows only unique elements
s = {1,2,3,10,1,2,3,4,'hi',4.5}
print(s)





#set doesn't allows indexing and slicing
#empty set representation
s1 = {}
s2 = set()
print(type(s1), type(s2))





# set operations
# 1.union()
s1 = {1,2,3,6}
s2 = {3,4,5,6}
print(s1.union(s2))
print(s1 | s2)
print("*******intersection***********************")
print(s1 & s2)
print("*******Difference*****************")
print(s1.difference(s2))
print(s1-s2)
print("*******symmetric difference********************")
print(s1.symmetric_difference(s2))
print("*******subset********************************")
print(s1.issubset(s2))
print({1,2}.issubset(s1))
print(set().issubset(s1)) #every empty set is a subset
print("*******superset*****************")
print(s2.issuperset(s1))
print(s1.issuperset({1,2}))
print({1,2,5}.issuperset(s1))
print("******Disjoint set*******************")
print(s1.isdisjoint(s2))
print(s1.isdisjoint({10}))
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
*******intersection***********************
{3, 6}
*******Difference*****************
{1, 2}
{1, 2}
*******symmetric difference********************
{1, 2, 4, 5}
*******subset********************************
False
True
True
*******superset*****************
False
True
False
******Disjoint set*******************
False
True
print(s1)
s1.difference_update(s2)
print(s1)



#add(ele) :It add to set, if the element is not present in set , otherwise nothing
#update(new_set) : set elements updates with new set elements
#remove(ele) : It removes the set element, if element not present in set it rises keyerror
#discard(ele): It removes the element from set otherwise nothing
s = {1,2,3,4}
s.add(10)
print(s)
s.update({1,2,5,6})
print(s)
s.remove(10)
print(s)
# s.remove(20)  #key error
#print(s)
s.discard(10)
print(s)
s.discard(5)
print(s)
print(len(s))
print(sum(s))
print(max(s))
print(min(s))
