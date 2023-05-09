import itertools as it

def print_list(things):
    n = 1
    for i in things:
        print("      " + str(n) + "): " + i)
        n += 1


print("Hello! Welcome to the Meal Plan Generator. This program will allow you to edit the preselected items for\nyour meals and then output the possible combinations for view!")




proteins = ["Beef", "Chicken", "Pork", "Eggs"]
vegtables = ["Green Beans", "Broccoli", "Corn", "Potatos", "Asparagus", "Mushrooms"]
sauces = ["Gravy", "Au Jus", "Steak Sauce" , "Mushroom Sauce"]
sides = ["Mac n' Cheese", "Garlic Bread" , "Mashed Potatos", "Rice" , "Salad"]
meal_time = ["Dinner" , "Lunch" , "Breakfast"]
meal_type = ["Entree", "Snack", "Sandwich"]
list_of_all = [meal_time, meal_type, proteins, vegtables, sides, sauces]

print("\n\033[1mThese are the possible selections for the meals: \n")
print("A. Proteins:")
print_list(proteins)
print("\nB. Vegatables:")
print_list(vegtables)
print("\nC. Sides:")
print_list(sides)
print("\nD. Sauces:")
print_list(sauces)
print("\nE. Meal Type:")
print_list(meal_type)
print("\nF. Meal Time")
print_list(meal_time)
print('\033[0m')


continue_var = True
while(continue_var):
    print("Are there any categories you would like to add or remove from?")

    selection = input("Please enter the category (single letter) you want to edit or N to continue: ")
    if(selection != 'N'):
        if(selection == 'A'):
            print_list(proteins)
            temp = input("\nEnter the number you want removed or type the item to add: ")
            if(temp == "1" or temp == "2"  or temp == "3" or temp == "4"):
                proteins.pop(int(temp)-1)
            else:
                proteins.append(temp)
        elif(selection == 'B'):
            print_list(vegtables)
            temp = input("\nEnter the number you want removed or type the item to add: ")
            if(temp == "1" or temp == "2"  or temp == "3" or temp == "4" or temp == "5" or temp == "6"):
                vegtables.pop(int(temp)-1)
            else:
                vegtables.append(temp)
        elif(selection == 'C'):
            print_list(sides)
            temp = input("\nEnter the number you want removed or type the item to add: ")
            if(temp == "1" or temp == "2"  or temp == "3" or temp == "4" or temp == "5"):
                sides.pop(int(temp)-1)
            else:
                sides.append(temp)
        elif(selection == 'D'):
            print_list(sauces)
            temp = input("\nEnter the number you want removed or type the item to add: ")
            if(temp == "1" or temp == "2"  or temp == "3" or temp == "4"):
                sauces.pop(int(temp)-1)
            else:
                sauces.append(temp)
        elif(selection == 'E'):
            print_list(meal_type)
            temp = input("\nEnter the number you want removed or type the item to add: ")
            if(temp == "1" or temp == "2"  or temp == "3"):
                meal_type.pop(int(temp)-1)
            else:
                meal_type.append(temp)
        elif(selection == 'F'):
            print_list(meal_time)
            temp = input("\nEnter the number you want removed or type the item to add: ")
            if(temp == "1" or temp == "2"  or temp == "3"):
                meal_time.pop(int(temp)-1)
            else:
                meal_time.append(temp)
    else:
        continue_var = False


number_of_possible = len(proteins) * len(vegtables) * len(sides) * len(sauces) * len(meal_type) * len(meal_time) 
print("\nGiven these selections for meals, there are " + str(number_of_possible) + " possible combinations able to be created!")
list_object = list(it.product(*list_of_all))
print_all = input("Would you like to see all possible combinations? (Y or N): ")
num = 0
if(print_all == 'Y'):
    for i in list_object:
        num += 1
        print(str(num) + ": ")
        for temp in i:
            print("  " + temp)