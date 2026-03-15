import tkinter as tk
<<<<<<< HEAD
from tkinter import ttk
=======
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b
import main

main.load_employees()

window=tk.Tk()
<<<<<<< HEAD
icon = tk.PhotoImage(file="icon.png")
window.iconphoto(False, icon)
window.title("Employee Management System")
window.configure(bg="#f4f6f7")

window.geometry("500x450")

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=(screen_width/2)-(500/2)
y=(screen_height/2)-(450/2)

window.geometry(f"500x450+{int(x)}+{int(y)}")
window.resizable(False,False)
=======
window.title("Employee Management System")
window.geometry("420x500")
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b

def add_employee():
    win=tk.Toplevel(window)
    win.title("Add Employee")
    win.geometry("300x250")

    tk.Label(win,text="Name").pack()
    name=tk.Entry(win)
    name.pack()

    tk.Label(win,text="Age").pack()
    age=tk.Entry(win)
    age.pack()

    tk.Label(win,text="Department").pack()
    dept=tk.Entry(win)
    dept.pack()

    def submit():
        new_emp={
            "id":main.generate_employee_id(),
            "name":name.get(),
            "age":int(age.get()),
            "department":dept.get()
        }
        main.employees.append(new_emp)
        main.save_employees()
        win.destroy()

    tk.Button(win,text="Submit",command=submit).pack(pady=5)
    tk.Button(win,text="Back",command=win.destroy).pack(pady=5)

<<<<<<< HEAD
=======
import tkinter as tk
from tkinter import ttk
import main

from tkinter import ttk
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b

def sort_column(tree,col,reverse):
    data=[(tree.set(k,col),k) for k in tree.get_children("")]
    try:
        data.sort(key=lambda t:int(t[0]),reverse=reverse)
    except:
        data.sort(reverse=reverse)
    for index,(val,k) in enumerate(data):
        tree.move(k,"",index)
    tree.heading(col,command=lambda:sort_column(tree,col,not reverse))

<<<<<<< HEAD

=======
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b
def view_employees():
    win=tk.Toplevel(window)
    win.title("Employees")
    win.geometry("700x400")

    frame=tk.Frame(win)
    frame.pack(fill="both",expand=True)

    tree=ttk.Treeview(frame,columns=("ID","Name","Age","Department"),show="headings")

    tree.heading("ID",text="ID",command=lambda:sort_column(tree,"ID",False))
    tree.heading("Name",text="Name",command=lambda:sort_column(tree,"Name",False))
    tree.heading("Age",text="Age",command=lambda:sort_column(tree,"Age",False))
    tree.heading("Department",text="Department",command=lambda:sort_column(tree,"Department",False))

    tree.column("ID",width=60,anchor="center")
    tree.column("Name",width=200)
    tree.column("Age",width=80,anchor="center")
    tree.column("Department",width=200)

    scroll_y=ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
    tree.configure(yscrollcommand=scroll_y.set)

    scroll_y.pack(side="right",fill="y")
    tree.pack(fill="both",expand=True)

    for emp in main.employees:
        tree.insert("",tk.END,values=(emp["id"],emp["name"],emp["age"],emp["department"]))

    tk.Button(win,text="Back",command=win.destroy).pack(pady=10)


def search_employee():
    win=tk.Toplevel(window)
    win.title("Search Employee")
    win.geometry("300x200")

    tk.Label(win,text="Enter Name").pack()
    name=tk.Entry(win)
    name.pack()

    result=tk.Label(win,text="")
    result.pack(pady=10)

    def search():
        for emp in main.employees:
            if emp["name"].lower()==name.get().lower():
                result.config(text=f"{emp['id']} | {emp['name']} | {emp['age']} | {emp['department']}")
                return
        result.config(text="Employee not found")

    tk.Button(win,text="Search",command=search).pack(pady=5)
    tk.Button(win,text="Back",command=win.destroy).pack(pady=5)

<<<<<<< HEAD

=======
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b
def delete_employee():
    win=tk.Toplevel(window)
    win.title("Delete Employee")
    win.geometry("300x200")

    tk.Label(win,text="Enter Employee ID").pack()

    emp_id=tk.Entry(win)
    emp_id.pack()

    result=tk.Label(win,text="")
    result.pack(pady=5)

    def delete():
        try:
            eid=int(emp_id.get())
        except:
            result.config(text="Invalid input")
            return

        found=False

        for emp in main.employees:
            if emp["id"]==eid:
                main.employees.remove(emp)
                main.reassign_employee_ids()
                main.save_employees()
                result.config(text="Employee deleted")
                found=True
                break

        if not found:
            result.config(text="Invalid ID, try again")

    tk.Button(win,text="Delete",command=delete).pack(pady=5)
    tk.Button(win,text="Back",command=win.destroy).pack(pady=5)
<<<<<<< HEAD


=======
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b
def update_employee():
    win=tk.Toplevel(window)
    win.title("Update Employee")
    win.geometry("300x300")

    tk.Label(win,text="Employee Name").pack()
    name=tk.Entry(win)
    name.pack()

    tk.Label(win,text="New Name").pack()
    new_name=tk.Entry(win)
    new_name.pack()

    tk.Label(win,text="New Age").pack()
    new_age=tk.Entry(win)
    new_age.pack()

    tk.Label(win,text="New Department").pack()
    new_dept=tk.Entry(win)
    new_dept.pack()

    def update():
        for emp in main.employees:
            if emp["name"].lower()==name.get().lower():
                emp["name"]=new_name.get()
                emp["age"]=int(new_age.get())
                emp["department"]=new_dept.get()
                main.save_employees()
                break
        win.destroy()

    tk.Button(win,text="Update",command=update).pack(pady=5)
    tk.Button(win,text="Back",command=win.destroy).pack(pady=5)

<<<<<<< HEAD

=======
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b
def statistics():
    win=tk.Toplevel(window)
    win.title("Statistics")
    win.geometry("300x250")

    stats={}
    for emp in main.employees:
        dept=emp["department"]
        if dept in stats:
            stats[dept]+=1
        else:
            stats[dept]=1

    for dept,count in stats.items():
        tk.Label(win,text=f"{dept} : {count}").pack()

    tk.Label(win,text=f"Total Employees : {len(main.employees)}").pack(pady=10)

    tk.Button(win,text="Back",command=win.destroy).pack()

<<<<<<< HEAD

title=tk.Label(window,text="Employee Management System",font=("Segoe UI",20,"bold"),bg="#f4f6f7",fg="#2c3e50")
title.pack(pady=30)

button_frame=tk.Frame(window,bg="#f4f6f7")
button_frame.pack()

btn_style={"width":25,"height":1,"font":("Segoe UI",11),"bg":"#3498db","fg":"white","bd":0,"cursor":"hand2","pady":5}
def on_enter(e):
    e.widget["background"]="#2980b9"

def on_leave(e):
    e.widget["background"]="#3498db"

b1=tk.Button(button_frame,text="Add Employee",command=add_employee,**btn_style)
b1.pack(pady=6)
b1.bind("<Enter>",on_enter)
b1.bind("<Leave>",on_leave)

b2=tk.Button(button_frame,text="View Employees",command=view_employees,**btn_style)
b2.pack(pady=6)
b2.bind("<Enter>",on_enter)
b2.bind("<Leave>",on_leave)

b3=tk.Button(button_frame,text="Search Employee",command=search_employee,**btn_style)
b3.pack(pady=6)
b3.bind("<Enter>",on_enter)
b3.bind("<Leave>",on_leave)

b4=tk.Button(button_frame,text="Delete Employee",command=delete_employee,**btn_style)
b4.pack(pady=6)
b4.bind("<Enter>",on_enter)
b4.bind("<Leave>",on_leave)

b5=tk.Button(button_frame,text="Update Employee",command=update_employee,**btn_style)
b5.pack(pady=6)
b5.bind("<Enter>",on_enter)
b5.bind("<Leave>",on_leave)

b6=tk.Button(button_frame,text="Show Statistics",command=statistics,**btn_style)
b6.pack(pady=6)
b6.bind("<Enter>",on_enter)
b6.bind("<Leave>",on_leave)

exit_btn=tk.Button(window,text="Exit",width=25,font=("Segoe UI",11),bg="#e74c3c",fg="white",activebackground="#c0392b",bd=0,cursor="hand2")
exit_btn.config(command=window.destroy)
exit_btn.pack(pady=20)
=======
tk.Label(window,text="Employee Management System",font=("Arial",18)).pack(pady=20)

tk.Button(window,text="Add Employee",width=22,command=add_employee).pack(pady=5)
tk.Button(window,text="View Employees",width=22,command=view_employees).pack(pady=5)
tk.Button(window,text="Search Employee",width=22,command=search_employee).pack(pady=5)
tk.Button(window,text="Delete Employee",width=22,command=delete_employee).pack(pady=5)
tk.Button(window,text="Update Employee",width=22,command=update_employee).pack(pady=5)
tk.Button(window,text="Show Statistics",width=22,command=statistics).pack(pady=5)
tk.Button(window,text="Exit",width=22,command=window.destroy).pack(pady=5)
>>>>>>> a0bfb7613958fc8dedf9592137f7b86f3e10db6b

window.mainloop()