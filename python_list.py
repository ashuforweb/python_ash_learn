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
