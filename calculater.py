from tkinter import *





def voroodi(sabet):
    kadr.insert(END, sabet)

def amaliat():
    text_result= kadr.get()
    if "+" in text_result:
        a, b = text_result.split("+")
        javab = float(a) + float(b)
    elif "-" in text_result:
        a, b = text_result.split("-")
        javab = float(a) - float(b)
    elif "*" in text_result:
        a, b = text_result.split("*")
        javab = float(a) * float(b)
    elif "/" in text_result:
        a, b = text_result.split("/")
        if float(b) != 0:
            javab = float(a) / float(b)
        else:
            javab = "error"
    else:
        javab = "valid"
    kadr.delete(0, END)
    kadr.insert(0, str(javab))


def delete():
    kadr.delete(0, END)








window = Tk()
window.title("Calculator")
window.config(bg="light blue")
window.geometry("270x300")
window.title("calculator")


kadr = Entry(window, width=50, font=("Arial", 20))
kadr.place(x=0,y=20)


Button(window, text="1", width=5,bg="black",fg="white", command=lambda: voroodi("1")).place(x=10,y=235)
Button(window, text="2", width=5,bg="black",fg="white", command=lambda: voroodi("2")).place(x=60,y=235)
Button(window, text="3", width=5,bg="black",fg="white", command=lambda: voroodi("3")).place(x=110,y=235)
Button(window, text="4", width=5,bg="black",fg="white", command=lambda: voroodi("4")).place(x=10,y=195)
Button(window, text="5", width=5,bg="black",fg="white", command=lambda: voroodi("5")).place(x=60,y=195)
Button(window, text="6", width=5,bg="black",fg="white", command=lambda: voroodi("6")).place(x=110,y=195)
Button(window, text="7", width=5,bg="black",fg="white", command=lambda: voroodi("7")).place(x=10,y=155)
Button(window, text="8", width=5,bg="black",fg="white", command=lambda: voroodi("8")).place(x=60,y=155)
Button(window, text="9", width=5,bg="black",fg="white", command=lambda: voroodi("9")).place(x=110,y=155)
Button(window, text="0", width=20,bg="black",fg="white", command=lambda: voroodi("0")).place(x=8,y=265)

Button(window, text="+", width=5,bg="black",fg="white", command=lambda: voroodi("+")).place(x=165,y=265)

Button(window, text="-", width=5,bg="black",fg="white", command=lambda: voroodi("-")).place(x=165,y=195)
Button(window, text="*", width=5,bg="black",fg="white", command=lambda: voroodi("*")).place(x=165,y=155)
Button(window, text="/", width=5,bg="black",fg="white", command=lambda: voroodi("/")).place(x=165,y=235)

Button(window, text="=", width=5,bg="black",fg="white", command=amaliat).place(x=220,y=183)
Button(window, text="delete",bg="black",fg="white", width=5,height=5, command=delete).place(x=220,y=210)


window.mainloop()
