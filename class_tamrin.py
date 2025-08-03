from tkinter import *
phone_list=[]
list_total=[]

def save_click():
    phone = {"name":name.get(),"quntity":quantity.get(),"price":price.get(),}
    total_zarb = {quantity.get()*price.get(),}
    list_total.append(total_zarb)
    phone_list.append(phone)
    print(phone_list)
    print(list_total)
    #print(list_total)
    #total.set(total.get() + person["total"])
    name.set("")
    quantity.set(0)
    price.set(0)
    total.set(total_zarb)







window = Tk()
window.title("phone")
window.geometry("300x300")

Label(window, text="name").place(x=20, y=20)
name =StringVar()
Entry(window, textvariable=name).place(x=80, y=20)

Label(window, text="quantity").place(x=20, y=60)
quantity = IntVar()
quantity.set(0)
Entry(window, textvariable=quantity).place(x=80, y=60)

Label(window, text="price").place(x=20, y=100)
price = IntVar()
price.set(0)
Entry(window, textvariable=price).place(x=80, y=100)

Label(window, text="total").place(x=80, y=150)
total =IntVar()
total.set(0)
Entry(window, textvariable=total).place(x=130, y=150)



Button(window,text="save",width = 10,command=save_click).place(x=80,y=180)









window.mainloop()