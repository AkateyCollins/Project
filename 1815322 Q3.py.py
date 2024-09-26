import math
#this program is to calculate the permissible permutation of n objects taken r at a time
#Step-1-----The user was asked to input the total number of objects that are present in the set n,
# and the number of selected objects arranged in a certain order r.


def factorial(number):
    product=1
    for numbers in range(1,number+1):
         product *=(numbers)
    return product


while True:

    total_number= int(input("What is the total number of objects in the set?\n"))
    selected_objects= int(input("What is the number of selected objects arranged? \n")) 
    #The permutation can only be done if total_number>=  selected_objects

    if total_number >= selected_objects:

        # finding the square root of (selected_object-1) and stored in the variable m
        m= math.sqrt(selected_objects-1).__floor__()
        second_factorial= factorial(total_number-selected_objects)
        # calculating the permutation given the foemula:
        Permutation= factorial(total_number)*m/ second_factorial
        print(Permutation)
        break

    else:

        print("Make sure total_number is greater than selected_objects !!!\n")
