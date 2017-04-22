# weekend = {"sun": "Sunday", "Mon": "Monday"}
# capitals = {}
# capitals["svk"] = "Batislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
#
# print weekend
# print weekend["sun"]
# print capitals["svk"]
# print "___________"
#
# for data in capitals:
#     print data
#
# print "__interkeys______"
#
# for key in capitals.iterkeys():
#     print key
#
# print "____intervalues_______"
#
# for each_val in capitals.itervalues():
#     print each_val
#
# print "___________"
# for every_key, every_value in capitals.iteritems():
#     print every_key,"=", every_value
#
# print "___nested dict________"
#
# context = {
# 'questions:': [
# {'id': 1, 'content': 'Why is there a light in the fridge, but none in the freezer?'},
# {'id': 2, 'content': 'why don\'t sheep shrink when it rains?'},
# {'id': 3, 'content': 'why are they called aprtments when they are all struck together?'},
# {'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
# ]
# }
#

# # for key,data in context.items():
# #     for value in data:
# #         print "Question #", value["id"], ":", value["content"]
# #         print "---"
# for key,data in context.items():
#     for value in data:
#         print "question #:", value['id'],":", value["content"]
#         print "-----*----*"
# # for key,data in context.items():
# #     for value in data:
# #         print "question #", value["id"],":", value["content"]
# #         print "------"
# for key,data in context.items():
#     for value in data:
#         print value['id'], ":", value["content"]
#
# for key,data in context.items():
#     for value in data:
#         print value['id']
#         print value['content']
#
# data={"house":"Haus", "cat": "Katze", "red": "rod"}
#
# print data.items()
# y = data.keys()
# x= data.values()
# print "------"
# print x[1]
# print y[2]

# print "---dic from lists---"
#
# dishes = ['pizza', 'sauerkrout', 'paella', 'hamburger']
# countries = ['italy', 'Germany', 'Spain', 'USA']
#
# contry_specialities = zip(countries,dishes)
# print contry_specialities

superheros = {
"quickster": ["The Flash", "Quick Silver"],
"buster":["The Hulk", "The Thing"],
"flyer": ["silver surfer", "Iron Man", "Superman"],
"detective": ["Bat Man", "The Owl", "The Arrow"],
}

for hero_type in superheros.iterkeys():
    

# print superheros
#
# print superheros["quickster"]

# for within_cat,my_hero in superheros.items():
#     print within_cat,my_hero
#     # print superheros[my_hero]
