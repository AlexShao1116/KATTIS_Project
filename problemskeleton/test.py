#!/usr/bin/env python3
import sys
from pathlib import Path


def counting_sort(nums):
    """Stable counting sort for non-negative integers."""
    if not nums:
        return []

    max_val = max(nums)
    n = len(nums)

    count = [0] * (max_val + 1)
    for x in nums:
        count[x] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * n
    for i in range(n - 1, -1, -1):
        x = nums[i]
        count[x] -= 1
        output[count[x]] = x

    return output


def solve_from_lines(lines):
    """
    Parse an .in file that has format:

        N D
        id_1
        id_2
        ...
        id_N

    IDs may contain leading zeros, but we interpret them as integers.
    """
    tokens = []
    for line in lines:
        tokens.extend(line.strip().split())

    if not tokens:
        return []

    N = int(tokens[0])
    D = int(tokens[1])  # we do not actually need D here
    id_strs = tokens[2:2 + N]

    # Interpret IDs as integers, ignoring leading zeros
    ids = [int(s) for s in id_strs]

    return counting_sort(ids)


def check_one(in_path: Path, ans_path: Path) -> bool:
    """Return True if .in and .ans are consistent with the counting-sort solution."""
    # Read input
    with in_path.open("r", encoding="utf-8") as fin:
        in_lines = fin.readlines()
    expected = solve_from_lines(in_lines)

    # Read answer file: each line is a string ID (possibly with leading zeros)
    with ans_path.open("r", encoding="utf-8") as fans:
        ans_lines = [line.strip() for line in fans]

    # Convert .ans lines to integers
    try:
        ans_nums = [int(s) for s in ans_lines]
    except ValueError:
        # If answer file has invalid formatting (non-integer), treat as mismatch
        return False

    return expected == ans_nums


def main():
    root = Path(__file__).resolve().parent
    data_dir = root / "data"
    sample_dir = data_dir / "sample"
    secret_dir = data_dir / "secret"

    all_ok = True

    print("Checking sample tests...")
    if sample_dir.exists():
        for in_path in sorted(sample_dir.glob("*.in")):
            ans_path = in_path.with_suffix(".ans")
            if not ans_path.exists():
                print(f"  [MISSING] {ans_path.name}")
                all_ok = False
                continue
            ok = check_one(in_path, ans_path)
            print(f"  {in_path.name}: {'OK' if ok else 'MISMATCH'}")
            if not ok:
                all_ok = False
    else:
        print("  No sample/ directory found.")
        all_ok = False

    print("\nChecking secret tests...")
    if secret_dir.exists():
        for in_path in sorted(secret_dir.glob("*.in")):
            ans_path = in_path.with_suffix(".ans")
            if not ans_path.exists():
                print(f"  [MISSING] {ans_path.name}")
                all_ok = False
                continue
            ok = check_one(in_path, ans_path)
            print(f"  {in_path.name}: {'OK' if ok else 'MISMATCH'}")
            if not ok:
                all_ok = False
    else:
        print("  No secret/ directory found.")
        all_ok = False

    print()
    if all_ok:
        print("✅ All .in / .ans pairs are consistent (as integer-sorted counting sort).")
    else:
        print("❌ Some tests do NOT match the solution. See logs above.")


if __name__ == "__main__":
    main()
