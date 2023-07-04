import tkinter as tk
from tkcalendar import DateEntry
import pickle
import os
import sys
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# task list
tasks = []

def load_tasks():
    if os.path.exists('tasks.pkl'):
        with open('tasks.pkl', 'rb') as f:
            return pickle.load(f)
    return []


def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)


def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, f"{task['name']} (Time: {task['stime']} - {task['etime']})")


def add_task():
    task_name = task_name_input.get()
    task_start_time = task_time_input1.get_date()
    task_end_time = task_time_input2.get_date()
    if task_name != "":
        tasks.append({'name': task_name, 'stime': task_start_time, 'etime': task_end_time})
        task_name_input.delete(0, tk.END)
        task_time_input1.set_date(date.today())  # set current date
        update_task_listbox()
        save_tasks()

    draw_timeline()


def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        del tasks[selected_task_index[0]]
        update_task_listbox()
        save_tasks()

    draw_timeline()


def delete_all_tasks():
    tasks.clear()
    update_task_listbox()
    save_tasks()

    draw_timeline()


def close_window():
    root.destroy()


def reload_app():
    # current python executable path
    python = sys.executable
    os.execl(python, python, * sys.argv)


def draw_timeline():
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task['name'] for task in tasks])

    for i, task in enumerate(tasks):
        start_date = mdates.date2num(task['stime'])
        end_date = mdates.date2num(task['etime'])
        ax.broken_barh([(start_date, end_date - start_date)], (i-0.4, 0.8))

    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.show()


tasks = load_tasks()

root = tk.Tk()
root.geometry("500x500")

# create reload button
reload_button = tk.Button(root, text="Reload", command=reload_app)
reload_button.pack()

task_name_label = tk.Label(root, text="Task Name : ")
task_name_label.pack()
# task_name_label.place(x=100, y=0)

task_name_input = tk.Entry(root)
task_name_input.pack()
# task_name_input.grid(row=0, column=0)
# task_name_input.place(x=250, y=0)

task_time_label = tk.Label(root, text="Task time:")
task_time_label.pack()

task_time_input1 = DateEntry(root)
task_time_input1.pack()
task_time_input2 = DateEntry(root)
task_time_input2.pack()

add_button = tk.Button(root, text="Add task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=400)
task_listbox.pack()

update_task_listbox()

delete_button = tk.Button(root, text="Delete task", command=delete_task)
delete_button.pack()

delete_all_button = tk.Button(root, text="Delete all tasks", command=delete_all_tasks)
delete_all_button.pack()

close_button = tk.Button(root, text="Close window", command=close_window)
close_button.pack()

root.mainloop()
