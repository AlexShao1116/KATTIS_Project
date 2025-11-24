import subprocess
import os

# Folder containing the secret inputs and answers
input_folder = "../../data/secret/"

# Java class (must match your public class name)
java_class = "solution_correct"
java_file = f"{java_class}.java"

# Compile the Java file first
print(f"Compiling {java_file}...")
try:
    subprocess.check_call(f"javac {java_file}", shell=True)
    print("Compilation successful!\n")
except subprocess.CalledProcessError:
    print("Compilation failed. Check your Java code.")
    exit(1)

# Test each input file
for file in os.listdir(input_folder):
    if file.endswith(".in"):
        testname = file[:-3]  # remove .in
        ansfile = os.path.join(input_folder, f"{testname}.ans")
        infile = os.path.join(input_folder, file)

        try:
            # Run the Java program
            result = subprocess.check_output(
                f"java {java_class} < {infile}",
                shell=True,
                text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Testing {testname}... RUNTIME ERROR")
            print(e.output)
            continue

        with open(ansfile, "r", encoding="utf-8") as f:
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
