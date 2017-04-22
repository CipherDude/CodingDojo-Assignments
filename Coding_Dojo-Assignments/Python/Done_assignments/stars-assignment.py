#stars assignment:


# **** Part I: Create a function called draw_stars() that takes a list of numbers and prints out *.
print "Stars: Part I"
def draw_stars(starList):
    for every_indx in starList:
        print every_indx*("*")

draw_stars([5, 2,4, 8,1, 8, 12])

# **** Part II: Create a function called draw_stars() that takes a list of numbers and prints out *.
# Modify the function above. Allow a list containing integers and strings to be passed to the
# draw_stars() function. When a string is passed, instead of displaying *, display the first
# letter of the string according to the example below. You may use the .lower() string method
# for this part.
print ""
print "Stars: part II"
def draw_stars(starList):
    for every_indx in starList:
        if type(every_indx) == str:
            print every_indx[0].lower() * len(every_indx)
        else:
            print every_indx * ("*")

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
