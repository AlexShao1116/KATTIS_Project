def naive_sort_desc_quadratic(serial_numbers):
    serial_numbers_copy = serial_numbers[:]
    n = len(serial_numbers_copy)
    
    for i in range(n):
        # find max in remaining array
        max_idx = i
        for j in range(i+1, n):
            if serial_numbers_copy[j] > serial_numbers_copy[max_idx]:
                max_idx = j
        # swap
        serial_numbers_copy[i], serial_numbers_copy[max_idx] = serial_numbers_copy[max_idx], serial_numbers_copy[i]
    
    return serial_numbers_copy


def main():
    nb_pieces_received = int(input())
    serial_numbers = list(map(int, input().split()))

    sorted_serials =  naive_sort_desc_quadratic(serial_numbers)

    # convert list to str with spaces
    str_sorted_serials = ' '.join(map(str, sorted_serials))
    print(str_sorted_serials)


if __name__ == "__main__":
    main()