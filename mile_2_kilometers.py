from tkinter import *

root = Tk()
root.minsize(width=100, height=100)
root.config(padx=20, pady=20)

#Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal_to = Label(text="Is equal to: ")
label_equal_to.grid(column=0, row=1)

label_zero = Label(text="0")
label_zero.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)


#function that converts miles to km
def converter():
    num = int(text_entry.get())
    result = num * 1.60934
    result = round(result,1)
    result = str(result)
    print(type(result))
    label_zero.config(text=result)


#button
button_calculate = Button(text="Calculate", command=converter)
button_calculate.grid(column=1, row=3)

#Entry
text_entry = Entry(width=10)
text_entry.insert(END, "0")
text_entry.grid(column=1, row=0)


root.mainloop()