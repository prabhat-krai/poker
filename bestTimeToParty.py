"""
A list of celebrities are arriving and we have their in and out times. 
You are allowed to party for an hour.
What time should you go to party?
"""

n = int(input("Number of celebrities : "))

timing = []
for i in range(n):
    print("Enter time for celebrity number ", i+1)
    in_time = int(input("In time : "))
    out_time = int(input("Out time : "))
    timing.append([in_time, out_time])

