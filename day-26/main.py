# # List comprehension ** Doesn't just work with lists
# #
# #  new_list = [new_item for item in list]
#
# def calc(n):
#     p = n * 8
#     return p
#
# string = "Jonathan"
# list = [1, 2, 3, 4]
# dict = {
#     1: "Cat",
#     2: "Dog",
#     3: "Goldfish",
#     4: "Hamster"
# }
# new_list = [calc(item) for item in list]
# pet_list = [dict[n] for n in list]
# pet_list_conditional = [dict[n].upper() for n in list if len(dict[n]) <= 3]
# name_list = [letter.upper() for letter in string]
# range_list = [n * 2 for n in range(1, 5)]
# range_list_conditional = [n * 2 for n in range(1, 5) if n % 2 == 0]
#
# print(new_list)
# print(pet_list)
# print(pet_list_conditional)
# print(name_list)
# print(range_list)
# print(range_list_conditional)

# import random
# names = ["Alex", "Brian", "Carol", "Diane", "Edward", "Frankie"]
#
# scores = {name: random.randint(50,100) for name in names}
# print(f"Scores: {scores}")
#
#
# passed = {key: value for (key, value) in scores.items() if value >= 70}
# failed = {key: value for (key, value) in scores.items() if value < 70}
#
# print(f"Passed: {passed}")
# print(f"Failed: {failed}")


