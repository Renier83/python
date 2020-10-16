# initial variable for shopping status
shopping = 'y'

#list to track pie purchase

pie_purchase = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# list of pie's
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Boku", "Burek", "Tamale", "Steak" ]

#Display
print("Welcome to the House Of Pies! Here is the list of our amazing pies:")

while shopping == "y":
    print("--------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak")
    
    pie_choice = input("Which pie would you like?")
    
    choice_index = int(pie_choice) - 1
    pie_purchase[choice_index] += 1
     
    
    
    print("----------------------------------")
    
    print("Awesome choice!" + pie_choice[choice_index] + "will be ready shortly!")
    
    shopping = input("Would you like another pie?: (y)es or (n)o?")
    
    #once completed
    print("--------------------------")
    
    print("You have purchased:")
    
    for pie_index in range(len(pie_list)):
        pie_count = str(pie_purchase[pie_index])
        pie_name = str(pie_list[pie_index])
        
        
        print(pie_count + " " + pie_name)
        
        