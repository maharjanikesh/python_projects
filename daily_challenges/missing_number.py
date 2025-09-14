def find_missing_numbers(arr):
    remaining_num = []
    highest_num = 0
    lowest_num = 1

    # Finding highest number among the array of numbers
    for num in arr:
        if num > highest_num: 
            highest_num = num

    # Appending the numbers not in a given array
    for num in range(lowest_num, highest_num+1):
        if num not in arr:
            remaining_num.append(num)

    if remaining_num:
        return remaining_num
    else:
        return []

print(find_missing_numbers([1, 3, 5]))