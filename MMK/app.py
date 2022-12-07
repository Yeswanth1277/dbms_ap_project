from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
from tkinter import font
import sqlite3

win = Tk()
win.state('zoomed')
win.config(bg='green')

def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("error","all feilds are required")
    else:
        con=mysql.connector.connect(host="localhost",username="root",password="Sai@2004",database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into appform values(%s,%s,%s,%s,%s,%s)",(
            patientid.get(),
            doctorid.get(),
            appointmentno.get(),
            AppointmentTime.get(),
            Appointmentdate.get(),
            description.get()
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
    patientid.set(row[0])
    doctorid.set(row[1])
    appointmentno.set(row[2])
    AppointmentTime.set(row[3])
    Appointmentdate.set(row[4])
    description.set(row[5])

#~~~~~~~~~~~~~~~~~~~~~~`
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~`prescrption data
# def pre():
#     txt_frme.insert(END,"Name of tablets:\t\t\t"+patientid.get()+'\n')
#     txt_frme.insert(END,"Refrence no:\t\t\t"+doctorid.get()+'\n')
#     txt_frme.insert(END, "Dose:\t\t\t" + appointmentno.get() + '\n')
#     txt_frme.insert(END, "No of tablets:\t\t\t" + AppointmentTime.get() + '\n')
#     txt_frme.insert(END, "issued date:\t\t\t" + Appointmentdate.get() + '\n')
#     txt_frme.insert(END, "exp date:\t\t\t" + description.get() + '\n')
# def search():
#     con = mysql.connector.connect(host="localhost", username="root", password="Sai@2004", database="mydata")
#     my_cursor = con.cursor()
#     global myresult
#     studname = e1.get()
#     coursename = e2.get()
#     fee = e3.get()
 
#     try:
#         mycursor.execute("SELECT * FROM record where id = '" + studname + "'")
#         myresult = mycursor.fetchall()
 
#         for x in myresult:
#             print(x)
#         e2.delete(0, END)
#         e2.insert(END, x[2])
#         e3.delete(0, END)
#         e3.insert(END, x[3])
 
#     except Exception as e:
#        print(e)
#        mysqldb.rollback()
#        mysqldb.close()
 
# root = Tk()
# root.title("Search Mysql")
# root.geometry("300x200")
 
# Label(root, text="Student ID").place(x=10, y=10)
# Button(root, text="Search", command=Ok ,height = 1, width = 13).place(x=140, y=40)
# Label(root, text="Course").place(x=10, y=80)
# Label(root, text="Fee").place(x=10, y=120)
 
# e1 = Entry(root)
# e1.place(x=140, y=10)
 
# e2 = Entry(root)
# e2.place(x=140, y=80)
 
# e3 = Entry(root)
# e3.place(x=140, y=120)
 
# root.mainloop()

#~~~~~~~~~~~clear
def clear():
    patientid.set("")
    doctorid.set("")
    appointmentno.set("")
    AppointmentTime.set("")
    Appointmentdate.set("")
    description.set("")
    # txt_frme.delete(1.0,END)

def exit():
    confirm=messagebox.askyesno('confirmation','are you sure you want to exit')
    if confirm>0:
        win.destroy()
        return


    
#frmae 1
frame1 = Frame(win, bd=15, relief=RIDGE)
frame1.place(x=50, y=200, width=1420, height=550,)
# label frame for patient info
lf1 = LabelFrame(frame1, text="Enter Patient Details", font="arial 40 bold", bd=10, bg="pink")
lf1.place(x=0, y=0, width=1520, height=620)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~`Patient data

# label frame for Enter Patient Details
Label(lf1, text="Name of the Patient : ", bg="pink",font="arial 20 ").place(x=100, y=50)
Label(lf1, text="Patient ID : ", bg="pink",font="arial 20").place(x=100, y=150)
Label(lf1, text="Doctor ID : ", bg="pink",font="arial 20").place(x=100, y=250)
Label(lf1, text="Appointment Time(HH:MM:SS) : ", bg="pink",font="arial 20").place(x=800, y=50)
Label(lf1, text="Appointment date(YYYY-MM-DD) : ", bg="pink",font="arial 20").place(x=800, y=150)
Label(lf1, text="Description : ", bg="pink",font="arial 20").place(x=800, y=250)


#text variables for evry entry feild
patientid = StringVar()
doctorid = StringVar()
appointmentno= StringVar()
AppointmentTime = StringVar()
Appointmentdate = StringVar()
description= StringVar()


# entry feild for all labels
e1 = Entry(lf1, bd=4,textvariable=patientid)
e1.place(x=100, y=100, width=500)
e2 = Entry(lf1, bd=4,textvariable=doctorid)
e2.place(x=100, y=200, width=500)
e3 = Entry(lf1, bd=4,textvariable=appointmentno)
e3.place(x=100, y=300, width=500)
e4 = Entry(lf1, bd=4,textvariable=AppointmentTime)
e4.place(x=800, y=100, width=500)
e5 = Entry(lf1, bd=4,textvariable=Appointmentdate)
e5.place(x=800, y=200, width=500)
e6 = Entry(lf1, bd=4,textvariable=description)
e6.place(x=800, y=300, width=500)


# HEADING
Label(win, text="MMK CONVULSENTORY SOLUTIONS", font="impack 51 bold", bg="blue", fg="white").pack(fill=X)
Label(win, text="APPOINTMENT FORM", font="impack 31 bold", bg="brown", fg="white",pady="5px").pack(fill=X)

# frame2 = Frame(win, bd=15, relief=RIDGE)
# frame2.place(x=0, y=360, width=1550, height=350)
# scroll_x = ttk.Scrollbar(frame2, orient=HORIZONTAL)
# scroll_x.pack(side='bottom', fill="x")
# scroll_y = ttk.Scrollbar(frame2, orient=VERTICAL)
# scroll_y.pack(side='right', fill="y")
  
table = ttk.Treeview( columns=('patientid', 'doctorid', 'appointmentno', 'AppointmentTime','Appointmentdate', 'description'))
# scroll_x = ttk.Scrollbar(command=table.xview)
# scroll_y = ttk.Scrollbar(command=table.yview)

# FRAME2

# prescription  data button
pd_btn = Button(win, text="save", font="ariel 15 bold", bg="orange", fg="white", bd=6, cursor="hand2",command=pd)
pd_btn.place(x=500, y=750, width=270)
# clear button
c_btn = Button(win, text="clear", font="ariel 15 bold", bg="blue", fg="white", bd=6, cursor="hand2",command=clear)
c_btn.place(x=770, y=750, width=270)
# search button
# d_btn = Button(win, text="search", font="ariel 15 bold", bg="brown", fg="white", bd=6, cursor="hand2",command=search)
# d_btn.place(x=230, y=750, width=270)
# exit button
c_btn = Button(win, text="exit", font="ariel 15 bold", bg="red", fg="white", bd=6, cursor="hand2",command=exit)
c_btn.place(x=1040, y=750, width=270)


fetch_data()
mainloop()