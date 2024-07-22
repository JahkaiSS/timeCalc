def time_calculator(duration, time_commitment1, time_commitment2):
    total_time = []
    total_time.append(duration * time_commitment1) 
    total_time.append(duration * time_commitment2) 
    return total_time

print(time_calculator(12,16,24))