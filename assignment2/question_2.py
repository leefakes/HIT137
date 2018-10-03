"""
Pizza ordering simulator.

This app will display a form which will allow the user to
select the base, sauce and toppings for their pizza.

The pizza cost will be totalled and t the end a countdown timer
is displayed to siumulate the wait time for the pizza to be
cooked. Although the clock will show minutes it will count down
faster.

"""

import tkinter as tk
from tkinter import ttk, TOP, RIDGE


class MainWindow(ttk.Frame):

    def __init__(self, master, data):
        self.master = master

        # Load data
        self.pizza_sizes = data["pizza_sizes"]
        self.pizza_crusts = data["pizza_crusts"]
        self.pizza_sauces = data["pizza_sauces"]
        self.pizza_toppings = data["pizza_toppings"]

        print(self.pizza_toppings)

        # Object variables
        self.pizza_size = ""
        self.pizza_crust = ""
        self.pizza_sauce = ""
        self.pizza_qty = 1

        # Create container
        container_frame = ttk.Frame(self.master)
        container_frame.config(padding=(10, 5, 10, 10))
        container_frame.pack(side=TOP, fill="both", expand="yes")

        # Create banner label
        label_frame = ttk.Frame(container_frame,
                                width=640,
                                height=300)
        label_frame.config(padding=(5,5))
        label_frame.pack(side=TOP,
                         fill="both",
                         expand="yes")

        # Add controls to banner label
        ttk.Label(label_frame,
                  text="Build Your Own Pizza",
                  font="Helvetica 16 bold italic",
                  ).pack()

        # Create order frame
        order_frame = ttk.LabelFrame(container_frame, text="My Order")
        order_frame.config(relief=RIDGE)
        order_frame.pack(side=TOP,
                         fill="both",
                         expand="yes")

        # Add controls to order frame
        pizza_size_combo = ttk.Combobox(order_frame)
        pizza_size_combo.config(textvariable=self.pizza_size,
                                values=list(self.pizza_sizes))
        pizza_size_combo.pack()
        pizza_crust = ttk.Combobox(order_frame)
        pizza_crust.config(textvariable=self.pizza_crust,
                           values=list(self.pizza_crusts))
        pizza_crust.pack()
        pizza_sauce = ttk.Combobox(order_frame)
        pizza_sauce.config(textvariable=self.pizza_sauce,
                           values=list(self.pizza_sauces))
        pizza_sauce.pack()

# TODO: Add loop of spinner boxes for the toppings
# TODO: Add method to total the order


def get_data():
    # These values would be read from database
    pizza_sizes = {"Family": 7,
                   "Large": 5,
                   "Medium": 5,
                   "Small": 3}

    pizza_crusts = {"Deep Pan": 2,
                    "Traditional": 1,
                    "Thin 'N' Crispy": 1,
                    "Stuffed Crust": 3}

    pizza_sauces = {"Tomato": 1,
                    "Extra Tomato Sauce": 1.50,
                    "BBQ Sauce": 1,
                    "Extra BBQ Sauce": 1.50,
                    "Remove Sauce": 0}

    pizza_toppings = {
            "MEAT":
            {
                    "Anchovies": 1.00,
                    "Bacon Rashers": 1.00,
                    "Beef": 1.00,
                    "Chicken": 1.00,
                    "Italian Sausage": 1.00,
                    "Pepperoni": 1.00,
                    "Prawns": 1.00,
                    "Smoky Honey Ham": 1.00,
                    "Steak": 1.00,
                    "Tandoori Chicken": 1.00
            },
            "VEGGIES":
            {
                    "Diced Tomato": 0.50,
                    "Green Capsicum": 0.50,
                    "Jalapeños": 0.50,
                    "Kalamata Olives": 0.50,
                    "Mushrooms": 0.50,
                    "Onion": 0.50,
                    "Pineapple": 0.50,
                    "Red Onion": 0.50,
                    "Roasted Red Capsicum": 0.50,
                    "Rocket": 0.50
            },
            "Extras":
            {
                    "Aioli Drizzle": 0.25,
                    "Buffalo Sauce Drizzle": 0.25,
                    "Cheddar": 0.25,
                    "Chilli Flakes": 0.25,
                    "Fetta": 0.25,
                    "Garlic": 0.25,
                    "Hollandaise Drizzle": 0.25,
                    "Oregano": 0.25,
                    "Parsley": 0.25,
                    "Smoky BBQ Drizzle": 0.25,
                    "Sour Cream Drizzle": 0.25,
                    "Sriracha Drizzle": 0.25
            }
    }

    return {
            "pizza_sizes": pizza_sizes,
            "pizza_crusts": pizza_crusts,
            "pizza_sauces": pizza_sauces,
            "pizza_toppings": pizza_toppings
           }


def main():    # Create the window manager and set the default sizes
    manager = tk.Tk()
    # manager.minsize(width=640, height=480)
    # manager.maxsize(width=800, height=600)
    manager.geometry('640x480')
    manager.tk_setPalette(background='#ececec')

    data = get_data()
    MainWindow(manager, data)
    manager.mainloop()

if __name__ == '__main__':
    main()
