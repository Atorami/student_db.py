from tkinter import *
from tkinter import ttk, messagebox


class Student:
    def __init__(self, name, surname, album_number):
        self.name = name
        self.surname = surname
        self.album_number = album_number


window = Tk()

db = []

student_name = StringVar(value='')
student_surname = StringVar(value='')
student_album = StringVar(value='')
student_album_id = StringVar(value='')


def show_all():
    for item in table.get_children():
        table.delete(item)

    for _ in db:
        table.insert('', END, values=(_.name, _.surname, _.album_number))
        # print(_.name, _.surname, _.album_number)


def save_student():
    name = student_name.get()
    surname = student_surname.get()
    album_number = student_album.get()

    for student in db:
        if student.album_number == album_number:
            messagebox.showerror("Error", "Student with the same album number already exists.")
            return

    db.append(Student(name, surname, album_number))

    student_name.set('')
    student_surname.set('')
    student_album.set('')

    messagebox.showinfo('Success', 'Student saved successfully')
    show_all()


def delete_student():
    album_id = student_album_id.get()
    found = False

    for student in db:
        if student.album_number == album_id:
            db.remove(student)
            messagebox.showinfo('Success', 'Student removed successfully')
            show_all()
            found = True
            break
        elif not found:
            messagebox.showerror('Error', 'Student dont exist')


def add_student_window():
    add_window = Toplevel(window)
    add_window.title('Add new student')
    add_window.geometry('300x170')
    add_window.resizable(width=False, height=False)

    student_name_label = Label(add_window, text='Student Name :')
    student_name_entry = Entry(add_window, textvariable=student_name)

    student_surname_label = Label(add_window, text='Student Surname :')
    student_surname_entry = Entry(add_window, textvariable=student_surname)

    student_album_label = Label(add_window, text='Student Album number :')
    student_album_entry = Entry(add_window, textvariable=student_album)

    save_btn = Button(add_window, text='Save Student', command=lambda: [save_student(), add_window.destroy()], width='15')

    student_name_label.pack()
    student_name_entry.pack()
    student_name_entry.focus()
    student_surname_label.pack()
    student_surname_entry.pack()
    student_album_label.pack()
    student_album_entry.pack()
    save_btn.pack(pady=10)

    Label(add_window).pack()


def delete_student_window():
    delete_window = Toplevel(window)
    delete_window.title('Delete student')
    delete_window.geometry('300x120')
    delete_window.resizable(width=False, height=False)

    student_id_label = Label(delete_window, text='Write student\'s album id :')
    student_id_entry = Entry(delete_window, textvariable=student_album_id)

    delete_btn = Button(delete_window, text='Delete Student', command=lambda: [delete_student(), delete_window.destroy()], width='15')

    student_id_label.pack(pady=5)
    student_id_entry.pack()
    delete_btn.pack(pady=5)


# Main window
window['bg'] = '#fafafa'
window.title('Student DB')
# window.geometry('800x600')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

window.resizable(width=False, height=False)
table_columns = ('student_name', 'student_surname', 'student_album_number')
table = ttk.Treeview(window, columns=table_columns, show='headings')
table.heading('student_name', text='Name')
table.heading('student_surname', text='Surname')
table.heading('student_album_number', text='Album Number')
frm_btn = Frame(window, relief=RAISED, bd=1)

btn1 = Button(frm_btn, text='Show all students', command=show_all, width='15')
btn2 = Button(frm_btn, text='Add student', command=add_student_window, width='15')
btn3 = Button(frm_btn, text='Delete student', command=delete_student_window, width='15')
btn4 = Button(frm_btn, text='Open file', width='15')
btn5 = Button(frm_btn, text='Save file', width='15')

btn1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn2.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn3.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn4.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn5.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

frm_btn.grid(row=0, column=0, sticky="ns")
table.grid(row=0, column=1, sticky="ns")

window.mainloop()
