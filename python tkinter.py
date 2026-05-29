import tkinter as tk
from tkinter import messagebox
import pymysql as sql

#Register
def register():
    name=rg_name.get()
    phone=rg_phone.get()
    email=rg_email.get()
    password=rg_ps.get()
    if not all ([name,phone,email,password]):
        messagebox.showwarning("Fieid warthing","Please fill all the fields")
        return None
    if len(phone) != 10:
        messagebox.showwarning("Fieid warthing","Phone number should be 10 digits")
        return None
    try:
        db=sql.connect(user="root",password="12345",host="localhost",database="mohan_tech",port=3306)
        cur =  db.cursor()
        cur.execute("""insert into users(name,email,phone,password) values (%s,%s,%s,%s)""",(name,email,phone,password))
        db.commit()
        db.close()
        messagebox.showinfo("Success", "User Registered")
    except Exception as e:
        messagebox.showerror("Error","User Registered Error",e)

def login():
    email=lg_email.get()
    password=lg_ps.get()
    if not all ([email,password]):
        messagebox.showwarning("Fieid warthing","Please fill all the fields")
    try:
        db = sql.connect(user="root", password="12345", host="localhost", database="mohan_tech", port=3306)
        cur = db.cursor()
        cur.execute((""" select * from users where email = %s and password=%s """),(email,password))
        if cur.fetchone():
            messagebox.showinfo("Success", "User Logged In")
            wg.tkraise()
        else:
            messagebox.showerror("Error","User Logged Failed")
        db.commit()
        db.close()
    except Exception as e:
        messagebox.showerror("Error","User Logged Error",e)

#tkinter
main = tk.Tk()
main.geometry("1366x768")
main.title("mohan")

# container frame
container = tk.Frame(main, bg="black")

# Signup frame
sg = tk.Frame(container, bg="lightblue")

# Login frame
lg = tk.Frame(container, bg="lightgreen")

# Welcome frame
wg = tk.Frame(container, bg="yellow")

for page in (container, sg, lg, wg):
    page.place(x=0, y=0, width=1366, height=768)

#singup page
#titele
tk.Label(sg, text="Singup From", bg="lightblue",fg="white",font=("Arial bold",35)).place(x=550,y=100)
#user name
tk.Label(sg,text="User Name :",bg="lightblue",fg="white",font=("Arial bold",28)).place(x=430,y=180)
rg_name = tk.Entry(sg,bg="white",fg="black",font=("Arial bold",20))
rg_name.place(x=700,y=190)
#User Phone
tk.Label(sg,text="User Phone :",bg="lightblue",fg="white",font=("Arial bold",28)).place(x=430,y=260)
rg_phone = tk.Entry(sg,bg="white",fg="black",font=("Arial bold",20))
rg_phone.place(x=700,y=270)
#User Email
tk.Label(sg,text="User Email :",bg="lightblue",fg="white",font=("Arial bold",28)).place(x=430,y=340)
rg_email = tk.Entry(sg,bg="white",fg="black",font=("Arial bold",20))
rg_email.place(x=700,y=350)
#User Password
tk.Label(sg,text="Password :",bg="lightblue",fg="white",font=("Arial bold",28)).place(x=430,y=420)
rg_ps = tk.Entry(sg,bg="white",fg="black",font=("Arial bold",20))
rg_ps.place(x=700,y=430)
#login page button
tk.Button(sg,text="Login",bg="gray",fg="white",font=("Arial bold",15),command=lambda:lg.tkraise()).place(x=700,y=500)
tk.Button(sg,text="Register",bg="gray",fg="white",font=("Arial bold",15),command=register).place(x=780,y=500)

#Login Page
#titele
tk.Label(lg, text="Login From", bg="lightgreen",fg="white",font=("Arial bold",35)).place(x=550,y=100)
#user name
tk.Label(lg,text="Email Id  :",bg="lightgreen",fg="white",font=("Arial bold",28)).place(x=430,y=180)
lg_email = tk.Entry(lg,bg="white",fg="black",font=("Arial bold",20))
lg_email.place(x=700,y=190)
#password
tk.Label(lg,text="Password :",bg="lightgreen",fg="white",font=("Arial bold",28)).place(x=430,y=260)
lg_ps = tk.Entry(lg,bg="white",fg="black",font=("Arial bold",20),show="*")
lg_ps.place(x=700,y=270)
#Welcome Page
tk.Button(lg,text="sing",bg="gray",fg="white",font=("Arial bold",15),command=lambda:sg.tkraise()).place(x=700,y=320)
tk.Button(lg,text="Login",bg="gray",fg="white",font=("Arial bold",15),command=login).place(x=780,y=320)

sg.tkraise()
main.mainloop()