import tkinter as tk
import yelp as yelp
import random
import socket
import requests
import json
import webbrowser

rlist = []
user_choices = []
search_results = []
results_dict = {}
#Gets user's IP and geographical location
hostname = socket.gethostname()
IPAD = socket.gethostbyname(hostname)
ip = requests.get("https://api.ipify.org").text
r = requests.get("http://api.ipstack.com/" + ip + "?access_key=142834bbe4ab45b22e84a39064652b97")
geo = json.loads(r.text)
latitude = geo['latitude']
longitude = geo['longitude']

class Restaurant():

    def __init__(self, name, rating, phone):
        self.name = name
        self.rating = rating
        self.phone = phone

    
     
def random_rest():
    if len(user_choices) != 0:
        my_choice  = random.choice(user_choices)
##        popup = tk.Tk()
##        popup.title("You have randomly chosen " + my_choice + "!")
##        popup.geometry("500x500+800+300")
        webbrowser.open('https://www.google.com/maps/search/' + my_choice)
##        choice_label = tk.Label(popup, text = "You have randomly chosen " + my_choice + "!")
##        choice_label.place(x = 100, y = 100)

def reset():
    random_button.config(state = "active")
    results.delete(0, tk.END)
    query = ""  
    selections.delete(0, tk.END)
    keyword_entry.delete(0, tk.END)
    del user_choices[:]
    del search_results[:]
    results_dict.clear()

def reset_search():
    del search_results[:]
    keyword_entry.delete(0, tk.END)
    results.delete(0, tk.END)
    random_button.config(state = "active")
    results.delete(0, tk.END)
    del search_results[:]
    query = ""

def get_directions():
    z = selections.get(selections.curselection())
    webbrowser.open('https://www.google.com/maps/search/' + z)

root = tk.Tk()
root.title("Food-roulette")
root.geometry("850x600+600+100")
root.resizable(False, False)

def search():
    if keyword_entry.get() != "":
        query = yelp.query_by_coordinate(term=keyword_entry.get(), lat = latitude, long = longitude , limit=10)

        for name in query:
            results.insert(tk.END, query[name]["name"])
            search_results.append(query[name]["name"])
            results_dict[query[name]["name"]] = query[name]["id"]
            print(query[name]['name'] + str(query[name]['rating']))


            r = Restaurant(query[name]['name'],query[name]['rating'],query[name]['phone'])
            rlist.append(r)
                                                                                 
            #print (query)
            #print ("\n\n\n\n")
            #print (results_dict)    

def move_right():
    # move item from user choices to search results
    if len(user_choices) != 0:
        user_choices.remove(selections.get(selections.curselection()))
        #print (user_choices)

        results.insert(tk.END, selections.get(selections.curselection()))
        selections.delete(selections.curselection())

def move_left():
    # move item from search results to user choices
    duplicate_found = False

    for item in user_choices:
        if item == results.get(results.curselection()):
            duplicate_found = True

    if duplicate_found == False:
        if len(search_results) != 0:
            user_choices.append(results.get(results.curselection()))
            selections.insert(tk.END, results.get(results.curselection()))

            results.delete(results.curselection())

            print (user_choices)

def get_info():
    uc = results.get(results.curselection())
    ipopup = tk.Tk()
    ipopup.title(uc)
    ipopup.geometry("500x200+800+300")
    choice_label2 = tk.Label(ipopup, text = "Info on " + uc + ":")
    choice_label2.place(x = 100, y = 0)
    for i in range(len(rlist)):
        if (uc == rlist[i].name):
            r = tk.Label(ipopup, text = "Rating: " + str(rlist[i].rating))
            r.place(x = 100, y = 40)
            ph = tk.Label(ipopup, text = "Phone: " + str(rlist[i].phone))
            ph.place(x = 100, y = 60)

random_button = tk.Button(root, text = "Choose a random restaurant", command = random_rest)
random_button.place(x = 625, y = 400)

info_button = tk.Button(root,text = "Get Info", command = get_info)
info_button.place(x=625, y = 500)

get_directions_button = tk.Button(root, text = "Get Directions", command = get_directions)
get_directions_button.place(x = 125, y = 470)

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
