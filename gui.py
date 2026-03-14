import tkinter as tk
import main

main.load_employees()

window=tk.Tk()
window.title("Employee Management System")
window.geometry("420x500")

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

import tkinter as tk
from tkinter import ttk
import main

from tkinter import ttk

def sort_column(tree,col,reverse):
    data=[(tree.set(k,col),k) for k in tree.get_children("")]
    try:
        data.sort(key=lambda t:int(t[0]),reverse=reverse)
    except:
        data.sort(reverse=reverse)
    for index,(val,k) in enumerate(data):
        tree.move(k,"",index)
    tree.heading(col,command=lambda:sort_column(tree,col,not reverse))

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

tk.Label(window,text="Employee Management System",font=("Arial",18)).pack(pady=20)

tk.Button(window,text="Add Employee",width=22,command=add_employee).pack(pady=5)
tk.Button(window,text="View Employees",width=22,command=view_employees).pack(pady=5)
tk.Button(window,text="Search Employee",width=22,command=search_employee).pack(pady=5)
tk.Button(window,text="Delete Employee",width=22,command=delete_employee).pack(pady=5)
tk.Button(window,text="Update Employee",width=22,command=update_employee).pack(pady=5)
tk.Button(window,text="Show Statistics",width=22,command=statistics).pack(pady=5)
tk.Button(window,text="Exit",width=22,command=window.destroy).pack(pady=5)

window.mainloop()