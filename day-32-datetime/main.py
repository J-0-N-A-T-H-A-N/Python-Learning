import datetime as dt
from tkinter import *

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
current_date = dt.datetime.now()
# date_of_birth = dt.datetime(year=1975, month=7, day=23)
# day_of_week = date_of_birth.weekday()
# print(f"You were born on a {days[day_of_week].capitalize()}")
# print(current_date.year)

def calc_birth_weekday():
    bd_year = year_select.get()
    bd_month = month_select.get()
    bd_day = day_select.get()
    date_of_birth = dt.datetime(year=bd_year, month=bd_month, day=bd_day)
    day_of_week = date_of_birth.weekday()
    result_label.config(text=f"You were born on a {days[day_of_week].capitalize()}")

window = Tk()
window.config(pady=50, padx=50)

year_select = IntVar(window)
year_select.set("Year")
year_dropdown = OptionMenu(window, year_select, *range(current_date.year, 1900, -1))
year_dropdown.grid(row=0, column=0, padx=20)

month_select = IntVar(window)
month_select.set("Month")
month_dropdown = OptionMenu(window, month_select, *range(1,13))
month_dropdown.grid(row=1, column=0, padx=20)

day_select = IntVar(window)
day_select.set("Day")
day_dropdown = OptionMenu(window, day_select, *range(1,32))
day_dropdown.grid(row=2, column=0, padx=20)

calc_button = Button(text="Calculate", command=calc_birth_weekday)
calc_button.grid(row=1,column=3, columnspan=3)

result_label = Label(text="")
result_label.grid(row=3, column=0, columnspan=3)







window.mainloop()
