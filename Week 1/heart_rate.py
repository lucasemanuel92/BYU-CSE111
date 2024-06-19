"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# The program needs to ask for age and shows the minimun and max to strength the heart
first_info = input("Please, insert your age: ")

age = int(first_info)

beat_range = 220 - age

max_range = beat_range * 0.85
min_range = beat_range * 0.65

print(f"Your age is {age}.")
print(f"When exercise to strengthen your heart, you should keep your heart rate between {min_range:.0f} and {max_range:.0f} beats per minute.")
