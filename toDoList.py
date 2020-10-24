from tkinter import *
import os
import sqlite3

#Function main
def main():
	#Define conn(connection), c(cursor) to be global 
	global conn
	global c

	#Connect to the database
	conn = sqlite3.connect("dbTODOLISTS.db") #This will create a new database [dbTODOLISTS.db] if it does not exist
	print("Connected to "+str(sqlite3.version))

	#Connect to cursor
	c = conn.cursor()
	print(c)

	#Create table [tasks] containing only one column [tasks_are]
	c.execute("""CREATE TABLE IF NOT EXISTS tasks(
					tasks_are text
			)""")

	#Initialize the tkinter window with Tk()
	main_win = Tk()
	main_win.title("Need To Do")
	main_win.resizable(False, False) #Disable resize
	main_win.eval('tk::PlaceWindow . center') #Center the window

	#List box to accomodate the tasks
	tasks_list = Listbox(main_win, bg="white", fg="black", width=60, selectbackground="#e6b1b1", selectforeground="black")
	tasks_list.grid(row=0, column=0, columnspan=3)

	#Execute SQLITE command to fetch all the data
	c.execute("SELECT * FROM tasks")

	#Create a variable to store the fetched data
	todoTasks = c.fetchall()

	#Use for loop to get all the data(tasks) one by one
	for task_one in todoTasks:
		tasks_list.insert(END, task_one)

	#Function to add task
	def add_task():
		#Limiting the number of tasks to 10
		if tasks_list.size() >= 10:
			task_given.delete(0, END)
			task_given.insert(END, "Only 10 tasks allowed")

			task_given.config(state='disabled')
			submit_task.config(state='disabled')

		else:
			try:
				#Create a list [listForTODO]. It will be useful for storing data in the database 
				listForTODO = []

				#Append the tasks to the created list
				listForTODO.append(task_given.get())

				#Execute SQLITE command to add data
				c.execute("INSERT INTO tasks VALUES(?)", listForTODO)

				#Commit to database
				conn.commit()

				#Refresh the entry bar
				tasks_list.insert(END, task_given.get())
				task_given.delete(0, END)

			except:
				print("Error Connecting")

	#Function to exit window
	def exit_():
		main_win.destroy()

	#Display Help
	def help_win():
		help_window = Tk()
		help_window.title("Help")
		help_window.resizable(False, False)

		help_win_menu = Menu(help_window)

		#Exit help 
		def exit_help():
			help_window.destroy()

		help_win_menu.add_command(label="Exit Help Window", command=exit_help)

		label_help = Label(help_window, text="To add tasks there is a entry on the lower side\nTo delete click on task and press the given delete button", font=('times',15,'bold'))
		label_help.pack()

		help_window.config(menu = help_win_menu)
		help_window.mainloop()

	def delete_sel_task():
	    return

	    ''' Was Unable to do this. If anyone knows how to do this dm me on my Instagram>> https://www.instagram.com/iamsainath.u/ '''

	#Function to delete all the tasks
	def delete_all_task():
		c.execute("DELETE FROM tasks WHERE rowid = 1")
		c.execute("DELETE FROM tasks WHERE rowid = 2")
		c.execute("DELETE FROM tasks WHERE rowid = 3")
		c.execute("DELETE FROM tasks WHERE rowid = 4")
		c.execute("DELETE FROM tasks WHERE rowid = 5")
		c.execute("DELETE FROM tasks WHERE rowid = 6")
		c.execute("DELETE FROM tasks WHERE rowid = 7")
		c.execute("DELETE FROM tasks WHERE rowid = 8")
		c.execute("DELETE FROM tasks WHERE rowid = 9")
		c.execute("DELETE FROM tasks WHERE rowid = 10")

		conn.commit()

		tasks_list.delete(0, END)

	#Skeleton of the code
	label = Label(main_win, text="Enter New Task Here>>")
	label.grid(row=1,column=0)

	task_given = Entry(main_win, width=27)
	task_given.grid(row=1,column=1)

	submit_task = Button(main_win, text="Add", command=add_task, relief=GROOVE)
	submit_task.grid(row=1,column=2)

	del_task = Button(main_win, text="Delete Selected", command=delete_sel_task, relief=GROOVE, state=DISABLED)
	del_task.grid(row=2,column=0)

	del_all = Button(main_win, text="Delete All", command=delete_all_task, relief=GROOVE)
	del_all.grid(row=2,column=2)

	menu = Menu(main_win)

	menu.add_command(label="Help", command=help_win)
	menu.add_command(label="Exit To Do Task", command=exit)

	main_win.config(menu = menu)
	main_win.mainloop()

#Pythonic thing
if __name__ == "__main__":
    main()
