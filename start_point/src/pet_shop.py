# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(lists, cash):
   lists["admin"]["total_cash"] += cash

def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

def increase_pets_sold(lists, sold): 
    lists["admin"]["pets_sold"] += sold

def get_stock_count(lists):
    return len(lists["pets"])

def get_pets_by_breed(lists, breed):
    pets = []
    for pet in lists["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    
    return pets 

def find_pet_by_name(lists, name):
    for pet in lists["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(lists, name):
    for pet in lists["pets"]:
        if pet["name"] == name:
            lists["pets"].remove(pet)

        
def add_pet_to_stock(lists, new_pet):
    lists["pets"].append(new_pet)
    count = len(lists["pets"])

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    count = len(customer["pets"])
    return count

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)







                            



        















