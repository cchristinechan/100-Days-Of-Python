from tkinter import *

FONT = ("Arial", 10, "normal")

def convert_miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609344
    converted_num_label["text"] = round(km, 2)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=30, pady=30)

# Entry
miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

converted_num_label = Label(text="0", font=FONT)
converted_num_label.grid(column=1, row=1)
converted_num_label.config(padx=10, pady=10)

km_label = Label(text="KM", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

#Button
button = Button(text="Calculate", command=convert_miles_to_km)  
button.grid(column=1, row=2)

window.mainloop()
