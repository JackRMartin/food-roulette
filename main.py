import tkinter as tk
import yelp as yelp
import random

user_choices = {}
search_results = []

def random_rest():
    pass
def reset():
    #choice_label.config(text = "")
    random_button.config(state = "active")
    results.delete(0, tk.END);
    query = "";
root = tk.Tk()
root.title("Food-roulette")
root.geometry("850x600+600+100")
root.resizable(False, False)

def search():
    query = yelp.query_api(term=keyword_entry.get(), location="fullerton", limit=10)

    for name in query:
        results.insert(tk.END, query[name]["name"])
        search_results.append(query[name]["name"])

def move_right():
    pass
def move_left():
    pass

random_button = tk.Button(root, text = "Choose a random restaurant", command = random_rest)
#random_button.grid(row=0, column=0)
#random_button.pack(padx = 5, pady = 10, side = "bottom")
random_button.place(x = 600, y = 525)

reset_button = tk.Button(root, text = "Reset", command = reset)
#reset_button.grid(row=0, column=1)
#reset_button.pack(padx = 5, pady = 10, side = "bottom")
reset_button.place(x = 600, y = 560)

search_btn = tk.Button(root, text = "Search", command = search)
search_btn.place(x = 650, y = 75)

move_to_selection_btn = tk.Button(root, text = ">>", command = move_right)
remove_from_selection_btn = tk.Button(root, text = "<<", command = move_left)

filter_label = tk.Label(root, text = "Filter by category", relief = "ridge")
filter_label.place(x = 650, y = 150)

delivery_btn = tk.Checkbutton(root, text = "Delivery Available")
delivery_btn.place(x = 650, y = 175)

is_open_btn = tk.Checkbutton(root, text = "Currently Open")
is_open_btn.place(x = 650, y = 200)

take_out_btn = tk.Checkbutton(root, text = "Take-out Available")
take_out_btn.place(x = 650, y = 225)

alcohol_btn = tk.Checkbutton(root, text = "Serves Alcohol")
alcohol_btn.place(x = 650, y = 250)

''''
price_label = tk.Label(root, text = "Price Range", relief = "ridge")
price_label.place(x = 525, y = 275)

price_scale = tk.Scale(root, from_=0, to_=100, orient = "horizontal")
price_scale.place(x = 525, y = 300)
'''

results_label = tk.Label(root, text = "Your Choices", relief = "ridge")
results_label.place(x = 105, y = 15)

selections = tk.Listbox(root, height = 20, width = 30)
selections.place(x = 50, y = 50)

selections_label = tk.Label(root, text = "Restaurant Results", relief = "ridge")
selections_label.place(x = 455, y = 15)

results = tk.Listbox(root, height = 20, width = 30)
results.place(x = 375, y = 50)



#results_scrollbar = tk.Scrollbar(results)

keyword_label = tk.Label(root, text = "Keyword Search", relief = "ridge")
keyword_label.place(x = 650, y = 25)

keyword_entry = tk.Entry(root)
keyword_entry.place(x = 650, y = 50)




















root.mainloop()

#
