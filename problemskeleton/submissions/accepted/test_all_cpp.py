import subprocess
import os

input_folder = "../../data/secret/"
exe_name = "solution_correct.exe"   # No './' on Windows!

for file in os.listdir(input_folder):
    if file.endswith(".in"):
        testname = file[:-3]     # remove .in
        ansfile = f"{input_folder}{testname}.ans"
        infile = f"{input_folder}{file}"

        try:
            # Run the C++ program
            result = subprocess.check_output(
                f"{exe_name} < {infile}",
                shell=True, text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Testing {testname}... CRASH")
            print("Program returned non-zero exit code.")
            print("Error output:")
            print(e.output)
            continue

        # Load expected output
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

