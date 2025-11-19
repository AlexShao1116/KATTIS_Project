#!/usr/bin/env python3
import os
import random

OUTPUT_DIR = "."     # folder where inputXX.txt / outputXX.txt will be written
MAX_N = 10**6
MAX_GRADE = 100
TOTAL_CASES = 20     # total number of test cases


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def counting_sort_desc(grades):
    """
    Generate the correct sorted grades using counting only.
    (No comparison-based sort: no sorted(), no .sort(), etc.)
    """
    freq = [0] * (MAX_GRADE + 1)
    for g in grades:
        freq[g] += 1

    result = []
    for g in range(MAX_GRADE, -1, -1):
        if freq[g] > 0:
            result.extend([g] * freq[g])
    return result


def write_case(case_id, grades):
    """
    Writes inputXX.txt and outputXX.txt for one test case.
    This is what you'll also use as your ‘write cases’:
    - some are edge cases
    - maybe 2 standard cases
    """
    n = len(grades)
    input_path = os.path.join(OUTPUT_DIR, f"input{case_id:02d}.txt")
    output_path = os.path.join(OUTPUT_DIR, f"output{case_id:02d}.txt")

    # input
    with open(input_path, "w") as fi:
        fi.write(str(n) + "\n")
        fi.write(" ".join(map(str, grades)) + "\n")

    # output via counting sort (non-comparison)
    sorted_grades = counting_sort_desc(grades)
    with open(output_path, "w") as fo:
        fo.write(" ".join(map(str, sorted_grades)) + "\n")


# ---------------------- Hand-crafted + standard cases ---------------------- #

def build_handcrafted_cases():
    """
    These are your ‘write cases’: edge cases + a couple of standard cases.
    We’ll use the first few case IDs for these.
    """

    cases = []

    # Standard Case 1: exactly the sample from the statement
    cases.append([
        75, 100, 88, 75, 60, 100, 90
    ])

    # Standard Case 2: another typical mix of grades
    cases.append([
        0, 50, 100, 100, 33, 67, 85, 85, 92, 10
    ])

    # Edge 1: Single student, grade 0
    cases.append([0])

    # Edge 2: Single student, grade 100
    cases.append([100])

    # Edge 3: All zeros
    cases.append([0] * 100)

    # Edge 4: All hundreds
    cases.append([100] * 100)

    # Edge 5: Alternating 0 and 100
    n = 200
    alt = []
    for i in range(n):
        alt.append(0 if i % 2 == 0 else 100)
    cases.append(alt)

    # Edge 6: Already descending
    cases.append([100, 99, 90, 80, 75, 60, 42, 0])

    # Edge 7: Already ascending
    cases.append([0, 5, 10, 20, 50, 75, 90, 100])

    # Edge 8: Many copies of a middle grade
    cases.append([50] * 123)

    # Edge 9: Very skewed – mostly 100, a few small grades
    skew = [100] * 1000 + [0] * 10 + [1] * 10 + [2] * 10
    cases.append(skew)

    return cases  # currently 11 cases (2 standard + 9 other edges)


# ----------------------------- Random cases ----------------------------- #

def random_case(n):
    return [random.randint(0, MAX_GRADE) for _ in range(n)]


def main():
    random.seed(2025)  # fixed seed for reproducibility
    ensure_dir(OUTPUT_DIR)

    case_id = 1
    handcrafted = build_handcrafted_cases()

    # 1) Write all handcrafted (edge + 2 standard) cases
    for grades in handcrafted:
        write_case(case_id, grades)
        case_id += 1

    # 2) Fill up to TOTAL_CASES with random cases
    # Remaining number of random test files:
    remaining = TOTAL_CASES - len(handcrafted)
    # If your handcrafted > TOTAL_CASES, you can reduce them or raise TOTAL_CASES.

    for i in range(remaining):
        # Design the random sizes to stress runtime / force counting sort
        if i < 4:
            # small random (sanity checks)
            n = random.randint(1, 200)
        elif i < 8:
            # medium random
            n = random.randint(10_000, 100_000)
        else:
            # large / near-worst-case random
            n = random.randint(500_000, MAX_N)

        grades = random_case(n)
        write_case(case_id, grades)
        case_id += 1

    print(f"Generated {TOTAL_CASES} test cases "
          f"({len(handcrafted)} handcrafted + {remaining} random).")


if __name__ == "__main__":
    main()
