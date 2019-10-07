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

def convert_into_start_and_leave_timings(timing):
    all_timing = []
    for i in range(len(timing)):
        all_timing.append([timing[i][0], 'enter'])
        all_timing.append([timing[i][1], 'exit'])
    return all_timing

get_timings = convert_into_start_and_leave_timings(timing)
get_timings.sort()

def find_best_time(get_timings):
    best_time = [float('-inf'),-1]
    curr_time = 0
    for i in range(len(get_timings)):
        if(get_timings[i][1] == 'enter'):
            curr_time +=1
        else:
            curr_time -=1
        if(curr_time > best_time[0]):
            best_time[0] = curr_time
            best_time[1] = get_timings[i][0]
    print("Time is {} and number of celebrities will be {}".format(best_time[1], best_time[0]))

find_best_time(get_timings)
        




