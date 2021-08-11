
# A simple notepad application


from tkinter import *

from tkinter import messagebox

import sqlite3

conn = sqlite3.connect('file.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE files (
    name text,
    body text
)""")
'''

root = Tk()
root.geometry('800x800')
root.title('DAP Notepad')

pad = Text(root, height=500, width=700, bd=5)
pad.configure(state='normal')
pad.grid(row=0, column=0, padx=10, pady=10)


def new_file():
    pad = Text(root, height=500, width=700, bd=5)
    pad.configure(state='normal')
    pad.grid(row=0, column=0)


def save_file():
    new_win = Toplevel()

    new_win.title('Save File - DAP Notepad')

    save_labelframe = LabelFrame(new_win, text='Save File', fg='black')
    save_labelframe.grid(row=0, column=3, padx=100)

    name_label = Label(save_labelframe, text='File Name', fg='black')
    name_label.grid(row=1, column=0, padx=10, pady=10)

    name = Entry(save_labelframe, fg='black', bg='white', width=25)
    name.grid(row=1, column=1, padx=10, pady=10)

    def save_into_db():
        conn = sqlite3.connect('file.db')
        c = conn.cursor()

        c.execute("INSERT INTO files VALUES (?, ?)", (name.get(), pad.get(1.0, END)))

        conn.commit()
        conn.close()

        root.title(name.get() + ' - DAP Notepad')

        new_win.destroy()

    save = Button(save_labelframe, fg='black', bg='white', text='Save', command=save_into_db)
    save.grid(row=1, column=2, pady=10, padx=10)
    name.delete(0, END)


def open_file():
    new_win = Toplevel()

    new_win.title('Open File - DAP Notepad')

    open_labelframe = LabelFrame(new_win, text='Open File', fg='black')
    open_labelframe.grid(row=0, column=0, padx=10, pady=10)

    name_label = Label(open_labelframe, text='Open File', fg='black')
    name_label.grid(row=1, column=0, padx=10, pady=10)

    name_of_file = Entry(open_labelframe, fg='black', bg='white', width=25)
    name_of_file.grid(row=1, column=1, padx=10, pady=10)

    def open_from_db():
        conn = sqlite3.connect('file.db')
        c = conn.cursor()

        new_win2 = Toplevel()

        c.execute("SELECT * FROM files WHERE name LIKE (?)", (name_of_file.get(),))
        items = c.fetchall()
        print_items = ''
        for item in items:
            print_items += item[1]
        opened_file = Text(new_win2, height=200, width=300)
        new_win.destroy()
        opened_file.configure(state='normal')
        opened_file.insert(1.0, print_items)
        opened_file.grid(row=0, column=0, padx=10, pady=10)

    open = Button(open_labelframe, fg='black', bg='white', text='Open', command=open_from_db)
    open.grid(row=1, column=2, padx=10, pady=10)


def delete_file():
    new_win = Toplevel()

    new_win.title('Delete File - DAP Notepad')

    delete_file_label = Label(new_win, text='Delete File', fg='black')
    delete_file_label.grid(row=0, column=0, padx=10, pady=10)

    delete_file_name = Entry(new_win, width=25, fg='black', bg='white')
    delete_file_name.grid(row=0, column=1, padx=10, pady=10)

    def delete_from_database():
        conn = sqlite3.connect('file.db')
        c = conn.cursor()

        popup = messagebox.askyesno('Delete File?',
                                    'You have chosen to delete the file \'' + delete_file_name.get() + '\' This action cannot be reversed. Do you want to proceed?')

        if popup == 1:
            c.execute("DELETE from files WHERE name LIKE (?)", (delete_file_name.get(),))

        conn.commit()
        conn.close()

    delete_btn = Button(new_win, text='Delete', fg='black', bg='white', command=delete_from_database)
    delete_btn.grid(row=0, column=2, padx=10, pady=10)


def delete_all():
    conn = sqlite3.connect('file.db')
    c = conn.cursor()

    warning = messagebox.askyesno('Delete All Files?',
                                  'You have chosen to delete all files. This action cannot be reversed. Do you wish to proceed?')

    if warning == 1:
        c.execute("DELETE FROM files")

    conn.commit()
    conn.close()


def about_notepad():
    new_win = Toplevel()

    info = LabelFrame(new_win, text='About DAP Notepad', fg='black')

    info.grid(row=0, column=0)

    info_label = Label(info,
                       text='DAP Notepad is an app developed by Dhruva Srinivas.\n It is an open-sourced notepad application.\n'
                            'It was developed using Python and Tkinter.\n The data was stored in SQLite3 databases.\n It\'s'
                            ' main features include easy accessibility, user-friendliness and speed.\n Enjoy! \n From The '
                            'Creator - Dhruva Srinivas', fg='black', bg='white')

    info_label.grid(row=0, column=0, padx=10, pady=10)


def navigation():
    new_win = Toplevel()

    navigate_frame = LabelFrame(new_win, text='Navigate', fg='black')
    navigate_frame.grid(row=0, column=0, padx=10, pady=10)

    navigate_label = Label(navigate_frame, text='Welcome to DAP Notepad Navigation!\n\n\n'
                                                ' Here we will be telling you how to use this notepad application.\n'
                                                ' This Notepad can be used to make quick and speedy notes and can be'
                                                ' used as a to-do list\n\n'
                                                ' To save your file:\n'
                                                ' File >> Save >> \'Enter Name\' >> Save\n\n'
                                                ' To open a file:\n'
                                                ' File >> Open >> \'Enter Name\' >> Open\n\n'
                                                ' To delete a file:\n'
                                                ' File >> Delete >> \'Enter Name\' >> Delete\n\n'
                                                ' To delete all files:\n'
                                                ' File >> Delete All\n\n'
                                                ' Version - 1.1 Windows')

    navigate_label.grid(row=0, column=0, padx=10, pady=10)


def terms():
    new_win = Toplevel()

    terms_frame = LabelFrame(new_win, text='Terms And Conditions', fg='black')
    terms_frame.grid(row=0, column=0, padx=10, pady=10)

    terms_label = Label(terms_frame, text='Terms And Conditions - DAP Notepad\n \n \n \n'
                                          ' * No Form Of Code can be reproduced in any manner.\n'
                                          ' * Recordings and screen recordings of this app is allowed as long as credit'
                                          ' is given.\n'
                                          ' An example of giving credit:\n '
                                          ' \' In Video Description (YouTube) \' \n'
                                          ' Application - DAP Notepad\n'
                                          ' * Photos and Screenshot exports are allowed. No credit needed.\n'
                                          ' * Code cannot be claimed as own.'
                                          ' \n\n\n'
                                          ' Copyright - 2020 Licensing - None')

    terms_label.grid(row=0, column=0, padx=10, pady=10)


def show_all():
    conn = sqlite3.connect('file.db')
    c = conn.cursor()

    new_win = Toplevel()

    show_frame = LabelFrame(new_win, text='All Files')
    show_frame.grid(row=0, column=0, padx=10, pady=10)

    c.execute("SELECT * FROM files")
    items = c.fetchall()

    print_item = ''

    for item in items:
        print_item += item[0] + '\n'

    files_label = Text(show_frame, height=15, width=25)
    files_label.insert(1.0, print_item)
    files_label.configure(state='disabled')
    files_label.grid(row=0, column=0, padx=10, pady=10)
    conn.commit()
    conn.close()


def new_window():
    new_win = Toplevel()

    pad = Text(new_win, height=500, width=700, bd=5)
    pad.configure(state='normal')
    pad.grid(row=0, column=0, padx=10, pady=10)


options = Menu(root)
root.config(menu=options)

file = Menu(options)
options.add_cascade(label='File', menu=file)
file.add_command(label='Save', command=save_file)
file.add_command(label='Open', command=open_file)
file.add_command(label='Delete', command=delete_file)
file.add_command(label='Delete All', command=delete_all)
file.add_separator()
file.add_command(label='Exit', command=root.quit)

help = Menu(options)
options.add_cascade(label='Help', menu=help)
help.add_command(label='About DAP Notepad', command=about_notepad)
help.add_command(label='Navigate', command=navigation)
help.add_command(label='Terms And Conditions', command=terms)

show = Menu(options)
options.add_cascade(label='Show', menu=show)
show.add_command(label='Show All Files', command=show_all)

new = Menu(options)
options.add_cascade(label='New', menu=new)
new.add_command(label='New File', command=new_file)
new.add_command(label='New Window', command=new_window)


root.mainloop()
