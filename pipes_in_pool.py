pool_volume = int(input())
p1_flow_rate = int(input())
p2_flow_rate = int(input())
hours = float(input())

p1_volume = p1_flow_rate * hours
p2_volume = p2_flow_rate * hours

p1_p2_volume = p1_volume + p2_volume
p1_volume_percent = p1_volume / p1_p2_volume * 100
p2_volume_percent = p2_volume / p1_p2_volume * 100

if p1_p2_volume <= pool_volume:
    full_in_percents = p1_p2_volume / pool_volume * 100
    print(f"The pool is {full_in_percents:.2f}% full. Pipe 1: {p1_volume_percent:.2f}%. Pipe 2: \
{p2_volume_percent:.2f}%.")
else:
    difference = p1_p2_volume - pool_volume
    print(f"For {hours} hours the pool overflows with {difference:.2f} liters.")
