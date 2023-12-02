#Program #3 - Creating a program that will ask how many apples and oranges you want to buy

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title ("Maihannn's Super Market")
root.geometry ( '1280x720')
bg_color="#EEF0F1"

#Variable
apple_input=IntVar()
orange_input=IntVar()
total_cost_input=IntVar()

cost_apple=StringVar()
cost_orange=StringVar()
cost_total=StringVar()

#Functions

def Total():
    if apple_input.get()==0 and orange_input.get()==0:
        messagebox.showerror("Error", "PLease select number of quantity")
    else:
        a=apple_input.get()
        o=orange_input.get()

    total=float(a*20.00+o*25.00)
    total_cost_input.set(a+o)
    cost_total.set("₱" + str(round(total, 2)))
    
    cost_apple.set("₱" + str(round(20.00, 2)))
    cost_orange.set("₱" + str(round(25.00, 2)))

def Receipt():
    text.delete(1.0, END)
    text.insert(END, "Item\t          Quantity \t\tPrice \n")
    text.insert (END, f"\nApple\t\t{apple_input.get()}\t {cost_apple.get()}")
    text.insert (END, f"\nOrange\t\t{orange_input.get()}\t {cost_orange.get()}") 
    text.insert (END, "\n\n==============================")
    text.insert (END, f"\nTotal Price\t\t{total_cost_input.get()}\t{cost_total.get()}")
    text.insert (END, "\n==============================")

def Reset():
    text.delete(1.0, END)
    apple_input.set(0)
    orange_input.set(0)
    total_cost_input.set(0)
    
    cost_apple.set("")
    cost_orange.set("")
    cost_total.set("")

def Exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

title=Label(root, text = "Maihannn's Super Market", bg="#E2F4E0", fg="#1A9423", font=("STIX", 35, "bold"), relief=GROOVE, bd=10)
title.pack(fill=X)

#Product_details

product_details_label=LabelFrame(root, text = "Product Details", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
product_details_label.place(x=25, y=90, width=800, height=400)

#headings

item=Label(product_details_label, text="Items", font=("Garuda", 25, "bold", "underline"), fg="#262224", bg="#EED3E1")
item.grid(row=0, column=0, padx=20, pady=15)

quantity=Label(product_details_label, text="Quantity", font=("Garuda", 25, "bold", "underline"), fg="#262224", bg="#EED3E1")
quantity.grid(row=0, column=1, padx=20, pady=15)

price=Label(product_details_label, text="Price", font=("Garuda", 25, "bold", "underline"), fg="#262224", bg="#EED3E1")
price.grid(row=0, column=2, padx=20, pady=15)

#Product
apple=Label(product_details_label, text="Apple", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
apple.grid(row=1, column=0, padx=20, pady=15)
apple_text=Entry (product_details_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=apple_input)
apple_text.grid (row=1, column=1, padx=20, pady=15)
apple_cost=Entry (product_details_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=cost_apple)
apple_cost.grid (row=1, column=2, padx=20, pady=15)

orange=Label(product_details_label, text="Orange", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
orange.grid(row=2, column=0, padx=20, pady=15)
orange_text=Entry (product_details_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=orange_input)
orange_text.grid (row=2, column=1, padx=20, pady=15)
orange_cost=Entry (product_details_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=cost_orange)
orange_cost.grid (row=2, column=2, padx=20, pady=15)

#total
total=Label(product_details_label, text="Total", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
total.grid(row=4, column=0, padx=20, pady=15)
total_text=Entry (product_details_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=total_cost_input)
total_text.grid (row=4, column=1, padx=20, pady=15)
total_cost=Entry (product_details_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=cost_total)
total_cost.grid (row=4, column=2, padx=20, pady=15)

#Receipt
receipt=Frame(root, relief=GROOVE, bd=7)
receipt.place(x=830, y=90,width=430, height = 400)
receipt_title=Label(receipt, text="Receipt", font=("Courier 10 Pitch", 20, "bold"), fg="#F63392", relief=GROOVE, bd=7).pack(fill=X)
scroll=Scrollbar(receipt, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)
text=Text(receipt, font=("Courier 10 Pitch", 17, "bold"), yscrollcommand=scroll.set)
text.pack(fill=BOTH)
scroll.config(command=text.yview)

#Buttons
button=Frame(root, relief=GROOVE, bd=10)
button.place(x=25, y=500, width=1235, height=120)

total_button=Button (button, text="Total", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Total)
total_button.grid(row=0, column=0, padx=20, pady=10)

receipt_button=Button (button, text="Receipt", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Receipt)
receipt_button.grid(row=0, column=1, padx=20, pady=10)

reset_button=Button (button, text="Reset", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Reset)
reset_button.grid(row=0, column=3, padx=20, pady=10)

exit_button=Button (button, text="Exit", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Exit)
exit_button.grid(row=0, column=4, padx=20, pady=10)

root.mainloop()
