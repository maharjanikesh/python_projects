def speeding(speeds, limit):
    speed_sum = 0
    average_count = 0


    for speed in speeds:
        if speed > limit:
            speed_sum += speed-limit
            average_count += 1 
    if speed_sum == 0:
        return [0, 0]
    else:
        average_speed = speed_sum /average_count

        return [average_count, average_speed]

print(speeding([100, 105, 95, 102], 100))