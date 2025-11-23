import io
import sys
from contextlib import redirect_stdout


def naive_sort_desc_Timesort(serial_numbers):
    if not serial_numbers:
        return []
    return sorted(serial_numbers, reverse=True)


def main():
    nb_pieces_received = int(input())
    serial_numbers = list(map(int, input().split()))

    sorted_serials = naive_sort_desc_Timesort(serial_numbers)

    print(" ".join(map(str, sorted_serials)))



