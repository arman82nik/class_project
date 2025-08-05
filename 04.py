from tkinter import *
from tkinter import messagebox
from tkinter import ttk




def reset_form():
    pass

def select_product(event):
    pass
def save_click():
    pass

def edit_click():
    pass

def remove_click():
    pass


window = Tk()
window.title("Orders")
window.geometry("710x360")
window.resizable(False, False)

# number
number = IntVar()
Label(window,text="number").place(x=20,y=20)
Entry(window, textvariable=number).place(x=100,y=20)

# owner
owner = StringVar()
Label(window,text="Name").place(x=20,y=60)
Entry(window, textvariable=owner).place(x=100,y=60)

# register_data
register_data = StringVar()
Label(window,text="register_data").place(x=20,y=100)
Entry(window, textvariable=register_data).place(x=100,y=100)

# operator
operator = IntVar()
Label(window,text="operator").place(x=20,y=140)
Entry(window, textvariable=operator).place(x=100,y=140)

# charge
charge = IntVar()
Label(window,text="charge").place(x=20,y=180)
Entry(window, textvariable=charge).place(x=100,y=180)

# Name_Search
owner_search = StringVar()
Label(window,text="Search owner").place(x=250,y=20)
Entry(window, textvariable=owner_search).place(x=330,y=20)

# owner_Search
owner_search = StringVar()
Label(window,text="Search owner").place(x=480,y=20)
Entry(window, textvariable=owner_search).place(x=560,y=20)


Button(window, text="Save", command=save_click, width=7).place(x=20,y=300)
Button(window, text="Edit", command=save_click, width=7).place(x=95,y=300)
Button(window, text="Remove", command=save_click, width=7).place(x=170,y=300)

table = ttk.Treeview(window, height=12,columns=(1,2,3,4,5),show="headings")
table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)

table.heading(1, text="number")
table.heading(2, text="owner")
table.heading(3, text="operator")
table.heading(4, text="data_register")
table.heading(5, text="charge")

table.bind("<<TreeviewSelect>>", select_product)

table.place(x=250, y = 60)


window.mainloop()



