import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.insert(0, select['pp_id'])
    e2.insert(0, select['name'])
    e3.insert(0, select['mobile'])
    e4.insert(0, select['gmail'])


def Add():
    passport_id = e1.get()
    name = e2.get()
    mobile = e3.get()
    gmail = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="passport3")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  registation (pp_id,name,mobile,gmail) VALUES (%s, %s, %s, %s)"
        val = (passport_id, name, mobile, gmail)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "passport inserted successfully...")
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="passport3")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT pp_id,name,mobile,gmail FROM registation")
    records = mycursor.fetchall()
    print(records)

    for i, (pp_id, name, mobile, gmail) in enumerate(records, start=1):
        mysqldb.close()


root = Tk()
root.geometry("800x500")
root.title("Passport vertification")
global e1
global e2
global e3
global e4

tk.Label(root, text="Passport Registation form", fg="pink", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Passport ID").place(x=70, y=10)
Label(root, text="Name").place(x=70, y=40)
Label(root, text="Mobile").place(x=70, y=70)
Label(root, text="gmail").place(x=70, y=100)
c = StringVar()
var = IntVar()
label_4 = Label(root, text="country", width=20, font=("bold", 10))
label_4.place(x=30, y=130)
list1 = ['Canada', 'australia', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa'];

droplist = OptionMenu(root, c, *list1)
droplist.config(width=20)
c.set("select your country")
droplist.place(x=70, y=150)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=235, y=200)

Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Process to submit", bg="#A89166", command=Add, height=2, width=13).place(x=360, y=290)

root.mainloop()
