#!/usr/bin/env python3
import random
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

# Fixed seed for reproducibility
RANDOM_SEED = 321

# Serial numbers must be in [0, 10000]
MAX_VAL = 10000

# Sizes for big stress tests (secret16–secret20)
# You can tune these depending on your judge's speed.
N_LARGE_16 = 200_000
N_LARGE_17 = 400_000
N_LARGE_18 = 600_000
N_LARGE_19 = 800_000
N_LARGE_20 = 1_000_000


# ============================================================
# Utility Functions
# ============================================================

def ensure_dir(p: Path):
    """Create a directory if it does not already exist."""
    p.mkdir(parents=True, exist_ok=True)


def rand_serial(low=0, high=MAX_VAL):
    """Return a random integer serial number in [low, high]."""
    return random.randint(low, high)


def write_case(base_path: Path, name: str, nums):
    """
    Write one pair of test files:
        base_path/name.in
        base_path/name.ans

    .in format (from Parts in Perfect Order):
        n
        p1 p2 ... pn

    .ans:
        same numbers sorted in descending order, space-separated.
    """
    N = len(nums)
    in_path = base_path / f"{name}.in"
    ans_path = base_path / f"{name}.ans"

    # Input file
    with in_path.open("w", encoding="utf-8") as f_in:
        f_in.write(f"{N}\n")                          # first line: n
        f_in.write(" ".join(map(str, nums)) + "\n")   # second line: n integers

    # Answer file
    sorted_desc = sorted(nums, reverse=True)
    with ans_path.open("w", encoding="utf-8") as f_ans:
        f_ans.write(" ".join(map(str, sorted_desc)) + "\n")

    print(f"Generated: {in_path}  and  {ans_path}")


# ============================================================
# Sample Test Cases (from problem statement)
# ============================================================

def generate_samples(sample_dir: Path):
    """Generate the 3 sample cases given in the PDF."""

    # Sample 1
    nums = [120, 870, 120, 999, 0, 870, 540, 999]
    write_case(sample_dir, "sample1", nums)

    # Sample 2
    nums = [42, 9000, 123, 500, 9000]
    write_case(sample_dir, "sample2", nums)

    # Sample 3
    nums = [5000]
    write_case(sample_dir, "sample3", nums)


# ============================================================
# Secret Test Cases (secret01–secret20)
# ============================================================

def generate_secret_cases(secret_dir: Path):
    """
    secret01–secret15: edge / medium / structured
    secret16–secret20: HUGE tests with very small value range (0..10)
    """
    # ---------- small & medium (same as before) ----------
    write_case(secret_dir, "secret01", [7])
    write_case(secret_dir, "secret02", [42] * 5)
    write_case(secret_dir, "secret03", list(range(10)))
    write_case(secret_dir, "secret04", list(range(20, 10, -1)))
    write_case(secret_dir, "secret05", [0] * 14 + [9999])

    write_case(secret_dir, "secret06", [rand_serial() for _ in range(100)])
    write_case(secret_dir, "secret07", [rand_serial() for _ in range(150)])
    write_case(secret_dir, "secret08", [rand_serial() for _ in range(120)])
    write_case(secret_dir, "secret09", [rand_serial(0, 9) for _ in range(50)])
    write_case(secret_dir, "secret10", [rand_serial(0, 50) for _ in range(150)])

    nums = sorted(rand_serial() for _ in range(200))
    for _ in range(15):
        i = random.randrange(200); j = random.randrange(200)
        nums[i], nums[j] = nums[j], nums[i]
    write_case(secret_dir, "secret11", nums)

    nums = []
    nums += [rand_serial(0, 500) for _ in range(80)]
    nums += [rand_serial(2000, 2500) for _ in range(70)]
    nums += [rand_serial(9000, 10000) for _ in range(70)]
    random.shuffle(nums)
    write_case(secret_dir, "secret12", nums)

    nums = []
    for _ in range(110):
        nums.append(rand_serial(0, 100))
        nums.append(rand_serial(9900, 10000))
    random.shuffle(nums)
    write_case(secret_dir, "secret13", nums)

    pattern = [0, 1, 10, 11, 100]
    write_case(secret_dir, "secret14", [random.choice(pattern) for _ in range(200)])

    nums = []
    nums += [rand_serial(0, 100) for _ in range(60)]
    nums += [rand_serial(9900, 10000) for _ in range(60)]
    nums += [rand_serial(4500, 4600) for _ in range(60)]
    random.shuffle(nums)
    write_case(secret_dir, "secret15", nums)

    # ---------- HUGE tests with small value range (0..10) ----------

    BIG_N = 1_000_000  # max n from problem

    # secret16: all random in [0, 10]
    nums = [rand_serial(0, 10) for _ in range(BIG_N)]
    write_case(secret_dir, "secret16", nums)

    # secret17: random in [0, 10], but with a heavy bias to one value
    nums = []
    for _ in range(BIG_N):
        if random.random() < 0.8:
            nums.append(5)   # dominant value
        else:
            nums.append(rand_serial(0, 10))
    write_case(secret_dir, "secret17", nums)

    # secret18: alternating low/high in [0, 10]
    nums = []
    for i in range(BIG_N):
        if i % 2 == 0:
            nums.append(rand_serial(0, 3))
        else:
            nums.append(rand_serial(7, 10))
    write_case(secret_dir, "secret18", nums)

    # secret19: long runs of same numbers in [0, 10]
    nums = []
    block_vals = [0, 3, 7, 10]
    block_size = 5000
    while len(nums) < BIG_N:
        v = random.choice(block_vals)
        nums.extend([v] * block_size)
    nums = nums[:BIG_N]
    random.shuffle(nums)  # optional: remove if you want obvious runs
    write_case(secret_dir, "secret19", nums)

    # secret20: mixture: half zeros, half random [0, 10]
    nums = [0] * (BIG_N // 2) + [rand_serial(0, 10) for _ in range(BIG_N - BIG_N // 2)]
    random.shuffle(nums)
    write_case(secret_dir, "secret20", nums)

# ============================================================
# Main Entry Point
# ============================================================

def main():
    random.seed(RANDOM_SEED)

    # Script is assumed to live in "test case generator/".
    # Problem root directory is one level above.
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

