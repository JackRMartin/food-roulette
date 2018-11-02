import tkinter as tk
import webbrowser
#test url 
url = "https://www.google.com/maps/search/MR+BBQ"

#opens the user's restaurant in a new browser and inputs their restaurant in the google maps search bar.
def open_directions():
    webbrowser.open(url)


def random_rest():
    #choice_label.config(text = "You chose a random restaurant")
    random_button.config(state = "disabled")
    reset_button.config(state = "active")
    for i in range(25):
        results.insert(tk.END, keyword_entry.get())

def reset():
    #choice_label.config(text = "")
    random_button.config(state = "active")
    reset_button.config(state = "disabled")
    results.delete(0, tk.END);

root = tk.Tk()
root.title("Food-roulette")
root.geometry("700x475+600+100")
root.resizable(False, False)



random_button = tk.Button(root, text = "Choose a random restaurant", command = random_rest)
#random_button.grid(row=0, column=0)
#random_button.pack(padx = 5, pady = 10, side = "bottom")
random_button.place(x = 300, y = 350)

reset_button = tk.Button(root, text = "reset", command = reset, state = "disabled")
#reset_button.grid(row=0, column=1)
#reset_button.pack(padx = 5, pady = 10, side = "bottom")
reset_button.place(x = 300, y = 380)

directions_button = tk.Button(root , text = "Directions", command = open_directions)
directions_button.place(x=300, y = 410)

#choice_label = tk.Label(root, text="")
#choice_label.grid(row=0,column=2)
#choice_label.pack(padx = 5, pady = 10, side = "bottom")
#choice_label.place(x = 10, y =10)


filter_label = tk.Label(root, text = "Filter by category", relief = "ridge")
filter_label.place(x = 535, y = 100)

delivery_btn = tk.Checkbutton(root, text = "Delivery Available")
delivery_btn.place(x = 525, y = 130)

is_open_btn = tk.Checkbutton(root, text = "Currently Open")
is_open_btn.place(x = 525, y = 160)

take_out_btn = tk.Checkbutton(root, text = "Take-out Available")
take_out_btn.place(x = 525, y = 190)

alcohol_btn = tk.Checkbutton(root, text = "Serves Alcohol")
alcohol_btn.place(x = 525, y = 220)

''''
price_label = tk.Label(root, text = "Price Range", relief = "ridge")
price_label.place(x = 525, y = 275)

price_scale = tk.Scale(root, from_=0, to_=100, orient = "horizontal")
price_scale.place(x = 525, y = 300)
'''

results_label = tk.Label(root, text = "Restaurant Results", relief = "ridge")
results_label.place(x = 105, y = 2)

results = tk.Listbox(root, height = 20, width = 30);
results.place(x = 50, y = 50)

results_scrollbar = tk.Scrollbar(results)


keyword_label = tk.Label(root, text = "Keyword Search", relief = "ridge")
keyword_label.place(x = 350, y = 25)

keyword_entry = tk.Entry(root)
keyword_entry.place(x = 325, y = 50)




















root.mainloop()

#
