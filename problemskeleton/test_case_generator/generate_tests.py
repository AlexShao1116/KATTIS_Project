#!/usr/bin/env python3
import os
import random
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

# Fixed seed for reproducibility
RANDOM_SEED = 321

# Number of secret test cases to generate
# (Modify to 30 if your project requires 30)
NUM_SECRET_CASES = 20


# ============================================================
# Utility Functions
# ============================================================

def ensure_dir(p: Path):
    """Create a directory if it does not already exist."""
    p.mkdir(parents=True, exist_ok=True)


def rand_id(D: int, low: int = None, high: int = None) -> str:
    """
    Generate a D-digit numeric ID with leading zeros.
    The ID value is uniformly drawn from [low, high].
    """
    if low is None:
        low = 0
    if high is None:
        high = 10**D - 1
    v = random.randint(low, high)
    return f"{v:0{D}d}"


def write_case(base_path: Path, name: str, ids, D: int):
    """
    Write one pair of test files:
        base_path/name.in
        base_path/name.ans

    .in contains unsorted IDs.
    .ans contains IDs sorted by numeric value.
    """
    N = len(ids)
    in_path = base_path / f"{name}.in"
    ans_path = base_path / f"{name}.ans"

    # Write input file
    with in_path.open("w", encoding="utf-8") as f_in:
        f_in.write(f"{N} {D}\n")
        for s in ids:
            f_in.write(s + "\n")

    # Write answer file (sorted)
    sorted_ids = sorted(ids, key=lambda x: int(x))
    with ans_path.open("w", encoding="utf-8") as f_ans:
        for s in sorted_ids:
            f_ans.write(s + "\n")

    print(f"Generated: {in_path}  and  {ans_path}")


# ============================================================
# Sample Test Cases (Shown to participants)
# ============================================================

def generate_samples(sample_dir: Path):
    """
    Generate the 3 sample cases required by the problem statement.
    Includes one edge case with N = 1.
    """

    # Sample 1: Small case with duplicates and leading zeros
    D = 3
    ids = ["002", "100", "011", "010", "002"]
    write_case(sample_dir, "sample1", ids, D)

    # Sample 2: Reverse order with duplicate values
    D = 2
    ids = ["99", "50", "50", "20", "10", "01", "00"]
    write_case(sample_dir, "sample2", ids, D)

    # Sample 3: Edge case (N = 1)
    D = 5
    ids = ["00042"]
    write_case(sample_dir, "sample3", ids, D)


# ============================================================
# Secret Test Cases
# ============================================================

def generate_secret_cases(secret_dir: Path):
    """
    Generate 20 secret test cases with specific purposes:

    secret01–secret05: Edge cases
    secret06–secret10: Normal random cases
    secret11–secret15: Complicated random / structured
    secret16–secret20: Large inputs / potential TLE stress
    """

    # ------------- Edge cases -------------

    # secret01: Minimal N = 1, small D
    name = "secret01"
    D = 3
    ids = ["007"]
    write_case(secret_dir, name, ids, D)

    # secret02: Small N, all IDs identical
    name = "secret02"
    D = 2
    ids = ["42"] * 5
    write_case(secret_dir, name, ids, D)

    # secret03: Small N, all distinct and already sorted
    name = "secret03"
    D = 3
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ids = [f"{v:0{D}d}" for v in vals]
    write_case(secret_dir, name, ids, D)

    # secret04: Small N, strictly reverse sorted
    name = "secret04"
    D = 3
    vals = list(range(20, 10, -1))  # 20..11
    ids = [f"{v:0{D}d}" for v in vals]
    write_case(secret_dir, name, ids, D)

    # secret05: Two-value imbalance (many zeros, one large)
    name = "secret05"
    D = 4
    ids = ["0000"] * 14 + ["9999"]
    write_case(secret_dir, name, ids, D)

    # ------------- Normal random cases -------------

    # secret06: Medium N random 3-digit IDs
    name = "secret06"
    D = 3
    ids = [rand_id(D) for _ in range(100)]
    write_case(secret_dir, name, ids, D)

    # secret07: Medium N random 4-digit IDs
    name = "secret07"
    D = 4
    ids = [rand_id(D) for _ in range(150)]
    write_case(secret_dir, name, ids, D)

    # secret08: Medium N random 5-digit IDs
    name = "secret08"
    D = 5
    ids = [rand_id(D) for _ in range(120)]
    write_case(secret_dir, name, ids, D)

    # secret09: Random digits (D = 1)
    name = "secret09"
    D = 1
    ids = [str(random.randint(0, 9)) for _ in range(50)]
    write_case(secret_dir, name, ids, D)

    # secret10: Random 3-digit, dense small numeric range 0..50
    name = "secret10"
    D = 3
    ids = [rand_id(D, 0, 50) for _ in range(150)]
    write_case(secret_dir, name, ids, D)

    # ------------- Complicated random / structured -------------

    # secret11: Almost sorted 4-digit IDs, with a few random swaps
    name = "secret11"
    D = 4
    N = 200
    vals = sorted(random.randint(0, 9999) for _ in range(N))
    ids = [f"{v:0{D}d}" for v in vals]
    # Perform a few random swaps to slightly disturb the order
    for _ in range(15):
        i = random.randrange(N)
        j = random.randrange(N)
        ids[i], ids[j] = ids[j], ids[i]
    write_case(secret_dir, name, ids, D)

    # secret12: Three clusters (low, mid, high) in 5 digits
    name = "secret12"
    D = 5
    ids = []
    # low cluster: 0..500
    ids += [rand_id(D, 0, 500) for _ in range(80)]
    # mid cluster: 20000..21000
    ids += [rand_id(D, 20000, 21000) for _ in range(70)]
    # high cluster: 90000..99999
    ids += [rand_id(D, 90000, 99999) for _ in range(70)]
    random.shuffle(ids)
    write_case(secret_dir, name, ids, D)

    # secret13: Alternating extremes (very small vs very large)
    name = "secret13"
    D = 5
    ids = []
    for _ in range(110):
        ids.append(rand_id(D, 0, 100))
        ids.append(rand_id(D, 90000, 99999))
    ids = ids[:200]  # ensure N = 200
    random.shuffle(ids)
    write_case(secret_dir, name, ids, D)

    # secret14: Repeating short pattern (many duplicates of a few values)
    name = "secret14"
    D = 3
    pattern = ["000", "001", "010", "011", "100"]
    ids = [random.choice(pattern) for _ in range(200)]
    write_case(secret_dir, name, ids, D)

    # secret15: Many duplicates near boundaries with leading zeros
    name = "secret15"
    D = 6
    ids = []
    # near 0 (e.g., 000000..000100)
    ids += [rand_id(D, 0, 100) for _ in range(60)]
    # near upper bound (e.g., 999900..999999)
    ids += [rand_id(D, 999900, 999999) for _ in range(60)]
    # some mid values
    ids += [rand_id(D, 500000, 500100) for _ in range(60)]
    random.shuffle(ids)
    write_case(secret_dir, name, ids, D)

    # ------------- Large / TLE-style cases -------------

    # Note: N are chosen to be reasonably large but still safe
    # for the assignment's total input size < 500 KB.

    # secret16: Large N random 3-digit IDs
    name = "secret16"
    D = 3
    N = 2000
    ids = [rand_id(D) for _ in range(N)]
    write_case(secret_dir, name, ids, D)

    # secret17: Large N 3-digit IDs, dense small range (0..50) with many duplicates
    name = "secret17"
    D = 3
    N = 2000
    ids = [rand_id(D, 0, 50) for _ in range(N)]
    write_case(secret_dir, name, ids, D)

    # secret18: Large N 4-digit IDs, already sorted (best-case)
    name = "secret18"
    D = 4
    N = 3000
    vals = sorted(random.randint(0, 9999) for _ in range(N))
    ids = [f"{v:0{D}d}" for v in vals]
    write_case(secret_dir, name, ids, D)

    # secret19: Large N 4-digit IDs, strictly descending (worst-case ordering)
    name = "secret19"
    D = 4
    N = 3000
    vals = sorted((random.randint(0,9999) for _ in range(N)), reverse=True)
    ids = [f"{v:0{D}d}" for v in vals]
    write_case(secret_dir, name, ids, D)

    # secret20: Large N 6-digit IDs, half very small, half very large
    name = "secret20"
    D = 6
    N = 4000
    ids = []
    # very small 0..1000
    ids += [rand_id(D, 0, 1000) for _ in range(N // 2)]
    # very large 900000..999999
    ids += [rand_id(D, 900000, 999999) for _ in range(N - N // 2)]
    random.shuffle(ids)
    write_case(secret_dir, name, ids, D)


# ============================================================
# Main Entry Point
# ============================================================

def main():
    random.seed(RANDOM_SEED)

    # The script is located in: test case generator/
    # The problem root directory is one level above
    root = Path(__file__).resolve().parents[1]

    data_dir = root / "data"
    sample_dir = data_dir / "sample"
    secret_dir = data_dir / "secret"

    ensure_dir(sample_dir)
    ensure_dir(secret_dir)

    print(f"Root directory:   {root}")
    print(f"Sample directory: {sample_dir}")
    print(f"Secret directory: {secret_dir}\n")

    generate_samples(sample_dir)
    generate_secret_cases(secret_dir)

    print("\nAll tests generated successfully.")


if __name__ == "__main__":
    main()
