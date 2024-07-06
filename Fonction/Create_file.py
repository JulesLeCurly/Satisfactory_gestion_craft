import os
from colorama import Fore, init

import Fonction.Lister_existing_craft as Lister_existing_craft

init(autoreset=True)

def Add_a_craft():
    existing_craft = Lister_existing_craft.lister_dossiers_craft()
    while True:
        craft_name = input("Enter the craft name: ")
        if craft_name in existing_craft:
            print("Craft already exist")
            continue
        else:
            os.mkdir(os.path.join("Craft", craft_name))
            print("Craft created")
            break
    
    material_dict = {}
    
    while True:
        material_needed = -1
        material_needed_index = -1
        while not material_needed_index in range(len(existing_craft)) or material_needed in material_dict:
            for i in range(len(existing_craft)):
                print(f" {i}: {existing_craft[i]}")
            print(" /: Raw material")
            
            try:
                user_choice = input("Enter the material needed for the craft: ")
                if user_choice == "/":
                    material_needed = "/"
                    break
                
                material_needed_index = int(user_choice)
                material_needed = existing_craft[material_needed_index]
                
            except ValueError:
                print(Fore.RED + "Invalid material. Please try again.")
                continue
            
            if not material_needed_index in range(len(existing_craft)):
                print(Fore.RED + "Invalid material. Please try again.")
            elif material_needed in material_dict:
                print(Fore.RED + "Material already select. Please try another material.")
                continue
        
        if user_choice != "/":
            quantity = -1
            while quantity < 0:
                try:
                    quantity = float(input("Enter the quantity of the material needed for the craft: "))
                except ValueError:
                    print(Fore.RED + "Invalid quantity. Please try again.")
                    continue
                if quantity < 0:
                    print(Fore.RED + "Invalid quantity. Please try again.")
                    continue
            
            material_dict[material_needed] = quantity
        else:
            quantity = "/"
            material_dict = {}
        
        
        print(Fore.GREEN + "Material added")
        
        if user_choice != "/":
            print("Do you want to add another material? (y/n)")
            choice = input().lower()
            if choice != "y":
                break
        else:
            break
    
    Path_craft = os.path.join("Craft", craft_name)
    
    File_Path = f"{Path_craft}/{craft_name}_craft_NB-1.txt"
        
    with open(File_Path, "w") as file:
        file.write(str(material_dict))
    
    print(Fore.GREEN + "Craft created successfully")

