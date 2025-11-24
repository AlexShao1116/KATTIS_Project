'''
WRONG ANSWER
NORMAL COUNT-SORT (ASCENDING ORDER)
EXPECTED DESCENDING ORDER
'''
def count_sort_inverse(serial_numbers):
    if not serial_numbers:
        return []

    n = len(serial_numbers)
    max_serial = max(serial_numbers)

    # freq of each
    freqArr = [0] * (max_serial + 1)

    # get freq of each element
    for serial in serial_numbers:
        freqArr[serial] += 1

    # compute sum
    for i in range(1, max_serial + 1):
        freqArr[i] += freqArr[i - 1]
        
    # build sorted array
    sorted_serials = [0] * n
    
    # iterate to backward
    for i in range(n - 1, -1, -1):
        serial = serial_numbers[i]
        sorted_serials[freqArr[serial] - 1] = serial
        freqArr[serial] -= 1

    return sorted_serials
    
def main():
    nb_pieces_received = int(input())
    list_serial_nb = list(map(int, input().split()))
    
    sorted_serial_nb_pieces = count_sort_inverse(list_serial_nb)
    str_sorted_serial_nb_pieces = ' '.join(map(str, sorted_serial_nb_pieces))
    print(str_sorted_serial_nb_pieces)
    

if __name__ == "__main__":
    main()
    
