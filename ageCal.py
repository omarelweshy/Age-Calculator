import datetime
import tkinter as tk

class Person:
    def __init__(self,birthdate):
        self.birthdate=birthdate
    def years(self):
        today=datetime.date.today()
        year = today.year-self.birthdate.year
        return year

    def month(self):
        today=datetime.date.today()
        month = today.month-self.birthdate.month
        return month

    def day(self):
        today=datetime.date.today()
        day = today.day-self.birthdate.day
        return day

def calculate_age():
    person=Person(datetime.date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get())))
    text_answer=tk.Text(master=window,height=20,width=30)
    text_answer.grid(column=1,row=5)
    answer_text = "Your age is: {years} years".format(years=person.years()) + "\n" + "and {month} month".format(month=person.month()) + "\n" + "and {day} Day".format(day=person.day())
    text_answer.insert(tk.END,answer_text)

#create frame
window=tk.Tk()

#create frame geometry
window.geometry("300x200")

#set the title of the frame
window.title("Age calculator App")


#adding Labels
year_label=tk.Label(text="Year")
month_label=tk.Label(text="Month")
day_label=tk.Label(text="Date")

year_label.grid(column=0,row=1)
month_label.grid(column=0,row=2)
day_label.grid(column=0,row=3 )

year_entry=tk.Entry()
month_entry=tk.Entry()
day_entry=tk.Entry()

year_entry.grid(column=1,row=1)
month_entry.grid(column=1,row=2)
day_entry.grid(column=1,row=3)

calculate_button=tk.Button(text="Calculate your Age!",command=calculate_age)
calculate_button.grid(column=1,row=4)

window.mainloop()
