import io
import sys
from contextlib import redirect_stdout

# ---------------------------------------------------------
# Your ORIGINAL solution functions stay the same. DO NOT modify!
# ---------------------------------------------------------

def naive_sort_desc_Timesort(serial_numbers):
    if not serial_numbers:
        return []
    return sorted(serial_numbers, reverse=True)


def main():
    nb_pieces_received = int(input())
    serial_numbers = list(map(int, input().split()))

    sorted_serials = naive_sort_desc_Timesort(serial_numbers)

    print(" ".join(map(str, sorted_serials)))


# ---------------------------------------------------------
# Testing utilities
# ---------------------------------------------------------

def run_program_with_input(text: str) -> str:
    """
    Run your existing main() using `text` as stdin.
    Capture stdout exactly as if running on Kattis.
    """
    old_stdin = sys.stdin
    old_stdout = sys.stdout

    sys.stdin = io.StringIO(text)
    buffer = io.StringIO()

    try:
        with redirect_stdout(buffer):
            main()  # run your actual solution
    finally:
        sys.stdin = old_stdin
        sys.stdout = old_stdout

    return buffer.getvalue().strip()


def run_test(in_file: str, out_file: str):
    """
    Read input/output files and compare with your program's output.
    """
    with open(in_file, "r") as f:
        input_text = f.read()

    with open(out_file, "r") as f:
        expected_output = f.read().strip()

    actual_output = run_program_with_input(input_text)

    print("===== Test Result =====")
    print(f"Input file:     {in_file}")
    print(f"Expected file:  {out_file}")
    print("------------------------")
    print("Expected:", expected_output)
    print("Actual:   ", actual_output)
    print("------------------------")

    if expected_output == actual_output:
        print("✅ PASS — output matches expected.")
    else:
        print("❌ FAIL — output does NOT match.")


# ---------------------------------------------------------
# Run a specific test file
# ---------------------------------------------------------

if __name__ == "__main__":
    # If you run from the project root use this:
    # run_test("data/secret/secret01.in", "data/secret/secret01.ans")

    # If you run from inside data/secret:
    run_test("secret19.in", "secret19.ans")
