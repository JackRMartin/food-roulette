import tkinter as tk


def random_rest():
    choice_label.config(text = "You chose a random restaurant")
    random_button.config(state = "disabled")
    reset_button.config(state = "active")

def reset():
    choice_label.config(text = "")
    random_button.config(state = "active")
    reset_button.config(state = "disabled")

root = tk.Tk()
root.title("Food-roulette")
root.geometry("700x700+600+100")
root.resizable(False, False)


####################
#                  #
#                  #
#     Buttons      #
#                  #
####################

random_button = tk.Button(root, text = "Choose a random restaurant", command = random_rest)
#random_button.grid(row=0, column=0)
#random_button.pack(padx = 5, pady = 10, side = "bottom")
random_button.place(x = 450, y = 650)

reset_button = tk.Button(root, text = "reset", command = reset, state = "disabled")
#reset_button.grid(row=0, column=1)
#reset_button.pack(padx = 5, pady = 10, side = "bottom")
reset_button.place(x = 600, y = 610)

choice_label = tk.Label(root, text="")
#choice_label.grid(row=0,column=2)
#choice_label.pack(padx = 5, pady = 10, side = "bottom")
choice_label.place(x = 10, y =10)


####################
#                  #
#     Filters      #
#                  #
####################

filter_label = tk.Label(root, text = "Filter by category", relief = "ridge")
filter_label.place(x = 525, y = 100)

delivery_btn = tk.Checkbutton(root, text = "Delivery Available")
delivery_btn.place(x = 525, y = 130)

is_open_btn = tk.Checkbutton(root, text = "Currently Open")
is_open_btn.place(x = 525, y = 160)

take_out_btn = tk.Checkbutton(root, text = "Take-out Available")
take_out_btn.place(x = 525, y = 190)

alcohol_btn = tk.Checkbutton(root, text = "Serves Alcohol")
alcohol_btn.place(x = 525, y = 220)























root.mainloop()

#
