def naive_sort_desc(serial_numbers):
    if not serial_numbers:
        return []

    # Simply sort in descending order
    return sorted(serial_numbers, reverse=True)


def main():
    nb_pieces_received = int(input())
    serial_numbers = list(map(int, input().split()))

    sorted_serials = naive_sort_desc(serial_numbers)

    # convert list to string with spaces
    str_sorted_serials = ' '.join(map(str, sorted_serials))
    print(str_sorted_serials)


if __name__ == "__main__":
    main()