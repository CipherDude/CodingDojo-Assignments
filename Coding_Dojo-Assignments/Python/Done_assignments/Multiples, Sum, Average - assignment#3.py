# Multiples:
#PART I: prints all the odd numbers from 1 to 1000

print "Multiples:PART I: prints all the odd numbers from 1 to 1000"
# for odd_num in range(1,1000 +1):
#     if odd_num % 2 == 1:
#         print odd_num

for odd_num in range(1,1001, 2):
    print odd_num



#Part II: Create another program that prints all the multiples of 5 from 5 to 1,000,000.
print "Multiples:PART II: prints all the multiples of 5 from 5 to 1,000,000."
# for multi5 in range(5, 1000000 +1):
#         if multi5 % 5 == 0:
#             print multi5

for multi5 in range(5,1000001,5):
    print multi5


#SUM LIST: sum of all the values in the list:
print "SUM LIST: sum of all the values in the list:"
# my_list = [1, 2, 5, 10, 255, 3]
# summed_list= sum(my_list)
# print summed_list

my_list = [1, 2, 5, 10, 255, 3]
summed_count = 0

for evry_num in my_list:
    summed_count += evry_num
print summed_count


# AVERAGE LIST:average of the values in the list
print "AVERAGE LIST:average of the values in the list:"
aList = [1, 2, 5, 10, 255, 3]
print sum(aList) / len(aList)


#??? Doesn't work
print sum/len(aList)
