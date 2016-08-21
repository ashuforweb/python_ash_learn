#Python lists and methods
'''append(x) this method takes element as an argument and add the element into
end of the list. For Example if you need to add 8 in existing list listTest'''
listTest = []
print listTest #will retrun empty list
listTest.append(8)
print listTest # will return list with element 8

'''extend(L) takes List as an argument and return joined list'''
listTest.extend(listTest)
print listTest #will print two elements 8,8

'''insert(i,x) takes indices and element as arguments, and inserts element at
given indices and pushes other elements down. For example if element is add at
location 2 of length 2 list 2nd element will now become 3rd element. indices
starts at 0'''
listTest.insert(1,5)
print listTest
