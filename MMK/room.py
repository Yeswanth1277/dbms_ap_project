from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
from tkinter import font
import sqlite3

win = Tk()
win.state('zoomed')
win.config(bg='green')

# HEADING
Label(win, text="MMK CONVULSENTORY SOLUTIONS", font="impack 31 bold", bg="blue", fg="white").pack(fill=X)
Label(win, text="ROOM ALLOCATION FORM", font="impack 31 bold", bg="brown", fg="white",pady="5px").pack(fill=X)


#frmae 1
frame1 = Frame(win, bd=15, relief=RIDGE)
frame1.place(x=20, y=244, width=1400, height=500,)
# label frame for patient info
lf1 = LabelFrame(frame1, text="Enter Patient Details", font="arial 25 bold", bd=10, bg="pink")
lf1.place(x=0, y=0, width=1520, height=670)


# label frame for Enter Patient Details
Label(lf1, text="patientname", bg="pink",font="arial 20 ").place(x=100, y=50)
Label(lf1, text="patientid", bg="pink",font="arial 20").place(x=100, y=150)
Label(lf1, text="admitdate", bg="pink",font="arial 20").place(x=100, y=250)
Label(lf1, text="dischargedate", bg="pink",font="arial 20").place(x=100, y=350)
Label(lf1, text="roomtype", bg="pink",font="arial 20").place(x=800, y=50)
Label(lf1, text="charge", bg="pink",font="arial 20").place(x=800, y=150)
Label(lf1, text="roomno", bg="pink",font="arial 20").place(x=800, y=250)

#text variables for evry entry feild
NameofthePatient = StringVar()
PatientID = StringVar()
Dateadmitted= StringVar()
Datedischarged = StringVar()
Roomtype  = StringVar()
Roomcharges= StringVar()
Roomnumber= StringVar()


# entry feild for all labels
e1 = Entry(lf1, bd=4,textvariable=NameofthePatient)
e1.place(x=100, y=100, width=470)
e2 = Entry(lf1, bd=4,textvariable=PatientID)
e2.place(x=100, y=200, width=470)
e3 = Entry(lf1, bd=4,textvariable=Dateadmitted)
e3.place(x=100, y=300, width=470)
e4 = Entry(lf1, bd=4,textvariable=Datedischarged)
e4.place(x=100, y=400, width=470)
e5 = Entry(lf1, bd=4,textvariable=Roomtype)
e5.place(x=800, y=100, width=470)
e6 = Entry(lf1, bd=4,textvariable=Roomcharges)
e6.place(x=800, y=200, width=470)
e7 = Entry(lf1, bd=4,textvariable=Roomnumber)
e7.place(x=800, y=300, width=470)

def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("error","all feilds are required")
    else:
        con=mysql.connector.connect(host="localhost",username="root",password="Sai@2004",database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into roomall values(%s,%s,%s,%s,%s,%s,%s)",(
            NameofthePatient.get(),
            PatientID.get(),
            Dateadmitted.get(),
            Datedischarged.get(),
            Roomtype.get(),
            Roomcharges.get(),
            Roomnumber.get()
        ))
        con.commit()
        con.close()
        messagebox.showinfo("sucess","record has been inserted")
def fetch_data():
    con = mysql.connector.connect(host="localhost", username="root", password="Sai@2004", database="mydata")
    my_cursor = con.cursor()
    my_cursor.execute("select * from appform")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert("",END,values=items)
        con.commit()
    con.close()
def get_data(event=''):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data["values"]
    NameofthePatient.set(row[0])
    PatientID.set(row[1])
    Dateadmitted.set(row[2])
    Datedischarged.set(row[3])
    Roomtype.set(row[4])
    Roomcharges.set(row[5])
    Roomnumber.set(row[6])

def exit():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to exit')
    if confirm>0:
        win.destroy()
        return

 
def clear():
    NameofthePatient.set("")
    PatientID.set("")
    Dateadmitted.set("")
    Datedischarged.set("")
    Roomtype.set("")
    Roomcharges.set("")   
    Roomnumber.set("")  

table = ttk.Treeview( columns=('NameofthePatient', 'PatientID', 'Dateadmitted', 'Datedischarged','Roomtype', 'Roomcharges','Roomnumber'))  

# exit button
c_btn = Button(win, text="exit", font="ariel 15 bold", bg="red", fg="white", bd=6, cursor="hand2",command=exit)
c_btn.place(x=300, y=750, width=270)
# clear button
c_btn = Button(win, text="clear", font="ariel 15 bold", bg="blue", fg="white", bd=6, cursor="hand2",command=clear)
c_btn.place(x=780, y=750, width=270)
# Save button
p_btn = Button(win, text="Save", font="ariel 15 bold", bg="green", fg="white", bd=6, cursor="hand2",command=pd)
p_btn.place(x=540, y=750, width=270)

fetch_data()
mainloop()