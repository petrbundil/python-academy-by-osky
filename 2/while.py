shopping_list = []

def print_menu():
    print("Menu:")
    print("1 - Get your shopping list")
    print("2 - Add item to shopping list")
    print("3 - Remove item from shopping list")
    print("0 - Exit\n")
    
def get_shopping_list():
    print("\nItems on the shopping list:", shopping_list)
    
def add_item_to_shopping_list():
    item = input("\nName of the item: ")
    if item != "":
        shopping_list.append(item)
        print("\nItem ", item, "has been added")
    else:
        print("\nYou have to specify an item")
        
def remove_item_from_shopping_list():
    item = input("\nName of the item: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print("\nItem", item, "has been removed")
    else:
        print("\nItem", item, "is not in the shopping list")
        
def reminder():
    print("\nHope you bought everything you had on the shopping list and didn't forget anything!")
    exit()

while True:
    print_menu()
    option = int(input("Enter your choice: "))
    if option == 1:
        get_shopping_list()
    elif option == 2:
        add_item_to_shopping_list()
    elif option == 3:
        remove_item_from_shopping_list()
    elif option == 0:
        reminder()
    else:
        print("\nInvalid option. Please enter number from 0 and 3.")
    print("")