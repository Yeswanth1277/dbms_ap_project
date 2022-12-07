from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector

win = Tk()
win.state('zoomed')
win.config(bg='green')

# HEADING
Label(win, text="MMK CONVULSENTORY SOLUTIONS", font="impack 31 bold", bg="blue", fg="white").pack(fill=X)
Label(win, text="EMPLOYEE REGISTRATION FORM", font="impack 31 bold", bg="brown", fg="white",pady="5px").pack(fill=X)

#frmae 1
frame1 = Frame(win, bd=15, relief=RIDGE)
frame1.place(x=50, y=180, width=1450, height=700,)
# label frame for patient info
lf1 = LabelFrame(frame1, text="Employee Details", font="arial 25 bold", bd=10, bg="pink")
lf1.place(x=0, y=0, width=1520, height=670)


# label frame for Employee Details
Label(lf1, text="Employee ID : ", bg="pink",font="arial 20 ").place(x=800, y=50)
Label(lf1, text="Employee Name : ", bg="pink",font="arial 20").place(x=50, y=50)
Label(lf1, text="Age : ", bg="pink",font="arial 20").place(x=50, y=150)
Label(lf1, text="Gender: ", bg="pink",font="arial 20").place(x=50, y=250)
Label(lf1, text="Contact number : ", bg="pink",font="arial 20").place(x=50, y=350)
Label(lf1, text="Email : ", bg="pink",font="arial 20").place(x=50, y=450)
Label(lf1, text="Designation : ", bg="pink",font="arial 20").place(x=800, y=150)
Label(lf1, text="Experience : ", bg="pink",font="arial 20").place(x=800, y=250)
Label(lf1, text="Salary : ", bg="pink",font="arial 20").place(x=800, y=350)

#text variables for evry entry feild
EmployeeID = StringVar()
EmployeeName = StringVar()
Age= StringVar()
Gender = StringVar()
Contactnumber = StringVar()
Email= StringVar()
Designation = StringVar()
Experience = StringVar()
Salary = StringVar()

# entry feild for all labels
e1 = Entry(lf1, bd=4,textvariable=EmployeeID)
e1.place(x=300, y=50, width=400)
e2 = Entry(lf1, bd=4,textvariable=EmployeeName)
e2.place(x=300, y=150, width=400)
e3 = Entry(lf1, bd=4,textvariable=Age)
e3.place(x=300, y=250, width=400)
e4 = Entry(lf1, bd=4,textvariable=Gender)
e4.place(x=300, y=350, width=400)
e5 = Entry(lf1, bd=4,textvariable=Contactnumber)
e5.place(x=300, y=450, width=400)
e6 = Entry(lf1, bd=4,textvariable=Email)
e6.place(x=1000, y=50, width=400)
e7 = Entry(lf1, bd=4,textvariable=Designation)
e7.place(x=1000, y=150, width=400)
e8 = Entry(lf1, bd=4,textvariable=Experience)
e8.place(x=1000, y=250, width=400)
e9 = Entry(lf1, bd=4,textvariable=Salary)
e9.place(x=1000, y=350, width=400)

def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("error","all feilds are required")
    else:
        con=mysql.connector.connect(host="localhost",username="root",password="Sai@2004",database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into empform values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            EmployeeID.get(),
            EmployeeName.get(),
            Age.get(),
            Gender.get(),
            Contactnumber.get(),
            Email.get(),
            Designation.get(),
            Experience.get(),
            Salary.get()
        ))
        con.commit()
        con.close()
        messagebox.showinfo("sucess","record has been inserted")

def clear():
    EmployeeID.set("")
    EmployeeName.set("")
    Age.set("")
    Gender.set("")
    Contactnumber.set("")
    Email.set("")
    Designation.set("")
    Experience.set("")
    Salary.set("")

#~~~~~~~~~~~`delete button~~~~~~~~~
# def delete():
#     con = mysql.connector.connect(host="localhost", username="root", password="qwerty_123", database="mydata")
#     my_cursor = con.cursor()
#     querry = ('delete from hospital where Reference = %s')
#     value = (ref.get(),)
#     my_cursor.execute(querry, value)
#     con.commit()
#     con.close()
#     messagebox.showinfo("deleted", "patient data has been deleted")

def exit():
    confirm=messagebox.askyesno('Confirmation','Are you sure you want to exit')
    if confirm>0:
        win.destroy()
        return

# Save button
p_btn = Button(win, text="Save", font="ariel 15 bold", bg="green", fg="white", bd=6, cursor="hand2",command=pd)
p_btn.place(x=650, y=750, width=270)
# clear button
c_btn = Button(win, text="clear", font="ariel 15 bold", bg="blue", fg="white", bd=6, cursor="hand2",command=clear)
c_btn.place(x=400, y=750, width=270)
# delete button
# d_btn = Button(win, text="delete", font="ariel 15 bold", bg="brown", fg="white", bd=6, cursor="hand2",command=delete)
# d_btn.place(x=730, y=750, width=270)
# exit button
c_btn = Button(win, text="exit", font="ariel 15 bold", bg="red", fg="white", bd=6, cursor="hand2",command=exit)
c_btn.place(x=900, y=750, width=270)


mainloop()