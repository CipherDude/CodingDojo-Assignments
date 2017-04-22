#Find and replace
str = "If monkeys like bananas, then I must be a monkey!"
print str
print str.find("monkey")
print str.replace("monkey", "allegator")

# Min. and max
x = [2,54,-2,7,12,98]
print "max number is:", max(x)
print "min number is:", min(x)

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print "first value is:", x[0]
print "last value is:", x[len(x)-1]

Fvalue = x[0]
Lvalue = x[-1]
newList = []
newList.append(Fvalue)
newList.append(Lvalue)
print newList

#from asnwer key:
print x[0],x[len(x)-1]

#new list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
sorted_list = x
print sorted_list
half_list_value = len(x)/2
total_list_value = len(x)
print half_list_value, total_list_value
list1 = sorted_list[:half_list_value]
print list1
list2 = sorted_list[half_list_value:]
print list2
list2.insert(0, list1)
print list2
