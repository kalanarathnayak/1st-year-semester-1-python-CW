# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1903043 
# Date: 17/04/2022

# declaration of global scope variables
progress_count = trailer_count = retriever_count = exclude_count = total_count = 0
continuation = "y"


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
            

print("Staff Version with Histogram\n") 
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

    # sorting the user inputted data sets into 4 different progression outcomes
    if credit_p == 120:
        progress_count += 1
        print("Progress\n")
    elif credit_p == 100:
        trailer_count += 1
        print("Progress (module trailer)\n")
    elif credit_p + credit_d >= 60:
        retriever_count += 1
        print("Module retriever\n")
    else:
        exclude_count += 1
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
        print("Excluded", f'{exclude_count:4}', ":", exclude_count * "*", "\n")
        print(total_count, "outcomes in total.")
        print("-"*52)
    else:
        # if entered y the loop will continue and get another set of data from the user
        continue
