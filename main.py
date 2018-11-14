import tkinter as tk
import yelp as yelp
import random

user_choices = []
search_results = []

def random_rest():
     my_choice  = random.choice(user_choices)
     popup = tk.Tk()
     popup.title("You have randomly chosen " + my_choice + "!")
     popup.geometry("500x500+800+300")
     choice_label = tk.Label(popup, text = "You have randomly chosen " + my_choice + "!")
     choice_label.place(x = 100, y = 100)

def reset():
    random_button.config(state = "active")
    delivery_btn.deselect()
    alcohol_btn.deselect()
    is_open_btn.deselect()
    take_out_btn.deselect()
    results.delete(0, tk.END)
    query = ""
    selections.delete(0, tk.END)
    keyword_entry.delete(0, tk.END)
    del user_choices[:]
    del search_results[:]

def reset_search():
    del search_results[:]
    keyword_entry.delete(0, tk.END)
    random_button.config(state = "active")
    delivery_btn.deselect()
    alcohol_btn.deselect()
    is_open_btn.deselect()
    take_out_btn.deselect()
    results.delete(0, tk.END)
    query = ""

root = tk.Tk()
root.title("Food-roulette")
root.geometry("850x600+600+100")
root.resizable(False, False)

def search():
    if keyword_entry.get() != "":
        query = yelp.query_by_location(term=keyword_entry.get(), location="fullerton", limit=1)

        for name in query:
            results.insert(tk.END, query[name]["name"])
            search_results.append(query[name]["name"])
            print (query)

def move_right():
    # move item from user choices to search results
    user_choices.remove(selections.get(selections.curselection()))
    print (user_choices)

    results.insert(tk.END, selections.get(selections.curselection()))
    selections.delete(selections.curselection())

def move_left():
    # move item from search results to user choices
    duplicate_found = False

    for item in user_choices:
        if item == results.get(results.curselection()):
            duplicate_found = True

    if duplicate_found == False:
        user_choices.append(results.get(results.curselection()))
        selections.insert(tk.END, results.get(results.curselection()))

    results.delete(results.curselection())

    print (user_choices)

random_button = tk.Button(root, text = "Choose a random restaurant", command = random_rest)
random_button.place(x = 625, y = 400)

reset_button = tk.Button(root, text = "Reset All", command = reset)
reset_button.place(x = 625, y = 435)

reset_search_btn = tk.Button(root, text = "Reset Search", command = reset_search)
reset_search_btn.place(x = 626, y = 470)

search_btn = tk.Button(root, text = "Search", command = search)
search_btn.place(x = 690, y = 75)

move_to_selection_btn = tk.Button(root, text = ">>", command = move_right)
move_to_selection_btn.place(x = 310, y = 200)
remove_from_selection_btn = tk.Button(root, text = "<<", command = move_left)
remove_from_selection_btn.place(x = 310, y = 250)

filter_label = tk.Label(root, text = "Filters(in progress)", relief = "ridge")
filter_label.place(x = 700, y = 150)
'''
delivery_btn = tk.Checkbutton(root, text = "Delivery Available")
delivery_btn.place(x = 650, y = 175)

is_open_btn = tk.Checkbutton(root, text = "Currently Open")
is_open_btn.place(x = 650, y = 200)

take_out_btn = tk.Checkbutton(root, text = "Take-out Available")
take_out_btn.place(x = 650, y = 225)

alcohol_btn = tk.Checkbutton(root, text = "Serves Alcohol")
alcohol_btn.place(x = 650, y = 250)
'''
results_label = tk.Label(root, text = "Your Choices", relief = "ridge")
results_label.place(x = 125, y = 15)

selections = tk.Listbox(root, height = 25, width = 30)
selections.place(x = 50, y = 50)

selections_label = tk.Label(root, text = "Restaurant Results", relief = "ridge")
selections_label.place(x = 435, y = 15)

results = tk.Listbox(root, height = 25, width = 30)
results.place(x = 375, y = 50)

keyword_label = tk.Label(root, text = "Keyword Search", relief = "ridge")
keyword_label.place(x = 675, y = 25)

keyword_entry = tk.Entry(root)
keyword_entry.place(x = 650, y = 50)




















root.mainloop()

#
