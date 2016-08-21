#Python lists and methods
'''append(x) this method takes element as an argument and add the element into
end of the list. For Example if you need to add 8 in existing list listTest'''
listTest = [1,2,3]
listTest.append(8)
print listTest # will return list with elements 1,2,3,8

'''extend(L) takes List as an argument and return joined list'''
listTest.extend(listTest)
print listTest #will print 1,2,3,8,1,2,3,8

'''insert(i,x) takes indices and element as arguments, and inserts element at
given indices and pushes other elements down. For example if element is add at
location 2 of length 2 list 2nd element will now become 3rd element. indices
starts at 0'''
listTest.insert(1,5)
print listTest #will print 1,5,2,3,8,1,2,3,8

'''remove(x) this method will remove the item which has value equal to x'''
listTest.remove(8) #will remove first element with value 8
print listTest #will print list 1,5,2,3,1,2,3,8

'''pop([i]) will remove the element at indices i; i is optional, if i is not
passed then last element will be removed'''
listTest.pop(4) #will remove element at postion 5
print listTest #will print 1,5,2,3,2,3,8

# '''clear() will delete all the items from the list. Only available in python 3'''
# listTest.clear() #will remove all the items from the list
# print listTest #will print empty list

'''index(x) will return indices of value x (first occurance) in the list. will throw an error
if element is not available'''
print listTest.index(5) #will print 1 as 5 is at position 2

'''count(x) returns number of times x appeared in list'''
print listTest.count(3) #will return 2 as 3 appears twice.
