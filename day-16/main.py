# import turtle
# from turtle import Turtle, Screen
# from math import sqrt
#
# timmy = Turtle()
#
# myscreen = Screen()
# print(myscreen.canvheight)
#
# timmy.shape("turtle")
# timmy.color("CadetBlue4")
# timmy.speed(1)
#
# timmy.forward(100)
#
# myscreen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()   # Create object called table using PrettyTable class
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Wartortle", "Water"])
table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
table.title = "Pokemon Chart"
print(table)
