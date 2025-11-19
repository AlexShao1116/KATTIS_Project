def count_sort_inverse(serial_numbers):
    if not serial_numbers:
        return []

    n = len(serial_numbers)
    max_serial = max(serial_numbers)

    countArr = [0] * (max_serial + 1)

    for serial in serial_numbers:
        countArr[serial] += 1

    for i in range(max_serial - 1, -1, -1):
        countArr[i] += countArr[i + 1]

    sorted_serials = [0] * n
    
    #BECAREFUL FOR RANGE
    for i in range(n, -1, -1):
        serial = serial_numbers[i]
        sorted_serials[countArr[serial] - 1] = serial
        countArr[serial] -= 1

    return sorted_serials
    
def main():
    nb_pieces_received = int(input())
    list_serial_nb = list(map(int, input().split()))
    
    sorted_serial_nb_pieces = count_sort_inverse(list_serial_nb)
    str_sorted_serial_nb_pieces = ' '.join(map(str, sorted_serial_nb_pieces))
    print(str_sorted_serial_nb_pieces)
    

if __name__ == "__main__":
    main()