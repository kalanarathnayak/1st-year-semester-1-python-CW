# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1903043 
# Date: 17/04/2022

# declaration of global scope variables
progress_count = trailer_count = retriever_count = exclude_count = total_count = 0
continuation = "y"

# declaration of empty lists to store validated user inputted data sets
progress_data, trailer_data, retriever_data, exclude_data = [], [], [], []


# function to validate user input
def validation(credit_cat):
    credit_range = [0, 20, 40, 60, 80, 100, 120]
    while True:
        try:
            print("Please enter your credit at", credit_cat, ":", end=" ")
            usr_input = int(input())
        except ValueError:
            print("Integer required\n")
            continue
        if usr_input not in credit_range:
            print("Out of range\n")
            continue
        else:
            return usr_input


print("Staff Version with Vertical Histogram Extension using list & Tuples\n")   
while continuation == "y":
    while True:
        credit_p, credit_d, credit_f = validation("pass "), validation("defer"), validation("fail ")
        credit_t = credit_p + credit_d + credit_f
        # validation of the total credit(the total should be equal to 120)
        if credit_t == 120:
            break
        else:
            print("Total incorrect.\n")
            continue

    # defining a tuple containing validated user inputted credits
    credit_tup = (credit_p, credit_d, credit_f)
    # sorting the user inputted data sets into 4 different progression outcomes and store them
    if credit_p == 120:
        progress_count += 1
        progress_data.append(credit_tup)  
        print("Progress\n")
    elif credit_p == 100:
        trailer_count += 1
        trailer_data.append(credit_tup)  
        print("Progress (module trailer)\n")
    elif credit_p + credit_d >= 60:
        retriever_count += 1
        retriever_data.append(credit_tup)  
        print("Module retriever\n")
    else:
        exclude_count += 1
        exclude_data.append(credit_tup)  
        print("Exclude\n")
    total_count += 1  # storing the total count of the user entered data sets

    # validation of the user input for continuation with getting another set of data(the valid inputs are either y or q)
    options = ["q", "y"]
    while True:
        continuation = str(input("Would you like to enter another set of data? \n" 
                                 "Enter 'y' for yes or 'q' to quit and view results: ")).lower()
        print("")
        if continuation not in options:
            print("'y' or 'q' required as an input to continue\n")
            continue
        else:
            break
        
    if continuation == "q":
        # if the user input is q then print the horizontal histogram
        print("-"*52)
        print("Horizontal Histogram")
        print("Progress", f'{progress_count:4}', ":", progress_count * "*")
        print("Trailer", f'{trailer_count:5}', ":", trailer_count * "*")
        print("Retriever", f'{retriever_count:3}', ":", retriever_count * "*")
        print("Excluded", f'{exclude_count:4}', ":", exclude_count * "*",  "\n")
        print(total_count, "outcomes in total.")
        print("-"*52)
        break
    else:
        # if entered y the loop will continue and get another set of data from the user
        continue
    
# printing the header of the vertical histogram
print("Progress", progress_count, "|",
      "Trailer", trailer_count, "|",
      "Retriever", retriever_count, "|",
      "Exclude", exclude_count)


# calculating the right justification value
def alig_spec(progression_s):
    al_val = len(str(progression_s)) + 11
    return al_val


al1, al2, al3 = alig_spec(progress_count), alig_spec(trailer_count), alig_spec(retriever_count)
# printing the stars vertically
# https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
# referred the above webpage to find out how to print an object vertically using a loop
for row in range(max(progress_count, trailer_count, retriever_count, exclude_count)):
    print(f'{"*":>4}' if row < progress_count else f'{" ":>4}',
          f'{"*":>{al1}}' if row < trailer_count else f'{" ":>{al1}}',
          f'{"*":>{al2}}' if row < retriever_count else f'{" ":>{al2}}',
          f'{"*":>{al3}}' if row < exclude_count else f'{" ":>{al3}}')
print("")
print(total_count, "outcomes in total.") 
print("-"*52)


# function for unpacking individual progression data lists which consist of tuples
def unpacking_list(progression_outcome, progression_out_cat):
    for i in range(len(progression_outcome)):
        print(progression_out_cat, end=" ")
        # https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
        # referred the above webpage to find out how to remove the parentheses from a tuple when printed
        print(*progression_outcome[i], sep=", ") 


unpacking_list(progress_data, "progress -")  
unpacking_list(trailer_data, "Progress (module trailer) -")      
unpacking_list(retriever_data, "Module retriever -")
unpacking_list(exclude_data, "Exclude -")
