

# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 
#Question 1(i)
def temperature_classifier():
    temperature = float(input("Enter the temperature value in °C: "))
    if temperature < 0:
        print("Freezing")

    elif 0 <= temperature <= 10:
        print("Cold")

    elif 11<= temperature <= 20:
        print("Moderate")

    elif 21<= temperature <=30:
        print("Warm")
    
    else:
        print("Hot")

# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place 
# def volume_of_a_sphere():
#     r = int(input("Enter the radius of the sphere: ")) 
#     import math
#     pie = math.pi
#     volume = (4/3)*pie*r**2
#     print(f"The volume of the {r} and {pie} is: {volume}") 



  