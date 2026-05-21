import tkinter as tk 
#tkinter: This handles the visual window and the text display label.

from time import strftime
#strftime from time: This grabs the exact time from your computer system.

def update_time():
    
#%I is for a 12-hour clock , %M is for minutes , %S is for seconds , %p adds the AM/PM indicator.
    
    current_time = strftime('%I:%M:%S %p')  # for 24-hour format
    clock_label.config(text=current_time)
    # Call the update_time function again after 1000ms (1 second)
    clock_label.after(1000, update_time)
# Initialize the main window
root = tk.Tk()
root.title("Digital Clock")
clock_label = tk.Label(
    root, 
    font=('calibri', 50, 'bold'), 
    background='black', 
    foreground='cyan'
)
clock_label.pack(anchor='center')
# Run the update function once to start the loop
update_time()
# Start the Tkinter application loop
root.mainloop()