import tkinter as tk
from tkinter import ttk
import main

# Load employee data from JSON file
main.load_employees()

# Create main application window
window=tk.Tk()
window.title("Employee Management System")
window.configure(bg="#f4f6f7")

window.geometry("500x450")

# Center the window on screen
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=(screen_width/2)-(500/2)
y=(screen_height/2)-(450/2)

window.geometry(f"500x450+{int(x)}+{int(y)}")
window.resizable(False,False)


# Button hover effects
def on_enter(e):
    e.widget["background"]="#2980b9"

def on_leave(e):
    e.widget["background"]="#3498db"


# Window to add a new employee
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

    # Save employee to list and JSON file
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


# Function to sort table columns
def sort_column(tree,col,reverse):
    data=[(tree.set(k,col),k) for k in tree.get_children("")]
    try:
        data.sort(key=lambda t:int(t[0]),reverse=reverse)
    except:
        data.sort(reverse=reverse)

    for index,(val,k) in enumerate(data):
        tree.move(k,"",index)

    tree.heading(col,command=lambda:sort_column(tree,col,not reverse))


# Window to display all employees in table format
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

    # Add scrollbar
    scroll=ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)

    scroll.pack(side="right",fill="y")
    tree.pack(fill="both",expand=True)

    # Insert employee data into table
    for emp in main.employees:
        tree.insert("",tk.END,values=(emp["id"],emp["name"],emp["age"],emp["department"]))

    tk.Button(win,text="Back",command=win.destroy).pack(pady=10)


# Search employee by name
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


# Delete employee using ID
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

        for emp in main.employees:
            if emp["id"]==eid:
                main.employees.remove(emp)
                main.reassign_employee_ids()
                main.save_employees()
                result.config(text="Employee deleted")
                return

        result.config(text="Invalid ID")

    tk.Button(win,text="Delete",command=delete).pack(pady=5)
    tk.Button(win,text="Back",command=win.destroy).pack(pady=5)


# Update employee information
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


# Show department statistics
def statistics():
    win=tk.Toplevel(window)
    win.title("Statistics")
    win.geometry("300x250")

    stats={}
    for emp in main.employees:
        dept=emp["department"]
        stats[dept]=stats.get(dept,0)+1

    for dept,count in stats.items():
        tk.Label(win,text=f"{dept} : {count}").pack()

    tk.Label(win,text=f"Total Employees : {len(main.employees)}").pack(pady=10)

    tk.Button(win,text="Back",command=win.destroy).pack()


# Application title
title=tk.Label(window,text="Employee Management System",font=("Segoe UI",20,"bold"),bg="#f4f6f7",fg="#2c3e50")
title.pack(pady=30)

button_frame=tk.Frame(window,bg="#f4f6f7")
button_frame.pack()

# Button styling
btn_style={"width":25,"height":1,"font":("Segoe UI",11),"bg":"#3498db","fg":"white","bd":0,"cursor":"hand2","pady":5}

# Button list
buttons=[
("Add Employee",add_employee),
("View Employees",view_employees),
("Search Employee",search_employee),
("Delete Employee",delete_employee),
("Update Employee",update_employee),
("Show Statistics",statistics)
]

# Create buttons dynamically
for text,cmd in buttons:
    b=tk.Button(button_frame,text=text,command=cmd,**btn_style)
    b.pack(pady=6)
    b.bind("<Enter>",on_enter)
    b.bind("<Leave>",on_leave)

# Exit button
exit_btn=tk.Button(window,text="Exit",width=25,font=("Segoe UI",11),bg="#e74c3c",fg="white",bd=0,cursor="hand2",command=window.destroy)
exit_btn.pack(pady=20)

# Run the GUI application
window.mainloop()
