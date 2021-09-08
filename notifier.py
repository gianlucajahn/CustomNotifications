# Importing all the necessary modules
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from plyer import notification
import time

# Defining the application and its properties
application = Tk()
application.title("Custom Notifications")
application.geometry("500x400")
current_rep = 0

# Giving the application a background image for a cleaner visualization and better user experience
img = Image.open("customnotifications_bg.png")
tkimage = ImageTk.PhotoImage(img)
img_label = Label(application, image=tkimage).grid()

'''
# To process the input we get from our user, we have to define a function that does so.
# We store the input from our user into variables (get_title, get_desc and get_time. Then, we make sure all input 
# prompts have been filled. If not, we give out an error to the user, telling him we in fact need all prompts to be
# filled by them to make our application work for them. Additionally, if the input for the notification timeframe is a 
# string, we give out an error telling our user to enter an integer instead. If they input a float data type, we convert 
# it into an integer for the user. If all requirements have been met, the user gets feedback about their notification 
# being set up. The application gets terminated and the notification loop is being started.
'''


def process_input():
    global current_rep
    get_title = title.get()
    get_desc = desc.get()
    get_time = minutes.get()
    get_rep = rep.get()

    if get_title == "" or get_desc == "" or get_time == "" or get_rep == "":
        messagebox.showerror("Error: EntryMissing: All fields need input for the application to work!")
    elif get_time == str:
        messagebox.showerror("Error: InvalidInput: The notification timeframe has to be an integer (a number)!")
    else:
        time_integer = int(float(get_time))
        entry_rep = int(float(get_rep))
        seconds = time_integer * 60
        messagebox.showinfo("Notification Setup", "Your notification has been set up.")
        application.destroy()

        '''
        # As long as the current amount of repetition cycles is smaller than the amount of repetitions that was entered
        # by the user in the repetition entry prompt, this while loop will repeat the notification with the sleep timer
        # the user configured. After every cycle, the amount of current repetitions is increased by 1, making sure the
        # current_rep value is accurate and working as intended.
        '''

        while current_rep < entry_rep:
            time.sleep(int(seconds))
            notification.notify(title=get_title,
                                message=get_desc,
                                app_name="Custom Notifications",
                                app_icon="icon.ico",
                                timeout=10)
            current_rep = current_rep + 1


# 1st label. It's purpose is to tell the user what kind of information he has to insert in the entry field next to it.
t_label = Label(application, text="Notification Title:", font=("poppins", 10), fg="#ffffff", bg="#292b2f")
t_label.place(x=12, y=120)

# 1st Entry. Takes title input.
title = Entry(application, width="25", font=("poppins", 13), bg="#9fa6ae")
title.place(x=123, y=120)

# 2nd label.
desc_label = Label(application, text="Description:", font=("poppins", 10), fg="#ffffff", bg="#292b2f")
desc_label.place(x=12, y=170)

# 2nd Entry. Takes Description Input.
desc = Entry(application, width="40", font=("poppins", 13), bg="#9fa6ae")
desc.place(x=123, y=170, height=30)

# 3rd label.
time_label = Label(application, text="Notify me in:", font=("poppins", 10), fg="#ffffff", bg="#292b2f")
time_label.place(x=12, y=225)

# 3rd Entry. Takes interval input for reminding cycles, in minutes.
minutes = Entry(application, width="5", font=("poppins", 13), bg="#9fa6ae")
minutes.place(x=123, y=225)

# 4hth label, telling the unit of time for the user to input.
time_min_label = Label(application, text="mins", font=("poppins", 10), bg="#292b2f", fg="#ffffff")
time_min_label.place(x=175, y=230)

# 5th label.
rep_label = Label(application, text="Repetitions:", font=("poppins", 10), fg="#ffffff", bg="#292b2f")
rep_label.place(x=12, y=270)

# 5th Entry. Takes interval/cycle count input.
rep = Entry(application, width="5", font=("poppins", 13), bg="#9fa6ae")
rep.place(x=123, y=270)

# 6th label, telling the amount of intervals/cycles.
rep_label = Label(application, text="times", font=("poppins", 10), fg="#ffffff", bg="#292b2f")
rep_label.place(x=175, y=270)

# The button to finalize and set up the notification, resulting in our process_input function to be called.
but = Button(application, text="Setup Notification", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#4bcce6", width=20,
             relief="flat",
             command=process_input)
but.place(x=170, y=340)

application.resizable(0, 0)
application.mainloop()
