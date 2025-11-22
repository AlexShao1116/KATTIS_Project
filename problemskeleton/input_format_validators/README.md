# DELIVERABLE 7
## What challenges did you encounter while creating the validators?
The main challenges I faced were ensuring that integers did not have leading zeros (except for 0) and verifying that the number on the first line (n) correctly matched the number of serial numbers provided on second line.

## How did you ensure the correctness and completeness of your validators?

To ensure the validators were correct and complete, I tested various edge cases with input.in:

Inputs where the first line n was outside the valid range.

Cases where n did not match the number of serial numbers on the second line (e.g., n = 1 but eight serial numbers given).

I verified that assertions correctly detected these errors in all cases.



## How do your validators handle edge cases and malformed inputs?
The validators handle edge cases and malformed inputs by:

Checking that n satisfies valid range: 1 ≤ n ≤ 1,000,000.

Ensure integers are correctly formatted with no leading zeros (except for 0).

Verifying that each serial number is within the allowed range: 0 ≤ number ≤ 10,000.

Confirming that the number of serial numbers matches n (len(numbers) == n).

Detecting extra lines beyond the expected input.

Using regular expressions to ensure all values are valid integers.