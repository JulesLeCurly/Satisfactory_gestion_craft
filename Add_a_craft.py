import Fonction.Create_file as Create_file

while True:
    print("Add a craft")
    print("1. Add a craft")
    print("2. Add a craft in a existing recette")
    print("Q. Exit")
    
    input_choice = input("Enter your choice: ")
    if input_choice == "1":
        Create_file.Add_a_craft()
    elif input_choice == "2":
        pass
    elif input_choice.lower() == "q":
        break
    else:
        print("Invalid choice")
    