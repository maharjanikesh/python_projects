def tribonacci_sequence(start_sequence, length):

    # If length is smaller, just slice
    if length <= len(start_sequence):
        return start_sequence[:length]

    while len(start_sequence) < length:
        next_val = sum(start_sequence[-3:])
        start_sequence.append(next_val)

    return start_sequence 


print(tribonacci_sequence([0, 0, 1], 10))