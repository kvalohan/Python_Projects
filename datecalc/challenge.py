import time

time_name1 = "monotonic"
time_name2 = "time"
time_name3 = "process_time"
time_name4 = "perf_counter"

print(f'The info for {time_name1} are\n\t{time.get_clock_info(time_name1)}')
print(f'The info for {time_name2} are\n\t{time.get_clock_info(time_name2)}')
print(f'The info for {time_name3} are\n\t{time.get_clock_info(time_name3)}')
print(f'The info for {time_name4} are\n\t{time.get_clock_info(time_name4)}')