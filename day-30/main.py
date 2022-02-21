#
# try:
#     file = open("file.txt")
#     mylist = [1,2,3,4]
#     print(mylist[3])
#
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("New File:")
#
# except IndexError as index_message:
#     print(f"Error: {index_message}")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise KeyError
