from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# import mainpage as Mpage

import mysql.connector

win = Tk()
win.state('zoomed')
win.config(bg='black')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~button function~~~~~~
def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("error","all feilds are required")
    else:
        con=mysql.connector.connect(host="localhost",username="root",password="Sai@2004",database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            dob.get(),
            bloodpressure.get(),
            storage.get(),
            medication.get(),
            patientid.get(),
            patientaddress.get(),
            nameofpatient.get()
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("sucess","record has been inserted")
def fetch_data():
    con = mysql.connector.connect(host="localhost", username="root", password="Sai@2004", database="mydata")
    my_cursor = con.cursor()
    my_cursor.execute("select * from hospital")
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
    nameoftablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablets.set(row[3])
    issuedate.set(row[4])
    expdate.set(row[5])
    dailydose.set(row[6])
    sideeffect.set(row[7])
    dob.set(row[8])
    bloodpressure.set(row[9])
    storage.set(row[10])
    medication.set(row[11])
    patientid.set(row[12])
    patientaddress.set(row[13])
    nameofpatient.set(row[14])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~`prescrption data
def pre():
    txt_frme.insert(END,"Name of tablets:\t\t\t"+nameoftablets.get()+'\n')
    txt_frme.insert(END,"Refrence no:\t\t\t"+ref.get()+'\n')
    txt_frme.insert(END, "Dose:\t\t\t" + dose.get() + '\n')
    txt_frme.insert(END, "No of tablets:\t\t\t" + nooftablets.get() + '\n')
    txt_frme.insert(END, "issued date:\t\t\t" + issuedate.get() + '\n')
    txt_frme.insert(END, "exp date:\t\t\t" + expdate.get() + '\n')
    txt_frme.insert(END,"daily dose:\t\t\t"+dailydose.get()+'\n')
    txt_frme.insert(END, "side effects:\t\t\t" + sideeffect.get() + '\n')
    txt_frme.insert(END, "DOB:\t\t\t" + dob.get() + '\n')
    txt_frme.insert(END, "bloodpressure:\t\t\t" + bloodpressure.get() + '\n')
    txt_frme.insert(END, "storage device:\t\t\t" + storage.get() + '\n')
    txt_frme.insert(END, "medication:\t\t\t" + medication.get() + '\n')
    txt_frme.insert(END, "patient id:\t\t\t" + patientid.get() + '\n')
    txt_frme.insert(END, "patient address:\t\t\t" + patientaddress.get() + '\n')
    txt_frme.insert(END, "name of patient:\t\t\t" + nameofpatient.get() + '\n')
#~~~~~~~~~~~`delete button~~~~~~~~~
def delete():
    con = mysql.connector.connect(host="localhost", username="root", password="Sai@2004", database="mydata")
    my_cursor = con.cursor()
    querry = ('delete from hospital where Reference = %s')
    value = (ref.get(),)
    my_cursor.execute(querry, value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo("deleted", "patient data has been deleted")
#~~~~~~~~~~~~~~~~~~~~~~~~~~clearbutton
def clear():
    nameoftablets.set("")
    ref.set("")
    dose.set("")
    nooftablets.set("")
    issuedate.set("")
    expdate.set("")
    dailydose.set("")
    sideeffect.set("")
    bloodpressure.set("")
    storage.set("")
    medication.set("")
    patientid.set("")
    nameofpatient.set("")
    dob.set("")
    patientaddress.set("")
    txt_frme.delete(1.0,END)
#~~~~~~~~~~~~~~~~exit
def exit():
    confirm=messagebox.askyesno('confirmation','are you sure you want to exit')
    if confirm>0:
        win.destroy()
        return

# HEADING
Label(win, text="MMK CONVULSENTORY SOLUTIONS", font="impack 31 bold", bg="blue", fg="white").pack(fill=X)

# FRAME1
frame1 = Frame(win, bd=15, relief=RIDGE)
frame1.place(x=0, y=54, width=1520, height=310)
# label frame for patient info
lf1 = LabelFrame(frame1, text="patient information", font="arial 10 bold", bd=10, bg="pink")
lf1.place(x=10, y=0, width=800, height=280)
# label frame for patient information
Label(lf1, text="name of tablets", bg="pink").place(x=5, y=10)
Label(lf1, text="refrence no", bg="pink").place(x=5, y=40)
Label(lf1, text="dose", bg="pink").place(x=5, y=70)
Label(lf1, text="no of tablets", bg="pink").place(x=5, y=100)
Label(lf1, text="issue date", bg="pink").place(x=5, y=130)
Label(lf1, text="exp.date", bg="pink").place(x=5, y=160)
Label(lf1, text="daily dose", bg="pink").place(x=5, y=190)
Label(lf1, text="side effects", bg="pink").place(x=5, y=220)
Label(lf1, text="blood pressure", bg="pink").place(x=370, y=20)
Label(lf1, text="storage device", bg="pink").place(x=370, y=50)
Label(lf1, text="medication", bg="pink").place(x=370, y=80)
Label(lf1, text="patient id", bg="pink").place(x=370, y=110)
Label(lf1, text="patient name", bg="pink").place(x=370, y=140)
Label(lf1, text="patient dob", bg="pink").place(x=370, y=170)
Label(lf1, text="patient address", bg="pink").place(x=370, y=200)
#text variables for evry entry feild
nameoftablets = StringVar()
ref = StringVar()
dose= StringVar()
nooftablets = StringVar()
issuedate = StringVar()
expdate= StringVar()
dailydose = StringVar()
sideeffect = StringVar()
bloodpressure = StringVar()
storage = StringVar()
medication = StringVar()
patientid = StringVar()
nameofpatient = StringVar()
dob = StringVar()
patientaddress = StringVar()









# entry feild for all labels
e1 = Entry(lf1, bd=4,textvariable=nameoftablets)
e1.place(x=130, y=10, width=200)
e2 = Entry(lf1, bd=4,textvariable=ref)
e2.place(x=130, y=40, width=200)
e3 = Entry(lf1, bd=4,textvariable=dose)
e3.place(x=130, y=70, width=200)
e4 = Entry(lf1, bd=4,textvariable=nooftablets)
e4.place(x=130, y=100, width=200)
e5 = Entry(lf1, bd=4,textvariable=issuedate)
e5.place(x=130, y=130, width=200)
e6 = Entry(lf1, bd=4,textvariable=expdate)
e6.place(x=130, y=160, width=200)
e7 = Entry(lf1, bd=4,textvariable=dailydose)
e7.place(x=130, y=190, width=200)
e8 = Entry(lf1, bd=4,textvariable=sideeffect)
e8.place(x=130, y=220, width=200)
e9 = Entry(lf1, bd=4,textvariable=dob)
e9.place(x=470, y=170, width=200)
e10 = Entry(lf1, bd=4,textvariable=bloodpressure)
e10.place(x=470, y=20, width=200)
e11 = Entry(lf1, bd=4,textvariable=storage)
e11.place(x=470, y=50, width=200)
e12 = Entry(lf1, bd=4,textvariable=medication)
e12.place(x=470, y=80, width=200)
e13 = Entry(lf1, bd=4,textvariable=patientid)
e13.place(x=470, y=110, width=200)
e14 = Entry(lf1, bd=4,textvariable=patientaddress)
e14.place(x=470, y=200, width=200)
e15 = Entry(lf1, bd=4,textvariable=nameofpatient)
e15.place(x=470, y=140, width=200)



# label frame for prescription
lf2 = LabelFrame(frame1, text="prescription", font="arial 12 bold", bd=10, bg="green")
lf2.place(x=920, y=0, width=510, height=280)
# textbox for prescrption
txt_frme = Text(lf2, font="impack 10 bold", width=40, height=30, bg="yellow")
txt_frme.pack(fill=BOTH)
# FRAME2
frame2 = Frame(win, bd=15, relief=RIDGE)
frame2.place(x=0, y=360, width=1550, height=350)
# delete button
d_btn = Button(win, text="delete", font="ariel 15 bold", bg="brown", fg="white", bd=6, cursor="hand2",command=delete)
d_btn.place(x=0, y=700, width=270)
# prescription button
p_btn = Button(win, text="prescription", font="ariel 15 bold", bg="purple", fg="white", bd=6, cursor="hand2",command=pre)
p_btn.place(x=270, y=700, width=270)
# prescription  data button
pd_btn = Button(win, text="save prescription data", font="ariel 15 bold", bg="green", fg="white", bd=6, cursor="hand2",command=pd)
pd_btn.place(x=540, y=700, width=270)
# clear button
c_btn = Button(win, text="clear", font="ariel 15 bold", bg="blue", fg="white", bd=6, cursor="hand2",command=clear)
c_btn.place(x=810, y=700, width=270)
# exit button
c_btn = Button(win, text="exit", font="ariel 15 bold", bg="red", fg="white", bd=6, cursor="hand2",command=exit)
c_btn.place(x=1080, y=700, width=270)
# SCROLL bar for prescrption data
scroll_x = ttk.Scrollbar(frame2, orient=HORIZONTAL)
scroll_x.pack(side='bottom', fill="x")
scroll_y = ttk.Scrollbar(frame2, orient=VERTICAL)
scroll_y.pack(side='right', fill="y")

table = ttk.Treeview(frame2, columns=('not', 'ref', 'dose', 'nots','issd', 'expd', 'dd', 'sd', 'dob', 'bp', 'st', 'med', 'id', 'pa', 'pn'),
                     xscrollcommand=scroll_y.set, yscrollcommand=scroll_x.set)
scroll_x = ttk.Scrollbar(command=table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)
# heading for prescrption data
table.heading('not', text='name of tablets')
table.heading('ref', text='refrence no')
table.heading('dose', text='dose')
table.heading('nots', text='no of tablets')
table.heading('issd', text='issue date')
table.heading('expd', text='exp.date')
table.heading('dd', text='daily dose')
table.heading('sd', text='side effects')
table.heading('dob', text='patient dob')
table.heading('bp', text='blood pressure')
table.heading('st', text='storage device')
table.heading('med', text='medication')
table.heading('id', text='patient id')
table.heading('pa', text='patient address')
table.heading('pn', text='patient name')


table['show'] = 'headings'
table.pack(fill=BOTH, expand=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
table.column('not',width=100)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('dob',width=100)
table.column('bp',width=100)
table.column('st',width=100)
table.column('med',width=100)
table.column('id',width=100)
table.column('pa',width=100)
table.column('pn',width=100)
table.bind('<ButtonRelease-1>',get_data)

# if __name__ == "__main__":
#     root = Tk()
#     obj = Mpage(root)
#     root.mainloop()

fetch_data()
mainloop()
