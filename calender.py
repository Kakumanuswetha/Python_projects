# import calendar module
import calendar
# import tkinter module
from tkinter import *
import calender
# This function displays calendar for a given year
def showCalender():
    gui = Tk()
    gui.config(background='light blue')
    gui.title("Calender for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()


if __name__ == '__main__':
    new = Tk()
    new.config(background='pink')
    new.title("Calender")
    new.geometry("450x340")
    new.grid_rowconfigure(0, weight=0)
    new.grid_columnconfigure(0, weight=1)
    cal = Label(new, text="Calender", bg='light green', font=("times", 28, "bold"),)
    # Label for enter year
    year = Label(new, text="Enter year", bg='grey')
    # text box for year input
    l1 = Label(new, text="   ", bg="light pink")
    l2 = Label(new, text="   ", bg="light pink")
    l3 = Label(new, text="   ", bg="light pink")
    year_field = Entry(new)
    button = Button(new, text='Show Calender', fg='Black', bg='light blue', command=showCalender)
    # adjusting widgets in position
    cal.grid(row=0, column=0)
    #cal.grid_columnconfigure(1, weight=1)
    l1.grid(row=1, column=0)
    #l1.grid_columnconfigure(1, weight=1)
    year.grid(row=2, column=0)
    #year.grid_columnconfigure(1, weight=1)
    l2.grid(row=3, column=0)
    #l2.grid_columnconfigure(1, weight=1)
    year_field.grid(row=4, column=0)
    #year_field.grid_columnconfigure(1, weight=1)
    l3.grid(row=5, column=0)
    #l3.grid_columnconfigure(1, weight=1)
    button.grid(row=6, column=0)
    new.mainloop()
