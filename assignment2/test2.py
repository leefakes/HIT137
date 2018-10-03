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

    return {
            "pizza_sizes": pizza_sizes,
            "pizza_crusts": pizza_crusts,
            "pizza_sauces": pizza_sauces
           }


data = get_data()
print(data)
