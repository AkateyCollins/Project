import math
#The program is to calculte the third angle (Gamma) of a triangle taking the values of the first angle and the second angle from the user
"""Calculate the angle 𝜸 and the length of side C in a triangle 
    given the angles 𝜶 and 𝜷 and the length of side A."""

def findC (first_angle, second_angle, length):
# Calculate the third angle of the triangle
    Third_angle= 180-(first_angle + second_angle)

# Calculate the length of side C using the law of sines
    length_of_C= math.sin(math.radians(Third_angle))*length/math.sin(math.radians(first_angle))

    return Third_angle,length_of_C

while True:
    try:

        first_angle=float(input("Input the value of angle Alpha: \n "))
        second_angle= float(input("Input the value of angle Betha: \n "))
        length= int(input("Input the length of side A of the triangle : \n"))

        if first_angle>=0 and second_angle>=0 and length>=0:
            if first_angle + second_angle < 180:  # Ensure the sum of angles is less than 180°
                Outcome=findC(first_angle,second_angle,length)
                print(f"The Value of  your third angle(𝜸) is {Outcome[0]} and the length of side A is {Outcome[1].__round__(2)}")
                
                break
            else:
                print("Error: The sum of angles exceeds 180°.")
            
        else:
            print(" Error:Make sure the values of your angles and length is greater than 0")
    except ValueError:
         print("Error: Please enter valid numeric values for angles and length.")
