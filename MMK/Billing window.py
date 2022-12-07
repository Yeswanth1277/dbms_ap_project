from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector

win = Tk()
win.state('zoomed')
win.config(bg='green')

# HEADING
Label(win, text="MMK CONVULSENTORY SOLUTIONS", font="impack 31 bold", bg="blue", fg="white").pack(fill=X)
Label(win, text="ACCOUNTS AND BILLING", font="impack 31 bold", bg="brown", fg="white",pady="5px").pack(fill=X)


#frmae 1
frame1 = Frame(win, bd=15, relief=RIDGE)
frame1.place(x=100, y=150, width=1340, height=580,)
# label frame for patient info
lf1 = LabelFrame(frame1, text="Account and Billing Details", font="arial 25 bold", bd=10, bg="pink")
lf1.place(x=0, y=0, width=1320, height=550)


# label frame for Enter Patient Details
Label(lf1, text="Bill number : ", bg="pink",font="arial 15").place(x=100, y=0)
Label(lf1, text="Name of the Patient : ", bg="pink",font="arial 15 ").place(x=100, y=100)
Label(lf1, text="Patient ID : ", bg="pink",font="arial 15").place(x=100, y=200)
Label(lf1, text="Total amount: ", bg="pink",font="arial 15").place(x=650, y=0)
Label(lf1, text="Amount paid: ", bg="pink",font="arial 15").place(x=650, y=100)
Label(lf1, text="Balance: ", bg="pink",font="arial 15").place(x=650, y=200)

#text variables for evry entry feild
Billnumber = StringVar()
NameofthePatient= StringVar()
PatientID = StringVar()
Total = StringVar()
Amount  = StringVar()
Balance= StringVar()


# entry feild for all labels
e1 = Entry(lf1, bd=4,textvariable=Billnumber)
e1.place(x=100, y=50, width=470)
e2 = Entry(lf1, bd=4,textvariable=NameofthePatient)
e2.place(x=100, y=150, width=470)
e3 = Entry(lf1, bd=4,textvariable=PatientID)
e3.place(x=100, y=250, width=470)
e4 = Entry(lf1, bd=4,textvariable=Total)
e4.place(x=650, y=50, width=470)
e5 = Entry(lf1, bd=4,textvariable=Amount)
e5.place(x=650, y=150, width=470)
e6 = Entry(lf1, bd=4,textvariable=Balance)
e6.place(x=650, y=250, width=470)

def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("error","all feilds are required")
    else:
        con=mysql.connector.connect(host="localhost",username="root",password="Sai@2004",database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into bill values(%s,%s,%s,%s,%s,%s)",(
            Billnumber.get(),
            NameofthePatient.get(),
            PatientID.get(),
            Total.get(),
            Amount.get(),
            Balance.get()
        ))
        con.commit()
        con.close()
        messagebox.showinfo("sucess","record has been inserted")

def exit():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to exit')
    if confirm>0:
        win.destroy()
        return

 
def clear():
    Billnumber.set("")
    NameofthePatient.set("")
    PatientID.set("")
    Total.set("")
    Amount.set("")
    Balance.set("")    

def delete():
    con = mysql.connector.connect(host="localhost", username="root", password="qwerty_123", database="mydata")
    my_cursor = con.cursor()
    querry = ('delete from hospital where Reference = %s')
    value = (ref.get(),)
    my_cursor.execute(querry, value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo("deleted", "patient data has been deleted")

# exit button
c_btn = Button(win, text="exit", font="ariel 15 bold", bg="red", fg="white", bd=6, cursor="hand2",command=exit)
c_btn.place(x=350, y=550, width=270)
# clear button
c_btn = Button(win, text="Save", font="ariel 15 bold", bg="green", fg="white", bd=6, cursor="hand2",command=pd)
c_btn.place(x=600, y=550, width=270)
# Save button
p_btn = Button(win, text="clear", font="ariel 15 bold", bg="blue", fg="white", bd=6, cursor="hand2",command=clear)
p_btn.place(x=850, y=550, width=270)
# delete button
# d_btn = Button(win, text="delete", font="ariel 15 bold", bg="brown", fg="white", bd=6, cursor="hand2",command=delete)
# d_btn.place(x=1000, y=550, width=270)

#fetch_data()
mainloop()