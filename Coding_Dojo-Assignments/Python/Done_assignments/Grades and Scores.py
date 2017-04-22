# Score and Grade:
import random

def random_grade_score(num):
    for each_num in range(num):
        random_num = random.randint(60,100)
        if random_num >= 90:
            print "Your Score is:", random_num,
            print "Your grade is: A"
        elif random_num >=  80:
            print "Your Score is:", random_num,
            print "Your grade is: B"
        elif random_num >= 70:
            print "Your Score is:", random_num,
            print "Your grade is: C"
        elif random_num >= 60:
            print "Your Score is:", random_num,
            print "Your grade is: D"
    print "End of the program. Bye!"

random_grade_score(10)
