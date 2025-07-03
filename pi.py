""" Summary:
Description:
    Calculating an approximate value of pi, with accuracy depending on the number of steps
    Uses Liu Hui's algorithm from around 3rd century, kind of
    Gives only 15 digits after the dot
    Step_amount of 15000 already gives a good value and 20000 gives the exact numbers for the visible digits
"""
import math
import time

print("\nInsert a number of steps (more is more accurate):")
step_amount: int = int(input("> "))
print()
start_time = time.time()
n: int = 3

for i in range(step_amount):
    n += i
    pi_lower_bound: float = n * math.sin(math.radians(180/n))
    pi_upper_bound: float = n * math.tan(math.radians(180/n))
    # uncomment print to show the values getting closer to PI
    # print(f"{pi_lower_bound} < π < {pi_upper_bound}")

print(f"--- {(time.time() - start_time)} seconds ---")
print(f"\n{pi_lower_bound} < π < {pi_upper_bound}\n")
