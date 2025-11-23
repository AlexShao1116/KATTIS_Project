import subprocess
import os

input_folder = "../../data/secret/"
for file in os.listdir(input_folder):
    if file.endswith(".in"):
        testname = file[:-3]     # remove .in
        ansfile = f"{input_folder}{testname}.ans"
        infile = f"{input_folder}{file}"

        result = subprocess.check_output(
            f"python solution_correct.py < {infile}",
            shell=True, text=True
        )

        with open(ansfile) as f:
            expected = f.read()

        print(f"Testing {testname}... ", end="")
        if result.strip() == expected.strip():
            print("OK")
        else:
            print("FAIL")
            print("Your output:")
            print(result)
            print("Expected:")
            print(expected)
