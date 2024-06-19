# Emter the width, aspect ratio and diameter and calculate the appropriate volume of the tire
# Import necessary libraries
import math
# Enter Information
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enther the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the  wheel in inches (ex 15): "))

# Making the calculus
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")