shopping_list = []
budget = int(input("\nEnter your budget: "))

pricelist = {"mleko": 25, "vejce": 33, "jogurt": 10, "chleba": 35}

def print_menu():
    print(f"\nMenu: (budget remaining: {budget_remaining()})")
    # print("\nMenu:")
    print("1 - Get your shopping list")
    print("2 - Add item to shopping list")
    print("3 - Remove item from shopping list")
    print("4 - Total price of your shopping")
    print("0 - Exit")
    print("\nBudget remaining is",budget_remaining(),"\n")
    
def get_shopping_list():
    print("\nItems on the shopping list:", shopping_list)

def add_item_to_shopping_list():
    print_pricelist_table()
    items = list(pricelist.keys())
    # print("Available items in pricelist are:", items)
    item = input("\nName of the item: ")

    if item != "":
        if item in items:
            # if total_price_of_shopping() + pricelist[item] <= 100:
            if pricelist[item] <= budget_remaining():
                shopping_list.append(item)
                print("\nItem ", item, "has been added")
            else:
                print("\nYou have no more money for this item.")
        else:
            print("\nItem", item, "is currently not available, please select item from pricelist")
    else:
        print("\nYou have to specify an item")

def remove_item_from_shopping_list():
    print("\n".join(shopping_list))
    item = input("\nName of the item: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print("\nItem", item, "has been removed")
    else:
        print("\nItem", item, "is not in the shopping list")
        
def total_price_of_shopping():
    total = 0
    for i in shopping_list:
        total += pricelist[i]
    #print ("\nPrice of shopping is", total)
    return total
    
def budget_remaining(): 
    reamining = budget - total_price_of_shopping()
    # print ("\nBudget remaining is", reamining)
    return reamining
    
def print_pricelist_table():
    print ("\n{:<10} {:<10}".format('Product', 'Price'))
    for key, value in pricelist.items():
        print ("{:<10} {:<10}".format(key, value))
    


while True:
    print_menu()
    option = input("\nEnter your choice: ")

    if option.isdigit():
        option = int(option)
        if option == 1:
            get_shopping_list()
        elif option == 2:
            add_item_to_shopping_list()
        elif option == 3:
            remove_item_from_shopping_list()
        elif option == 4:
            print("\nYour expense is", total_price_of_shopping())
        elif option == 0:
            print("\nHope you bought everything you had on the shopping list and didn't forget anything!")
            exit()
    else:
        print("\nInvalid option. Please enter number from 0 to 3.")
    print("")
