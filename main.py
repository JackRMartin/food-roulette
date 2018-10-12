import tkinter as tk


def random_rest():
    choice_label.config(text="You chose a random restaurant")
    random_button.config(state="disabled")
    reset_button.config(state="active")

def reset():
    choice_label.config(text="")
    random_button.config(state="active")
    reset_button.config(state="disabled")

root = tk.Tk()
root.title("Food-roulette")
root.geometry("700x700+600+100")

random_button = tk.Button(root, text= "Choose a random restaurant", command=random_rest)
random_button.pack(padx = 5, pady = 10, side = "bottom")

reset_button = tk.Button(root, text = "reset", command = reset, state = "disabled")
reset_button.pack(padx = 5, pady = 10, side = "bottom")

choice_label = tk.Label(root, text="")
choice_label.pack(padx = 5, pady = 10, side = "bottom")



root.mainloop()




































#
